from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from .answering import CodebaseAnswerer
from .debug_bundle import build_debug_bundle, compare_debug_bundles
from .indexer import SQLiteIndexer
from .llm import LlmConfigError, LlmRequestError
from .qa import CodebaseQA


class ApiError(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class CodebaseApi:
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

    def serve(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        server = ThreadingHTTPServer((host, port), make_handler_class(self))
        try:
            print(f"USES Indexer API listening on http://{host}:{port}")
            server.serve_forever()
        finally:
            server.server_close()

    def handle_request(
        self,
        method: str,
        path: str,
        body: bytes | None = None,
    ) -> tuple[int, dict[str, Any]]:
        parsed = urlparse(path)
        route = parsed.path
        query_params = parse_qs(parsed.query)

        if route == "/health" and method == "GET":
            return HTTPStatus.OK, {
                "status": "ok",
                "service": "uses-indexer-api",
                "default_db_path": self.default_db_path,
                "routes": [
                    "GET /health",
                    "GET /db-summary",
                    "POST /query",
                    "POST /evidence",
                    "POST /ask",
                    "POST /answer",
                    "POST /debug-bundle",
                    "POST /compare-debug-bundles",
                ],
            }

        if route == "/db-summary" and method == "GET":
            db_path = self._resolve_db_path(query_params.get("db_path", [None])[0])
            return HTTPStatus.OK, self.indexer.summarize_db(db_path)

        if route == "/query" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            query = self._require_string(payload, "query")
            limit = _coerce_int(payload.get("limit", 20), "limit")
            return HTTPStatus.OK, self.indexer.query_index(db_path, query, limit=limit, debug=bool(payload.get("debug", False)))

        if route == "/evidence" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            query = self._require_string(payload, "query")
            limit = _coerce_int(payload.get("limit", 6), "limit")
            context_window = _coerce_int(payload.get("context_window", 2), "context_window")
            related_limit = _coerce_int(payload.get("related_limit", 3), "related_limit")
            return HTTPStatus.OK, self.indexer.assemble_evidence(
                db_path,
                query,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
                debug=bool(payload.get("debug", False)),
            )

        if route == "/ask" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            question = self._require_string(payload, "question")
            evidence_limit = _coerce_int(payload.get("evidence_limit", 6), "evidence_limit")
            context_window = _coerce_int(payload.get("context_window", 2), "context_window")
            related_limit = _coerce_int(payload.get("related_limit", 3), "related_limit")
            return HTTPStatus.OK, self.qa.ask(
                db_path,
                question,
                evidence_limit=evidence_limit,
                context_window=context_window,
                related_limit=related_limit,
            )

        if route == "/answer" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            question = self._require_string(payload, "question")
            evidence_limit = _coerce_int(payload.get("evidence_limit", 6), "evidence_limit")
            context_window = _coerce_int(payload.get("context_window", 2), "context_window")
            related_limit = _coerce_int(payload.get("related_limit", 3), "related_limit")
            allow_draft_fallback = bool(payload.get("allow_draft_fallback", True))
            try:
                result = self.answerer.answer(
                    db_path,
                    question,
                    evidence_limit=evidence_limit,
                    context_window=context_window,
                    related_limit=related_limit,
                    allow_draft_fallback=allow_draft_fallback,
                )
            except LlmConfigError as exc:
                raise ApiError(HTTPStatus.BAD_REQUEST, str(exc)) from exc
            except LlmRequestError as exc:
                raise ApiError(HTTPStatus.BAD_GATEWAY, str(exc)) from exc
            return HTTPStatus.OK, result

        if route == "/debug-bundle" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            question = self._require_string(payload, "question")
            limit = _coerce_int(payload.get("limit", 6), "limit")
            context_window = _coerce_int(payload.get("context_window", 2), "context_window")
            related_limit = _coerce_int(payload.get("related_limit", 3), "related_limit")
            return HTTPStatus.OK, build_debug_bundle(
                indexer=self.indexer,
                answerer=self.answerer,
                db_path=db_path,
                question=question,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
            )

        if route == "/compare-debug-bundles" and method == "POST":
            payload = self._parse_json_body(body)
            before_path = self._require_string(payload, "before_path")
            after_path = self._require_string(payload, "after_path")
            return HTTPStatus.OK, compare_debug_bundles(before_path, after_path)

        if route in {"/query", "/evidence", "/ask", "/answer", "/debug-bundle", "/compare-debug-bundles"} and method != "POST":
            raise ApiError(HTTPStatus.METHOD_NOT_ALLOWED, f"{route} only supports POST")

        raise ApiError(HTTPStatus.NOT_FOUND, f"Unknown route: {route}")

    def _resolve_db_path(self, explicit_db_path: str | None) -> str:
        db_path = explicit_db_path or self.default_db_path
        if not db_path:
            raise ApiError(HTTPStatus.BAD_REQUEST, "db_path is required")
        return db_path

    def _parse_json_body(self, body: bytes | None) -> dict[str, Any]:
        if not body:
            return {}
        try:
            parsed = json.loads(body.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise ApiError(HTTPStatus.BAD_REQUEST, f"Invalid JSON body: {exc.msg}") from exc
        if not isinstance(parsed, dict):
            raise ApiError(HTTPStatus.BAD_REQUEST, "JSON body must be an object")
        return parsed

    def _require_string(self, payload: dict[str, Any], key: str) -> str:
        value = payload.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ApiError(HTTPStatus.BAD_REQUEST, f"{key} is required")
        return value.strip()


def make_handler_class(api: CodebaseApi) -> type[BaseHTTPRequestHandler]:
    class ApiHandler(BaseHTTPRequestHandler):
        server_version = "UsesIndexerAPI/0.1"

        def do_GET(self) -> None:  # noqa: N802
            self._dispatch()

        def do_POST(self) -> None:  # noqa: N802
            self._dispatch()

        def do_OPTIONS(self) -> None:  # noqa: N802
            self.send_response(HTTPStatus.NO_CONTENT)
            self._write_common_headers(content_length=0)
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            return

        def _dispatch(self) -> None:
            body = None
            if self.command == "POST":
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length) if length > 0 else b""

            try:
                status_code, payload = api.handle_request(self.command, self.path, body)
            except ApiError as exc:
                status_code = exc.status_code
                payload = {"error": exc.message}
            except Exception as exc:  # pragma: no cover
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
                payload = {"error": str(exc)}

            encoded = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(int(status_code))
            self._write_common_headers(content_length=len(encoded))
            self.end_headers()
            self.wfile.write(encoded)

        def _write_common_headers(self, *, content_length: int) -> None:
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(content_length))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")

    return ApiHandler


def _coerce_int(value: Any, field_name: str) -> int:
    try:
        coerced = int(value)
    except (TypeError, ValueError) as exc:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be an integer") from exc
    if coerced <= 0:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be greater than 0")
    return coerced
