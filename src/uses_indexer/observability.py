from __future__ import annotations


TRACE_SCHEMA_VERSION = "1.0"


def build_retrieval_debug_payload(
    *,
    query: str,
    fts_query: str | None,
    candidate_limit: int,
    query_analysis: dict[str, object],
    source_trace: dict[str, list[dict[str, object]]],
    source_counts: dict[str, int],
    reranked: list[dict[str, object]],
) -> dict[str, object]:
    rerank_preview = [
        {
            "procedure_name": str(item.get("procedure_name") or ""),
            "matched_text": str(item.get("matched_text") or ""),
            "score": round(float(item.get("score") or 0.0), 6),
            "reasons": list(item.get("reasons") or []),
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
    return {
        "schema": "uses_indexer.debug.retrieval",
        "version": TRACE_SCHEMA_VERSION,
        "query_analysis": query_analysis,
        "retrieval_contributions": retrieval_contributions,
        "rerank_preview": rerank_preview,
        "trace": {
            "stage": "retrieval",
            "query": query,
            "fts_query": fts_query,
            "candidate_limit": int(candidate_limit),
            "query_analysis": query_analysis,
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
    return {
        "schema": "uses_indexer.debug.evidence",
        "version": TRACE_SCHEMA_VERSION,
        "retrieval": retrieval_debug,
        "evidence_pruning": evidence_pruning,
        "trace": {
            "stage": "evidence",
            "query": query,
            "selection_limit": int(limit),
            "context_window": int(context_window),
            "related_limit": int(related_limit),
            "retrieval_trace": (retrieval_debug or {}).get("trace"),
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
    vector_stats: dict[str, object],
) -> dict[str, object]:
    reindexed_paths = sorted([*added_paths, *changed_paths])
    return {
        "schema": "uses_indexer.debug.incremental_build",
        "version": TRACE_SCHEMA_VERSION,
        "trace": {
            "stage": "incremental_build",
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
            "vector_stats": vector_stats,
        },
    }
