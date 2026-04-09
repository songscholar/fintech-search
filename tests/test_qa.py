from __future__ import annotations

from pathlib import Path

from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.qa import CodebaseQA


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [获取记录][uses_fund_real(idx_x)][fund_account = @fund_account]
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


def _prepare_qa(tmp_path: Path) -> tuple[CodebaseQA, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
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
    assert "AF_SAMPLE" in result["draft_answer"]["answer"]
    assert result["draft_answer"]["supporting_locations"]


def test_ask_returns_insufficient_evidence_when_no_hits(tmp_path: Path) -> None:
    qa, db_path = _prepare_qa(tmp_path)

    result = qa.ask(db_path, "完全不存在的业务问题", evidence_limit=2, context_window=1, related_limit=1)

    assert result["draft_answer"]["status"] == "insufficient_evidence"
    assert result["evidence_count"] == 0
