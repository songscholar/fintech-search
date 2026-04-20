from __future__ import annotations

import json
import os
import sqlite3
import time
from heapq import nlargest
from pathlib import Path
from typing import TYPE_CHECKING

from .constants import VECTOR_SIMILARITY_THRESHOLD
from .embeddings import EmbeddingRequestError, dot_similarity
from .index_utils import build_fts_query, merge_candidate
from .observability import build_retrieval_debug_payload
from .response_schema import apply_response_envelope
from .rerank import (
    analyze_query,
    apply_call_chain_rerank,
    rerank_candidate,
    vector_hint_tokens,
)
from .semantic_recovery import maybe_int

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
        return apply_response_envelope(payload, kind="query")

    def retrieve_candidates(
        self,
        conn: sqlite3.Connection,
        *,
        db_path: str | Path,
        query: str,
        candidate_limit: int,
        debug: bool = False,
    ) -> tuple[list[dict[str, object]], str | None, dict[str, object], dict[str, object] | None]:
        started_at = time.perf_counter()
        context_fetch = self.owner._context_fetch_service
        fts_query = build_fts_query(query)
        query_analysis = analyze_query(query)
        candidates: dict[tuple[object, ...], dict[str, object]] = {}
        vector_status = self._vector_status(conn)
        source_trace: dict[str, list[dict[str, object]]] = {}
        source_counts: dict[str, int] = {}

        if fts_query:
            fts_candidates = self._run_fts_queries(conn, raw_query=query, fts_query=fts_query, limit=candidate_limit)
            source_trace["fts"] = [self._trace_candidate(item) for item in fts_candidates[:20]]
            source_counts["fts"] = len(fts_candidates)
            for candidate in fts_candidates:
                merge_candidate(candidates, candidate)

        vector_candidates, vector_status = self._run_vector_queries(
            conn,
            db_path=db_path,
            query=query,
            limit=candidate_limit,
            initial_status=vector_status,
        )
        source_trace["vector"] = [self._trace_candidate(item) for item in vector_candidates[:20]]
        source_counts["vector"] = len(vector_candidates)
        for candidate in vector_candidates:
            merge_candidate(candidates, candidate)

        like_candidates = self._run_like_queries(conn, query=query, limit=candidate_limit)
        source_trace["like"] = [self._trace_candidate(item) for item in like_candidates[:20]]
        source_counts["like"] = len(like_candidates)
        for candidate in like_candidates:
            merge_candidate(candidates, candidate)

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
            procedure_call_neighbors=lambda procedure_name: context_fetch.procedure_call_neighbors(
                conn,
                procedure_name=procedure_name,
            ),
        )

        retrieval_debug = None
        if debug:
            retrieval_debug = build_retrieval_debug_payload(
                query=query,
                fts_query=fts_query,
                candidate_limit=candidate_limit,
                query_analysis=query_analysis,
                source_trace=source_trace,
                source_counts=source_counts,
                reranked=reranked,
                elapsed_ms=(time.perf_counter() - started_at) * 1000.0,
            )

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
            vector_rows = self._load_chunk_vector_cache(conn, db_path)
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

    def _vector_status(self, conn: sqlite3.Connection) -> dict[str, object]:
        db_provider = self.owner._metadata(conn, "embedding_provider")
        db_model = self.owner._metadata(conn, "embedding_model")
        db_dimension_raw = self.owner._metadata(conn, "embedding_dimension")
        vector_enabled = (self.owner._metadata(conn, "vector_enabled") or "").lower() == "true"
        vector_count = int(conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0])

        current_info = self.owner.embedder.info
        status = {
            "enabled": False,
            "reason": "metadata_missing",
            "index_provider": db_provider,
            "index_model": db_model,
            "index_dimension": maybe_int(db_dimension_raw),
            "query_provider": current_info.provider,
            "query_model": current_info.model,
            "query_dimension": current_info.dimension,
        }

        if not vector_enabled or vector_count == 0:
            status["reason"] = "vector_index_unavailable"
            return status

        if not db_provider or not db_model:
            return status

        if current_info.provider != db_provider or current_info.model != db_model:
            status["reason"] = "embedding_space_mismatch"
            return status

        db_dimension = maybe_int(db_dimension_raw)
        if db_dimension and current_info.dimension and current_info.dimension != db_dimension:
            status["reason"] = "embedding_space_mismatch"
            return status

        status["enabled"] = True
        status["reason"] = "compatible"
        return status

    def _load_chunk_vector_cache(
        self,
        conn: sqlite3.Connection,
        db_path: str | Path,
    ) -> list[dict[str, object]]:
        db_file = Path(db_path)
        stat = os.stat(db_file)
        embedder_info = self.owner.embedder.info
        cache_key = (
            str(db_file.resolve()),
            stat.st_mtime_ns,
            stat.st_size,
            embedder_info.provider,
            embedder_info.model,
        )
        cached = self.owner._vector_cache.get(cache_key)
        if cached is not None:
            return cached

        self.owner._vector_cache = {
            key: value
            for key, value in self.owner._vector_cache.items()
            if key == cache_key
        }

        rows = conn.execute(
            """
            SELECT
              cv.chunk_id AS chunk_id,
              c.procedure_id AS procedure_id,
              c.file_id AS file_id,
              f.path AS file_path,
              p.name AS procedure_name,
              p.chinese_name AS chinese_name,
              p.object_id AS object_id,
              c.line_start AS line_start,
              c.line_end AS line_end,
              c.summary_text AS summary_text,
              c.content AS content,
              cv.vector_json AS vector_json
            FROM chunk_vectors cv
            JOIN chunks c ON c.id = cv.chunk_id
            JOIN procedures p ON p.id = c.procedure_id
            JOIN files f ON f.id = c.file_id
            WHERE cv.provider = ? AND cv.model = ?
            """,
            (
                embedder_info.provider,
                embedder_info.model,
            ),
        ).fetchall()

        cached_rows = [
            {
                "chunk_id": int(row["chunk_id"]),
                "procedure_id": int(row["procedure_id"]),
                "file_id": int(row["file_id"]),
                "file_path": str(row["file_path"]),
                "procedure_name": str(row["procedure_name"]),
                "chinese_name": row["chinese_name"] if row["chinese_name"] else None,
                "object_id": row["object_id"] if row["object_id"] else None,
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "summary_text": str(row["summary_text"]),
                "content": str(row["content"]),
                "vector": [float(value) for value in json.loads(row["vector_json"])],
            }
            for row in rows
        ]
        self.owner._vector_cache[cache_key] = cached_rows
        return cached_rows

    def _run_fts_queries(
        self,
        conn: sqlite3.Connection,
        *,
        raw_query: str,
        fts_query: str,
        limit: int,
    ) -> list[dict[str, object]]:
        queries = [
            (
                """
                SELECT
                  'block' AS hit_type,
                  113.0 AS base_score,
                  'fts_block' AS retrieval_source,
                  b.id AS entity_id,
                  b.procedure_id AS procedure_id,
                  b.file_id AS file_id,
                  b.anchor_statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  b.line_start AS line_start,
                  b.line_end AS line_end,
                  COALESCE(NULLIF(b.summary_text, ''), b.block_type) AS matched_text,
                  'block_summary' AS match_source,
                  -bm25(blocks_fts, 2.0, 1.0, 1.0, 1.0, 6.0, 4.0) AS source_rank,
                  COALESCE(b.summary_text, '') || ' ' || COALESCE(b.excerpt, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM blocks_fts
                JOIN blocks b ON b.id = blocks_fts.rowid
                JOIN procedures p ON p.id = b.procedure_id
                JOIN files f ON f.id = b.file_id
                WHERE blocks_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
            (
                """
                SELECT
                  'chunk' AS hit_type,
                  111.0 AS base_score,
                  'fts_chunk' AS retrieval_source,
                  c.id AS entity_id,
                  c.procedure_id AS procedure_id,
                  c.file_id AS file_id,
                  NULL AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  c.line_start AS line_start,
                  c.line_end AS line_end,
                  COALESCE(NULLIF(c.summary_text, ''), c.chunk_type) AS matched_text,
                  'chunk_summary' AS match_source,
                  -bm25(chunks_fts, 2.0, 1.5, 1.0, 6.0, 4.0) AS source_rank,
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.content, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM chunks_fts
                JOIN chunks c ON c.id = chunks_fts.rowid
                JOIN procedures p ON p.id = c.procedure_id
                JOIN files f ON f.id = c.file_id
                WHERE chunks_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
            (
                """
                SELECT
                  'procedure' AS hit_type,
                  115.0 AS base_score,
                  'fts_procedure' AS retrieval_source,
                  p.id AS entity_id,
                  p.id AS procedure_id,
                  f.id AS file_id,
                  NULL AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  NULL AS line_start,
                  NULL AS line_end,
                  COALESCE(NULLIF(p.chinese_name, ''), p.name) AS matched_text,
                  'procedure_fts' AS match_source,
                  -bm25(procedures_fts, 8.0, 5.0, 2.0) AS source_rank,
                  COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') || ' ' || COALESCE(p.object_id, '') || ' ' || COALESCE(f.path, '') AS search_text
                FROM procedures_fts
                JOIN procedures p ON p.id = procedures_fts.rowid
                JOIN files f ON f.id = p.file_id
                WHERE procedures_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
            (
                """
                SELECT
                  'action' AS hit_type,
                  108.0 AS base_score,
                  'fts_action' AS retrieval_source,
                  a.id AS entity_id,
                  a.procedure_id AS procedure_id,
                  a.file_id AS file_id,
                  a.statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  CASE
                    WHEN instr(COALESCE(a.action_name, ''), ?) > 0 THEN COALESCE(a.action_name, '')
                    WHEN instr(COALESCE(a.target_name, ''), ?) > 0 THEN COALESCE(a.target_name, '')
                    ELSE COALESCE(NULLIF(a.target_name, ''), a.action_name)
                  END AS matched_text,
                  CASE
                    WHEN instr(COALESCE(a.action_name, ''), ?) > 0 THEN 'action_name'
                    WHEN instr(COALESCE(a.target_name, ''), ?) > 0 THEN 'action_target'
                    ELSE 'action_fts'
                  END AS match_source,
                  -bm25(actions_fts, 7.0, 4.0, 2.0, 1.0, 1.0) AS source_rank,
                  COALESCE(a.action_name, '') || ' ' || COALESCE(a.target_name, '') || ' ' || COALESCE(s.raw, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM actions_fts
                JOIN actions a ON a.id = actions_fts.rowid
                JOIN procedures p ON p.id = a.procedure_id
                JOIN files f ON f.id = a.file_id
                JOIN statements s ON s.id = a.statement_id
                WHERE actions_fts MATCH ?
                LIMIT ?
                """,
                (raw_query, raw_query, raw_query, raw_query, fts_query, limit),
            ),
            (
                """
                SELECT
                  'statement' AS hit_type,
                  98.0 AS base_score,
                  'fts_statement' AS retrieval_source,
                  s.id AS entity_id,
                  s.procedure_id AS procedure_id,
                  s.file_id AS file_id,
                  s.id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  s.raw AS matched_text,
                  s.kind AS match_source,
                  -bm25(statements_fts, 6.0, 2.0, 2.0, 2.0, 1.5, 1.0) AS source_rank,
                  COALESCE(s.raw, '') || ' ' || COALESCE(s.name, '') || ' ' || COALESCE(s.condition, '') || ' ' || COALESCE(s.target, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM statements_fts
                JOIN statements s ON s.id = statements_fts.rowid
                JOIN procedures p ON p.id = s.procedure_id
                JOIN files f ON f.id = s.file_id
                WHERE statements_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
            (
                """
                SELECT
                  'edge' AS hit_type,
                  86.0 AS base_score,
                  'fts_edge' AS retrieval_source,
                  e.id AS entity_id,
                  e.procedure_id AS procedure_id,
                  e.file_id AS file_id,
                  e.statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  e.target_name AS matched_text,
                  e.edge_type AS match_source,
                  -bm25(edges_fts, 5.0, 1.0, 4.0, 1.0, 1.0, 1.0) AS source_rank,
                  COALESCE(e.edge_type, '') || ' ' || COALESCE(e.source_name, '') || ' ' || COALESCE(e.target_name, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM edges_fts
                JOIN edges e ON e.id = edges_fts.rowid
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = e.file_id
                LEFT JOIN statements s ON s.id = e.statement_id
                WHERE edges_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
        ]

        hits: list[dict[str, object]] = []
        for sql, params in queries:
            try:
                rows = conn.execute(sql, params).fetchall()
            except sqlite3.OperationalError:
                continue
            hits.extend(_row_to_hit(row) for row in rows)
        return hits

    def _run_like_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query: str,
        limit: int,
    ) -> list[dict[str, object]]:
        like = f"%{query}%"
        queries = [
            (
                """
                SELECT
                  'block' AS hit_type,
                  79.0 AS base_score,
                  'like_block' AS retrieval_source,
                  b.id AS entity_id,
                  b.procedure_id AS procedure_id,
                  b.file_id AS file_id,
                  b.anchor_statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  b.line_start AS line_start,
                  b.line_end AS line_end,
                  COALESCE(NULLIF(b.summary_text, ''), b.block_type) AS matched_text,
                  'block_summary' AS match_source,
                  0.0 AS source_rank,
                  COALESCE(b.summary_text, '') || ' ' || COALESCE(b.excerpt, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM blocks b
                JOIN procedures p ON p.id = b.procedure_id
                JOIN files f ON f.id = b.file_id
                WHERE COALESCE(b.summary_text, '') LIKE ? OR COALESCE(b.excerpt, '') LIKE ? OR COALESCE(b.anchor_name, '') LIKE ?
                LIMIT ?
                """,
                (like, like, like, limit),
            ),
            (
                """
                SELECT
                  'chunk' AS hit_type,
                  74.0 AS base_score,
                  'like_chunk' AS retrieval_source,
                  c.id AS entity_id,
                  c.procedure_id AS procedure_id,
                  c.file_id AS file_id,
                  NULL AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  c.line_start AS line_start,
                  c.line_end AS line_end,
                  COALESCE(NULLIF(c.summary_text, ''), c.chunk_type) AS matched_text,
                  'chunk_summary' AS match_source,
                  0.0 AS source_rank,
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.content, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text
                FROM chunks c
                JOIN procedures p ON p.id = c.procedure_id
                JOIN files f ON f.id = c.file_id
                WHERE COALESCE(c.summary_text, '') LIKE ? OR COALESCE(c.content, '') LIKE ?
                LIMIT ?
                """,
                (like, like, limit),
            ),
            (
                """
                SELECT
                  'procedure' AS hit_type,
                  78.0 AS base_score,
                  'like_procedure' AS retrieval_source,
                  p.id AS entity_id,
                  p.id AS procedure_id,
                  f.id AS file_id,
                  NULL AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  NULL AS line_start,
                  NULL AS line_end,
                  CASE
                    WHEN p.name LIKE ? THEN p.name
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN COALESCE(p.chinese_name, '')
                    WHEN COALESCE(p.object_id, '') LIKE ? THEN COALESCE(p.object_id, '')
                    ELSE f.path
                  END AS matched_text,
                  CASE
                    WHEN p.name LIKE ? THEN 'procedure_name'
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN 'procedure_chinese_name'
                    WHEN COALESCE(p.object_id, '') LIKE ? THEN 'procedure_object_id'
                    ELSE 'file_path'
                  END AS match_source,
                  0.0 AS source_rank,
                  COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') || ' ' || COALESCE(p.object_id, '') || ' ' || COALESCE(f.path, '') AS search_text
                FROM procedures p
                JOIN files f ON f.id = p.file_id
                WHERE p.name LIKE ? OR COALESCE(p.chinese_name, '') LIKE ? OR COALESCE(p.object_id, '') LIKE ? OR f.path LIKE ?
                LIMIT ?
                """,
                (like, like, like, like, like, like, like, like, like, like, limit),
            ),
            (
                """
                SELECT
                  'action' AS hit_type,
                  72.0 AS base_score,
                  'like_action' AS retrieval_source,
                  a.id AS entity_id,
                  a.procedure_id AS procedure_id,
                  a.file_id AS file_id,
                  a.statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  CASE
                    WHEN COALESCE(a.action_name, '') LIKE ? THEN COALESCE(a.action_name, '')
                    ELSE COALESCE(a.target_name, '')
                  END AS matched_text,
                  CASE
                    WHEN COALESCE(a.action_name, '') LIKE ? THEN 'action_name'
                    ELSE 'action_target'
                  END AS match_source,
                  0.0 AS source_rank,
                  COALESCE(a.action_name, '') || ' ' || COALESCE(a.target_name, '') || ' ' || COALESCE(s.raw, '') || ' ' || COALESCE(p.name, '') AS search_text
                FROM actions a
                JOIN procedures p ON p.id = a.procedure_id
                JOIN files f ON f.id = a.file_id
                JOIN statements s ON s.id = a.statement_id
                WHERE COALESCE(a.action_name, '') LIKE ? OR COALESCE(a.target_name, '') LIKE ?
                LIMIT ?
                """,
                (like, like, like, like, limit),
            ),
            (
                """
                SELECT
                  'variable' AS hit_type,
                  68.0 AS base_score,
                  'like_variable' AS retrieval_source,
                  v.id AS entity_id,
                  v.procedure_id AS procedure_id,
                  v.file_id AS file_id,
                  v.statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  v.var_name AS matched_text,
                  v.access_type AS match_source,
                  0.0 AS source_rank,
                  COALESCE(v.var_name, '') || ' ' || COALESCE(s.raw, '') || ' ' || COALESCE(p.name, '') AS search_text
                FROM variable_refs v
                JOIN procedures p ON p.id = v.procedure_id
                JOIN files f ON f.id = v.file_id
                JOIN statements s ON s.id = v.statement_id
                WHERE v.var_name LIKE ?
                LIMIT ?
                """,
                (like, limit),
            ),
            (
                """
                SELECT
                  'statement' AS hit_type,
                  62.0 AS base_score,
                  'like_statement' AS retrieval_source,
                  s.id AS entity_id,
                  s.procedure_id AS procedure_id,
                  s.file_id AS file_id,
                  s.id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  s.raw AS matched_text,
                  s.kind AS match_source,
                  0.0 AS source_rank,
                  COALESCE(s.raw, '') || ' ' || COALESCE(s.name, '') || ' ' || COALESCE(s.condition, '') || ' ' || COALESCE(s.target, '') || ' ' || COALESCE(p.name, '') AS search_text
                FROM statements s
                JOIN procedures p ON p.id = s.procedure_id
                JOIN files f ON f.id = s.file_id
                WHERE s.raw LIKE ?
                LIMIT ?
                """,
                (like, limit),
            ),
            (
                """
                SELECT
                  'edge' AS hit_type,
                  58.0 AS base_score,
                  'like_edge' AS retrieval_source,
                  e.id AS entity_id,
                  e.procedure_id AS procedure_id,
                  e.file_id AS file_id,
                  e.statement_id AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  e.target_name AS matched_text,
                  e.edge_type AS match_source,
                  0.0 AS source_rank,
                  COALESCE(e.edge_type, '') || ' ' || COALESCE(e.target_name, '') || ' ' || COALESCE(p.name, '') AS search_text
                FROM edges e
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = e.file_id
                LEFT JOIN statements s ON s.id = e.statement_id
                WHERE e.target_name LIKE ?
                LIMIT ?
                """,
                (like, limit),
            ),
        ]

        hits: list[dict[str, object]] = []
        for sql, params in queries:
            rows = conn.execute(sql, params).fetchall()
            hits.extend(_row_to_hit(row) for row in rows)
        return hits

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


def _row_to_hit(row: sqlite3.Row) -> dict[str, object]:
    return {
        "hit_type": str(row["hit_type"]),
        "entity_id": int(row["entity_id"]),
        "procedure_id": int(row["procedure_id"]),
        "file_id": int(row["file_id"]),
        "statement_id": int(row["statement_id"]) if row["statement_id"] is not None else None,
        "file_path": str(row["file_path"]),
        "procedure_name": str(row["procedure_name"]),
        "chinese_name": row["chinese_name"] if "chinese_name" in row.keys() and row["chinese_name"] else None,
        "object_id": row["object_id"] if "object_id" in row.keys() and row["object_id"] else None,
        "line_start": int(row["line_start"]) if row["line_start"] is not None else None,
        "line_end": int(row["line_end"]) if row["line_end"] is not None else None,
        "matched_text": str(row["matched_text"]),
        "match_source": str(row["match_source"]),
        "retrieval_source": str(row["retrieval_source"]),
        "base_score": float(row["base_score"]),
        "source_rank": float(row["source_rank"]),
        "search_text": str(row["search_text"]),
        "reasons": [],
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
