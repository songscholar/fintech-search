from __future__ import annotations

from pathlib import Path

from .answer_strategy import AdaptiveAnswerStrategy
from .llm import LlmConfigError, LlmRequestError, OpenAICompatibleLlm
from .qa import CodebaseQA
from .response_schema import apply_response_envelope
from .strategy_config import AnswerExecutionPolicy


class CodebaseAnswerer:
    def __init__(
        self,
        qa: CodebaseQA | None = None,
        llm: OpenAICompatibleLlm | None = None,
        strategy: AdaptiveAnswerStrategy | None = None,
        policy: AnswerExecutionPolicy | None = None,
    ) -> None:
        self.qa = qa or CodebaseQA()
        self.llm = llm or OpenAICompatibleLlm.from_env()
        self.strategy = strategy or AdaptiveAnswerStrategy()
        self.policy = policy or AnswerExecutionPolicy()

    def answer(
        self,
        db_path: str | Path,
        question: str,
        *,
        evidence_limit: int | None = None,
        context_window: int | None = None,
        related_limit: int | None = None,
        allow_draft_fallback: bool | None = None,
    ) -> dict[str, object]:
        effective_allow_draft_fallback = (
            self.policy.allow_draft_fallback
            if allow_draft_fallback is None
            else allow_draft_fallback
        )
        qa_bundle = self.qa.ask(
            db_path,
            question,
            evidence_limit=evidence_limit,
            context_window=context_window,
            related_limit=related_limit,
        )

        prompt_package = self.strategy.build_prompt_package(qa_bundle)
        qa_bundle["prompt_package"] = prompt_package
        llm_enabled = self.llm.is_configured()
        draft_answer = dict(qa_bundle.get("draft_answer") or {})
        confidence = dict(draft_answer.get("confidence") or {})
        confidence_score = float(confidence.get("score") or 0.0)
        low_confidence = confidence_score < float(self.policy.low_confidence_threshold)
        review_required = bool(draft_answer.get("review_required"))

        if (low_confidence or (review_required and confidence_score < 0.65)) and self.policy.prefer_guarded_draft_on_low_confidence:
            guarded_text = self._build_guarded_low_confidence_answer(qa_bundle)
            return self._build_result(
                qa_bundle,
                answer_text=guarded_text,
                answer_source="guarded_draft",
                model_response=None,
                error=None,
            )

        if llm_enabled:
            try:
                llm_result = self.llm.complete(
                    system_prompt=str(prompt_package["system_prompt"]),
                    user_prompt=str(prompt_package["user_prompt"]),
                )
            except (LlmConfigError, LlmRequestError) as exc:
                if not effective_allow_draft_fallback:
                    raise
                return self._build_result(
                    qa_bundle,
                    answer_text=str(qa_bundle["draft_answer"]["answer"]),
                    answer_source="draft_fallback",
                    model_response=None,
                    error=str(exc),
                )

            return self._build_result(
                qa_bundle,
                answer_text=str(llm_result["content"]),
                answer_source="llm",
                model_response=llm_result,
                error=None,
            )

        if not effective_allow_draft_fallback:
            raise LlmConfigError(
                "LLM is not configured and allow_draft_fallback is false."
            )

        return self._build_result(
            qa_bundle,
            answer_text=str(qa_bundle["draft_answer"]["answer"]),
            answer_source="draft",
            model_response=None,
            error=None,
        )

    def _build_guarded_low_confidence_answer(self, qa_bundle: dict[str, object]) -> str:
        draft_answer = dict(qa_bundle.get("draft_answer") or {})
        supporting_locations = list(draft_answer.get("supporting_locations") or [])
        decision = dict(draft_answer.get("decision") or {})
        lead = supporting_locations[0] if supporting_locations else None
        lines = [
            "结论: 当前证据不足以支持一个高置信度的最终结论，下面只给出最可能的候选位置和明确的不确定点。",
        ]
        if lead:
            lines.append("候选位置:")
            lines.append(
                f"- {lead['procedure_name']} {lead['file_path']}:{lead['line_start']}-{lead['line_end']}"
            )
        uncertainties = list(draft_answer.get("uncertainties") or [])
        if uncertainties:
            lines.append("不确定点:")
            for item in uncertainties[:3]:
                lines.append(f"- {item}")
        if decision.get("conflict_summary"):
            lines.append("决策提示:")
            lines.append(f"- {decision['conflict_summary']}")
        if decision.get("recommendation"):
            lines.append("处理建议:")
            lines.append(f"- {decision['recommendation']}")
        if decision.get("evidence_alignment"):
            lines.append("证据一致性:")
            lines.append(f"- {decision['evidence_alignment']}")
        secondary_candidates = list(draft_answer.get("secondary_candidates") or [])
        if secondary_candidates:
            lines.append("其他近似候选:")
            for item in secondary_candidates[:2]:
                lines.append(
                    f"- {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}"
                )
        lines.append("建议:")
        lines.append("- 继续查看主候选过程的上下游调用、相关表访问和失败处理分支。")
        return "\n".join(lines)

    def _build_result(
        self,
        qa_bundle: dict[str, object],
        *,
        answer_text: str,
        answer_source: str,
        model_response: dict[str, object] | None,
        error: str | None,
    ) -> dict[str, object]:
        result = dict(qa_bundle)
        draft_answer = dict(qa_bundle.get("draft_answer") or {})
        evidence = list(qa_bundle.get("evidence") or [])
        citations = [
            {
                "rank": int(item["rank"]),
                "procedure_name": str(item["procedure_name"]),
                "file_path": str(item["file_path"]),
                "line_start": int(item["line_start"]),
                "line_end": int(item["line_end"]),
                "matched_text": str(item["matched_text"]),
                "retrieval_source": str(item["retrieval_source"]),
                "match_source": str(item["match_source"]),
            }
            for item in evidence[:3]
        ]
        result["answer_source"] = answer_source
        result["final_answer"] = {
            "text": answer_text,
            "source": answer_source,
            "tier": (
                "guarded_low_confidence"
                if answer_source == "guarded_draft"
                else draft_answer.get("tier") if answer_source != "llm" else "llm_grounded"
            ),
            "confidence": draft_answer.get("confidence"),
            "grounding": {
                "citations": citations,
                "supporting_locations": list(draft_answer.get("supporting_locations") or []),
                "primary_candidate": dict(draft_answer.get("primary_candidate") or {}),
                "secondary_candidates": list(draft_answer.get("secondary_candidates") or []),
                "uncertainties": list(draft_answer.get("uncertainties") or []),
                "decision": dict(draft_answer.get("decision") or {}),
            },
            "review_required": answer_source == "guarded_draft" or bool(draft_answer.get("review_required")),
            "used_model": model_response["model"] if model_response else None,
            "provider": model_response["provider"] if model_response else None,
            "error": error,
        }
        if model_response:
            result["model_response"] = {
                "provider": model_response["provider"],
                "model": model_response["model"],
                "base_url": model_response["base_url"],
            }
        return apply_response_envelope(result, kind="answer")
