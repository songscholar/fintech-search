from __future__ import annotations

import re
from typing import Callable

from .constants import (
    CALL_CHAIN_INTENT_KEYWORDS,
    CHINESE_QUERY_SPLIT_RE,
    FAILURE_INTENT_KEYWORDS,
    FAILURE_MATCH_HINTS,
    FOCUS_EXCLUDED_QUERY_TERMS,
    GENERIC_QUERY_TERMS,
    METADATA_INTENT_KEYWORDS,
    PROCEDURE_INTENT_KEYWORDS,
    QUERY_PROCEDURE_RE,
    QUERY_TOKEN_RE,
    QUERY_VARIABLE_RE,
    READ_INTENT_KEYWORDS,
    SQL_READ_HINTS,
    SQL_WRITE_HINTS,
    TABLE_INTENT_KEYWORDS,
    TABLE_TOKEN_PREFIXES,
    TOPIC_INTENT_KEYWORDS,
    VARIABLE_INTENT_KEYWORDS,
    WRITE_INTENT_KEYWORDS,
)


def analyze_query(query: str) -> dict[str, object]:
    lowered = query.lower()
    tokens = tokenize_query(query)
    token_set = set(tokens)
    procedure_terms_ordered: list[str] = []
    seen_procedure_terms: set[str] = set()
    for match in QUERY_PROCEDURE_RE.finditer(query):
        token = match.group(0).lower()
        if token not in seen_procedure_terms:
            seen_procedure_terms.add(token)
            procedure_terms_ordered.append(token)
    procedure_terms = set(procedure_terms_ordered)
    variable_terms = {match.group(0).lower() for match in QUERY_VARIABLE_RE.finditer(query)}
    underscored_tokens = {
        token.lower()
        for token in QUERY_TOKEN_RE.findall(query)
        if "_" in token
    }
    table_terms = {
        token
        for token in underscored_tokens
        if token.startswith(TABLE_TOKEN_PREFIXES) and token not in procedure_terms
    }

    wants_variable = bool(variable_terms) or contains_any(lowered, VARIABLE_INTENT_KEYWORDS)
    if wants_variable:
        variable_terms.update(
            token
            for token in underscored_tokens
            if token not in procedure_terms and token not in table_terms
        )

    wants_table_sql = bool(table_terms) or contains_any(lowered, TABLE_INTENT_KEYWORDS)
    wants_table_write = contains_any(lowered, WRITE_INTENT_KEYWORDS)
    wants_table_read = contains_any(lowered, READ_INTENT_KEYWORDS)
    wants_call_chain = contains_any(lowered, CALL_CHAIN_INTENT_KEYWORDS)
    wants_callers = contains_any(lowered, ("被谁调用", "谁调用", "上游", "入口"))
    wants_failure_flow = contains_any(lowered, FAILURE_INTENT_KEYWORDS)
    wants_procedure = bool(procedure_terms) or contains_any(lowered, PROCEDURE_INTENT_KEYWORDS)
    wants_metadata = contains_any(lowered, METADATA_INTENT_KEYWORDS)
    wants_topic = contains_any(lowered, TOPIC_INTENT_KEYWORDS)
    wants_variable_write = wants_variable and contains_any(lowered, WRITE_INTENT_KEYWORDS + ("赋值",))
    wants_variable_read = wants_variable and contains_any(lowered, READ_INTENT_KEYWORDS + ("读取",))
    query_type = _classify_query_type(
        wants_table_sql=wants_table_sql,
        wants_table_write=wants_table_write,
        wants_table_read=wants_table_read,
        wants_variable=wants_variable,
        wants_variable_write=wants_variable_write,
        wants_variable_read=wants_variable_read,
        wants_call_chain=wants_call_chain,
        wants_callers=wants_callers,
        wants_failure_flow=wants_failure_flow,
        wants_metadata=wants_metadata,
        wants_topic=wants_topic,
        wants_procedure=wants_procedure,
    )
    focus_terms = {
        token
        for token in token_set
        if len(token) >= 2
        and token not in FOCUS_EXCLUDED_QUERY_TERMS
        and token not in procedure_terms
        and token not in variable_terms
        and token not in table_terms
    }

    intents = []
    for name, enabled in (
        ("table_sql", wants_table_sql),
        ("table_write", wants_table_write),
        ("table_read", wants_table_read),
        ("variable", wants_variable),
        ("call_chain", wants_call_chain),
        ("failure_flow", wants_failure_flow),
        ("metadata", wants_metadata),
        ("topic", wants_topic),
        ("procedure", wants_procedure),
    ):
        if enabled:
            intents.append(name)

    return {
        "tokens": tokens,
        "token_set": token_set,
        "procedure_terms": sorted(procedure_terms),
        "procedure_terms_ordered": procedure_terms_ordered,
        "variable_terms": sorted(variable_terms),
        "table_terms": sorted(table_terms),
        "focus_terms": sorted(focus_terms),
        "intents": intents,
        "wants_table_sql": wants_table_sql,
        "wants_table_write": wants_table_write,
        "wants_table_read": wants_table_read,
        "wants_variable": wants_variable,
        "wants_call_chain": wants_call_chain,
        "wants_callers": wants_callers,
        "wants_failure_flow": wants_failure_flow,
        "wants_metadata": wants_metadata,
        "wants_topic": wants_topic,
        "wants_variable_write": wants_variable_write,
        "wants_variable_read": wants_variable_read,
        "wants_procedure": wants_procedure,
        "query_type": query_type,
    }


