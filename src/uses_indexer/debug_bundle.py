from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .answering import CodebaseAnswerer
from .indexer import SQLiteIndexer


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

    return {
        "bundle_kind": "debug_bundle_comparison",
        "before_path": str(before_path),
        "after_path": str(after_path),
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


def _load_debug_bundle(path: str | Path) -> dict[str, object]:
    candidate = Path(path)
    if candidate.is_dir():
        candidate = candidate / "bundle.json"
    payload = json.loads(candidate.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Debug bundle must be a JSON object: {candidate}")
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
