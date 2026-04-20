from __future__ import annotations

import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from heapq import nlargest
from pathlib import Path

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
from .index_write import IndexWriteService
from .models import CodeStatement, ParsedUnit
from .parser import ASSIGN_RE, UftDslParser, is_supported_path
from .retrieval import RetrievalService
from .semantic_recovery import (
    build_semantic_chunks,
    classify_call_semantics,
    classify_mc_publish,
    coerce_call_semantics,
    collect_block_entities,
    extract_sql_access_edges,
    format_excerpt,
    maybe_int,
    recover_blocks,
    SEMANTIC_RULE_REGISTRY,
    summarize_block,
    update_string_hints,
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

READ_ACTIONS = {"获取记录", "获取字段", "遍历记录开始", "遍历记录池开始", "记录为空", "记录不为空"}
WRITE_ACTIONS = {"插入记录", "修改记录", "清空记录池", "数据回库"}
COMPONENT_ACTIONS = {"获取组件", "插入组件", "尾部插入组件", "遍历组件开始", "遍历组件结束", "组件大小"}
TABLE_WITH_INDEX_RE = re.compile(r"^(?P<table>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<index>[^)]+)\)$")
QUERY_TOKEN_RE = re.compile(r"[\u4e00-\u9fff]+|[A-Za-z0-9_]+")
CHUNK_SIGNIFICANT_LIMIT = 6
VECTOR_SIMILARITY_THRESHOLD = 0.05
CHINESE_QUERY_SPLIT_RE = re.compile(r"(?:被谁调用|谁调用|在哪里|在哪儿|哪里|哪些|哪个|谁|什么|如何|怎么|是否|能否|可以|请问|一下|调用|流程|的|了|在|是|和|与|及|或|并|把|将|从|到|为|对|按|里)")
GENERIC_QUERY_TERMS = {
    "逻辑",
    "代码",
    "流程",
    "实现",
    "位置",
    "地方",
    "相关",
    "问题",
    "功能",
    "模块",
    "方法",
}
PAIRED_BLOCK_ACTIONS = {
    "transaction": ("事务处理开始", "事务处理结束"),
    "sql_query": ("查询SQL语句开始", "查询SQL语句结束"),
    "record_loop": ("遍历记录开始", "遍历记录结束"),
    "record_pool_loop": ("遍历记录池开始", "遍历记录池结束"),
    "component_loop": ("遍历组件开始", "遍历组件结束"),
}
SINGLE_BLOCK_ACTIONS = {
    "通用SQL执行": "sql_execute",
}
BRACE_ATTACHED_BLOCK_ACTIONS = {
    "处理失败": "failure_handler",
    "EXCEPTION": "exception_handler",
    "WHEN_OTHERS": "when_others_handler",
}
EXIT_LABEL_NAMES = {"svr_end"}
SQL_FROM_JOIN_RE = re.compile(r"\b(?:from|join)\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_UPDATE_RE = re.compile(r"\bupdate\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_INSERT_RE = re.compile(r"\binsert\s+into\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_DELETE_RE = re.compile(r"\bdelete\s+from\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_MERGE_RE = re.compile(r"\bmerge\s+into\s+([A-Za-z_][A-Za-z0-9_$.]*)", re.IGNORECASE)
SQL_STRING_RE = re.compile(r"'(?:''|[^'])*'")
SQL_SKIP_TABLES = {"dual"}
DOUBLE_QUOTED_STRING_RE = re.compile(r'"((?:\\.|[^"\\])*)"')
CALL_EXPR_RE = re.compile(r"(?P<func>hs_snprintf|snprintf|sprintf|hs_strcpy|strcpy)\s*\((?P<args>.*)\)\s*;?\s*$", re.DOTALL)
TRACKED_STRING_VAR_TOKENS = ("sql", "table", "where", "column", "group", "order", "join")
QUERY_PROCEDURE_RE = re.compile(r"\b(?:AF|LF|LS|RS|AS)_[A-Za-z0-9_]+\b")
QUERY_VARIABLE_RE = re.compile(r"@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?")
TABLE_TOKEN_PREFIXES = ("uses_", "reload_", "upbs_", "usps_", "uact_", "stb_", "ufx_", "udp_")
TABLE_INTENT_KEYWORDS = ("表", "sql", "数据库", "查询", "读取", "select", "from", "join", "update", "delete", "insert", "merge")
WRITE_INTENT_KEYWORDS = ("更新", "修改", "删除", "清空", "写入", "update", "delete", "insert", "merge")
READ_INTENT_KEYWORDS = ("查询", "读取", "获取", "select", "from", "join")
VARIABLE_INTENT_KEYWORDS = ("变量", "赋值", "写入", "读取", "参数", "字段")
CALL_CHAIN_INTENT_KEYWORDS = ("调用链", "被谁调用", "谁调用", "调用", "链路", "上游", "下游")
FAILURE_INTENT_KEYWORDS = ("失败", "报错", "异常", "exception", "when_others", "goto", "svr_end", "退出", "错误")
PROCEDURE_INTENT_KEYWORDS = ("过程", "函数", "服务", "接口", "原子", "方法")
SQL_WRITE_HINTS = (" update ", " delete ", " insert ", " merge ", "writes_table", "清空记录池", "修改记录", "插入记录")
SQL_READ_HINTS = (" select ", " from ", " join ", "reads_table", "获取记录", "获取字段")
FAILURE_MATCH_HINTS = ("失败", "报错", "异常", "exception", "when_others", "svr_end", "goto", "处理失败", "业务报错返回")
FOCUS_EXCLUDED_QUERY_TERMS = (
    GENERIC_QUERY_TERMS
    | set(TABLE_INTENT_KEYWORDS)
    | set(WRITE_INTENT_KEYWORDS)
    | set(READ_INTENT_KEYWORDS)
    | set(VARIABLE_INTENT_KEYWORDS)
    | set(CALL_CHAIN_INTENT_KEYWORDS)
    | set(FAILURE_INTENT_KEYWORDS)
    | set(PROCEDURE_INTENT_KEYWORDS)
    | {"执行", "处理"}
)


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
        return summary

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
            detail = _json_loads(str(row["detail_json"]))
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
            detail = _json_loads(str(row["detail_json"]))
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
        return _json(value)

    def _maybe_int(self, value: object) -> int | None:
        return _maybe_int(value)

    def _paths_match(self, left: str | Path, right: str | Path) -> bool:
        return _paths_match(left, right)

    def _embedder_batch_size(self, embedder: Embedder) -> int:
        return _embedder_batch_size(embedder)

    def _derive_target(self, statement: CodeStatement) -> tuple[str | None, str]:
        return _derive_target(statement)

    def _metadata_edges_for_statement(self, statement: CodeStatement) -> list[dict[str, object]]:
        return _metadata_edges_for_statement(statement)

    def _classify_call_semantics(self, source_name: str, target_name: str) -> dict[str, object]:
        return classify_call_semantics(source_name, target_name)

    def _classify_mc_publish(self, statement: CodeStatement) -> dict[str, object] | None:
        return classify_mc_publish(statement)

    def _build_fts_query(self, query: str) -> str | None:
        return _build_fts_query(query)

    def _merge_candidate(self, store: dict[tuple[object, ...], dict[str, object]], candidate: dict[str, object]) -> None:
        _merge_candidate(store, candidate)

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

def _recover_blocks(statements: list[CodeStatement]) -> list[dict[str, object]]:
    if not statements:
        return []

    brace_pairs = _brace_pairs(statements)
    blocks: list[dict[str, object]] = []
    paired_stacks: dict[str, list[int]] = {block_type: [] for block_type in PAIRED_BLOCK_ACTIONS}

    for seq, statement in enumerate(statements, start=1):
        if statement.kind == "goto" and statement.target:
            block_type = "goto_exit" if statement.target in EXIT_LABEL_NAMES else "goto_jump"
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=block_type,
                    anchor_name=statement.target,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )
            continue

        if statement.kind == "label" and statement.target in EXIT_LABEL_NAMES:
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type="exit_label",
                    anchor_name=statement.target,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )
            continue

        if statement.kind != "action" or not statement.name:
            continue

        for block_type, (start_name, end_name) in PAIRED_BLOCK_ACTIONS.items():
            if statement.name == start_name:
                paired_stacks[block_type].append(seq)
                break
            if statement.name == end_name and paired_stacks[block_type]:
                start_seq = paired_stacks[block_type].pop()
                blocks.append(
                    _make_recovered_block(
                        statements=statements,
                        block_type=block_type,
                        anchor_name=start_name,
                        anchor_seq=start_seq,
                        statement_start_seq=start_seq,
                        statement_end_seq=seq,
                    )
                )
                break

        single_block_type = SINGLE_BLOCK_ACTIONS.get(statement.name)
        if single_block_type is not None:
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=single_block_type,
                    anchor_name=statement.name,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=seq,
                )
            )

        brace_block_type = BRACE_ATTACHED_BLOCK_ACTIONS.get(statement.name)
        if brace_block_type is not None:
            end_seq = _find_brace_attached_end(statements, start_seq=seq, brace_pairs=brace_pairs)
            blocks.append(
                _make_recovered_block(
                    statements=statements,
                    block_type=brace_block_type,
                    anchor_name=statement.name,
                    anchor_seq=seq,
                    statement_start_seq=seq,
                    statement_end_seq=end_seq,
                )
            )

    blocks.sort(key=lambda item: (int(item["statement_start_seq"]), int(item["statement_end_seq"]), str(item["block_type"])))
    deduped: list[dict[str, object]] = []
    seen: set[tuple[object, ...]] = set()
    for block in blocks:
        key = (
            block["block_type"],
            block["statement_start_seq"],
            block["statement_end_seq"],
            block["anchor_name"],
        )
        if key in seen:
            continue
        seen.add(key)
        deduped.append(block)
    return deduped


