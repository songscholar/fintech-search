from __future__ import annotations

import json
import sqlite3
from types import SimpleNamespace
from pathlib import Path

from uses_indexer.embeddings import EmbeddingInfo, EmbeddingRequestError
from uses_indexer.indexer import SQLiteIndexer


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <histories modifiedDate="2026-04-09 10:00:00" version="V1" orderNumber="T1" modifiedBy="Tester" modified="新增"/>
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [AF_DEEP][][deep_flag = @deep_flag]
  [事务处理开始]
  [通用SQL执行][select * from uses_fund_real where fund_account = @fund_account][count = @sql_row_count]
  [事务处理结束]
  [获取记录][uses_fund_real(idx_x)][fund_account = @fund_account]
  [处理失败]
  {
    [EXCEPTION]
    [WHEN_OTHERS]
    {
      [业务报错返回][ERR_FUND_QRY_FUNDREAL_FAIL][查询交易资金表失败]
    }
  }
  goto svr_end;
  <svr_end>:
  @row_count = 1;
  ]]></code>
</business:Function>
"""

CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_入口" objectId="2">
  <inputParameters id="fund_account" uuid="u3"/>
  <outputParameters id="row_count" uuid="u4"/>
  <code><![CDATA[
  [AF_SAMPLE][][row_count = @row_count]
  [获取字段][uses_fund_real(idx_x)][fund_account = @fund_account]
  ]]></code>
</business:Service>
"""

DEEP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_深层" objectId="3">
  <inputParameters id="fund_account" uuid="u5"/>
  <outputParameters id="deep_flag" uuid="u6"/>
  <code><![CDATA[
  [获取记录][uses_deep_table(idx_x)][fund_account = @fund_account]
  [通用SQL执行][update uses_deep_table set deep_flag = 1 where fund_account = @fund_account][]
  @table_name = "uses_dynamic_table";
  sprintf(@sql_str, "delete from %s where fund_account = %s", @table_name, @fund_account);
  [通用SQL执行][@sql_str][]
  @deep_flag = 1;
  ]]></code>
</business:Function>
"""

LS_LOCAL_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_本地调用方" objectId="11">
  <code><![CDATA[
  [AF_LOCAL][][]
  ]]></code>
</business:Service>
"""

LF_LOCAL_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_测试_本地调用方" objectId="12">
  <code><![CDATA[
  [LF_HELPER][][]
  ]]></code>
</business:Function>
"""

AF_LOCAL_TARGET_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_本地目标" objectId="13">
  <code><![CDATA[
  @result = 1;
  ]]></code>
</business:Function>
"""

LF_HELPER_TARGET_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_测试_LF目标" objectId="14">
  <code><![CDATA[
  @result = 1;
  ]]></code>
</business:Function>
"""

LS_RPC_TARGET_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_RPC目标" objectId="15">
  <code><![CDATA[
  @result = 1;
  ]]></code>
</business:Service>
"""

LS_RPC_CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_RPC调用方" objectId="16">
  <code><![CDATA[
  [LS_REMOTE][][]
  ]]></code>
</business:Service>
"""

LF_RPC_CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_测试_RPC调用方" objectId="17">
  <code><![CDATA[
  [LS_REMOTE][][]
  ]]></code>
</business:Function>
"""

AF_RPC_CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_RPC调用方" objectId="18">
  <code><![CDATA[
  [LS_REMOTE][][]
  ]]></code>
