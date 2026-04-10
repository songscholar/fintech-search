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
from .models import CodeStatement, ParsedUnit
from .parser import ASSIGN_RE, SUPPORTED_SUFFIXES, UftDslParser

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
CHINESE_QUERY_SPLIT_RE = re.compile(r"(?:在哪里|在哪儿|哪里|什么|如何|怎么|是否|能否|可以|请问|一下|的|了|在|是|和|与|及|或|并|把|将|从|到|为|对|按|里)")
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


class SQLiteIndexer:
    def __init__(
        self,
        parser: UftDslParser | None = None,
        embedder: Embedder | None = None,
    ) -> None:
        self.parser = parser or UftDslParser()
        self.embedder = embedder or create_embedder_from_env()
        self._vector_cache: dict[tuple[str, int, int, str, str], list[dict[str, object]]] = {}

    def build_index(self, source_root: str | Path, db_path: str | Path, *, resume_vectors: bool = False) -> dict[str, object]:
        root = Path(source_root)
        db_file = Path(db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)

        if resume_vectors:
            return self.resume_chunk_vectors(root, db_file)

        if db_file.exists():
            db_file.unlink()

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        conn.executescript(SCHEMA_SQL)

        files = sorted(
            path for path in root.rglob("*")
            if path.is_file() and path.suffix in SUPPORTED_SUFFIXES
        )

        unit_kind_counter: Counter[str] = Counter()
        prefix_counter: Counter[str] = Counter()
        statement_counter: Counter[str] = Counter()
        edge_counter: Counter[str] = Counter()
        variable_ref_counter: Counter[str] = Counter()
        action_counter: Counter[str] = Counter()
        chunk_counter: Counter[str] = Counter()
        vector_counter: Counter[str] = Counter()
        block_counter: Counter[str] = Counter()
        block_edge_counter: Counter[str] = Counter()
        initial_embedder_info = self.embedder.info

        try:
            with conn:
                conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("source_root", str(root)))
                conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("file_count", str(len(files))))
                conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("schema_version", "6"))
                conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("fts_enabled", "true"))
                conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("vector_enabled", "true"))
                self._store_embedding_metadata(conn, initial_embedder_info)

                for path in files:
                    unit = self.parser.parse_path(path)
                    file_id, procedure_id = self._insert_unit(conn, unit)

                    unit_kind_counter[unit.unit_kind] += 1
                    prefix_counter[unit.prefix] += 1

                    for statement in unit.statements:
                        statement_counter[statement.kind] += 1

                    local_edges, local_var_refs, local_actions, local_chunks, local_vectors, local_blocks, local_block_edges = self._insert_statements(conn, file_id, procedure_id, unit)
                    edge_counter.update(local_edges)
                    variable_ref_counter.update(local_var_refs)
                    action_counter.update(local_actions)
                    chunk_counter.update(local_chunks)
                    vector_counter.update(local_vectors)
                    block_counter.update(local_blocks)
                    block_edge_counter.update(local_block_edges)

            vector_stats = self._populate_missing_chunk_vectors(conn)
        finally:
            conn.close()
        self._vector_cache.clear()

        db_summary = self.summarize_db(db_file)

        return {
            "source_root": str(root),
            "db_path": str(db_file),
            "file_count": int(db_summary["files"]),
            "unit_kind_counts": db_summary["unit_kind_counts"],
            "prefix_counts": db_summary["file_prefix_counts"],
            "statement_counts": db_summary["statement_kind_counts"],
            "edge_counts": db_summary["edge_type_counts"],
            "variable_ref_counts": db_summary["variable_ref_type_counts"],
            "action_counts": dict(action_counter),
            "chunk_counts": db_summary["chunk_type_counts"],
            "vector_counts": db_summary["vector_provider_counts"],
            "block_counts": db_summary["block_type_counts"],
            "block_edge_counts": db_summary["block_edge_type_counts"],
            "fts_counts": db_summary["fts_counts"],
            "vector_stats": vector_stats,
            "embedding": {
                "provider": db_summary["embedding"]["provider"],
                "model": db_summary["embedding"]["model"],
                "dimension": int(db_summary["embedding"]["dimension"] or 0),
            },
        }

    def resume_chunk_vectors(self, source_root: str | Path, db_path: str | Path) -> dict[str, object]:
        root = Path(source_root)
        db_file = Path(db_path)
        if not db_file.exists():
            raise FileNotFoundError(f"Cannot resume vectors because database does not exist: {db_file}")

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        try:
            self._validate_resume_source(conn, root)
            vector_stats = self._populate_missing_chunk_vectors(conn)
        finally:
            conn.close()
        self._vector_cache.clear()

        db_summary = self.summarize_db(db_file)
        return {
            "source_root": str(root),
            "db_path": str(db_file),
            "resume_vectors": True,
            "file_count": int(db_summary["files"]),
            "chunk_counts": db_summary["chunk_type_counts"],
            "vector_counts": db_summary["vector_provider_counts"],
            "vector_stats": vector_stats,
            "embedding": {
                "provider": db_summary["embedding"]["provider"],
                "model": db_summary["embedding"]["model"],
                "dimension": int(db_summary["embedding"]["dimension"] or 0),
            },
        }

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
            "procedures": scalar("SELECT COUNT(*) FROM procedures"),
            "histories": scalar("SELECT COUNT(*) FROM histories"),
            "params": scalar("SELECT COUNT(*) FROM params"),
            "statements": scalar("SELECT COUNT(*) FROM statements"),
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
            "variable_ref_type_counts": grouped("SELECT access_type, COUNT(*) FROM variable_refs GROUP BY access_type ORDER BY COUNT(*) DESC"),
            "edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
            "chunk_type_counts": grouped("SELECT chunk_type, COUNT(*) FROM chunks GROUP BY chunk_type ORDER BY COUNT(*) DESC"),
            "vector_provider_counts": grouped("SELECT provider, COUNT(*) FROM chunk_vectors GROUP BY provider ORDER BY COUNT(*) DESC"),
            "block_type_counts": grouped("SELECT block_type, COUNT(*) FROM blocks GROUP BY block_type ORDER BY COUNT(*) DESC"),
            "block_edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM block_edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
        }
        conn.close()
        return summary

    def _metadata(self, conn: sqlite3.Connection, key: str) -> str | None:
        row = conn.execute("SELECT value FROM metadata WHERE key = ?", (key,)).fetchone()
        if row is None:
            return None
        return str(row[0])

    def query_index(self, db_path: str | Path, query: str, limit: int = 20) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        candidates, fts_query, vector_status = self._retrieve_candidates(
            conn,
            db_path=db_path,
            query=query,
            candidate_limit=max(limit * 6, 30),
        )
        conn.close()

        hits = [
            _public_hit(candidate, rank=index)
            for index, candidate in enumerate(candidates[:limit], start=1)
        ]

        return {
            "db_path": str(db_path),
            "query": query,
            "fts_query": fts_query,
            "retrieval_strategy": "fts(block/chunk/procedure/action/statement/edge) + vector(if compatible) + sql fallback + python rerank",
            "vector_status": vector_status,
            "candidate_count": len(candidates),
            "hit_count": len(hits),
            "hits": hits,
        }

    def assemble_evidence(
        self,
        db_path: str | Path,
        query: str,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
    ) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        candidates, fts_query, vector_status = self._retrieve_candidates(
            conn,
            db_path=db_path,
            query=query,
            candidate_limit=max(limit * 8, 40),
        )

        evidence_blocks: list[dict[str, object]] = []
        seen_contexts: set[tuple[int, int, int]] = set()
        procedure_counts: defaultdict[int, int] = defaultdict(int)

        for rank, candidate in enumerate(candidates, start=1):
            procedure_id = int(candidate["procedure_id"])
            if procedure_counts[procedure_id] >= 2:
                continue

            if candidate["hit_type"] == "chunk":
                context = self._fetch_chunk_block(conn, chunk_id=int(candidate["entity_id"]))
            elif candidate["hit_type"] == "block":
                context = self._fetch_block_context(conn, block_id=int(candidate["entity_id"]))
            else:
                context = self._fetch_context_block(
                    conn,
                    procedure_id=procedure_id,
                    statement_id=_maybe_int(candidate.get("statement_id")),
                    context_window=context_window,
                )
            context_key = (
                procedure_id,
                int(context["line_start"]),
                int(context["line_end"]),
            )
            if context_key in seen_contexts:
                continue

            seen_contexts.add(context_key)
            procedure_counts[procedure_id] += 1

            evidence_blocks.append(
                {
                    "rank": rank,
                    "score": round(float(candidate["score"]), 3),
                    "hit_type": candidate["hit_type"],
                    "retrieval_source": candidate["retrieval_source"],
                    "match_source": candidate["match_source"],
                    "procedure_name": candidate["procedure_name"],
                    "file_path": candidate["file_path"],
                    "matched_text": candidate["matched_text"],
                    "reasons": list(candidate["reasons"]),
                    "chunk_type": context.get("chunk_type"),
                    "chunk_summary": context.get("summary_text"),
                    "block_type": context.get("block_type"),
                    "block_summary": context.get("block_summary"),
                    "line_start": context["line_start"],
                    "line_end": context["line_end"],
                    "excerpt": context["excerpt"],
                    "context_statements": context["statements"],
                    "recovered_blocks": self._fetch_covering_blocks(
                        conn,
                        procedure_id=procedure_id,
                        line_start=int(context["line_start"]),
                        line_end=int(context["line_end"]),
                        limit=3,
                    ),
                    "related_context": self._fetch_related_context(
                        conn,
                        procedure_id=procedure_id,
                        procedure_name=str(candidate["procedure_name"]),
                        related_limit=related_limit,
                    ),
                }
            )

            if len(evidence_blocks) >= limit:
                break

        llm_context = self._build_llm_context(query, evidence_blocks)
        conn.close()

        return {
            "db_path": str(db_path),
            "query": query,
            "fts_query": fts_query,
            "retrieval_strategy": "fts(block/chunk/procedure/action/statement/edge) + vector(if compatible) + sql fallback + python rerank + evidence assembly",
            "vector_status": vector_status,
            "candidate_count": len(candidates),
            "evidence_count": len(evidence_blocks),
            "evidence": evidence_blocks,
            "llm_context": llm_context,
        }

    def _insert_unit(self, conn: sqlite3.Connection, unit: ParsedUnit) -> tuple[int, int]:
        attributes_json = _json(unit.attributes)
        cursor = conn.execute(
            """
            INSERT INTO files(path, file_name, unit_kind, prefix, name, chinese_name, object_id, code_line_count, attributes_json)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                unit.path,
                unit.file_name,
                unit.unit_kind,
                unit.prefix,
                unit.name,
                unit.chinese_name,
                unit.object_id,
                unit.code_line_count,
                attributes_json,
            ),
        )
        file_id = int(cursor.lastrowid)

        cursor = conn.execute(
            """
            INSERT INTO procedures(file_id, name, prefix, unit_kind, chinese_name, object_id)
            VALUES(?, ?, ?, ?, ?, ?)
            """,
            (file_id, unit.name, unit.prefix, unit.unit_kind, unit.chinese_name, unit.object_id),
        )
        procedure_id = int(cursor.lastrowid)

        conn.execute(
            """
            INSERT INTO procedures_fts(rowid, name, chinese_name, path)
            VALUES(?, ?, ?, ?)
            """,
            (procedure_id, unit.name, unit.chinese_name or "", unit.path),
        )

        for seq, history in enumerate(unit.histories, start=1):
            conn.execute(
                """
                INSERT INTO histories(file_id, seq, modified_date, version, order_number, modified_by, modified, extra_attributes_json)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    seq,
                    history.modified_date,
                    history.version,
                    history.order_number,
                    history.modified_by,
                    history.modified,
                    _json(history.extra_attributes),
                ),
            )

        for seq, param in enumerate(unit.parameters, start=1):
            conn.execute(
                """
                INSERT INTO params(file_id, seq, category, param_id, uuid, param_type, type_name, name, comments, default_value, flags, extra_attributes_json)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    seq,
                    param.category,
                    param.param_id,
                    param.uuid,
                    param.param_type,
                    param.type_name,
                    param.name,
                    param.comments,
                    param.default_value,
                    param.flags,
                    _json(param.extra_attributes),
                ),
            )

        return file_id, procedure_id

    def _insert_statements(
        self,
        conn: sqlite3.Connection,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
    ) -> tuple[Counter[str], Counter[str], Counter[str], Counter[str], Counter[str], Counter[str], Counter[str]]:
        edge_counter: Counter[str] = Counter()
        variable_ref_counter: Counter[str] = Counter()
        action_counter: Counter[str] = Counter()
        chunk_counter: Counter[str] = Counter()
        vector_counter: Counter[str] = Counter()
        block_counter: Counter[str] = Counter()
        block_edge_counter: Counter[str] = Counter()
        statement_ids_by_seq: dict[int, int] = {}
        string_hints: dict[str, str] = {}

        for seq, statement in enumerate(unit.statements, start=1):
            cursor = conn.execute(
                """
                INSERT INTO statements(file_id, procedure_id, seq, kind, line_start, line_end, raw, tag, name, condition, target, groups_json, arguments_json, reads_json, writes_json)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    procedure_id,
                    seq,
                    statement.kind,
                    statement.line_start,
                    statement.line_end,
                    statement.raw,
                    statement.tag,
                    statement.name,
                    statement.condition,
                    statement.target,
                    _json(statement.groups),
                    _json(statement.arguments),
                    _json(statement.reads),
                    _json(statement.writes),
                ),
            )
            statement_id = int(cursor.lastrowid)
            statement_ids_by_seq[seq] = statement_id

            conn.execute(
                """
                INSERT INTO statements_fts(rowid, raw, name, condition, target, procedure_name, file_path)
                VALUES(?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    statement_id,
                    statement.raw,
                    statement.name or "",
                    statement.condition or "",
                    statement.target or "",
                    unit.name,
                    unit.path,
                ),
            )

            self._insert_variable_refs(conn, file_id, procedure_id, statement_id, statement, variable_ref_counter)
            inserted_actions = self._insert_action_and_edges(
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
            action_counter.update(inserted_actions)
            _update_string_hints(string_hints, statement)

        local_chunks, local_vectors = self._insert_chunks(conn, file_id=file_id, procedure_id=procedure_id, unit=unit)
        chunk_counter.update(local_chunks)
        vector_counter.update(local_vectors)
        local_blocks, local_block_edges = self._insert_blocks(
            conn,
            file_id=file_id,
            procedure_id=procedure_id,
            unit=unit,
            statement_ids_by_seq=statement_ids_by_seq,
        )
        block_counter.update(local_blocks)
        block_edge_counter.update(local_block_edges)

        return edge_counter, variable_ref_counter, action_counter, chunk_counter, vector_counter, block_counter, block_edge_counter

    def _insert_chunks(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
    ) -> tuple[Counter[str], Counter[str]]:
        counter: Counter[str] = Counter()
        vector_counter: Counter[str] = Counter()
        semantic_chunks = _build_semantic_chunks(unit.name, unit.statements)
        if not semantic_chunks:
            return counter, vector_counter

        for seq, chunk in enumerate(semantic_chunks, start=1):
            cursor = conn.execute(
                """
                INSERT INTO chunks(
                  file_id,
                  procedure_id,
                  seq,
                  chunk_type,
                  line_start,
                  line_end,
                  statement_start_seq,
                  statement_end_seq,
                  statement_count,
                  anchor_kinds_json,
                  action_names_json,
                  target_names_json,
                  variable_names_json,
                  content,
                  summary_text
                )
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    procedure_id,
                    seq,
                    chunk["chunk_type"],
                    chunk["line_start"],
                    chunk["line_end"],
                    chunk["statement_start_seq"],
                    chunk["statement_end_seq"],
                    chunk["statement_count"],
                    _json(chunk["anchor_kinds"]),
                    _json(chunk["action_names"]),
                    _json(chunk["target_names"]),
                    _json(chunk["variable_names"]),
                    chunk["content"],
                    chunk["summary_text"],
                ),
            )
            chunk_id = int(cursor.lastrowid)
            conn.execute(
                """
                INSERT INTO chunks_fts(rowid, chunk_type, procedure_name, file_path, summary_text, content)
                VALUES(?, ?, ?, ?, ?, ?)
                """,
                (
                    chunk_id,
                    chunk["chunk_type"],
                    unit.name,
                    unit.path,
                    chunk["summary_text"],
                    chunk["content"],
                ),
            )
            counter[str(chunk["chunk_type"])] += 1

        return counter, vector_counter

    def _populate_missing_chunk_vectors(self, conn: sqlite3.Connection) -> dict[str, object]:
        self._validate_vector_space_for_population(conn)
        batch_size = _embedder_batch_size(self.embedder)
        missing_before = self._missing_chunk_vector_count(conn)
        inserted = 0
        batches = 0
        provider_counts: Counter[str] = Counter()

        while True:
            rows = conn.execute(
                """
                SELECT c.id, c.summary_text, c.content
                FROM chunks c
                LEFT JOIN chunk_vectors cv ON cv.chunk_id = c.id
                WHERE cv.chunk_id IS NULL
                ORDER BY c.id
                LIMIT ?
                """,
                (batch_size,),
            ).fetchall()
            if not rows:
                break

            embedding_inputs = [f"{row[1]}\n{row[2]}" for row in rows]
            vectors = self.embedder.embed_texts(embedding_inputs)
            embedder_info = self.embedder.info

            with conn:
                for row, vector in zip(rows, vectors, strict=True):
                    conn.execute(
                        """
                        INSERT OR REPLACE INTO chunk_vectors(chunk_id, provider, model, dimension, vector_json)
                        VALUES(?, ?, ?, ?, ?)
                        """,
                        (
                            int(row[0]),
                            embedder_info.provider,
                            embedder_info.model,
                            len(vector),
                            _json(vector),
                        ),
                    )
                    provider_counts[embedder_info.provider] += 1
                self._store_embedding_metadata(conn, embedder_info)

            inserted += len(rows)
            batches += 1

        final_info = self.embedder.info
        with conn:
            self._store_embedding_metadata(conn, final_info)

        return {
            "batch_size": batch_size,
            "missing_before": missing_before,
            "inserted": inserted,
            "batches": batches,
            "missing_after": self._missing_chunk_vector_count(conn),
            "provider_counts": dict(provider_counts),
        }

    def _validate_resume_source(self, conn: sqlite3.Connection, root: Path) -> None:
        source_root = self._metadata(conn, "source_root")
        if source_root is None:
            raise EmbeddingConfigError("Cannot resume vectors because source_root metadata is missing")
        if not _paths_match(source_root, root):
            raise EmbeddingConfigError(f"Cannot resume vectors for {root}; index source_root is {source_root}")

    def _validate_vector_space_for_population(self, conn: sqlite3.Connection) -> None:
        current_info = self.embedder.info
        db_provider = self._metadata(conn, "embedding_provider")
        db_model = self._metadata(conn, "embedding_model")
        db_dimension = _maybe_int(self._metadata(conn, "embedding_dimension"))

        if db_provider and current_info.provider != db_provider:
            raise EmbeddingConfigError(
                f"Embedding provider mismatch: index has {db_provider}, current config has {current_info.provider}"
            )
        if db_model and current_info.model != db_model:
            raise EmbeddingConfigError(
                f"Embedding model mismatch: index has {db_model}, current config has {current_info.model}"
            )
        if db_dimension and current_info.dimension and current_info.dimension != db_dimension:
            raise EmbeddingConfigError(
                f"Embedding dimension mismatch: index has {db_dimension}, current config has {current_info.dimension}"
            )

    def _store_embedding_metadata(self, conn: sqlite3.Connection, info: EmbeddingInfo) -> None:
        dimension = info.dimension
        if dimension == 0:
            dimension = _maybe_int(self._metadata(conn, "embedding_dimension")) or 0
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("embedding_provider", info.provider))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("embedding_model", info.model))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("embedding_dimension", str(dimension)))

    def _missing_chunk_vector_count(self, conn: sqlite3.Connection) -> int:
        return int(
            conn.execute(
                """
                SELECT COUNT(*)
                FROM chunks c
                LEFT JOIN chunk_vectors cv ON cv.chunk_id = c.id
                WHERE cv.chunk_id IS NULL
                """
            ).fetchone()[0]
        )

    def _insert_blocks(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
        statement_ids_by_seq: dict[int, int],
    ) -> tuple[Counter[str], Counter[str]]:
        block_counter: Counter[str] = Counter()
        block_edge_counter: Counter[str] = Counter()
        recovered_blocks = _recover_blocks(unit.statements)

        for seq, block in enumerate(recovered_blocks, start=1):
            statements = unit.statements[block["statement_start_seq"] - 1 : block["statement_end_seq"]]
            statement_rows = [
                {
                    "statement_id": statement_ids_by_seq.get(block["statement_start_seq"] + offset),
                    "seq": block["statement_start_seq"] + offset,
                    "kind": statement.kind,
                    "line_start": statement.line_start,
                    "line_end": statement.line_end,
                    "raw": statement.raw,
                }
                for offset, statement in enumerate(statements)
            ]
            action_names, target_names, variable_names = _collect_block_entities(statements)
            summary_text = _summarize_block(
                procedure_name=unit.name,
                block_type=str(block["block_type"]),
                anchor_name=str(block["anchor_name"]),
                statements=statements,
                action_names=action_names,
                target_names=target_names,
            )
            excerpt = _format_excerpt(statement_rows)
            table_names = self._fetch_block_table_names(
                conn,
                procedure_id=procedure_id,
                statement_start_seq=int(block["statement_start_seq"]),
                statement_end_seq=int(block["statement_end_seq"]),
            )

            cursor = conn.execute(
                """
                INSERT INTO blocks(
                  file_id,
                  procedure_id,
                  seq,
                  block_type,
                  anchor_name,
                  line_start,
                  line_end,
                  statement_start_seq,
                  statement_end_seq,
                  statement_count,
                  anchor_statement_id,
                  summary_text,
                  excerpt,
                  action_names_json,
                  target_names_json,
                  table_names_json,
                  variable_names_json
                )
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    procedure_id,
                    seq,
                    block["block_type"],
                    block["anchor_name"],
                    block["line_start"],
                    block["line_end"],
                    block["statement_start_seq"],
                    block["statement_end_seq"],
                    len(statements),
                    statement_ids_by_seq.get(int(block["anchor_seq"])),
                    summary_text,
                    excerpt,
                    _json(action_names),
                    _json(target_names),
                    _json(table_names),
                    _json(variable_names),
                ),
            )
            block_id = int(cursor.lastrowid)
            conn.execute(
                """
                INSERT INTO blocks_fts(rowid, block_type, anchor_name, procedure_name, file_path, summary_text, excerpt)
                VALUES(?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    block_id,
                    block["block_type"],
                    block["anchor_name"],
                    unit.name,
                    unit.path,
                    summary_text,
                    excerpt,
                ),
            )
            block_counter[str(block["block_type"])] += 1

            for edge in self._fetch_block_edges(
                conn,
                procedure_id=procedure_id,
                statement_start_seq=int(block["statement_start_seq"]),
                statement_end_seq=int(block["statement_end_seq"]),
            ):
                conn.execute(
                    """
                    INSERT INTO block_edges(block_id, edge_type, target_name, target_kind, detail_json)
                    VALUES(?, ?, ?, ?, ?)
                    """,
                    (
                        block_id,
                        edge["edge_type"],
                        edge["target_name"],
                        edge["target_kind"],
                        _json(edge["detail"]),
                    ),
                )
                block_edge_counter[str(edge["edge_type"])] += 1

        return block_counter, block_edge_counter

    def _fetch_block_table_names(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_start_seq: int,
        statement_end_seq: int,
    ) -> list[str]:
        rows = conn.execute(
            """
            SELECT DISTINCT e.target_name
            FROM edges e
            JOIN statements s ON s.id = e.statement_id
            WHERE e.procedure_id = ?
              AND s.seq BETWEEN ? AND ?
              AND e.edge_type IN ('reads_table', 'writes_table', 'reads_dynamic_table', 'writes_dynamic_table')
            ORDER BY e.target_name
            """,
            (procedure_id, statement_start_seq, statement_end_seq),
        ).fetchall()
        return [str(row[0]) for row in rows]

    def _fetch_block_edges(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_start_seq: int,
        statement_end_seq: int,
    ) -> list[dict[str, object]]:
        rows = conn.execute(
            """
            SELECT DISTINCT
              e.edge_type AS edge_type,
              e.target_name AS target_name,
              e.target_kind AS target_kind,
              e.detail_json AS detail_json
            FROM edges e
            JOIN statements s ON s.id = e.statement_id
            WHERE e.procedure_id = ?
              AND s.seq BETWEEN ? AND ?
            ORDER BY e.edge_type, e.target_name
            """,
            (procedure_id, statement_start_seq, statement_end_seq),
        ).fetchall()
        return [
            {
                "edge_type": str(row[0]),
                "target_name": str(row[1]),
                "target_kind": str(row[2]),
                "detail": json.loads(row[3]),
            }
            for row in rows
        ]

    def _insert_variable_refs(
        self,
        conn: sqlite3.Connection,
        file_id: int,
        procedure_id: int,
        statement_id: int,
        statement: CodeStatement,
        counter: Counter[str],
    ) -> None:
        for var_name in statement.reads:
            conn.execute(
                """
                INSERT INTO variable_refs(file_id, procedure_id, statement_id, var_name, access_type)
                VALUES(?, ?, ?, ?, ?)
                """,
                (file_id, procedure_id, statement_id, var_name, "read"),
            )
            counter["read"] += 1

        for var_name in statement.writes:
            conn.execute(
                """
                INSERT INTO variable_refs(file_id, procedure_id, statement_id, var_name, access_type)
                VALUES(?, ?, ?, ?, ?)
                """,
                (file_id, procedure_id, statement_id, var_name, "write"),
            )
            counter["write"] += 1

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
        action_counter: Counter[str] = Counter()
        action_name = statement.name if statement.kind in {"action", "call"} else None
        target_name, target_kind = _derive_target(statement)

        if action_name is not None:
            cursor = conn.execute(
                """
                INSERT INTO actions(file_id, procedure_id, statement_id, seq, kind, tag, action_name, target_name, target_kind)
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    file_id,
                    procedure_id,
                    statement_id,
                    seq,
                    statement.kind,
                    statement.tag,
                    action_name,
                    target_name,
                    target_kind,
                ),
            )
            action_id = int(cursor.lastrowid)
            action_counter[statement.kind] += 1
            conn.execute(
                """
                INSERT INTO actions_fts(rowid, action_name, target_name, procedure_name, file_path, raw)
                VALUES(?, ?, ?, ?, ?, ?)
                """,
                (
                    action_id,
                    action_name,
                    target_name or "",
                    unit.name,
                    unit.path,
                    statement.raw,
                ),
            )

        if statement.kind == "call" and statement.name:
            self._insert_edge(
                conn,
                file_id=file_id,
                procedure_id=procedure_id,
                statement_id=statement_id,
                procedure_name=unit.name,
                file_path=unit.path,
                edge_type="calls_procedure",
                source_name=unit.name,
                target_name=statement.name,
                target_kind="procedure",
                detail={"tag": statement.tag, "line_start": statement.line_start, "line_end": statement.line_end},
            )
            edge_counter["calls_procedure"] += 1

        if statement.kind == "action" and statement.name:
            self._insert_edge(
                conn,
                file_id=file_id,
                procedure_id=procedure_id,
                statement_id=statement_id,
                procedure_name=unit.name,
                file_path=unit.path,
                edge_type="uses_action",
                source_name=unit.name,
                target_name=statement.name,
                target_kind="action",
                detail={"tag": statement.tag, "line_start": statement.line_start, "line_end": statement.line_end},
            )
            edge_counter["uses_action"] += 1

            if target_name and target_kind != "unknown":
                if statement.name in READ_ACTIONS:
                    edge_type = "reads_table" if target_kind == "table" else "uses_target"
                elif statement.name in WRITE_ACTIONS:
                    edge_type = "writes_table" if target_kind == "table" else "uses_target"
                elif statement.name in COMPONENT_ACTIONS:
                    edge_type = "uses_component"
                else:
                    edge_type = "uses_target"

                self._insert_edge(
                    conn,
                    file_id=file_id,
                    procedure_id=procedure_id,
                    statement_id=statement_id,
                    procedure_name=unit.name,
                    file_path=unit.path,
                    edge_type=edge_type,
                    source_name=unit.name,
                    target_name=target_name,
                    target_kind=target_kind,
                    detail={"action_name": statement.name, "tag": statement.tag},
                )
                edge_counter[edge_type] += 1

            for sql_edge in _extract_sql_access_edges(statement, string_hints):
                self._insert_edge(
                    conn,
                    file_id=file_id,
                    procedure_id=procedure_id,
                    statement_id=statement_id,
                    procedure_name=unit.name,
                    file_path=unit.path,
                    edge_type=str(sql_edge["edge_type"]),
                    source_name=unit.name,
                    target_name=str(sql_edge["target_name"]),
                    target_kind="table",
                    detail={
                        "action_name": statement.name,
                        "sql_operation": sql_edge["operation"],
                        "sql_source": sql_edge["sql_source"],
                    },
                )
                edge_counter[str(sql_edge["edge_type"])] += 1

        if statement.kind == "assignment" and statement.writes:
            for target in statement.writes:
                self._insert_edge(
                    conn,
                    file_id=file_id,
                    procedure_id=procedure_id,
                    statement_id=statement_id,
                    procedure_name=unit.name,
                    file_path=unit.path,
                    edge_type="writes_variable",
                    source_name=unit.name,
                    target_name=target,
                    target_kind="variable",
                    detail={"line_start": statement.line_start, "line_end": statement.line_end},
                )
                edge_counter["writes_variable"] += 1

        if statement.kind == "goto" and statement.target:
            self._insert_edge(
                conn,
                file_id=file_id,
                procedure_id=procedure_id,
                statement_id=statement_id,
                procedure_name=unit.name,
                file_path=unit.path,
                edge_type="jumps_to_label",
                source_name=unit.name,
                target_name=statement.target,
                target_kind="label",
                detail={"line_start": statement.line_start, "line_end": statement.line_end},
            )
            edge_counter["jumps_to_label"] += 1

            if statement.target in EXIT_LABEL_NAMES:
                self._insert_edge(
                    conn,
                    file_id=file_id,
                    procedure_id=procedure_id,
                    statement_id=statement_id,
                    procedure_name=unit.name,
                    file_path=unit.path,
                    edge_type="jumps_to_exit",
                    source_name=unit.name,
                    target_name=statement.target,
                    target_kind="label",
                    detail={"line_start": statement.line_start, "line_end": statement.line_end},
                )
                edge_counter["jumps_to_exit"] += 1

        if statement.kind == "label" and statement.target:
            self._insert_edge(
                conn,
                file_id=file_id,
                procedure_id=procedure_id,
                statement_id=statement_id,
                procedure_name=unit.name,
                file_path=unit.path,
                edge_type="defines_label",
                source_name=unit.name,
                target_name=statement.target,
                target_kind="label",
                detail={"line_start": statement.line_start, "line_end": statement.line_end},
            )
            edge_counter["defines_label"] += 1

        return action_counter

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
        cursor = conn.execute(
            """
            INSERT INTO edges(file_id, procedure_id, statement_id, edge_type, source_name, target_name, target_kind, detail_json)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                file_id,
                procedure_id,
                statement_id,
                edge_type,
                source_name,
                target_name,
                target_kind,
                _json(detail),
            ),
        )
        edge_id = int(cursor.lastrowid)

        conn.execute(
            """
            INSERT INTO edges_fts(rowid, edge_type, source_name, target_name, target_kind, procedure_name, file_path)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            (edge_id, edge_type, source_name, target_name, target_kind, procedure_name, file_path),
        )

    def _retrieve_candidates(
        self,
        conn: sqlite3.Connection,
        *,
        db_path: str | Path,
        query: str,
        candidate_limit: int,
    ) -> tuple[list[dict[str, object]], str | None, dict[str, object]]:
        fts_query = _build_fts_query(query)
        query_analysis = _analyze_query(query)
        candidates: dict[tuple[object, ...], dict[str, object]] = {}
        vector_status = self._vector_status(conn)

        if fts_query:
            for candidate in self._run_fts_queries(conn, raw_query=query, fts_query=fts_query, limit=candidate_limit):
                _merge_candidate(candidates, candidate)

        vector_candidates, vector_status = self._run_vector_queries(
            conn,
            db_path=db_path,
            query=query,
            limit=candidate_limit,
            initial_status=vector_status,
        )
        for candidate in vector_candidates:
            _merge_candidate(candidates, candidate)

        for candidate in self._run_like_queries(conn, query=query, limit=candidate_limit):
            _merge_candidate(candidates, candidate)

        ranked = sorted(
            (
                self._rerank_candidate(candidate, query=query, query_analysis=query_analysis)
                for candidate in candidates.values()
            ),
            key=lambda item: (-float(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"])),
        )
        ranked = self._apply_call_chain_rerank(
            conn,
            ranked,
            seed_limit=min(candidate_limit, 12),
            query_analysis=query_analysis,
        )
        return ranked, fts_query, vector_status

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
            query_vector = self.embedder.embed_texts([query])[0]
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
        overlap_hints = _vector_hint_tokens(query)

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
        db_provider = self._metadata(conn, "embedding_provider")
        db_model = self._metadata(conn, "embedding_model")
        db_dimension_raw = self._metadata(conn, "embedding_dimension")
        vector_enabled = (self._metadata(conn, "vector_enabled") or "").lower() == "true"
        vector_count = int(conn.execute("SELECT COUNT(*) FROM chunk_vectors").fetchone()[0])

        current_info = self.embedder.info
        status = {
            "enabled": False,
            "reason": "metadata_missing",
            "index_provider": db_provider,
            "index_model": db_model,
            "index_dimension": _maybe_int(db_dimension_raw),
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

        db_dimension = _maybe_int(db_dimension_raw)
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
        embedder_info = self.embedder.info
        cache_key = (
            str(db_file.resolve()),
            stat.st_mtime_ns,
            stat.st_size,
            embedder_info.provider,
            embedder_info.model,
        )
        cached = self._vector_cache.get(cache_key)
        if cached is not None:
            return cached

        self._vector_cache = {
            key: value
            for key, value in self._vector_cache.items()
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
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "summary_text": str(row["summary_text"]),
                "content": str(row["content"]),
                "vector": [float(value) for value in json.loads(row["vector_json"])],
            }
            for row in rows
        ]
        self._vector_cache[cache_key] = cached_rows
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
                  b.line_start AS line_start,
                  b.line_end AS line_end,
                  COALESCE(NULLIF(b.summary_text, ''), b.block_type) AS matched_text,
                  'block_summary' AS match_source,
                  -bm25(blocks_fts, 2.0, 1.0, 1.0, 1.0, 6.0, 4.0) AS source_rank,
                  COALESCE(b.summary_text, '') || ' ' || COALESCE(b.excerpt, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  c.line_start AS line_start,
                  c.line_end AS line_end,
                  COALESCE(NULLIF(c.summary_text, ''), c.chunk_type) AS matched_text,
                  'chunk_summary' AS match_source,
                  -bm25(chunks_fts, 2.0, 1.5, 1.0, 6.0, 4.0) AS source_rank,
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.content, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  NULL AS line_start,
                  NULL AS line_end,
                  COALESCE(NULLIF(p.chinese_name, ''), p.name) AS matched_text,
                  'procedure_fts' AS match_source,
                  -bm25(procedures_fts, 8.0, 5.0, 2.0) AS source_rank,
                  COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') || ' ' || COALESCE(f.path, '') AS search_text
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
                  COALESCE(a.action_name, '') || ' ' || COALESCE(a.target_name, '') || ' ' || COALESCE(s.raw, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  s.raw AS matched_text,
                  s.kind AS match_source,
                  -bm25(statements_fts, 6.0, 2.0, 2.0, 2.0, 1.5, 1.0) AS source_rank,
                  COALESCE(s.raw, '') || ' ' || COALESCE(s.name, '') || ' ' || COALESCE(s.condition, '') || ' ' || COALESCE(s.target, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  s.line_start AS line_start,
                  s.line_end AS line_end,
                  e.target_name AS matched_text,
                  e.edge_type AS match_source,
                  -bm25(edges_fts, 5.0, 1.0, 4.0, 1.0, 1.0, 1.0) AS source_rank,
                  COALESCE(e.edge_type, '') || ' ' || COALESCE(e.source_name, '') || ' ' || COALESCE(e.target_name, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  b.line_start AS line_start,
                  b.line_end AS line_end,
                  COALESCE(NULLIF(b.summary_text, ''), b.block_type) AS matched_text,
                  'block_summary' AS match_source,
                  0.0 AS source_rank,
                  COALESCE(b.summary_text, '') || ' ' || COALESCE(b.excerpt, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  c.line_start AS line_start,
                  c.line_end AS line_end,
                  COALESCE(NULLIF(c.summary_text, ''), c.chunk_type) AS matched_text,
                  'chunk_summary' AS match_source,
                  0.0 AS source_rank,
                  COALESCE(c.summary_text, '') || ' ' || COALESCE(c.content, '') || ' ' || COALESCE(p.name, '') AS search_text
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
                  NULL AS line_start,
                  NULL AS line_end,
                  CASE
                    WHEN p.name LIKE ? THEN p.name
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN COALESCE(p.chinese_name, '')
                    ELSE f.path
                  END AS matched_text,
                  CASE
                    WHEN p.name LIKE ? THEN 'procedure_name'
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN 'procedure_chinese_name'
                    ELSE 'file_path'
                  END AS match_source,
                  0.0 AS source_rank,
                  COALESCE(p.name, '') || ' ' || COALESCE(p.chinese_name, '') || ' ' || COALESCE(f.path, '') AS search_text
                FROM procedures p
                JOIN files f ON f.id = p.file_id
                WHERE p.name LIKE ? OR COALESCE(p.chinese_name, '') LIKE ? OR f.path LIKE ?
                LIMIT ?
                """,
                (like, like, like, like, like, like, like, limit),
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

    def _rerank_candidate(
        self,
        candidate: dict[str, object],
        *,
        query: str,
        query_analysis: dict[str, object],
    ) -> dict[str, object]:
        normalized_query = query.strip().lower()
        query_tokens = _tokenize_query(query)
        search_text = str(candidate.get("search_text") or "").lower()
        matched_text = str(candidate.get("matched_text") or "").lower()
        procedure_name = str(candidate.get("procedure_name") or "").lower()
        file_path = str(candidate.get("file_path") or "").lower()

        overlap_tokens = [token for token in query_tokens if token in search_text]
        coverage = len(set(overlap_tokens))
        token_ratio = coverage / max(len(query_tokens), 1)

        score = float(candidate["base_score"])
        reasons = list(candidate.get("reasons", []))

        if str(candidate["retrieval_source"]).startswith("fts"):
            score += 10.0
            reasons.append("fts_hit")

        if coverage:
            score += coverage * 6.0
            score += token_ratio * 18.0
            reasons.append(f"token_overlap={coverage}/{max(len(query_tokens), 1)}")

        if normalized_query and normalized_query in matched_text:
            score += 16.0
            reasons.append("exact_match_in_hit")
        elif normalized_query and normalized_query in search_text:
            score += 9.0
            reasons.append("exact_match_in_context")

        if normalized_query and normalized_query in procedure_name:
            score += 8.0
            reasons.append("procedure_name_match")

        if normalized_query and normalized_query in file_path:
            score += 4.0
            reasons.append("file_path_match")

        if candidate["hit_type"] == "chunk":
            score += 5.0
        elif candidate["hit_type"] == "action":
            score += 4.0
        elif candidate["hit_type"] == "procedure":
            score += 3.0

        matched_via = list(candidate.get("matched_via", []))
        if len(matched_via) > 1:
            score += min(len(matched_via) * 1.5, 4.5)
            reasons.append(f"multi_source_match={len(matched_via)}")

        intent_bonus, intent_reasons = _intent_bonus(
            candidate=candidate,
            query_analysis=query_analysis,
            search_text=search_text,
            matched_text=matched_text,
            procedure_name=procedure_name,
        )
        score += intent_bonus
        reasons.extend(intent_reasons)

        score += max(min(float(candidate.get("source_rank") or 0.0), 12.0), -12.0)

        candidate["score"] = round(score, 6)
        candidate["reasons"] = reasons
        return candidate

    def _apply_call_chain_rerank(
        self,
        conn: sqlite3.Connection,
        ranked: list[dict[str, object]],
        *,
        seed_limit: int,
        query_analysis: dict[str, object],
    ) -> list[dict[str, object]]:
        if not ranked:
            return ranked

        seed_names = {
            str(item["procedure_name"])
            for item in ranked[:seed_limit]
            if item.get("procedure_name")
        }
        if not seed_names:
            return ranked

        neighbor_cache: dict[str, tuple[set[str], set[str]]] = {}
        reranked: list[dict[str, object]] = []
        call_chain_multiplier = _call_chain_bonus_multiplier(query_analysis)
        for candidate in ranked:
            procedure_name = str(candidate.get("procedure_name") or "")
            if not procedure_name:
                reranked.append(candidate)
                continue

            one_hop, two_hop = neighbor_cache.get(procedure_name, (set(), set()))
            if not one_hop and not two_hop:
                one_hop, two_hop = self._procedure_call_neighbors(conn, procedure_name=procedure_name)
                neighbor_cache[procedure_name] = (one_hop, two_hop)

            one_overlap = sorted((one_hop - {procedure_name}) & seed_names)
            two_overlap = sorted((two_hop - one_hop - {procedure_name}) & seed_names)
            if one_overlap or two_overlap:
                bonus = (len(one_overlap) * 3.0 + len(two_overlap) * 1.5) * call_chain_multiplier
                candidate["score"] = round(float(candidate["score"]) + bonus, 6)
                reasons = list(candidate.get("reasons", []))
                if one_overlap:
                    reasons.append(f"call_chain_one_hop={','.join(one_overlap[:3])}")
                if two_overlap:
                    reasons.append(f"call_chain_two_hop={','.join(two_overlap[:3])}")
                if call_chain_multiplier != 1.0:
                    reasons.append(f"call_chain_weight={call_chain_multiplier:.2f}")
                candidate["reasons"] = reasons

            reranked.append(candidate)

        return sorted(
            reranked,
            key=lambda item: (-float(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"])),
        )

    def _procedure_call_neighbors(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_name: str,
    ) -> tuple[set[str], set[str]]:
        aliases = self._procedure_aliases(conn, procedure_name=procedure_name)

        outgoing = {
            self._resolve_procedure_name(conn, str(row[0]))
            for row in conn.execute(
                """
                SELECT DISTINCT target_name
                FROM edges
                WHERE source_name = ? AND edge_type = 'calls_procedure'
                """,
                (procedure_name,),
            ).fetchall()
        }
        incoming = {
            str(row[0])
            for row in conn.execute(
                f"""
                SELECT DISTINCT source_name
                FROM edges
                WHERE target_name IN ({",".join("?" for _ in aliases)}) AND edge_type = 'calls_procedure'
                """,
                aliases,
            ).fetchall()
        }

        one_hop = outgoing | incoming
        two_hop: set[str] = set()
        frontier = list(one_hop)
        for neighbor_name in frontier:
            second_outgoing = {
                self._resolve_procedure_name(conn, str(row[0]))
                for row in conn.execute(
                    """
                    SELECT DISTINCT target_name
                    FROM edges
                    WHERE source_name = ? AND edge_type = 'calls_procedure'
                    """,
                    (neighbor_name,),
                ).fetchall()
            }
            second_incoming = {
                str(row[0])
                for row in conn.execute(
                    f"""
                    SELECT DISTINCT source_name
                    FROM edges
                    WHERE target_name IN ({",".join("?" for _ in self._procedure_aliases(conn, procedure_name=neighbor_name))}) AND edge_type = 'calls_procedure'
                    """,
                    self._procedure_aliases(conn, procedure_name=neighbor_name),
                ).fetchall()
            }
            two_hop.update(second_outgoing)
            two_hop.update(second_incoming)

        return one_hop, two_hop

    def _fetch_context_block(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_id: int | None,
        context_window: int,
    ) -> dict[str, object]:
        if statement_id is not None:
            anchor = conn.execute(
                "SELECT seq FROM statements WHERE id = ?",
                (statement_id,),
            ).fetchone()
        else:
            anchor = None

        if anchor is not None:
            start_seq = max(int(anchor["seq"]) - context_window, 1)
            end_seq = int(anchor["seq"]) + context_window
            rows = conn.execute(
                """
                SELECT id, seq, kind, line_start, line_end, raw
                FROM statements
                WHERE procedure_id = ? AND seq BETWEEN ? AND ?
                ORDER BY seq
                """,
                (procedure_id, start_seq, end_seq),
            ).fetchall()
        else:
            rows = conn.execute(
                """
                SELECT id, seq, kind, line_start, line_end, raw
                FROM statements
                WHERE procedure_id = ? AND kind != 'brace'
                ORDER BY seq
                LIMIT ?
                """,
                (procedure_id, max(context_window * 2 + 1, 5)),
            ).fetchall()

        if not rows:
            rows = conn.execute(
                """
                SELECT id, seq, kind, line_start, line_end, raw
                FROM statements
                WHERE procedure_id = ?
                ORDER BY seq
                LIMIT 5
                """,
                (procedure_id,),
            ).fetchall()

        statements = [
            {
                "statement_id": int(row["id"]),
                "seq": int(row["seq"]),
                "kind": str(row["kind"]),
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "raw": str(row["raw"]),
            }
            for row in rows
        ]
        line_start = min((item["line_start"] for item in statements), default=0)
        line_end = max((item["line_end"] for item in statements), default=0)

        return {
            "line_start": line_start,
            "line_end": line_end,
            "statements": statements,
            "excerpt": _format_excerpt(statements),
        }

    def _fetch_chunk_block(
        self,
        conn: sqlite3.Connection,
        *,
        chunk_id: int,
    ) -> dict[str, object]:
        chunk_row = conn.execute(
            """
            SELECT
              procedure_id,
              chunk_type,
              line_start,
              line_end,
              statement_start_seq,
              statement_end_seq,
              summary_text
            FROM chunks
            WHERE id = ?
            """,
            (chunk_id,),
        ).fetchone()
        if chunk_row is None:
            raise ValueError(f"Chunk does not exist: {chunk_id}")

        rows = conn.execute(
            """
            SELECT id, seq, kind, line_start, line_end, raw
            FROM statements
            WHERE procedure_id = ? AND seq BETWEEN ? AND ?
            ORDER BY seq
            """,
            (
                int(chunk_row["procedure_id"]),
                int(chunk_row["statement_start_seq"]),
                int(chunk_row["statement_end_seq"]),
            ),
        ).fetchall()

        statements = [
            {
                "statement_id": int(row["id"]),
                "seq": int(row["seq"]),
                "kind": str(row["kind"]),
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "raw": str(row["raw"]),
            }
            for row in rows
        ]
        return {
            "chunk_type": str(chunk_row["chunk_type"]),
            "summary_text": str(chunk_row["summary_text"]),
            "line_start": int(chunk_row["line_start"]),
            "line_end": int(chunk_row["line_end"]),
            "statements": statements,
            "excerpt": _format_excerpt(statements),
        }

    def _fetch_block_context(
        self,
        conn: sqlite3.Connection,
        *,
        block_id: int,
    ) -> dict[str, object]:
        block_row = conn.execute(
            """
            SELECT
              procedure_id,
              block_type,
              summary_text,
              line_start,
              line_end,
              statement_start_seq,
              statement_end_seq
            FROM blocks
            WHERE id = ?
            """,
            (block_id,),
        ).fetchone()
        if block_row is None:
            raise ValueError(f"Block does not exist: {block_id}")

        rows = conn.execute(
            """
            SELECT id, seq, kind, line_start, line_end, raw
            FROM statements
            WHERE procedure_id = ? AND seq BETWEEN ? AND ?
            ORDER BY seq
            """,
            (
                int(block_row["procedure_id"]),
                int(block_row["statement_start_seq"]),
                int(block_row["statement_end_seq"]),
            ),
        ).fetchall()

        statements = [
            {
                "statement_id": int(row["id"]),
                "seq": int(row["seq"]),
                "kind": str(row["kind"]),
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "raw": str(row["raw"]),
            }
            for row in rows
        ]
        return {
            "block_type": str(block_row["block_type"]),
            "block_summary": str(block_row["summary_text"]),
            "line_start": int(block_row["line_start"]),
            "line_end": int(block_row["line_end"]),
            "statements": statements,
            "excerpt": _format_excerpt(statements),
        }

    def _fetch_covering_blocks(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        line_start: int,
        line_end: int,
        limit: int,
    ) -> list[dict[str, object]]:
        rows = conn.execute(
            """
            SELECT
              id,
              block_type,
              anchor_name,
              line_start,
              line_end,
              summary_text
            FROM blocks
            WHERE procedure_id = ?
              AND line_start <= ?
              AND line_end >= ?
            ORDER BY (line_end - line_start) ASC, line_start ASC
            LIMIT ?
            """,
            (procedure_id, line_end, line_start, limit),
        ).fetchall()

        blocks = []
        for row in rows:
            block_id = int(row["id"])
            blocks.append(
                {
                    "block_type": str(row["block_type"]),
                    "anchor_name": str(row["anchor_name"]),
                    "line_start": int(row["line_start"]),
                    "line_end": int(row["line_end"]),
                    "summary_text": str(row["summary_text"]),
                    "relations": self._fetch_block_relation_summary(conn, block_id=block_id, limit=4),
                }
            )
        return blocks

    def _fetch_block_relation_summary(
        self,
        conn: sqlite3.Connection,
        *,
        block_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        rows = conn.execute(
            """
            SELECT edge_type, target_name, target_kind
            FROM block_edges
            WHERE block_id = ?
            ORDER BY
              CASE edge_type
                WHEN 'calls_procedure' THEN 0
                WHEN 'reads_table' THEN 1
                WHEN 'writes_table' THEN 2
                WHEN 'reads_dynamic_table' THEN 3
                WHEN 'writes_dynamic_table' THEN 4
                ELSE 3
              END,
              target_name
            LIMIT ?
            """,
            (block_id, limit),
        ).fetchall()
        return [
            {
                "edge_type": str(row["edge_type"]),
                "target_name": str(row["target_name"]),
                "target_kind": str(row["target_kind"]),
            }
            for row in rows
        ]

    def _fetch_related_context(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        related_limit: int,
    ) -> dict[str, object]:
        aliases = self._procedure_aliases(conn, procedure_id=procedure_id, procedure_name=procedure_name)
        outgoing_calls = [
            self._resolve_procedure_name(conn, str(row["target_name"]))
            for row in conn.execute(
                """
                SELECT DISTINCT target_name
                FROM edges
                WHERE procedure_id = ? AND edge_type = 'calls_procedure'
                ORDER BY target_name
                LIMIT ?
                """,
                (procedure_id, related_limit),
            ).fetchall()
        ]
        outgoing_calls = _dedupe_strings(outgoing_calls)

        incoming_callers = [
            str(row["source_name"])
            for row in conn.execute(
                f"""
                SELECT DISTINCT source_name
                FROM edges
                WHERE edge_type = 'calls_procedure' AND target_name IN ({",".join("?" for _ in aliases)})
                ORDER BY source_name
                LIMIT ?
                """,
                (*aliases, related_limit),
            ).fetchall()
        ]

        related_tables = [
            {
                "name": str(row["target_name"]),
                "edge_type": str(row["edge_type"]),
            }
            for row in conn.execute(
                """
                SELECT DISTINCT target_name, edge_type
                FROM edges
                WHERE procedure_id = ? AND edge_type IN ('reads_table', 'writes_table', 'reads_dynamic_table', 'writes_dynamic_table')
                ORDER BY target_name
                LIMIT ?
                """,
                (procedure_id, related_limit),
            ).fetchall()
        ]

        related_actions = [
            str(row["action_name"])
            for row in conn.execute(
                """
                SELECT DISTINCT action_name
                FROM actions
                WHERE procedure_id = ? AND kind = 'action'
                ORDER BY action_name
                LIMIT ?
                """,
                (procedure_id, related_limit),
            ).fetchall()
        ]

        control_flow = [
            {
                "edge_type": str(row["edge_type"]),
                "target_name": str(row["target_name"]),
            }
            for row in conn.execute(
                """
                SELECT DISTINCT edge_type, target_name
                FROM edges
                WHERE procedure_id = ?
                  AND edge_type IN ('jumps_to_label', 'jumps_to_exit', 'defines_label')
                ORDER BY edge_type, target_name
                LIMIT ?
                """,
                (procedure_id, related_limit),
            ).fetchall()
        ]

        two_hop_outgoing = self._fetch_call_chain_paths(
            conn,
            procedure_name=procedure_name,
            direction="outgoing",
            limit=related_limit,
        )
        two_hop_incoming = self._fetch_call_chain_paths(
            conn,
            procedure_name=procedure_name,
            direction="incoming",
            limit=related_limit,
        )

        related_procedures = self._fetch_related_procedure_summaries(
            conn,
            outgoing_calls=outgoing_calls,
            incoming_callers=incoming_callers,
            related_limit=related_limit,
        )

        return {
            "outgoing_calls": outgoing_calls,
            "incoming_callers": incoming_callers,
            "related_tables": related_tables,
            "related_actions": related_actions,
            "control_flow": control_flow,
            "two_hop_outgoing": two_hop_outgoing,
            "two_hop_incoming": two_hop_incoming,
            "related_procedures": related_procedures,
        }

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
        if procedure_id is not None:
            row = conn.execute(
                "SELECT name, chinese_name FROM procedures WHERE id = ?",
                (procedure_id,),
            ).fetchone()
        elif procedure_name is not None:
            row = conn.execute(
                """
                SELECT name, chinese_name
                FROM procedures
                WHERE name = ? OR chinese_name = ?
                ORDER BY CASE WHEN name = ? THEN 0 ELSE 1 END
                LIMIT 1
                """,
                (procedure_name, procedure_name, procedure_name),
            ).fetchone()
        else:
            row = None

        if row is None:
            return tuple(name for name in [procedure_name] if name)

        aliases = [str(row["name"])]
        if row["chinese_name"]:
            aliases.append(str(row["chinese_name"]))
        return tuple(dict.fromkeys(item for item in aliases if item))

    def _resolve_procedure_name(self, conn: sqlite3.Connection, raw_name: str) -> str:
        aliases = self._procedure_aliases(conn, procedure_name=raw_name)
        if aliases:
            return aliases[0]
        return raw_name

    def _fetch_related_procedure_summaries(
        self,
        conn: sqlite3.Connection,
        *,
        outgoing_calls: list[str],
        incoming_callers: list[str],
        related_limit: int,
    ) -> list[dict[str, object]]:
        related: list[dict[str, object]] = []
        seen: set[tuple[str, str]] = set()

        for relation_type, names in (("calls", outgoing_calls), ("called_by", incoming_callers)):
            for procedure_name in names[:related_limit]:
                info = self._lookup_procedure_summary(conn, procedure_name)
                if info is None:
                    continue
                key = (relation_type, str(info["procedure_name"]))
                if key in seen:
                    continue
                seen.add(key)
                related.append({"relation_type": relation_type, **info})
                if len(related) >= related_limit:
                    return related

        return related

    def _lookup_procedure_summary(
        self,
        conn: sqlite3.Connection,
        procedure_name: str,
    ) -> dict[str, object] | None:
        row = conn.execute(
            """
            SELECT
              p.name AS procedure_name,
              p.chinese_name AS chinese_name,
              f.path AS file_path,
              c.line_start AS line_start,
              c.line_end AS line_end,
              c.chunk_type AS chunk_type,
              c.summary_text AS summary_text
            FROM procedures p
            JOIN files f ON f.id = p.file_id
            LEFT JOIN chunks c ON c.procedure_id = p.id
            WHERE p.name = ? OR p.chinese_name = ?
            ORDER BY CASE WHEN p.name = ? THEN 0 ELSE 1 END, c.seq
            LIMIT 1
            """,
            (procedure_name, procedure_name, procedure_name),
        ).fetchone()
        if row is None:
            return None
        return {
            "procedure_name": str(row["procedure_name"]),
            "chinese_name": str(row["chinese_name"]) if row["chinese_name"] is not None else None,
            "file_path": str(row["file_path"]),
            "line_start": _maybe_int(row["line_start"]),
            "line_end": _maybe_int(row["line_end"]),
            "chunk_type": str(row["chunk_type"]) if row["chunk_type"] is not None else None,
            "summary_text": str(row["summary_text"]) if row["summary_text"] is not None else None,
        }

    def _build_llm_context(self, query: str, evidence_blocks: list[dict[str, object]]) -> str:
        lines = [
            f"Question: {query}",
            "",
            "Use only the following indexed evidence when answering.",
        ]

        for block in evidence_blocks:
            lines.extend(
                [
                    "",
                    f"[Evidence {block['rank']}]",
                    f"Procedure: {block['procedure_name']}",
                    f"File: {block['file_path']}",
                    f"Lines: {block['line_start']}-{block['line_end']}",
                    f"Matched text: {block['matched_text']}",
                    f"Match source: {block['match_source']}",
                    f"Retrieval source: {block['retrieval_source']}",
                    f"Why relevant: {', '.join(block['reasons'])}",
                    "Snippet:",
                    str(block["excerpt"]),
                ]
            )

            related = block["related_context"]
            if block.get("chunk_type"):
                lines.append(f"Chunk type: {block['chunk_type']}")
            if block.get("chunk_summary"):
                lines.append(f"Chunk summary: {block['chunk_summary']}")
            if block.get("block_type"):
                lines.append(f"Recovered block type: {block['block_type']}")
            if block.get("block_summary"):
                lines.append(f"Recovered block summary: {block['block_summary']}")
            if block.get("recovered_blocks"):
                for item in block["recovered_blocks"]:
                    relation_desc = ", ".join(
                        f"{rel['edge_type']}:{rel['target_name']}"
                        for rel in item["relations"]
                    )
                    suffix = f" | {relation_desc}" if relation_desc else ""
                    lines.append(
                        f"Covering block: {item['block_type']} [{item['line_start']}-{item['line_end']}] "
                        f"{item['summary_text']}{suffix}".strip()
                    )
            if related["outgoing_calls"]:
                lines.append(f"Related calls: {', '.join(related['outgoing_calls'])}")
            if related["incoming_callers"]:
                lines.append(f"Incoming callers: {', '.join(related['incoming_callers'])}")
            if related["related_tables"]:
                table_desc = ", ".join(
                    f"{item['edge_type']}:{item['name']}"
                    for item in related["related_tables"]
                )
                lines.append(f"Related tables: {table_desc}")
            if related["related_actions"]:
                lines.append(f"Related actions: {', '.join(related['related_actions'])}")
            if related["control_flow"]:
                flow_desc = ", ".join(
                    f"{item['edge_type']}:{item['target_name']}"
                    for item in related["control_flow"]
                )
                lines.append(f"Control flow: {flow_desc}")
            if related["two_hop_outgoing"]:
                outgoing_desc = ", ".join(
                    f"{item['via_name']} -> {item['procedure_name']}"
                    for item in related["two_hop_outgoing"]
                )
                lines.append(f"Two-hop outgoing chain: {outgoing_desc}")
            if related["two_hop_incoming"]:
                incoming_desc = ", ".join(
                    f"{item['procedure_name']} -> {item['via_name']}"
                    for item in related["two_hop_incoming"]
                )
                lines.append(f"Two-hop incoming chain: {incoming_desc}")
            if related["related_procedures"]:
                for item in related["related_procedures"]:
                    summary_text = item["summary_text"] or ""
                    lines.append(
                        f"Related procedure ({item['relation_type']}): {item['procedure_name']} "
                        f"[{item['line_start']}-{item['line_end']}] {summary_text}".strip()
                    )

        return "\n".join(lines)


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
    if statement.kind == "call" and statement.name:
        return statement.name, "procedure"

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


def _row_to_hit(row: sqlite3.Row) -> dict[str, object]:
    return {
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
        if hit_type in {"chunk", "action", "edge", "statement"} and (
            "call_flow" in combined
            or "calls_procedure" in combined
            or any(str(term) in combined for term in query_analysis["procedure_terms"])
        ):
            bonus += 14.0 if query_analysis["wants_callers"] else 9.0
            reasons.append("intent_call_chain")

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
        "file_path": candidate["file_path"],
        "line_start": candidate["line_start"],
        "line_end": candidate["line_end"],
        "matched_text": candidate["matched_text"],
        "reasons": list(candidate["reasons"]),
        "matched_via": list(candidate.get("matched_via", [])),
    }


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


def _truncate_text(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def _dedupe_strings(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))
