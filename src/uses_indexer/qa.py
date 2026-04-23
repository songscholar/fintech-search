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


QUERY_SECTION_LABELS = {
    "implementation_location": "实现位置",
    "location": "实现位置",
    "callers": "上游调用",
    "callees": "下游调用",
    "table_write": "表写入",
    "table_read": "表读取",
    "table_access": "表访问",
    "variable_write": "变量写入",
    "variable_read": "变量读取",
    "variable_flow": "变量链路",
    "metadata_definition": "Metadata 定义",
    "topic_publish": "Topic 发布",
    "failure_flow": "失败处理路径",
}


LEAD_SUMMARY_LABELS = {
    "implementation_location": "最可能的实现过程",
    "location": "最可能的实现过程",
    "callers": "最关键的上游调用过程",
    "callees": "最关键的下游调用过程",
    "table_write": "最关键的表写入过程",
    "table_read": "最关键的表读取过程",
    "table_access": "最关键的表访问过程",
    "variable_write": "最关键的变量写入过程",
    "variable_read": "最关键的变量读取过程",
    "variable_flow": "最关键的变量链路过程",
    "metadata_definition": "最关键的 metadata 定义过程",
    "topic_publish": "最关键的 topic 发布过程",
    "failure_flow": "最关键的失败处理过程",
}