def _brace_pairs(statements: list[CodeStatement]) -> dict[int, int]:
    stack: list[int] = []
    pairs: dict[int, int] = {}
    for seq, statement in enumerate(statements, start=1):
        if statement.kind != "brace":
            continue
        if statement.name == "{":
            stack.append(seq)
        elif statement.name == "}" and stack:
            pairs[stack.pop()] = seq
    return pairs


def _find_brace_attached_end(
    statements: list[CodeStatement],
    *,
    start_seq: int,
    brace_pairs: dict[int, int],
) -> int:
    for seq in range(start_seq + 1, len(statements) + 1):
        statement = statements[seq - 1]
        if statement.kind == "comment":
            continue
        if statement.kind == "action" and statement.name in {"EXCEPTION", "WHEN_OTHERS"}:
            continue
        if statement.kind == "brace" and statement.name == "{":
            return brace_pairs.get(seq, seq)
        return seq
    return start_seq


def _make_recovered_block(
    *,
    statements: list[CodeStatement],
    block_type: str,
    anchor_name: str,
    anchor_seq: int,
    statement_start_seq: int,
    statement_end_seq: int,
) -> dict[str, object]:
    block_statements = statements[statement_start_seq - 1 : statement_end_seq]
    line_start = min(statement.line_start for statement in block_statements)
    line_end = max(statement.line_end for statement in block_statements)
    return {
        "block_type": block_type,
        "anchor_name": anchor_name,
        "anchor_seq": anchor_seq,
        "statement_start_seq": statement_start_seq,
        "statement_end_seq": statement_end_seq,
        "line_start": line_start,
        "line_end": line_end,
    }


def _collect_block_entities(statements: list[CodeStatement]) -> tuple[list[str], list[str], list[str]]:
    action_names = sorted({statement.name for statement in statements if statement.name})
    target_names: set[str] = set()
    variable_names: set[str] = set()

    for statement in statements:
        target_name, _ = _derive_target(statement)
        if target_name:
            target_names.add(target_name)
        variable_names.update(statement.reads)
        variable_names.update(statement.writes)

    return action_names, sorted(target_names), sorted(variable_names)


