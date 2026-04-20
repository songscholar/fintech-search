from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PromptProfile:
    name: str
    guidance: str
    max_evidence_blocks: int
    max_context_chars: int


class AdaptiveAnswerStrategy:
    def select_profile(self, question: str) -> PromptProfile:
        lowered = question.lower()
        if any(token in lowered for token in ("调用链", "谁调用", "被谁调用", "上游", "下游")):
            return PromptProfile(
                name="call_chain",
                guidance="重点解释调用入口、调用方向、主候选链路和可能的上游/下游过程。",
                max_evidence_blocks=5,
                max_context_chars=10000,
            )
        if any(token in lowered for token in ("sql", "表", "数据库", "查询", "读取", "update", "insert", "delete", "merge")):
            return PromptProfile(
                name="table_sql",
                guidance="重点解释表访问、读写方向、SQL 语义和关联过程。",
                max_evidence_blocks=6,
                max_context_chars=12000,
            )
        return PromptProfile(
            name="default",
            guidance="先给结论，再给证据和不确定点，避免展开与问题无关的背景。",
            max_evidence_blocks=6,
            max_context_chars=12000,
        )

    def build_prompt_package(self, qa_bundle: dict[str, object]) -> dict[str, object]:
        question = str(qa_bundle["question"])
        profile = self.select_profile(question)
        base_prompt = dict(qa_bundle["prompt_package"])
        llm_context = str(qa_bundle["llm_context"])
        compressed_context = self._compress_context(
            llm_context=llm_context,
            evidence=list(qa_bundle["evidence"]),
            profile=profile,
        )
        base_prompt["system_prompt"] = (
            f"{base_prompt['system_prompt']}\n\n"
            f"当前回答策略: {profile.name}\n"
            f"策略要求: {profile.guidance}"
        )
        base_prompt["user_prompt"] = (
            f"用户问题: {question}\n\n"
            f"{base_prompt['answer_format'].strip()}\n\n"
            f"以下是可用证据：\n{compressed_context}"
        )
        base_prompt["strategy_profile"] = profile.name
        base_prompt["compressed_llm_context"] = compressed_context
        return base_prompt

    def _compress_context(
        self,
        *,
        llm_context: str,
        evidence: list[dict[str, object]],
        profile: PromptProfile,
    ) -> str:
        if len(llm_context) <= profile.max_context_chars and len(evidence) <= profile.max_evidence_blocks:
            return llm_context

        selected = evidence[: profile.max_evidence_blocks]
        lines = []
        for item in selected:
            lines.extend(
                [
                    f"[Evidence {item['rank']}] {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}",
                    f"Matched text: {item['matched_text']}",
                    f"Why relevant: {', '.join(item['reasons'][:4])}",
                    f"Snippet: {str(item['excerpt'])[:400]}",
                    "",
                ]
            )
        compressed = "\n".join(lines).strip()
        if len(compressed) > profile.max_context_chars:
            return compressed[: profile.max_context_chars - 3].rstrip() + "..."
        return compressed
