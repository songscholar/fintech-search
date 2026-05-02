from __future__ import annotations

import sqlite3
from collections import deque
from typing import TYPE_CHECKING

from .index_utils import json_loads_object
from .semantic_recovery import coerce_call_semantics, format_excerpt, maybe_int


if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


class ContextFetchService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner
        self._call_graph: dict[str, dict[str, set[str]]] | None = None

    def preload_call_graph(self, conn: sqlite3.Connection) -> None:
        """一次性加载全部 calls_procedure edges 到内存邻接表，避免逐 procedure SQL 查询。"""
        if self._call_graph is not None:
            return
        outgoing: dict[str, set[str]] = {}
        incoming: dict[str, set[str]] = {}
        for row in conn.execute(
            "SELECT source_name, target_name FROM edges WHERE edge_type = 'calls_procedure'"
        ):
            source = str(row[0])
            target = str(row[1])
            outgoing.setdefault(source, set()).add(target)
            incoming.setdefault(target, set()).add(source)
        self._call_graph = {"outgoing": outgoing, "incoming": incoming}

    def _procedure_call_neighbors_fast(
        self,
        procedure_name: str,
        max_depth: int = 10,
    ) -> tuple[dict[int, set[str]], dict[int, set[str]]]:
        """基于内存邻接表的 BFS，零 SQL 开销。"""
        outgoing_map: dict[str, set[str]] = self._call_graph["outgoing"]
        incoming_map: dict[str, set[str]] = self._call_graph["incoming"]

        outgoing_hops: dict[int, set[str]] = {1: set()}
        incoming_hops: dict[int, set[str]] = {1: set()}

        outgoing_hops[1] = outgoing_map.get(procedure_name, set()).copy()
        incoming_hops[1] = incoming_map.get(procedure_name, set()).copy()

        visited: set[str] = {procedure_name}
        visited.update(outgoing_hops[1])
        visited.update(incoming_hops[1])
        current_outgoing = outgoing_hops[1].copy()
        current_incoming = incoming_hops[1].copy()

        for depth in range(2, max_depth + 1):
            next_outgoing: set[str] = set()
            next_incoming: set[str] = set()

            for neighbor_name in current_outgoing:
                if neighbor_name in visited:
                    continue
                next_outgoing.update(outgoing_map.get(neighbor_name, set()) - visited)

            for neighbor_name in current_incoming:
                if neighbor_name in visited:
                    continue
                next_incoming.update(incoming_map.get(neighbor_name, set()) - visited)

            visited.update(next_outgoing)
            visited.update(next_incoming)
            if next_outgoing:
                outgoing_hops[depth] = next_outgoing
            if next_incoming:
                incoming_hops[depth] = next_incoming
            current_outgoing = next_outgoing
            current_incoming = next_incoming
            if not current_outgoing and not current_incoming:
                break

        return outgoing_hops, incoming_hops

    def procedure_call_neighbors(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_name: str,
        max_depth: int = 10,
    ) -> tuple[dict[int, set[str]], dict[int, set[str]]]:
        if self._call_graph is not None:
            return self._procedure_call_neighbors_fast(procedure_name, max_depth)

        outgoing_hops: dict[int, set[str]] = {1: set()}
        incoming_hops: dict[int, set[str]] = {1: set()}

        outgoing_hops[1] = {
            self.resolve_procedure_name(conn, str(row[0]))
            for row in conn.execute(
                """
                SELECT DISTINCT target_name
                FROM edges
                WHERE source_name = ? AND edge_type = 'calls_procedure'
                """,
                (procedure_name,),
            ).fetchall()
        }

        aliases = self.procedure_aliases(conn, procedure_name=procedure_name)
        incoming_hops[1] = {
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

        visited: set[str] = {procedure_name}
        visited.update(outgoing_hops[1])
        visited.update(incoming_hops[1])
        current_outgoing = outgoing_hops[1].copy()
        current_incoming = incoming_hops[1].copy()

        for depth in range(2, max_depth + 1):
            next_outgoing: set[str] = set()
            next_incoming: set[str] = set()

            for neighbor_name in current_outgoing:
                if neighbor_name in visited:
                    continue
                next_level_out = {
                    self.resolve_procedure_name(conn, str(row[0]))
                    for row in conn.execute(
                        """
                        SELECT DISTINCT target_name
                        FROM edges
                        WHERE source_name = ? AND edge_type = 'calls_procedure'
                        """,
                        (neighbor_name,),
                    ).fetchall()
                }
                next_outgoing.update(next_level_out - visited)

            for neighbor_name in current_incoming:
                if neighbor_name in visited:
                    continue
                neighbor_aliases = self.procedure_aliases(conn, procedure_name=neighbor_name)
                next_level_in = {
                    str(row[0])
                    for row in conn.execute(
                        f"""
                        SELECT DISTINCT source_name
                        FROM edges
                        WHERE target_name IN ({",".join("?" for _ in neighbor_aliases)}) AND edge_type = 'calls_procedure'
                        """,
                        neighbor_aliases,
                    ).fetchall()
                }
                next_incoming.update(next_level_in - visited)

            visited.update(next_outgoing)
            visited.update(next_incoming)
            if next_outgoing:
                outgoing_hops[depth] = next_outgoing
            if next_incoming:
                incoming_hops[depth] = next_incoming
            current_outgoing = next_outgoing
            current_incoming = next_incoming
            if not current_outgoing and not current_incoming:
                break

        return outgoing_hops, incoming_hops

    def fetch_context_block(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        statement_id: int | None,
        context_window: int,
    ) -> dict[str, object]:
        if statement_id is not None:
            anchor = conn.execute("SELECT seq FROM statements WHERE id = ?", (statement_id,)).fetchone()
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

        statements = [_statement_row(row) for row in rows]
        return {
            "line_start": min((item["line_start"] for item in statements), default=0),
            "line_end": max((item["line_end"] for item in statements), default=0),
            "statements": statements,
            "excerpt": format_excerpt(statements),
        }

    def fetch_chunk_block(
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
        statements = [_statement_row(row) for row in rows]
        return {
            "chunk_type": str(chunk_row["chunk_type"]),
            "summary_text": str(chunk_row["summary_text"]),
            "line_start": int(chunk_row["line_start"]),
            "line_end": int(chunk_row["line_end"]),
            "statements": statements,
            "excerpt": format_excerpt(statements),
        }

    def fetch_block_context(
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
        statements = [_statement_row(row) for row in rows]
        return {
            "block_type": str(block_row["block_type"]),
            "block_summary": str(block_row["summary_text"]),
            "line_start": int(block_row["line_start"]),
            "line_end": int(block_row["line_end"]),
            "statements": statements,
            "excerpt": format_excerpt(statements),
        }

    def fetch_covering_blocks(
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

        return [
            {
                "block_type": str(row["block_type"]),
                "anchor_name": str(row["anchor_name"]),
                "line_start": int(row["line_start"]),
                "line_end": int(row["line_end"]),
                "summary_text": str(row["summary_text"]),
                "relations": self.fetch_block_relation_summary(conn, block_id=int(row["id"]), limit=4),
            }
            for row in rows
        ]

    def fetch_block_relation_summary(
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

    def fetch_related_context(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        related_limit: int,
    ) -> dict[str, object]:
        aliases = self.procedure_aliases(conn, procedure_id=procedure_id, procedure_name=procedure_name)
        outgoing_call_edges = self.fetch_related_call_edges(
            conn,
            procedure_id=procedure_id,
            procedure_name=procedure_name,
            aliases=aliases,
            direction="outgoing",
            limit=related_limit,
        )
        outgoing_calls = [str(item["procedure_name"]) for item in outgoing_call_edges]
        incoming_caller_edges = self.fetch_related_call_edges(
            conn,
            procedure_id=procedure_id,
            procedure_name=procedure_name,
            aliases=aliases,
            direction="incoming",
            limit=related_limit,
        )
        incoming_callers = [str(item["procedure_name"]) for item in incoming_caller_edges]

        related_tables = [
            {"name": str(row["target_name"]), "edge_type": str(row["edge_type"])}
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
            {"edge_type": str(row["edge_type"]), "target_name": str(row["target_name"])}
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

        outgoing_hops, incoming_hops = self.procedure_call_neighbors(conn, procedure_name=procedure_name, max_depth=5)
        multi_hop_outgoing: list[dict[str, object]] = []
        multi_hop_incoming: list[dict[str, object]] = []
        for depth in range(2, 6):
            for proc_name in list(outgoing_hops.get(depth, set()))[:related_limit]:
                summary = self.lookup_procedure_summary(conn, proc_name)
                if summary:
                    summary["hop_depth"] = depth
                    summary["direction"] = "outgoing"
                    multi_hop_outgoing.append(summary)
            for proc_name in list(incoming_hops.get(depth, set()))[:related_limit]:
                summary = self.lookup_procedure_summary(conn, proc_name)
                if summary:
                    summary["hop_depth"] = depth
                    summary["direction"] = "incoming"
                    multi_hop_incoming.append(summary)

        return {
            "outgoing_calls": outgoing_calls,
            "incoming_callers": incoming_callers,
            "outgoing_call_edges": outgoing_call_edges,
            "incoming_caller_edges": incoming_caller_edges,
            "published_mc_topics": self.fetch_related_mc_topics(conn, procedure_id=procedure_id, limit=related_limit),
            "metadata_relations": self.fetch_related_metadata_relations(conn, procedure_id=procedure_id, limit=related_limit),
            "related_tables": related_tables,
            "related_actions": related_actions,
            "control_flow": control_flow,
            "multi_hop_outgoing": multi_hop_outgoing,
            "multi_hop_incoming": multi_hop_incoming,
            "related_procedures": self.fetch_related_procedure_summaries(
                conn,
                outgoing_calls=outgoing_calls,
                incoming_callers=incoming_callers,
                related_limit=related_limit,
            ),
        }

    def fetch_related_metadata_relations(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        rows = conn.execute(
            """
            SELECT DISTINCT edge_type, target_name, target_kind
            FROM edges
            WHERE procedure_id = ?
              AND (
                edge_type LIKE 'defines_%'
                OR edge_type LIKE 'references_%'
                OR edge_type LIKE 'maps_%'
                OR edge_type LIKE 'contains_%'
                OR edge_type IN ('uses_datatype', 'uses_default_value', 'uses_standard_type', 'topic_filter_field')
              )
            ORDER BY edge_type, target_name
            LIMIT ?
            """,
            (procedure_id, limit),
        ).fetchall()
        return [
            {
                "edge_type": str(row["edge_type"]),
                "target_name": str(row["target_name"]),
                "target_kind": str(row["target_kind"]),
            }
            for row in rows
        ]

    def fetch_related_mc_topics(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        limit: int,
    ) -> list[dict[str, object]]:
        rows = conn.execute(
            """
            SELECT DISTINCT target_name, detail_json
            FROM edges
            WHERE procedure_id = ? AND edge_type = 'publishes_mc_topic'
            ORDER BY target_name
            LIMIT ?
            """,
            (procedure_id, limit),
        ).fetchall()
        topics: list[dict[str, object]] = []
        seen_names: set[str] = set()
        for row in rows:
            topic_name = str(row["target_name"])
            if topic_name in seen_names:
                continue
            seen_names.add(topic_name)
            detail = json_loads_object(str(row["detail_json"]))
            topics.append(
                {
                    "topic_name": topic_name,
                    "publish_mode": str(detail.get("publish_mode") or "unknown"),
                    "publish_mode_label": str(detail.get("publish_mode_label") or "未知发布方式"),
                    "message_label": str(detail.get("message_label") or "消息中心主题发布"),
                    "communication_label": str(detail.get("communication_label") or "跨核心消息发布"),
                }
            )
        return topics

    def fetch_related_call_edges(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int,
        procedure_name: str,
        aliases: tuple[str, ...],
        direction: str,
        limit: int,
    ) -> list[dict[str, object]]:
        if direction == "outgoing":
            rows = conn.execute(
                """
                SELECT DISTINCT target_name, detail_json
                FROM edges
                WHERE procedure_id = ? AND edge_type = 'calls_procedure'
                ORDER BY target_name
                LIMIT ?
                """,
                (procedure_id, limit),
            ).fetchall()
            items: list[dict[str, object]] = []
            seen_names: set[str] = set()
            for row in rows:
                target_name = self.resolve_procedure_name(conn, str(row["target_name"]))
                if target_name in seen_names:
                    continue
                seen_names.add(target_name)
                detail = json_loads_object(str(row["detail_json"]))
                semantic = coerce_call_semantics(detail, source_name=procedure_name, target_name=target_name)
                items.append({"procedure_name": target_name, **semantic})
            return items

        rows = conn.execute(
            f"""
            SELECT DISTINCT source_name, detail_json
            FROM edges
            WHERE edge_type = 'calls_procedure' AND target_name IN ({",".join("?" for _ in aliases)})
            ORDER BY source_name
            LIMIT ?
            """,
            (*aliases, limit),
        ).fetchall()
        items: list[dict[str, object]] = []
        seen_names: set[str] = set()
        for row in rows:
            source_name = str(row["source_name"])
            if source_name in seen_names:
                continue
            seen_names.add(source_name)
            detail = json_loads_object(str(row["detail_json"]))
            semantic = coerce_call_semantics(detail, source_name=source_name, target_name=procedure_name)
            items.append({"procedure_name": source_name, **semantic})
        return items

    def find_shortest_call_path(
        self,
        conn: sqlite3.Connection,
        *,
        source_procedure: str,
        target_procedure: str,
        max_depth: int = 4,
    ) -> list[str] | None:
        source_name = self.resolve_procedure_name(conn, source_procedure)
        target_name = self.resolve_procedure_name(conn, target_procedure)
        if not source_name or not target_name:
            return None
        if source_name == target_name:
            return [source_name]

        target_aliases = set(self.procedure_aliases(conn, procedure_name=target_name))
        queue: deque[tuple[str, list[str]]] = deque([(source_name, [source_name])])
        visited: set[str] = {source_name}

        while queue:
            current_name, path = queue.popleft()
            if len(path) > max_depth + 1:
                continue
            rows = conn.execute(
                """
                SELECT DISTINCT target_name
                FROM edges
                WHERE source_name = ? AND edge_type = 'calls_procedure'
                ORDER BY target_name
                """,
                (current_name,),
            ).fetchall()
            for row in rows:
                neighbor_name = self.resolve_procedure_name(conn, str(row["target_name"]))
                if not neighbor_name:
                    continue
                next_path = [*path, neighbor_name]
                neighbor_aliases = set(self.procedure_aliases(conn, procedure_name=neighbor_name))
                if target_aliases & neighbor_aliases:
                    return next_path
                if neighbor_name in visited or len(next_path) > max_depth + 1:
                    continue
                visited.add(neighbor_name)
                queue.append((neighbor_name, next_path))

        return None

    def procedure_aliases(
        self,
        conn: sqlite3.Connection,
        *,
        procedure_id: int | None = None,
        procedure_name: str | None = None,
    ) -> tuple[str, ...]:
        if procedure_id is not None:
            row = conn.execute("SELECT name, chinese_name FROM procedures WHERE id = ?", (procedure_id,)).fetchone()
        elif procedure_name is not None:
            row = conn.execute(
                """
                SELECT name, chinese_name
                FROM procedures
                WHERE lower(name) = lower(?) OR lower(COALESCE(chinese_name, '')) = lower(?)
                ORDER BY CASE WHEN lower(name) = lower(?) THEN 0 ELSE 1 END
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

    def resolve_procedure_name(self, conn: sqlite3.Connection, raw_name: str) -> str:
        aliases = self.procedure_aliases(conn, procedure_name=raw_name)
        return aliases[0] if aliases else raw_name

    def fetch_related_procedure_summaries(
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
                info = self.lookup_procedure_summary(conn, procedure_name)
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

    def lookup_procedure_summary(
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
            WHERE lower(p.name) = lower(?) OR lower(COALESCE(p.chinese_name, '')) = lower(?)
            ORDER BY CASE WHEN lower(p.name) = lower(?) THEN 0 ELSE 1 END, c.seq
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
            "line_start": maybe_int(row["line_start"]),
            "line_end": maybe_int(row["line_end"]),
            "chunk_type": str(row["chunk_type"]) if row["chunk_type"] is not None else None,
            "summary_text": str(row["summary_text"]) if row["summary_text"] is not None else None,
        }


def _statement_row(row: sqlite3.Row) -> dict[str, object]:
    return {
        "statement_id": int(row["id"]),
        "seq": int(row["seq"]),
        "kind": str(row["kind"]),
        "line_start": int(row["line_start"]),
        "line_end": int(row["line_end"]),
        "raw": str(row["raw"]),
    }