def _summarize_block(
    *,
    procedure_name: str,
    block_type: str,
    anchor_name: str,
    statements: list[CodeStatement],
    action_names: list[str],
    target_names: list[str],
) -> str:
    sql_preview = _extract_sql_preview(statements)
    action_preview = ", ".join(action_names[:4])
    target_preview = ", ".join(target_names[:3])
    statement_count = len(statements)

    if block_type == "transaction":
        summary = f"{procedure_name} 的事务块，包含 {statement_count} 条语句"
    elif block_type == "sql_query":
        summary = f"{procedure_name} 的 SQL 查询块"
    elif block_type == "sql_execute":
        summary = f"{procedure_name} 的 SQL 执行语句"
    elif block_type == "failure_handler":
        summary = f"{procedure_name} 的失败处理块"
    elif block_type == "exception_handler":
        summary = f"{procedure_name} 的 EXCEPTION 异常处理块"
    elif block_type == "when_others_handler":
        summary = f"{procedure_name} 的 WHEN_OTHERS 兜底处理块"
    elif block_type == "goto_exit":
        summary = f"{procedure_name} 的退出跳转语句，跳向 {anchor_name}"
    elif block_type == "goto_jump":
        summary = f"{procedure_name} 的跳转语句，跳向 {anchor_name}"
    elif block_type == "exit_label":
        summary = f"{procedure_name} 的退出标签 {anchor_name}"
    elif block_type.endswith("_loop"):
        summary = f"{procedure_name} 的 {anchor_name} 代码块"
    else:
        summary = f"{procedure_name} 的 {anchor_name} 代码块"

    parts = [summary]
    if sql_preview:
        parts.append(f"SQL={sql_preview}")
    if action_preview:
        parts.append(f"actions={action_preview}")
    if target_preview:
        parts.append(f"targets={target_preview}")
    return " | ".join(parts)


def _extract_sql_preview(statements: list[CodeStatement]) -> str | None:
    for statement in statements:
        if statement.kind != "action" or statement.name not in {"查询SQL语句开始", "通用SQL执行"}:
            continue
        if len(statement.groups) < 2:
            continue
        sql_text = " ".join(statement.groups[1].split())
        if sql_text:
            return _truncate_text(sql_text, 120)
    return None


def _extract_sql_access_edges(
    statement: CodeStatement,
    string_hints: dict[str, str],
) -> list[dict[str, str]]:
    if statement.kind != "action" or statement.name not in {"通用SQL执行", "查询SQL语句开始"}:
        return []
    if len(statement.groups) < 2:
        return []

    sql_text = _resolve_sql_text(statement.groups[1].strip(), string_hints)
    if not sql_text:
        return []

    normalized = _normalize_sql(sql_text)
    if not normalized:
        return []

    accesses: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    def add(edge_type: str, table_name: str, operation: str) -> None:
        normalized_table, normalized_edge_type = _normalize_table_reference(table_name, edge_type)
        if not normalized_table or not normalized_edge_type:
            return
        key = (normalized_edge_type, normalized_table)
        if key in seen:
            return
        seen.add(key)
        accesses.append(
            {
                "edge_type": normalized_edge_type,
                "target_name": normalized_table,
                "operation": operation,
                "sql_source": _truncate_text(normalized, 160),
            }
        )

    lower = normalized.lower()
    if lower.startswith("select "):
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "select")
        return accesses

    if lower.startswith("update "):
        for table_name in SQL_UPDATE_RE.findall(normalized):
            add("writes_table", table_name, "update")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "update_context")
        return accesses

    if lower.startswith("insert "):
        for table_name in SQL_INSERT_RE.findall(normalized):
            add("writes_table", table_name, "insert")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "insert_select")
        return accesses

    if lower.startswith("delete "):
        for table_name in SQL_DELETE_RE.findall(normalized):
            add("writes_table", table_name, "delete")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "delete_context")
        return accesses

    if lower.startswith("merge "):
        for table_name in SQL_MERGE_RE.findall(normalized):
            add("writes_table", table_name, "merge")
        for table_name in SQL_FROM_JOIN_RE.findall(normalized):
            add("reads_table", table_name, "merge_context")
        return accesses

    return accesses


def _normalize_sql(sql_text: str) -> str:
    without_strings = SQL_STRING_RE.sub(" ", sql_text)
    normalized = " ".join(without_strings.replace("\n", " ").replace("\t", " ").split())
    return normalized


def _resolve_sql_text(raw_group: str, string_hints: dict[str, str]) -> str | None:
    candidate = raw_group.strip()
    if not candidate:
        return None
    if candidate.startswith("@"):
        return string_hints.get(candidate)
    return candidate


def _normalize_table_reference(name: str, edge_type: str) -> tuple[str | None, str | None]:
    normalized_table = _normalize_table_name(name)
    if normalized_table:
        return normalized_table, edge_type
    dynamic_table = _normalize_dynamic_table_name(name)
    if dynamic_table:
        dynamic_edge = "reads_dynamic_table" if edge_type == "reads_table" else "writes_dynamic_table"
        return dynamic_table, dynamic_edge
    return None, None


def _normalize_table_name(name: str) -> str | None:
    candidate = name.strip().strip(",;")
    if not candidate:
        return None
    if candidate.startswith("@") or "%" in candidate:
        return None
    if "." in candidate:
        candidate = candidate.split(".")[-1]
    lower = candidate.lower()
    if lower in SQL_SKIP_TABLES:
        return None
    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_$]*", candidate):
        return None
    return candidate


def _normalize_dynamic_table_name(name: str) -> str | None:
    candidate = name.strip().strip(",;")
    if not candidate.startswith("@"):
        return None
    if not re.fullmatch(r"@[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?", candidate):
        return None
    return candidate


def _update_string_hints(string_hints: dict[str, str], statement: CodeStatement) -> None:
    updates = _extract_string_hint_updates(statement, string_hints)
    for var_name, value in updates.items():
        if value is None:
            string_hints.pop(var_name, None)
        else:
            string_hints[var_name] = value


def _extract_string_hint_updates(statement: CodeStatement, string_hints: dict[str, str]) -> dict[str, str | None]:
    if not statement.writes:
        return {}

    tracked_writes = [var_name for var_name in statement.writes if _is_tracked_string_var(var_name)]
    if not tracked_writes:
        return {}

    raw = statement.raw.strip()
    updates: dict[str, str | None] = {}

    assignment_match = ASSIGN_RE.match(raw)
    if assignment_match:
        lhs = assignment_match.group("lhs")
        rhs = raw.split("=", 1)[1].rstrip(";").strip()
        resolved = _resolve_string_expression(rhs, string_hints)
        updates[lhs] = resolved
        return updates

    call_match = CALL_EXPR_RE.match(raw)
    if call_match:
        func = call_match.group("func")
        args = _split_call_args(call_match.group("args"))
        if func in {"hs_strcpy", "strcpy"} and len(args) >= 2:
            dest = args[0].strip()
            if _is_tracked_string_var(dest):
                updates[dest] = _resolve_string_expression(args[1], string_hints)
            return updates

        if func in {"sprintf", "snprintf", "hs_snprintf"}:
            dest_index = 0
            format_index = 1 if func == "sprintf" else 2
            if len(args) <= format_index:
                return updates
            dest = args[dest_index].strip()
            if not _is_tracked_string_var(dest):
                return updates
            rendered = _render_format_call(
                format_expr=args[format_index],
                value_exprs=args[format_index + 1 :],
                string_hints=string_hints,
            )
            updates[dest] = rendered
            return updates

    for var_name in tracked_writes:
        updates[var_name] = None
    return updates


