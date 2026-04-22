from __future__ import annotations

from dataclasses import dataclass

from .rerank import analyze_query
from .strategy_config import AnswerStrategyConfig

@dataclass(frozen=True, slots=True)
class PromptProfile:
    name: str
    guidance: str
    max_evidence_blocks: int
    max_context_chars: int
    answer_sections: tuple[str, ...]


class AdaptiveAnswerStrategy:
    def __init__(self, config: AnswerStrategyConfig | None = None) -> None:
        self.config = config or AnswerStrategyConfig()

    def select_profile(self, question: str) -> PromptProfile:
        query_type = str(analyze_query(question).get("query_type") or "location")
        profile_name = {
            "callers": "call_chain",
            "callees": "call_chain",
            "table_write": "table_sql",
            "table_read": "table_sql",
            "failure_flow": "failure_flow",
            "variable_write": "variable_flow",
            "variable_read": "variable_flow",
            "variable": "variable_flow",
            "metadata": "metadata",
            "topic": "topic",
            "procedure": "procedure_lookup",
            "location": "procedure_lookup",
        }.get(query_type, "default")
        return self._named_profile(profile_name)

    def build_question_plan(self, question: str, profile: PromptProfile) -> dict[str, object]:
        query_analysis = analyze_query(question)
        return {
            "query_type": str(query_analysis.get("query_type") or "location"),
            "intents": list(query_analysis.get("intents") or []),
            "focus_terms": list(query_analysis.get("focus_terms") or []),
            "answer_sections": list(profile.answer_sections),
            "grounding_requirements": [
                "必须引用过程名、文件路径和行号。",
                "只基于 evidence 中出现的实现和关系作答。",
                "如果多个候选同时成立，要区分主候选和次候选。",
            ],
        }

    def build_prompt_package(self, qa_bundle: dict[str, object]) -> dict[str, object]:
        question = str(qa_bundle["question"])
        profile = self.select_profile(question)
        question_plan = self.build_question_plan(question, profile)
        base_prompt = dict(qa_bundle["prompt_package"])
        llm_context = str(qa_bundle["llm_context"])
        compressed_context = self._compress_context(
            llm_context=llm_context,
            evidence=list(qa_bundle["evidence"]),
            profile=profile,
            question_plan=question_plan,
        )
        base_prompt["system_prompt"] = (
            f"{base_prompt['system_prompt']}\n\n"
            f"当前回答策略: {profile.name}\n"
            f"策略要求: {profile.guidance}\n"
            f"回答分段: {' / '.join(profile.answer_sections)}"
        )
        base_prompt["user_prompt"] = (
            f"用户问题: {question}\n\n"
            f"问题类型: {question_plan['query_type']}\n"
            f"回答关注点: {', '.join(question_plan['answer_sections'])}\n\n"
            f"{base_prompt['answer_format'].strip()}\n\n"
            f"以下是可用证据：\n{compressed_context}"
        )
        base_prompt["strategy_profile"] = profile.name
        base_prompt["question_plan"] = question_plan
        base_prompt["compressed_llm_context"] = compressed_context
        return base_prompt

    def _compress_context(
        self,
        *,
        llm_context: str,
        evidence: list[dict[str, object]],
        profile: PromptProfile,
        question_plan: dict[str, object],
    ) -> str:
        if len(llm_context) <= profile.max_context_chars and len(evidence) <= profile.max_evidence_blocks:
            return llm_context

        query_type = str(question_plan.get("query_type") or "location")
        ranked_evidence = sorted(
            evidence,
            key=lambda item: self._evidence_priority(query_type, item),
            reverse=True,
        )
        selected: list[dict[str, object]] = []
        seen_locations: set[tuple[str, int, int]] = set()
        seen_procedures: dict[str, int] = {}
        for item in ranked_evidence:
            key = (str(item["file_path"]), int(item["line_start"]), int(item["line_end"]))
            if key in seen_locations:
                continue
            procedure_name = str(item["procedure_name"])
            if seen_procedures.get(procedure_name, 0) >= 2:
                continue
            seen_locations.add(key)
            seen_procedures[procedure_name] = seen_procedures.get(procedure_name, 0) + 1
            selected.append(item)
            if len(selected) >= profile.max_evidence_blocks:
                break
        lines = []
        for item in selected:
            related = dict(item.get("related_context") or {})
            relation_lines: list[str] = []
            evidence_strength = self._evidence_strength(query_type, item)
            if question_plan["query_type"] in {"callers", "callees"} and related.get("outgoing_calls"):
                relation_lines.append(f"Call chain: {', '.join(str(name) for name in related['outgoing_calls'][:4])}")
            if question_plan["query_type"] in {"table_write", "table_read"} and related.get("related_tables"):
                relation_lines.append(
                    "Tables: " + ", ".join(
                        f"{table['edge_type']}:{table['name']}"
                        for table in related["related_tables"][:4]
                    )
                )
            if question_plan["query_type"] == "failure_flow" and related.get("control_flow"):
                relation_lines.append(
                    "Failure flow: " + ", ".join(
                        f"{item['edge_type']}:{item['target_name']}"
                        for item in related["control_flow"][:4]
                    )
                )
            if question_plan["query_type"] == "metadata" and related.get("metadata_relations"):
                relation_lines.append(
                    "Metadata: " + ", ".join(
                        f"{item['edge_type']}:{item['target_name']}"
                        for item in related["metadata_relations"][:4]
                    )
                )
            lines.extend(
                [
                    f"[Evidence {item['rank']}] {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}",
                    f"Evidence strength: {evidence_strength}",
                    f"Matched text: {item['matched_text']}",
                    f"Why relevant: {', '.join(item['reasons'][:4])}",
                    f"Snippet: {str(item['excerpt'])[:400]}",
                    *relation_lines,
                    "",
                ]
            )
        compressed = "\n".join(lines).strip()
        if len(compressed) > profile.max_context_chars:
            return compressed[: profile.max_context_chars - 3].rstrip() + "..."
        return compressed

    def _evidence_priority(self, query_type: str, item: dict[str, object]) -> tuple[float, float, int]:
        retrieval_source = str(item.get("retrieval_source") or "")
        match_source = str(item.get("match_source") or "")
        hit_type = str(item.get("hit_type") or "")
        score = float(item.get("score") or 0.0)
        direct_bonus = 0.0

        if query_type in {"callers", "callees"} and retrieval_source == "relation_call_edge":
            direct_bonus += 40.0
        if query_type in {"table_write", "table_read"} and retrieval_source == "relation_table_edge":
            direct_bonus += 38.0
        if query_type in {"variable_write", "variable_read", "variable"} and match_source == "assignment":
            direct_bonus += 42.0
        elif query_type in {"variable_write", "variable_read", "variable"} and retrieval_source == "relation_variable_edge":
            direct_bonus += 30.0
        if query_type == "failure_flow" and retrieval_source == "relation_failure_block":
            direct_bonus += 40.0
        elif query_type == "failure_flow" and hit_type == "block":
            direct_bonus += 26.0
        if retrieval_source.startswith("fts_block"):
            direct_bonus += 8.0

        return (direct_bonus + score, score, -int(item.get("rank") or 0))

    def _evidence_strength(self, query_type: str, item: dict[str, object]) -> str:
        retrieval_source = str(item.get("retrieval_source") or "")
        match_source = str(item.get("match_source") or "")
        hit_type = str(item.get("hit_type") or "")
        if query_type in {"variable_write", "variable_read", "variable"} and match_source == "assignment":
            return "direct_assignment"
        if retrieval_source in {
            "relation_call_edge",
            "relation_table_edge",
            "relation_variable_edge",
            "relation_failure_block",
        }:
            return "direct_relation"
        if hit_type == "block":
            return "structural_block"
        return "contextual"

    def _named_profile(self, name: str) -> PromptProfile:
        config = self.config.profile(name)
        return PromptProfile(
            name=name,
            guidance=config.guidance,
            max_evidence_blocks=config.max_evidence_blocks,
            max_context_chars=config.max_context_chars,
            answer_sections=config.answer_sections,
        )
