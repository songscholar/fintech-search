from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .answering import CodebaseAnswerer
from .indexer import SQLiteIndexer


@dataclass(frozen=True, slots=True)
class DebugBundlePanelThresholds:
    max_changed_cases: int | None = None
    max_high_priority_cases: int | None = None
    max_verdict_counts: dict[str, int] | None = None
    max_focus_area_counts: dict[str, int] | None = None


def build_debug_bundle(
    *,
    indexer: SQLiteIndexer,
    answerer: CodebaseAnswerer,
    db_path: str,
    question: str,
    limit: int,
    context_window: int,
    related_limit: int,
) -> dict[str, object]:
    query_result = indexer.query_index(db_path, question, limit=limit, debug=True)
    evidence_result = indexer.assemble_evidence(
        db_path,
        question,
        limit=limit,
        context_window=context_window,
        related_limit=related_limit,
        debug=True,
    )
    answer_result = answerer.answer(
        db_path,
        question,
        evidence_limit=limit,
        context_window=context_window,
        related_limit=related_limit,
    )
    return {
        "db_path": db_path,
        "question": question,
        "bundle_kind": "debug_bundle",
        "query": query_result,
        "evidence": evidence_result,
        "answer": answer_result,
    }


def write_debug_bundle_archive(bundle: dict[str, object], archive_dir: str | Path) -> dict[str, object]:
    root = Path(archive_dir)
    root.mkdir(parents=True, exist_ok=True)

    query_path = root / "query.json"
    evidence_path = root / "evidence.json"
    answer_path = root / "answer.json"
    summary_path = root / "bundle_summary.json"
    bundle_path = root / "bundle.json"

    query_path.write_text(json.dumps(bundle["query"], ensure_ascii=False, indent=2), encoding="utf-8")
    evidence_path.write_text(json.dumps(bundle["evidence"], ensure_ascii=False, indent=2), encoding="utf-8")
    answer_path.write_text(json.dumps(bundle["answer"], ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "bundle_kind": "debug_bundle_summary",
        "question": bundle["question"],
        "db_path": bundle["db_path"],
        "query_hit_count": bundle["query"]["hit_count"],
        "evidence_count": bundle["evidence"]["evidence_count"],
        "answer_source": bundle["answer"]["answer_source"],
        "response_kinds": {
            "query": bundle["query"].get("response_kind", "query"),
            "evidence": bundle["evidence"].get("response_kind", "evidence"),
            "answer": bundle["answer"].get("response_kind", "answer"),
        },
        "trace_ids": {
            "query": ((bundle["query"].get("debug") or {}).get("metadata") or {}).get("trace_id"),
            "evidence": ((bundle["evidence"].get("debug") or {}).get("metadata") or {}).get("trace_id"),
        },
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    bundle_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "archive_dir": str(root),
        "files": {
            "bundle": str(bundle_path),
            "summary": str(summary_path),
            "query": str(query_path),
            "evidence": str(evidence_path),
            "answer": str(answer_path),
        },
    }


def compare_debug_bundles(before_path: str | Path, after_path: str | Path) -> dict[str, object]:
    before_bundle = _load_debug_bundle(before_path)
    after_bundle = _load_debug_bundle(after_path)
    comparison = compare_debug_bundles_from_payloads(before_bundle, after_bundle)
    comparison["before_path"] = str(before_path)
    comparison["after_path"] = str(after_path)
    return comparison


def render_debug_bundle_comparison_markdown(comparison: dict[str, object]) -> str:
    review_summary = dict(comparison.get("review_summary") or {})
    summary = dict(comparison.get("summary") or {})
    query = dict(comparison.get("query") or {})
    evidence = dict(comparison.get("evidence") or {})
    answer = dict(comparison.get("answer") or {})

    lines = [
        "# Debug Bundle Comparison",
        "",
        f"- Verdict: {review_summary.get('verdict', 'unknown')}",
        f"- Priority: {review_summary.get('priority', 'medium')}",
        f"- Focus area: {review_summary.get('focus_area', 'general')}",
        f"- Query hits delta: {_render_delta(summary.get('query_hit_count'))}",
        f"- Candidates delta: {_render_delta(summary.get('candidate_count'))}",
        f"- Evidence delta: {_render_delta(summary.get('evidence_count'))}",
        f"- Query type changed: {bool((summary.get('query_type') or {}).get('changed'))}",
        f"- Top hit changed: {bool(query.get('top_hit_changed'))}",
        f"- Top evidence changed: {bool(evidence.get('top_evidence_changed'))}",
        f"- Final answer changed: {bool(answer.get('final_answer_changed'))}",
        "",
        "## Findings",
    ]

    findings = list(review_summary.get("findings") or [])
    if findings:
        lines.extend(f"- {item}" for item in findings)
    else:
        lines.append("- No major differences detected.")

    lines.extend(["", "## Suggested Next Steps"])
    next_steps = list(review_summary.get("next_steps") or [])
    if next_steps:
        lines.extend(f"- {item}" for item in next_steps)
    else:
        lines.append("- No follow-up needed.")

    if answer.get("before_final_answer_excerpt") or answer.get("after_final_answer_excerpt"):
        lines.extend(
            [
                "",
                "## Final Answer Excerpts",
                f"- Before: {answer.get('before_final_answer_excerpt') or ''}",
                f"- After: {answer.get('after_final_answer_excerpt') or ''}",
            ]
        )

    return "\n".join(lines).strip() + "\n"


def build_debug_bundle_regression_panel(
    *,
    indexer: SQLiteIndexer,
    answerer: CodebaseAnswerer,
    before_db_path: str,
    after_db_path: str,
    cases_path: str | Path,
    limit: int,
    context_window: int,
    related_limit: int,
    archive_dir: str | Path | None = None,
) -> dict[str, object]:
    cases = _load_regression_cases(cases_path)
    comparisons: list[dict[str, object]] = []
    archive_manifest: list[dict[str, object]] = []

    archive_root = Path(archive_dir) if archive_dir else None
    if archive_root is not None:
        archive_root.mkdir(parents=True, exist_ok=True)

    for index, case in enumerate(cases, start=1):
        case_id = str(case.get("id") or f"case-{index}")
        question = str(case["question"])
        tags = [str(item) for item in list(case.get("tags") or [])]

        before_bundle = build_debug_bundle(
            indexer=indexer,
            answerer=answerer,
            db_path=before_db_path,
            question=question,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
        )
        after_bundle = build_debug_bundle(
            indexer=indexer,
            answerer=answerer,
            db_path=after_db_path,
            question=question,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
        )

        comparison = compare_debug_bundles_from_payloads(before_bundle, after_bundle)
        comparison["case_id"] = case_id
        comparison["question_text"] = question
        comparison["tags"] = tags
        comparisons.append(comparison)

        if archive_root is not None:
            case_dir = archive_root / f"{index:02d}_{_slugify(case_id)}"
            before_dir = case_dir / "before"
            after_dir = case_dir / "after"
            before_archive = write_debug_bundle_archive(before_bundle, before_dir)
            after_archive = write_debug_bundle_archive(after_bundle, after_dir)
            comparison_path = case_dir / "comparison.json"
            markdown_path = case_dir / "comparison.md"
            comparison_path.write_text(json.dumps(comparison, ensure_ascii=False, indent=2), encoding="utf-8")
            markdown_path.write_text(str(comparison.get("markdown_summary") or ""), encoding="utf-8")
            archive_manifest.append(
                {
                    "case_id": case_id,
                    "question": question,
                    "tags": tags,
                    "before_archive_dir": before_archive["archive_dir"],
                    "after_archive_dir": after_archive["archive_dir"],
                    "comparison_json": str(comparison_path),
                    "comparison_markdown": str(markdown_path),
                }
            )

    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": before_db_path,
        "after_db_path": after_db_path,
        "cases_path": str(cases_path),
        "case_count": len(comparisons),
        "summary": _summarize_regression_panel(comparisons),
        "cases": comparisons,
        "archive_manifest": archive_manifest,
    }
    panel["markdown_summary"] = render_debug_bundle_regression_panel_markdown(panel)
    if archive_root is not None:
        panel["archive"] = write_debug_bundle_regression_panel_archive(panel, archive_root)
    return panel


