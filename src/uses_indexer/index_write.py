from __future__ import annotations

import json
import sqlite3
from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from .constants import COMPONENT_ACTIONS, EXIT_LABEL_NAMES, READ_ACTIONS, WRITE_ACTIONS
from .embeddings import EmbeddingConfigError, EmbeddingInfo
from .index_utils import embedder_batch_size, json_dumps, maybe_int, paths_match
from .metadata_store import read_metadata, write_metadata_map
from .metadata_semantics import derive_target, metadata_edges_for_statement
from .models import CodeStatement, ParsedUnit
from .semantic_recovery import (
    build_semantic_chunks,
    classify_call_semantics,
    classify_mc_publish,
    collect_block_entities,
    extract_sql_access_edges,
    format_excerpt,
    recover_blocks,
    summarize_block,
    update_string_hints,
)


if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


class IndexWriteService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner

    def insert_unit(self, conn: sqlite3.Connection, unit: ParsedUnit) -> tuple[int, int]:
        attributes_json = json_dumps(unit.attributes)
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
            INSERT INTO procedures_fts(rowid, name, chinese_name, object_id, path)
            VALUES(?, ?, ?, ?, ?)
            """,
            (procedure_id, unit.name, unit.chinese_name or "", unit.object_id or "", unit.path),
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
                    json_dumps(history.extra_attributes),
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
                    json_dumps(param.extra_attributes),
                ),
            )

        return file_id, procedure_id

    def insert_statements(
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
                    json_dumps(statement.groups),
                    json_dumps(statement.arguments),
                    json_dumps(statement.reads),
                    json_dumps(statement.writes),
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

            self.insert_variable_refs(conn, file_id, procedure_id, statement_id, statement, variable_ref_counter)
            inserted_actions = self.insert_action_and_edges(
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
            update_string_hints(string_hints, statement)

        local_chunks, local_vectors = self.insert_chunks(conn, file_id=file_id, procedure_id=procedure_id, unit=unit)
        chunk_counter.update(local_chunks)
        vector_counter.update(local_vectors)
        local_blocks, local_block_edges = self.insert_blocks(
            conn,
            file_id=file_id,
            procedure_id=procedure_id,
            unit=unit,
            statement_ids_by_seq=statement_ids_by_seq,
        )
        block_counter.update(local_blocks)
        block_edge_counter.update(local_block_edges)

        return edge_counter, variable_ref_counter, action_counter, chunk_counter, vector_counter, block_counter, block_edge_counter

    def insert_chunks(
        self,
        conn: sqlite3.Connection,
        *,
        file_id: int,
        procedure_id: int,
        unit: ParsedUnit,
    ) -> tuple[Counter[str], Counter[str]]:
        counter: Counter[str] = Counter()
        vector_counter: Counter[str] = Counter()
        semantic_chunks = build_semantic_chunks(unit.name, unit.statements)
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
                    json_dumps(chunk["anchor_kinds"]),
                    json_dumps(chunk["action_names"]),
                    json_dumps(chunk["target_names"]),
                    json_dumps(chunk["variable_names"]),
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

    def populate_missing_chunk_vectors(self, conn: sqlite3.Connection) -> dict[str, object]:
        self.validate_vector_space_for_population(conn)
        batch_size = embedder_batch_size(self.owner.embedder)
        missing_before = self.missing_chunk_vector_count(conn)
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
            vectors = self.owner.embedder.embed_texts(embedding_inputs)
            embedder_info = self.owner.embedder.info

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
                            json_dumps(vector),
                        ),
                    )
                    provider_counts[embedder_info.provider] += 1
                self.store_embedding_metadata(conn, embedder_info)

            inserted += len(rows)
            batches += 1

        final_info = self.owner.embedder.info
        with conn:
            self.store_embedding_metadata(conn, final_info)

        return {
            "batch_size": batch_size,
            "missing_before": missing_before,
            "inserted": inserted,
            "batches": batches,
            "missing_after": self.missing_chunk_vector_count(conn),
            "provider_counts": dict(provider_counts),
        }

    def validate_resume_source(self, conn: sqlite3.Connection, root: Path) -> None:
        source_root = read_metadata(conn, "source_root")
        if source_root is None:
            raise EmbeddingConfigError("Cannot resume vectors because source_root metadata is missing")
        if not paths_match(source_root, root):
            raise EmbeddingConfigError(f"Cannot resume vectors for {root}; index source_root is {source_root}")

    def validate_vector_space_for_population(self, conn: sqlite3.Connection) -> None:
        current_info = self.owner.embedder.info
        db_provider = read_metadata(conn, "embedding_provider")
        db_model = read_metadata(conn, "embedding_model")
        db_dimension = maybe_int(read_metadata(conn, "embedding_dimension"))

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

    def store_embedding_metadata(self, conn: sqlite3.Connection, info: EmbeddingInfo) -> None:
        dimension = info.dimension
        if dimension == 0:
            dimension = maybe_int(read_metadata(conn, "embedding_dimension")) or 0
        write_metadata_map(
            conn,
            {
                "embedding_provider": info.provider,
                "embedding_model": info.model,
                "embedding_dimension": str(dimension),
            },
        )

    def missing_chunk_vector_count(self, conn: sqlite3.Connection) -> int:
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

    def insert_blocks(
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
        recovered_blocks = recover_blocks(unit.statements)

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
            action_names, target_names, variable_names = collect_block_entities(statements)
            summary_text = summarize_block(
                procedure_name=unit.name,
                block_type=str(block["block_type"]),
                anchor_name=str(block["anchor_name"]),
                statements=statements,
                action_names=action_names,
                target_names=target_names,
            )
            excerpt = format_excerpt(statement_rows)
            table_names = self.fetch_block_table_names(
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
                    json_dumps(action_names),
                    json_dumps(target_names),
                    json_dumps(table_names),
                    json_dumps(variable_names),
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

            for edge in self.fetch_block_edges(
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
                        json_dumps(edge["detail"]),
                    ),
                )
                block_edge_counter[str(edge["edge_type"])] += 1

        return block_counter, block_edge_counter

    def fetch_block_table_names(
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

    def fetch_block_edges(
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

    def insert_variable_refs(
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

    def insert_action_and_edges(
        self,
        conn: sqlite3.Connection,
        *,
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
        action_name = statement.name if statement.kind in {"action", "call", "metadata_item"} else None
        target_name, target_kind = derive_target(statement)

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

        if statement.kind == "metadata_item":
            for metadata_edge in metadata_edges_for_statement(statement):
                self.insert_edge(
                    conn,
                    file_id=file_id,
                    procedure_id=procedure_id,
                    statement_id=statement_id,
                    procedure_name=unit.name,
                    file_path=unit.path,
                    edge_type=str(metadata_edge["edge_type"]),
                    source_name=unit.name,
                    target_name=str(metadata_edge["target_name"]),
                    target_kind=str(metadata_edge["target_kind"]),
                    detail={
                        "metadata_tag": statement.tag,
                        "line_start": statement.line_start,
                        "line_end": statement.line_end,
                        **dict(metadata_edge.get("detail") or {}),
                    },
                )
                edge_counter[str(metadata_edge["edge_type"])] += 1
            return action_counter

        if statement.kind == "call" and statement.name:
            call_detail = {
                "tag": statement.tag,
                "line_start": statement.line_start,
                "line_end": statement.line_end,
                **classify_call_semantics(unit.name, statement.name),
            }
            self.insert_edge(
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
                detail=call_detail,
            )
            edge_counter["calls_procedure"] += 1

        if statement.kind == "action" and statement.name:
            mc_publish_detail = classify_mc_publish(statement)
            self.insert_edge(
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
                if mc_publish_detail is not None:
                    edge_type = "publishes_mc_topic"
                elif statement.name in READ_ACTIONS:
                    edge_type = "reads_table" if target_kind == "table" else "uses_target"
                elif statement.name in WRITE_ACTIONS:
                    edge_type = "writes_table" if target_kind == "table" else "uses_target"
                elif statement.name in COMPONENT_ACTIONS:
                    edge_type = "uses_component"
                else:
                    edge_type = "uses_target"

                self.insert_edge(
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
                    detail={
                        "action_name": statement.name,
                        "tag": statement.tag,
                        **(mc_publish_detail or {}),
                    },
                )
                edge_counter[edge_type] += 1

            for sql_edge in extract_sql_access_edges(statement, string_hints):
                self.insert_edge(
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
                self.insert_edge(
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
            self.insert_edge(
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
                self.insert_edge(
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
            self.insert_edge(
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

    def insert_edge(
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
                json_dumps(detail),
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
