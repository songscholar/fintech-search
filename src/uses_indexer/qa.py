from __future__ import annotations

from collections import OrderedDict
from pathlib import Path

from .indexer import SQLiteIndexer
from .rerank import analyze_query
from .response_schema import apply_response_envelope
from .strategy_config import QaPolicy


SYSTEM_PROMPT = """你是一个面向 USES/UFT DSL 代码库的问答助手。

回答时必须遵守这些规则：
1. 只能基于给定证据回答，不要编造仓库中不存在的实现。
2. 先给结论，再给证据文件和行号。
3. 如果存在多个候选实现，要明确说明主候选和次候选。
4. 如果证据不足，要直接说明不确定点。
5. 回答尽量简洁，但要保留文件路径、过程名和关键条件。
"""


ANSWER_FORMAT = """请按下面结构回答：

结论:
- 用简洁中文概括这个问题最可能对应的实现位置和逻辑。

证据:
- 列出 1 到 3 个最关键的过程、文件路径和行号。

推断:
- 用 2 到 4 句说明为什么这些证据能回答问题。

不确定点:
- 如果有证据不足、存在多个候选或需要继续深挖的地方，请明确写出。
"""


class CodebaseQA:
    def __init__(self, indexer: SQLiteIndexer | None = None, policy: QaPolicy | None = None) -> None:
        self.indexer = indexer or SQLiteIndexer()
        self.policy = policy or QaPolicy()

    def ask(
        self,
        db_path: str | Path,
        question: str,
        *,
        evidence_limit: int | None = None,
        context_window: int | None = None,
        related_limit: int | None = None,
    ) -> dict[str, object]:
        effective_evidence_limit = evidence_limit or self.policy.evidence_limit
        effective_context_window = context_window if context_window is not None else self.policy.context_window
        effective_related_limit = related_limit if related_limit is not None else self.policy.related_limit
        evidence_bundle = self.indexer.assemble_evidence(
            db_path,
            question,
            limit=effective_evidence_limit,
            context_window=effective_context_window,
            related_limit=effective_related_limit,
        )

        prompt_package = {
            "system_prompt": SYSTEM_PROMPT,
            "answer_format": ANSWER_FORMAT,
            "user_prompt": self._build_user_prompt(question, str(evidence_bundle["llm_context"])),
        }

        return apply_response_envelope({
            "db_path": str(db_path),
            "question": question,
            "qa_policy": {
                "evidence_limit": effective_evidence_limit,
                "context_window": effective_context_window,
                "related_limit": effective_related_limit,
            },
            "evidence_count": evidence_bundle["evidence_count"],
            "evidence": evidence_bundle["evidence"],
            "llm_context": evidence_bundle["llm_context"],
            "prompt_package": prompt_package,
            "draft_answer": self._build_draft_answer(question, evidence_bundle["evidence"]),
        }, kind="ask")

    def _build_user_prompt(self, question: str, llm_context: str) -> str:
        return "\n".join(
            [
                f"用户问题: {question}",
                "",
                ANSWER_FORMAT.strip(),
                "",
                "以下是可用证据：",
                llm_context,
            ]
        )

    def _build_draft_answer(self, question: str, evidence: list[dict[str, object]]) -> dict[str, object]:
        question_analysis = analyze_query(question)
        query_type = str(question_analysis.get("query_type") or "location")
        if not evidence:
            return {
                "status": "insufficient_evidence",
                "answer": "当前索引库里没有检索到足够直接的证据，暂时无法可靠回答这个问题。",
                "summary_points": [],
                "supporting_locations": [],
                "uncertainties": ["未命中可直接支撑该问题的过程或语句，需要换关键词或补充向量检索。"],
                "tier": "retrieval_only",
                "query_type": query_type,
                "confidence": {"score": 0.1, "label": "low"},
            }

        top_evidence = evidence[:3]
        top_locations = []
        unique_locations: OrderedDict[tuple[str, int, int], dict[str, object]] = OrderedDict()
        for item in top_evidence:
            key = (str(item["file_path"]), int(item["line_start"]), int(item["line_end"]))
            unique_locations.setdefault(
                key,
                {
                    "procedure_name": item["procedure_name"],
                    "file_path": item["file_path"],
                    "line_start": item["line_start"],
                    "line_end": item["line_end"],
                    "matched_text": item["matched_text"],
                },
            )
        top_locations = list(unique_locations.values())

        lead = top_evidence[0]
        lead_desc = (
            f"最直接的证据位于过程 {lead['procedure_name']}，"
            f"文件 {lead['file_path']} 的 {lead['line_start']}-{lead['line_end']} 行附近。"
        )

        summary_points = [lead_desc]
        for item in top_evidence[1:]:
            summary_points.append(
                f"另一个候选过程是 {item['procedure_name']}，命中的关键文本是 {item['matched_text']}。"
            )

        related_hints = []
        for item in top_evidence:
            related = item.get("related_context", {})
            outgoing_calls = related.get("outgoing_calls") or []
            related_tables = related.get("related_tables") or []
            if outgoing_calls:
                related_hints.append(
                    f"{item['procedure_name']} 还关联调用 {', '.join(outgoing_calls[:3])}。"
                )
            if related_tables:
                table_desc = ", ".join(
                    f"{table['edge_type']}:{table['name']}"
                    for table in related_tables[:3]
                )
                related_hints.append(f"{item['procedure_name']} 涉及表访问 {table_desc}。")

        answer_lines = [f"结论: 围绕“{question}”，当前索引最优先命中的实现位置是 {lead['procedure_name']}。"]
        if query_type in {"callers", "callees"}:
            answer_lines.append("主调用链:")
        elif query_type in {"table_write", "table_read"}:
            answer_lines.append("表访问:")
        elif query_type == "failure_flow":
            answer_lines.append("失败处理路径:")
        elif query_type in {"variable_write", "variable_read", "variable"}:
            answer_lines.append("变量流向:")
        elif query_type == "metadata":
            answer_lines.append("元数据关系:")
        elif query_type == "topic":
            answer_lines.append("主题关系:")
        else:
            answer_lines.append("实现位置:")
        for line in summary_points:
            answer_lines.append(f"- {line}")
        for line in related_hints[:2]:
            answer_lines.append(f"- {line}")
        answer_lines.append("关键证据:")
        for item in top_locations:
            answer_lines.append(
                f"- {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}"
            )

        uncertainties = []
        if len(top_evidence) > 1:
            uncertainties.append("仓库里存在多个相近候选过程，最终答案可能依赖具体业务场景。")
        if not related_hints:
            uncertainties.append("当前证据主要来自直接命中语句，尚未展开更深层调用链。")
        if uncertainties:
            answer_lines.append("不确定点:")
            for item in uncertainties:
                answer_lines.append(f"- {item}")

        confidence = self._estimate_confidence(top_evidence, related_hints, uncertainties)
        return {
            "status": "ok",
            "answer": "\n".join(answer_lines),
            "summary_points": summary_points + related_hints[:2],
            "supporting_locations": top_locations,
            "uncertainties": uncertainties,
            "tier": "grounded_summary",
            "query_type": query_type,
            "confidence": confidence,
        }

    def _estimate_confidence(
        self,
        evidence: list[dict[str, object]],
        related_hints: list[str],
        uncertainties: list[str],
    ) -> dict[str, object]:
        score = 0.35 + min(len(evidence), 3) * 0.15
        if related_hints:
            score += 0.1
        if uncertainties:
            score -= min(len(uncertainties), 2) * 0.08
        score = max(0.1, min(round(score, 2), 0.95))
        if score >= 0.75:
            label = "high"
        elif score >= 0.55:
            label = "medium"
        else:
            label = "low"
        return {"score": score, "label": label}