def evaluate_debug_bundle_regression_panel_thresholds(
    panel: dict[str, object],
    thresholds: DebugBundlePanelThresholds,
) -> dict[str, object]:
    summary = dict(panel.get("summary") or {})
    checks: list[dict[str, object]] = []

    if thresholds.max_changed_cases is not None:
        checks.append(
            _panel_threshold_check(
                metric="changed_case_count",
                actual=_coerce_panel_int(summary.get("changed_case_count")),
                expected=thresholds.max_changed_cases,
            )
        )

    if thresholds.max_high_priority_cases is not None:
        checks.append(
            _panel_threshold_check(
                metric="high_priority_case_count",
                actual=len(list(summary.get("high_priority_cases") or [])),
                expected=thresholds.max_high_priority_cases,
            )
        )

    verdict_counts = dict(summary.get("verdict_counts") or {})
    for verdict, expected in sorted((thresholds.max_verdict_counts or {}).items()):
        checks.append(
            _panel_threshold_check(
                metric=f"verdict_counts.{verdict}",
                actual=_coerce_panel_int(verdict_counts.get(verdict, 0)),
                expected=expected,
            )
        )

    focus_area_counts = dict(summary.get("focus_area_counts") or {})
    for focus_area, expected in sorted((thresholds.max_focus_area_counts or {}).items()):
        checks.append(
            _panel_threshold_check(
                metric=f"focus_area_counts.{focus_area}",
                actual=_coerce_panel_int(focus_area_counts.get(focus_area, 0)),
                expected=expected,
            )
        )

    return {
        "status": "pass" if all(item["passed"] for item in checks) else "fail",
        "check_count": len(checks),
        "failed_count": sum(1 for item in checks if not item["passed"]),
        "checks": checks,
    }


