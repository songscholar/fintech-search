from __future__ import annotations

from pathlib import Path

from .answer_strategy import AdaptiveAnswerStrategy
from .llm import LlmConfigError, LlmRequestError, OpenAICompatibleLlm
from .qa import CodebaseQA
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
        result["answer_source"] = answer_source
        result["final_answer"] = {
            "text": answer_text,
            "source": answer_source,
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
        return result