QUERY_SUMMARY_HINT_LABELS = {
    "table_write": "表写入重点",
    "table_read": "表读取重点",
    "table_access": "表访问重点",
    "variable_write": "变量写入重点",
    "variable_read": "变量读取重点",
    "variable_flow": "变量链路重点",
    "metadata_definition": "metadata 定义重点",
    "topic_publish": "topic 发布重点",
    "callers": "上游调用重点",
    "callees": "下游调用重点",
}


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
        if self._should_discard_weak_evidence(evidence_bundle["evidence"]):
            evidence_bundle = {
                **evidence_bundle,
                "evidence_count": 0,
                "evidence": [],
                "llm_context": "当前没有检索到足够直接的代码证据。",
            }

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

    def _should_discard_weak_evidence(self, evidence: list[dict[str, object]]) -> bool:
        if not evidence:
            return False

        strongest_similarity = 0.0
        for item in evidence:
            matched_via = {
                str(value)
                for value in (item.get("matched_via") or [item.get("retrieval_source")])
                if str(value)
            }
            if not matched_via or matched_via - {"vector_chunk"}:
                return False
            for reason in item.get("reasons") or []:
                text = str(reason)
                if text.startswith("vector_similarity="):
                    try:
                        strongest_similarity = max(strongest_similarity, float(text.split("=", 1)[1]))
                    except ValueError:
                        continue

        return strongest_similarity < 0.2

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
        top_unique_evidence: list[dict[str, object]] = []
        seen_candidates: set[tuple[str, str, int, int]] = set()
        for item in evidence:
            key = (
                str(item["procedure_name"]),
                str(item["file_path"]),
                int(item["line_start"]),
                int(item["line_end"]),
            )
            if key in seen_candidates:
                continue
            seen_candidates.add(key)
            top_unique_evidence.append(item)
            if len(top_unique_evidence) >= 3:
                break
        if top_unique_evidence:
            top_evidence = top_unique_evidence
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
        path_hints = []
        bridge_candidates: list[str] = []
        failure_hints: list[str] = []
        flow_path_hints: list[str] = []
        support_flow_path_hints: list[str] = []
        retrieval_sources = {str(item.get("retrieval_source") or "") for item in top_evidence}

        candidate_groups: OrderedDict[tuple[str, str], dict[str, object]] = OrderedDict()
        for item in top_evidence:
            group_key = (str(item["procedure_name"]), str(item["file_path"]))
            group = candidate_groups.setdefault(
                group_key,
                {
                    "procedure_name": item["procedure_name"],
                    "file_path": item["file_path"],
                    "line_start": item["line_start"],
                    "line_end": item["line_end"],
                    "retrieval_source": item["retrieval_source"],
                    "match_source": item["match_source"],
                    "procedure_profile": dict(item.get("procedure_profile") or {}),
                    "aggregate_score": 0.0,
                    "best_item_score": -1.0,
                    "matched_via": set(),
                    "sources": set(),
                },
            )
            group["aggregate_score"] = float(group["aggregate_score"]) + float(item.get("score") or 0.0)
            group["matched_via"].update(item.get("matched_via") or [item["retrieval_source"]])
            group["sources"].add(str(item["retrieval_source"]))
            if float(item.get("score") or 0.0) >= float(group["best_item_score"]):
                group["best_item_score"] = float(item.get("score") or 0.0)
                group["line_start"] = item["line_start"]
                group["line_end"] = item["line_end"]
                group["retrieval_source"] = item["retrieval_source"]
                group["match_source"] = item["match_source"]
                group["procedure_profile"] = dict(item.get("procedure_profile") or {})

        grouped_candidates = sorted(
            candidate_groups.values(),
            key=lambda item: (-float(item["aggregate_score"]), str(item["procedure_name"]), str(item["file_path"])),
        )
        lead_group = grouped_candidates[0]
        lead = next(
            (
                item
                for item in top_evidence
                if str(item["procedure_name"]) == str(lead_group["procedure_name"])
                and str(item["file_path"]) == str(lead_group["file_path"])
            ),
            top_evidence[0],
        )
        primary_candidate = {
            "procedure_name": lead_group["procedure_name"],
            "file_path": lead_group["file_path"],
            "line_start": lead_group["line_start"],
            "line_end": lead_group["line_end"],
            "retrieval_source": lead_group["retrieval_source"],
            "match_source": lead_group["match_source"],
            "procedure_profile": dict(lead_group.get("procedure_profile") or {}),
            "aggregate_score": round(float(lead_group["aggregate_score"]), 3),
            "matched_via": sorted(str(item) for item in lead_group.get("matched_via", set())),
        }
        secondary_candidates = [
            {
                "procedure_name": item["procedure_name"],
                "file_path": item["file_path"],
                "line_start": item["line_start"],
                "line_end": item["line_end"],
                "retrieval_source": item["retrieval_source"],
                "match_source": item["match_source"],
                "procedure_profile": dict(item.get("procedure_profile") or {}),
                "aggregate_score": round(float(item["aggregate_score"]), 3),
                "matched_via": sorted(str(value) for value in item.get("matched_via", set())),
            }
            for item in grouped_candidates[1:3]
        ]
        lead_label = LEAD_SUMMARY_LABELS.get(query_type, "最直接的证据过程")
        lead_desc = (
            f"{lead_label}是 {lead['procedure_name']}，"
            f"文件 {lead['file_path']} 的 {lead['line_start']}-{lead['line_end']} 行附近。"
        )

        summary_points = [lead_desc]
        query_specific_summary = self._build_query_specific_summary(
            query_type=query_type,
            primary_candidate=primary_candidate,
        )
        if query_specific_summary:
            summary_points.append(query_specific_summary)
        profile_hints: list[str] = []
        graph_hints: list[str] = []
        for item in top_evidence[1:]:
            summary_points.append(
                f"另一个候选过程是 {item['procedure_name']}，命中的关键文本是 {item['matched_text']}。"
            )

        related_hints = []
        for item in top_evidence:
            related = item.get("related_context", {})
            outgoing_calls = related.get("outgoing_calls") or []
            related_tables = related.get("related_tables") or []
            if "feature_call_bridge" in item.get("reasons", []):
                bridge_candidates.append(str(item["procedure_name"]))
            path_reason = next(
                (
                    str(reason)
                    for reason in item.get("reasons", [])
                    if str(reason).startswith("path_bridge=")
                ),
                "",
            )
            if path_reason:
                path_value = path_reason.removeprefix("path_bridge=")
                path_hints.append(
                    "调用链桥接路径为 "
                    + path_value
                    + "。"
                )
                path_steps = [step.strip() for step in path_value.split("->") if step.strip()]
                if len(path_steps) > 2:
                    bridge_candidates.extend(path_steps[1:-1])
            table_flow_path_reason = next(
                (
                    str(reason)
                    for reason in item.get("reasons", [])
                    if str(reason).startswith("table_flow_path=")
                ),
                "",
            )
            if table_flow_path_reason:
                hint = "表访问链路为 " + table_flow_path_reason.removeprefix("table_flow_path=") + "。"
                if "table_flow_priority=main" in item.get("reasons", []):
                    flow_path_hints.append(hint)
                else:
                    support_flow_path_hints.append(hint)
            variable_flow_path_reason = next(
                (
                    str(reason)
                    for reason in item.get("reasons", [])
                    if str(reason).startswith("variable_flow_path=")
                ),
                "",
            )
            if variable_flow_path_reason:
                hint = "变量链路为 " + variable_flow_path_reason.removeprefix("variable_flow_path=") + "。"
                if "variable_flow_priority=main" in item.get("reasons", []):
                    flow_path_hints.append(hint)
                else:
                    support_flow_path_hints.append(hint)
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
            profile = dict(item.get("procedure_profile") or {})
            if query_type in {"table_write", "table_read", "table_access"} and (profile.get("core_write_tables") or profile.get("core_read_tables")):
                table_names = list(profile.get("core_write_tables") or []) or list(profile.get("core_read_tables") or [])
                profile_hints.append(
                    f"{item['procedure_name']} 的核心表访问包括 {', '.join(str(name) for name in table_names[:3])}。"
                )
            if query_type in {"variable_write", "variable_read", "variable_flow"} and profile.get("core_variable_writes"):
                profile_hints.append(
                    f"{item['procedure_name']} 的主要变量写入包括 {', '.join(str(name) for name in profile.get('core_variable_writes')[:3])}。"
                )
            if query_type == "metadata_definition" and str(profile.get("metadata_role") or "") == "referencer":
                refs = ", ".join(str(name) for name in (profile.get("core_metadata_refs") or [])[:3])
                profile_hints.append(
                    f"{item['procedure_name']} 属于 metadata 引用过程。"
                    + (f" 核心 metadata 引用包括 {refs}。" if refs else "")
                )
            if query_type == "topic_publish" and str(profile.get("topic_role") or "") == "publisher":
                topics = ", ".join(str(name) for name in (profile.get("core_topics") or [])[:3])
                profile_hints.append(
                    f"{item['procedure_name']} 属于 topic 发布过程。"
                    + (f" 发布主题包括 {topics}。" if topics else "")
                )
            if str(item.get("retrieval_source") or "") == "relation_graph_profile":
                graph_focus_value = str(item.get("graph_focus_value") or "")
                graph_focus_role = str(item.get("graph_focus_role") or "")
                if graph_focus_value:
                    graph_hints.append(
                        f"{item['procedure_name']} 的结构化关系图显示 {graph_focus_value}"
                        + (f" 角色为 {graph_focus_role}。" if graph_focus_role else "。")
                    )
            if query_type == "failure_flow":
                recovered_blocks = list(item.get("recovered_blocks") or [])
                failure_blocks = [
                    str(block.get("block_type") or "")
                    for block in recovered_blocks
                    if str(block.get("block_type") or "") in {"failure_handler", "exception_handler", "when_others_handler"}
                ]
                if failure_blocks:
                    failure_hints.append(
                        f"{item['procedure_name']} 覆盖失败处理块 {', '.join(dict.fromkeys(failure_blocks))}。"
                    )

        if not graph_hints:
            lead_profile = dict(primary_candidate.get("procedure_profile") or {})
            relation_graph = dict(lead_profile.get("relation_graph") or {})
            fallback_hint = ""
            if query_type in {"variable_write", "variable_read", "variable_flow"}:
                variable_terms = [str(term).lower() for term in (question_analysis.get("variable_terms") or []) if str(term).strip()]
                for item in relation_graph.get("variables") or []:
                    name = str(item.get("name") or "")
                    role = str(item.get("role") or "")
                    if not name:
                        continue
                    if variable_terms and not any(term in name.lower() for term in variable_terms):
                        continue
                    fallback_hint = (
                        f"{primary_candidate['procedure_name']} 的结构化关系图显示 {name}"
                        + (f" 角色为 {role}。" if role else "。")
                    )
                    break
            elif query_type in {"table_write", "table_read", "table_access"}:
                table_terms = [str(term).lower() for term in (question_analysis.get("table_terms") or []) if str(term).strip()]
                for item in relation_graph.get("tables") or []:
                    name = str(item.get("name") or "")
                    role = str(item.get("role") or "")
                    if not name:
                        continue
                    if table_terms and not any(term in name.lower() for term in table_terms):
                        continue
                    fallback_hint = (
                        f"{primary_candidate['procedure_name']} 的结构化关系图显示 {name}"
                        + (f" 角色为 {role}。" if role else "。")
                    )
                    break
            if fallback_hint:
                graph_hints.append(fallback_hint)

        answer_lines = [f"结论: 围绕“{question}”，当前索引最优先命中的实现位置是 {lead['procedure_name']}。"]
        section_label = QUERY_SECTION_LABELS.get(query_type, "实现位置")
        if query_type in {"callers", "callees"}:
            answer_lines.append(f"{section_label}:")
        elif query_type in {"table_write", "table_read", "table_access"}:
            answer_lines.append(f"{section_label}:")
        elif query_type == "failure_flow":
            answer_lines.append("失败处理路径:")
        elif query_type in {"variable_write", "variable_read", "variable_flow"}:
            answer_lines.append(f"{section_label}:")
        elif query_type in {"metadata_definition", "topic_publish"}:
            answer_lines.append(f"{section_label}:")
        else:
            answer_lines.append(f"{section_label}:")
        for line in summary_points:
            answer_lines.append(f"- {line}")
        for line in failure_hints[:2]:
            answer_lines.append(f"- {line}")
        for line in profile_hints[:2]:
            answer_lines.append(f"- {line}")
        for line in graph_hints[:1]:
            answer_lines.append(f"- {line}")
        for line in related_hints[:2]:
            answer_lines.append(f"- {line}")
        answer_lines.append("关键证据:")
        for item in top_locations:
            answer_lines.append(
                f"- {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}"
            )
        answer_lines.append("主候选:")
        answer_lines.append(
            f"- {primary_candidate['procedure_name']} {primary_candidate['file_path']}:{primary_candidate['line_start']}-{primary_candidate['line_end']}"
        )
        if secondary_candidates:
            answer_lines.append("次候选:")
            for item in secondary_candidates[:2]:
                answer_lines.append(
                    f"- {item['procedure_name']} {item['file_path']}:{item['line_start']}-{item['line_end']}"
                )

        uncertainties = []
        if len(top_evidence) > 1:
            uncertainties.append("仓库里存在多个相近候选过程，最终答案可能依赖具体业务场景。")
        if not related_hints:
            uncertainties.append("当前证据主要来自直接命中语句，尚未展开更深层调用链。")
        if query_type in {"callers", "callees"} and "relation_path_bridge" not in retrieval_sources and "relation_multi_hop_context" not in retrieval_sources:
            uncertainties.append("当前调用链回答主要基于直连命中，尚未形成更完整的桥接路径证据。")
        if query_type == "failure_flow" and "relation_failure_block" not in retrieval_sources and not failure_hints:
            uncertainties.append("当前失败路径回答缺少直接的失败处理块证据，需要继续检查异常分支和报错语句。")
        if bridge_candidates:
            bridge_label = "、".join(dict.fromkeys(bridge_candidates))
            summary_points.append(f"桥接候选过程: {bridge_label}。")
        if failure_hints:
            summary_points.extend(failure_hints[:1])
        if uncertainties:
            answer_lines.append("不确定点:")
            for item in uncertainties:
                answer_lines.append(f"- {item}")
        if support_flow_path_hints:
            answer_lines.append("辅助链路:")
            for item in support_flow_path_hints[:2]:
                answer_lines.append(f"- {item}")

        confidence = self._estimate_confidence(
            top_evidence,
            related_hints,
            uncertainties,
            query_type=query_type,
            failure_hints=failure_hints,
            secondary_candidates=secondary_candidates,
            primary_candidate=primary_candidate,
        )
        prioritized_hints = [*path_hints, *flow_path_hints, *graph_hints, *profile_hints, *related_hints]
        review_required = self._should_require_review(
            query_type=query_type,
            primary_candidate=primary_candidate,
            secondary_candidates=secondary_candidates,
            confidence=confidence,
        )
        decision = self._build_decision(
            query_type=query_type,
            primary_candidate=primary_candidate,
            secondary_candidates=secondary_candidates,
            confidence=confidence,
            review_required=review_required,
        )
        if decision.get("conflict_summary"):
            uncertainties.append(str(decision["conflict_summary"]))
        return {
            "status": "ok",
            "answer": "\n".join(answer_lines),
            "summary_points": summary_points + prioritized_hints[:2],
            "supporting_locations": top_locations,
            "primary_candidate": primary_candidate,
            "secondary_candidates": secondary_candidates,
            "uncertainties": uncertainties,
            "tier": "grounded_summary",
            "query_type": query_type,
            "confidence": confidence,
            "review_required": review_required,
            "decision": decision,
        }

    def _build_query_specific_summary(
        self,
        *,
        query_type: str,
        primary_candidate: dict[str, object],
    ) -> str:
        profile = dict(primary_candidate.get("procedure_profile") or {})
        procedure_name = str(primary_candidate.get("procedure_name") or "")
        label = QUERY_SUMMARY_HINT_LABELS.get(query_type)
        if not label or not procedure_name:
            return ""

        if query_type in {"table_write", "table_read", "table_access"}:
            table_names = list(profile.get("core_write_tables") or []) or list(profile.get("core_read_tables") or [])
            if table_names:
                return f"{label}: {procedure_name} 重点涉及 {', '.join(str(name) for name in table_names[:3])}。"

        if query_type in {"variable_write", "variable_read", "variable_flow"}:
            variable_names = list(profile.get("core_variable_writes") or [])
            if query_type in {"variable_read", "variable_flow"}:
                variable_names = variable_names or list(profile.get("core_variable_reads") or [])
            if variable_names:
                return f"{label}: {procedure_name} 重点变量包括 {', '.join(str(name) for name in variable_names[:3])}。"

        if query_type == "metadata_definition":
            refs = list(profile.get("core_metadata_refs") or [])
            if refs:
                return f"{label}: {procedure_name} 重点 metadata 引用包括 {', '.join(str(name) for name in refs[:3])}。"

        if query_type == "topic_publish":
            topics = list(profile.get("core_topics") or [])
            if topics:
                return f"{label}: {procedure_name} 发布主题包括 {', '.join(str(name) for name in topics[:3])}。"

        if query_type in {"callers", "callees"}:
            calls = list(profile.get("core_callers") or []) if query_type == "callers" else list(profile.get("core_calls") or [])
            if calls:
                return f"{label}: {procedure_name} 直接关联 {', '.join(str(name) for name in calls[:3])}。"

        return ""

    def _estimate_confidence(
        self,
        evidence: list[dict[str, object]],
        related_hints: list[str],
        uncertainties: list[str],
        *,
        query_type: str,
        failure_hints: list[str],
        secondary_candidates: list[dict[str, object]],
        primary_candidate: dict[str, object],
    ) -> dict[str, object]:
        score = 0.35 + min(len(evidence), 3) * 0.15
        top_score = float(evidence[0].get("score") or 0.0) if evidence else 0.0
        second_score = float(evidence[1].get("score") or 0.0) if len(evidence) > 1 else 0.0
        group_top_score = float(primary_candidate.get("aggregate_score") or 0.0)
        group_second_score = float(secondary_candidates[0].get("aggregate_score") or 0.0) if secondary_candidates else 0.0
        if related_hints:
            score += 0.1
        if any(
            "path_bridge=" in " ".join(str(reason) for reason in item.get("reasons", []))
            for item in evidence
        ):
            score += 0.12
        if any("feature_call_bridge" in item.get("reasons", []) for item in evidence):
            score += 0.06
        if query_type == "failure_flow":
            if any(str(item.get("retrieval_source") or "") == "relation_failure_block" for item in evidence):
                score += 0.12
            if failure_hints:
                score += 0.08
        if top_score and second_score:
            if top_score - second_score >= 8.0:
                score += 0.08
            elif top_score - second_score <= 2.0 and secondary_candidates:
                score -= 0.06
        if group_top_score and group_second_score:
            if group_top_score - group_second_score >= 10.0:
                score += 0.05
            elif group_top_score - group_second_score <= 3.0:
                score -= 0.04
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

    def _should_require_review(
        self,
        *,
        query_type: str,
        primary_candidate: dict[str, object],
        secondary_candidates: list[dict[str, object]],
        confidence: dict[str, object],
    ) -> bool:
        confidence_score = float(confidence.get("score") or 0.0)
        if confidence_score < 0.45:
            return True
        if not secondary_candidates:
            return False
        if query_type not in {"table_write", "table_read", "table_access", "variable_write", "variable_read", "variable_flow", "metadata_definition", "topic_publish"}:
            return False
        primary_score = float(primary_candidate.get("aggregate_score") or 0.0)
        secondary_score = float(secondary_candidates[0].get("aggregate_score") or 0.0)
        return primary_score > 0 and secondary_score > 0 and (primary_score - secondary_score) <= 12.0

    def _build_decision(
        self,
        *,
        query_type: str,
        primary_candidate: dict[str, object],
        secondary_candidates: list[dict[str, object]],
        confidence: dict[str, object],
        review_required: bool,
    ) -> dict[str, object]:
        primary_score = float(primary_candidate.get("aggregate_score") or 0.0)
        secondary_score = float(secondary_candidates[0].get("aggregate_score") or 0.0) if secondary_candidates else 0.0
        score_gap = round(primary_score - secondary_score, 3) if secondary_score else round(primary_score, 3)
        primary_sources = {str(item) for item in primary_candidate.get("matched_via") or [] if str(item)}
        secondary_sources = (
            {str(item) for item in secondary_candidates[0].get("matched_via") or [] if str(item)}
            if secondary_candidates
            else set()
        )
        evidence_alignment = "aligned"
        if not secondary_candidates:
            state = "resolved"
            conflict_summary = ""
            conflict_kind = "none"
        elif review_required:
            state = "competitive"
            conflict_summary = (
                f"主候选 {primary_candidate.get('procedure_name')} 与次候选 {secondary_candidates[0].get('procedure_name')} 分差较小，"
                "需要人工复核最终落点。"
            )
            conflict_kind = "candidate_competition"
            if primary_sources and secondary_sources and primary_sources != secondary_sources:
                conflict_kind = "evidence_divergence"
                evidence_alignment = "divergent"
        else:
            state = "resolved"
            conflict_summary = ""
            conflict_kind = "none"
        if float(confidence.get("score") or 0.0) < 0.45:
            state = "guarded"
            if not conflict_summary:
                conflict_summary = "当前证据整体偏弱，需要保守解释并继续核验上下文。"
            conflict_kind = "low_confidence"
            evidence_alignment = "partial"
        recommendation = (
            "优先查看主候选的上下游调用和相同实体的链路证据。"
            if conflict_kind in {"candidate_competition", "evidence_divergence"}
            else "补充更多直接证据后再形成最终结论。"
            if conflict_kind == "low_confidence"
            else "当前可以按主候选继续展开。"
        )
        return {
            "state": state,
            "query_type": query_type,
            "primary_score": round(primary_score, 3),
            "secondary_score": round(secondary_score, 3),
            "score_gap": score_gap,
            "conflict_kind": conflict_kind,
            "evidence_alignment": evidence_alignment,
            "conflict_summary": conflict_summary,
            "recommendation": recommendation,
        }
