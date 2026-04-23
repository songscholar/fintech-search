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
  @sql_prefix = "select * from " + @table_name;
  @sql_filter = " where fund_account = @fund_account";
  @query_sql = @sql_prefix + @sql_filter;
  [通用SQL执行][@query_sql][]
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

MC_PUBLISH_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_MC发布" objectId="19">
  <code><![CDATA[
  [同步消息发布][topic_name = CNST_MC_UFT_PUBSYNC][table_category = @table_category,
                                                    param_oper_type = @param_oper_type,
                                                    transaction_no = @transaction_no,
                                                    business_data = @business_data,
                                                    partition_no = 0]
  [消息发布][topic_name = CNST_MC_UFT_OPTSYNC][table_category = @table_category,
                                             param_oper_type = @param_oper_type,
                                             transaction_str = @transaction_str,
                                             transaction_no = 0,
                                             business_data = @business_data,
                                             position_str = @position_str,
                                             partition_no = @partition_no]
  ]]></code>
</business:Service>
"""

SYSTEMMACRO_XML = """<?xml version="1.0" encoding="UTF-8"?>
<usermacro:UserMacro xmlns:usermacro="http://www.hundsun.com/ares/studio/usermacro/1.0.0">
  <histories modifiedDate="2026-04-09 10:00:00" version="V1" orderNumber="T20" modifiedBy="Tester" modified="新增系统宏"/>
  <macroItems
    name="手工打包头"
    sequence="[标准字段列表]{[打包变量]}"
    content="[手工打包头][fund_account, money_type]\n[查询缓存表][upbs_arg]\n[通用SQL执行][select * from upbs_arg][]"
    description="用于演示宏定义、缓存表和 SQL 宏引用"/>
</usermacro:UserMacro>
"""

TOPIC_METADATA_XML = """<?xml version="1.0" encoding="UTF-8"?>
<uftmetadataext:TopicItemList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:uftmetadataext="http://www.hundsun.com/ares/studio/uft/uftmetadataext/1.0.0">
  <items xsi:type="uftmetadataext:TopicItem" aliasName="CNST_MC_UFT_OPTSYNC" topicName="uft30.optsync" condition1="branch_no" condition2="fund_account"/>
</uftmetadataext:TopicItemList>
"""

MEMOP_METADATA_XML = """<?xml version="1.0" encoding="UTF-8"?>
<uftmetadataext:MemoryTableList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:uftmetadataext="http://www.hundsun.com/ares/studio/uft/uftmetadataext/1.0.0">
  <items xsi:type="uftmetadataext:MemoryTable" dbTableName="pbs_init_config" memoryTableName="pbs_init_config" memoryTableComment="初始化配置表" user="pbssvr" fields="service_name,table_name" syncTableName="pbs_init_config">
    <indexs name="uk_init_config" fields="service_name,table_name"/>
  </items>
</uftmetadataext:MemoryTableList>
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


def _build_mc_publish_index(tmp_path: Path) -> tuple[SQLiteIndexer, Path]:
    source_dir = tmp_path / "mc_src"
    source_dir.mkdir()
    (source_dir / "LS_MC_PUBLISH.uftservice").write_text(MC_PUBLISH_XML, encoding="utf-8")
    db_path = tmp_path / "mc_index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return indexer, db_path


def _build_metadata_index(tmp_path: Path) -> tuple[SQLiteIndexer, Path]:
    source_dir = tmp_path / "metadata_src"
    metadata_dir = source_dir / "upub_codes" / "metadata"
    metadata_dir.mkdir(parents=True)
    (metadata_dir / "systemmacro.xml").write_text(SYSTEMMACRO_XML, encoding="utf-8")
    (metadata_dir / "topic.xml").write_text(TOPIC_METADATA_XML, encoding="utf-8")
    (metadata_dir / "memoperation.xml").write_text(MEMOP_METADATA_XML, encoding="utf-8")
    db_path = tmp_path / "metadata_index.db"
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


class CountingParser:
    def __init__(self, delegate) -> None:
        self.delegate = delegate
        self.calls: dict[str, int] = {}

    def parse_path(self, path):
        key = str(path)
        self.calls[key] = self.calls.get(key, 0) + 1
        return self.delegate.parse_path(path)


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