def _is_tracked_string_var(var_name: str) -> bool:
    lowered = var_name.lower()
    return any(token in lowered for token in TRACKED_STRING_VAR_TOKENS)


def _resolve_string_expression(expr: str, string_hints: dict[str, str]) -> str | None:
    candidate = expr.strip()
    quoted = _parse_double_quoted_string(candidate)
    if quoted is not None:
        return quoted
    if candidate.startswith("@"):
        return string_hints.get(candidate, candidate if _is_tracked_string_var(candidate) else None)
    return None


def _render_format_call(
    *,
    format_expr: str,
    value_exprs: list[str],
    string_hints: dict[str, str],
) -> str | None:
    format_template = _resolve_string_expression(format_expr, string_hints)
    if format_template is None:
        return None

    rendered_parts: list[str] = []
    value_index = 0
    index = 0
    while index < len(format_template):
        if format_template[index] != "%":
            rendered_parts.append(format_template[index])
            index += 1
            continue

        if index + 1 < len(format_template) and format_template[index + 1] == "%":
            rendered_parts.append("%")
            index += 2
            continue

        match = re.match(r"%[-+#0-9.]*[A-Za-z]", format_template[index:])
        if not match:
            rendered_parts.append(format_template[index])
            index += 1
            continue

        placeholder = match.group(0)
        if value_index >= len(value_exprs):
            rendered_parts.append(placeholder)
        else:
            rendered_parts.append(_render_format_value(value_exprs[value_index], string_hints))
            value_index += 1
        index += len(placeholder)

    return "".join(rendered_parts)


def _render_format_value(expr: str, string_hints: dict[str, str]) -> str:
    resolved = _resolve_string_expression(expr, string_hints)
    if resolved is not None:
        return resolved
    candidate = expr.strip()
    if candidate.startswith("@"):
        return candidate
    return candidate


def _parse_double_quoted_string(expr: str) -> str | None:
    match = DOUBLE_QUOTED_STRING_RE.fullmatch(expr.strip())
    if match is None:
        return None
    return bytes(match.group(1), "utf-8").decode("unicode_escape")


def _split_call_args(raw_args: str) -> list[str]:
    args: list[str] = []
    current: list[str] = []
    depth = 0
    in_string = False
    escape = False

    for char in raw_args:
        if in_string:
            current.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
            current.append(char)
            continue
        if char == "(":
            depth += 1
            current.append(char)
            continue
        if char == ")":
            depth = max(depth - 1, 0)
            current.append(char)
            continue
        if char == "," and depth == 0:
            args.append("".join(current).strip())
            current = []
            continue
        current.append(char)

    tail = "".join(current).strip()
    if tail:
        args.append(tail)
    return args


def _build_semantic_chunks(
    procedure_name: str,
    statements: list[CodeStatement],
) -> list[dict[str, object]]:
    chunks: list[dict[str, object]] = []
    current: list[tuple[int, CodeStatement]] = []
    significant_count = 0

    def flush() -> None:
        nonlocal current, significant_count
        chunk = _make_chunk(procedure_name, current)
        if chunk is not None:
            chunks.append(chunk)
        current = []
        significant_count = 0

    for seq, statement in enumerate(statements, start=1):
        if statement.kind == "brace":
            if current:
                current.append((seq, statement))
            continue

        if current and _should_start_new_chunk(current, statement, significant_count):
            flush()

        current.append((seq, statement))
        if statement.kind != "comment":
            significant_count += 1

    flush()
    return chunks


def _should_start_new_chunk(
    current: list[tuple[int, CodeStatement]],
    statement: CodeStatement,
    significant_count: int,
) -> bool:
    if statement.kind == "metadata_item":
        return bool(current)
    if any(item.kind == "metadata_item" for _, item in current):
        return True
    if statement.kind == "label":
        return True
    if significant_count >= CHUNK_SIGNIFICANT_LIMIT:
        return True
    if statement.kind in {"control", "goto"} and significant_count >= 2:
        return True
    if statement.kind in {"call", "action"} and any(item.kind == "control" for _, item in current):
        return True
    return False


def _make_chunk(
    procedure_name: str,
    entries: list[tuple[int, CodeStatement]],
) -> dict[str, object] | None:
    if not entries:
        return None

    significant_entries = [(seq, statement) for seq, statement in entries if statement.kind != "brace"]
    if not significant_entries:
        return None

    non_comment_entries = [
        (seq, statement)
        for seq, statement in significant_entries
        if statement.kind != "comment"
    ]
    if not non_comment_entries:
        return None

    line_start = min(statement.line_start for _, statement in significant_entries)
    line_end = max(statement.line_end for _, statement in significant_entries)
    statement_start_seq = min(seq for seq, _ in significant_entries)
    statement_end_seq = max(seq for seq, _ in significant_entries)

    anchor_kinds = _unique_preserve_order(statement.kind for _, statement in non_comment_entries)
    action_names = _unique_preserve_order(
        statement.name
        for _, statement in non_comment_entries
        if statement.kind in {"action", "call"} and statement.name
    )
    metadata_names = _unique_preserve_order(
        statement.name
        for _, statement in non_comment_entries
        if statement.kind == "metadata_item" and statement.name
    )
    target_names = _unique_preserve_order(
        target
        for _, statement in non_comment_entries
        for target in _statement_targets(statement)
    )
    variable_names = _unique_preserve_order(
        variable
        for _, statement in non_comment_entries
        for variable in [*statement.reads, *statement.writes]
    )
    conditions = _unique_preserve_order(
        statement.condition
        for _, statement in non_comment_entries
        if statement.condition
    )
    comment_fragments = _unique_preserve_order(
        _clean_comment(statement.raw)
        for _, statement in significant_entries
        if statement.kind == "comment" and _clean_comment(statement.raw)
    )

    chunk_type = _infer_chunk_type(non_comment_entries)
    summary_parts = [procedure_name, chunk_type]
    if action_names:
        summary_parts.append(f"actions: {', '.join(action_names[:4])}")
    if metadata_names:
        summary_parts.append(f"metadata: {', '.join(metadata_names[:4])}")
    if target_names:
        summary_parts.append(f"targets: {', '.join(target_names[:4])}")
    if conditions:
        summary_parts.append(f"conditions: {', '.join(conditions[:2])}")
    if variable_names:
        summary_parts.append(f"vars: {', '.join(variable_names[:6])}")
    if comment_fragments:
        summary_parts.append(f"notes: {'; '.join(comment_fragments[:2])}")

    content = "\n".join(statement.raw.rstrip("\n") for _, statement in entries if statement.raw.strip())
    return {
        "chunk_type": chunk_type,
        "line_start": line_start,
        "line_end": line_end,
        "statement_start_seq": statement_start_seq,
        "statement_end_seq": statement_end_seq,
        "statement_count": len(significant_entries),
        "anchor_kinds": anchor_kinds,
        "action_names": action_names,
        "target_names": target_names,
        "variable_names": variable_names,
        "content": content,
        "summary_text": " | ".join(summary_parts),
    }


