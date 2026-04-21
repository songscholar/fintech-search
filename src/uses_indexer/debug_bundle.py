from __future__ import annotations

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
