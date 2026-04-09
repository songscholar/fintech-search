from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, TextIO

from .answering import CodebaseAnswerer
from .indexer import SQLiteIndexer
from .qa import CodebaseQA

JSON_RPC_VERSION = "2.0"
MCP_PROTOCOL_VERSION = "2025-11-25"


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
        default_db_path: str | Path | None = None,
    ) -> None:
        self.indexer = indexer or SQLiteIndexer()
        self.qa = qa or CodebaseQA(self.indexer)
        self.answerer = answerer or CodebaseAnswerer(self.qa)
        self.default_db_path = str(default_db_path) if default_db_path else None
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
        ]

    def _tool_db_summary(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        return self.indexer.summarize_db(db_path)

    def _tool_query_codebase(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=10)
        return self.indexer.query_index(db_path, query, limit=limit)

    def _tool_assemble_evidence(self, arguments: dict[str, object]) -> dict[str, object]:
        db_path = self._resolve_db_path(arguments)
        query = self._required_string(arguments, "query")
        limit = self._optional_int(arguments, "limit", default=6)
        context_window = self._optional_int(arguments, "context_window", default=2)
        related_limit = self._optional_int(arguments, "related_limit", default=3)
        return self.indexer.assemble_evidence(
            db_path,
            query,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
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
            return None
        if not isinstance(value, str):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be a string."})
        return value

    def _optional_int(self, arguments: dict[str, object], name: str, *, default: int) -> int:
        value = arguments.get(name)
        if value is None:
            value = arguments.get(self._camel_name(name))
        if value is None:
            return default
        if isinstance(value, bool) or not isinstance(value, int):
            raise McpProtocolError(-32602, "Invalid params", {"detail": f"{name} must be an integer."})
        return value

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
