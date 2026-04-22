from __future__ import annotations

import sqlite3
import time
from pathlib import Path
from typing import TYPE_CHECKING

from .observability import build_evidence_debug_payload
from .response_schema import apply_response_envelope
from .semantic_recovery import format_call_edge_label, format_mc_topic_label, maybe_int


if TYPE_CHECKING:
    from .indexer import SQLiteIndexer


class EvidenceService:
    def __init__(self, owner: "SQLiteIndexer") -> None:
        self.owner = owner

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
        started_at = time.perf_counter()
        context_fetch = self.owner._context_fetch_service
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        candidates, fts_query, vector_status, retrieval_debug = self.owner._retrieval_service.retrieve_candidates(
            conn,
            db_path=db_path,
            query=query,
            candidate_limit=max(limit * 8, 40),
            debug=debug,
        )

        evidence_blocks: list[dict[str, object]] = []
        seen_contexts: set[tuple[int, int, int]] = set()
        context_indexes: dict[tuple[int, int, int], int] = {}
        procedure_counts: dict[int, int] = {}
        pruned_events: list[dict[str, object]] = []

        for rank, candidate in enumerate(candidates, start=1):
            procedure_id = int(candidate["procedure_id"])
            if procedure_counts.get(procedure_id, 0) >= 2:
                if debug:
                    pruned_events.append(
                        {
                            "reason": "procedure_evidence_cap",
                            "procedure_name": str(candidate["procedure_name"]),
                            "rank": rank,
                        }
                    )
                continue

            if candidate["hit_type"] == "chunk":
                context = context_fetch.fetch_chunk_block(conn, chunk_id=int(candidate["entity_id"]))
            elif candidate["hit_type"] == "block":
                context = context_fetch.fetch_block_context(conn, block_id=int(candidate["entity_id"]))
            else:
                context = context_fetch.fetch_context_block(
                    conn,
                    procedure_id=procedure_id,
                    statement_id=maybe_int(candidate.get("statement_id")),
                    context_window=context_window,
                )
            context_key = (
                procedure_id,
                int(context["line_start"]),
                int(context["line_end"]),
            )
            if context_key in seen_contexts:
                existing_index = context_indexes.get(context_key)
                if existing_index is not None:
                    existing_block = evidence_blocks[existing_index]
                    merged_reasons = list(existing_block.get("reasons") or [])
                    for reason in candidate.get("reasons", []):
                        if reason not in merged_reasons:
                            merged_reasons.append(reason)
                    existing_block["reasons"] = merged_reasons
                    matched_via = list(existing_block.get("matched_via") or [existing_block["retrieval_source"]])
                    retrieval_source = str(candidate["retrieval_source"])
                    if retrieval_source not in matched_via:
                        matched_via.append(retrieval_source)
                    existing_block["matched_via"] = matched_via
                if debug:
                    pruned_events.append(
                        {
                            "reason": "duplicate_context",
                            "procedure_name": str(candidate["procedure_name"]),
                            "line_start": int(context["line_start"]),
                            "line_end": int(context["line_end"]),
                            "rank": rank,
                        }
                    )
                continue

            seen_contexts.add(context_key)
            context_indexes[context_key] = len(evidence_blocks)
            procedure_counts[procedure_id] = procedure_counts.get(procedure_id, 0) + 1

            evidence_blocks.append(
                {
                    "rank": rank,
                    "score": round(float(candidate["score"]), 3),
                    "hit_type": candidate["hit_type"],
                    "retrieval_source": candidate["retrieval_source"],
                    "matched_via": list(candidate.get("matched_via", [candidate["retrieval_source"]])),
                    "match_source": candidate["match_source"],
                    "procedure_name": candidate["procedure_name"],
                    "chinese_name": candidate.get("chinese_name"),
                    "object_id": candidate.get("object_id"),
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
                    "recovered_blocks": context_fetch.fetch_covering_blocks(
                        conn,
                        procedure_id=procedure_id,
                        line_start=int(context["line_start"]),
                        line_end=int(context["line_end"]),
                        limit=3,
                    ),
                    "related_context": context_fetch.fetch_related_context(
                        conn,
                        procedure_id=procedure_id,
                        procedure_name=str(candidate["procedure_name"]),
                        related_limit=related_limit,
                    ),
                }
            )

            if len(evidence_blocks) >= limit:
                break

        llm_context = build_llm_context(query, evidence_blocks)
        conn.close()

        payload = {
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
        if debug:
            payload["debug"] = build_evidence_debug_payload(
                query=query,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
                retrieval_debug=retrieval_debug,
                pruned_events=pruned_events,
                evidence_blocks=evidence_blocks,
                elapsed_ms=(time.perf_counter() - started_at) * 1000.0,
            )
        return apply_response_envelope(payload, kind="evidence")


def build_llm_context(query: str, evidence_blocks: list[dict[str, object]]) -> str:
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
        if related["outgoing_call_edges"]:
            lines.append(
                "Related calls: "
                + ", ".join(format_call_edge_label(item) for item in related["outgoing_call_edges"])
            )
        elif related["outgoing_calls"]:
            lines.append(f"Related calls: {', '.join(related['outgoing_calls'])}")
        if related["incoming_caller_edges"]:
            lines.append(
                "Incoming callers: "
                + ", ".join(format_call_edge_label(item) for item in related["incoming_caller_edges"])
            )
        elif related["incoming_callers"]:
            lines.append(f"Incoming callers: {', '.join(related['incoming_callers'])}")
        if related["related_tables"]:
            table_desc = ", ".join(
                f"{item['edge_type']}:{item['name']}"
                for item in related["related_tables"]
            )
            lines.append(f"Related tables: {table_desc}")
        if related["related_actions"]:
            lines.append(f"Related actions: {', '.join(related['related_actions'])}")
        if related["published_mc_topics"]:
            lines.append(
                "Published MC topics: "
                + ", ".join(format_mc_topic_label(item) for item in related["published_mc_topics"])
            )
        if related["metadata_relations"]:
            metadata_desc = ", ".join(
                f"{item['edge_type']}:{item['target_name']}"
                for item in related["metadata_relations"]
            )
            lines.append(f"Metadata relations: {metadata_desc}")
        if related["control_flow"]:
            flow_desc = ", ".join(
                f"{item['edge_type']}:{item['target_name']}"
                for item in related["control_flow"]
            )
            lines.append(f"Control flow: {flow_desc}")
        if related["multi_hop_outgoing"]:
            for item in related["multi_hop_outgoing"]:
                depth = item.get("hop_depth", 2)
                lines.append(f"{depth}-hop outgoing: {block['procedure_name']} -> ... -> {item['procedure_name']}")
        if related["multi_hop_incoming"]:
            for item in related["multi_hop_incoming"]:
                depth = item.get("hop_depth", 2)
                lines.append(f"{depth}-hop incoming: {item['procedure_name']} -> ... -> {block['procedure_name']}")
        if related["related_procedures"]:
            for item in related["related_procedures"]:
                summary_text = item["summary_text"] or ""
                lines.append(
                    f"Related procedure ({item['relation_type']}): {item['procedure_name']} "
                    f"[{item['line_start']}-{item['line_end']}] {summary_text}".strip()
                )

    return "\n".join(lines)