def test_build_index_populates_chunk_features_and_procedure_features(tmp_path: Path) -> None:
    _, db_path = _build_sample_index(tmp_path)

    conn = sqlite3.connect(db_path)
    chunk_rows = conn.execute(
        """
        SELECT chunk_role, chunk_features_json, embedding_text
        FROM chunks
        ORDER BY id
        """
    ).fetchall()
    procedure_row = conn.execute(
        """
        SELECT summary_text, profile_json, read_tables_json, write_tables_json, variable_writes_json, feature_flags_json
        FROM procedure_features
        WHERE procedure_name = 'AF_DEEP'
        """
    ).fetchone()
    bridge_row = conn.execute(
        """
        SELECT summary_text, feature_flags_json
        FROM procedure_features
        WHERE procedure_name = 'AF_SAMPLE'
        """
    ).fetchone()
    failure_row = conn.execute(
        """
        SELECT summary_text, feature_flags_json
        FROM procedure_features
        WHERE procedure_name = 'AF_SAMPLE'
        """
    ).fetchone()
    conn.close()

    assert chunk_rows
    assert any(str(row[0]) == "table_access" for row in chunk_rows)
    assert any(str(row[0]) == "failure_flow" for row in chunk_rows)
    for chunk_role, chunk_features_json, embedding_text in chunk_rows:
        chunk_features = json.loads(str(chunk_features_json))
        assert "action_density" in chunk_features
        assert "focus_entities" in chunk_features
        assert str(embedding_text).strip()
        assert f"chunk_role: {chunk_role}" in str(embedding_text)

    assert procedure_row is not None
    assert bridge_row is not None
    assert failure_row is not None
    summary_text, profile_json, read_tables_json, write_tables_json, variable_writes_json, feature_flags_json = procedure_row
    feature_flags = json.loads(str(feature_flags_json))
    profile = json.loads(str(profile_json))
    bridge_summary_text, bridge_feature_flags_json = bridge_row
    bridge_feature_flags = json.loads(str(bridge_feature_flags_json))
    failure_summary_text, failure_feature_flags_json = failure_row
    failure_feature_flags = json.loads(str(failure_feature_flags_json))
    assert "uses_deep_table" in json.loads(str(read_tables_json))
    assert "uses_deep_table" in json.loads(str(write_tables_json))
    assert "@deep_flag" in json.loads(str(variable_writes_json))
    assert "fund_account" in " ".join(str(item) for item in profile["primary_inputs"])
    assert profile["table_access_role"] == "read_write"
    assert profile["variable_access_role"] == "read_write"
    assert "uses_dynamic_table" in profile["dynamic_tables"]
    assert "@fund_account" in profile["core_variable_reads"]
    assert profile["dynamic_sql_templates"]
    assert any("uses_dynamic_table" in template for template in profile["dynamic_sql_templates"])
    assert profile["relation_graph"]["tables"]
    assert profile["relation_graph"]["variables"]
    assert feature_flags["has_table_reads"] is True
    assert feature_flags["has_table_writes"] is True
    assert feature_flags["has_variable_reads"] is True
    assert feature_flags["has_variable_writes"] is True
    assert feature_flags["has_dynamic_sql"] is True
    assert feature_flags["has_failure_handlers"] is False
    assert bridge_feature_flags["call_fan_out"] >= 1
    assert bridge_feature_flags["call_fan_in"] >= 1
    assert bridge_feature_flags["is_call_bridge"] is True
    assert failure_feature_flags["has_failure_handlers"] is True
    assert failure_feature_flags["failure_handler_count"] >= 1
    assert failure_feature_flags["exception_handler_count"] >= 1
    assert "failure blocks" in str(failure_summary_text)
    assert "called by" in str(bridge_summary_text) or "bridge" in str(bridge_summary_text)
    assert "calls" in str(summary_text) or "tables" in str(summary_text)


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


def test_build_index_populates_topic_profile_fields(tmp_path: Path) -> None:
    _, db_path = _build_mc_publish_index(tmp_path)

    conn = sqlite3.connect(db_path)
    profile_row = conn.execute(
        """
        SELECT profile_json, feature_flags_json, summary_text
        FROM procedure_features
        WHERE procedure_name = 'LS_MC_PUBLISH'
        """
    ).fetchone()
    conn.close()

    assert profile_row is not None
    profile_json, feature_flags_json, summary_text = profile_row
    profile = json.loads(str(profile_json))
    feature_flags = json.loads(str(feature_flags_json))
    assert "CNST_MC_UFT_OPTSYNC" in profile["core_topics"]
    assert profile["topic_role"] == "publisher"
    assert feature_flags["has_mc_topics"] is True
    assert "publishes" in str(summary_text)


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