def write_debug_bundle_regression_panel_archive(panel: dict[str, object], archive_dir: str | Path) -> dict[str, object]:
    root = Path(archive_dir)
    root.mkdir(parents=True, exist_ok=True)
    panel_path = root / "panel.json"
    markdown_path = root / "panel.md"
    summary_path = root / "panel_summary.json"

    panel_path.write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    markdown_path.write_text(str(panel.get("markdown_summary") or ""), encoding="utf-8")

    summary = {
        "bundle_kind": "debug_bundle_regression_panel_summary",
        "before_db_path": panel.get("before_db_path"),
        "after_db_path": panel.get("after_db_path"),
        "cases_path": panel.get("cases_path"),
        "case_count": panel.get("case_count"),
        "summary": panel.get("summary"),
        "thresholds": panel.get("thresholds"),
    }
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "archive_dir": str(root),
        "files": {
            "panel": str(panel_path),
            "markdown": str(markdown_path),
            "summary": str(summary_path),
        },
    }


def compare_debug_bundle_regression_panels(before_path: str | Path, after_path: str | Path) -> dict[str, object]:
    before_panel = _load_debug_bundle_regression_panel(before_path)
    after_panel = _load_debug_bundle_regression_panel(after_path)

    before_summary = dict(before_panel.get("summary") or {})
    after_summary = dict(after_panel.get("summary") or {})
    before_cases = {str(item.get("case_id") or item.get("question_text") or index): item for index, item in enumerate(list(before_panel.get("cases") or []), start=1)}
    after_cases = {str(item.get("case_id") or item.get("question_text") or index): item for index, item in enumerate(list(after_panel.get("cases") or []), start=1)}
    case_ids = sorted(set(before_cases) | set(after_cases))

    verdict_delta = _count_delta(
        dict(before_summary.get("verdict_counts") or {}),
        dict(after_summary.get("verdict_counts") or {}),
    )
    priority_delta = _count_delta(
        dict(before_summary.get("priority_counts") or {}),
        dict(after_summary.get("priority_counts") or {}),
    )
    focus_area_delta = _count_delta(
        dict(before_summary.get("focus_area_counts") or {}),
        dict(after_summary.get("focus_area_counts") or {}),
    )

    case_changes: list[dict[str, object]] = []
    for case_id in case_ids:
        before_case = before_cases.get(case_id)
        after_case = after_cases.get(case_id)
        if before_case is None or after_case is None:
            continue
        before_review = dict(before_case.get("review_summary") or {})
        after_review = dict(after_case.get("review_summary") or {})
        verdict_before = str(before_review.get("verdict") or "unknown")
        verdict_after = str(after_review.get("verdict") or "unknown")
        focus_before = str(before_review.get("focus_area") or "stable")
        focus_after = str(after_review.get("focus_area") or "stable")
        changed = verdict_before != verdict_after or focus_before != focus_after
        case_changes.append(
            {
                "case_id": case_id,
                "question": after_case.get("question_text") or before_case.get("question_text"),
                "changed": changed,
                "before_verdict": verdict_before,
                "after_verdict": verdict_after,
                "before_focus_area": focus_before,
                "after_focus_area": focus_after,
                "before_priority": before_review.get("priority"),
                "after_priority": after_review.get("priority"),
            }
        )

    comparison = {
        "bundle_kind": "debug_bundle_regression_panel_comparison",
        "before_path": str(before_path),
        "after_path": str(after_path),
        "summary": {
            "case_count": _numeric_delta(before_panel.get("case_count"), after_panel.get("case_count")),
            "changed_case_count": _numeric_delta(before_summary.get("changed_case_count"), after_summary.get("changed_case_count")),
            "stable_case_count": _numeric_delta(before_summary.get("stable_case_count"), after_summary.get("stable_case_count")),
            "verdict_counts_delta": verdict_delta,
            "priority_counts_delta": priority_delta,
            "focus_area_counts_delta": focus_area_delta,
        },
        "high_priority_cases": {
            "before": list(before_summary.get("high_priority_cases") or []),
            "after": list(after_summary.get("high_priority_cases") or []),
        },
        "case_changes": case_changes,
    }
    comparison["review_summary"] = _build_panel_comparison_review_summary(comparison)
    comparison["markdown_summary"] = render_debug_bundle_regression_panel_comparison_markdown(comparison)
    return comparison