</business:Function>
"""


def _write_sample_sources(tmp_path: Path) -> Path:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")
    (source_dir / "AF_DEEP.uftatomfunction").write_text(DEEP_XML, encoding="utf-8")
    return source_dir


def _build_sample_index(tmp_path: Path) -> tuple[SQLiteIndexer, Path]:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return indexer, db_path


def _build_call_semantic_index(tmp_path: Path) -> tuple[SQLiteIndexer, Path]:
    source_dir = tmp_path / "semantic_src"
    source_dir.mkdir()
    (source_dir / "LS_LOCAL.uftservice").write_text(LS_LOCAL_XML, encoding="utf-8")
    (source_dir / "LF_LOCAL.uftfunction").write_text(LF_LOCAL_XML, encoding="utf-8")
    (source_dir / "AF_LOCAL.uftatomfunction").write_text(AF_LOCAL_TARGET_XML, encoding="utf-8")
    (source_dir / "LF_HELPER.uftfunction").write_text(LF_HELPER_TARGET_XML, encoding="utf-8")
    (source_dir / "LS_REMOTE.uftservice").write_text(LS_RPC_TARGET_XML, encoding="utf-8")
    (source_dir / "LS_RPC_CALLER.uftservice").write_text(LS_RPC_CALLER_XML, encoding="utf-8")
    (source_dir / "LF_RPC_CALLER.uftfunction").write_text(LF_RPC_CALLER_XML, encoding="utf-8")
    (source_dir / "AF_RPC_CALLER.uftatomfunction").write_text(AF_RPC_CALLER_XML, encoding="utf-8")
    db_path = tmp_path / "semantic_index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return indexer, db_path


class MismatchEmbedder:
    @property
    def info(self) -> EmbeddingInfo:
        return EmbeddingInfo(provider="openai-compatible", model="text-embedding-3-large", dimension=3072)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return [[0.1] * 3072 for _ in texts]


class FailingEmbedder:
    @property
    def info(self) -> EmbeddingInfo:
        return EmbeddingInfo(provider="local-hash", model="local-hash-256", dimension=256)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        raise EmbeddingRequestError("boom")


class RecordingBatchEmbedder:
    def __init__(self, batch_size: int = 1000, fail_after_batches: int | None = None, dimension: int = 2) -> None:
        self.config = SimpleNamespace(batch_size=batch_size)
        self.fail_after_batches = fail_after_batches
        self.dimension = dimension
        self.calls: list[list[str]] = []

    @property
    def info(self) -> EmbeddingInfo:
        return EmbeddingInfo(provider="recording", model="recording-v1", dimension=self.dimension)

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        self.calls.append(list(texts))
        if self.fail_after_batches is not None and len(self.calls) > self.fail_after_batches:
            raise EmbeddingRequestError("planned failure")
        return [[float(index + 1), float(len(text))] for index, text in enumerate(texts)]


def test_build_index_creates_sqlite_tables_and_fts(tmp_path: Path) -> None:
    _, db_path = _build_sample_index(tmp_path)

    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT COUNT(*) FROM files").fetchone()[0] == 3
    assert conn.execute("SELECT COUNT(*) FROM procedures").fetchone()[0] == 3
    assert conn.execute("SELECT COUNT(*) FROM params").fetchone()[0] == 6
    assert conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'calls_procedure'").fetchone()[0] == 3
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'reads_table'").fetchone()[0] >= 3
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'writes_table'").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM blocks").fetchone()[0] >= 3
    assert conn.execute("SELECT COUNT(*) FROM block_edges").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'jumps_to_label'").fetchone()[0] >= 1
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'defines_label'").fetchone()[0] >= 1
    assert conn.execute("SELECT COUNT(*) FROM procedures_fts").fetchone()[0] == 3
    assert conn.execute("SELECT COUNT(*) FROM statements_fts").fetchone()[0] >= 5
    assert conn.execute("SELECT COUNT(*) FROM actions_fts").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM edges_fts").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM blocks_fts").fetchone()[0] >= 3
    conn.close()


def test_build_index_populates_vectors_in_global_batches(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "index.db"
    embedder = RecordingBatchEmbedder(batch_size=1000)
    indexer = SQLiteIndexer(embedder=embedder)

    result = indexer.build_index(source_dir, db_path)

    conn = sqlite3.connect(db_path)
    chunk_count = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    vector_count = conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0]
    conn.close()

    assert chunk_count > 1
    assert vector_count == chunk_count
    assert len(embedder.calls) == 1
    assert len(embedder.calls[0]) == chunk_count
    assert result["vector_stats"]["batches"] == 1
    assert result["vector_stats"]["missing_after"] == 0


def test_build_index_commits_vector_batches_before_failure(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "index.db"
    embedder = RecordingBatchEmbedder(batch_size=1, fail_after_batches=1)
    indexer = SQLiteIndexer(embedder=embedder)

    try:
        indexer.build_index(source_dir, db_path)
    except EmbeddingRequestError as exc:
        assert "planned failure" in str(exc)
    else:
        raise AssertionError("Expected EmbeddingRequestError")

    conn = sqlite3.connect(db_path)
    chunk_count = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    vector_count = conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0]
    conn.close()

    assert chunk_count > 1
    assert vector_count == 1


def test_build_index_resume_vectors_skips_existing_vectors(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "index.db"
    SQLiteIndexer(embedder=RecordingBatchEmbedder(batch_size=1000)).build_index(source_dir, db_path)

    conn = sqlite3.connect(db_path)
    conn.execute("DELETE FROM chunk_vectors WHERE chunk_id = (SELECT MIN(chunk_id) FROM chunk_vectors)")
    conn.commit()
    chunk_count = conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
    conn.close()

    resume_embedder = RecordingBatchEmbedder(batch_size=1000)
    result = SQLiteIndexer(embedder=resume_embedder).build_index(source_dir, db_path, resume_vectors=True)

    conn = sqlite3.connect(db_path)
    vector_count = conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0]
    conn.close()

    assert vector_count == chunk_count
    assert len(resume_embedder.calls) == 1
    assert len(resume_embedder.calls[0]) == 1
    assert result["resume_vectors"] is True
    assert result["vector_stats"]["missing_before"] == 1
    assert result["vector_stats"]["missing_after"] == 0


def test_build_index_resume_vectors_preserves_known_db_dimension(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "index.db"
    SQLiteIndexer(embedder=RecordingBatchEmbedder(batch_size=1000, dimension=2)).build_index(source_dir, db_path)

    resume_embedder = RecordingBatchEmbedder(batch_size=1000, dimension=0)
    result = SQLiteIndexer(embedder=resume_embedder).build_index(source_dir, db_path, resume_vectors=True)

    conn = sqlite3.connect(db_path)
    dimension = conn.execute("SELECT value FROM metadata WHERE key = 'embedding_dimension'").fetchone()[0]
    conn.close()

    assert resume_embedder.calls == []
    assert result["vector_stats"]["missing_before"] == 0
    assert result["embedding"]["dimension"] == 2
    assert dimension == "2"


def test_query_index_uses_fts_and_rerank(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "证券代码获取", limit=10)
    assert result["hit_count"] >= 1
    assert result["fts_query"] is not None
    assert any(str(hit["retrieval_source"]).startswith("fts_") for hit in result["hits"])
    assert any(hit["hit_type"] == "chunk" for hit in result["hits"])
    assert any("token_overlap" in " ".join(hit["reasons"]) for hit in result["hits"])
    assert any("证券代码获取" in str(hit["matched_text"]) for hit in result["hits"])


def test_query_index_includes_vector_retrieval_for_related_query(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "证券信息获取", limit=10)

    assert result["hit_count"] >= 1
    assert any(hit["retrieval_source"] == "vector_chunk" for hit in result["hits"])


def test_query_index_includes_block_hits_for_failure_and_sql_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "查询交易资金表失败", limit=10)

    assert result["hit_count"] >= 1
    assert any(hit["hit_type"] == "block" for hit in result["hits"])


def test_call_semantics_are_classified_in_edges_and_summary(tmp_path: Path) -> None:
    indexer, db_path = _build_call_semantic_index(tmp_path)

    conn = sqlite3.connect(db_path)
    edge_rows = conn.execute(
        """
        SELECT source_name, target_name, detail_json
        FROM edges
        WHERE edge_type = 'calls_procedure'
        ORDER BY source_name, target_name
        """
    ).fetchall()
    conn.close()

    details = {
        (str(source_name), str(target_name)): json.loads(str(detail_json))
        for source_name, target_name, detail_json in edge_rows
    }

    assert details[("LS_LOCAL", "AF_LOCAL")]["call_kind"] == "local_function_call"
    assert details[("LS_LOCAL", "AF_LOCAL")]["call_rule"] == "LS->AF"
    assert details[("LF_LOCAL", "LF_HELPER")]["call_kind"] == "local_function_call"
    assert details[("LF_LOCAL", "LF_HELPER")]["call_rule"] == "LF->LF"
    assert details[("LS_RPC_CALLER", "LS_REMOTE")]["call_kind"] == "rpc_call"
    assert details[("LS_RPC_CALLER", "LS_REMOTE")]["call_rule"] == "LS->LS"
    assert details[("LF_RPC_CALLER", "LS_REMOTE")]["call_kind"] == "rpc_call"
    assert details[("LF_RPC_CALLER", "LS_REMOTE")]["call_rule"] == "LF->LS"
    assert details[("AF_RPC_CALLER", "LS_REMOTE")]["call_kind"] == "rpc_call"
    assert details[("AF_RPC_CALLER", "LS_REMOTE")]["call_rule"] == "AF->LS"

    summary = indexer.summarize_db(db_path)
    assert summary["call_kind_counts"]["local_function_call"] == 2
    assert summary["call_kind_counts"]["rpc_call"] == 3
    assert summary["call_rule_counts"]["LS->AF"] == 1
    assert summary["call_rule_counts"]["LF->LF"] == 1
    assert summary["call_rule_counts"]["LS->LS"] == 1
    assert summary["call_rule_counts"]["LF->LS"] == 1
    assert summary["call_rule_counts"]["AF->LS"] == 1


def test_related_context_exposes_call_semantics_labels(tmp_path: Path) -> None:
    indexer, db_path = _build_call_semantic_index(tmp_path)

    evidence = indexer.assemble_evidence(db_path, "LS_REMOTE 被谁调用", limit=3)
    llm_context = str(evidence["llm_context"])

    assert "系统间RPC调用 LS->LS" in llm_context
    assert "系统间RPC调用 LF->LS" in llm_context
    assert "系统间RPC调用 AF->LS" in llm_context


def test_query_index_includes_control_flow_hits_for_exit_labels(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "svr_end", limit=10)

    assert result["hit_count"] >= 1
    assert any(hit["match_source"] in {"block_summary", "label", "goto"} or hit["matched_text"] == "svr_end" for hit in result["hits"])


def test_query_index_extracts_sql_table_edges_and_multi_hop_bonus(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_deep_table", limit=10)

    assert result["hit_count"] >= 1
    assert any("call_chain_" in " ".join(hit["reasons"]) for hit in result["hits"])
    assert any("uses_deep_table" in str(hit["matched_text"]) or "uses_deep_table" in " ".join(hit["reasons"]) for hit in result["hits"])


def test_query_index_recovers_dynamic_sql_tables(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_dynamic_table", limit=10)

    assert result["hit_count"] >= 1
    assert any("uses_dynamic_table" in str(hit["matched_text"]) or "uses_dynamic_table" in " ".join(hit["reasons"]) for hit in result["hits"])


def test_query_index_applies_intent_aware_rerank(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    variable_result = indexer.query_index(db_path, "@deep_flag 在哪里赋值", limit=5)
    assert variable_result["hits"][0]["match_source"] == "assignment"
    assert "intent_assignment_statement" in variable_result["hits"][0]["reasons"]

    table_result = indexer.query_index(db_path, "uses_deep_table 在哪里更新", limit=5)
    assert table_result["hits"][0]["hit_type"] == "block"
    assert "intent_sql_block" in table_result["hits"][0]["reasons"]

    call_result = indexer.query_index(db_path, "AF_DEEP 被谁调用", limit=5)
    assert call_result["hits"][0]["procedure_name"] == "AF_SAMPLE"
    assert "intent_call_chain" in call_result["hits"][0]["reasons"]

    failure_result = indexer.query_index(db_path, "查询失败在哪里处理", limit=5)
    assert failure_result["hits"][0]["hit_type"] == "block"
    assert "intent_failure_block" in failure_result["hits"][0]["reasons"]


def test_query_index_keeps_exact_call_focus_above_vector_only_context(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "哪些流程调用证券代码获取", limit=6)

    assert result["hits"][0]["procedure_name"] == "AF_SAMPLE"
    assert "证券代码获取" in str(result["hits"][0]["matched_text"])
    assert "focus_match_in_hit=证券代码获取" in result["hits"][0]["reasons"]

    vector_mismatches = [
        index
        for index, hit in enumerate(result["hits"])
        if hit["retrieval_source"] == "vector_chunk" and "vector_focus_mismatch" in hit["reasons"]
    ]
    exact_focus_hits = [
        index
        for index, hit in enumerate(result["hits"])
        if "证券代码获取" in str(hit["matched_text"])
    ]
    assert exact_focus_hits
    assert vector_mismatches
    assert max(exact_focus_hits) < min(vector_mismatches)


def test_query_index_disables_vector_when_embedding_space_mismatches(tmp_path: Path) -> None:
    _, db_path = _build_sample_index(tmp_path)
    indexer = SQLiteIndexer(embedder=MismatchEmbedder())

    result = indexer.query_index(db_path, "证券信息获取", limit=10)

    assert result["vector_status"]["enabled"] is False
    assert result["vector_status"]["reason"] == "embedding_space_mismatch"
    assert all(hit["retrieval_source"] != "vector_chunk" for hit in result["hits"])


def test_query_index_falls_back_to_fts_when_vector_request_fails(tmp_path: Path) -> None:
    _, db_path = _build_sample_index(tmp_path)
    indexer = SQLiteIndexer(embedder=FailingEmbedder())

    result = indexer.query_index(db_path, "证券代码获取", limit=10)

    assert result["hit_count"] >= 1
    assert result["vector_status"]["enabled"] is False
    assert result["vector_status"]["reason"] == "query_embedding_failed"
    assert any(str(hit["retrieval_source"]).startswith("fts_") for hit in result["hits"])


def test_assemble_evidence_returns_llm_ready_context(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "证券代码获取的逻辑在哪里", limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] >= 1
    assert result["fts_query"] == "证券代码获取*"
    assert "Use only the following indexed evidence" in result["llm_context"]

    af_sample_block = next(
        block for block in result["evidence"]
        if block["procedure_name"] == "AF_SAMPLE"
    )
    assert "AF_系统参数公用_证券代码获取" in af_sample_block["excerpt"]
    assert "LS_FLOW" in af_sample_block["related_context"]["incoming_callers"]
    assert any(item["edge_type"] in {"jumps_to_label", "jumps_to_exit", "defines_label"} for item in af_sample_block["related_context"]["control_flow"])
    assert any(item["via_name"] == "LS_FLOW" for item in af_sample_block["related_context"]["two_hop_incoming"]) or af_sample_block["related_context"]["two_hop_incoming"] == []
    assert af_sample_block["chunk_type"] in {None, "call_flow", "call_block", "action_block", "control_block"}
    assert any(item["block_type"] in {"transaction", "sql_execute", "failure_handler"} for item in af_sample_block["recovered_blocks"])
    assert "Related procedure" in result["llm_context"]
    assert "Covering block:" in result["llm_context"]
    assert "Control flow:" in result["llm_context"]


def test_assemble_evidence_includes_two_hop_call_chain(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "LS_FLOW", limit=3, context_window=1, related_limit=3)

    ls_flow_block = next(block for block in result["evidence"] if block["procedure_name"] == "LS_FLOW")
    assert any(item["via_name"] == "AF_SAMPLE" and item["procedure_name"] == "AF_DEEP" for item in ls_flow_block["related_context"]["two_hop_outgoing"])
    assert "Two-hop outgoing chain:" in result["llm_context"]


def test_assemble_evidence_surfaces_exception_blocks_for_failure_query(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "查询交易资金表失败在哪里处理", limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] >= 1
    failure_block = result["evidence"][0]
    block_types = {item["block_type"] for item in failure_block["recovered_blocks"]}
    assert "failure_handler" in block_types or failure_block.get("block_type") == "failure_handler"
    assert "exception_handler" in block_types or "when_others_handler" in block_types
