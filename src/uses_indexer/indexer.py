from __future__ import annotations

import json
import re
import sqlite3
from collections import Counter
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

        with conn:
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("source_root", str(root)))
            conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("file_count", str(len(files))))

            for path in files:
                unit = self.parser.parse_path(path)
                file_id, procedure_id = self._insert_unit(conn, unit)

                unit_kind_counter[unit.unit_kind] += 1
                prefix_counter[unit.prefix] += 1

                for statement in unit.statements:
                    statement_counter[statement.kind] += 1

                local_edges, local_var_refs = self._insert_statements(conn, file_id, procedure_id, unit)
                edge_counter.update(local_edges)
                variable_ref_counter.update(local_var_refs)

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
            "file_prefix_counts": grouped("SELECT prefix, COUNT(*) FROM files GROUP BY prefix ORDER BY COUNT(*) DESC"),
            "statement_kind_counts": grouped("SELECT kind, COUNT(*) FROM statements GROUP BY kind ORDER BY COUNT(*) DESC"),
            "edge_type_counts": grouped("SELECT edge_type, COUNT(*) FROM edges GROUP BY edge_type ORDER BY COUNT(*) DESC"),
        }
        conn.close()
        return summary

    def query_index(self, db_path: str | Path, query: str, limit: int = 20) -> dict[str, object]:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        like = f"%{query}%"

        hits: list[dict[str, object]] = []
        seen: set[tuple[str, str, int | None, str]] = set()

        queries = [
            (
                """
                SELECT
                  'procedure' AS hit_type,
                  100 AS score,
                  p.name AS procedure_name,
                  f.path AS file_path,
                  NULL AS line_start,
                  CASE
                    WHEN p.name LIKE ? THEN p.name
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN COALESCE(p.chinese_name, '')
                    ELSE f.path
                  END AS matched_text,
                  CASE
                    WHEN p.name LIKE ? THEN 'procedure_name'
                    WHEN COALESCE(p.chinese_name, '') LIKE ? THEN 'procedure_chinese_name'
                    ELSE 'file_path'
                  END AS match_source
                FROM procedures p
                JOIN files f ON f.id = p.file_id
                WHERE p.name LIKE ? OR COALESCE(p.chinese_name, '') LIKE ? OR f.path LIKE ?
                ORDER BY score DESC, p.name
                LIMIT ?
                """,
                (like, like, like, like, like, like, like, limit),
            ),
            (
                """
                SELECT
                  'action' AS hit_type,
                  80 AS score,
                  p.name AS procedure_name,
                  f.path AS file_path,
                  s.line_start AS line_start,
                  CASE
                    WHEN COALESCE(a.action_name, '') LIKE ? THEN COALESCE(a.action_name, '')
                    ELSE COALESCE(a.target_name, '')
                  END AS matched_text,
                  CASE
                    WHEN COALESCE(a.action_name, '') LIKE ? THEN 'action_name'
                    ELSE 'action_target'
                  END AS match_source
                FROM actions a
                JOIN procedures p ON p.id = a.procedure_id
                JOIN files f ON f.id = a.file_id
                JOIN statements s ON s.id = a.statement_id
                WHERE COALESCE(a.action_name, '') LIKE ? OR COALESCE(a.target_name, '') LIKE ?
                ORDER BY score DESC, a.action_name
                LIMIT ?
                """,
                (like, like, like, like, limit),
            ),
            (
                """
                SELECT
                  'variable' AS hit_type,
                  60 AS score,
                  p.name AS procedure_name,
                  f.path AS file_path,
                  s.line_start AS line_start,
                  v.var_name AS matched_text,
                  v.access_type AS match_source
                FROM variable_refs v
                JOIN procedures p ON p.id = v.procedure_id
                JOIN files f ON f.id = v.file_id
                JOIN statements s ON s.id = v.statement_id
                WHERE v.var_name LIKE ?
                ORDER BY score DESC, v.var_name
                LIMIT ?
                """,
                (like, limit),
            ),
            (
                """
                SELECT
                  'statement' AS hit_type,
                  50 AS score,
                  p.name AS procedure_name,
                  f.path AS file_path,
                  s.line_start AS line_start,
                  s.raw AS matched_text,
                  s.kind AS match_source
                FROM statements s
                JOIN procedures p ON p.id = s.procedure_id
                JOIN files f ON f.id = s.file_id
                WHERE s.raw LIKE ?
                ORDER BY score DESC, s.line_start
                LIMIT ?
                """,
                (like, limit),
            ),
            (
                """
                SELECT
                  'edge' AS hit_type,
                  40 AS score,
                  p.name AS procedure_name,
                  f.path AS file_path,
                  NULL AS line_start,
                  e.target_name AS matched_text,
                  e.edge_type AS match_source
                FROM edges e
                JOIN procedures p ON p.id = e.procedure_id
                JOIN files f ON f.id = e.file_id
                WHERE e.target_name LIKE ?
                ORDER BY score DESC, e.target_name
                LIMIT ?
                """,
                (like, limit),
            ),
        ]

        for sql, params in queries:
            for row in conn.execute(sql, params).fetchall():
                key = (str(row["hit_type"]), str(row["procedure_name"]), row["line_start"], str(row["matched_text"]))
                if key in seen:
                    continue
                seen.add(key)
                hits.append(
                    {
                        "hit_type": row["hit_type"],
                        "score": row["score"],
                        "procedure_name": row["procedure_name"],
                        "file_path": row["file_path"],
                        "line_start": row["line_start"],
                        "matched_text": row["matched_text"],
                        "match_source": row["match_source"],
                    }
                )

        hits.sort(key=lambda item: (-int(item["score"]), str(item["procedure_name"]), int(item["line_start"] or 0)))
        conn.close()

        return {
            "db_path": str(db_path),
            "query": query,
            "limit": limit,
            "hit_count": min(len(hits), limit),
            "hits": hits[:limit],
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
    ) -> tuple[Counter[str], Counter[str]]:
        edge_counter: Counter[str] = Counter()
        variable_ref_counter: Counter[str] = Counter()

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

            self._insert_variable_refs(conn, file_id, procedure_id, statement_id, statement, variable_ref_counter)
            self._insert_action_and_edges(conn, file_id, procedure_id, statement_id, unit, statement, seq, edge_counter)

        return edge_counter, variable_ref_counter

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
    ) -> None:
        action_name = statement.name if statement.kind in {"action", "call"} else None
        target_name, target_kind = _derive_target(statement)

        if action_name is not None:
            conn.execute(
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

        if statement.kind == "call" and statement.name:
            self._insert_edge(
                conn,
                file_id=file_id,
                procedure_id=procedure_id,
                statement_id=statement_id,
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
                    edge_type="writes_variable",
                    source_name=unit.name,
                    target_name=target,
                    target_kind="variable",
                    detail={"line_start": statement.line_start, "line_end": statement.line_end},
                )
                edge_counter["writes_variable"] += 1

    def _insert_edge(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        statement_id: int | None,
        edge_type: str,
        source_name: str,
        target_name: str,
        target_kind: str,
        detail: dict[str, object],
    ) -> None:
        conn.execute(
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


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