def compare_debug_bundles_from_payloads(
    before_bundle: dict[str, object],
    after_bundle: dict[str, object],
) -> dict[str, object]:
    before_query = dict(before_bundle.get("query") or {})
    after_query = dict(after_bundle.get("query") or {})
    before_evidence = dict(before_bundle.get("evidence") or {})
    after_evidence = dict(after_bundle.get("evidence") or {})
    before_answer = dict(before_bundle.get("answer") or {})
    after_answer = dict(after_bundle.get("answer") or {})

    before_query_type = _query_type(before_query)
    after_query_type = _query_type(after_query)
    before_hit_signatures = _top_hit_signatures(before_query)
    after_hit_signatures = _top_hit_signatures(after_query)
    before_evidence_signatures = _top_evidence_signatures(before_evidence)
    after_evidence_signatures = _top_evidence_signatures(after_evidence)
    before_answer_text = _answer_text(before_answer)
    after_answer_text = _answer_text(after_answer)

    warnings: list[str] = []
    if before_bundle.get("question") != after_bundle.get("question"):
        warnings.append("question_changed")
    if before_bundle.get("db_path") != after_bundle.get("db_path"):
        warnings.append("db_path_changed")
    if before_query_type != after_query_type:
        warnings.append("query_type_changed")

    comparison = {
        "bundle_kind": "debug_bundle_comparison",
        "before_path": None,
        "after_path": None,
        "question": {
            "before": before_bundle.get("question"),
            "after": after_bundle.get("question"),
            "changed": before_bundle.get("question") != after_bundle.get("question"),
        },
        "db_path": {
            "before": before_bundle.get("db_path"),
            "after": after_bundle.get("db_path"),
            "changed": before_bundle.get("db_path") != after_bundle.get("db_path"),
        },
        "warnings": warnings,
        "summary": {
            "query_hit_count": _numeric_delta(before_query.get("hit_count"), after_query.get("hit_count")),
            "candidate_count": _numeric_delta(before_query.get("candidate_count"), after_query.get("candidate_count")),
            "evidence_count": _numeric_delta(before_evidence.get("evidence_count"), after_evidence.get("evidence_count")),
            "query_type": {
                "before": before_query_type,
                "after": after_query_type,
                "changed": before_query_type != after_query_type,
            },
            "answer_source": {
                "before": before_answer.get("answer_source"),
                "after": after_answer.get("answer_source"),
                "changed": before_answer.get("answer_source") != after_answer.get("answer_source"),
            },
            "final_answer_changed": before_answer_text != after_answer_text,
        },
        "query": {
            "top_hit_changed": _top_first(before_hit_signatures) != _top_first(after_hit_signatures),
            "before_top_hits": before_hit_signatures,
            "after_top_hits": after_hit_signatures,
            "added_top_hits": [item for item in after_hit_signatures if item not in before_hit_signatures],
            "removed_top_hits": [item for item in before_hit_signatures if item not in after_hit_signatures],
            "trace_ids": {
                "before": _trace_id(before_query),
                "after": _trace_id(after_query),
            },
        },
        "evidence": {
            "top_evidence_changed": _top_first(before_evidence_signatures) != _top_first(after_evidence_signatures),
            "before_top_evidence": before_evidence_signatures,
            "after_top_evidence": after_evidence_signatures,
            "added_top_evidence": [item for item in after_evidence_signatures if item not in before_evidence_signatures],
            "removed_top_evidence": [item for item in before_evidence_signatures if item not in after_evidence_signatures],
            "trace_ids": {
                "before": _trace_id(before_evidence),
                "after": _trace_id(after_evidence),
            },
        },
        "answer": {
            "before_source": before_answer.get("answer_source"),
            "after_source": after_answer.get("answer_source"),
            "draft_answer_changed": _draft_answer_text(before_answer) != _draft_answer_text(after_answer),
            "final_answer_changed": before_answer_text != after_answer_text,
            "before_final_answer_excerpt": _truncate(before_answer_text),
            "after_final_answer_excerpt": _truncate(after_answer_text),
        },
    }
    comparison["review_summary"] = _build_review_summary(comparison)
    comparison["markdown_summary"] = render_debug_bundle_comparison_markdown(comparison)
    return comparison