def _infer_chunk_type(entries: list[tuple[int, CodeStatement]]) -> str:
    kinds = {statement.kind for _, statement in entries}
    if kinds == {"metadata_item"}:
        return "metadata_block"
    if "control" in kinds:
        return "control_block"
    if "call" in kinds and "action" in kinds:
        return "call_flow"
    if "call" in kinds:
        return "call_block"
    if "action" in kinds:
        return "action_block"
    if "assignment" in kinds:
        return "assignment_block"
    if "raw" in kinds:
        return "raw_block"
    return "statement_block"


def _statement_targets(statement: CodeStatement) -> list[str]:
    targets: list[str] = []
    derived_target, derived_kind = _derive_target(statement)
    if derived_target and derived_kind != "unknown":
        targets.append(derived_target)
    if statement.target and statement.target not in targets:
        targets.append(statement.target)
    return targets


def _clean_comment(raw: str) -> str:
    stripped = raw.strip()
    if stripped.startswith("//"):
        return stripped[2:].strip()
    return stripped


def _unique_preserve_order(values: list[str] | tuple[str, ...] | object) -> list[str]:
    items = list(values)
    result: list[str] = []
    seen: set[str] = set()
    for value in items:
        if value is None:
            continue
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        result.append(text)
    return result


def _derive_target(statement: CodeStatement) -> tuple[str | None, str]:
    if statement.kind == "metadata_item":
        if statement.target:
            return statement.target, _metadata_target_kind(statement)
        if statement.name:
            return statement.name, _metadata_entity_kind(statement.tag)
        return None, "metadata"

    if statement.kind == "call" and statement.name:
        return statement.name, "procedure"

    mc_publish_detail = classify_mc_publish(statement)
    if mc_publish_detail is not None and mc_publish_detail.get("topic_name"):
        return str(mc_publish_detail["topic_name"]), "mc_topic"

    if not statement.groups or len(statement.groups) < 2:
        return None, "unknown"

    candidate = statement.groups[1].strip()
    if not candidate:
        return None, "unknown"

    if candidate.startswith("@"):
        return candidate, "variable"

    table_match = TABLE_WITH_INDEX_RE.match(candidate)
    if table_match:
        return table_match.group("table"), "table"

    if "(" in candidate and ")" in candidate:
        return candidate, "expression"

    if "=" in candidate:
        return candidate, "expression"

    lowered = candidate.lower()
    if lowered.startswith("select ") or lowered.startswith("update ") or lowered.startswith("delete ") or lowered.startswith("insert "):
        return candidate, "sql"

    if candidate.startswith("comp_"):
        return candidate, "component"

    return candidate, "table"


def _metadata_entity_kind(tag: str | None) -> str:
    mapping = {
        "metadata_macro": "macro",
        "metadata_topic": "topic_alias",
        "metadata_constant": "constant",
        "metadata_errorno": "error_code",
        "metadata_standard_field": "standard_field",
        "metadata_business_datatype": "business_datatype",
        "metadata_common_datatype": "common_datatype",
        "metadata_standard_datatype": "standard_datatype",
        "metadata_default_value": "default_value",
        "metadata_dictionary": "dictionary",
        "metadata_component": "component",
        "metadata_component_field": "component_field",
        "metadata_component_index": "component_index",
        "metadata_memory_table": "memory_table",
        "metadata_memory_index": "memory_index",
        "metadata_standard_object": "standard_object",
        "metadata_serial_number": "serial_number",
        "metadata_status": "status",
        "metadata_sysconfig": "sysconfig",
        "metadata_user_context": "user_context",
        "metadata_interface_struct": "interface_struct",
        "metadata_multicast": "multicast",
        "metadata_heterogeneous_component": "heterogeneous_component",
        "metadata_word_change_rule": "word_change_rule",
        "metadata_operation": "operation",
        "metadata_standard_datatype_mapping": "data_mapping",
        "metadata_default_value_mapping": "data_mapping",
        "metadata_standard_field_property": "field_property",
        "metadata_data_mapping": "data_mapping",
        "metadata_index": "index",
    }
    return mapping.get(str(tag or ""), "metadata")


def _metadata_target_kind(statement: CodeStatement) -> str:
    tag = str(statement.tag or "")
    if tag == "metadata_topic":
        return "mc_topic"
    if tag == "metadata_errorno":
        return "error_number"
    if tag in {"metadata_standard_field", "metadata_business_datatype", "metadata_common_datatype"}:
        return "datatype"
    if tag == "metadata_constant":
        return "constant_value"
    if tag in {"metadata_memory_table", "metadata_component"}:
        return "table"
    if tag in {"metadata_standard_object", "metadata_user_context", "metadata_interface_struct"}:
        return "type_reference"
    if tag == "metadata_operation":
        return "tool_file"
    return _metadata_entity_kind(statement.tag)


