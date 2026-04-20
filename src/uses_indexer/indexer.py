from __future__ import annotations

import os
import sqlite3
from collections import Counter, defaultdict
from heapq import nlargest
from pathlib import Path

from .constants import (
    COMPONENT_ACTIONS,
    EXIT_LABEL_NAMES,
    READ_ACTIONS,
    WRITE_ACTIONS,
)
from .embeddings import (
    Embedder,
    EmbeddingConfigError,
    EmbeddingInfo,
    EmbeddingRequestError,
    create_embedder_from_env,
    dot_similarity,
)
from .context_fetch import ContextFetchService
from .evidence import EvidenceService
from .index_build import IndexBuildService
from .index_utils import (
    embedder_batch_size,
    json_dumps,
    json_loads_object,
    maybe_int,
    paths_match,
)
from .index_write import IndexWriteService
from .models import CodeStatement, ParsedUnit
from .parser import ASSIGN_RE, UftDslParser, is_supported_path
from .retrieval import RetrievalService
from .response_schema import apply_response_envelope
from .semantic_recovery import (
    classify_call_semantics,
    classify_mc_publish,
    coerce_call_semantics,
    maybe_int,
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

    def _json(self, value: object) -> str:
        return json_dumps(value)

    def _maybe_int(self, value: object) -> int | None:
        return maybe_int(value)

    def _paths_match(self, left: str | Path, right: str | Path) -> bool:
        return paths_match(left, right)

    def _embedder_batch_size(self, embedder: Embedder) -> int:
        return embedder_batch_size(embedder)

    def _classify_call_semantics(self, source_name: str, target_name: str) -> dict[str, object]:
        return classify_call_semantics(source_name, target_name)

    def _classify_mc_publish(self, statement: CodeStatement) -> dict[str, object] | None:
        return classify_mc_publish(statement)

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

    def _insert_unit(self, conn: sqlite3.Connection, unit: ParsedUnit) -> tuple[int, int]:
        return self._index_write_service.insert_unit(conn, unit)

    def _insert_statements(
        self,
        conn: sqlite3.Connection,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
    ) -> tuple[Counter[str], Counter[str], Counter[str], Counter[str], Counter[str], Counter[str], Counter[str]]:
        return self._index_write_service.insert_statements(conn, file_id, procedure_id, unit)

    def _insert_chunks(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
    ) -> tuple[Counter[str], Counter[str]]:
        return self._index_write_service.insert_chunks(conn, file_id=file_id, procedure_id=procedure_id, unit=unit)

    def _populate_missing_chunk_vectors(self, conn: sqlite3.Connection) -> dict[str, object]:
        return self._index_write_service.populate_missing_chunk_vectors(conn)

    def _validate_resume_source(self, conn: sqlite3.Connection, root: Path) -> None:
        self._index_write_service.validate_resume_source(conn, root)

    def _validate_vector_space_for_population(self, conn: sqlite3.Connection) -> None:
        self._index_write_service.validate_vector_space_for_population(conn)

    def _store_embedding_metadata(self, conn: sqlite3.Connection, info: EmbeddingInfo) -> None:
        self._index_write_service.store_embedding_metadata(conn, info)

    def _missing_chunk_vector_count(self, conn: sqlite3.Connection) -> int:
        return self._index_write_service.missing_chunk_vector_count(conn)

    def _insert_blocks(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
        statement_ids_by_seq: dict[int, int],
    ) -> tuple[Counter[str], Counter[str]]:
        return self._index_write_service.insert_blocks(
            conn,
            file_id=file_id,
            procedure_id=procedure_id,
            unit=unit,
            statement_ids_by_seq=statement_ids_by_seq,
        )

    def _fetch_block_table_names(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_start_seq: int,
        statement_end_seq: int,
    ) -> list[str]:
        return self._index_write_service.fetch_block_table_names(
            conn,
            procedure_id=procedure_id,
            statement_start_seq=statement_start_seq,
            statement_end_seq=statement_end_seq,
        )

    def _fetch_block_edges(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_start_seq: int,
        statement_end_seq: int,
    ) -> list[dict[str, object]]:
        return self._index_write_service.fetch_block_edges(
            conn,
            procedure_id=procedure_id,
            statement_start_seq=statement_start_seq,
            statement_end_seq=statement_end_seq,
        )

    def _insert_variable_refs(
        self,
        conn: sqlite3.Connection,
        file_id: int,
        procedure_id: int,
        statement_id: int,
        statement: CodeStatement,
        counter: Counter[str],
    ) -> None:
        self._index_write_service.insert_variable_refs(conn, file_id, procedure_id, statement_id, statement, counter)

    def _insert_action_and_edges(
        self,
        conn: sqlite3.Connection,
        file_id: int,
        procedure_id: int,
        statement_id: int,
        unit: ParsedUnit,
        statement: CodeStatement,
        seq: int,
        edge_counter: Counter[str],
        string_hints: dict[str, str],
    ) -> Counter[str]:
        return self._index_write_service.insert_action_and_edges(
            conn,
            file_id=file_id,
            procedure_id=procedure_id,
            statement_id=statement_id,
            unit=unit,
            statement=statement,
            seq=seq,
            edge_counter=edge_counter,
            string_hints=string_hints,
        )

    def _insert_edge(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        statement_id: int | None,
        procedure_name: str,
        file_path: str,
        edge_type: str,
        source_name: str,
        target_name: str,
        target_kind: str,
        detail: dict[str, object],
    ) -> None:
        self._index_write_service.insert_edge(
            conn,
            file_id=file_id,
            procedure_id=procedure_id,
            statement_id=statement_id,
            procedure_name=procedure_name,
            file_path=file_path,
            edge_type=edge_type,
            source_name=source_name,
            target_name=target_name,
            target_kind=target_kind,
            detail=detail,
        )

    def _procedure_call_neighbors(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_name: str,
        max_depth: int = 10,
    ) -> tuple[dict[int, set[str]], dict[int, set[str]]]:
        return self._context_fetch_service.procedure_call_neighbors(
            conn,
            procedure_name=procedure_name,
            max_depth=max_depth,
        )

    def _fetch_context_block(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_id: int | None,
        context_window: int,
    ) -> dict[str, object]:
        return self._context_fetch_service.fetch_context_block(
            conn,
            procedure_id=procedure_id,
            statement_id=statement_id,
            context_window=context_window,
        )

    def _fetch_chunk_block(
        self,
        conn: sqlite3.Connection,
        *,
        chunk_id: int,
    ) -> dict[str, object]:
        return self._context_fetch_service.fetch_chunk_block(conn, chunk_id=chunk_id)

    def _fetch_block_context(
        self,
        conn: sqlite3.Connection,
        *,
        block_id: int,
    ) -> dict[str, object]:
        return self._context_fetch_service.fetch_block_context(conn, block_id=block_id)

    def _fetch_covering_blocks(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        line_start: int,
        line_end: int,
        limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_covering_blocks(
            conn,
            procedure_id=procedure_id,
            line_start=line_start,
            line_end=line_end,
            limit=limit,
        )

    def _fetch_block_relation_summary(
        self,
        conn: sqlite3.Connection,
        *,
        block_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_block_relation_summary(conn, block_id=block_id, limit=limit)

    def _fetch_related_context(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        related_limit: int,
    ) -> dict[str, object]:
        return self._context_fetch_service.fetch_related_context(
            conn,
            procedure_id=procedure_id,
            procedure_name=procedure_name,
            related_limit=related_limit,
        )

    def _fetch_related_metadata_relations(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_related_metadata_relations(
            conn,
            procedure_id=procedure_id,
            limit=limit,
        )

    def _fetch_related_mc_topics(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_related_mc_topics(conn, procedure_id=procedure_id, limit=limit)

    def _fetch_related_call_edges(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        aliases: tuple[str, ...],
        direction: str,
        limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_related_call_edges(
            conn,
            procedure_id=procedure_id,
            procedure_name=procedure_name,
            aliases=aliases,
            direction=direction,
            limit=limit,
        )

    def _fetch_call_chain_paths(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_name: str,
        direction: str,
        limit: int,
    ) -> list[dict[str, object]]:
        chains: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()

        if direction == "outgoing":
            raw_via_rows = conn.execute(
                """
                SELECT DISTINCT target_name
                FROM edges
                WHERE source_name = ? AND edge_type = 'calls_procedure'
                ORDER BY target_name
                """,
                (procedure_name,),
            ).fetchall()
            via_names = [self._resolve_procedure_name(conn, str(row["target_name"])) for row in raw_via_rows]
            for via_name in via_names:
                for row in conn.execute(
                    """
                    SELECT DISTINCT target_name
                    FROM edges
                    WHERE source_name = ? AND edge_type = 'calls_procedure'
                    ORDER BY target_name
                    LIMIT ?
                    """,
                    (via_name, limit),
                ).fetchall():
                    end_name = self._resolve_procedure_name(conn, str(row["target_name"]))
                    if end_name == procedure_name:
                        continue
                    key = (via_name, end_name)
                    if key in seen:
                        continue
                    seen.add(key)
                    chain = self._lookup_procedure_summary(conn, end_name)
                    if chain is None:
                        continue
                    chain["via_name"] = via_name
                    chain["direction"] = direction
                    chains.append(chain)
                    if len(chains) >= limit:
                        return chains
        else:
            alias_names = self._procedure_aliases(conn, procedure_name=procedure_name)
            raw_via_rows = conn.execute(
                f"""
                SELECT DISTINCT source_name
                FROM edges
                WHERE edge_type = 'calls_procedure' AND target_name IN ({",".join("?" for _ in alias_names)})
                ORDER BY source_name
                """,
                tuple(alias_names),
            ).fetchall()
            via_names = [str(row["source_name"]) for row in raw_via_rows]
            for via_name in via_names:
                via_aliases = self._procedure_aliases(conn, procedure_name=via_name)
                caller_rows = conn.execute(
                    f"""
                    SELECT DISTINCT source_name
                    FROM edges
                    WHERE edge_type = 'calls_procedure' AND target_name IN ({",".join("?" for _ in via_aliases)})
                    ORDER BY source_name
                    LIMIT ?
                    """,
                    (*via_aliases, limit),
                ).fetchall()
                for row in caller_rows:
                    end_name = str(row["source_name"])
                    if end_name == procedure_name:
                        continue
                    key = (via_name, end_name)
                    if key in seen:
                        continue
                    seen.add(key)
                    chain = self._lookup_procedure_summary(conn, end_name)
                    if chain is None:
                        continue
                    chain["via_name"] = via_name
                    chain["direction"] = direction
                    chains.append(chain)
                    if len(chains) >= limit:
                        return chains

        return chains

    def _procedure_aliases(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int | None = None,
        procedure_name: str | None = None,
    ) -> tuple[str, ...]:
        return self._context_fetch_service.procedure_aliases(
            conn,
            procedure_id=procedure_id,
            procedure_name=procedure_name,
        )

    def _resolve_procedure_name(self, conn: sqlite3.Connection, raw_name: str) -> str:
        return self._context_fetch_service.resolve_procedure_name(conn, raw_name)

    def _fetch_related_procedure_summaries(
        self,
        conn: sqlite3.Connection,
        *,
        outgoing_calls: list[str],
        incoming_callers: list[str],
        related_limit: int,
    ) -> list[dict[str, object]]:
        return self._context_fetch_service.fetch_related_procedure_summaries(
            conn,
            outgoing_calls=outgoing_calls,
            incoming_callers=incoming_callers,
            related_limit=related_limit,
        )

    def _lookup_procedure_summary(
        self,
        conn: sqlite3.Connection,
        procedure_name: str,
    ) -> dict[str, object] | None:
        return self._context_fetch_service.lookup_procedure_summary(conn, procedure_name)


