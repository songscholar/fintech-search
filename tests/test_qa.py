from __future__ import annotations

from pathlib import Path

from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.qa import CodebaseQA
from uses_indexer.strategy_config import QaPolicy


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [AF_DEEP][][]
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

DEEP_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_深层" objectId="3">
  <code><![CDATA[
  @deep_flag = 1;
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

TOPIC_METADATA_XML = """<?xml version="1.0" encoding="UTF-8"?>
<uftmetadataext:TopicItemList xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:uftmetadataext="http://www.hundsun.com/ares/studio/uft/uftmetadataext/1.0.0">
  <items xsi:type="uftmetadataext:TopicItem" aliasName="CNST_MC_UFT_OPTSYNC" topicName="uft30.optsync" condition1="branch_no" condition2="fund_account"/>
</uftmetadataext:TopicItemList>
"""


def _prepare_qa(tmp_path: Path) -> tuple[CodebaseQA, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")
    (source_dir / "AF_DEEP.uftatomfunction").write_text(DEEP_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return CodebaseQA(indexer), db_path


def _prepare_topic_qa(tmp_path: Path) -> tuple[CodebaseQA, Path]:
    source_dir = tmp_path / "topic_src"
    source_dir.mkdir()
    (source_dir / "LS_MC_PUBLISH.uftservice").write_text(MC_PUBLISH_XML, encoding="utf-8")

    db_path = tmp_path / "topic_index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return CodebaseQA(indexer), db_path


def _prepare_metadata_qa(tmp_path: Path) -> tuple[CodebaseQA, Path]:
    source_dir = tmp_path / "metadata_src"
    metadata_dir = source_dir / "upub_codes" / "metadata"
    metadata_dir.mkdir(parents=True)
    (metadata_dir / "topic.xml").write_text(TOPIC_METADATA_XML, encoding="utf-8")

    db_path = tmp_path / "metadata_index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    return CodebaseQA(indexer), db_path


def test_ask_builds_prompt_and_draft_answer(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "证券代码获取的逻辑在哪里", evidence_limit=3, context_window=1, related_limit=2)

    assert result["evidence_count"] >= 1
    assert "你是一个面向 USES/UFT DSL 代码库的问答助手" in result["prompt_package"]["system_prompt"]
    assert "用户问题: 证券代码获取的逻辑在哪里" in result["prompt_package"]["user_prompt"]
    assert result["draft_answer"]["status"] == "ok"
    assert result["draft_answer"]["tier"] == "grounded_summary"
    assert result["draft_answer"]["confidence"]["label"] in {"medium", "high"}
    assert "AF_SAMPLE" in result["draft_answer"]["answer"]
    assert result["draft_answer"]["supporting_locations"]
    assert result["draft_answer"]["primary_candidate"]["procedure_name"] == "AF_SAMPLE"


def test_ask_returns_insufficient_evidence_when_no_hits(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "完全不存在的业务问题", evidence_limit=2, context_window=1, related_limit=1)

    assert result["draft_answer"]["status"] == "insufficient_evidence"
    assert result["draft_answer"]["tier"] == "retrieval_only"
    assert result["draft_answer"]["confidence"]["label"] == "low"
    assert result["evidence_count"] == 0


def test_qa_policy_supplies_default_limits(tmp_path: Path) -> None:
    _, db_path = _prepare_qa(tmp_path)
    source_dir = tmp_path / "src"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer, policy=QaPolicy(evidence_limit=2, context_window=1, related_limit=1))

    result = qa.ask(db_path, "证券代码获取的逻辑在哪里")

    assert result["qa_policy"] == {
        "evidence_limit": 2,
        "context_window": 1,
        "related_limit": 1,
    }


def test_ask_tracks_primary_and_secondary_candidates(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "AF_SAMPLE 被谁调用", evidence_limit=3, context_window=1, related_limit=2)

    assert result["draft_answer"]["primary_candidate"]
    assert result["draft_answer"]["primary_candidate"]["procedure_name"] in {"AF_SAMPLE", "LS_FLOW"}
    assert isinstance(result["draft_answer"]["secondary_candidates"], list)
    assert float(result["draft_answer"]["primary_candidate"]["aggregate_score"]) >= 0.0
    secondary_names = [item["procedure_name"] for item in result["draft_answer"]["secondary_candidates"]]
    assert len(secondary_names) == len(set(secondary_names))


def test_ask_uses_query_specific_section_for_callers(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "AF_DEEP 被谁调用", evidence_limit=3, context_window=1, related_limit=2)

    assert result["draft_answer"]["query_type"] == "callers"
    assert "上游调用:" in result["draft_answer"]["answer"]


def test_ask_surfaces_path_bridge_summary_for_call_chain_questions(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "LS_FLOW 到 AF_DEEP 的调用链路", evidence_limit=3, context_window=1, related_limit=2)

    summary_points = list(result["draft_answer"]["summary_points"])
    assert any("调用链桥接路径" in item for item in summary_points)
    assert any("桥接候选过程" in item for item in summary_points)
    assert result["draft_answer"]["confidence"]["score"] >= 0.55


def test_ask_surfaces_profile_hints_for_table_queries(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "uses_fund_real 在哪里读取", evidence_limit=3, context_window=1, related_limit=2)

    summary_points = list(result["draft_answer"]["summary_points"])
    assert any("核心表访问" in item for item in summary_points)


def test_ask_surfaces_failure_path_summary_for_failure_questions(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "查询交易资金表失败在哪里处理", evidence_limit=3, context_window=1, related_limit=2)

    summary_points = list(result["draft_answer"]["summary_points"])
    assert any("失败处理块" in item for item in summary_points)
    assert result["draft_answer"]["confidence"]["label"] in {"medium", "high"}


def test_ask_surfaces_topic_profile_hints_for_topic_queries(tmp_path: Path) -> None:
    qa, db_path = _prepare_topic_qa(tmp_path)

    result = qa.ask(db_path, "CNST_MC_UFT_OPTSYNC topic 发布", evidence_limit=3, context_window=1, related_limit=2)

    assert result["draft_answer"]["query_type"] == "topic_publish"
    summary_points = list(result["draft_answer"]["summary_points"])
    assert any("发布主题包括" in item for item in summary_points)


def test_ask_uses_metadata_specific_summary_for_metadata_queries(tmp_path: Path) -> None:
    qa, db_path = _prepare_metadata_qa(tmp_path)

    result = qa.ask(db_path, "CNST_MC_UFT_OPTSYNC metadata 定义", evidence_limit=3, context_window=0, related_limit=2)

    assert result["draft_answer"]["query_type"] == "metadata_definition"
    assert "Metadata 定义:" in result["draft_answer"]["answer"]
    summary_points = list(result["draft_answer"]["summary_points"])
    assert any("metadata 定义过程" in item for item in summary_points)