def _metadata_argument_values(statement: CodeStatement, key: str) -> list[str]:
    values: list[str] = []
    for group in statement.arguments:
        for item in group:
            if item.get("key") != key:
                continue
            value = str(item.get("value") or "").strip()
            if value:
                values.append(value)
    return values


def _metadata_first_value(statement: CodeStatement, *keys: str) -> str | None:
    for key in keys:
        values = _metadata_argument_values(statement, key)
        if values:
            return values[0]
    return None


def _split_csv_values(raw: str) -> list[str]:
    if raw == "*":
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]


def _classify_metadata_ref(value: str) -> tuple[str, str]:
    if value.startswith("CNST_"):
        return "references_constant", "constant"
    if value.startswith(("ERR_", "LDP_", "UFTCORE_ERR_")) or re.fullmatch(r"-?\d+", value):
        return "references_error_code", "error_code"
    if value.startswith("comp_"):
        return "references_component", "component"
    if value.startswith("Hs"):
        return "references_datatype", "datatype"
    if value.startswith("uft") and "." in value:
        return "references_topic_name", "mc_topic"
    if value.startswith("idx_"):
        return "references_index", "index"
    return "references_metadata", "metadata"


def _metadata_definition_edge_type(statement: CodeStatement) -> str:
    entity_kind = _metadata_entity_kind(statement.tag)
    if entity_kind == "metadata":
        return "defines_metadata_item"
    return f"defines_{entity_kind}"


def _metadata_edges_for_statement(statement: CodeStatement) -> list[dict[str, object]]:
    if statement.kind != "metadata_item":
        return []

    edges: list[dict[str, object]] = []
    seen: set[tuple[str, str, str]] = set()

    def add(edge_type: str, target_name: str | None, target_kind: str, detail: dict[str, object] | None = None) -> None:
        name = str(target_name or "").strip()
        if not name:
            return
        key = (edge_type, name, target_kind)
        if key in seen:
            return
        seen.add(key)
        edges.append(
            {
                "edge_type": edge_type,
                "target_name": name,
                "target_kind": target_kind,
                "detail": detail or {},
            }
        )

    if statement.name:
        add(
            _metadata_definition_edge_type(statement),
            statement.name,
            _metadata_entity_kind(statement.tag),
            {"metadata_name": statement.name},
        )

    primary_target = statement.target
    if primary_target:
        if statement.tag == "metadata_topic":
            add("maps_topic_name", primary_target, "mc_topic")
        elif statement.tag == "metadata_memory_table":
            add("maps_db_table", primary_target, "table")
        elif statement.tag == "metadata_component":
            add("maps_component_name", primary_target, "component")
        elif statement.tag == "metadata_standard_field":
            add("uses_datatype", primary_target, "datatype")
        elif statement.tag in {"metadata_business_datatype", "metadata_common_datatype"}:
            add("uses_standard_type", primary_target, "standard_type")
        elif statement.tag == "metadata_standard_object":
            add("maps_object_type", primary_target, "type_reference")
        elif statement.tag == "metadata_errorno":
            add("maps_error_number", primary_target, "error_number")
        elif statement.tag == "metadata_constant":
            add("maps_constant_value", primary_target, "constant_value")
        elif statement.tag == "metadata_operation":
            add("maps_tool_file", primary_target, "tool_file")

    data_type = _metadata_first_value(statement, "dataType", "stdType")
    if data_type:
        edge_type = "uses_standard_type" if _metadata_first_value(statement, "stdType") == data_type else "uses_datatype"
        target_kind = "standard_type" if edge_type == "uses_standard_type" else "datatype"
        add(edge_type, data_type, target_kind)

    default_value = _metadata_first_value(statement, "defaultValue")
    if default_value:
        add("uses_default_value", default_value, "default_value")

    memory_table_name = _metadata_first_value(statement, "memoryTableName")
    if memory_table_name:
        add("maps_memory_table", memory_table_name, "table")

    db_table_name = _metadata_first_value(statement, "dbTableName", "dbTableAliasName")
    if db_table_name:
        add("maps_db_table", db_table_name, "table")

    sync_table_name = _metadata_first_value(statement, "syncTableName")
    if sync_table_name:
        add("maps_sync_table", sync_table_name, "table")

    alias_name = _metadata_first_value(statement, "aliasName")
    if alias_name and statement.tag == "metadata_topic":
        add("defines_topic_alias", alias_name, "topic_alias")

    for key in ("condition1", "condition2", "condition3", "condition4", "condition5", "condition6"):
        for value in _metadata_argument_values(statement, key):
            add("topic_filter_field", value, "field")

    for raw_fields in _metadata_argument_values(statement, "fields"):
        for field_name in _split_csv_values(raw_fields):
            add("contains_field", field_name, "field")

    for child_item in _metadata_argument_values(statement, "child_item"):
        add("contains_field", child_item, "field")

    for child_index in _metadata_argument_values(statement, "child_index"):
        add("contains_index", child_index, "index")

    for data_mapping in _metadata_argument_values(statement, "data_mapping"):
        add("maps_data_value", data_mapping, "mapping")

    for ref in _metadata_argument_values(statement, "ref"):
        if statement.name and ref == statement.name:
            continue
        if primary_target and ref == primary_target:
            continue
        edge_type, target_kind = _classify_metadata_ref(ref)
        add(edge_type, ref, target_kind)

    return edges


def _row_to_hit(row: sqlite3.Row) -> dict[str, object]:
    result = {
        "hit_type": str(row["hit_type"]),
        "entity_id": _maybe_int(row["entity_id"]),
        "procedure_id": int(row["procedure_id"]),
        "file_id": int(row["file_id"]),
        "statement_id": _maybe_int(row["statement_id"]),
        "file_path": str(row["file_path"]),
        "procedure_name": str(row["procedure_name"]),
        "line_start": _maybe_int(row["line_start"]),
        "line_end": _maybe_int(row["line_end"]),
        "matched_text": str(row["matched_text"]),
        "match_source": str(row["match_source"]),
        "retrieval_source": str(row["retrieval_source"]),
        "base_score": float(row["base_score"]),
        "source_rank": float(row["source_rank"]),
        "search_text": str(row["search_text"]),
        "reasons": [],
    }
    if "chinese_name" in row.keys():
        result["chinese_name"] = row["chinese_name"] if row["chinese_name"] else None
    if "object_id" in row.keys():
        result["object_id"] = row["object_id"] if row["object_id"] else None
    return result


