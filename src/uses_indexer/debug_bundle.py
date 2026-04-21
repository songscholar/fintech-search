from __future__ import annotations

import json
from pathlib import Path

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
            "query": bundle["query"]["response_kind"],
            "evidence": bundle["evidence"]["response_kind"],
            "answer": bundle["answer"]["response_kind"],
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
