from __future__ import annotations

import sqlite3
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


def _build_sample_index(tmp_path: Path) -> tuple[SQLiteIndexer, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
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


def test_build_index_creates_sqlite_tables_and_fts(tmp_path: Path) -> None:
    _, db_path = _build_sample_index(tmp_path)

    conn = sqlite3.connect(db_path)
    assert conn.execute("SELECT COUNT(*) FROM files").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM procedures").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM params").fetchone()[0] == 4
    assert conn.execute("SELECT COUNT(*) FROM actions").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'calls_procedure'").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM edges WHERE edge_type = 'reads_table'").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM chunks").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM blocks").fetchone()[0] >= 3
    assert conn.execute("SELECT COUNT(*) FROM block_edges").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM procedures_fts").fetchone()[0] == 2
    assert conn.execute("SELECT COUNT(*) FROM statements_fts").fetchone()[0] >= 5
    assert conn.execute("SELECT COUNT(*) FROM actions_fts").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM edges_fts").fetchone()[0] >= 4
    assert conn.execute("SELECT COUNT(*) FROM chunks_fts").fetchone()[0] >= 2
    assert conn.execute("SELECT COUNT(*) FROM blocks_fts").fetchone()[0] >= 3
    conn.close()


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
    assert af_sample_block["chunk_type"] in {None, "call_flow", "call_block", "action_block", "control_block"}
    assert any(item["block_type"] in {"transaction", "sql_execute", "failure_handler"} for item in af_sample_block["recovered_blocks"])
    assert "Related procedure" in result["llm_context"]
    assert "Covering block:" in result["llm_context"]