def tokenize_query(query: str) -> list[str]:
    tokens: list[str] = []
    seen: set[str] = set()

    for raw_token in QUERY_TOKEN_RE.findall(query):
        lowered = raw_token.lower()
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            fragments = [
                fragment.strip()
                for fragment in CHINESE_QUERY_SPLIT_RE.split(raw_token)
                if len(fragment.strip()) >= 2
            ]
            if not fragments:
                fragments = [raw_token]
            for fragment in fragments:
                if fragment in GENERIC_QUERY_TERMS:
                    continue
                if fragment not in seen:
                    seen.add(fragment)
                    tokens.append(fragment)
            continue

        if lowered not in seen:
            seen.add(lowered)
            tokens.append(lowered)

    return tokens


def rerank_candidate(
    candidate: dict[str, object],
    *,
    query: str,
    query_analysis: dict[str, object],
) -> dict[str, object]:
    normalized_query = query.strip().lower()
    query_tokens = tokenize_query(query)
    search_text = str(candidate.get("search_text") or "").lower()
    matched_text = str(candidate.get("matched_text") or "").lower()
    procedure_name = str(candidate.get("procedure_name") or "").lower()
    file_path = str(candidate.get("file_path") or "").lower()
    chunk_role = str(candidate.get("chunk_role") or "")
    chunk_features = dict(candidate.get("chunk_features") or {})
    feature_flags = dict(candidate.get("feature_flags") or {})

    overlap_tokens = [token for token in query_tokens if token in search_text]
    coverage = len(set(overlap_tokens))
    token_ratio = coverage / max(len(query_tokens), 1)

    score = float(candidate["base_score"])
    reasons = list(candidate.get("reasons", []))
    score_breakdown = {
        "base_score": round(score, 6),
        "fts_bonus": 0.0,
        "token_bonus": 0.0,
        "focus_bonus": 0.0,
        "exact_bonus": 0.0,
        "name_bonus": 0.0,
        "source_bonus": 0.0,
        "intent_bonus": 0.0,
        "vector_penalty": 0.0,
        "type_bonus": 0.0,
        "multi_source_bonus": 0.0,
        "feature_bonus": 0.0,
    }

    if str(candidate["retrieval_source"]).startswith("fts"):
        score += 10.0
        score_breakdown["fts_bonus"] += 10.0
        reasons.append("fts_hit")

    if coverage:
        token_bonus = coverage * 6.0 + token_ratio * 18.0
        score += token_bonus
        score_breakdown["token_bonus"] += token_bonus
        reasons.append(f"token_overlap={coverage}/{max(len(query_tokens), 1)}")

    focus_terms = list(query_analysis.get("focus_terms", []))
    focus_in_hit = [str(term) for term in focus_terms if str(term) and str(term) in matched_text]
    focus_in_context = [str(term) for term in focus_terms if str(term) and str(term) in search_text]
    if focus_in_hit:
        focus_bonus = min(len(focus_in_hit) * 14.0, 24.0)
        score += focus_bonus
        score_breakdown["focus_bonus"] += focus_bonus
        reasons.append(f"focus_match_in_hit={','.join(focus_in_hit[:3])}")
    elif focus_in_context:
        focus_bonus = min(len(focus_in_context) * 8.0, 16.0)
        score += focus_bonus
        score_breakdown["focus_bonus"] += focus_bonus
        reasons.append(f"focus_match_in_context={','.join(focus_in_context[:3])}")

    if normalized_query and normalized_query in matched_text:
        score += 16.0
        score_breakdown["exact_bonus"] += 16.0
        reasons.append("exact_match_in_hit")
    elif normalized_query and normalized_query in search_text:
        score += 9.0
        score_breakdown["exact_bonus"] += 9.0
        reasons.append("exact_match_in_context")

    if normalized_query and normalized_query == procedure_name:
        score += 100.0
        score_breakdown["name_bonus"] += 100.0
        reasons.append("procedure_name_exact_match")
    elif normalized_query and normalized_query in procedure_name:
        score += 8.0
        score_breakdown["name_bonus"] += 8.0
        reasons.append("procedure_name_match")

    chinese_name = candidate.get("chinese_name")
    if chinese_name and normalized_query and normalized_query in str(chinese_name).lower():
        score += 90.0
        score_breakdown["name_bonus"] += 90.0
        reasons.append("chinese_name_match")

    if normalized_query and normalized_query in file_path:
        score += 4.0
        score_breakdown["name_bonus"] += 4.0
        reasons.append("file_path_match")

    if candidate.get("object_id") == normalized_query:
        score += 100.0
        score_breakdown["name_bonus"] += 100.0
        reasons.append("object_id_exact_match")

    if candidate["hit_type"] == "chunk":
        score += 5.0
        score_breakdown["type_bonus"] += 5.0
    elif candidate["hit_type"] == "action":
        score += 4.0
        score_breakdown["type_bonus"] += 4.0
    elif candidate["hit_type"] == "procedure":
        score += 3.0
        score_breakdown["type_bonus"] += 3.0

    matched_via = list(candidate.get("matched_via", []))
    if len(matched_via) > 1:
        multi_source_bonus = min(len(matched_via) * 1.5, 4.5)
        score += multi_source_bonus
        score_breakdown["multi_source_bonus"] += multi_source_bonus
        reasons.append(f"multi_source_match={len(matched_via)}")

    intent_bonus, intent_reasons = _intent_bonus(
        candidate=candidate,
        query_analysis=query_analysis,
        search_text=search_text,
        matched_text=matched_text,
        procedure_name=procedure_name,
    )
    score += intent_bonus
    score_breakdown["intent_bonus"] += intent_bonus
    reasons.extend(intent_reasons)

    feature_bonus, feature_reasons = _feature_bonus(
        query_analysis=query_analysis,
        hit_type=hit_type(candidate),
        chunk_role=chunk_role,
        chunk_features=chunk_features,
        feature_flags=feature_flags,
    )
    score += feature_bonus
    score_breakdown["feature_bonus"] += feature_bonus
    reasons.extend(feature_reasons)

    if (
        candidate.get("retrieval_source") == "vector_chunk"
        and query_analysis["wants_call_chain"]
        and focus_terms
        and not (focus_in_hit or focus_in_context)
    ):
        score -= 14.0
        score_breakdown["vector_penalty"] -= 14.0
        reasons.append("vector_focus_mismatch")

    source_bonus = max(min(float(candidate.get("source_rank") or 0.0), 12.0), -12.0)
    score += source_bonus
    score_breakdown["source_bonus"] += source_bonus

    candidate["score"] = round(score, 6)
    candidate["reasons"] = reasons
    candidate["debug_rerank"] = {
        "query_tokens": query_tokens,
        "token_overlap": sorted(set(overlap_tokens)),
        "query_analysis": query_analysis,
        "score_breakdown": score_breakdown,
        "score_before_rerank": round(float(candidate["base_score"]), 6),
        "score_after_rerank": round(score, 6),
    }
    return candidate


