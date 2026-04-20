from __future__ import annotations

import os
import sqlite3
from collections import Counter
from pathlib import Path

from .constants import (
    COMPONENT_ACTIONS,
    EXIT_LABEL_NAMES,
    READ_ACTIONS,
    WRITE_ACTIONS,
)
from .embeddings import (
    Embedder,
    create_embedder_from_env,
)
from .context_fetch import ContextFetchService
from .evidence import EvidenceService
from .index_build import IndexBuildService
from .index_utils import json_loads_object
from .index_write import IndexWriteService
from .parser import UftDslParser
from .retrieval import RetrievalService
from .response_schema import apply_response_envelope
from .semantic_recovery import (
    coerce_call_semantics,
    SEMANTIC_RULE_REGISTRY,
)

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS files (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT NOT NULL UNIQUE,
  file_name TEXT NOT NULL,
  unit_kind TEXT NOT NULL,
  prefix TEXT NOT NULL,
  name TEXT NOT NULL,
  chinese_name TEXT,
  object_id TEXT,
  code_line_count INTEGER NOT NULL DEFAULT 0,
  attributes_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS procedures (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  prefix TEXT NOT NULL,
  unit_kind TEXT NOT NULL,
  chinese_name TEXT,
  object_id TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS histories (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  modified_date TEXT,
  version TEXT,
  order_number TEXT,
  modified_by TEXT,
  modified TEXT,
  extra_attributes_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS params (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  category TEXT NOT NULL,
  param_id TEXT NOT NULL,
  uuid TEXT,
  param_type TEXT,
  type_name TEXT,
  name TEXT,
  comments TEXT,
  default_value TEXT,
  flags TEXT,
  extra_attributes_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS statements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  kind TEXT NOT NULL,
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  raw TEXT NOT NULL,
  tag TEXT,
  name TEXT,
  condition TEXT,
  target TEXT,
  groups_json TEXT NOT NULL DEFAULT '[]',
  arguments_json TEXT NOT NULL DEFAULT '[]',
  reads_json TEXT NOT NULL DEFAULT '[]',
  writes_json TEXT NOT NULL DEFAULT '[]',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS actions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER NOT NULL UNIQUE,
  seq INTEGER NOT NULL,
  kind TEXT NOT NULL,
  tag TEXT,
  action_name TEXT,
  target_name TEXT,
  target_kind TEXT,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS variable_refs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER NOT NULL,
  var_name TEXT NOT NULL,
  access_type TEXT NOT NULL,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS edges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  statement_id INTEGER,
  edge_type TEXT NOT NULL,
  source_name TEXT NOT NULL,
  target_name TEXT NOT NULL,
  target_kind TEXT NOT NULL,
  detail_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(statement_id) REFERENCES statements(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS chunks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  chunk_type TEXT NOT NULL,
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  statement_start_seq INTEGER NOT NULL,
  statement_end_seq INTEGER NOT NULL,
  statement_count INTEGER NOT NULL,
  anchor_kinds_json TEXT NOT NULL DEFAULT '[]',
  action_names_json TEXT NOT NULL DEFAULT '[]',
  target_names_json TEXT NOT NULL DEFAULT '[]',
  variable_names_json TEXT NOT NULL DEFAULT '[]',
  content TEXT NOT NULL,
  summary_text TEXT NOT NULL,
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS chunk_vectors (
  chunk_id INTEGER PRIMARY KEY,
  provider TEXT NOT NULL,
  model TEXT NOT NULL,
  dimension INTEGER NOT NULL,
  vector_json TEXT NOT NULL,
  FOREIGN KEY(chunk_id) REFERENCES chunks(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS blocks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  file_id INTEGER NOT NULL,
  procedure_id INTEGER NOT NULL,
  seq INTEGER NOT NULL,
  block_type TEXT NOT NULL,
  anchor_name TEXT NOT NULL,
  line_start INTEGER NOT NULL,
  line_end INTEGER NOT NULL,
  statement_start_seq INTEGER NOT NULL,
  statement_end_seq INTEGER NOT NULL,
  statement_count INTEGER NOT NULL,
  anchor_statement_id INTEGER,
  summary_text TEXT NOT NULL,
  excerpt TEXT NOT NULL,
  action_names_json TEXT NOT NULL DEFAULT '[]',
  target_names_json TEXT NOT NULL DEFAULT '[]',
  table_names_json TEXT NOT NULL DEFAULT '[]',
  variable_names_json TEXT NOT NULL DEFAULT '[]',
  FOREIGN KEY(file_id) REFERENCES files(id) ON DELETE CASCADE,
  FOREIGN KEY(procedure_id) REFERENCES procedures(id) ON DELETE CASCADE,
  FOREIGN KEY(anchor_statement_id) REFERENCES statements(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS block_edges (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  block_id INTEGER NOT NULL,
  edge_type TEXT NOT NULL,
  target_name TEXT NOT NULL,
  target_kind TEXT NOT NULL,
  detail_json TEXT NOT NULL DEFAULT '{}',
  FOREIGN KEY(block_id) REFERENCES blocks(id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE IF NOT EXISTS procedures_fts USING fts5(
  name,
  chinese_name,
  object_id,
  path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS statements_fts USING fts5(
  raw,
  name,
  condition,
  target,
  procedure_name,
  file_path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS actions_fts USING fts5(
  action_name,
  target_name,
  procedure_name,
  file_path,
  raw,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS edges_fts USING fts5(
  edge_type,
  source_name,
  target_name,
  target_kind,
  procedure_name,
  file_path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
  chunk_type,
  procedure_name,
  file_path,
  summary_text,
  content,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS blocks_fts USING fts5(
  block_type,
  anchor_name,
  procedure_name,
  file_path,
  summary_text,
  excerpt,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE INDEX IF NOT EXISTS idx_files_prefix ON files(prefix);
CREATE INDEX IF NOT EXISTS idx_files_unit_kind ON files(unit_kind);
CREATE INDEX IF NOT EXISTS idx_procedures_name ON procedures(name);
CREATE INDEX IF NOT EXISTS idx_params_param_id ON params(param_id);
CREATE INDEX IF NOT EXISTS idx_statements_kind ON statements(kind);
CREATE INDEX IF NOT EXISTS idx_statements_name ON statements(name);
CREATE INDEX IF NOT EXISTS idx_actions_action_name ON actions(action_name);
CREATE INDEX IF NOT EXISTS idx_variable_refs_name ON variable_refs(var_name);
CREATE INDEX IF NOT EXISTS idx_edges_target_name ON edges(target_name);
CREATE INDEX IF NOT EXISTS idx_edges_edge_type ON edges(edge_type);
CREATE INDEX IF NOT EXISTS idx_chunks_procedure_seq ON chunks(procedure_id, seq);
CREATE INDEX IF NOT EXISTS idx_chunk_vectors_provider ON chunk_vectors(provider, model);
CREATE INDEX IF NOT EXISTS idx_blocks_procedure_seq ON blocks(procedure_id, seq);
CREATE INDEX IF NOT EXISTS idx_blocks_type ON blocks(block_type);
CREATE INDEX IF NOT EXISTS idx_block_edges_block ON block_edges(block_id);
CREATE INDEX IF NOT EXISTS idx_block_edges_type ON block_edges(edge_type);
"""

class SQLiteIndexer:
    SCHEMA_SQL = SCHEMA_SQL
    READ_ACTIONS = READ_ACTIONS
    WRITE_ACTIONS = WRITE_ACTIONS
    COMPONENT_ACTIONS = COMPONENT_ACTIONS
    EXIT_LABEL_NAMES = EXIT_LABEL_NAMES

    def __init__(
        self,
        parser: UftDslParser | None = None,
        embedder: Embedder | None = None,
    ) -> None:
        self.parser = parser or UftDslParser()
        self.embedder = embedder or create_embedder_from_env()
        self._vector_cache: dict[tuple[str, int, int, str, str], list[dict[str, object]]] = {}
        self._index_build_service = IndexBuildService(self)
        self._retrieval_service = RetrievalService(self)
        self._evidence_service = EvidenceService(self)
        self._context_fetch_service = ContextFetchService(self)
        self._index_write_service = IndexWriteService(self)

    def build_index(
        self,
        source_root: str | Path,
        db_path: str | Path,
        *,
        resume_vectors: bool = False,
        incremental: bool = False,
        index_type: str = "all",
    ) -> dict[str, object]:
        return self._index_build_service.build_index(
            source_root,
            db_path,
            resume_vectors=resume_vectors,
            incremental=incremental,
            index_type=index_type,
        )

    def resume_chunk_vectors(self, source_root: str | Path, db_path: str | Path, index_type: str = "all") -> dict[str, object]:
        return self._index_build_service.resume_chunk_vectors(source_root, db_path, index_type=index_type)

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
                "provider": self._metadata(conn, "embedding_provider"),
                "model": self._metadata(conn, "embedding_model"),
                "dimension": self._metadata(conn, "embedding_dimension"),
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

    def _metadata(self, conn: sqlite3.Connection, key: str) -> str | None:
        row = conn.execute("SELECT value FROM metadata WHERE key = ?", (key,)).fetchone()
        if row is None:
            return None
        return str(row[0])

    def query_index(self, db_path: str | Path, query: str, limit: int = 20, *, debug: bool = False) -> dict[str, object]:
        return self._retrieval_service.query_index(db_path, query, limit=limit, debug=debug)

    def assemble_evidence(
        self,
        db_path: str | Path,
        query: str,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
        *,
        debug: bool = False,
    ) -> dict[str, object]:
        return self._evidence_service.assemble_evidence(
            db_path,
            query,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
            debug=debug,
        )


