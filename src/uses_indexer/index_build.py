from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from .embeddings import EmbeddingConfigError, EmbeddingInfo
from .metadata_store import read_metadata, write_metadata_map
from .observability import build_incremental_trace
from .models import ParsedUnit
from .parser import is_supported_path
from .semantic_recovery import build_semantic_chunks, recover_blocks


if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


INDEX_STATE_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS indexed_files (
  path TEXT PRIMARY KEY,
  file_size INTEGER NOT NULL,
  mtime_ns INTEGER NOT NULL,
  fingerprint TEXT NOT NULL,
  index_type TEXT NOT NULL,
  code_fingerprint TEXT NOT NULL DEFAULT '',
  unit_signature TEXT NOT NULL DEFAULT ''
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
        write_service = self.owner._index_write_service
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
        self._ensure_index_state_schema(conn)

        files = self._collect_files(root, index_type=index_type)
        initial_embedder_info = self.owner.embedder.info
        parse_cache: dict[str, ParsedUnit] = {}
        parse_stats = {"hits": 0, "misses": 0}

        try:
            with conn:
                self._store_index_metadata(conn, root=root, file_count=len(files), index_type=index_type, embedder_info=initial_embedder_info)
                counters = self._index_files(conn, files, parse_cache=parse_cache, parse_stats=parse_stats)
                self._upsert_indexed_file_state(
                    conn,
                    files,
                    index_type=index_type,
                    parse_cache=parse_cache,
                    parse_stats=parse_stats,
                )

            vector_stats = write_service.populate_missing_chunk_vectors(conn)
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
            build_stats={
                "parsed_unit_count": len(parse_cache),
                "parse_cache_hits": int(parse_stats["hits"]),
                "parse_cache_misses": int(parse_stats["misses"]),
            },
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
        write_service = self.owner._index_write_service
        if not db_file.exists():
            return self.build_index(root, db_file, index_type=index_type)

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        self._ensure_index_state_schema(conn)
        try:
            write_service.validate_resume_source(conn, root)
            existing_index_type = read_metadata(conn, "index_type")
            if existing_index_type and existing_index_type != index_type:
                raise EmbeddingConfigError(
                    f"Cannot run incremental build with index_type={index_type}; existing db was built as {existing_index_type}"
                )

            files = self._collect_files(root, index_type=index_type)
            parse_cache: dict[str, ParsedUnit] = {}
            parse_stats = {"hits": 0, "misses": 0}
            current_state = {str(path): self._fingerprint_path(path) for path in files}
            stored_state = {
                str(row[0]): {
                    "file_size": int(row[1]),
                    "mtime_ns": int(row[2]),
                    "fingerprint": str(row[3]),
                    "code_fingerprint": str(row[4] or ""),
                    "unit_signature": str(row[5] or ""),
                }
                for row in conn.execute(
                    "SELECT path, file_size, mtime_ns, fingerprint, code_fingerprint, unit_signature FROM indexed_files WHERE index_type = ?",
                    (index_type,),
                ).fetchall()
            }

            added_paths = sorted(path for path in current_state if path not in stored_state)
            removed_paths = sorted(path for path in stored_state if path not in current_state)
            changed_paths = sorted(
                path
                for path, fingerprint in current_state.items()
                if path in stored_state and fingerprint["fingerprint"] != stored_state[path]["fingerprint"]
            )

            if not added_paths and not changed_paths and not removed_paths:
                db_summary = self.owner.summarize_db(db_file)
                payload = self._build_summary_payload(
                    db_file=db_file,
                    root=root,
                    index_type=index_type,
                    db_summary=db_summary,
                    vector_stats={
                        "batch_size": 0,
                        "missing_before": 0,
                        "inserted": 0,
                        "batches": 0,
                        "missing_after": 0,
                        "provider_counts": {},
                        "reused": 0,
                        "reuse_candidates": 0,
                        "reused_chunk_count": 0,
                    },
                    counters={
                        "unit_kind": Counter(),
                        "prefix": Counter(),
                        "statement": Counter(),
                        "edge": Counter(),
                        "variable_ref": Counter(),
                        "action": Counter(),
                        "chunk": Counter(),
                        "vector": Counter(),
                        "block": Counter(),
                        "block_edge": Counter(),
                    },
                    incremental=True,
                    build_stats={
                        "parsed_unit_count": 0,
                        "parse_cache_hits": 0,
                        "parse_cache_misses": 0,
                        "metadata_refresh_count": 0,
                    },
                )
                payload["incremental_changes"] = {
                    "added": [],
                    "changed": [],
                    "metadata_only": [],
                    "reindexed": [],
                    "removed": [],
                }
                payload["incremental_execution_plan"] = {
                    "metadata_refresh_count": 0,
                    "metadata_refresh_paths": [],
                    "reindex_paths": [],
                    "remove_paths": [],
                    "noop": True,
                }
                payload["incremental_trace"] = build_incremental_trace(
                    index_type=index_type,
                    current_file_count=len(current_state),
                    stored_file_count=len(stored_state),
                    added_paths=[],
                    changed_paths=[],
                    removed_paths=[],
                    affected_units=[],
                    rebuild_scope={"summary": {"reindexed_procedure_count": 0, "metadata_refresh_count": 0}, "items": []},
                    vector_stats=payload["vector_stats"],
                    elapsed_ms=(time.perf_counter() - started_at) * 1000.0,
                )
                payload["incremental_impact"] = {
                    "affected_unit_count": 0,
                    "affected_units": [],
                }
                payload["incremental_scope"] = {
                    "summary": {
                        "reindexed_procedure_count": 0,
                        "metadata_refresh_count": 0,
                        "removed_procedure_count": 0,
                        "after_statement_count": 0,
                        "after_chunk_count": 0,
                        "after_block_count": 0,
                        "after_vector_target_count": 0,
                        "rebuild_target_statement_count": 0,
                        "rebuild_target_chunk_count": 0,
                        "rebuild_target_block_count": 0,
                        "delta_statement_count": 0,
                        "delta_chunk_count": 0,
                        "delta_block_count": 0,
                        "delta_vector_target_count": 0,
                    },
                    "items": [],
                }
                payload["noop"] = True
                return payload

            metadata_only_paths = sorted(
                path
                for path in changed_paths
                if self._is_metadata_only_change(
                    Path(path),
                    stored_state=stored_state[path],
                    parse_cache=parse_cache,
                    parse_stats=parse_stats,
                )
            )
            rebuild_paths = sorted(path for path in changed_paths if path not in set(metadata_only_paths))
            changed_files = [Path(path) for path in [*added_paths, *rebuild_paths]]
            previous_scope = {
                path: self._describe_index_scope(conn, path)
                for path in [*changed_paths, *removed_paths]
            }
            reusable_vectors = self._collect_reusable_chunk_vectors(conn, rebuild_paths)
            affected_units = self._build_incremental_impact_report(
                conn,
                added_paths=added_paths,
                changed_paths=changed_paths,
                removed_paths=removed_paths,
                metadata_only_paths=metadata_only_paths,
                parse_cache=parse_cache,
                parse_stats=parse_stats,
            )

            with conn:
                for path in [*removed_paths, *rebuild_paths]:
                    self._delete_indexed_path(conn, path)
                counters = self._index_files(conn, changed_files, parse_cache=parse_cache, parse_stats=parse_stats)
                metadata_refresh_count = 0
                for path in metadata_only_paths:
                    unit = self._parse_unit(Path(path), parse_cache=parse_cache, parse_stats=parse_stats)
                    if self.owner._index_write_service.refresh_unit_metadata(conn, path=path, unit=unit):
                        metadata_refresh_count += 1
                reused_vector_stats = self._restore_reusable_chunk_vectors(conn, reusable_vectors)
                self._upsert_indexed_file_state(
                    conn,
                    files,
                    index_type=index_type,
                    parse_cache=parse_cache,
                    parse_stats=parse_stats,
                )
                self._store_index_metadata(conn, root=root, file_count=len(files), index_type=index_type, embedder_info=self.owner.embedder.info)

            vector_stats = write_service.populate_missing_chunk_vectors(conn)
            vector_stats["reused"] = int(reused_vector_stats["reused"])
            vector_stats["reuse_candidates"] = int(reused_vector_stats["reuse_candidates"])
            vector_stats["reused_chunk_count"] = int(reused_vector_stats["reused_chunk_count"])
            current_scope = {
                path: self._describe_index_scope(conn, path)
                for path in [*added_paths, *changed_paths]
            }
            rebuild_scope = self._build_rebuild_scope_report(
                added_paths=added_paths,
                changed_paths=changed_paths,
                removed_paths=removed_paths,
                previous_scope=previous_scope,
                current_scope=current_scope,
                metadata_only_paths=metadata_only_paths,
            )
            db_summary = self.owner.summarize_db(db_file)
            payload = self._build_summary_payload(
                db_file=db_file,
                root=root,
                index_type=index_type,
                db_summary=db_summary,
                vector_stats=vector_stats,
                counters=counters,
                incremental=True,
                build_stats={
                    "parsed_unit_count": len(parse_cache),
                    "parse_cache_hits": int(parse_stats["hits"]),
                    "parse_cache_misses": int(parse_stats["misses"]),
                    "metadata_refresh_count": metadata_refresh_count,
                },
            )
            payload["incremental_changes"] = {
                "added": added_paths,
                "changed": changed_paths,
                "metadata_only": metadata_only_paths,
                "reindexed": rebuild_paths,
                "removed": removed_paths,
            }
            payload["incremental_execution_plan"] = {
                "metadata_refresh_count": metadata_refresh_count,
                "metadata_refresh_paths": metadata_only_paths,
                "reindex_paths": [*added_paths, *rebuild_paths],
                "remove_paths": removed_paths,
            }
            payload["incremental_trace"] = build_incremental_trace(
                index_type=index_type,
                current_file_count=len(current_state),
                stored_file_count=len(stored_state),
                added_paths=added_paths,
                changed_paths=changed_paths,
                removed_paths=removed_paths,
                affected_units=affected_units,
                rebuild_scope=rebuild_scope,
                vector_stats=vector_stats,
                elapsed_ms=(time.perf_counter() - started_at) * 1000.0,
            )
            payload["incremental_impact"] = {
                "affected_unit_count": len(affected_units),
                "affected_units": affected_units,
            }
            payload["incremental_scope"] = rebuild_scope
            return payload
        finally:
            conn.close()
            self.owner._vector_cache.clear()

    def _collect_reusable_chunk_vectors(
        self,
        conn: sqlite3.Connection,
        paths: list[str],
    ) -> dict[str, dict[str, tuple[str, str, int, str]]]:
        if not paths:
            return {}
        db_provider = read_metadata(conn, "embedding_provider")
        db_model = read_metadata(conn, "embedding_model")
        current_info = self.owner.embedder.info
        if db_provider and current_info.provider != db_provider:
            return {}
        if db_model and current_info.model != db_model:
            return {}

        placeholders = ",".join("?" for _ in paths)
        rows = conn.execute(
            f"""
            SELECT
              f.path,
              c.embedding_text,
              cv.provider,
              cv.model,
              cv.dimension,
              cv.vector_json
            FROM files f
            JOIN procedures p ON p.file_id = f.id
            JOIN chunks c ON c.procedure_id = p.id
            JOIN chunk_vectors cv ON cv.chunk_id = c.id
            WHERE f.path IN ({placeholders})
            """,
            paths,
        ).fetchall()
        reusable: dict[str, dict[str, tuple[str, str, int, str]]] = {}
        for path, embedding_text, provider, model, dimension, vector_json in rows:
            normalized_path = str(path)
            normalized_text = str(embedding_text or "").strip()
            if not normalized_text:
                continue
            reusable.setdefault(normalized_path, {}).setdefault(
                normalized_text,
                (str(provider), str(model), int(dimension), str(vector_json)),
            )
        return reusable

    def _restore_reusable_chunk_vectors(
        self,
        conn: sqlite3.Connection,
        reusable_vectors: dict[str, dict[str, tuple[str, str, int, str]]],
    ) -> dict[str, int]:
        if not reusable_vectors:
            return {"reused": 0, "reuse_candidates": 0, "reused_chunk_count": 0}

        reused = 0
        reuse_candidates = sum(len(items) for items in reusable_vectors.values())
        reused_chunk_ids: set[int] = set()

        for path, vector_map in reusable_vectors.items():
            rows = conn.execute(
                """
                SELECT c.id, c.embedding_text
                FROM files f
                JOIN procedures p ON p.file_id = f.id
                JOIN chunks c ON c.procedure_id = p.id
                LEFT JOIN chunk_vectors cv ON cv.chunk_id = c.id
                WHERE f.path = ? AND cv.chunk_id IS NULL
                """,
                (path,),
            ).fetchall()
            for chunk_id, embedding_text in rows:
                normalized_text = str(embedding_text or "").strip()
                if not normalized_text or normalized_text not in vector_map:
                    continue
                provider, model, dimension, vector_json = vector_map[normalized_text]
                conn.execute(
                    """
                    INSERT OR REPLACE INTO chunk_vectors(chunk_id, provider, model, dimension, vector_json)
                    VALUES(?, ?, ?, ?, ?)
                    """,
                    (int(chunk_id), provider, model, dimension, vector_json),
                )
                reused += 1
                reused_chunk_ids.add(int(chunk_id))

        return {
            "reused": reused,
            "reuse_candidates": reuse_candidates,
            "reused_chunk_count": len(reused_chunk_ids),
        }

    def resume_chunk_vectors(self, source_root: str | Path, db_path: str | Path, index_type: str = "all") -> dict[str, object]:
        root = Path(source_root)
        db_file = Path(db_path)
        if not db_file.exists():
            raise FileNotFoundError(f"Cannot resume vectors because database does not exist: {db_file}")

        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys=ON")
        write_service = self.owner._index_write_service
        try:
            write_service.validate_resume_source(conn, root)
            vector_stats = write_service.populate_missing_chunk_vectors(conn)
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

    def _parse_unit(
        self,
        path: Path,
        *,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> ParsedUnit:
        cache_key = str(path)
        cached = parse_cache.get(cache_key)
        if cached is not None:
            parse_stats["hits"] += 1
            return cached
        parse_stats["misses"] += 1
        parsed = self.owner.parser.parse_path(path)
        parse_cache[cache_key] = parsed
        return parsed

    def _ensure_index_state_schema(self, conn: sqlite3.Connection) -> None:
        conn.executescript(INDEX_STATE_SCHEMA_SQL)
        columns = {
            str(row[1])
            for row in conn.execute("PRAGMA table_info(indexed_files)").fetchall()
        }
        if "code_fingerprint" not in columns:
            conn.execute("ALTER TABLE indexed_files ADD COLUMN code_fingerprint TEXT NOT NULL DEFAULT ''")
        if "unit_signature" not in columns:
            conn.execute("ALTER TABLE indexed_files ADD COLUMN unit_signature TEXT NOT NULL DEFAULT ''")

    def _unit_code_fingerprint(self, unit: ParsedUnit) -> str:
        payload = [
            {
                "kind": statement.kind,
                "line_start": statement.line_start,
                "line_end": statement.line_end,
                "raw": statement.raw,
                "tag": statement.tag,
                "name": statement.name,
                "condition": statement.condition,
                "target": statement.target,
                "reads": statement.reads,
                "writes": statement.writes,
            }
            for statement in unit.statements
        ]
        return hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ).hexdigest()

    def _unit_signature(self, unit: ParsedUnit) -> str:
        payload = {
            "file_name": unit.file_name,
            "unit_kind": unit.unit_kind,
            "prefix": unit.prefix,
            "name": unit.name,
        }
        return hashlib.sha256(
            json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ).hexdigest()

    def _build_index_state_record(
        self,
        path: Path,
        *,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> dict[str, object]:
        fingerprint = self._fingerprint_path(path)
        unit = self._parse_unit(path, parse_cache=parse_cache, parse_stats=parse_stats)
        return {
            **fingerprint,
            "code_fingerprint": self._unit_code_fingerprint(unit),
            "unit_signature": self._unit_signature(unit),
        }

    def _is_metadata_only_change(
        self,
        path: Path,
        *,
        stored_state: dict[str, object],
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> bool:
        unit = self._parse_unit(path, parse_cache=parse_cache, parse_stats=parse_stats)
        return (
            self._unit_code_fingerprint(unit) == str(stored_state.get("code_fingerprint") or "")
            and self._unit_signature(unit) == str(stored_state.get("unit_signature") or "")
        )

    def _index_files(
        self,
        conn: sqlite3.Connection,
        files: list[Path],
        *,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> dict[str, Counter[str]]:
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
            unit = self._parse_unit(path, parse_cache=parse_cache, parse_stats=parse_stats)
            file_id, procedure_id = self.owner._index_write_service.insert_unit(conn, unit)
            unit_kind_counter[unit.unit_kind] += 1
            prefix_counter[unit.prefix] += 1
            for statement in unit.statements:
                statement_counter[statement.kind] += 1
            local_edges, local_var_refs, local_actions, local_chunks, local_vectors, local_blocks, local_block_edges = self.owner._index_write_service.insert_statements(
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
        write_metadata_map(
            conn,
            {
                "source_root": str(root),
                "file_count": str(file_count),
                "schema_version": "8",
                "fts_enabled": "true",
                "vector_enabled": "true",
                "index_type": index_type,
            },
        )
        self.owner._index_write_service.store_embedding_metadata(conn, embedder_info)

    def _upsert_indexed_file_state(
        self,
        conn: sqlite3.Connection,
        files: list[Path],
        *,
        index_type: str,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> None:
        conn.execute("DELETE FROM indexed_files WHERE index_type = ?", (index_type,))
        conn.executemany(
            """
            INSERT OR REPLACE INTO indexed_files(path, file_size, mtime_ns, fingerprint, index_type, code_fingerprint, unit_signature)
            VALUES(?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    str(path),
                    state["file_size"],
                    state["mtime_ns"],
                    state["fingerprint"],
                    index_type,
                    state["code_fingerprint"],
                    state["unit_signature"],
                )
                for path in files
                for state in [self._build_index_state_record(path, parse_cache=parse_cache, parse_stats=parse_stats)]
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
        metadata_only_paths: list[str],
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> list[dict[str, object]]:
        affected_units: list[dict[str, object]] = []
        for path in added_paths:
            estimated_scope = self._estimate_source_scope(Path(path), parse_cache=parse_cache, parse_stats=parse_stats)
            affected_units.append(
                {
                    "change_type": "added",
                    **self._describe_source_unit(Path(path), parse_cache=parse_cache, parse_stats=parse_stats),
                    "rebuild_targets": self._scope_to_rebuild_targets(estimated_scope),
                }
            )
        for path in changed_paths:
            estimated_scope = self._estimate_source_scope(Path(path), parse_cache=parse_cache, parse_stats=parse_stats)
            affected_units.append(
                {
                    "change_type": "metadata_only" if path in metadata_only_paths else "changed",
                    **self._describe_indexed_unit(conn, path),
                    "rebuild_targets": self._scope_to_rebuild_targets({} if path in metadata_only_paths else estimated_scope),
                }
            )
        for path in removed_paths:
            indexed_scope = self._describe_index_scope(conn, path)
            affected_units.append(
                {
                    "change_type": "removed",
                    **self._describe_indexed_unit(conn, path),
                    "rebuild_targets": self._scope_to_rebuild_targets(indexed_scope),
                }
            )

        affected_units.sort(
            key=lambda item: (
                str(item.get("change_type") or ""),
                str(item.get("procedure_name") or ""),
                str(item.get("file_path") or ""),
            )
        )
        return affected_units

    def _describe_source_unit(
        self,
        path: Path,
        *,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> dict[str, object]:
        unit = self._parse_unit(path, parse_cache=parse_cache, parse_stats=parse_stats)
        return {
            "file_path": str(path),
            "procedure_name": unit.name,
            "unit_kind": unit.unit_kind,
            "prefix": unit.prefix,
            "chinese_name": unit.chinese_name,
            "object_id": unit.object_id,
        }

    def _estimate_source_scope(
        self,
        path: Path,
        *,
        parse_cache: dict[str, ParsedUnit],
        parse_stats: dict[str, int],
    ) -> dict[str, object]:
        unit = self._parse_unit(path, parse_cache=parse_cache, parse_stats=parse_stats)
        action_count = sum(1 for statement in unit.statements if statement.kind == "action")
        estimated_chunks = build_semantic_chunks(unit.name, unit.statements)
        estimated_blocks = recover_blocks(unit.statements)
        chunk_role_counts = Counter(str(chunk.get("chunk_role") or "general") for chunk in estimated_chunks)
        block_type_counts = Counter(str(block.get("block_type") or "unknown") for block in estimated_blocks)
        feature_flags = {
            "has_calls": any(statement.kind == "call" for statement in unit.statements),
            "has_table_reads": any("获取记录" == statement.name for statement in unit.statements if statement.kind == "action"),
            "has_table_writes": any("通用SQL执行" == statement.name for statement in unit.statements if statement.kind == "action"),
            "has_variable_writes": any(bool(statement.writes) for statement in unit.statements),
            "has_failure_chunks": "failure_flow" in chunk_role_counts,
            "has_call_chain_chunks": "call_chain" in chunk_role_counts,
            "has_table_access_chunks": "table_access" in chunk_role_counts,
        }
        return {
            "file_path": str(path),
            "procedure_name": unit.name,
            "statement_count": len(unit.statements),
            "action_count": action_count,
            "chunk_count": len(estimated_chunks),
            "block_count": len(estimated_blocks),
            "edge_count": 0,
            "vector_target_count": len(estimated_chunks),
            "chunk_role_counts": dict(chunk_role_counts),
            "block_type_counts": dict(block_type_counts),
            "feature_flags": feature_flags,
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

    def _describe_index_scope(self, conn: sqlite3.Connection, path: str) -> dict[str, object]:
        unit = self._describe_indexed_unit(conn, path)
        row = conn.execute(
            """
            SELECT
              COUNT(DISTINCT s.id) AS statement_count,
              COUNT(DISTINCT a.id) AS action_count,
              COUNT(DISTINCT c.id) AS chunk_count,
              COUNT(DISTINCT b.id) AS block_count,
              COUNT(DISTINCT e.id) AS edge_count
            FROM files f
            JOIN procedures p ON p.file_id = f.id
            LEFT JOIN statements s ON s.procedure_id = p.id
            LEFT JOIN actions a ON a.procedure_id = p.id
            LEFT JOIN chunks c ON c.procedure_id = p.id
            LEFT JOIN blocks b ON b.procedure_id = p.id
            LEFT JOIN edges e ON e.procedure_id = p.id
            WHERE f.path = ?
            """,
            (path,),
        ).fetchone()
        counts = {
            "statement_count": int(row[0]) if row and row[0] is not None else 0,
            "action_count": int(row[1]) if row and row[1] is not None else 0,
            "chunk_count": int(row[2]) if row and row[2] is not None else 0,
            "block_count": int(row[3]) if row and row[3] is not None else 0,
            "edge_count": int(row[4]) if row and row[4] is not None else 0,
            "vector_target_count": int(row[2]) if row and row[2] is not None else 0,
        }
        chunk_role_counts = {
            str(role): int(count)
            for role, count in conn.execute(
                """
                SELECT c.chunk_role, COUNT(*)
                FROM files f
                JOIN procedures p ON p.file_id = f.id
                JOIN chunks c ON c.procedure_id = p.id
                WHERE f.path = ?
                GROUP BY c.chunk_role
                ORDER BY c.chunk_role
                """,
                (path,),
            ).fetchall()
        }
        block_type_counts = {
            str(block_type): int(count)
            for block_type, count in conn.execute(
                """
                SELECT b.block_type, COUNT(*)
                FROM files f
                JOIN procedures p ON p.file_id = f.id
                JOIN blocks b ON b.procedure_id = p.id
                WHERE f.path = ?
                GROUP BY b.block_type
                ORDER BY b.block_type
                """,
                (path,),
            ).fetchall()
        }
        feature_flags_row = conn.execute(
            """
            SELECT pf.feature_flags_json
            FROM files f
            JOIN procedures p ON p.file_id = f.id
            JOIN procedure_features pf ON pf.procedure_id = p.id
            WHERE f.path = ?
            LIMIT 1
            """,
            (path,),
        ).fetchone()
        feature_flags = json.loads(str(feature_flags_row[0])) if feature_flags_row and feature_flags_row[0] else {}
        return {
            **unit,
            **counts,
            "chunk_role_counts": chunk_role_counts,
            "block_type_counts": block_type_counts,
            "feature_flags": feature_flags,
        }

    def _scope_to_rebuild_targets(self, scope: dict[str, object]) -> dict[str, int]:
        return {
            "procedure_count": 1 if scope.get("procedure_name") else 0,
            "statement_count": int(scope.get("statement_count") or 0),
            "chunk_count": int(scope.get("chunk_count") or 0),
            "block_count": int(scope.get("block_count") or 0),
            "vector_target_count": int(
                scope.get("vector_target_count")
                or scope.get("chunk_count")
                or 0
            ),
        }

    def _scope_delta(
        self,
        before: dict[str, object] | None,
        after: dict[str, object] | None,
    ) -> dict[str, object]:
        before_scope = before or {}
        after_scope = after or {}

        def delta_int(key: str) -> int:
            return int(after_scope.get(key) or 0) - int(before_scope.get(key) or 0)

        def delta_mapping(key: str) -> dict[str, int]:
            before_map = dict(before_scope.get(key) or {})
            after_map = dict(after_scope.get(key) or {})
            result: dict[str, int] = {}
            for name in sorted(set(before_map) | set(after_map)):
                result[name] = int(after_map.get(name) or 0) - int(before_map.get(name) or 0)
            return result

        def changed_flags() -> dict[str, dict[str, object]]:
            before_flags = dict(before_scope.get("feature_flags") or {})
            after_flags = dict(after_scope.get("feature_flags") or {})
            result: dict[str, dict[str, object]] = {}
            for name in sorted(set(before_flags) | set(after_flags)):
                before_value = before_flags.get(name)
                after_value = after_flags.get(name)
                if before_value != after_value:
                    result[name] = {"before": before_value, "after": after_value}
            return result

        return {
            "statement_count": delta_int("statement_count"),
            "action_count": delta_int("action_count"),
            "chunk_count": delta_int("chunk_count"),
            "block_count": delta_int("block_count"),
            "edge_count": delta_int("edge_count"),
            "vector_target_count": delta_int("vector_target_count"),
            "chunk_role_counts": delta_mapping("chunk_role_counts"),
            "block_type_counts": delta_mapping("block_type_counts"),
            "feature_flags": changed_flags(),
        }

    def _build_rebuild_scope_report(
        self,
        *,
        added_paths: list[str],
        changed_paths: list[str],
        removed_paths: list[str],
        previous_scope: dict[str, dict[str, object]],
        current_scope: dict[str, dict[str, object]],
        metadata_only_paths: list[str],
    ) -> dict[str, object]:
        items: list[dict[str, object]] = []

        for path in added_paths:
            current = dict(current_scope.get(path) or {"file_path": path})
            items.append(
                {
                    "change_type": "added",
                    "file_path": path,
                    "procedure_name": current.get("procedure_name"),
                    "rebuild_targets": self._scope_to_rebuild_targets(current),
                    "before": None,
                    "after": current,
                }
            )

        for path in changed_paths:
            before = dict(previous_scope.get(path) or {"file_path": path})
            after = dict(current_scope.get(path) or {"file_path": path})
            metadata_only = path in metadata_only_paths
            items.append(
                {
                    "change_type": "metadata_only" if metadata_only else "changed",
                    "file_path": path,
                    "procedure_name": after.get("procedure_name") or before.get("procedure_name"),
                    "rebuild_targets": self._scope_to_rebuild_targets({} if metadata_only else (after or before)),
                    "before": before,
                    "after": after,
                    "delta": self._scope_delta(before, after),
                }
            )

        for path in removed_paths:
            before = dict(previous_scope.get(path) or {"file_path": path})
            items.append(
                {
                    "change_type": "removed",
                    "file_path": path,
                    "procedure_name": before.get("procedure_name"),
                    "rebuild_targets": self._scope_to_rebuild_targets(before),
                    "before": before,
                    "after": None,
                    "delta": self._scope_delta(before, None),
                }
            )

        items.sort(
            key=lambda item: (
                str(item.get("change_type") or ""),
                str(item.get("procedure_name") or ""),
                str(item.get("file_path") or ""),
            )
        )

        summary = {
            "reindexed_procedure_count": len([item for item in items if item["change_type"] in {"added", "changed"}]),
            "metadata_refresh_count": len([item for item in items if item["change_type"] == "metadata_only"]),
            "removed_procedure_count": len([item for item in items if item["change_type"] == "removed"]),
            "after_statement_count": sum(int((item.get("after") or {}).get("statement_count") or 0) for item in items),
            "after_chunk_count": sum(int((item.get("after") or {}).get("chunk_count") or 0) for item in items),
            "after_block_count": sum(int((item.get("after") or {}).get("block_count") or 0) for item in items),
            "after_vector_target_count": sum(int((item.get("after") or {}).get("vector_target_count") or 0) for item in items),
            "rebuild_target_statement_count": sum(
                int(((item.get("after") or item.get("before") or {}).get("statement_count") or 0))
                for item in items
            ),
            "rebuild_target_chunk_count": sum(
                int(((item.get("after") or item.get("before") or {}).get("chunk_count") or 0))
                for item in items
            ),
            "rebuild_target_block_count": sum(
                int(((item.get("after") or item.get("before") or {}).get("block_count") or 0))
                for item in items
            ),
            "delta_statement_count": sum(int((item.get("delta") or {}).get("statement_count") or 0) for item in items),
            "delta_chunk_count": sum(int((item.get("delta") or {}).get("chunk_count") or 0) for item in items),
            "delta_block_count": sum(int((item.get("delta") or {}).get("block_count") or 0) for item in items),
            "delta_vector_target_count": sum(int((item.get("delta") or {}).get("vector_target_count") or 0) for item in items),
        }
        return {
            "summary": summary,
            "items": items,
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
        build_stats: dict[str, int] | None = None,
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
            "build_stats": build_stats or {},
        }
        if incremental:
            payload["incremental"] = True
        return payload