def apply_call_chain_rerank(
    ranked: list[dict[str, object]],
    *,
    seed_limit: int,
    query_analysis: dict[str, object],
    procedure_call_neighbors: Callable[[str], tuple[dict[int, set[str]], dict[int, set[str]]]],
) -> list[dict[str, object]]:
    if not ranked:
        return ranked

    seed_names = {
        str(item["procedure_name"])
        for item in ranked[:seed_limit]
        if item.get("procedure_name")
    }
    if not seed_names:
        return ranked

    neighbor_cache: dict[str, tuple[dict[int, set[str]], dict[int, set[str]]]] = {}
    reranked: list[dict[str, object]] = []
    call_chain_multiplier = _call_chain_bonus_multiplier(query_analysis)
    depth_bonus = {1: 3.0, 2: 1.5, 3: 1.0, 4: 0.6, 5: 0.4, 6: 0.25, 7: 0.15, 8: 0.1, 9: 0.05, 10: 0.02}

    for candidate in ranked:
        procedure_name = str(candidate.get("procedure_name") or "")
        if not procedure_name:
            reranked.append(candidate)
            continue

        cached = neighbor_cache.get(procedure_name)
        if cached is None:
            cached = procedure_call_neighbors(procedure_name)
            neighbor_cache[procedure_name] = cached
        outgoing_hops, incoming_hops = cached

        all_overlaps: dict[int, list[str]] = {}
        for depth in range(1, 6):
            depth_out = outgoing_hops.get(depth, set())
            depth_in = incoming_hops.get(depth, set())
            depth_neighbors = (depth_out | depth_in) - {procedure_name}
            overlap = sorted(depth_neighbors & seed_names)
            if overlap:
                all_overlaps[depth] = overlap

        if all_overlaps:
            combined = (
                f"{candidate.get('search_text') or ''} "
                f"{candidate.get('matched_text') or ''} "
                f"{candidate.get('procedure_name') or ''}"
            ).lower()
            if (
                query_analysis["wants_call_chain"]
                and query_analysis.get("focus_terms")
                and not focus_terms_present(query_analysis, combined)
            ):
                reranked.append(candidate)
                continue

            bonus = 0.0
            for depth, overlap in all_overlaps.items():
                bonus += len(overlap) * depth_bonus.get(depth, 0.1)
            bonus *= call_chain_multiplier

            candidate["score"] = round(float(candidate["score"]) + bonus, 6)
            reasons = list(candidate.get("reasons", []))
            reasons.append(f"call_chain_bonus={bonus:.3f}")
            for depth in sorted(all_overlaps):
                reasons.append(f"call_chain_{depth}={','.join(all_overlaps[depth][:3])}")
            if call_chain_multiplier != 1.0:
                reasons.append(f"call_chain_weight={call_chain_multiplier:.2f}")
            candidate["reasons"] = reasons

            debug_rerank = dict(candidate.get("debug_rerank") or {})
            debug_rerank["call_chain_overlap"] = {
                str(depth): overlaps
                for depth, overlaps in sorted(all_overlaps.items())
            }
            debug_rerank["call_chain_bonus"] = round(bonus, 6)
            debug_rerank["score_after_call_chain"] = round(float(candidate["score"]), 6)
            candidate["debug_rerank"] = debug_rerank

        reranked.append(candidate)

    return sorted(
        reranked,
        key=lambda item: (-float(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"])),
    )


def contains_any(value: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in value for keyword in keywords)


def focus_terms_present(query_analysis: dict[str, object], value: str) -> bool:
    return any(str(term) and str(term) in value for term in query_analysis.get("focus_terms", []))


def vector_hint_tokens(query: str) -> list[str]:
    hints: list[str] = []
    seen: set[str] = set()

    for raw_token in QUERY_TOKEN_RE.findall(query):
        lowered = raw_token.lower()
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            fragments = [
                fragment.strip()
                for fragment in CHINESE_QUERY_SPLIT_RE.split(raw_token)
                if len(fragment.strip()) >= 2 and fragment.strip() not in GENERIC_QUERY_TERMS
            ]
            for fragment in fragments or [raw_token]:
                if len(fragment) >= 2:
                    for size in (2, 3):
                        if len(fragment) < size:
                            continue
                        for index in range(0, len(fragment) - size + 1):
                            token = fragment[index : index + size]
                            if token not in seen:
                                seen.add(token)
                                hints.append(token)
            continue

        if lowered not in seen and len(lowered) >= 3:
            seen.add(lowered)
            hints.append(lowered)
        if "_" in lowered:
            for part in lowered.split("_"):
                if len(part) >= 3 and part not in seen:
                    seen.add(part)
                    hints.append(part)

    return hints


def _intent_bonus(
    *,
    candidate: dict[str, object],
    query_analysis: dict[str, object],
    search_text: str,
    matched_text: str,
    procedure_name: str,
) -> tuple[float, list[str]]:
    bonus = 0.0
    reasons: list[str] = []
    hit_type = str(candidate.get("hit_type") or "")
    match_source = str(candidate.get("match_source") or "").lower()
    combined = f"{search_text} {matched_text} {procedure_name}".lower()

    for term in query_analysis["procedure_terms"]:
        if str(term) and str(term) in combined:
            bonus += 8.0 if hit_type == "procedure" else 5.0
            reasons.append(f"procedure_focus={term}")
            break

    for term in query_analysis["table_terms"]:
        if str(term) and str(term) in combined:
            bonus += 9.0
            reasons.append(f"table_focus={term}")
            break

    for term in query_analysis["variable_terms"]:
        if str(term) and str(term) in combined:
            bonus += 8.0
            reasons.append(f"variable_focus={term}")
            break

    if query_analysis["wants_table_sql"]:
        if hit_type == "edge" and match_source in {"reads_table", "writes_table", "reads_dynamic_table", "writes_dynamic_table"}:
            bonus += 28.0
            reasons.append("intent_table_edge")
        elif hit_type == "edge" and match_source == "table_edge_relation":
            bonus += 26.0 if query_analysis["wants_table_write"] else 22.0
            reasons.append("intent_exact_table_edge")
        elif candidate.get("retrieval_source") == "relation_neighbor_context":
            bonus += 18.0
            reasons.append("intent_table_neighbor_context")
        elif hit_type == "block" and _looks_like_sql_evidence(combined):
            bonus += 30.0
            reasons.append("intent_sql_block")
        elif hit_type == "action" and _looks_like_sql_evidence(combined):
            bonus += 8.0
            reasons.append("intent_sql_action")

        if query_analysis["wants_table_write"] and contains_any(combined, SQL_WRITE_HINTS):
            bonus += 12.0
            reasons.append("write_operation_match")
        if query_analysis["wants_table_read"] and contains_any(combined, SQL_READ_HINTS):
            bonus += 7.0
            reasons.append("read_operation_match")

    if query_analysis["wants_variable"]:
        if hit_type == "variable":
            bonus += 24.0
            reasons.append("intent_variable_hit")
        elif hit_type == "statement" and match_source == "assignment":
            bonus += 28.0
            reasons.append("intent_assignment_statement")
        elif hit_type == "chunk" and "assignment_block" in combined:
            bonus += 12.0
            reasons.append("intent_assignment_chunk")

        if "=" in combined or "writes_variable" in combined or match_source == "write":
            bonus += 8.0
            reasons.append("variable_write_match")
        if hit_type == "edge" and match_source == "variable_edge_relation":
            bonus += 12.0 if query_analysis.get("wants_variable_write") else 8.0
            reasons.append("intent_exact_variable_edge")
        elif candidate.get("retrieval_source") == "relation_neighbor_context":
            bonus += 14.0
            reasons.append("intent_variable_neighbor_context")
        if query_analysis.get("wants_variable_read") and match_source == "read":
            bonus += 10.0
            reasons.append("variable_read_match")
        if query_analysis.get("wants_variable_write") and ("writes_variable" in combined or match_source == "write"):
            bonus += 10.0
            reasons.append("variable_write_focus")

    if query_analysis["wants_failure_flow"]:
        if hit_type == "block":
            bonus += 36.0
            reasons.append("intent_failure_block")
            if match_source == "failure_block_relation":
                bonus += 14.0
                reasons.append("intent_exact_failure_block")
        elif candidate.get("retrieval_source") == "relation_neighbor_context":
            bonus += 14.0
            reasons.append("intent_failure_neighbor_context")
        elif hit_type == "chunk" and contains_any(combined, FAILURE_MATCH_HINTS):
            bonus += 4.0
            reasons.append("intent_failure_chunk")

        if contains_any(combined, FAILURE_MATCH_HINTS):
            bonus += 8.0
            reasons.append("failure_flow_match")

    if query_analysis["wants_call_chain"]:
        if hit_type == "procedure":
            bonus += 4.0 if query_analysis["wants_callers"] else 8.0
            reasons.append("intent_call_chain_procedure")
            if candidate.get("retrieval_source") == "relation_path_bridge":
                bonus += 18.0
                reasons.append("intent_path_bridge")
            if candidate.get("retrieval_source") == "relation_multi_hop_context":
                bonus += 10.0
                reasons.append("intent_multi_hop_context")
        has_procedure_focus = any(str(term) in combined for term in query_analysis["procedure_terms"])
        has_text_focus = focus_terms_present(query_analysis, combined)
        has_call_signal = "call_flow" in combined or "call_block" in combined or "calls_procedure" in combined
        if hit_type in {"chunk", "action", "edge", "statement"} and (
            has_procedure_focus
            or (has_text_focus and has_call_signal)
        ):
            bonus += 14.0 if query_analysis["wants_callers"] else 9.0
            reasons.append("intent_call_chain")
            if has_text_focus:
                reasons.append("intent_call_chain_focus")

    if query_analysis.get("wants_metadata"):
        if "references_" in combined or "metadata" in combined:
            bonus += 12.0
            reasons.append("intent_metadata")

    if query_analysis.get("wants_topic"):
        if "publishes_mc_topic" in combined or "mc_topic" in combined or "topic" in combined:
            bonus += 14.0
            reasons.append("intent_topic")

    if query_analysis["wants_procedure"] and not query_analysis["wants_call_chain"]:
        if hit_type == "procedure":
            bonus += 10.0
            reasons.append("intent_procedure")
        elif any(str(term) in combined for term in query_analysis["procedure_terms"]):
            bonus += 5.0
            reasons.append("intent_procedure_context")

    return bonus, reasons


def _looks_like_sql_evidence(value: str) -> bool:
    return (
        "sql" in value
        or " select " in value
        or " update " in value
        or " delete " in value
        or " insert " in value
        or " merge " in value
        or "通用sql执行" in value
    )


def _call_chain_bonus_multiplier(query_analysis: dict[str, object]) -> float:
    if query_analysis["wants_call_chain"]:
        return 1.5
    if query_analysis["wants_variable"] or query_analysis["wants_failure_flow"]:
        return 0.35
    if query_analysis["wants_table_sql"]:
        return 0.6
    return 1.0


def _feature_bonus(
    *,
    query_analysis: dict[str, object],
    hit_type: str,
    chunk_role: str,
    chunk_features: dict[str, object],
    feature_flags: dict[str, object],
) -> tuple[float, list[str]]:
    bonus = 0.0
    reasons: list[str] = []
    query_type = str(query_analysis.get("query_type") or "")

    if query_type in {"table_write", "table_read"}:
        if chunk_role == "table_access":
            bonus += 10.0
            reasons.append("feature_table_access_chunk")
        if bool(feature_flags.get("has_table_reads")) or bool(feature_flags.get("has_table_writes")):
            bonus += 12.0
            reasons.append("feature_table_procedure")

    if query_type in {"variable_write", "variable_read", "variable"}:
        if chunk_role == "variable_flow":
            bonus += 12.0
            reasons.append("feature_variable_flow_chunk")
        if bool(feature_flags.get("has_variable_writes")):
            bonus += 14.0 if hit_type == "procedure" else 8.0
            reasons.append("feature_variable_procedure")

    if query_type in {"callers", "callees"}:
        if chunk_role == "call_chain":
            bonus += 12.0
            reasons.append("feature_call_chain_chunk")
        if bool(feature_flags.get("has_calls")):
            bonus += 10.0
            reasons.append("feature_call_procedure")
        if bool(feature_flags.get("is_call_bridge")):
            bonus += 8.0
            reasons.append("feature_call_bridge")
        call_fan_in = int(feature_flags.get("call_fan_in") or 0)
        call_fan_out = int(feature_flags.get("call_fan_out") or 0)
        if query_analysis.get("procedure_terms") and call_fan_in and call_fan_out:
            bonus += min(call_fan_in + call_fan_out, 4) * 1.5
            reasons.append("feature_call_fan_balance")

    if query_type == "failure_flow":
        if chunk_role == "failure_flow" or bool(chunk_features.get("has_failure_markers")):
            bonus += 16.0
            reasons.append("feature_failure_chunk")
        if bool(feature_flags.get("has_failure_chunks")):
            bonus += 10.0
            reasons.append("feature_failure_procedure")
        if bool(feature_flags.get("has_failure_handlers")):
            bonus += 10.0
            reasons.append("feature_failure_handlers")
        failure_handler_count = int(feature_flags.get("failure_handler_count") or 0)
        exception_handler_count = int(feature_flags.get("exception_handler_count") or 0)
        when_others_handler_count = int(feature_flags.get("when_others_handler_count") or 0)
        if failure_handler_count or exception_handler_count or when_others_handler_count:
            bonus += min(
                failure_handler_count * 3.0
                + exception_handler_count * 2.0
                + when_others_handler_count * 1.5,
                10.0,
            )
            reasons.append("feature_failure_handler_counts")

    if query_type == "metadata" and bool(feature_flags.get("has_metadata_refs")):
        bonus += 10.0
        reasons.append("feature_metadata_procedure")

    if query_type == "topic" and bool(feature_flags.get("has_mc_topics")):
        bonus += 12.0
        reasons.append("feature_topic_procedure")

    if hit_type == "chunk" and float(chunk_features.get("action_density") or 0.0) >= 0.5:
        bonus += 2.0
        reasons.append("feature_dense_chunk")

    return bonus, reasons


def hit_type(candidate: dict[str, object]) -> str:
    return str(candidate.get("hit_type") or "")


def _classify_query_type(
    *,
    wants_table_sql: bool,
    wants_table_write: bool,
    wants_table_read: bool,
    wants_variable: bool,
    wants_variable_write: bool,
    wants_variable_read: bool,
    wants_call_chain: bool,
    wants_callers: bool,
    wants_failure_flow: bool,
    wants_metadata: bool,
    wants_topic: bool,
    wants_procedure: bool,
) -> str:
    if wants_call_chain:
        return "callers" if wants_callers else "callees"
    if wants_failure_flow:
        return "failure_flow"
    if wants_table_sql and wants_table_write:
        return "table_write"
    if wants_table_sql and wants_table_read:
        return "table_read"
    if wants_variable_write:
        return "variable_write"
    if wants_variable_read:
        return "variable_read"
    if wants_metadata:
        return "metadata"
    if wants_topic:
        return "topic"
    if wants_variable:
        return "variable"
    if wants_procedure:
        return "procedure"
    return "location"
