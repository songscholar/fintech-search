from __future__ import annotations

from pathlib import Path

from uses_indexer.answer_strategy import AdaptiveAnswerStrategy
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.embeddings import LocalHashedEmbedder
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.qa import CodebaseQA
from uses_indexer.strategy_config import (
    AnswerExecutionPolicy,
    AnswerStrategyConfig,
    PromptProfileConfig,
    QaPolicy,
)


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
    indexer = SQLiteIndexer(embedder=LocalHashedEmbedder())
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    return CodebaseAnswerer(qa=qa, llm=llm), db_path


def test_answer_uses_draft_when_llm_not_configured(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm(None))

    result = answerer.answer(db_path, "证券代码获取的逻辑在哪里", evidence_limit=2)

    assert result["answer_source"] == "draft"
    assert result["final_answer"]["source"] == "draft"
    assert result["final_answer"]["tier"] == "grounded_summary"
    assert result["final_answer"]["confidence"]["label"] in {"medium", "high"}
    assert result["final_answer"]["grounding"]["citations"]
    assert result["final_answer"]["grounding"]["citations"][0]["retrieval_source"]
    assert result["final_answer"]["grounding"]["primary_candidate"]
    assert "AF_SAMPLE" in result["final_answer"]["text"]


def test_answer_uses_llm_when_available(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm("这是模型生成的最终答案。"))

    result = answerer.answer(db_path, "证券代码获取的逻辑在哪里", evidence_limit=2)

    assert result["answer_source"] == "llm"
    assert result["final_answer"]["text"] == "这是模型生成的最终答案。"
    assert result["final_answer"]["used_model"] == "stub-model"
    assert result["final_answer"]["tier"] == "llm_grounded"
    assert result["final_answer"]["grounding"]["citations"]


def test_answer_strategy_adds_profile_metadata(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm("调用链答案"))

    result = answerer.answer(db_path, "AF_SAMPLE 被谁调用", evidence_limit=2)

    assert result["prompt_package"]["strategy_profile"] == "call_chain"
    assert "策略要求" in result["prompt_package"]["system_prompt"]
    assert result["prompt_package"]["question_plan"]["query_type"] == "callers"


def test_answer_strategy_uses_custom_profile_config(tmp_path: Path) -> None:
    strategy = AdaptiveAnswerStrategy(
        AnswerStrategyConfig(
            profiles={
                "call_chain": PromptProfileConfig("自定义调用链说明", 2, 500),
                "table_sql": PromptProfileConfig("自定义表说明", 2, 500),
                "default": PromptProfileConfig("默认说明", 2, 500),
            }
        )
    )
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")
    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer(embedder=LocalHashedEmbedder())
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer, policy=QaPolicy(evidence_limit=2, context_window=1, related_limit=1))
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm("调用链答案"), strategy=strategy)

    result = answerer.answer(db_path, "AF_SAMPLE 被谁调用")

    assert result["prompt_package"]["strategy_profile"] == "call_chain"
    assert "自定义调用链说明" in result["prompt_package"]["system_prompt"]


def test_answer_execution_policy_controls_fallback(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")
    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer(embedder=LocalHashedEmbedder())
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(
        qa=qa,
        llm=StubLlm(None),
        policy=AnswerExecutionPolicy(allow_draft_fallback=False),
    )

    try:
        answerer.answer(db_path, "证券代码获取的逻辑在哪里")
    except Exception as exc:  # pragma: no cover - explicit behavior assertion
        assert "allow_draft_fallback is false" in str(exc)
    else:  # pragma: no cover
        raise AssertionError("Expected fallback-disabled answer call to raise")


def test_answer_uses_guarded_draft_for_low_confidence_questions(tmp_path: Path) -> None:
    answerer, db_path = _build_answerer(tmp_path, llm=StubLlm("这是一条本不该被使用的模型答案。"))

    result = answerer.answer(db_path, "完全不存在的业务问题", evidence_limit=2)

    assert result["answer_source"] == "guarded_draft"
    assert result["final_answer"]["tier"] == "guarded_low_confidence"
    assert result["final_answer"]["review_required"] is True
    assert "当前证据不足" in result["final_answer"]["text"]
