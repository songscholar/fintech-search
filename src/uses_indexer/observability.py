from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from .constants import TRACE_PRODUCER, TRACE_SCHEMA_VERSION


def _trace_metadata(
    *,
    schema: str,
    parent_trace_id: str | None = None,
) -> dict[str, object]:
    metadata = {
        "trace_id": str(uuid4()),
        "producer": TRACE_PRODUCER,
        "schema": schema,
        "version": TRACE_SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    if parent_trace_id:
        metadata["parent_trace_id"] = parent_trace_id
    return metadata


def build_retrieval_debug_payload(
    *,
    query: str,
    fts_query: str | None,
    candidate_limit: int,
    query_analysis: dict[str, object],
    source_trace: dict[str, list[dict[str, object]]],
    source_counts: dict[str, int],
    reranked: list[dict[str, object]],
    elapsed_ms: float | None = None,
) -> dict[str, object]:
    rank_by_entity = {
        (str(item.get("hit_type") or ""), int(item.get("entity_id") or 0)): index
        for index, item in enumerate(reranked, start=1)
    }
    rerank_preview = [
        {
            "procedure_name": str(item.get("procedure_name") or ""),
            "matched_text": str(item.get("matched_text") or ""),
            "rank_after": rank_by_entity.get((str(item.get("hit_type") or ""), int(item.get("entity_id") or 0))),
            "score": round(float(item.get("score") or 0.0), 6),
            "reasons": list(item.get("reasons") or []),
            "score_before_rerank": round(float((item.get("debug_rerank") or {}).get("score_before_rerank") or 0.0), 6),
            "score_after_rerank": round(float((item.get("debug_rerank") or {}).get("score_after_rerank") or 0.0), 6),
            "score_after_call_chain": round(float((item.get("debug_rerank") or {}).get("score_after_call_chain") or item.get("score") or 0.0), 6),
            "breakdown": dict((item.get("debug_rerank") or {}).get("score_breakdown") or {}),
        }
        for item in reranked[:20]
    ]
    retrieval_contributions = {
        source: {
            "candidate_count": int(source_counts.get(source, 0)),
            "top_candidates": items,
        }
        for source, items in source_trace.items()
    }
    trace_sources = [
        {
            "source": source,
            "candidate_count": int(source_counts.get(source, 0)),
            "top_candidates": items,
        }
        for source, items in source_trace.items()
    ]
    metadata = _trace_metadata(schema="uses_indexer.debug.retrieval")
    return {
        "schema": "uses_indexer.debug.retrieval",
        "version": TRACE_SCHEMA_VERSION,
        "metadata": metadata,
        "query_analysis": query_analysis,
        "retrieval_contributions": retrieval_contributions,
        "rerank_preview": rerank_preview,
        "trace": {
            "stage": "retrieval",
            "elapsed_ms": round(float(elapsed_ms or 0.0), 3),
            "query": query,
            "fts_query": fts_query,
            "candidate_limit": int(candidate_limit),
            "query_analysis": query_analysis,
            "summary": {
                "source_count": len(source_trace),
                "merged_candidate_count": sum(int(source_counts.get(source, 0)) for source in source_trace),
                "reranked_candidate_count": len(reranked),
            },
            "sources": trace_sources,
            "rerank": {
                "candidate_count": len(reranked),
                "top_candidates": rerank_preview,
            },
        },
    }


def build_evidence_debug_payload(
    *,
    query: str,
    limit: int,
    context_window: int,
    related_limit: int,
    retrieval_debug: dict[str, object] | None,
    pruned_events: list[dict[str, object]],
    evidence_blocks: list[dict[str, object]],
    elapsed_ms: float | None = None,
) -> dict[str, object]:
    selected_evidence = [
        {
            "rank": int(block["rank"]),
            "procedure_name": str(block["procedure_name"]),
            "line_start": int(block["line_start"]),
            "line_end": int(block["line_end"]),
            "hit_type": str(block["hit_type"]),
            "retrieval_source": str(block["retrieval_source"]),
        }
        for block in evidence_blocks
    ]
    evidence_pruning = {
        "events": pruned_events[:50],
        "total_pruned": len(pruned_events),
    }
    retrieval_trace_id = None
    if isinstance(retrieval_debug, dict):
        metadata = retrieval_debug.get("metadata", {})
        if isinstance(metadata, dict):
            retrieval_trace_id = str(metadata.get("trace_id") or "") or None
    metadata = _trace_metadata(
        schema="uses_indexer.debug.evidence",
        parent_trace_id=retrieval_trace_id,
    )
    return {
        "schema": "uses_indexer.debug.evidence",
        "version": TRACE_SCHEMA_VERSION,
        "metadata": metadata,
        "retrieval": retrieval_debug,
        "evidence_pruning": evidence_pruning,
        "trace": {
            "stage": "evidence",
            "elapsed_ms": round(float(elapsed_ms or 0.0), 3),
            "query": query,
            "selection_limit": int(limit),
            "context_window": int(context_window),
            "related_limit": int(related_limit),
            "retrieval_trace": (retrieval_debug or {}).get("trace"),
            "summary": {
                "selected_count": len(selected_evidence),
                "pruned_count": len(pruned_events),
                "retrieval_trace_id": retrieval_trace_id,
            },
            "selection": {
                "selected_count": len(selected_evidence),
                "selected_evidence": selected_evidence,
                "pruned_count": len(pruned_events),
                "pruned_events": pruned_events[:50],
            },
        },
    }


def build_incremental_trace(
    *,
    index_type: str,
    current_file_count: int,
    stored_file_count: int,
    added_paths: list[str],
    changed_paths: list[str],
    removed_paths: list[str],
    affected_units: list[dict[str, object]],
    rebuild_scope: dict[str, object] | None,
    vector_stats: dict[str, object],
    elapsed_ms: float | None = None,
) -> dict[str, object]:
    reindexed_paths = sorted([*added_paths, *changed_paths])
    return {
        "schema": "uses_indexer.debug.incremental_build",
        "version": TRACE_SCHEMA_VERSION,
        "metadata": _trace_metadata(schema="uses_indexer.debug.incremental_build"),
        "trace": {
            "stage": "incremental_build",
            "elapsed_ms": round(float(elapsed_ms or 0.0), 3),
            "index_type": index_type,
            "file_scan": {
                "current_file_count": int(current_file_count),
                "stored_file_count": int(stored_file_count),
            },
            "changes": {
                "added_count": len(added_paths),
                "changed_count": len(changed_paths),
                "removed_count": len(removed_paths),
                "added": added_paths,
                "changed": changed_paths,
                "removed": removed_paths,
                "reindexed": reindexed_paths,
            },
            "impact": {
                "affected_unit_count": len(affected_units),
                "affected_units": affected_units,
            },
            "rebuild_scope": rebuild_scope or {"summary": {}, "items": []},
            "vector_stats": vector_stats,
            "summary": {
                "reindexed_count": len(reindexed_paths),
                "affected_unit_count": len(affected_units),
                "rebuild_target_statement_count": int(((rebuild_scope or {}).get("summary") or {}).get("rebuild_target_statement_count") or 0),
                "rebuild_target_chunk_count": int(((rebuild_scope or {}).get("summary") or {}).get("rebuild_target_chunk_count") or 0),
                "rebuild_target_block_count": int(((rebuild_scope or {}).get("summary") or {}).get("rebuild_target_block_count") or 0),
                "after_chunk_count": int(((rebuild_scope or {}).get("summary") or {}).get("after_chunk_count") or 0),
                "after_block_count": int(((rebuild_scope or {}).get("summary") or {}).get("after_block_count") or 0),
            },
        },
    }