def _merge_candidate(
    store: dict[tuple[object, ...], dict[str, object]],
    candidate: dict[str, object],
) -> None:
    key = (
        candidate["hit_type"],
        candidate["entity_id"],
        candidate["statement_id"],
        candidate["procedure_id"],
        candidate["matched_text"],
    )
    existing = store.get(key)
    if existing is None:
        candidate["matched_via"] = [candidate["retrieval_source"]]
        store[key] = candidate
        return

    matched_via = list(existing.get("matched_via", []))
    retrieval_source = str(candidate["retrieval_source"])
    if retrieval_source not in matched_via:
        matched_via.append(retrieval_source)
    existing["matched_via"] = matched_via

    if float(candidate["base_score"]) > float(existing["base_score"]):
        for field in ("matched_text", "match_source", "retrieval_source", "base_score", "source_rank"):
            existing[field] = candidate[field]

    search_text = str(existing.get("search_text") or "")
    incoming = str(candidate.get("search_text") or "")
    if incoming and incoming not in search_text:
        existing["search_text"] = f"{search_text}\n{incoming}".strip()


def _build_fts_query(query: str) -> str | None:
    tokens = _tokenize_query(query)
    if not tokens:
        return None
    return " OR ".join(f"{token}*" if len(token) > 1 else token for token in tokens)


def _analyze_query(query: str) -> dict[str, object]:
    lowered = query.lower()
    tokens = _tokenize_query(query)
    token_set = set(tokens)
    procedure_terms = {match.group(0).lower() for match in QUERY_PROCEDURE_RE.finditer(query)}
    variable_terms = {match.group(0).lower() for match in QUERY_VARIABLE_RE.finditer(query)}
    underscored_tokens = {
        token.lower()
        for token in QUERY_TOKEN_RE.findall(query)
        if "_" in token
    }
    table_terms = {
        token
        for token in underscored_tokens
        if token.startswith(TABLE_TOKEN_PREFIXES) and token not in procedure_terms
    }

    wants_variable = bool(variable_terms) or _contains_any(lowered, VARIABLE_INTENT_KEYWORDS)
    if wants_variable:
        variable_terms.update(
            token
            for token in underscored_tokens
            if token not in procedure_terms and token not in table_terms
        )

    wants_table_sql = bool(table_terms) or _contains_any(lowered, TABLE_INTENT_KEYWORDS)
    wants_table_write = _contains_any(lowered, WRITE_INTENT_KEYWORDS)
    wants_table_read = _contains_any(lowered, READ_INTENT_KEYWORDS)
    wants_call_chain = _contains_any(lowered, CALL_CHAIN_INTENT_KEYWORDS)
    wants_callers = _contains_any(lowered, ("被谁调用", "谁调用", "上游", "入口"))
    wants_failure_flow = _contains_any(lowered, FAILURE_INTENT_KEYWORDS)
    wants_procedure = bool(procedure_terms) or _contains_any(lowered, PROCEDURE_INTENT_KEYWORDS)
    focus_terms = {
        token
        for token in token_set
        if len(token) >= 2
        and token not in FOCUS_EXCLUDED_QUERY_TERMS
        and token not in procedure_terms
        and token not in variable_terms
        and token not in table_terms
    }

    intents = []
    for name, enabled in (
        ("table_sql", wants_table_sql),
        ("table_write", wants_table_write),
        ("table_read", wants_table_read),
        ("variable", wants_variable),
        ("call_chain", wants_call_chain),
        ("failure_flow", wants_failure_flow),
        ("procedure", wants_procedure),
    ):
        if enabled:
            intents.append(name)

    return {
        "tokens": tokens,
        "token_set": token_set,
        "procedure_terms": sorted(procedure_terms),
        "variable_terms": sorted(variable_terms),
        "table_terms": sorted(table_terms),
        "focus_terms": sorted(focus_terms),
        "intents": intents,
        "wants_table_sql": wants_table_sql,
        "wants_table_write": wants_table_write,
        "wants_table_read": wants_table_read,
        "wants_variable": wants_variable,
        "wants_call_chain": wants_call_chain,
        "wants_callers": wants_callers,
        "wants_failure_flow": wants_failure_flow,
        "wants_procedure": wants_procedure,
    }


def _contains_any(value: str, keywords: tuple[str, ...]) -> bool:
    return any(keyword in value for keyword in keywords)


def _focus_terms_present(query_analysis: dict[str, object], value: str) -> bool:
    return any(str(term) and str(term) in value for term in query_analysis.get("focus_terms", []))


