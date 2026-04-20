from __future__ import annotations

import json
import os
import sqlite3
from heapq import nlargest
from pathlib import Path
from typing import TYPE_CHECKING

from .embeddings import EmbeddingRequestError, dot_similarity
from .rerank import (
    analyze_query,
    apply_call_chain_rerank,
    rerank_candidate,
    vector_hint_tokens,
)


VECTOR_SIMILARITY_THRESHOLD = 0.05

if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


class RetrievalService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner

    def query_index(
        self,
        db_path: str | Path,
        query: str,
        limit: int = 20,
        *,
        debug: bool = False,
    ) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        candidates, fts_query, vector_status, retrieval_debug = self.retrieve_candidates(
            conn,
            db_path=db_path,
            query=query,
            candidate_limit=max(limit * 6, 30),
            debug=debug,
        )
        conn.close()

        hits = [
            _public_hit(candidate, rank=index)
            for index, candidate in enumerate(candidates[:limit], start=1)
        ]

        payload = {
            "db_path": str(db_path),
            "query": query,
            "fts_query": fts_query,
            "retrieval_strategy": "fts(block/chunk/procedure/action/statement/edge) + vector(if compatible) + sql fallback + python rerank",
            "vector_status": vector_status,
            "candidate_count": len(candidates),
            "hit_count": len(hits),
            "hits": hits,
        }
        if debug:
            payload["debug"] = retrieval_debug
        return payload

    def retrieve_candidates(
        self,
        conn: sqlite3.Connection,
        *,
        db_path: str | Path,
        query: str,
        candidate_limit: int,
        debug: bool = False,
    ) -> tuple[list[dict[str, object]], str | None, dict[str, object], dict[str, object] | None]:
        fts_query = self.owner._build_fts_query(query)
        query_analysis = analyze_query(query)
        candidates: dict[tuple[object, ...], dict[str, object]] = {}
        vector_status = self.owner._vector_status(conn)
        source_trace: dict[str, list[dict[str, object]]] = {}

        if fts_query:
            fts_candidates = self.owner._run_fts_queries(conn, raw_query=query, fts_query=fts_query, limit=candidate_limit)
            source_trace["fts"] = [self._trace_candidate(item) for item in fts_candidates[:20]]
            for candidate in fts_candidates:
                self.owner._merge_candidate(candidates, candidate)

        vector_candidates, vector_status = self._run_vector_queries(
            conn,
            db_path=db_path,
            query=query,
            limit=candidate_limit,
            initial_status=vector_status,
        )
        source_trace["vector"] = [self._trace_candidate(item) for item in vector_candidates[:20]]
        for candidate in vector_candidates:
            self.owner._merge_candidate(candidates, candidate)

        like_candidates = self.owner._run_like_queries(conn, query=query, limit=candidate_limit)
        source_trace["like"] = [self._trace_candidate(item) for item in like_candidates[:20]]
        for candidate in like_candidates:
            self.owner._merge_candidate(candidates, candidate)

        merged = list(candidates.values())
        for candidate in merged:
            candidate["debug_retrieval"] = {
                "retrieval_source": candidate.get("retrieval_source"),
                "matched_via": list(candidate.get("matched_via", [])),
                "source_rank": candidate.get("source_rank"),
            }

        reranked = [
            rerank_candidate(candidate, query=query, query_analysis=query_analysis)
            for candidate in merged
        ]
        reranked.sort(
            key=lambda item: (-float(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"]))
        )
        reranked = apply_call_chain_rerank(
            reranked,
            seed_limit=min(candidate_limit, 12),
            query_analysis=query_analysis,
            procedure_call_neighbors=lambda procedure_name: self.owner._procedure_call_neighbors(
                conn,
                procedure_name=procedure_name,
            ),
        )

        retrieval_debug = None
        if debug:
            retrieval_debug = {
                "query_analysis": query_analysis,
                "retrieval_contributions": {
                    source: {
                        "candidate_count": len(items),
                        "top_candidates": items,
                    }
                    for source, items in source_trace.items()
                },
                "rerank_preview": [
                    {
                        "procedure_name": str(item.get("procedure_name") or ""),
                        "matched_text": str(item.get("matched_text") or ""),
                        "score": round(float(item.get("score") or 0.0), 6),
                        "reasons": list(item.get("reasons") or []),
                        "breakdown": dict((item.get("debug_rerank") or {}).get("score_breakdown") or {}),
                    }
                    for item in reranked[:20]
                ],
            }

        return reranked, fts_query, vector_status, retrieval_debug

    def _run_vector_queries(
        self,
        conn: sqlite3.Connection,
        *,
        db_path: str | Path,
        query: str,
        limit: int,
        initial_status: dict[str, object],
    ) -> tuple[list[dict[str, object]], dict[str, object]]:
        if not bool(initial_status.get("enabled")):
            return [], initial_status

        try:
            query_vector = self.owner.embedder.embed_texts([query])[0]
        except EmbeddingRequestError as exc:
            return [], {
                **initial_status,
                "enabled": False,
                "reason": "query_embedding_failed",
                "detail": str(exc),
            }

        if not any(query_vector):
            return [], {
                **initial_status,
                "enabled": False,
                "reason": "empty_query_vector",
            }
        overlap_hints = vector_hint_tokens(query)

        candidates = []
        try:
            vector_rows = self.owner._load_chunk_vector_cache(conn, db_path)
        except sqlite3.OperationalError:
            return [], {
                **initial_status,
                "enabled": False,
                "reason": "vector_cache_unavailable",
            }

        for row in vector_rows:
            similarity = dot_similarity(query_vector, row["vector"])
            if similarity <= VECTOR_SIMILARITY_THRESHOLD:
                continue
            search_text = f"{row['summary_text']} {row['content']}".lower()
            if overlap_hints and not any(hint in search_text for hint in overlap_hints):
                continue
            candidate = {
                "hit_type": "chunk",
                "entity_id": int(row["chunk_id"]),
                "procedure_id": int(row["procedure_id"]),
                "file_id": int(row["file_id"]),
                "statement_id": None,
                "file_path": str(row["file_path"]),
                "procedure_name": str(row["procedure_name"]),
                "chinese_name": row["chinese_name"] if row["chinese_name"] else None,
                "object_id": row["object_id"] if row["object_id"] else None,
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "matched_text": str(row["summary_text"]),
                "match_source": "chunk_vector",
                "retrieval_source": "vector_chunk",
                "base_score": 84.0,
                "source_rank": similarity * 18.0,
                "search_text": search_text,
                "reasons": [f"vector_similarity={similarity:.3f}"],
            }
            candidates.append(candidate)

        return nlargest(limit, candidates, key=lambda item: float(item["source_rank"])), {
            **initial_status,
            "reason": "enabled",
        }

    def _trace_candidate(self, candidate: dict[str, object]) -> dict[str, object]:
        return {
            "hit_type": str(candidate.get("hit_type") or ""),
            "procedure_name": str(candidate.get("procedure_name") or ""),
            "file_path": str(candidate.get("file_path") or ""),
            "matched_text": str(candidate.get("matched_text") or ""),
            "match_source": str(candidate.get("match_source") or ""),
            "retrieval_source": str(candidate.get("retrieval_source") or ""),
            "base_score": round(float(candidate.get("base_score") or 0.0), 3),
            "source_rank": round(float(candidate.get("source_rank") or 0.0), 3),
        }


def _public_hit(candidate: dict[str, object], *, rank: int) -> dict[str, object]:
    return {
        "rank": rank,
        "score": round(float(candidate["score"]), 3),
        "hit_type": candidate["hit_type"],
        "retrieval_source": candidate["retrieval_source"],
        "match_source": candidate["match_source"],
        "procedure_name": candidate["procedure_name"],
        "chinese_name": candidate.get("chinese_name"),
        "object_id": candidate.get("object_id"),
        "file_path": candidate["file_path"],
        "line_start": candidate["line_start"],
        "line_end": candidate["line_end"],
        "matched_text": candidate["matched_text"],
        "reasons": list(candidate["reasons"]),
        "matched_via": list(candidate.get("matched_via", [])),
    }