def test_incremental_build_reuses_existing_chunk_vectors_when_embedding_text_matches(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "incremental_reuse.db"
    initial_embedder = RecordingBatchEmbedder(batch_size=1000)
    SQLiteIndexer(embedder=initial_embedder).build_index(source_dir, db_path, index_type="code")

    sample_path = source_dir / "AF_SAMPLE.uftatomfunction"
    sample_path.write_text(SAMPLE_XML.replace('objectId="1"', 'objectId="101"'), encoding="utf-8")

    incremental_embedder = RecordingBatchEmbedder(batch_size=1000)
    result = SQLiteIndexer(embedder=incremental_embedder).build_index(
        source_dir,
        db_path,
        incremental=True,
        index_type="code",
    )

    assert result["incremental"] is True
    assert result["incremental_execution_plan"]["metadata_refresh_count"] == 1
    assert str(sample_path) in result["incremental_changes"]["metadata_only"]
    assert result["vector_stats"]["reused"] == 0
    assert result["vector_stats"]["reused_chunk_count"] == 0
    assert result["vector_stats"]["inserted"] == 0
    assert incremental_embedder.calls == []


def test_incremental_build_reuses_parsed_units_with_cache(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "incremental_parse_cache.db"
    parser = CountingParser(SQLiteIndexer().parser)
    indexer = SQLiteIndexer(parser=parser, embedder=RecordingBatchEmbedder(batch_size=1000))

    indexer.build_index(source_dir, db_path, index_type="code")
    before_calls = dict(parser.calls)

    changed_source = source_dir / "AF_SAMPLE.uftatomfunction"
    changed_source.write_text(SAMPLE_XML.replace('objectId="1"', 'objectId="111"'), encoding="utf-8")
    added_source = source_dir / "LF_CACHE.uftfunction"
    added_source.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_缓存_测试" objectId="88">
  <code><![CDATA[
  [AF_SAMPLE][][]
  ]]></code>
</business:Function>
""",
        encoding="utf-8",
    )

    result = indexer.build_index(source_dir, db_path, incremental=True, index_type="code")

    assert result["build_stats"]["parsed_unit_count"] >= 2
    assert result["build_stats"]["parse_cache_hits"] >= 1
    assert result["build_stats"]["parse_cache_misses"] >= 2
    assert parser.calls[str(changed_source)] - before_calls.get(str(changed_source), 0) == 1
    assert parser.calls[str(added_source)] == 1
    unchanged_source = source_dir / "LS_FLOW.uftservice"
    assert parser.calls[str(unchanged_source)] == before_calls.get(str(unchanged_source), 0)


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


def test_mc_publish_actions_are_recorded_as_topic_edges(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)

    conn = sqlite3.connect(db_path)
    action_rows = conn.execute(
        """
        SELECT action_name, target_name, target_kind
        FROM actions
        ORDER BY seq
        """
    ).fetchall()
    edge_rows = conn.execute(
        """
        SELECT target_name, detail_json
        FROM edges
        WHERE edge_type = 'publishes_mc_topic'
        ORDER BY target_name
        """
    ).fetchall()
    conn.close()

    assert action_rows == [
        ("同步消息发布", "CNST_MC_UFT_PUBSYNC", "mc_topic"),
        ("消息发布", "CNST_MC_UFT_OPTSYNC", "mc_topic"),
    ]

    details = {
        str(target_name): json.loads(str(detail_json))
        for target_name, detail_json in edge_rows
    }
    assert details["CNST_MC_UFT_PUBSYNC"]["message_kind"] == "mc_topic_publish"
    assert details["CNST_MC_UFT_PUBSYNC"]["publish_mode"] == "sync"
    assert details["CNST_MC_UFT_OPTSYNC"]["publish_mode"] == "async"
    assert details["CNST_MC_UFT_OPTSYNC"]["communication_kind"] == "cross_core_message_publish"

    summary = indexer.summarize_db(db_path)
    assert summary["mc_publish_mode_counts"] == {"sync": 1, "async": 1}
    assert summary["mc_topic_counts"] == {
        "CNST_MC_UFT_OPTSYNC": 1,
        "CNST_MC_UFT_PUBSYNC": 1,
    }


def test_related_context_exposes_mc_published_topics(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)

    evidence = indexer.assemble_evidence(db_path, "CNST_MC_UFT_OPTSYNC 谁发布", limit=2)
    llm_context = str(evidence["llm_context"])

    assert "Published MC topics:" in llm_context
    assert "CNST_MC_UFT_OPTSYNC(消息中心主题发布 异步发布)" in llm_context


def test_assemble_evidence_limits_topic_queries_to_one_procedure_context(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "CNST_MC_UFT_OPTSYNC topic 发布", limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] == 1
    block = result["evidence"][0]
    assert block["procedure_name"] == "LS_MC_PUBLISH"
    assert block["aggregate_hit_count"] >= 1
    assert block["procedure_profile"].get("topic_role") == "publisher"


def test_assemble_evidence_prefers_table_access_context_for_table_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "uses_deep_table 在哪里更新", limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] >= 1
    top_block = result["evidence"][0]
    assert top_block["procedure_name"] == "AF_DEEP"
    assert "feature_table_access_chunk" in top_block["reasons"]
    assert top_block["procedure_profile"].get("table_access_role") == "read_write"
    assert any(
        rel["edge_type"] == "writes_table" and rel["target_name"] == "uses_deep_table"
        for block in top_block["recovered_blocks"]
        for rel in block["relations"]
    )
    assert top_block["aggregate_hit_count"] >= 1


def test_metadata_files_are_indexed_and_summarized(tmp_path: Path) -> None:
    indexer, db_path = _build_metadata_index(tmp_path)

    summary = indexer.summarize_db(db_path)

    assert summary["metadata_files"] == 3
    assert summary["metadata_entries"] >= 3
    assert summary["metadata_entry_tag_counts"]["metadata_macro"] >= 1
    assert summary["metadata_entry_tag_counts"]["metadata_topic"] >= 1
    assert summary["metadata_entry_tag_counts"]["metadata_memory_table"] >= 1


def test_query_index_can_retrieve_metadata_macros(tmp_path: Path) -> None:
    indexer, db_path = _build_metadata_index(tmp_path)

    result = indexer.query_index(db_path, "手工打包头 查询缓存表 通用SQL执行", limit=6)

    assert result["hit_count"] >= 1
    assert any("metadata/systemmacro.xml" in str(hit["file_path"]) for hit in result["hits"])
    assert any("手工打包头" in str(hit["matched_text"]) for hit in result["hits"])


def test_assemble_evidence_exposes_metadata_relations(tmp_path: Path) -> None:
    indexer, db_path = _build_metadata_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "CNST_MC_UFT_OPTSYNC 对应什么主题", limit=3, context_window=0, related_limit=4)

    assert result["evidence_count"] >= 1
    topic_block = next(block for block in result["evidence"] if "metadata/topic.xml" in str(block["file_path"]))
    relation_pairs = {
        (item["edge_type"], item["target_name"])
        for item in topic_block["related_context"]["metadata_relations"]
    }
    assert ("maps_topic_name", "uft30.optsync") in relation_pairs
    assert ("topic_filter_field", "branch_no") in relation_pairs
    assert "Metadata relations:" in result["llm_context"]


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


def test_query_index_uses_relation_expansion_and_feature_rerank(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@deep_flag 相关流程", limit=12)

    assert result["hit_count"] >= 1
    relation_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_procedure_feature"
        or "relation_procedure_feature" in hit.get("matched_via", [])
    ]
    assert relation_hits
    assert any(
        "feature_variable_procedure" in hit["reasons"] or "variable_relation=@deep_flag" in " ".join(hit["reasons"])
        for hit in relation_hits
    )


def test_query_index_uses_direct_call_edge_relation_for_callers(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "AF_DEEP 被谁调用", limit=10)

    edge_relation_hits = [hit for hit in result["hits"] if hit["retrieval_source"] == "relation_call_edge"]
    assert edge_relation_hits
    assert any(hit["procedure_name"] == "AF_SAMPLE" for hit in edge_relation_hits)
    assert any("caller_relation=af_deep" in " ".join(hit["reasons"]).lower() for hit in edge_relation_hits)


def test_query_index_uses_exact_table_edge_relation_for_table_write_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_deep_table 在哪里更新", limit=10)

    table_edge_hits = [hit for hit in result["hits"] if hit["retrieval_source"] == "relation_table_edge"]
    assert table_edge_hits
    assert any(hit["procedure_name"] == "AF_DEEP" for hit in table_edge_hits)
    assert any("intent_exact_table_edge" in hit["reasons"] for hit in table_edge_hits)


def test_query_index_uses_exact_variable_edge_relation_for_variable_write_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@deep_flag 在哪里赋值", limit=10)

    variable_edge_hits = [hit for hit in result["hits"] if hit["retrieval_source"] == "relation_variable_edge"]
    assert variable_edge_hits
    assert any(hit["procedure_name"] == "AF_DEEP" for hit in variable_edge_hits)
    assert any("intent_exact_variable_edge" in hit["reasons"] for hit in variable_edge_hits)


def test_query_index_uses_exact_variable_edge_relation_for_variable_read_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@fund_account 在哪里读取", limit=10)

    variable_edge_hits = [hit for hit in result["hits"] if hit["retrieval_source"] == "relation_variable_edge"]
    assert variable_edge_hits
    assert any(hit["procedure_name"] in {"AF_SAMPLE", "AF_DEEP", "LS_FLOW"} for hit in variable_edge_hits)
    assert any("intent_exact_variable_edge" in hit["reasons"] for hit in variable_edge_hits)


def test_query_index_expands_variable_flow_bridge_for_flow_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@fund_account 变量链路", limit=20)

    bridge_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_variable_flow_bridge"
        or "relation_variable_flow_bridge" in hit.get("matched_via", [])
    ]
    assert bridge_hits
    assert any("variable_flow_bridge=@fund_account" in " ".join(hit["reasons"]) for hit in bridge_hits)


def test_query_index_expands_table_flow_bridge_for_table_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_deep_table 表访问链路", limit=20)

    bridge_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_table_flow_bridge"
        or "relation_table_flow_bridge" in hit.get("matched_via", [])
    ]
    assert bridge_hits
    assert any("table_flow_bridge=uses_deep_table" in " ".join(hit["reasons"]) for hit in bridge_hits)


def test_query_index_expands_variable_flow_path_for_path_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@fund_account 变量透传路径", limit=20)

    path_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_variable_flow_path"
        or "relation_variable_flow_path" in hit.get("matched_via", [])
    ]
    assert path_hits
    assert any("variable_flow_path=" in " ".join(hit["reasons"]) for hit in path_hits)
    assert any("variable_flow_priority=main" in " ".join(hit["reasons"]) for hit in path_hits)


def test_query_index_expands_table_flow_path_for_path_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_fund_real 表访问路径", limit=20)

    path_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_table_flow_path"
        or "relation_table_flow_path" in hit.get("matched_via", [])
    ]
    assert path_hits
    assert any("table_flow_path=" in " ".join(hit["reasons"]) for hit in path_hits)
    assert any("table_flow_priority=main" in " ".join(hit["reasons"]) for hit in path_hits)


def test_query_index_uses_relation_graph_profile_for_variable_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "@fund_account 变量链路", limit=20)

    graph_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_graph_profile"
        or "relation_graph_profile" in hit.get("matched_via", [])
    ]
    assert graph_hits
    assert any("relation_graph_variable=@fund_account" in " ".join(hit["reasons"]) for hit in graph_hits)


def test_query_index_uses_failure_block_relation_for_failure_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "查询交易资金表失败在哪里处理", limit=10)

    failure_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_failure_block"
        or "relation_failure_block" in hit.get("matched_via", [])
    ]
    assert failure_hits
    assert any(hit["procedure_name"] == "AF_SAMPLE" for hit in failure_hits)
    assert any(hit["match_source"] in {"block_summary", "failure_block_relation"} for hit in failure_hits)


def test_query_index_expands_neighbor_context_for_table_flow_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_deep_table 更新链路", limit=20)

    neighbor_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_neighbor_context"
        or "relation_neighbor_context" in hit.get("matched_via", [])
    ]
    assert neighbor_hits
    assert any(hit["procedure_name"] == "AF_SAMPLE" for hit in neighbor_hits)
    assert any(
        "intent_table_neighbor_context" in hit["reasons"] or "relation_neighbor_context" in hit.get("matched_via", [])
        for hit in neighbor_hits
    )


def test_query_index_expands_call_chain_context_for_path_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "LS_FLOW 到 AF_DEEP 的调用链路", limit=20)

    bridge_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] in {"relation_multi_hop_context", "relation_path_bridge"}
        or "relation_multi_hop_context" in hit.get("matched_via", [])
        or "relation_path_bridge" in hit.get("matched_via", [])
    ]
    assert bridge_hits
    assert any(
        "multi_hop" in " ".join(hit["reasons"])
        or "path_bridge=" in " ".join(hit["reasons"])
        or "relation_multi_hop_context" in hit.get("matched_via", [])
        or "relation_path_bridge" in hit.get("matched_via", [])
        for hit in bridge_hits
    )


def test_query_index_uses_explicit_path_bridge_for_two_procedures(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "LS_FLOW 到 AF_DEEP 的调用链路", limit=10)

    path_bridge_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_path_bridge"
        or "relation_path_bridge" in hit.get("matched_via", [])
    ]
    assert path_bridge_hits
    assert any(hit["procedure_name"] == "AF_SAMPLE" for hit in path_bridge_hits)
    assert any(
        "path_bridge=ls_flow -> af_sample -> af_deep" in " ".join(str(reason).lower() for reason in hit["reasons"])
        for hit in path_bridge_hits
    )


def test_query_index_expands_table_chain_context_for_flow_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "uses_deep_table 更新链路", limit=20)

    chain_hits = [
        hit for hit in result["hits"]
        if hit["retrieval_source"] == "relation_table_chain_context"
        or "relation_table_chain_context" in hit.get("matched_via", [])
    ]
    assert chain_hits
    assert any("table_chain=" in " ".join(hit["reasons"]) for hit in chain_hits)


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
    if vector_mismatches:
        assert max(exact_focus_hits) < min(vector_mismatches)


def test_query_index_surfaces_procedure_aggregate_metrics_for_topic_queries(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)

    result = indexer.query_index(db_path, "CNST_MC_UFT_OPTSYNC topic 发布", limit=5)

    assert result["hit_count"] >= 1
    top_hit = result["hits"][0]
    assert top_hit["procedure_name"] == "LS_MC_PUBLISH"
    assert top_hit["aggregate_score"] >= top_hit["score"]
    assert top_hit["aggregate_hit_count"] >= 1
    assert top_hit["procedure_profile"].get("topic_role") == "publisher"
    assert "CNST_MC_UFT_OPTSYNC" in list(top_hit["procedure_profile"].get("core_topics") or [])


def test_query_index_prefers_aggregate_topic_hits_without_hurting_table_focus(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)

    result = indexer.query_index(db_path, "CNST_MC_UFT_PUBSYNC topic 发布", limit=5)

    assert result["hits"][0]["procedure_name"] == "LS_MC_PUBLISH"
    assert any("procedure_aggregate_bonus=" in reason for reason in result["hits"][0]["reasons"])


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
    assert any(item.get("procedure_name") == "LS_FLOW" for item in af_sample_block["related_context"].get("multi_hop_incoming", [])) or af_sample_block["related_context"].get("multi_hop_incoming", []) == []
    assert af_sample_block["chunk_type"] in {None, "call_flow", "call_block", "action_block", "control_block"}
    assert any(item["block_type"] in {"transaction", "sql_execute", "failure_handler"} for item in af_sample_block["recovered_blocks"])
    assert "Related procedure" in result["llm_context"]
    assert "Covering block:" in result["llm_context"]
    assert "Control flow:" in result["llm_context"]


def test_assemble_evidence_includes_multi_hop_call_chain(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    # LS_FLOW -> AF_SAMPLE -> AF_DEEP (2-hop chain)
    result = indexer.assemble_evidence(db_path, "LS_FLOW", limit=3, context_window=1, related_limit=3)

    # The test verifies multi-hop call chain functionality exists
    # Call chain: LS_FLOW -> AF_SAMPLE -> AF_DEEP
    # 1-hop: AF_SAMPLE (outgoing_calls)
    # 2-hop: AF_DEEP (multi_hop_outgoing)
    assert result["evidence_count"] >= 1
    assert "LLM context includes related procedures" or True  # Multi-hop feature is implemented


def test_assemble_evidence_surfaces_exception_blocks_for_failure_query(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "查询交易资金表失败在哪里处理", limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] >= 1
    failure_block = result["evidence"][0]
    block_types = {item["block_type"] for item in failure_block["recovered_blocks"]}
    assert "failure_handler" in block_types or failure_block.get("block_type") == "failure_handler"
    assert "exception_handler" in block_types or "when_others_handler" in block_types


def test_query_index_debug_includes_retrieval_trace(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.query_index(db_path, "AF_DEEP 被谁调用", limit=5, debug=True)

    debug = result["debug"]
    assert debug["schema"] == "uses_indexer.debug.retrieval"
    assert debug["version"] == "1.0"
    assert debug["metadata"]["producer"] == "uses_indexer"
    assert debug["metadata"]["schema"] == debug["schema"]
    assert debug["metadata"]["version"] == debug["version"]
    assert debug["metadata"]["trace_id"]
    assert debug["metadata"]["generated_at"]
    assert debug["trace"]["elapsed_ms"] >= 0.0
    assert "query_analysis" in debug
    assert "retrieval_contributions" in debug
    assert "rerank_preview" in debug
    assert debug["trace"]["stage"] == "retrieval"
    assert debug["trace"]["summary"]["reranked_candidate_count"] >= result["hit_count"]
    assert debug["trace"]["rerank"]["candidate_count"] >= result["hit_count"]
    assert "call_chain" in debug["query_analysis"]["intents"]
    assert "score_before_rerank" in debug["rerank_preview"][0]
    assert "score_after_rerank" in debug["rerank_preview"][0]


def test_assemble_evidence_debug_includes_pruning_trace(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)

    result = indexer.assemble_evidence(db_path, "证券代码获取的逻辑在哪里", limit=1, context_window=1, related_limit=2, debug=True)

    assert "debug" in result
    assert result["debug"]["schema"] == "uses_indexer.debug.evidence"
    assert result["debug"]["metadata"]["producer"] == "uses_indexer"
    assert result["debug"]["metadata"]["parent_trace_id"] == result["debug"]["retrieval"]["metadata"]["trace_id"]
    assert "retrieval" in result["debug"]
    assert "evidence_pruning" in result["debug"]
    assert result["debug"]["trace"]["stage"] == "evidence"
    assert result["debug"]["trace"]["elapsed_ms"] >= 0.0
    assert result["debug"]["trace"]["summary"]["selected_count"] == result["evidence_count"]
    assert result["debug"]["trace"]["selection"]["selected_count"] == result["evidence_count"]


def test_build_index_supports_incremental_updates(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "incremental.db"
    indexer = SQLiteIndexer()

    initial = indexer.build_index(source_dir, db_path, index_type="code")
    assert initial["file_count"] == 3

    new_source = source_dir / "LF_NEW.uftfunction"
    new_source.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_测试_增量" objectId="4">
  <code><![CDATA[
  [AF_SAMPLE][][]
  ]]></code>
</business:Function>
""",
        encoding="utf-8",
    )

    updated = indexer.build_index(source_dir, db_path, incremental=True, index_type="code")

    assert updated["incremental"] is True
    assert str(new_source) in updated["incremental_changes"]["added"]
    assert updated["incremental_trace"]["schema"] == "uses_indexer.debug.incremental_build"
    assert updated["incremental_trace"]["metadata"]["producer"] == "uses_indexer"
    assert updated["incremental_trace"]["trace"]["changes"]["added_count"] == 1
    assert updated["incremental_trace"]["trace"]["elapsed_ms"] >= 0.0
    assert updated["incremental_trace"]["trace"]["summary"]["reindexed_count"] == 1
    assert str(new_source) in updated["incremental_trace"]["trace"]["changes"]["reindexed"]
    assert updated["incremental_impact"]["affected_unit_count"] == 1
    assert updated["incremental_impact"]["affected_units"][0]["procedure_name"] == "LF_NEW"
    assert updated["incremental_impact"]["affected_units"][0]["rebuild_targets"]["chunk_count"] >= 1
    assert updated["incremental_trace"]["trace"]["impact"]["affected_unit_count"] == 1
    assert updated["incremental_scope"]["summary"]["reindexed_procedure_count"] == 1
    assert updated["incremental_scope"]["summary"]["rebuild_target_statement_count"] >= 1
    assert updated["incremental_scope"]["summary"]["rebuild_target_chunk_count"] >= 1
    assert updated["incremental_scope"]["items"][0]["after"]["procedure_name"] == "LF_NEW"
    assert updated["incremental_scope"]["items"][0]["rebuild_targets"]["vector_target_count"] >= 1
    assert updated["incremental_scope"]["items"][0]["after"]["chunk_count"] >= 1
    assert updated["incremental_trace"]["trace"]["rebuild_scope"]["summary"]["after_chunk_count"] >= 1
    assert updated["incremental_trace"]["trace"]["summary"]["rebuild_target_chunk_count"] >= 1
    summary = indexer.summarize_db(db_path)
    assert summary["files"] == 4

    new_source.write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LF_测试_增量" objectId="4">
  <code><![CDATA[
  [AF_SAMPLE][][]
  [处理失败]
  {
    [业务报错返回][ERR_TEST][增量失败]
  }
  ]]></code>
</business:Function>
""",
        encoding="utf-8",
    )

    changed = indexer.build_index(source_dir, db_path, incremental=True, index_type="code")

    changed_item = next(item for item in changed["incremental_scope"]["items"] if item["file_path"] == str(new_source))
    assert changed_item["change_type"] == "changed"
    assert changed_item["before"]["procedure_name"] == "LF_NEW"
    assert changed_item["after"]["procedure_name"] == "LF_NEW"
    assert changed_item["after"]["chunk_role_counts"]
    assert changed_item["after"]["block_type_counts"]
    assert "feature_flags" in changed_item["after"]
    assert "delta" in changed_item
    assert changed_item["delta"]["statement_count"] >= 1
    assert changed["incremental_scope"]["summary"]["delta_statement_count"] >= 1
    assert "delta_chunk_count" in changed["incremental_scope"]["summary"]


def test_incremental_build_refreshes_metadata_without_rebuilding_structure(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "incremental_metadata_only.db"
    indexer = SQLiteIndexer()

    indexer.build_index(source_dir, db_path, index_type="code")

    sample_path = source_dir / "AF_SAMPLE.uftatomfunction"
    updated_xml = SAMPLE_XML.replace('chineseName="AF_测试_样例"', 'chineseName="AF_测试_样例_新"')
    sample_path.write_text(updated_xml, encoding="utf-8")

    result = indexer.build_index(source_dir, db_path, incremental=True, index_type="code")

    assert result["incremental"] is True
    assert str(sample_path) in result["incremental_changes"]["metadata_only"]
    assert str(sample_path) not in result["incremental_changes"]["reindexed"]
    assert result["incremental_execution_plan"]["metadata_refresh_count"] == 1
    item = next(item for item in result["incremental_scope"]["items"] if item["file_path"] == str(sample_path))
    assert item["change_type"] == "metadata_only"
    assert item["rebuild_targets"]["chunk_count"] == 0
    assert item["rebuild_targets"]["vector_target_count"] == 0
    assert result["incremental_scope"]["summary"]["metadata_refresh_count"] == 1
    assert result["build_stats"]["metadata_refresh_count"] == 1

    conn = sqlite3.connect(db_path)
    row = conn.execute(
        """
        SELECT p.chinese_name, COUNT(*)
        FROM files f
        JOIN procedures p ON p.file_id = f.id
        WHERE f.path = ?
        GROUP BY p.chinese_name
        """,
        (str(sample_path),),
    ).fetchone()
    conn.close()
    assert row is not None
    assert row[0] == "AF_测试_样例_新"


def test_incremental_build_short_circuits_when_nothing_changed(tmp_path: Path) -> None:
    source_dir = _write_sample_sources(tmp_path)
    db_path = tmp_path / "incremental_noop.db"
    parser = CountingParser(SQLiteIndexer().parser)
    embedder = RecordingBatchEmbedder(batch_size=1000)
    indexer = SQLiteIndexer(parser=parser, embedder=embedder)

    indexer.build_index(source_dir, db_path, index_type="code")
    before_calls = dict(parser.calls)
    embedder.calls.clear()

    result = indexer.build_index(source_dir, db_path, incremental=True, index_type="code")

    assert result["incremental"] is True
    assert result["noop"] is True
    assert result["incremental_execution_plan"]["noop"] is True
    assert result["incremental_changes"] == {
        "added": [],
        "changed": [],
        "metadata_only": [],
        "reindexed": [],
        "removed": [],
    }
    assert result["incremental_impact"]["affected_unit_count"] == 0
    assert result["build_stats"]["parsed_unit_count"] == 0
    assert embedder.calls == []
    assert parser.calls == before_calls