def _intent_bonus(
    *,
    candidate: dict[str, object],
    query_analysis: dict[str, object],
    search_text: str,
    matched_text: str,
    procedure_name: str,
) -> tuple[float, list[str]]:
    bonus = 0.0
    reasons: list[str] = []
    hit_type = str(candidate.get("hit_type") or "")
    match_source = str(candidate.get("match_source") or "").lower()
    combined = f"{search_text} {matched_text} {procedure_name}".lower()

    for term in query_analysis["procedure_terms"]:
        if str(term) and str(term) in combined:
            bonus += 8.0 if hit_type == "procedure" else 5.0
            reasons.append(f"procedure_focus={term}")
            break

    for term in query_analysis["table_terms"]:
        if str(term) and str(term) in combined:
            bonus += 9.0
            reasons.append(f"table_focus={term}")
            break

    for term in query_analysis["variable_terms"]:
        if str(term) and str(term) in combined:
            bonus += 8.0
            reasons.append(f"variable_focus={term}")
            break

    if query_analysis["wants_table_sql"]:
        if hit_type == "edge" and match_source in {"reads_table", "writes_table", "reads_dynamic_table", "writes_dynamic_table"}:
            bonus += 28.0
            reasons.append("intent_table_edge")
        elif hit_type == "block" and _looks_like_sql_evidence(combined):
            bonus += 20.0
            reasons.append("intent_sql_block")
        elif hit_type == "action" and _looks_like_sql_evidence(combined):
            bonus += 8.0
            reasons.append("intent_sql_action")

        if query_analysis["wants_table_write"] and _contains_any(combined, SQL_WRITE_HINTS):
            bonus += 12.0
            reasons.append("write_operation_match")
        if query_analysis["wants_table_read"] and _contains_any(combined, SQL_READ_HINTS):
            bonus += 7.0
            reasons.append("read_operation_match")

    if query_analysis["wants_variable"]:
        if hit_type == "variable":
            bonus += 24.0
            reasons.append("intent_variable_hit")
        elif hit_type == "statement" and match_source == "assignment":
            bonus += 28.0
            reasons.append("intent_assignment_statement")
        elif hit_type == "chunk" and "assignment_block" in combined:
            bonus += 12.0
            reasons.append("intent_assignment_chunk")

        if "=" in combined or "writes_variable" in combined or match_source == "write":
            bonus += 8.0
            reasons.append("variable_write_match")

    if query_analysis["wants_failure_flow"]:
        if hit_type == "block":
            bonus += 16.0
            reasons.append("intent_failure_block")
        elif hit_type == "chunk" and _contains_any(combined, FAILURE_MATCH_HINTS):
            bonus += 8.0
            reasons.append("intent_failure_chunk")

        if _contains_any(combined, FAILURE_MATCH_HINTS):
            bonus += 8.0
            reasons.append("failure_flow_match")

    if query_analysis["wants_call_chain"]:
        if hit_type == "procedure":
            bonus += 4.0 if query_analysis["wants_callers"] else 8.0
            reasons.append("intent_call_chain_procedure")
        has_procedure_focus = any(str(term) in combined for term in query_analysis["procedure_terms"])
        has_text_focus = _focus_terms_present(query_analysis, combined)
        has_call_signal = "call_flow" in combined or "call_block" in combined or "calls_procedure" in combined
        if hit_type in {"chunk", "action", "edge", "statement"} and (
            has_procedure_focus
            or (has_text_focus and has_call_signal)
        ):
            bonus += 14.0 if query_analysis["wants_callers"] else 9.0
            reasons.append("intent_call_chain")
            if has_text_focus:
                reasons.append("intent_call_chain_focus")

    if query_analysis["wants_procedure"] and not query_analysis["wants_call_chain"]:
        if hit_type == "procedure":
            bonus += 10.0
            reasons.append("intent_procedure")
        elif any(str(term) in combined for term in query_analysis["procedure_terms"]):
            bonus += 5.0
            reasons.append("intent_procedure_context")

    return bonus, reasons


def _looks_like_sql_evidence(value: str) -> bool:
    return (
        "sql" in value
        or " select " in value
        or " update " in value
        or " delete " in value
        or " insert " in value
        or " merge " in value
        or "通用sql执行" in value
    )


def _call_chain_bonus_multiplier(query_analysis: dict[str, object]) -> float:
    if query_analysis["wants_call_chain"]:
        return 1.5
    if query_analysis["wants_variable"] or query_analysis["wants_failure_flow"]:
        return 0.35
    if query_analysis["wants_table_sql"]:
        return 0.6
    return 1.0


def _tokenize_query(query: str) -> list[str]:
    tokens: list[str] = []
    seen: set[str] = set()

    for raw_token in QUERY_TOKEN_RE.findall(query):
        lowered = raw_token.lower()
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            fragments = [
                fragment.strip()
                for fragment in CHINESE_QUERY_SPLIT_RE.split(raw_token)
                if len(fragment.strip()) >= 2
            ]
            if not fragments:
                fragments = [raw_token]
            for fragment in fragments:
                if fragment in GENERIC_QUERY_TERMS:
                    continue
                if fragment not in seen:
                    seen.add(fragment)
                    tokens.append(fragment)
            continue

        if lowered not in seen:
            seen.add(lowered)
            tokens.append(lowered)

    return tokens


def _vector_hint_tokens(query: str) -> list[str]:
    hints: list[str] = []
    seen: set[str] = set()

    for raw_token in QUERY_TOKEN_RE.findall(query):
        lowered = raw_token.lower()
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            fragments = [
                fragment.strip()
                for fragment in CHINESE_QUERY_SPLIT_RE.split(raw_token)
                if len(fragment.strip()) >= 2 and fragment.strip() not in GENERIC_QUERY_TERMS
            ]
            for fragment in fragments or [raw_token]:
                if len(fragment) >= 2:
                    for size in (2, 3):
                        if len(fragment) < size:
                            continue
                        for index in range(0, len(fragment) - size + 1):
                            token = fragment[index : index + size]
                            if token not in seen:
                                seen.add(token)
                                hints.append(token)
            continue

        if lowered not in seen and len(lowered) >= 3:
            seen.add(lowered)
            hints.append(lowered)
        if "_" in lowered:
            for part in lowered.split("_"):
                if len(part) >= 3 and part not in seen:
                    seen.add(part)
                    hints.append(part)

    return hints


def _format_excerpt(statements: list[dict[str, object]]) -> str:
    lines: list[str] = []
    for statement in statements:
        raw = str(statement["raw"]).strip("\n")
        if not raw:
            continue
        raw_lines = raw.splitlines()
        for index, raw_line in enumerate(raw_lines):
            prefix = f"L{statement['line_start'] + index}: " if index == 0 else "    "
            lines.append(f"{prefix}{raw_line.rstrip()}")
    return "\n".join(lines)


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


def _extract_action_argument(statement: CodeStatement, key: str) -> str | None:
    for group in statement.arguments:
        for item in group:
            if item.get("key") == key and item.get("value"):
                return _normalize_argument_value(str(item["value"]))
    return None


def _normalize_argument_value(value: str) -> str:
    candidate = value.strip()
    quoted = _parse_double_quoted_string(candidate)
    if quoted is not None:
        return quoted
    if candidate.startswith("'") and candidate.endswith("'") and len(candidate) >= 2:
        return candidate[1:-1]
    return candidate

def _maybe_int(value: object) -> int | None:
    if value is None:
        return None
    return int(value)


def _embedder_batch_size(embedder: Embedder) -> int:
    config = getattr(embedder, "config", None)
    raw_batch_size = getattr(config, "batch_size", 512)
    try:
        batch_size = int(raw_batch_size)
    except (TypeError, ValueError):
        return 512
    return max(batch_size, 1)


def _paths_match(left: str | Path, right: str | Path) -> bool:
    try:
        return Path(left).expanduser().resolve() == Path(right).expanduser().resolve()
    except OSError:
        return str(left) == str(right)


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _json_loads(value: str) -> dict[str, object]:
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return {}
    if isinstance(loaded, dict):
        return loaded
    return {}


def _truncate_text(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def _dedupe_strings(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))
