from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, TextIO

from .answering import CodebaseAnswerer
from .constants import JSON_RPC_VERSION, MCP_PROTOCOL_VERSION
from .debug_bundle import (
    DebugBundlePanelThresholds,
    build_debug_bundle,
    build_debug_bundle_regression_panel,
    compare_debug_bundles,
    compare_debug_bundle_regression_panel_latest_baseline,
    compare_debug_bundle_regression_panel_baseline,
    compare_debug_bundle_regression_panels,
    delete_debug_bundle_regression_panel_baseline,
    evaluate_debug_bundle_regression_panel_thresholds,
    load_debug_bundle_regression_panel_baseline,
    load_debug_bundle_regression_panel_release_workflow,
    list_debug_bundle_regression_panel_baselines,
    list_debug_bundle_regression_panel_release_workflows,
    guarded_promote_debug_bundle_regression_panel_baseline,
    promote_debug_bundle_regression_panel_baseline,
    save_debug_bundle_regression_panel_baseline,
    evaluate_debug_bundle_regression_panel_promotion_gate,
    run_debug_bundle_regression_panel_release_workflow,
    summarize_debug_bundle_regression_panel_baseline_trend,
)
from .indexer import SQLiteIndexer
from .qa import CodebaseQA
from .table_indexer import TableIndexer


