from __future__ import annotations

import hashlib
import sqlite3
import time
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from .embeddings import EmbeddingConfigError, EmbeddingInfo
from .observability import build_incremental_trace
from .parser import is_supported_path


if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


INDEX_STATE_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS indexed_files (
  path TEXT PRIMARY KEY,
  file_size INTEGER NOT NULL,
  mtime_ns INTEGER NOT NULL,
  fingerprint TEXT NOT NULL,
  index_type TEXT NOT NULL
);
"""


class IndexBuildService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner

    def build_index(
        self,
        source_root: str | Path,
        db_path: str | Path,
        *,
        resume_vectors: bool = False,
        incremental: bool = False,
        index_type: str = "all",
    ) -> dict[str, object]:
        started_at = time.perf_counter()
        root = Path(source_root)
        db_file = Path(db_path)
        db_file.parent.mkdir(parents=True, exist_ok=True)

        if resume_vectors:
            return self.resume_chunk_vectors(root, db_file, index_type=index_type)
        if incremental:
            return self.incremental_build_index(root, db_file, index_type=index_type)

        if db_file.exists():
            db_file.unlink()

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        conn.executescript(self.owner.SCHEMA_SQL)
        conn.executescript(INDEX_STATE_SCHEMA_SQL)

        files = self._collect_files(root, index_type=index_type)
        initial_embedder_info = self.owner.embedder.info

        try:
            with conn:
                self._store_index_metadata(conn, root=root, file_count=len(files), index_type=index_type, embedder_info=initial_embedder_info)
                counters = self._index_files(conn, files)
                self._upsert_indexed_file_state(conn, files, index_type=index_type)

            vector_stats = self.owner._populate_missing_chunk_vectors(conn)
        finally:
            conn.close()
        self.owner._vector_cache.clear()

        db_summary = self.owner.summarize_db(db_file)
        return self._build_summary_payload(
            db_file=db_file,
            root=root,
            index_type=index_type,
            db_summary=db_summary,
            vector_stats=vector_stats,
            counters=counters,
            incremental=False,
        )

    def incremental_build_index(
        self,
        source_root: str | Path,
        db_path: str | Path,
        *,
        index_type: str = "all",
    ) -> dict[str, object]:
        started_at = time.perf_counter()
        root = Path(source_root)
        db_file = Path(db_path)
        if not db_file.exists():
            return self.build_index(root, db_file, index_type=index_type)

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        conn.executescript(INDEX_STATE_SCHEMA_SQL)
        try:
            self.owner._validate_resume_source(conn, root)
            existing_index_type = self.owner._metadata(conn, "index_type")
            if existing_index_type and existing_index_type != index_type:
                raise EmbeddingConfigError(
                    f"Cannot run incremental build with index_type={index_type}; existing db was built as {existing_index_type}"
                )

            files = self._collect_files(root, index_type=index_type)
            current_state = {str(path): self._fingerprint_path(path) for path in files}
            stored_state = {
                str(row[0]): {
                    "file_size": int(row[1]),
                    "mtime_ns": int(row[2]),
                    "fingerprint": str(row[3]),
                }
                for row in conn.execute(
                    "SELECT path, file_size, mtime_ns, fingerprint FROM indexed_files WHERE index_type = ?",
                    (index_type,),
                ).fetchall()
            }

            added_paths = sorted(path for path in current_state if path not in stored_state)
            removed_paths = sorted(path for path in stored_state if path not in current_state)
            changed_paths = sorted(
                path
                for path, fingerprint in current_state.items()
                if path in stored_state and fingerprint != stored_state[path]
            )

            changed_files = [Path(path) for path in [*added_paths, *changed_paths]]
            affected_units = self._build_incremental_impact_report(
                conn,
                added_paths=added_paths,
                changed_paths=changed_paths,
                removed_paths=removed_paths,
            )

            with conn:
                for path in [*removed_paths, *changed_paths]:
                    self._delete_indexed_path(conn, path)
                counters = self._index_files(conn, changed_files)
                self._upsert_indexed_file_state(conn, files, index_type=index_type)
                self._store_index_metadata(conn, root=root, file_count=len(files), index_type=index_type, embedder_info=self.owner.embedder.info)

            vector_stats = self.owner._populate_missing_chunk_vectors(conn)
            db_summary = self.owner.summarize_db(db_file)
            payload = self._build_summary_payload(
                db_file=db_file,
                root=root,
                index_type=index_type,
                db_summary=db_summary,
                vector_stats=vector_stats,
                counters=counters,
                incremental=True,
            )
            payload["incremental_changes"] = {
                "added": added_paths,
                "changed": changed_paths,
                "removed": removed_paths,
            }
            payload["incremental_trace"] = build_incremental_trace(
                index_type=index_type,
                current_file_count=len(current_state),
                stored_file_count=len(stored_state),
                added_paths=added_paths,
                changed_paths=changed_paths,
                removed_paths=removed_paths,
                affected_units=affected_units,
                vector_stats=vector_stats,
                elapsed_ms=(time.perf_counter() - started_at) * 1000.0,
            )
            payload["incremental_impact"] = {
                "affected_unit_count": len(affected_units),
                "affected_units": affected_units,
            }
            return payload
        finally:
            conn.close()
            self.owner._vector_cache.clear()

    def resume_chunk_vectors(self, source_root: str | Path, db_path: str | Path, index_type: str = "all") -> dict[str, object]:
        root = Path(source_root)
        db_file = Path(db_path)
        if not db_file.exists():
            raise FileNotFoundError(f"Cannot resume vectors because database does not exist: {db_file}")

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        try:
            self.owner._validate_resume_source(conn, root)
            vector_stats = self.owner._populate_missing_chunk_vectors(conn)
        finally:
            conn.close()
        self.owner._vector_cache.clear()

        db_summary = self.owner.summarize_db(db_file)
        return {
            "source_root": str(root),
            "db_path": str(db_file),
            "resume_vectors": True,
            "index_type": index_type,
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

    def _collect_files(self, root: Path, *, index_type: str) -> list[Path]:
        def is_metadata_path(path: Path) -> bool:
            return "metadata" in str(path).lower() and path.suffix not in (".uftfunction", ".uftservice", ".uftatomfunction", ".uftfactorservice", ".extinterface")

        def is_code_path(path: Path) -> bool:
            return path.suffix in (".uftfunction", ".uftservice", ".uftatomfunction", ".uftfactorservice", ".extinterface") and "metadata" not in str(path).lower()

        return sorted(
            path for path in root.rglob("*")
            if path.is_file() and is_supported_path(path) and (
                index_type == "all" or
                (index_type == "metadata" and is_metadata_path(path)) or
                (index_type == "code" and is_code_path(path))
            ) and not any(excluded in str(path) for excluded in ["通用数据", "commondata", "tools"])
        )

    def _index_files(self, conn: sqlite3.Connection, files: list[Path]) -> dict[str, Counter[str]]:
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

        for path in files:
            unit = self.owner.parser.parse_path(path)
            file_id, procedure_id = self.owner._insert_unit(conn, unit)
            unit_kind_counter[unit.unit_kind] += 1
            prefix_counter[unit.prefix] += 1
            for statement in unit.statements:
                statement_counter[statement.kind] += 1
            local_edges, local_var_refs, local_actions, local_chunks, local_vectors, local_blocks, local_block_edges = self.owner._insert_statements(
                conn,
                file_id,
                procedure_id,
                unit,
            )
            edge_counter.update(local_edges)
            variable_ref_counter.update(local_var_refs)
            action_counter.update(local_actions)
            chunk_counter.update(local_chunks)
            vector_counter.update(local_vectors)
            block_counter.update(local_blocks)
            block_edge_counter.update(local_block_edges)

        return {
            "unit_kind": unit_kind_counter,
            "prefix": prefix_counter,
            "statement": statement_counter,
            "edge": edge_counter,
            "variable_ref": variable_ref_counter,
            "action": action_counter,
            "chunk": chunk_counter,
            "vector": vector_counter,
            "block": block_counter,
            "block_edge": block_edge_counter,
        }

    def _store_index_metadata(
        self,
        conn: sqlite3.Connection,
        *,
        root: Path,
        file_count: int,
        index_type: str,
        embedder_info: EmbeddingInfo,
    ) -> None:
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("source_root", str(root)))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("file_count", str(file_count)))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("schema_version", "8"))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("fts_enabled", "true"))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("vector_enabled", "true"))
        conn.execute("INSERT OR REPLACE INTO metadata(key, value) VALUES(?, ?)", ("index_type", index_type))
        self.owner._store_embedding_metadata(conn, embedder_info)

    def _upsert_indexed_file_state(self, conn: sqlite3.Connection, files: list[Path], *, index_type: str) -> None:
        conn.execute("DELETE FROM indexed_files WHERE index_type = ?", (index_type,))
        conn.executemany(
            """
            INSERT OR REPLACE INTO indexed_files(path, file_size, mtime_ns, fingerprint, index_type)
            VALUES(?, ?, ?, ?, ?)
            """,
            [
                (
                    str(path),
                    fingerprint["file_size"],
                    fingerprint["mtime_ns"],
                    fingerprint["fingerprint"],
                    index_type,
                )
                for path in files
                for fingerprint in [self._fingerprint_path(path)]
            ],
        )

    def _fingerprint_path(self, path: Path) -> dict[str, object]:
        stat = path.stat()
        raw = f"{path}:{stat.st_size}:{stat.st_mtime_ns}".encode("utf-8")
        return {
            "file_size": int(stat.st_size),
            "mtime_ns": int(stat.st_mtime_ns),
            "fingerprint": hashlib.sha256(raw).hexdigest(),
        }

    def _delete_indexed_path(self, conn: sqlite3.Connection, path: str) -> None:
        file_row = conn.execute(
            "SELECT id FROM files WHERE path = ?",
            (path,),
        ).fetchone()
        if file_row is None:
            conn.execute("DELETE FROM indexed_files WHERE path = ?", (path,))
            return

        file_id = int(file_row[0])
        procedure_ids = [int(row[0]) for row in conn.execute("SELECT id FROM procedures WHERE file_id = ?", (file_id,)).fetchall()]
        statement_ids = [int(row[0]) for row in conn.execute("SELECT id FROM statements WHERE file_id = ?", (file_id,)).fetchall()]
        action_ids = [int(row[0]) for row in conn.execute("SELECT id FROM actions WHERE file_id = ?", (file_id,)).fetchall()]
        edge_ids = [int(row[0]) for row in conn.execute("SELECT id FROM edges WHERE file_id = ?", (file_id,)).fetchall()]
        chunk_ids = [int(row[0]) for row in conn.execute("SELECT id FROM chunks WHERE file_id = ?", (file_id,)).fetchall()]
        block_ids = [int(row[0]) for row in conn.execute("SELECT id FROM blocks WHERE file_id = ?", (file_id,)).fetchall()]

        self._delete_fts_rows(conn, "procedures_fts", procedure_ids)
        self._delete_fts_rows(conn, "statements_fts", statement_ids)
        self._delete_fts_rows(conn, "actions_fts", action_ids)
        self._delete_fts_rows(conn, "edges_fts", edge_ids)
        self._delete_fts_rows(conn, "chunks_fts", chunk_ids)
        self._delete_fts_rows(conn, "blocks_fts", block_ids)

        conn.execute("DELETE FROM files WHERE id = ?", (file_id,))
        conn.execute("DELETE FROM indexed_files WHERE path = ?", (path,))

    def _delete_fts_rows(self, conn: sqlite3.Connection, table: str, row_ids: list[int]) -> None:
        if not row_ids:
            return
        placeholders = ",".join("?" for _ in row_ids)
        conn.execute(
            f"DELETE FROM {table} WHERE rowid IN ({placeholders})",
            row_ids,
        )

    def _build_incremental_impact_report(
        self,
        conn: sqlite3.Connection,
        *,
        added_paths: list[str],
        changed_paths: list[str],
        removed_paths: list[str],
    ) -> list[dict[str, object]]:
        affected_units: list[dict[str, object]] = []
        for path in added_paths:
            affected_units.append({"change_type": "added", **self._describe_source_unit(Path(path))})
        for path in changed_paths:
            affected_units.append({"change_type": "changed", **self._describe_indexed_unit(conn, path)})
        for path in removed_paths:
            affected_units.append({"change_type": "removed", **self._describe_indexed_unit(conn, path)})

        affected_units.sort(
            key=lambda item: (
                str(item.get("change_type") or ""),
                str(item.get("procedure_name") or ""),
                str(item.get("file_path") or ""),
            )
        )
        return affected_units

    def _describe_source_unit(self, path: Path) -> dict[str, object]:
        unit = self.owner.parser.parse_path(path)
        return {
            "file_path": str(path),
            "procedure_name": unit.name,
            "unit_kind": unit.unit_kind,
            "prefix": unit.prefix,
            "chinese_name": unit.chinese_name,
            "object_id": unit.object_id,
        }

    def _describe_indexed_unit(self, conn: sqlite3.Connection, path: str) -> dict[str, object]:
        row = conn.execute(
            """
            SELECT
              f.path,
              f.unit_kind,
              f.prefix,
              p.name,
              p.chinese_name,
              p.object_id
            FROM files f
            JOIN procedures p ON p.file_id = f.id
            WHERE f.path = ?
            LIMIT 1
            """,
            (path,),
        ).fetchone()
        if row is None:
            return {
                "file_path": path,
                "procedure_name": None,
                "unit_kind": None,
                "prefix": None,
                "chinese_name": None,
                "object_id": None,
            }
        return {
            "file_path": str(row[0]),
            "unit_kind": str(row[1]) if row[1] is not None else None,
            "prefix": str(row[2]) if row[2] is not None else None,
            "procedure_name": str(row[3]) if row[3] is not None else None,
            "chinese_name": str(row[4]) if row[4] is not None else None,
            "object_id": str(row[5]) if row[5] is not None else None,
        }

    def _build_summary_payload(
        self,
        *,
        db_file: Path,
        root: Path,
        index_type: str,
        db_summary: dict[str, object],
        vector_stats: dict[str, object],
        counters: dict[str, Counter[str]],
        incremental: bool,
    ) -> dict[str, object]:
        payload = {
            "source_root": str(root),
            "db_path": str(db_file),
            "index_type": index_type,
            "file_count": int(db_summary["files"]),
            "unit_kind_counts": db_summary["unit_kind_counts"],
            "prefix_counts": db_summary["file_prefix_counts"],
            "statement_counts": db_summary["statement_kind_counts"],
            "edge_counts": db_summary["edge_type_counts"],
            "variable_ref_counts": db_summary["variable_ref_type_counts"],
            "action_counts": dict(counters["action"]),
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
        if incremental:
            payload["incremental"] = True
        return payload
