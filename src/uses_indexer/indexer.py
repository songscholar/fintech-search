from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter, defaultdict
from pathlib import Path

from .models import CodeStatement, ParsedUnit
from .parser import SUPPORTED_SUFFIXES, UftDslParser

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
"""

READ_ACTIONS = {"获取记录", "获取字段", "遍历记录开始", "遍历记录池开始", "记录为空", "记录不为空"}
WRITE_ACTIONS = {"插入记录", "修改记录", "清空记录池", "数据回库"}
COMPONENT_ACTIONS = {"获取组件", "插入组件", "尾部插入组件", "遍历组件开始", "遍历组件结束", "组件大小"}
TABLE_WITH_INDEX_RE = re.compile(r"^(?P<table>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<index>[^)]+)\)$")
QUERY_TOKEN_RE = re.compile(r"[\u4e00-\u9fff]+|[A-Za-z0-9_]+")
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


class SQLiteIndexer:
    def __init__(self, parser: UftDslParser | None = None) -> None:
        self.parser = parser or UftDslParser()

    def build_index(self, source_root: str | Path, db_path: str | Path) -> dict[str, object]:
        root = Path(source_root)
        db_file = Path(db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)

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

        with conn:
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("source_root", str(root)))
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("file_count", str(len(files))))
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("schema_version", "3"))
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("fts_enabled", "true"))

            for path in files:
                unit = self.parser.parse_path(path)
                file_id, procedure_id = self._insert_unit(conn, unit)

                unit_kind_counter[unit.unit_kind] += 1
                prefix_counter[unit.prefix] += 1

                for statement in unit.statements:
                    statement_counter[statement.kind] += 1

                local_edges, local_var_refs, local_actions = self._insert_statements(conn, file_id, procedure_id, unit)
                edge_counter.update(local_edges)
                variable_ref_counter.update(local_var_refs)
                action_counter.update(local_actions)

        conn.close()

        return {
            "source_root": str(root),
            "db_path": str(db_file),
            "file_count": len(files),
            "unit_kind_counts": dict(unit_kind_counter),
            "prefix_counts": dict(prefix_counter),
            "statement_counts": dict(statement_counter),
            "edge_counts": dict(edge_counter),
            "variable_ref_counts": dict(variable_ref_counter),
            "fts_counts": {
                "procedures_fts": len(files),
                "statements_fts": sum(statement_counter.values()),
                "actions_fts": sum(action_counter.values()),
                "edges_fts": sum(edge_counter.values()),
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
            "fts_counts": {
                "procedures_fts": scalar("SELECT COUNT(*) FROM procedures_fts"),
                "statements_fts": scalar("SELECT COUNT(*) FROM statements_fts"),
                "actions_fts": scalar("SELECT COUNT(*) FROM actions_fts"),
                "edges_fts": scalar("SELECT COUNT(*) FROM edges_fts"),
            },
            "file_prefix_counts": grouped("SELECT prefix, COUNT(*) FROM files GROUP BY prefix ORDER BY COUNT(*) DESC"),
            "statement_kind_counts": grouped("SELECT kind, COUNT(*) FROM statements GROUP BY kind ORDER BY COUNT(*) DESC"),
            "edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
        }
        conn.close()
        return summary

    def query_index(self, db_path: str | Path, query: str, limit: int = 20) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        candidates, fts_query = self._retrieve_candidates(conn, query, candidate_limit=max(limit * 6, 30))
        conn.close()

        hits = [
            _public_hit(candidate, rank=index)
            for index, candidate in enumerate(candidates[:limit], start=1)
        ]

        return {
            "db_path": str(db_path),
            "query": query,
            "fts_query": fts_query,
            "retrieval_strategy": "fts + sql fallback + python rerank",
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
        candidates, fts_query = self._retrieve_candidates(conn, query, candidate_limit=max(limit * 8, 40))

        evidence_blocks: list[dict[str, object]] = []
        seen_contexts: set[tuple[int, int, int]] = set()
        procedure_counts: defaultdict[int, int] = defaultdict(int)

        for rank, candidate in enumerate(candidates, start=1):
            procedure_id = int(candidate["procedure_id"])
            if procedure_counts[procedure_id] >= 2:
                continue

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
                    "line_start": context["line_start"],
                    "line_end": context["line_end"],
                    "excerpt": context["excerpt"],
                    "context_statements": context["statements"],
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
            "retrieval_strategy": "fts + sql fallback + python rerank + evidence assembly",
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
    ) -> tuple[Counter[str], Counter[str], Counter[str]]:
        edge_counter: Counter[str] = Counter()
        variable_ref_counter: Counter[str] = Counter()
        action_counter: Counter[str] = Counter()

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
            )
            action_counter.update(inserted_actions)

        return edge_counter, variable_ref_counter, action_counter

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
        query: str,
        candidate_limit: int,
    ) -> tuple[list[dict[str, object]], str | None]:
        fts_query = _build_fts_query(query)
        candidates: dict[tuple[object, ...], dict[str, object]] = {}

        if fts_query:
            for candidate in self._run_fts_queries(conn, raw_query=query, fts_query=fts_query, limit=candidate_limit):
                _merge_candidate(candidates, candidate)

        for candidate in self._run_like_queries(conn, query=query, limit=candidate_limit):
            _merge_candidate(candidates, candidate)

        ranked = sorted(
            (
                self._rerank_candidate(candidate, query=query)
                for candidate in candidates.values()
            ),
            key=lambda item: (-float(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0), str(item["matched_text"])),
        )
        return ranked, fts_query

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

        if candidate["hit_type"] == "action":
            score += 4.0
        elif candidate["hit_type"] == "procedure":
            score += 3.0

        score += max(min(float(candidate.get("source_rank") or 0.0), 12.0), -12.0)

        candidate["score"] = round(score, 6)
        candidate["reasons"] = reasons
        return candidate

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

    def _fetch_related_context(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        related_limit: int,
    ) -> dict[str, object]:
        outgoing_calls = [
            str(row["target_name"])
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

        incoming_callers = [
            str(row["source_name"])
            for row in conn.execute(
                """
                SELECT DISTINCT source_name
                FROM edges
                WHERE edge_type = 'calls_procedure' AND target_name = ?
                ORDER BY source_name
                LIMIT ?
                """,
                (procedure_name, related_limit),
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
                WHERE procedure_id = ? AND edge_type IN ('reads_table', 'writes_table')
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

        return {
            "outgoing_calls": outgoing_calls,
            "incoming_callers": incoming_callers,
            "related_tables": related_tables,
            "related_actions": related_actions,
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

        return "\n".join(lines)


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


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
