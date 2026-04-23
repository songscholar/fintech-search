from __future__ import annotations

import json
import sqlite3
from collections import Counter
from pathlib import Path

from .table_parser import TableStructureParser, TableStructure, TableField, TableIndex

TABLE_SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS tables (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  path TEXT NOT NULL UNIQUE,
  file_name TEXT NOT NULL,
  table_name TEXT NOT NULL,
  chinese_name TEXT,
  object_id TEXT,
  space TEXT,
  run_mode TEXT,
  has_history INTEGER NOT NULL DEFAULT 0,
  data_storage_medium TEXT,
  index_space TEXT,
  history_space TEXT,
  history_index_space TEXT,
  archive_space TEXT,
  archive_index_space TEXT
);

CREATE TABLE IF NOT EXISTS table_fields (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  table_id INTEGER NOT NULL,
  field_id TEXT NOT NULL,
  allow_null INTEGER NOT NULL DEFAULT 0,
  uuid TEXT,
  data_type TEXT,
  chinese_name TEXT,
  dictionary_type TEXT,
  description TEXT,
  public_type TEXT,
  comments TEXT,
  FOREIGN KEY(table_id) REFERENCES tables(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS table_indexes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  table_id INTEGER NOT NULL,
  index_name TEXT NOT NULL,
  global_index INTEGER NOT NULL DEFAULT 0,
  flags TEXT,
  index_type_ex TEXT,
  field_names_json TEXT NOT NULL DEFAULT '[]',
  FOREIGN KEY(table_id) REFERENCES tables(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tablespace_relations (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  space TEXT NOT NULL UNIQUE,
  index_space TEXT,
  history_space TEXT,
  history_index_space TEXT,
  archive_space TEXT,
  archive_index_space TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS tables_fts USING fts5(
  table_name,
  chinese_name,
  object_id,
  space,
  index_space,
  history_space,
  archive_space,
  path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS table_fields_fts USING fts5(
  field_id,
  data_type,
  chinese_name,
  dictionary_type,
  description,
  public_type,
  comments,
  table_name,
  path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE VIRTUAL TABLE IF NOT EXISTS table_indexes_fts USING fts5(
  index_name,
  field_names,
  table_name,
  path,
  tokenize='unicode61 remove_diacritics 0'
);

CREATE INDEX IF NOT EXISTS idx_tables_name ON tables(table_name);
CREATE INDEX IF NOT EXISTS idx_tables_space ON tables(space);
CREATE INDEX IF NOT EXISTS idx_table_fields_table_id ON table_fields(table_id);
CREATE INDEX IF NOT EXISTS idx_table_indexes_table_id ON table_indexes(table_id);
"""


class TableIndexer:
    def __init__(self, parser: TableStructureParser | None = None) -> None:
        self.parser = parser or TableStructureParser()

    def build_index(
        self,
        source_root: str | Path,
        db_path: str | Path,
        stdfield_path: str | Path | None = None,
        mdbobject_path: str | Path | None = None,
    ) -> dict:
        root = Path(source_root)
        db_file = Path(db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)

        if db_file.exists():
            db_file.unlink()

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        conn.executescript(TABLE_SCHEMA_SQL)

        resolved_stdfield_path = self._resolve_stdfield_path(root, stdfield_path)
        if resolved_stdfield_path:
            self.parser.load_standard_fields(resolved_stdfield_path)
        if mdbobject_path:
            self.parser.load_tablespace_relations(mdbobject_path)

        tables = sorted(
            path for path in root.rglob("*.uftstructure")
            if path.is_file()
        )

        table_counter: Counter[str] = Counter()
        field_counter: Counter[str] = Counter()
        index_counter: Counter[str] = Counter()

        try:
            with conn:
                conn.execute(
                    "INSERT OR REPLACE INTO tablespace_relations(space, index_space, history_space, history_index_space, archive_space, archive_index_space) VALUES(?, ?, ?, ?, ?, ?)",
                    ("HS_UFT_DATA", "HS_UFT_IDX", "HS_RPT_DATA", "HS_RPT_IDX", "HS_UFT_DATA", "HS_UFT_IDX"),
                )
                conn.execute(
                    "INSERT OR REPLACE INTO tablespace_relations(space, index_space, history_space, history_index_space, archive_space, archive_index_space) VALUES(?, ?, ?, ?, ?, ?)",
                    ("HS_UARG_DATA", "HS_UARG_IDX", "HS_RPT_DATA", "HS_RPT_IDX", "HS_UARG_DATA", "HS_UARG_IDX"),
                )
                conn.execute(
                    "INSERT OR REPLACE INTO tablespace_relations(space, index_space, history_space, history_index_space, archive_space, archive_index_space) VALUES(?, ?, ?, ?, ?, ?)",
                    ("HS_USMS_DATA", "HS_USMS_IDX", "HS_RPT_DATA", "HS_RPT_IDX", "HS_USMS_DATA", "HS_USMS_IDX"),
                )

                for table_path in tables:
                    structure = self.parser.parse_path(table_path)
                    table_id = self._insert_table(conn, structure)

                    table_counter[structure.space or "unknown"] += 1
                    field_counter["total"] += len(structure.fields)
                    index_counter["total"] += len(structure.indexes)

            db_summary = self._summarize_db(conn)
        finally:
            conn.close()

        return {
            "source_root": str(root),
            "db_path": str(db_file),
            "table_count": len(tables),
            "table_space_counts": dict(table_counter),
            "field_count": field_counter["total"],
            "index_count": index_counter["total"],
            "standard_field_count": len(self.parser.standard_fields),
            "db_summary": db_summary,
        }

    def _insert_table(self, conn: sqlite3.Connection, structure: TableStructure) -> int:
        cursor = conn.execute(
            """
            INSERT INTO tables(path, file_name, table_name, chinese_name, object_id, space, run_mode, has_history, 
                              data_storage_medium, index_space, history_space, history_index_space, archive_space, archive_index_space)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                structure.path,
                structure.file_name,
                structure.table_name,
                structure.chinese_name,
                structure.object_id,
                structure.space,
                structure.run_mode,
                1 if structure.has_history else 0,
                structure.data_storage_medium,
                structure.index_space,
                structure.history_space,
                structure.history_index_space,
                structure.archive_space,
                structure.archive_index_space,
            ),
        )
        table_id = int(cursor.lastrowid)

        conn.execute(
            """
            INSERT INTO tables_fts(rowid, table_name, chinese_name, object_id, space, index_space, history_space, archive_space, path)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                table_id,
                structure.table_name,
                structure.chinese_name or "",
                structure.object_id or "",
                structure.space or "",
                structure.index_space or "",
                structure.history_space or "",
                structure.archive_space or "",
                structure.path,
            ),
        )

        for field in structure.fields:
            self._insert_field(conn, table_id, field)

        for idx in structure.indexes:
            self._insert_index(conn, table_id, idx, structure.table_name, structure.path)

        return table_id

    def _insert_field(self, conn: sqlite3.Connection, table_id: int, field: TableField) -> None:
        cursor = conn.execute(
            """
            INSERT INTO table_fields(table_id, field_id, allow_null, uuid, data_type, chinese_name, dictionary_type, description, public_type, comments)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                table_id,
                field.id,
                1 if field.allow_null else 0,
                field.uuid,
                field.data_type,
                field.chinese_name,
                field.dictionary_type,
                field.description,
                field.public_type,
                field.comments,
            ),
        )
        field_id = int(cursor.lastrowid)

        cursor.execute("SELECT table_name, path FROM tables WHERE id = ?", (table_id,))
        row = cursor.fetchone()
        table_name, path = row if row else ("", "")

        conn.execute(
            """
            INSERT INTO table_fields_fts(rowid, field_id, data_type, chinese_name, dictionary_type, description, public_type, comments, table_name, path)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                field_id,
                field.id,
                field.data_type or "",
                field.chinese_name or "",
                field.dictionary_type or "",
                field.description or "",
                field.public_type or "",
                field.comments or "",
                table_name,
                path,
            ),
        )

    def _insert_index(self, conn: sqlite3.Connection, table_id: int, index: TableIndex, table_name: str, path: str) -> None:
        field_names_json = json.dumps(index.fields, ensure_ascii=False)

        cursor = conn.execute(
            """
            INSERT INTO table_indexes(table_id, index_name, global_index, flags, index_type_ex, field_names_json)
            VALUES(?, ?, ?, ?, ?, ?)
            """,
            (
                table_id,
                index.name,
                1 if index.global_index else 0,
                index.flags,
                index.index_type_ex,
                field_names_json,
            ),
        )
        index_id = int(cursor.lastrowid)

        field_names_str = ",".join(index.fields)
        conn.execute(
            """
            INSERT INTO table_indexes_fts(rowid, index_name, field_names, table_name, path)
            VALUES(?, ?, ?, ?, ?)
            """,
            (
                index_id,
                index.name,
                field_names_str,
                table_name,
                path,
            ),
        )

    def _summarize_db(self, conn: sqlite3.Connection) -> dict:
        def scalar(query: str) -> int:
            return int(conn.execute(query).fetchone()[0])

        def grouped(query: str) -> dict:
            rows = conn.execute(query).fetchall()
            return {str(row[0]): int(row[1]) for row in rows}

        return {
            "tables": scalar("SELECT COUNT(*) FROM tables"),
            "table_fields": scalar("SELECT COUNT(*) FROM table_fields"),
            "table_fields_with_chinese_name": scalar("SELECT COUNT(*) FROM table_fields WHERE COALESCE(chinese_name, '') != ''"),
            "table_fields_with_data_type": scalar("SELECT COUNT(*) FROM table_fields WHERE COALESCE(data_type, '') != ''"),
            "table_fields_with_dictionary_type": scalar("SELECT COUNT(*) FROM table_fields WHERE COALESCE(dictionary_type, '') != ''"),
            "table_indexes": scalar("SELECT COUNT(*) FROM table_indexes"),
            "table_space_counts": grouped("SELECT space, COUNT(*) FROM tables GROUP BY space ORDER BY COUNT(*) DESC"),
        }

    def _resolve_stdfield_path(self, source_root: Path, stdfield_path: str | Path | None) -> Path | None:
        candidates: list[Path] = []
        if stdfield_path:
            candidates.append(Path(stdfield_path))
        candidates.extend(
            [
                source_root / "stdfield.stdfield",
                source_root.parent / "metadata" / "stdfield.stdfield",
                source_root.parent / "stdfield.stdfield",
            ]
        )
        candidates.extend(parent / "metadata" / "stdfield.stdfield" for parent in source_root.parents)
        for candidate in candidates:
            if candidate.exists():
                return candidate
        return None

    def query_index(self, db_path: str | Path, query: str, limit: int = 20) -> dict:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row

        results = []
        try:
            cursor = conn.execute(
                """
                SELECT t.*,
                       (SELECT COUNT(*) FROM table_fields WHERE table_id = t.id) as field_count,
                       (SELECT COUNT(*) FROM table_indexes WHERE table_id = t.id) as index_count
                FROM tables t
                JOIN tables_fts fts ON t.id = fts.rowid
                WHERE tables_fts MATCH ?
                ORDER BY rank
                LIMIT ?
                """,
                (query, limit),
            )
            results = [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()

        return {
            "db_path": str(db_path),
            "query": query,
            "hit_count": len(results),
            "hits": results,
        }

    def db_summary(self, db_path: str | Path) -> dict:
        conn = sqlite3.connect(db_path)
        summary = self._summarize_db(conn)
        conn.close()
        return summary