def _load_debug_bundle(path: str | Path) -> dict[str, object]:
    candidate = Path(path)
    if candidate.is_dir():
        candidate = candidate / "bundle.json"
    payload = json.loads(candidate.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Debug bundle must be a JSON object: {candidate}")
    return payload


def _load_regression_cases(path: str | Path) -> list[dict[str, object]]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        raw_cases = payload.get("cases", [])
    elif isinstance(payload, list):
        raw_cases = payload
    else:
        raise ValueError(f"Regression cases must be a JSON object or list: {path}")
    if not isinstance(raw_cases, list):
        raise ValueError(f"Regression cases must contain a list under 'cases': {path}")
    cases: list[dict[str, object]] = []
    for index, item in enumerate(raw_cases, start=1):
        if not isinstance(item, dict) or not item.get("question"):
            raise ValueError(f"Regression case #{index} is missing a question: {path}")
        cases.append(item)
    return cases


def _load_debug_bundle_regression_panel(path: str | Path) -> dict[str, object]:
    candidate = Path(path)
    if candidate.is_dir():
        candidate = candidate / "panel.json"
    payload = json.loads(candidate.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Debug bundle regression panel must be a JSON object: {candidate}")
    return payload


def _query_type(query_payload: dict[str, object]) -> str:
    debug_payload = dict(query_payload.get("debug") or {})
    metadata = dict(debug_payload.get("metadata") or {})
    query_analysis = dict(debug_payload.get("query_analysis") or {})
    return str(query_analysis.get("query_type") or metadata.get("query_type") or "unknown")


def _trace_id(payload: dict[str, object]) -> str | None:
    debug_payload = dict(payload.get("debug") or {})
    metadata = dict(debug_payload.get("metadata") or {})
    value = metadata.get("trace_id")
    return str(value) if value else None


def _top_hit_signatures(query_payload: dict[str, object], limit: int = 5) -> list[dict[str, object]]:
    hits = list(query_payload.get("hits") or [])
    return [_hit_signature(hit) for hit in hits[:limit] if isinstance(hit, dict)]


def _top_evidence_signatures(evidence_payload: dict[str, object], limit: int = 5) -> list[dict[str, object]]:
    evidence_blocks = list(evidence_payload.get("evidence") or [])
    return [_evidence_signature(block) for block in evidence_blocks[:limit] if isinstance(block, dict)]


def _hit_signature(hit: dict[str, Any]) -> dict[str, object]:
    return {
        "rank": hit.get("rank"),
        "procedure_name": hit.get("procedure_name"),
        "file_path": hit.get("file_path"),
        "line_start": hit.get("line_start"),
        "line_end": hit.get("line_end"),
        "match_source": hit.get("match_source"),
        "retrieval_source": hit.get("retrieval_source"),
        "matched_text": _truncate(str(hit.get("matched_text") or ""), limit=120),
    }


def _evidence_signature(block: dict[str, Any]) -> dict[str, object]:
    return {
        "rank": block.get("rank"),
        "procedure_name": block.get("procedure_name"),
        "file_path": block.get("file_path"),
        "line_start": block.get("line_start"),
        "line_end": block.get("line_end"),
        "matched_text": _truncate(str(block.get("matched_text") or ""), limit=120),
    }


def _numeric_delta(before: object, after: object) -> dict[str, object]:
    before_value = _coerce_number(before)
    after_value = _coerce_number(after)
    delta = None
    if before_value is not None and after_value is not None:
        delta = after_value - before_value
    return {"before": before_value, "after": after_value, "delta": delta}


def _coerce_number(value: object) -> float | int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, (int, float)):
        return value
    return None


def _answer_text(answer_payload: dict[str, object]) -> str:
    final_answer = dict(answer_payload.get("final_answer") or {})
    return str(final_answer.get("text") or "")


def _draft_answer_text(answer_payload: dict[str, object]) -> str:
    draft_answer = dict(answer_payload.get("draft_answer") or {})
    return str(draft_answer.get("text") or "")


def _truncate(text: str, *, limit: int = 160) -> str:
    stripped = text.strip()
    if len(stripped) <= limit:
        return stripped
    return stripped[: limit - 3] + "..."


def _top_first(items: list[dict[str, object]]) -> dict[str, object] | None:
    return items[0] if items else None


def _build_review_summary(comparison: dict[str, object]) -> dict[str, object]:
    warnings = list(comparison.get("warnings") or [])
    summary = dict(comparison.get("summary") or {})
    query = dict(comparison.get("query") or {})
    evidence = dict(comparison.get("evidence") or {})
    answer = dict(comparison.get("answer") or {})
    findings: list[str] = []
    next_steps: list[str] = []

    if warnings:
        findings.append(f"Input drift detected: {', '.join(warnings)}.")
        next_steps.append("Confirm the two bundles come from the same question and comparable index/database inputs.")

    if bool((summary.get("query_type") or {}).get("changed")):
        findings.append("Query understanding changed between the two runs.")
        next_steps.append("Inspect query analysis first; query_type drift can invalidate downstream hit/evidence comparisons.")

    query_hit_delta = _delta_value(summary.get("query_hit_count"))
    candidate_delta = _delta_value(summary.get("candidate_count"))
    evidence_delta = _delta_value(summary.get("evidence_count"))

    if query_hit_delta is not None and query_hit_delta > 0:
        findings.append(f"Top-level hit count increased by {query_hit_delta}.")
    elif query_hit_delta is not None and query_hit_delta < 0:
        findings.append(f"Top-level hit count dropped by {abs(query_hit_delta)}.")
        next_steps.append("Check retrieval contributions and rerank changes; recall may have regressed.")

    if candidate_delta is not None and candidate_delta > 0 and bool(query.get("top_hit_changed")):
        findings.append("Candidate pool grew and the top hit changed.")
        next_steps.append("Review rerank behavior; broader recall may be pushing a weaker hit to the top.")

    if evidence_delta is not None and evidence_delta < 0:
        findings.append(f"Evidence count dropped by {abs(evidence_delta)}.")
        next_steps.append("Inspect evidence pruning decisions and procedure evidence caps.")

    if bool(evidence.get("top_evidence_changed")):
        findings.append("Top evidence block changed.")
        next_steps.append("Compare evidence snippets to verify the new context still supports the same conclusion.")

    if bool(answer.get("final_answer_changed")):
        findings.append("Final answer text changed.")
        next_steps.append("Check whether the answer shift is grounded in retrieval/evidence changes or only in answer policy.")

    answer_source = dict(summary.get("answer_source") or {})
    if bool(answer_source.get("changed")):
        findings.append(
            f"Answer source changed from {answer_source.get('before')} to {answer_source.get('after')}."
        )

    focus_area = _determine_focus_area(comparison)
    verdict = _determine_verdict(comparison)
    priority = _determine_priority(comparison, warnings)

    if not findings:
        findings.append("No significant behavioral differences were detected in query, evidence, or answer output.")

    if not next_steps:
        next_steps.append("If this change was intentional, keep the current baseline as the new comparison reference.")

    return {
        "verdict": verdict,
        "priority": priority,
        "focus_area": focus_area,
        "findings": findings,
        "next_steps": next_steps,
    }


def _determine_focus_area(comparison: dict[str, object]) -> str:
    summary = dict(comparison.get("summary") or {})
    query = dict(comparison.get("query") or {})
    evidence = dict(comparison.get("evidence") or {})
    answer = dict(comparison.get("answer") or {})

    if bool((summary.get("query_type") or {}).get("changed")):
        return "query_understanding"
    if bool(query.get("top_hit_changed")):
        return "retrieval"
    if bool(evidence.get("top_evidence_changed")):
        return "evidence"
    if bool(answer.get("final_answer_changed")):
        return "answering"
    return "stable"


def _determine_verdict(comparison: dict[str, object]) -> str:
    warnings = list(comparison.get("warnings") or [])
    summary = dict(comparison.get("summary") or {})
    query = dict(comparison.get("query") or {})
    evidence = dict(comparison.get("evidence") or {})
    answer = dict(comparison.get("answer") or {})
    query_hit_delta = _delta_value(summary.get("query_hit_count"))
    evidence_delta = _delta_value(summary.get("evidence_count"))

    if "question_changed" in warnings:
        return "invalid_comparison"
    if bool((summary.get("query_type") or {}).get("changed")):
        return "query_drift"
    if (query_hit_delta is not None and query_hit_delta < 0) or (evidence_delta is not None and evidence_delta < 0):
        return "possible_regression"
    if bool(query.get("top_hit_changed")) or bool(evidence.get("top_evidence_changed")) or bool(answer.get("final_answer_changed")):
        return "behavior_changed"
    return "stable"


def _determine_priority(comparison: dict[str, object], warnings: list[str]) -> str:
    summary = dict(comparison.get("summary") or {})
    query_hit_delta = _delta_value(summary.get("query_hit_count"))
    evidence_delta = _delta_value(summary.get("evidence_count"))
    if "question_changed" in warnings or bool((summary.get("query_type") or {}).get("changed")):
        return "high"
    if (query_hit_delta is not None and query_hit_delta < 0) or (evidence_delta is not None and evidence_delta < 0):
        return "high"
    if query_hit_delta or evidence_delta:
        return "medium"
    return "low"


def _delta_value(delta_payload: object) -> float | int | None:
    if not isinstance(delta_payload, dict):
        return None
    return _coerce_number(delta_payload.get("delta"))


def _render_delta(delta_payload: object) -> str:
    if not isinstance(delta_payload, dict):
        return "n/a"
    before = delta_payload.get("before")
    after = delta_payload.get("after")
    delta = delta_payload.get("delta")
    return f"{before} -> {after} ({delta:+})" if isinstance(delta, (int, float)) else f"{before} -> {after}"


def _summarize_regression_panel(comparisons: list[dict[str, object]]) -> dict[str, object]:
    verdict_counts: dict[str, int] = {}
    priority_counts: dict[str, int] = {}
    focus_area_counts: dict[str, int] = {}
    changed_cases = 0
    high_priority_cases: list[dict[str, object]] = []

    for item in comparisons:
        review = dict(item.get("review_summary") or {})
        verdict = str(review.get("verdict") or "unknown")
        priority = str(review.get("priority") or "medium")
        focus_area = str(review.get("focus_area") or "stable")
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
        focus_area_counts[focus_area] = focus_area_counts.get(focus_area, 0) + 1

        if verdict != "stable":
            changed_cases += 1
        if priority == "high":
            high_priority_cases.append(
                {
                    "case_id": item.get("case_id"),
                    "question": item.get("question_text") or (item.get("question") or {}).get("after"),
                    "verdict": verdict,
                    "focus_area": focus_area,
                }
            )

    return {
        "changed_case_count": changed_cases,
        "stable_case_count": len(comparisons) - changed_cases,
        "verdict_counts": verdict_counts,
        "priority_counts": priority_counts,
        "focus_area_counts": focus_area_counts,
        "high_priority_cases": high_priority_cases,
    }


def render_debug_bundle_regression_panel_markdown(panel: dict[str, object]) -> str:
    summary = dict(panel.get("summary") or {})
    thresholds = dict(panel.get("thresholds") or {})
    lines = [
        "# Debug Bundle Regression Panel",
        "",
        f"- Before DB: {panel.get('before_db_path')}",
        f"- After DB: {panel.get('after_db_path')}",
        f"- Cases: {panel.get('case_count')}",
        f"- Changed cases: {summary.get('changed_case_count')}",
        f"- Stable cases: {summary.get('stable_case_count')}",
        "",
        "## Verdict Counts",
    ]

    verdict_counts = dict(summary.get("verdict_counts") or {})
    if verdict_counts:
        lines.extend(f"- {key}: {value}" for key, value in sorted(verdict_counts.items()))
    else:
        lines.append("- none")

    lines.extend(["", "## Priority Counts"])
    priority_counts = dict(summary.get("priority_counts") or {})
    if priority_counts:
        lines.extend(f"- {key}: {value}" for key, value in sorted(priority_counts.items()))
    else:
        lines.append("- none")

    lines.extend(["", "## Focus Areas"])
    focus_area_counts = dict(summary.get("focus_area_counts") or {})
    if focus_area_counts:
        lines.extend(f"- {key}: {value}" for key, value in sorted(focus_area_counts.items()))
    else:
        lines.append("- none")

    lines.extend(["", "## High Priority Cases"])
    high_priority_cases = list(summary.get("high_priority_cases") or [])
    if high_priority_cases:
        for case in high_priority_cases:
            lines.append(
                f"- {case.get('case_id')}: {case.get('question')} "
                f"[verdict={case.get('verdict')}, focus={case.get('focus_area')}]"
            )
    else:
        lines.append("- none")

    if thresholds:
        lines.extend(
            [
                "",
                "## Threshold Status",
                f"- Status: {thresholds.get('status')}",
                f"- Failed checks: {thresholds.get('failed_count')}",
            ]
        )

    lines.extend(["", "## Case Summaries"])
    for case in list(panel.get("cases") or []):
        review = dict(case.get("review_summary") or {})
        lines.append(
            f"- {case.get('case_id')}: verdict={review.get('verdict')}, "
            f"priority={review.get('priority')}, focus={review.get('focus_area')}"
        )
        findings = list(review.get("findings") or [])
        if findings:
            lines.append(f"  findings: {findings[0]}")

    return "\n".join(lines).strip() + "\n"


def render_debug_bundle_regression_panel_comparison_markdown(comparison: dict[str, object]) -> str:
    summary = dict(comparison.get("summary") or {})
    review = dict(comparison.get("review_summary") or {})
    lines = [
        "# Debug Bundle Regression Panel Comparison",
        "",
        f"- Verdict: {review.get('verdict', 'unknown')}",
        f"- Priority: {review.get('priority', 'medium')}",
        f"- Changed cases delta: {_render_delta(summary.get('changed_case_count'))}",
        f"- Stable cases delta: {_render_delta(summary.get('stable_case_count'))}",
        "",
        "## Verdict Delta",
    ]
    verdict_delta = dict(summary.get("verdict_counts_delta") or {})
    if verdict_delta:
        lines.extend(f"- {key}: {value:+}" for key, value in sorted(verdict_delta.items()))
    else:
        lines.append("- none")

    lines.extend(["", "## Findings"])
    findings = list(review.get("findings") or [])
    if findings:
        lines.extend(f"- {item}" for item in findings)
    else:
        lines.append("- No major panel-level changes detected.")

    lines.extend(["", "## Suggested Next Steps"])
    next_steps = list(review.get("next_steps") or [])
    if next_steps:
        lines.extend(f"- {item}" for item in next_steps)
    else:
        lines.append("- No follow-up needed.")

    return "\n".join(lines).strip() + "\n"


def _slugify(value: str) -> str:
    lowered = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", lowered)
    trimmed = normalized.strip("-")
    return trimmed or "case"


def _count_delta(before: dict[str, int], after: dict[str, int]) -> dict[str, int]:
    keys = sorted(set(before) | set(after))
    return {key: int(after.get(key, 0)) - int(before.get(key, 0)) for key in keys}


def _build_panel_comparison_review_summary(comparison: dict[str, object]) -> dict[str, object]:
    summary = dict(comparison.get("summary") or {})
    findings: list[str] = []
    next_steps: list[str] = []

    changed_case_delta = _delta_value(summary.get("changed_case_count"))
    if changed_case_delta is not None and changed_case_delta > 0:
        findings.append(f"Changed case count increased by {changed_case_delta}.")
        next_steps.append("Inspect newly changed cases first; the current panel baseline is noisier than before.")
    elif changed_case_delta is not None and changed_case_delta < 0:
        findings.append(f"Changed case count decreased by {abs(changed_case_delta)}.")

    verdict_delta = dict(summary.get("verdict_counts_delta") or {})
    possible_regression_delta = int(verdict_delta.get("possible_regression", 0))
    high_priority_after = len(list((comparison.get("high_priority_cases") or {}).get("after") or []))
    if possible_regression_delta > 0:
        findings.append(f"`possible_regression` cases increased by {possible_regression_delta}.")
        next_steps.append("Review the cases that newly entered possible_regression before accepting this baseline.")
    if high_priority_after > 0:
        findings.append(f"There are {high_priority_after} high priority cases in the current panel.")
        next_steps.append("Start from the high priority cases list and inspect each comparison.md archive.")

    if not findings:
        findings.append("No significant panel-level regressions were detected against the saved baseline.")
    if not next_steps:
        next_steps.append("If this panel is the new expected state, store it as the next baseline archive.")

    verdict = "possible_regression" if possible_regression_delta > 0 else ("changed" if changed_case_delta else "stable")
    priority = "high" if possible_regression_delta > 0 or high_priority_after > 0 else ("medium" if changed_case_delta else "low")
    return {
        "verdict": verdict,
        "priority": priority,
        "findings": findings,
        "next_steps": next_steps,
    }


def _panel_threshold_check(*, metric: str, actual: int | None, expected: int) -> dict[str, object]:
    passed = actual is not None and actual <= expected
    return {
        "metric": metric,
        "actual": actual,
        "expected": expected,
        "comparator": "<=",
        "passed": passed,
    }


def _coerce_panel_int(value: object) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    return None
