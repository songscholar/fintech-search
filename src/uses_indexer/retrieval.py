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
from .metadata_store import read_metadata
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

        relation_candidates = self._run_relation_queries(conn, query_analysis=query_analysis, limit=candidate_limit)
        source_trace["relation"] = [self._trace_candidate(item) for item in relation_candidates[:20]]
        source_counts["relation"] = len(relation_candidates)
        for candidate in relation_candidates:
            merge_candidate(candidates, candidate)

        relation_graph_candidates = self._run_relation_graph_queries(
            conn,
            query_analysis=query_analysis,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["relation_graph"] = [self._trace_candidate(item) for item in relation_graph_candidates[:20]]
        source_counts["relation_graph"] = len(relation_graph_candidates)
        for candidate in relation_graph_candidates:
            merge_candidate(candidates, candidate)

        flow_bridge_candidates = self._run_entity_flow_bridge_queries(
            conn,
            query_analysis=query_analysis,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["flow_bridge"] = [self._trace_candidate(item) for item in flow_bridge_candidates[:20]]
        source_counts["flow_bridge"] = len(flow_bridge_candidates)
        for candidate in flow_bridge_candidates:
            merge_candidate(candidates, candidate)

        path_bridge_candidates = self._run_path_bridge_queries(
            conn,
            query_analysis=query_analysis,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["path_bridge"] = [self._trace_candidate(item) for item in path_bridge_candidates[:20]]
        source_counts["path_bridge"] = len(path_bridge_candidates)
        for candidate in path_bridge_candidates:
            merge_candidate(candidates, candidate)

        focus_chain_candidates = self._run_focus_chain_queries(
            conn,
            query_analysis=query_analysis,
            relation_candidates=relation_candidates,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["focus_chain"] = [self._trace_candidate(item) for item in focus_chain_candidates[:20]]
        source_counts["focus_chain"] = len(focus_chain_candidates)
        for candidate in focus_chain_candidates:
            merge_candidate(candidates, candidate)

        entity_path_candidates = self._run_entity_path_queries(
            conn,
            query_analysis=query_analysis,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["entity_path"] = [self._trace_candidate(item) for item in entity_path_candidates[:20]]
        source_counts["entity_path"] = len(entity_path_candidates)
        for candidate in entity_path_candidates:
            merge_candidate(candidates, candidate)

        neighbor_candidates = self._run_neighbor_expansion_queries(
            conn,
            query_analysis=query_analysis,
            relation_candidates=relation_candidates,
            limit=candidate_limit,
        )
        source_trace["neighbor"] = [self._trace_candidate(item) for item in neighbor_candidates[:20]]
        source_counts["neighbor"] = len(neighbor_candidates)
        for candidate in neighbor_candidates:
            merge_candidate(candidates, candidate)

        merged = list(candidates.values())
        self._hydrate_missing_procedure_profiles(conn, merged)
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
        multi_hop_candidates = self._run_multi_hop_expansion_queries(
            conn,
            query_analysis=query_analysis,
            ranked_candidates=reranked,
            limit=max(candidate_limit // 2, 8),
        )
        source_trace["multi_hop"] = [self._trace_candidate(item) for item in multi_hop_candidates[:20]]
        source_counts["multi_hop"] = len(multi_hop_candidates)
        if multi_hop_candidates:
            for candidate in multi_hop_candidates:
                merge_candidate(candidates, candidate)
            reranked = [
                rerank_candidate(candidate, query=query, query_analysis=query_analysis)
                for candidate in candidates.values()
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
        reranked = self._apply_procedure_aggregate_rerank(
            reranked,
            query_analysis=query_analysis,
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

    def _hydrate_missing_procedure_profiles(
        self,
        conn: sqlite3.Connection,
        candidates: list[dict[str, object]],
    ) -> None:
        procedure_ids = sorted(
            {
                int(candidate["procedure_id"])
                for candidate in candidates
                if candidate.get("procedure_id") is not None and not candidate.get("procedure_profile")
            }
        )
        if not procedure_ids:
            return
        placeholders = ",".join("?" for _ in procedure_ids)
        rows = conn.execute(
            f"""
            SELECT procedure_id, profile_json
            FROM procedure_features
            WHERE procedure_id IN ({placeholders})
            """,
            tuple(procedure_ids),
        ).fetchall()
        profile_map = {
            int(row[0]): json.loads(str(row[1]))
            for row in rows
            if row[1]
        }
        for candidate in candidates:
            procedure_id = candidate.get("procedure_id")
            if procedure_id is None or candidate.get("procedure_profile"):
                continue
            candidate["procedure_profile"] = dict(profile_map.get(int(procedure_id)) or {})

    def _apply_procedure_aggregate_rerank(
        self,
        ranked: list[dict[str, object]],
        *,
        query_analysis: dict[str, object],
    ) -> list[dict[str, object]]:
        if not ranked:
            return ranked

        grouped: dict[tuple[str, str], dict[str, object]] = {}
        for candidate in ranked:
            key = (str(candidate.get("procedure_name") or ""), str(candidate.get("file_path") or ""))
            group = grouped.setdefault(
                key,
                {
                    "score_total": 0.0,
                    "count": 0,
                    "matched_via": set(),
                    "sources": set(),
                },
            )
            group["score_total"] = float(group["score_total"]) + float(candidate.get("score") or 0.0)
            group["count"] = int(group["count"]) + 1
            group["matched_via"].update(candidate.get("matched_via") or [candidate.get("retrieval_source")])
            group["sources"].add(str(candidate.get("retrieval_source") or ""))

        reranked: list[dict[str, object]] = []
        query_type = str(query_analysis.get("query_type") or "")
        for candidate in ranked:
            key = (str(candidate.get("procedure_name") or ""), str(candidate.get("file_path") or ""))
            group = grouped[key]
            aggregate_score = float(group["score_total"])
            aggregate_hits = int(group["count"])
            aggregate_bonus = min(max(aggregate_hits - 1, 0) * 2.0, 6.0)
            if query_type in {"topic_publish", "metadata_definition", "table_write", "table_read", "table_access", "variable_write", "variable_read", "variable_flow"}:
                aggregate_bonus += min(len(group["sources"]) * 0.8, 2.4)
            candidate["aggregate_score"] = round(aggregate_score, 6)
            candidate["aggregate_hit_count"] = aggregate_hits
            candidate["matched_via"] = sorted(str(item) for item in group["matched_via"] if str(item))
            if aggregate_bonus:
                candidate["score"] = round(float(candidate["score"]) + aggregate_bonus, 6)
                reasons = list(candidate.get("reasons", []))
                reasons.append(f"procedure_aggregate_hits={aggregate_hits}")
                reasons.append(f"procedure_aggregate_bonus={aggregate_bonus:.3f}")
                candidate["reasons"] = reasons
                debug_rerank = dict(candidate.get("debug_rerank") or {})
                debug_rerank["procedure_aggregate_score"] = round(aggregate_score, 6)
                debug_rerank["procedure_aggregate_hits"] = aggregate_hits
                debug_rerank["score_after_procedure_aggregate"] = round(float(candidate["score"]), 6)
                candidate["debug_rerank"] = debug_rerank
            reranked.append(candidate)

        return sorted(
            reranked,
            key=lambda item: (-float(item["score"]), -float(item.get("aggregate_score") or 0.0), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"])),
        )

    def _run_focus_chain_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        relation_candidates: list[dict[str, object]],
        limit: int,
    ) -> list[dict[str, object]]:
        tokens = {str(token) for token in query_analysis.get("tokens") or []}
        if not any(
            any(keyword in token for keyword in ("链路", "路径", "流转", "透传"))
            for token in tokens
        ):
            return []
        focus_mode = None
        seed_sources: set[str] = set()
        if query_analysis.get("wants_table_sql"):
            focus_mode = "table"
            seed_sources.add("relation_table_edge")
        elif query_analysis.get("wants_variable"):
            focus_mode = "variable"
            seed_sources.add("relation_variable_edge")
        if focus_mode is None:
            return []

        context_fetch = self.owner._context_fetch_service
        seed_names: list[str] = []
        for item in relation_candidates:
            if str(item.get("retrieval_source") or "") not in seed_sources:
                continue
            procedure_name = str(item.get("procedure_name") or "")
            if procedure_name and procedure_name not in seed_names:
                seed_names.append(procedure_name)
            if len(seed_names) >= 2:
                break
        if not seed_names:
            return []

        focus_term = ""
        if focus_mode == "table":
            focus_term = str((query_analysis.get("table_terms") or [""])[0] or "")
        elif focus_mode == "variable":
            focus_term = str((query_analysis.get("variable_terms") or [""])[0] or "")

        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()
        for procedure_name in seed_names:
            _, incoming_hops = context_fetch.procedure_call_neighbors(
                conn,
                procedure_name=procedure_name,
                max_depth=3,
            )
            for depth in (1, 2):
                for caller_name in sorted(incoming_hops.get(depth, set())):
                    if caller_name == procedure_name:
                        continue
                    key = (caller_name, procedure_name)
                    if key in seen:
                        continue
                    seen.add(key)
                    path = context_fetch.find_shortest_call_path(
                        conn,
                        source_procedure=caller_name,
                        target_procedure=procedure_name,
                        max_depth=4,
                    )
                    if not path or len(path) <= 1:
                        continue
                    summary = context_fetch.lookup_procedure_summary(conn, caller_name)
                    if summary is None:
                        continue
                    row = conn.execute(
                        """
                        SELECT p.id, f.id, p.chinese_name, p.object_id, f.path
                        FROM procedures p
                        JOIN files f ON f.id = p.file_id
                        WHERE lower(p.name) = lower(?) OR lower(COALESCE(p.chinese_name, '')) = lower(?)
                        ORDER BY CASE WHEN lower(p.name) = lower(?) THEN 0 ELSE 1 END
                        LIMIT 1
                        """,
                        (caller_name, caller_name, caller_name),
                    ).fetchone()
                    if row is None:
                        continue
                    path_label = " -> ".join(path)
                    candidates.append(
                        {
                            "hit_type": "procedure",
                            "entity_id": int(row[0]),
                            "procedure_id": int(row[0]),
                            "file_id": int(row[1]),
                            "statement_id": None,
                            "file_path": str(row[4]),
                            "procedure_name": str(summary["procedure_name"]),
                            "chinese_name": row[2] if row[2] else None,
                            "object_id": row[3] if row[3] else None,
                            "line_start": summary.get("line_start"),
                            "line_end": summary.get("line_end"),
                            "matched_text": path_label,
                            "match_source": f"{focus_mode}_chain_context",
                            "retrieval_source": f"relation_{focus_mode}_chain_context",
                            "base_score": 89.0 if focus_mode == "table" else 85.0,
                            "source_rank": 8.9 if focus_mode == "table" else 8.5,
                            "search_text": f"{path_label} {focus_term} {summary.get('summary_text') or ''}",
                            "procedure_summary": str(summary.get("summary_text") or ""),
                            "reasons": [
                                f"{focus_mode}_chain={path_label}",
                                f"{focus_mode}_seed={procedure_name}",
                                f"{focus_mode}_focus={focus_term}",
                            ],
                        }
                    )
                    if len(candidates) >= limit:
                        return candidates
        return candidates[:limit]

    def _run_entity_flow_bridge_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        limit: int,
    ) -> list[dict[str, object]]:
        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()

        def add_table_bridge(table_name: str) -> None:
            rows = conn.execute(
                """
                SELECT
                  p.id,
                  p.file_id,
                  p.name,
                  p.chinese_name,
                  p.object_id,
                  f.path,
                  pf.summary_text,
                  pf.feature_flags_json,
                  pf.profile_json,
                  GROUP_CONCAT(DISTINCT e.edge_type) AS edge_types
                FROM edges e
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = p.file_id
                JOIN procedure_features pf ON pf.procedure_id = p.id
                WHERE lower(e.target_name) = lower(?)
                  AND e.edge_type IN ('reads_table', 'writes_table', 'reads_dynamic_table', 'writes_dynamic_table')
                GROUP BY p.id, p.file_id, p.name, p.chinese_name, p.object_id, f.path, pf.summary_text, pf.feature_flags_json, pf.profile_json
                LIMIT ?
                """,
                (table_name, limit),
            ).fetchall()
            for row in rows:
                edge_types = {part for part in str(row[9] or "").split(",") if part}
                flow_mode = (
                    "read_write"
                    if edge_types & {"reads_table", "reads_dynamic_table"} and edge_types & {"writes_table", "writes_dynamic_table"}
                    else "write"
                    if edge_types & {"writes_table", "writes_dynamic_table"}
                    else "read"
                )
                key = ("table", f"{row[2]}::{row[5]}")
                if key in seen:
                    continue
                seen.add(key)
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[5]),
                        "procedure_name": str(row[2]),
                        "chinese_name": row[3] if row[3] else None,
                        "object_id": row[4] if row[4] else None,
                        "line_start": None,
                        "line_end": None,
                        "matched_text": f"{table_name} ({flow_mode})",
                        "match_source": "table_flow_bridge",
                        "retrieval_source": "relation_table_flow_bridge",
                        "base_score": 93.0,
                        "source_rank": 9.3,
                        "search_text": f"{table_name} {flow_mode} {row[6]}",
                        "procedure_summary": str(row[6]),
                        "feature_flags": json.loads(str(row[7] or "{}")),
                        "procedure_profile": json.loads(str(row[8] or "{}")),
                        "reasons": [f"table_flow_bridge={table_name}", f"table_flow_mode={flow_mode}"],
                    }
                )

        def add_variable_bridge(variable_name: str) -> None:
            rows = conn.execute(
                """
                SELECT
                  p.id,
                  p.file_id,
                  p.name,
                  p.chinese_name,
                  p.object_id,
                  f.path,
                  pf.summary_text,
                  pf.feature_flags_json,
                  pf.profile_json,
                  GROUP_CONCAT(DISTINCT v.access_type) AS access_types
                FROM variable_refs v
                JOIN procedures p ON p.id = v.procedure_id
                JOIN files f ON f.id = p.file_id
                JOIN procedure_features pf ON pf.procedure_id = p.id
                WHERE lower(v.var_name) = lower(?)
                GROUP BY p.id, p.file_id, p.name, p.chinese_name, p.object_id, f.path, pf.summary_text, pf.feature_flags_json, pf.profile_json
                LIMIT ?
                """,
                (variable_name, limit),
            ).fetchall()
            for row in rows:
                access_types = {part for part in str(row[9] or "").split(",") if part}
                flow_mode = (
                    "read_write"
                    if {"read", "write"} <= access_types
                    else "write"
                    if "write" in access_types
                    else "read"
                )
                key = ("variable", f"{row[2]}::{row[5]}")
                if key in seen:
                    continue
                seen.add(key)
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[5]),
                        "procedure_name": str(row[2]),
                        "chinese_name": row[3] if row[3] else None,
                        "object_id": row[4] if row[4] else None,
                        "line_start": None,
                        "line_end": None,
                        "matched_text": f"{variable_name} ({flow_mode})",
                        "match_source": "variable_flow_bridge",
                        "retrieval_source": "relation_variable_flow_bridge",
                        "base_score": 89.0,
                        "source_rank": 8.9,
                        "search_text": f"{variable_name} {flow_mode} {row[6]}",
                        "procedure_summary": str(row[6]),
                        "feature_flags": json.loads(str(row[7] or "{}")),
                        "procedure_profile": json.loads(str(row[8] or "{}")),
                        "reasons": [f"variable_flow_bridge={variable_name}", f"variable_flow_mode={flow_mode}"],
                    }
                )

        for table_name in query_analysis.get("table_terms", [])[:3]:
            add_table_bridge(str(table_name))
        for variable_name in query_analysis.get("variable_terms", [])[:3]:
            add_variable_bridge(str(variable_name))
        return candidates[:limit]

    def _run_entity_path_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        limit: int,
    ) -> list[dict[str, object]]:
        tokens = {str(token) for token in query_analysis.get("tokens") or []}
        if not any(
            any(keyword in token for keyword in ("链路", "路径", "流转", "透传"))
            for token in tokens
        ):
            return []

        context_fetch = self.owner._context_fetch_service
        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()

        def load_seed_procedures(*, mode: str, term: str) -> list[str]:
            if mode == "table":
                rows = conn.execute(
                    """
                    SELECT DISTINCT source_name
                    FROM edges
                    WHERE lower(target_name) = lower(?)
                      AND edge_type IN ('reads_table', 'writes_table', 'reads_dynamic_table', 'writes_dynamic_table')
                    ORDER BY source_name
                    LIMIT 6
                    """,
                    (term,),
                ).fetchall()
                return [str(row[0]) for row in rows]
            rows = conn.execute(
                """
                SELECT DISTINCT source_name
                FROM edges
                WHERE edge_type IN ('reads_variable', 'writes_variable')
                  AND (
                    lower(target_name) = lower(?)
                    OR lower(replace(target_name, '@', '')) = lower(replace(?, '@', ''))
                  )
                ORDER BY source_name
                LIMIT 6
                """,
                (term, term),
            ).fetchall()
            return [str(row[0]) for row in rows]

        def add_path_candidates(*, mode: str, term: str) -> None:
            seed_names = load_seed_procedures(mode=mode, term=term)
            if len(seed_names) < 2:
                return
            first_path = True
            for source_name in seed_names:
                for target_name in seed_names:
                    if source_name == target_name:
                        continue
                    path = context_fetch.find_shortest_call_path(
                        conn,
                        source_procedure=source_name,
                        target_procedure=target_name,
                        max_depth=4,
                    )
                    if not path or len(path) < 2:
                        continue
                    path_label = " -> ".join(path)
                    path_priority = "main" if first_path else "support"
                    first_path = False
                    for step_index, procedure_name in enumerate(path, start=1):
                        row = conn.execute(
                            """
                            SELECT p.id, f.id, p.chinese_name, p.object_id, f.path, pf.summary_text, pf.feature_flags_json, pf.profile_json
                            FROM procedures p
                            JOIN files f ON f.id = p.file_id
                            JOIN procedure_features pf ON pf.procedure_id = p.id
                            WHERE lower(p.name) = lower(?) OR lower(COALESCE(p.chinese_name, '')) = lower(?)
                            ORDER BY CASE WHEN lower(p.name) = lower(?) THEN 0 ELSE 1 END
                            LIMIT 1
                            """,
                            (procedure_name, procedure_name, procedure_name),
                        ).fetchone()
                        if row is None:
                            continue
                        key = (mode, f"{procedure_name}::{path_label}")
                        if key in seen:
                            continue
                        seen.add(key)
                        candidates.append(
                            {
                                "hit_type": "procedure",
                                "entity_id": int(row[0]),
                                "procedure_id": int(row[0]),
                                "file_id": int(row[1]),
                                "statement_id": None,
                                "file_path": str(row[4]),
                                "procedure_name": procedure_name,
                                "chinese_name": row[2] if row[2] else None,
                                "object_id": row[3] if row[3] else None,
                                "line_start": None,
                                "line_end": None,
                                "matched_text": path_label,
                                "match_source": f"{mode}_flow_path",
                                "retrieval_source": f"relation_{mode}_flow_path",
                                "base_score": 96.0 if mode == "table" else 92.0,
                                "source_rank": 9.6 if mode == "table" else 9.2,
                                "search_text": f"{term} {path_label} {row[5]}",
                                "procedure_summary": str(row[5]),
                                "feature_flags": json.loads(str(row[6] or "{}")),
                                "procedure_profile": json.loads(str(row[7] or "{}")),
                                "flow_path_role": (
                                    "endpoint"
                                    if step_index in {1, len(path)}
                                    else "bridge"
                                ),
                                "flow_path_priority": path_priority,
                                "reasons": [
                                    f"{mode}_flow_path={path_label}",
                                    f"{mode}_flow_focus={term}",
                                    f"{mode}_flow_step={step_index}/{len(path)}",
                                    f"{mode}_flow_priority={path_priority}",
                                ],
                            }
                        )
                        if len(candidates) >= limit:
                            return

        for table_name in query_analysis.get("table_terms", [])[:2]:
            add_path_candidates(mode="table", term=str(table_name))
            if len(candidates) >= limit:
                return candidates[:limit]
        for variable_name in query_analysis.get("variable_terms", [])[:2]:
            add_path_candidates(mode="variable", term=str(variable_name))
            if len(candidates) >= limit:
                return candidates[:limit]

        return candidates[:limit]

    def _run_relation_graph_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        limit: int,
    ) -> list[dict[str, object]]:
        focus_specs: list[tuple[str, str, float]] = []
        focus_specs.extend(("table", str(term), 92.0) for term in query_analysis.get("table_terms", [])[:4])
        focus_specs.extend(("variable", str(term), 89.0) for term in query_analysis.get("variable_terms", [])[:4])
        if query_analysis.get("wants_topic"):
            focus_specs.extend(("topic", str(term), 93.0) for term in query_analysis.get("focus_terms", [])[:4])
        if query_analysis.get("wants_metadata"):
            focus_specs.extend(("metadata", str(term), 90.0) for term in query_analysis.get("focus_terms", [])[:4])
        if not focus_specs:
            return []

        rows = conn.execute(
            """
            SELECT
              pf.procedure_id,
              pf.file_id,
              pf.procedure_name,
              pf.summary_text,
              pf.feature_flags_json,
              pf.profile_json,
              p.chinese_name,
              p.object_id,
              f.path
            FROM procedure_features pf
            JOIN procedures p ON p.id = pf.procedure_id
            JOIN files f ON f.id = pf.file_id
            """
        ).fetchall()

        candidates: list[dict[str, object]] = []
        seen: set[tuple[int, str, str]] = set()
        for row in rows:
            profile = json.loads(str(row[5] or "{}"))
            for mode, term, score in focus_specs:
                match_detail = self._match_relation_graph_focus(profile, mode=mode, term=term)
                if not match_detail:
                    continue
                key = (int(row[0]), mode, term.lower())
                if key in seen:
                    continue
                seen.add(key)
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[8]),
                        "procedure_name": str(row[2]),
                        "chinese_name": row[6] if row[6] else None,
                        "object_id": row[7] if row[7] else None,
                        "line_start": None,
                        "line_end": None,
                        "matched_text": match_detail,
                        "match_source": "relation_graph_entity",
                        "retrieval_source": "relation_graph_profile",
                        "base_score": score,
                        "source_rank": score / 10.0,
                        "search_text": f"{term} {match_detail} {row[3]}",
                        "procedure_summary": str(row[3]),
                        "feature_flags": json.loads(str(row[4] or "{}")),
                        "procedure_profile": profile,
                        "reasons": [f"relation_graph_{mode}={term}"],
                    }
                )
                if len(candidates) >= limit:
                    return candidates[:limit]
        return candidates[:limit]

    def _match_relation_graph_focus(
        self,
        profile: dict[str, object],
        *,
        mode: str,
        term: str,
    ) -> str | None:
        lowered = term.lower()
        relation_graph = dict(profile.get("relation_graph") or {})
        if mode == "table":
            for item in relation_graph.get("tables") or []:
                name = str(dict(item).get("name") or "")
                if lowered == name.lower():
                    return f"{name} ({dict(item).get('mode') or 'unknown'})"
        elif mode == "variable":
            for item in relation_graph.get("variables") or []:
                name = str(dict(item).get("name") or "")
                normalized = name.lower().replace("@", "")
                if lowered.replace("@", "") == normalized:
                    return f"{name} ({dict(item).get('mode') or 'unknown'})"
        elif mode == "topic":
            for name in relation_graph.get("topics") or []:
                text = str(name)
                if lowered in text.lower():
                    return text
        elif mode == "metadata":
            for name in relation_graph.get("metadata_refs") or []:
                text = str(name)
                if lowered in text.lower():
                    return text
        return None

    def _run_path_bridge_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        limit: int,
    ) -> list[dict[str, object]]:
        if not query_analysis.get("wants_call_chain"):
            return []
        ordered_terms = [str(term) for term in query_analysis.get("procedure_terms_ordered") or [] if str(term)]
        if len(ordered_terms) < 2:
            return []

        context_fetch = self.owner._context_fetch_service
        candidates: list[dict[str, object]] = []
        seen_names: set[str] = set()

        for index in range(len(ordered_terms) - 1):
            source_name = ordered_terms[index]
            target_name = ordered_terms[index + 1]
            path = context_fetch.find_shortest_call_path(
                conn,
                source_procedure=source_name,
                target_procedure=target_name,
                max_depth=4,
            )
            if not path or len(path) <= 2:
                continue
            path_label = " -> ".join(path)
            intermediates = path[1:-1]
            for step_index, procedure_name in enumerate(intermediates, start=2):
                if procedure_name in seen_names:
                    continue
                seen_names.add(procedure_name)
                summary = context_fetch.lookup_procedure_summary(conn, procedure_name)
                if summary is None:
                    continue
                row = conn.execute(
                    """
                    SELECT p.id, f.id, p.chinese_name, p.object_id, f.path
                    FROM procedures p
                    JOIN files f ON f.id = p.file_id
                    WHERE lower(p.name) = lower(?) OR lower(COALESCE(p.chinese_name, '')) = lower(?)
                    ORDER BY CASE WHEN lower(p.name) = lower(?) THEN 0 ELSE 1 END
                    LIMIT 1
                    """,
                    (procedure_name, procedure_name, procedure_name),
                ).fetchone()
                if row is None:
                    continue
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[4]),
                        "procedure_name": str(summary["procedure_name"]),
                        "chinese_name": row[2] if row[2] else None,
                        "object_id": row[3] if row[3] else None,
                        "line_start": summary.get("line_start"),
                        "line_end": summary.get("line_end"),
                        "matched_text": path_label,
                        "match_source": "procedure_path_bridge",
                        "retrieval_source": "relation_path_bridge",
                        "base_score": 97.0,
                        "source_rank": 9.7,
                        "search_text": f"{path_label} {summary.get('summary_text') or ''}",
                        "procedure_summary": str(summary.get("summary_text") or ""),
                        "reasons": [
                            f"path_bridge={path_label}",
                            f"path_bridge_step={step_index}/{len(path)}",
                            f"path_bridge_pair={source_name}->{target_name}",
                        ],
                    }
                )
                if len(candidates) >= limit:
                    return candidates

        return candidates[:limit]

    def _run_neighbor_expansion_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        relation_candidates: list[dict[str, object]],
        limit: int,
    ) -> list[dict[str, object]]:
        wants_table = bool(query_analysis.get("wants_table_sql"))
        wants_variable = bool(query_analysis.get("wants_variable"))
        wants_failure = bool(query_analysis.get("wants_failure_flow"))
        if not any((wants_table, wants_variable, wants_failure)):
            return []

        context_fetch = self.owner._context_fetch_service
        seed_sources: set[str] = set()
        if wants_table:
            seed_sources.add("relation_table_edge")
        if wants_variable:
            seed_sources.add("relation_variable_edge")
        if wants_failure:
            seed_sources.add("relation_failure_block")
        seeds: list[str] = []
        seen_seed_names: set[str] = set()
        for item in relation_candidates:
            if str(item.get("retrieval_source") or "") not in seed_sources:
                continue
            procedure_name = str(item.get("procedure_name") or "")
            if not procedure_name or procedure_name in seen_seed_names:
                continue
            seen_seed_names.add(procedure_name)
            seeds.append(procedure_name)
            if len(seeds) >= 3:
                break
        if not seeds:
            return []

        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, str, str]] = set()
        for procedure_name in seeds:
            outgoing_hops, incoming_hops = context_fetch.procedure_call_neighbors(
                conn,
                procedure_name=procedure_name,
                max_depth=1,
            )
            for direction, neighbors in (("incoming", incoming_hops.get(1, set())), ("outgoing", outgoing_hops.get(1, set()))):
                for neighbor_name in sorted(neighbors):
                    if neighbor_name == procedure_name:
                        continue
                    key = (procedure_name, direction, neighbor_name)
                    if key in seen:
                        continue
                    seen.add(key)
                    row = conn.execute(
                        """
                        SELECT p.id, f.id, p.chinese_name, p.object_id, f.path
                        FROM procedures p
                        JOIN files f ON f.id = p.file_id
                        WHERE p.name = ? OR p.chinese_name = ?
                        ORDER BY CASE WHEN p.name = ? THEN 0 ELSE 1 END
                        LIMIT 1
                        """,
                        (neighbor_name, neighbor_name, neighbor_name),
                    ).fetchone()
                    summary = context_fetch.lookup_procedure_summary(conn, neighbor_name)
                    if summary is None or row is None:
                        continue
                    matched_text = f"{neighbor_name} {'->' if direction == 'incoming' else '<-'} {procedure_name}"
                    candidates.append(
                        {
                            "hit_type": "procedure",
                            "entity_id": int(row[0]),
                            "procedure_id": int(row[0]),
                            "file_id": int(row[1]),
                            "statement_id": None,
                            "file_path": str(row[4]),
                            "procedure_name": str(summary["procedure_name"]),
                            "chinese_name": row[2] if row[2] else None,
                            "object_id": row[3] if row[3] else None,
                            "line_start": summary.get("line_start"),
                            "line_end": summary.get("line_end"),
                            "matched_text": matched_text,
                            "match_source": f"neighbor_{direction}_context",
                            "retrieval_source": "relation_neighbor_context",
                            "base_score": 88.0 if direction == "incoming" else 82.0,
                            "source_rank": 8.8 if direction == "incoming" else 8.2,
                            "search_text": f"{matched_text} {summary.get('summary_text') or ''}",
                            "procedure_summary": str(summary.get("summary_text") or ""),
                            "reasons": [f"neighbor_{direction}={procedure_name}"],
                        }
                    )
        return candidates[:limit]

    def _run_multi_hop_expansion_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        ranked_candidates: list[dict[str, object]],
        limit: int,
    ) -> list[dict[str, object]]:
        if not query_analysis.get("wants_call_chain"):
            return []
        tokens = {str(token) for token in query_analysis.get("tokens") or []}
        if not any(token in {"链路", "路径", "调用链", "上游", "下游"} for token in tokens):
            return []

        context_fetch = self.owner._context_fetch_service
        seeds: list[str] = []
        for item in ranked_candidates[:6]:
            procedure_name = str(item.get("procedure_name") or "")
            if procedure_name and procedure_name not in seeds:
                seeds.append(procedure_name)
            if len(seeds) >= 2:
                break
        if not seeds:
            return []

        candidates: list[dict[str, object]] = []
        seen: set[tuple[str, int, str]] = set()
        for procedure_name in seeds:
            outgoing_hops, incoming_hops = context_fetch.procedure_call_neighbors(
                conn,
                procedure_name=procedure_name,
                max_depth=3,
            )
            for direction, hop_map in (("incoming", incoming_hops), ("outgoing", outgoing_hops)):
                for depth in (2, 3):
                    for neighbor_name in sorted(hop_map.get(depth, set())):
                        if neighbor_name == procedure_name:
                            continue
                        key = (neighbor_name, depth, direction)
                        if key in seen:
                            continue
                        seen.add(key)
                        summary = context_fetch.lookup_procedure_summary(conn, neighbor_name)
                        if summary is None:
                            continue
                        row = conn.execute(
                            """
                            SELECT p.id, f.id, p.chinese_name, p.object_id, f.path
                            FROM procedures p
                            JOIN files f ON f.id = p.file_id
                            WHERE p.name = ? OR p.chinese_name = ?
                            ORDER BY CASE WHEN p.name = ? THEN 0 ELSE 1 END
                            LIMIT 1
                            """,
                            (neighbor_name, neighbor_name, neighbor_name),
                        ).fetchone()
                        if row is None:
                            continue
                        matched_text = f"{neighbor_name} {'->' if direction == 'incoming' else '<-'} ... ({depth}-hop) {procedure_name}"
                        candidates.append(
                            {
                                "hit_type": "procedure",
                                "entity_id": int(row[0]),
                                "procedure_id": int(row[0]),
                                "file_id": int(row[1]),
                                "statement_id": None,
                                "file_path": str(row[4]),
                                "procedure_name": str(summary["procedure_name"]),
                                "chinese_name": row[2] if row[2] else None,
                                "object_id": row[3] if row[3] else None,
                                "line_start": summary.get("line_start"),
                                "line_end": summary.get("line_end"),
                                "matched_text": matched_text,
                                "match_source": f"multi_hop_{direction}_{depth}",
                                "retrieval_source": "relation_multi_hop_context",
                                "base_score": 76.0 - depth,
                                "source_rank": 7.6 - depth * 0.2,
                                "search_text": f"{matched_text} {summary.get('summary_text') or ''}",
                                "procedure_summary": str(summary.get("summary_text") or ""),
                                "reasons": [f"multi_hop_{direction}_depth={depth}", f"seed={procedure_name}"],
                            }
                        )
        return candidates[:limit]

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
        db_provider = read_metadata(conn, "embedding_provider")
        db_model = read_metadata(conn, "embedding_model")
        db_dimension_raw = read_metadata(conn, "embedding_dimension")
        vector_enabled = (read_metadata(conn, "vector_enabled") or "").lower() == "true"
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
                  'procedure' AS hit_type,
                  109.0 AS base_score,
                  'fts_procedure_feature' AS retrieval_source,
                  pf.procedure_id AS entity_id,
                  pf.procedure_id AS procedure_id,
                  pf.file_id AS file_id,
                  NULL AS statement_id,
                  f.path AS file_path,
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  NULL AS line_start,
                  NULL AS line_end,
                  pf.summary_text AS matched_text,
                  'procedure_feature_summary' AS match_source,
                  -bm25(procedure_features_fts, 5.0, 3.0) AS source_rank,
                  pf.summary_text AS search_text,
                  pf.summary_text AS procedure_summary,
                  pf.feature_flags_json AS feature_flags_json,
                  pf.profile_json AS profile_json
                FROM procedure_features_fts
                JOIN procedure_features pf ON pf.procedure_id = procedure_features_fts.rowid
                JOIN procedures p ON p.id = pf.procedure_id
                JOIN files f ON f.id = pf.file_id
                WHERE procedure_features_fts MATCH ?
                LIMIT ?
                """,
                (fts_query, limit),
            ),
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
                  -bm25(chunks_fts, 2.0, 1.0, 1.5, 1.0, 6.0, 4.0) AS source_rank,
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.embedding_text, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text,
                  c.chunk_role AS chunk_role,
                  c.chunk_features_json AS chunk_features_json
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
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.embedding_text, '') || ' ' || COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') AS search_text,
                  c.chunk_role AS chunk_role,
                  c.chunk_features_json AS chunk_features_json
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

    def _run_relation_queries(
        self,
        conn: sqlite3.Connection,
        *,
        query_analysis: dict[str, object],
        limit: int,
    ) -> list[dict[str, object]]:
        candidates: list[dict[str, object]] = []
        seen: set[tuple[int, str]] = set()

        def add_procedure_candidates(
            term: str,
            field_name: str,
            score: float,
            reason: str,
            *,
            where_sql: str,
            params: tuple[object, ...],
        ) -> None:
            rows = conn.execute(
                f"""
                SELECT
                  pf.procedure_id,
                  pf.file_id,
                  pf.procedure_name,
                  pf.summary_text,
                  pf.feature_flags_json,
                  pf.profile_json,
                  p.chinese_name,
                  p.object_id,
                  f.path
                FROM procedure_features pf
                JOIN procedures p ON p.id = pf.procedure_id
                JOIN files f ON f.id = pf.file_id
                WHERE {where_sql}
                LIMIT ?
                """,
                (*params, limit),
            ).fetchall()
            for row in rows:
                key = (int(row[0]), field_name)
                if key in seen:
                    continue
                seen.add(key)
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[8]),
                        "procedure_name": str(row[2]),
                        "chinese_name": row[6] if row[6] else None,
                        "object_id": row[7] if row[7] else None,
                        "line_start": None,
                        "line_end": None,
                        "matched_text": str(row[3]),
                        "match_source": field_name,
                        "retrieval_source": "relation_procedure_feature",
                        "base_score": score,
                        "source_rank": score / 10.0,
                        "search_text": str(row[3]),
                        "procedure_summary": str(row[3]),
                        "feature_flags": json.loads(str(row[4] or "{}")),
                        "procedure_profile": json.loads(str(row[5] or "{}")),
                        "reasons": [f"{reason}={term}"],
                    }
                )

        def add_call_edge_candidates(term: str, *, callers: bool) -> None:
            if callers:
                rows = conn.execute(
                    """
                    SELECT
                      pf.procedure_id,
                      pf.file_id,
                      pf.procedure_name,
                      pf.summary_text,
                      pf.feature_flags_json,
                      pf.profile_json,
                      p.chinese_name,
                      p.object_id,
                      f.path,
                      e.source_name,
                      e.target_name
                    FROM edges e
                    JOIN procedures p ON p.name = e.source_name
                    JOIN files f ON f.id = p.file_id
                    JOIN procedure_features pf ON pf.procedure_id = p.id
                    WHERE e.edge_type = 'calls_procedure'
                      AND lower(e.target_name) = lower(?)
                    LIMIT ?
                    """,
                    (term, limit),
                ).fetchall()
                field_name = "caller_relation"
                reason = "caller_relation"
            else:
                rows = conn.execute(
                    """
                    SELECT
                      pf.procedure_id,
                      pf.file_id,
                      pf.procedure_name,
                      pf.summary_text,
                      pf.feature_flags_json,
                      pf.profile_json,
                      p.chinese_name,
                      p.object_id,
                      f.path,
                      e.source_name,
                      e.target_name
                    FROM edges e
                    JOIN procedures p ON p.name = e.target_name
                    JOIN files f ON f.id = p.file_id
                    JOIN procedure_features pf ON pf.procedure_id = p.id
                    WHERE e.edge_type = 'calls_procedure'
                      AND lower(e.source_name) = lower(?)
                    LIMIT ?
                    """,
                    (term, limit),
                ).fetchall()
                field_name = "callee_relation"
                reason = "callee_relation"

            for row in rows:
                key = (int(row[0]), field_name)
                if key in seen:
                    continue
                seen.add(key)
                edge_path = f"{row[8]} -> {row[9]}"
                candidates.append(
                    {
                        "hit_type": "procedure",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[0]),
                        "file_id": int(row[1]),
                        "statement_id": None,
                        "file_path": str(row[8]),
                        "procedure_name": str(row[2]),
                        "chinese_name": row[6] if row[6] else None,
                        "object_id": row[7] if row[7] else None,
                        "line_start": None,
                        "line_end": None,
                        "matched_text": edge_path,
                        "match_source": field_name,
                        "retrieval_source": "relation_call_edge",
                        "base_score": 97.0 if callers else 95.0,
                        "source_rank": 9.7 if callers else 9.5,
                        "search_text": f"{edge_path} {row[3]}",
                        "procedure_summary": str(row[3]),
                        "feature_flags": json.loads(str(row[4] or "{}")),
                        "procedure_profile": json.loads(str(row[5] or "{}")),
                        "reasons": [f"{reason}={term}"],
                    }
                )

        def add_exact_edge_candidates(
            term: str,
            *,
            edge_types: tuple[str, ...],
            field_name: str,
            retrieval_source: str,
            reason: str,
            score: float,
        ) -> None:
            placeholders = ",".join("?" for _ in edge_types)
            rows = conn.execute(
                f"""
                SELECT
                  e.id,
                  e.procedure_id,
                  e.file_id,
                  e.statement_id,
                  e.edge_type,
                  e.target_name,
                  e.source_name,
                  pf.summary_text,
                  pf.feature_flags_json,
                  pf.profile_json,
                  p.name,
                  p.chinese_name,
                  p.object_id,
                  f.path,
                  s.line_start,
                  s.line_end
                FROM edges e
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = e.file_id
                JOIN procedure_features pf ON pf.procedure_id = e.procedure_id
                LEFT JOIN statements s ON s.id = e.statement_id
                WHERE e.edge_type IN ({placeholders})
                  AND lower(e.target_name) = lower(?)
                LIMIT ?
                """,
                (*edge_types, term, limit),
            ).fetchall()
            for row in rows:
                key = (int(row[0]), field_name)
                if key in seen:
                    continue
                seen.add(key)
                edge_label = f"{row[6]} -> {row[5]}"
                candidates.append(
                    {
                        "hit_type": "edge",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[1]),
                        "file_id": int(row[2]),
                        "statement_id": int(row[3]) if row[3] is not None else None,
                        "file_path": str(row[13]),
                        "procedure_name": str(row[10]),
                        "chinese_name": row[11] if row[11] else None,
                        "object_id": row[12] if row[12] else None,
                        "line_start": int(row[14]) if row[14] is not None else None,
                        "line_end": int(row[15]) if row[15] is not None else None,
                        "matched_text": edge_label,
                        "match_source": field_name,
                        "retrieval_source": retrieval_source,
                        "base_score": score,
                        "source_rank": score / 10.0,
                        "search_text": f"{edge_label} {row[4]} {row[7]}",
                        "procedure_summary": str(row[7]),
                        "feature_flags": json.loads(str(row[8] or "{}")),
                        "procedure_profile": json.loads(str(row[9] or "{}")),
                        "reasons": [f"{reason}={term}", f"edge_type={row[4]}"],
                    }
                )

        def add_exact_variable_edge_candidates(term: str, *, score: float) -> None:
            rows = conn.execute(
                """
                SELECT
                  e.id,
                  e.procedure_id,
                  e.file_id,
                  e.statement_id,
                  e.edge_type,
                  e.target_name,
                  e.source_name,
                  pf.summary_text,
                  pf.feature_flags_json,
                  pf.profile_json,
                  p.name,
                  p.chinese_name,
                  p.object_id,
                  f.path,
                  s.line_start,
                  s.line_end
                FROM edges e
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = e.file_id
                JOIN procedure_features pf ON pf.procedure_id = e.procedure_id
                LEFT JOIN statements s ON s.id = e.statement_id
                WHERE e.edge_type IN ('writes_variable', 'reads_variable')
                  AND (
                    lower(e.target_name) = lower(?)
                    OR lower(replace(e.target_name, '@', '')) = lower(replace(?, '@', ''))
                  )
                LIMIT ?
                """,
                (term, term, limit),
            ).fetchall()
            for row in rows:
                key = (int(row[0]), "variable_edge_relation")
                if key in seen:
                    continue
                seen.add(key)
                edge_label = f"{row[6]} -> {row[5]}"
                candidates.append(
                    {
                        "hit_type": "edge",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[1]),
                        "file_id": int(row[2]),
                        "statement_id": int(row[3]) if row[3] is not None else None,
                        "file_path": str(row[13]),
                        "procedure_name": str(row[10]),
                        "chinese_name": row[11] if row[11] else None,
                        "object_id": row[12] if row[12] else None,
                        "line_start": int(row[14]) if row[14] is not None else None,
                        "line_end": int(row[15]) if row[15] is not None else None,
                        "matched_text": edge_label,
                        "match_source": "variable_edge_relation",
                        "retrieval_source": "relation_variable_edge",
                        "base_score": score,
                        "source_rank": score / 10.0,
                        "search_text": f"{edge_label} {row[4]} {row[7]}",
                        "procedure_summary": str(row[7]),
                        "feature_flags": json.loads(str(row[8] or "{}")),
                        "procedure_profile": json.loads(str(row[9] or "{}")),
                        "reasons": [f"variable_edge_relation={term}", f"edge_type={row[4]}"],
                    }
                )

        def add_failure_block_candidates() -> None:
            rows = conn.execute(
                """
                SELECT
                  b.id,
                  b.procedure_id,
                  b.file_id,
                  b.anchor_statement_id,
                  b.block_type,
                  b.summary_text,
                  b.excerpt,
                  b.line_start,
                  b.line_end,
                  p.name,
                  p.chinese_name,
                  p.object_id,
                  f.path,
                  pf.feature_flags_json
                FROM blocks b
                JOIN procedures p ON p.id = b.procedure_id
                JOIN files f ON f.id = b.file_id
                JOIN procedure_features pf ON pf.procedure_id = b.procedure_id
                WHERE b.block_type IN ('failure_handler', 'exception_handler', 'when_others_handler')
                ORDER BY
                  CASE b.block_type
                    WHEN 'failure_handler' THEN 0
                    WHEN 'exception_handler' THEN 1
                    ELSE 2
                  END,
                  b.line_start
                LIMIT ?
                """,
                (limit,),
            ).fetchall()
            for row in rows:
                key = (int(row[0]), "failure_block_relation")
                if key in seen:
                    continue
                seen.add(key)
                summary = str(row[5] or row[4])
                candidates.append(
                    {
                        "hit_type": "block",
                        "entity_id": int(row[0]),
                        "procedure_id": int(row[1]),
                        "file_id": int(row[2]),
                        "statement_id": int(row[3]) if row[3] is not None else None,
                        "file_path": str(row[12]),
                        "procedure_name": str(row[9]),
                        "chinese_name": row[10] if row[10] else None,
                        "object_id": row[11] if row[11] else None,
                        "line_start": int(row[7]),
                        "line_end": int(row[8]),
                        "matched_text": summary,
                        "match_source": "failure_block_relation",
                        "retrieval_source": "relation_failure_block",
                        "base_score": 99.0,
                        "source_rank": 9.9,
                        "search_text": f"{summary} {row[6]} {row[4]}",
                        "feature_flags": json.loads(str(row[13] or "{}")),
                        "reasons": [f"failure_block={row[4]}"],
                    }
                )

        if query_analysis.get("wants_call_chain"):
            for term in query_analysis.get("procedure_terms", []):
                add_call_edge_candidates(str(term), callers=bool(query_analysis.get("wants_callers")))

        for term in query_analysis.get("procedure_terms", []):
            lowered = f"%{str(term).lower()}%"
            add_procedure_candidates(
                str(term),
                "procedure_relation",
                89.0,
                "procedure_relation",
                where_sql="""
                lower(pf.procedure_name) LIKE ?
                OR lower(COALESCE(p.chinese_name, '')) LIKE ?
                OR lower(COALESCE(p.object_id, '')) LIKE ?
                OR lower(pf.summary_text) LIKE ?
                """,
                params=(lowered, lowered, lowered, lowered),
            )
        for term in query_analysis.get("table_terms", []):
            lowered = f"%{str(term).lower()}%"
            add_exact_edge_candidates(
                str(term),
                edge_types=("reads_table", "writes_table", "reads_dynamic_table", "writes_dynamic_table"),
                field_name="table_edge_relation",
                retrieval_source="relation_table_edge",
                reason="table_edge_relation",
                score=96.0 if query_analysis.get("wants_table_write") else 94.0,
            )
            add_procedure_candidates(
                str(term),
                "table_relation",
                91.0,
                "table_relation",
                where_sql="""
                lower(pf.read_tables_json) LIKE ?
                OR lower(pf.write_tables_json) LIKE ?
                OR lower(pf.summary_text) LIKE ?
                """,
                params=(lowered, lowered, lowered),
            )
        for term in query_analysis.get("variable_terms", []):
            lowered = f"%{str(term).lower()}%"
            add_exact_variable_edge_candidates(
                str(term),
                score=86.0 if query_analysis.get("wants_variable_write") else 83.0 if query_analysis.get("wants_variable_read") else 80.0,
            )
            add_procedure_candidates(
                str(term),
                "variable_relation",
                88.0,
                "variable_relation",
                where_sql="""
                lower(pf.variable_reads_json) LIKE ?
                OR lower(pf.variable_writes_json) LIKE ?
                OR lower(pf.summary_text) LIKE ?
                """,
                params=(lowered, lowered, lowered),
            )
        if query_analysis.get("wants_failure_flow"):
            add_failure_block_candidates()
        if query_analysis.get("wants_metadata"):
            for term in query_analysis.get("focus_terms", [])[:6]:
                lowered = f"%{str(term).lower()}%"
                add_procedure_candidates(
                    str(term),
                    "metadata_relation",
                    90.0,
                    "metadata_relation",
                    where_sql="""
                    lower(pf.metadata_refs_json) LIKE ?
                    OR lower(pf.summary_text) LIKE ?
                    """,
                    params=(lowered, lowered),
                )
        if query_analysis.get("wants_topic"):
            for term in [*query_analysis.get("focus_terms", [])[:6], *query_analysis.get("procedure_terms", [])[:2]]:
                lowered = f"%{str(term).lower()}%"
                add_procedure_candidates(
                    str(term),
                    "topic_relation",
                    92.0,
                    "topic_relation",
                    where_sql="""
                    lower(pf.mc_topics_json) LIKE ?
                    OR lower(pf.summary_text) LIKE ?
                    """,
                    params=(lowered, lowered),
                )
        for term in query_analysis.get("focus_terms", [])[:6]:
            lowered = f"%{str(term).lower()}%"
            add_procedure_candidates(
                str(term),
                "focus_relation",
                82.0,
                "focus_relation",
                where_sql="""
                lower(pf.summary_text) LIKE ?
                OR lower(pf.actions_json) LIKE ?
                OR lower(pf.outgoing_calls_json) LIKE ?
                OR lower(pf.incoming_callers_json) LIKE ?
                """,
                params=(lowered, lowered, lowered, lowered),
            )

        return candidates[:limit]

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
    result = {
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
    if "chunk_role" in row.keys() and row["chunk_role"] is not None:
        result["chunk_role"] = str(row["chunk_role"])
    if "chunk_features_json" in row.keys() and row["chunk_features_json"]:
        result["chunk_features"] = json.loads(str(row["chunk_features_json"]))
    if "procedure_summary" in row.keys() and row["procedure_summary"]:
        result["procedure_summary"] = str(row["procedure_summary"])
    if "feature_flags_json" in row.keys() and row["feature_flags_json"]:
        result["feature_flags"] = json.loads(str(row["feature_flags_json"]))
    if "profile_json" in row.keys() and row["profile_json"]:
        result["procedure_profile"] = json.loads(str(row["profile_json"]))
    return result


def _public_hit(candidate: dict[str, object], *, rank: int) -> dict[str, object]:
    return {
        "rank": rank,
        "score": round(float(candidate["score"]), 3),
        "aggregate_score": round(float(candidate.get("aggregate_score") or candidate["score"]), 3),
        "aggregate_hit_count": int(candidate.get("aggregate_hit_count") or 1),
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
        "procedure_profile": dict(candidate.get("procedure_profile") or {}),
    }