class McpProtocolError(Exception):
    def __init__(self, code: int, message: str, data: dict[str, object] | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.data = data


class CodebaseMcpServer:
    def __init__(
        self,
        *,
        indexer: SQLiteIndexer | None = None,
        qa: CodebaseQA | None = None,
        answerer: CodebaseAnswerer | None = None,
        table_indexer: TableIndexer | None = None,
        default_db_path: str | Path | None = None,
        default_metadata_db_path: str | Path | None = None,
        default_table_db_path: str | Path | None = None,
    ) -> None:
        self.indexer = indexer or SQLiteIndexer()
        self.qa = qa or CodebaseQA(self.indexer)
        self.answerer = answerer or CodebaseAnswerer(self.qa)
        self.table_indexer = table_indexer or TableIndexer()
        self.default_db_path = str(default_db_path) if default_db_path else None
        self.default_metadata_db_path = str(default_metadata_db_path) if default_metadata_db_path else None
        self.default_table_db_path = str(default_table_db_path) if default_table_db_path else None
        self._initialized = False

    def serve(
        self,
        *,
        input_stream: TextIO | None = None,
        output_stream: TextIO | None = None,
    ) -> None:
        input_stream = input_stream or sys.stdin
        output_stream = output_stream or sys.stdout

        for raw_line in input_stream:
            line = raw_line.strip()
            if not line:
                continue
            response = self.handle_message(line)
            if response is None:
                continue
            output_stream.write(json.dumps(response, ensure_ascii=False, separators=(",", ":")) + "\n")
            output_stream.flush()

    def handle_message(self, message: str | dict[str, object]) -> dict[str, object] | None:
        try:
            payload = self._coerce_payload(message)
        except McpProtocolError as exc:
            return self._error_response(None, exc)

        message_id = payload.get("id")

        try:
            return self._dispatch(payload)
        except McpProtocolError as exc:
            return self._error_response(message_id, exc)
        except Exception as exc:  # pragma: no cover - defensive guard for MCP transport
            return self._error_response(
                message_id,
                McpProtocolError(-32603, "Internal error", {"detail": str(exc)}),
            )

    def _coerce_payload(self, message: str | dict[str, object]) -> dict[str, object]:
        if isinstance(message, dict):
            payload = message
        else:
            try:
                payload = json.loads(message)
            except json.JSONDecodeError as exc:
                raise McpProtocolError(-32700, "Parse error", {"detail": str(exc)}) from exc

        if not isinstance(payload, dict):
            raise McpProtocolError(-32600, "Invalid Request", {"detail": "JSON-RPC payload must be an object."})

        if payload.get("jsonrpc") != JSON_RPC_VERSION:
            raise McpProtocolError(-32600, "Invalid Request", {"detail": "jsonrpc must be '2.0'."})

        method = payload.get("method")
        if not isinstance(method, str) or not method:
            raise McpProtocolError(-32600, "Invalid Request", {"detail": "method must be a non-empty string."})

        return payload

    def _dispatch(self, payload: dict[str, object]) -> dict[str, object] | None:
        method = str(payload["method"])
        params = payload.get("params")
        message_id = payload.get("id")

        if params is None:
            params = {}
        if not isinstance(params, dict):
            raise McpProtocolError(-32602, "Invalid params", {"detail": "params must be an object."})

        if method == "initialize":
            result = self._handle_initialize(params)
            return self._success_response(message_id, result)

        if method == "notifications/initialized":
            self._initialized = True
            return None

        if method == "notifications/cancelled":
            return None

        if method == "ping":
            return self._success_response(message_id, {})

        if method == "tools/list":
            return self._success_response(message_id, {"tools": self._tool_definitions()})

        if method == "tools/call":
            result = self._handle_tool_call(params)
            return self._success_response(message_id, result)

        raise McpProtocolError(-32601, "Method not found", {"method": method})

    def _handle_initialize(self, params: dict[str, object]) -> dict[str, object]:
        requested_version = params.get("protocolVersion")
        if requested_version and not isinstance(requested_version, str):
            raise McpProtocolError(-32602, "Invalid params", {"detail": "protocolVersion must be a string."})

        return {
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {
                "tools": {
                    "listChanged": False,
                }
            },
            "serverInfo": {
                "name": "uses-indexer-mcp",
                "version": "0.2.0",
            },
            "instructions": self._server_instructions(),
        }

    def _handle_tool_call(self, params: dict[str, object]) -> dict[str, object]:
        name = params.get("name")
        arguments = params.get("arguments", {})

        if not isinstance(name, str) or not name:
            raise McpProtocolError(-32602, "Invalid params", {"detail": "tools/call requires a non-empty tool name."})
        if not isinstance(arguments, dict):
            raise McpProtocolError(-32602, "Invalid params", {"detail": "tool arguments must be an object."})

        tool_map = {
            "db_summary": self._tool_db_summary,
            "query_codebase": self._tool_query_codebase,
            "assemble_evidence": self._tool_assemble_evidence,
            "ask_codebase": self._tool_ask_codebase,
            "answer_codebase": self._tool_answer_codebase,
            "debug_bundle": self._tool_debug_bundle,
            "compare_debug_bundles": self._tool_compare_debug_bundles,
            "compare_debug_bundle_panel": self._tool_compare_debug_bundle_panel,
            "compare_debug_bundle_panels": self._tool_compare_debug_bundle_panels,
            "save_debug_bundle_panel_baseline": self._tool_save_debug_bundle_panel_baseline,
            "list_debug_bundle_panel_baselines": self._tool_list_debug_bundle_panel_baselines,
            "show_debug_bundle_panel_baseline_trend": self._tool_show_debug_bundle_panel_baseline_trend,
            "show_debug_bundle_panel_baseline": self._tool_show_debug_bundle_panel_baseline,
            "list_debug_bundle_panel_release_workflows": self._tool_list_debug_bundle_panel_release_workflows,
            "show_debug_bundle_panel_release_workflow": self._tool_show_debug_bundle_panel_release_workflow,
            "evaluate_debug_bundle_panel_promotion_gate": self._tool_evaluate_debug_bundle_panel_promotion_gate,
            "promote_debug_bundle_panel_baseline": self._tool_promote_debug_bundle_panel_baseline,
            "run_debug_bundle_panel_release_workflow": self._tool_run_debug_bundle_panel_release_workflow,
            "delete_debug_bundle_panel_baseline": self._tool_delete_debug_bundle_panel_baseline,
            "compare_debug_bundle_panel_baseline": self._tool_compare_debug_bundle_panel_baseline,
            "compare_debug_bundle_panel_latest_baseline": self._tool_compare_debug_bundle_panel_latest_baseline,
            "query_metadata": self._tool_query_metadata,
            "query_table": self._tool_query_table,
        }

        handler = tool_map.get(name)
        if handler is None:
            raise McpProtocolError(-32601, "Method not found", {"detail": f"Unknown tool: {name}"})

        try:
            structured = handler(arguments)
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(structured, ensure_ascii=False, indent=2),
                    }
                ],
                "structuredContent": structured,
                "isError": False,
            }
        except McpProtocolError:
            raise
        except Exception as exc:
            error_payload = {"tool": name, "detail": str(exc)}
            return {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps({"error": error_payload}, ensure_ascii=False, indent=2),
                    }
                ],
                "structuredContent": {"error": error_payload},
                "isError": True,
            }

    def _tool_definitions(self) -> list[dict[str, object]]:
        return [
            {
                "name": "db_summary",
                "description": "Read high-level statistics for the indexed USES/UFT SQLite database.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {
                            "type": "string",
                            "description": "Optional SQLite database path. Defaults to the server's configured index.",
                        }
                    },
                    "additionalProperties": False,
                },
            },
            {
                "name": "query_codebase",
                "description": "Run keyword retrieval against the indexed USES/UFT codebase and return ranked hits.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "query": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 50},
                        "debug": {"type": "boolean"},
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "assemble_evidence",
                "description": "Build grounded evidence blocks, context windows, and LLM-ready context for a repository question.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "query": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "context_window": {"type": "integer", "minimum": 0, "maximum": 20},
                        "related_limit": {"type": "integer", "minimum": 0, "maximum": 20},
                        "debug": {"type": "boolean"},
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "ask_codebase",
                "description": "Prepare a full QA package for the indexed USES/UFT codebase, including evidence and prompt material.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "question": {"type": "string"},
                        "evidence_limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "context_window": {"type": "integer", "minimum": 0, "maximum": 20},
                        "related_limit": {"type": "integer", "minimum": 0, "maximum": 20},
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "answer_codebase",
                "description": "Return the final grounded answer for a USES/UFT repository question, using an external LLM when configured.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "question": {"type": "string"},
                        "evidence_limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "context_window": {"type": "integer", "minimum": 0, "maximum": 20},
                        "related_limit": {"type": "integer", "minimum": 0, "maximum": 20},
                        "allow_draft_fallback": {"type": "boolean"},
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "debug_bundle",
                "description": "Bundle query, evidence, and answer output for a single question to support debugging and offline replay.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "question": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "context_window": {"type": "integer", "minimum": 0, "maximum": 20},
                        "related_limit": {"type": "integer", "minimum": 0, "maximum": 20}
                    },
                    "required": ["question"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "compare_debug_bundles",
                "description": "Compare two debug bundle archives or bundle.json files and summarize query/evidence/answer differences.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "before_path": {"type": "string"},
                        "after_path": {"type": "string"},
                    },
                    "required": ["before_path", "after_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "compare_debug_bundle_panel",
                "description": "Run a fixed question set across before/after DBs, build a regression panel, and evaluate optional panel thresholds.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "before_db_path": {"type": "string"},
                        "after_db_path": {"type": "string"},
                        "cases_path": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "context_window": {"type": "integer", "minimum": 0, "maximum": 20},
                        "related_limit": {"type": "integer", "minimum": 0, "maximum": 20},
                        "archive_dir": {"type": "string"},
                        "max_changed_cases": {"type": "integer", "minimum": 0},
                        "max_high_priority_cases": {"type": "integer", "minimum": 0},
                        "max_verdict_counts": {
                            "type": "object",
                            "additionalProperties": {"type": "integer", "minimum": 0}
                        },
                        "max_focus_area_counts": {
                            "type": "object",
                            "additionalProperties": {"type": "integer", "minimum": 0}
                        }
                    },
                    "required": ["before_db_path", "after_db_path", "cases_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "compare_debug_bundle_panels",
                "description": "Compare two saved debug bundle regression panel archives or panel.json files.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "before_path": {"type": "string"},
                        "after_path": {"type": "string"},
                    },
                    "required": ["before_path", "after_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "save_debug_bundle_panel_baseline",
                "description": "Save a named baseline from a debug bundle regression panel archive or panel.json file.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                        "baseline_notes": {"type": "string"},
                        "baseline_tags": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["panel_path", "baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "list_debug_bundle_panel_baselines",
                "description": "List saved debug bundle regression panel baselines.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_dir": {"type": "string"},
                        "baseline_tag": {"type": "string"},
                    },
                    "additionalProperties": False,
                },
            },
            {
                "name": "show_debug_bundle_panel_baseline_trend",
                "description": "Show baseline trend history for saved debug bundle regression panel baselines.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_dir": {"type": "string"},
                        "baseline_tag": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1},
                    },
                    "additionalProperties": False,
                },
            },
            {
                "name": "show_debug_bundle_panel_baseline",
                "description": "Show full metadata for a saved debug bundle regression panel baseline.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                    },
                    "required": ["baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "list_debug_bundle_panel_release_workflows",
                "description": "List saved debug bundle panel release workflow archives.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "workflow_dir": {"type": "string"},
                        "baseline_tag": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "additionalProperties": False,
                },
            },
            {
                "name": "show_debug_bundle_panel_release_workflow",
                "description": "Show a saved debug bundle panel release workflow archive.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "workflow_path": {"type": "string"},
                    },
                    "required": ["workflow_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "promote_debug_bundle_panel_baseline",
                "description": "Promote a panel archive or panel.json file to the active named debug bundle regression panel baseline.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                        "baseline_notes": {"type": "string"},
                        "baseline_tags": {"type": "array", "items": {"type": "string"}},
                        "gate_baseline_tag": {"type": "string"},
                        "require_threshold_pass": {"type": "boolean"},
                        "blocked_latest_verdicts": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["panel_path", "baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "evaluate_debug_bundle_panel_promotion_gate",
                "description": "Evaluate whether a panel can be safely promoted to a named debug bundle regression panel baseline.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                        "baseline_tag": {"type": "string"},
                        "require_threshold_pass": {"type": "boolean"},
                        "blocked_latest_verdicts": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["panel_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "run_debug_bundle_panel_release_workflow",
                "description": "Run latest-baseline comparison, promotion gate, and optional promote as one release workflow.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                        "baseline_notes": {"type": "string"},
                        "baseline_tags": {"type": "array", "items": {"type": "string"}},
                        "gate_baseline_tag": {"type": "string"},
                        "require_threshold_pass": {"type": "boolean"},
                        "blocked_latest_verdicts": {"type": "array", "items": {"type": "string"}},
                        "auto_promote": {"type": "boolean"},
                        "archive_dir": {"type": "string"},
                    },
                    "required": ["panel_path", "baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "delete_debug_bundle_panel_baseline",
                "description": "Delete a saved debug bundle regression panel baseline.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                    },
                    "required": ["baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "compare_debug_bundle_panel_baseline",
                "description": "Compare a panel archive against a saved named debug bundle regression panel baseline.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_name": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                    },
                    "required": ["panel_path", "baseline_name"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "compare_debug_bundle_panel_latest_baseline",
                "description": "Compare a panel archive against the most recently saved debug bundle regression panel baseline, optionally filtered by tag.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "panel_path": {"type": "string"},
                        "baseline_dir": {"type": "string"},
                        "baseline_tag": {"type": "string"},
                    },
                    "required": ["panel_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "query_metadata",
                "description": "Query metadata index (constants, configs, error numbers, etc.) for USES/UFT codebase.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "query": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 50},
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "query_table",
                "description": "Query table structure index for USES/UFT codebase.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "db_path": {"type": "string"},
                        "query": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 50},
                    },
                    "required": ["query"],
                    "additionalProperties": False,
                },
            },
        ]

    def _resolve_metadata_db_path(self, arguments: dict[str, object]) -> str:
        db_path = self._optional_string(arguments, "db_path")
        if not db_path:
            db_path = self._optional_string(arguments, "metadata_db_path")
        if not db_path:
            db_path = self.default_metadata_db_path
        if not db_path:
            raise McpProtocolError(-32602, "Invalid params", {"detail": "db_path is required for metadata query when no default is configured."})
        db_file = Path(db_path)
        if not db_file.exists():
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"SQLite database does not exist: {db_file}"})
        return str(db_file)

    def _resolve_table_db_path(self, arguments: dict[str, object]) -> str:
        db_path = self._optional_string(arguments, "db_path")
        if not db_path:
            db_path = self._optional_string(arguments, "table_db_path")
        if not db_path:
            db_path = self.default_table_db_path
        if not db_path:
            raise McpProtocolError(-32602, "Invalid params", {"detail": "db_path is required for table query when no default is configured."})
        db_file = Path(db_path)
        if not db_file.exists():
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"SQLite database does not exist: {db_file}"})
        return str(db_file)

    def _tool_query_metadata(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_metadata_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=10)
        return self.indexer.query_index(db_path, query, limit=limit)

    def _tool_query_table(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_table_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=10)
        return self.table_indexer.query_index(db_path, query, limit=limit)

    def _tool_db_summary(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        return self.indexer.summarize_db(db_path)

    def _tool_query_codebase(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=10)
        debug = self._optional_bool(arguments, "debug", default=False)
        return self.indexer.query_index(db_path, query, limit=limit, debug=debug)

    def _tool_assemble_evidence(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        debug = self._optional_bool(arguments, "debug", default=False)
        return self.indexer.assemble_evidence(
            db_path,
            query,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
            debug=debug,
        )

    def _tool_ask_codebase(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        question = self._required_string(arguments, "question")
        evidence_limit = self._optional_int(arguments, "evidence_limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        return self.qa.ask(
            db_path,
            question,
            evidence_limit=evidence_limit,
            context_window=context_window,
            related_limit=related_limit,
        )

    def _tool_answer_codebase(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        question = self._required_string(arguments, "question")
        evidence_limit = self._optional_int(arguments, "evidence_limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        allow_draft_fallback = self._optional_bool(arguments, "allow_draft_fallback", default=True)
        return self.answerer.answer(
            db_path,
            question,
            evidence_limit=evidence_limit,
            context_window=context_window,
            related_limit=related_limit,
            allow_draft_fallback=allow_draft_fallback,
        )

    def _tool_debug_bundle(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        question = self._required_string(arguments, "question")
        limit = self._optional_int(arguments, "limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        return build_debug_bundle(
            indexer=self.indexer,
            answerer=self.answerer,
            db_path=db_path,
            question=question,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
        )

    def _tool_compare_debug_bundles(self, arguments: dict[str, object]) -> dict[str, object]:
        before_path = self._required_string(arguments, "before_path")
        after_path = self._required_string(arguments, "after_path")
        return compare_debug_bundles(before_path, after_path)

    def _tool_compare_debug_bundle_panel(self, arguments: dict[str, object]) -> dict[str, object]:
        before_db_path = self._required_string(arguments, "before_db_path")
        after_db_path = self._required_string(arguments, "after_db_path")
        cases_path = self._required_string(arguments, "cases_path")
        limit = self._optional_int(arguments, "limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        archive_dir = self._optional_string(arguments, "archive_dir")
        result = build_debug_bundle_regression_panel(
            indexer=self.indexer,
            answerer=self.answerer,
            before_db_path=before_db_path,
            after_db_path=after_db_path,
            cases_path=cases_path,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
            archive_dir=archive_dir,
        )
        result["thresholds"] = evaluate_debug_bundle_regression_panel_thresholds(
            result,
            DebugBundlePanelThresholds(
                max_changed_cases=self._optional_nonnegative_int(arguments, "max_changed_cases"),
                max_high_priority_cases=self._optional_nonnegative_int(arguments, "max_high_priority_cases"),
                max_verdict_counts=self._optional_named_int_mapping(arguments, "max_verdict_counts"),
                max_focus_area_counts=self._optional_named_int_mapping(arguments, "max_focus_area_counts"),
            ),
        )
        return result

    def _tool_compare_debug_bundle_panels(self, arguments: dict[str, object]) -> dict[str, object]:
        before_path = self._required_string(arguments, "before_path")
        after_path = self._required_string(arguments, "after_path")
        return compare_debug_bundle_regression_panels(before_path, after_path)

    def _tool_save_debug_bundle_panel_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_notes = self._optional_string(arguments, "baseline_notes")
        baseline_tags = self._optional_string_list(arguments, "baseline_tags")
        return save_debug_bundle_regression_panel_baseline(
            panel_path,
            baseline_name,
            baseline_dir=baseline_dir,
            baseline_notes=baseline_notes,
            baseline_tags=baseline_tags,
        )

    def _tool_list_debug_bundle_panel_baselines(self, arguments: dict[str, object]) -> dict[str, object]:
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_tag = self._optional_string(arguments, "baseline_tag")
        return list_debug_bundle_regression_panel_baselines(baseline_dir=baseline_dir, baseline_tag=baseline_tag)

    def _tool_show_debug_bundle_panel_baseline_trend(self, arguments: dict[str, object]) -> dict[str, object]:
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_tag = self._optional_string(arguments, "baseline_tag")
        limit = self._optional_nonnegative_int(arguments, "limit")
        if limit == 0:
            raise McpProtocolError(-32602, "Invalid params", {"detail": "limit must be >= 1."})
        return summarize_debug_bundle_regression_panel_baseline_trend(
            baseline_dir=baseline_dir,
            baseline_tag=baseline_tag,
            limit=limit,
        )

    def _tool_show_debug_bundle_panel_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        return load_debug_bundle_regression_panel_baseline(baseline_name, baseline_dir=baseline_dir)

    def _tool_list_debug_bundle_panel_release_workflows(self, arguments: dict[str, object]) -> dict[str, object]:
        workflow_dir = self._optional_string(arguments, "workflow_dir")
        baseline_tag = self._optional_string(arguments, "baseline_tag")
        status = self._optional_string(arguments, "status")
        return list_debug_bundle_regression_panel_release_workflows(
            workflow_dir=workflow_dir,
            baseline_tag=baseline_tag,
            status=status,
        )

    def _tool_show_debug_bundle_panel_release_workflow(self, arguments: dict[str, object]) -> dict[str, object]:
        workflow_path = self._required_string(arguments, "workflow_path")
        return load_debug_bundle_regression_panel_release_workflow(workflow_path)

    def _tool_promote_debug_bundle_panel_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_notes = self._optional_string(arguments, "baseline_notes")
        baseline_tags = self._optional_string_list(arguments, "baseline_tags")
        gate_baseline_tag = self._optional_string(arguments, "gate_baseline_tag")
        require_threshold_pass = self._optional_bool(arguments, "require_threshold_pass", default=False)
        blocked_latest_verdicts = self._optional_string_list(arguments, "blocked_latest_verdicts")
        if require_threshold_pass or blocked_latest_verdicts:
            return guarded_promote_debug_bundle_regression_panel_baseline(
                panel_path,
                baseline_name,
                baseline_dir=baseline_dir,
                baseline_notes=baseline_notes,
                baseline_tags=baseline_tags,
                gate_baseline_tag=gate_baseline_tag,
                require_threshold_pass=require_threshold_pass,
                blocked_latest_verdicts=blocked_latest_verdicts,
            )
        return promote_debug_bundle_regression_panel_baseline(
            panel_path,
            baseline_name,
            baseline_dir=baseline_dir,
            baseline_notes=baseline_notes,
            baseline_tags=baseline_tags,
        )

    def _tool_evaluate_debug_bundle_panel_promotion_gate(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_tag = self._optional_string(arguments, "baseline_tag")
        require_threshold_pass = self._optional_bool(arguments, "require_threshold_pass", default=False)
        blocked_latest_verdicts = self._optional_string_list(arguments, "blocked_latest_verdicts")
        return evaluate_debug_bundle_regression_panel_promotion_gate(
            panel_path,
            baseline_dir=baseline_dir,
            baseline_tag=baseline_tag,
            require_threshold_pass=require_threshold_pass,
            blocked_latest_verdicts=blocked_latest_verdicts,
        )

    def _tool_run_debug_bundle_panel_release_workflow(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_notes = self._optional_string(arguments, "baseline_notes")
        baseline_tags = self._optional_string_list(arguments, "baseline_tags")
        gate_baseline_tag = self._optional_string(arguments, "gate_baseline_tag")
        require_threshold_pass = self._optional_bool(arguments, "require_threshold_pass", default=False)
        blocked_latest_verdicts = self._optional_string_list(arguments, "blocked_latest_verdicts")
        auto_promote = self._optional_bool(arguments, "auto_promote", default=True)
        archive_dir = self._optional_string(arguments, "archive_dir")
        return run_debug_bundle_regression_panel_release_workflow(
            panel_path,
            baseline_name,
            baseline_dir=baseline_dir,
            baseline_notes=baseline_notes,
            baseline_tags=baseline_tags,
            gate_baseline_tag=gate_baseline_tag,
            require_threshold_pass=require_threshold_pass,
            blocked_latest_verdicts=blocked_latest_verdicts,
            auto_promote=auto_promote,
            archive_dir=archive_dir,
        )

    def _tool_delete_debug_bundle_panel_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        return delete_debug_bundle_regression_panel_baseline(baseline_name, baseline_dir=baseline_dir)

    def _tool_compare_debug_bundle_panel_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_name = self._required_string(arguments, "baseline_name")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        return compare_debug_bundle_regression_panel_baseline(panel_path, baseline_name, baseline_dir=baseline_dir)

    def _tool_compare_debug_bundle_panel_latest_baseline(self, arguments: dict[str, object]) -> dict[str, object]:
        panel_path = self._required_string(arguments, "panel_path")
        baseline_dir = self._optional_string(arguments, "baseline_dir")
        baseline_tag = self._optional_string(arguments, "baseline_tag")
        return compare_debug_bundle_regression_panel_latest_baseline(
            panel_path,
            baseline_dir=baseline_dir,
            baseline_tag=baseline_tag,
        )

    def _resolve_db_path(self, arguments: dict[str, object]) -> str:
        db_path = self._optional_string(arguments, "db_path")
        if not db_path:
            db_path = self._optional_string(arguments, "dbPath")
        if not db_path:
            db_path = self.default_db_path
        if not db_path:
            raise McpProtocolError(-32602, "Invalid params", {"detail": "db_path is required when no default database is configured."})

        db_file = Path(db_path)
        if not db_file.exists():
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"SQLite database does not exist: {db_file}"})
        return str(db_file)

    def _required_string(self, arguments: dict[str, object], name: str) -> str:
        value = arguments.get(name)
        if value is None:
            alt_name = self._camel_name(name)
            value = arguments.get(alt_name)
        if not isinstance(value, str) or not value.strip():
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be a non-empty string."})
        return value.strip()

    def _optional_string(self, arguments: dict[str, object], name: str) -> str | None:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return None
        if not isinstance(value, str):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be a string."})
        return value

    def _optional_string_list(self, arguments: dict[str, object], name: str) -> list[str] | None:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return None
        if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be a list of strings."})
        return list(value)

    def _optional_int(self, arguments: dict[str, object], name: str, *, default: int) -> int:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return default
        if isinstance(value, bool) or not isinstance(value, int):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be an integer."})
        return value

    def _optional_nonnegative_int(self, arguments: dict[str, object], name: str) -> int | None:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return None
        if isinstance(value, bool) or not isinstance(value, int):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be an integer."})
        if value < 0:
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be >= 0."})
        return value

    def _optional_named_int_mapping(self, arguments: dict[str, object], name: str) -> dict[str, int] | None:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return None
        if not isinstance(value, dict):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be an object."})
        result: dict[str, int] = {}
        for key, raw_value in value.items():
            if not isinstance(key, str) or not key.strip():
                raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} keys must be non-empty strings."})
            if isinstance(raw_value, bool) or not isinstance(raw_value, int):
                raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name}.{key} must be an integer."})
            if raw_value < 0:
                raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name}.{key} must be >= 0."})
            result[key.strip()] = raw_value
        return result

    def _optional_bool(self, arguments: dict[str, object], name: str, *, default: bool) -> bool:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return default
        if not isinstance(value, bool):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be a boolean."})
        return value

    def _camel_name(self, snake_name: str) -> str:
        parts = snake_name.split("_")
        return parts[0] + "".join(part.capitalize() for part in parts[1:])

    def _server_instructions(self) -> str:
        if self.default_db_path:
            return f"Use these tools to answer questions about the indexed USES/UFT codebase. Default db_path: {self.default_db_path}"
        return "Use these tools to answer questions about the indexed USES/UFT codebase."

    def _success_response(self, message_id: object, result: dict[str, object]) -> dict[str, object]:
        return {
            "jsonrpc": JSON_RPC_VERSION,
            "id": message_id,
            "result": result,
        }

    def _error_response(self, message_id: object, exc: McpProtocolError) -> dict[str, object]:
        error_payload: dict[str, Any] = {
            "code": exc.code,
            "message": exc.message,
        }
        if exc.data is not None:
            error_payload["data"] = exc.data
        return {
            "jsonrpc": JSON_RPC_VERSION,
            "id": message_id,
            "error": error_payload,
        }
