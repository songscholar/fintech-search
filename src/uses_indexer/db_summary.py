from __future__ import annotations

import sqlite3
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from .index_utils import json_loads_object
from .metadata_store import read_metadata
from .response_schema import apply_response_envelope
from .semantic_recovery import SEMANTIC_RULE_REGISTRY, coerce_call_semantics

if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


class DbSummaryService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner

    def summarize_db(self, db_path: str | Path) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        def scalar(query: str) -> int:
            return int(conn.execute(query).fetchone()[0])

        def grouped(query: str) -> dict[str, int]:
            rows = conn.execute(query).fetchall()
            return {str(row[0]): int(row[1]) for row in rows}

        summary = {
            "db_path": str(db_path),
            "files": scalar("SELECT COUNT(*) FROM files"),
            "metadata_files": scalar("SELECT COUNT(*) FROM files WHERE path LIKE '%/metadata/%'"),
            "procedures": scalar("SELECT COUNT(*) FROM procedures"),
            "histories": scalar("SELECT COUNT(*) FROM histories"),
            "params": scalar("SELECT COUNT(*) FROM params"),
            "statements": scalar("SELECT COUNT(*) FROM statements"),
            "metadata_entries": scalar("SELECT COUNT(*) FROM statements WHERE kind = 'metadata_item'"),
            "actions": scalar("SELECT COUNT(*) FROM actions"),
            "variable_refs": scalar("SELECT COUNT(*) FROM variable_refs"),
            "edges": scalar("SELECT COUNT(*) FROM edges"),
            "chunks": scalar("SELECT COUNT(*) FROM chunks"),
            "chunk_vectors": scalar("SELECT COUNT(*) FROM chunk_vectors"),
            "blocks": scalar("SELECT COUNT(*) FROM blocks"),
            "block_edges": scalar("SELECT COUNT(*) FROM block_edges"),
            "fts_counts": {
                "procedures_fts": scalar("SELECT COUNT(*) FROM procedures_fts"),
                "statements_fts": scalar("SELECT COUNT(*) FROM statements_fts"),
                "actions_fts": scalar("SELECT COUNT(*) FROM actions_fts"),
                "edges_fts": scalar("SELECT COUNT(*) FROM edges_fts"),
                "chunks_fts": scalar("SELECT COUNT(*) FROM chunks_fts"),
                "blocks_fts": scalar("SELECT COUNT(*) FROM blocks_fts"),
            },
            "embedding": {
                "provider": read_metadata(conn, "embedding_provider"),
                "model": read_metadata(conn, "embedding_model"),
                "dimension": read_metadata(conn, "embedding_dimension"),
            },
            "unit_kind_counts": grouped("SELECT unit_kind, COUNT(*) FROM files GROUP BY unit_kind ORDER BY COUNT(*) DESC"),
            "file_prefix_counts": grouped("SELECT prefix, COUNT(*) FROM files GROUP BY prefix ORDER BY COUNT(*) DESC"),
            "statement_kind_counts": grouped("SELECT kind, COUNT(*) FROM statements GROUP BY kind ORDER BY COUNT(*) DESC"),
            "metadata_entry_tag_counts": grouped(
                "SELECT tag, COUNT(*) FROM statements WHERE kind = 'metadata_item' GROUP BY tag ORDER BY COUNT(*) DESC"
            ),
            "variable_ref_type_counts": grouped("SELECT access_type, COUNT(*) FROM variable_refs GROUP BY access_type ORDER BY COUNT(*) DESC"),
            "edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
            "chunk_type_counts": grouped("SELECT chunk_type, COUNT(*) FROM chunks GROUP BY chunk_type ORDER BY COUNT(*) DESC"),
            "vector_provider_counts": grouped("SELECT provider, COUNT(*) FROM chunk_vectors GROUP BY provider ORDER BY COUNT(*) DESC"),
            "block_type_counts": grouped("SELECT block_type, COUNT(*) FROM blocks GROUP BY block_type ORDER BY COUNT(*) DESC"),
            "block_edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM block_edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
        }
        summary.update(self._summarize_call_semantics(conn))
        summary.update(self._summarize_mc_publish_semantics(conn))
        summary["semantic_rule_registry"] = SEMANTIC_RULE_REGISTRY
        conn.close()
        return apply_response_envelope(summary, kind="db_summary")

    def _summarize_call_semantics(self, conn: sqlite3.Connection) -> dict[str, object]:
        rows = conn.execute(
            """
            SELECT source_name, target_name, detail_json
            FROM edges
            WHERE edge_type = 'calls_procedure'
            """
        ).fetchall()
        call_kind_counts: Counter[str] = Counter()
        call_rule_counts: Counter[str] = Counter()

        for row in rows:
            detail = json_loads_object(str(row["detail_json"]))
            semantic = coerce_call_semantics(
                detail,
                source_name=str(row["source_name"]),
                target_name=str(row["target_name"]),
            )
            call_kind_counts[str(semantic["call_kind"])] += 1
            if semantic["call_rule"]:
                call_rule_counts[str(semantic["call_rule"])] += 1

        return {
            "call_kind_counts": dict(call_kind_counts),
            "call_rule_counts": dict(call_rule_counts),
        }

    def _summarize_mc_publish_semantics(self, conn: sqlite3.Connection) -> dict[str, object]:
        rows = conn.execute(
            """
            SELECT target_name, detail_json
            FROM edges
            WHERE edge_type = 'publishes_mc_topic'
            """
        ).fetchall()
        mode_counts: Counter[str] = Counter()
        topic_counts: Counter[str] = Counter()

        for row in rows:
            detail = json_loads_object(str(row["detail_json"]))
            publish_mode = str(detail.get("publish_mode") or "unknown")
            mode_counts[publish_mode] += 1
            topic_counts[str(row["target_name"])] += 1

        return {
            "mc_publish_mode_counts": dict(mode_counts),
            "mc_topic_counts": dict(topic_counts),
        }
