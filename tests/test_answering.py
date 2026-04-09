from __future__ import annotations

from pathlib import Path

from uses_indexer.answering import CodebaseAnswerer
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


class StubLlm:
    def __init__(self, content: str | None = None) -> None:
        self.content = content

    def is_configured(self) -> bool:
        return self.content is not None

    def complete(self, *, system_prompt: str, user_prompt: str) -> dict[str, object]:
        assert "用户问题:" in user_prompt
        return {
            "provider": "stub",
            "model": "stub-model",
            "base_url": "stub://local",
            "content": self.content or "",
            "raw_response": {},
        }


def _build_answerer(tmp_path: Path, *, llm: StubLlm | None = None) -> tuple[CodebaseAnswerer, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    return CodebaseAnswerer(qa=qa, llm=llm), db_path


def test_answer_uses_draft_when_llm_not_configured(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm(None))

    result = answerer.answer(db_path, "证券代码获取的逻辑在哪里", evidence_limit=2)

    assert result["answer_source"] == "draft"
    assert result["final_answer"]["source"] == "draft"
    assert "AF_SAMPLE" in result["final_answer"]["text"]


def test_answer_uses_llm_when_available(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm("这是模型生成的最终答案。"))

    result = answerer.answer(db_path, "证券代码获取的逻辑在哪里", evidence_limit=2)

    assert result["answer_source"] == "llm"
    assert result["final_answer"]["text"] == "这是模型生成的最终答案。"
    assert result["final_answer"]["used_model"] == "stub-model"
