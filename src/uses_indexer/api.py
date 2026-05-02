from __future__ import annotations

import json
import mimetypes
import time
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from .agent_gateway import AgentConfigError, AgentGateway, AgentRequestError
from .answering import CodebaseAnswerer
from .debug_bundle import (
    DebugBundlePanelThresholds,
    build_debug_bundle,
    build_debug_bundle_regression_panel,
    compare_debug_bundles,
    compare_debug_bundle_regression_panel_latest_baseline,
    compare_debug_bundle_regression_panel_baseline,
    compare_debug_bundle_regression_panels,
    compare_debug_bundle_regression_panel_release_workflows,
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
from .llm import LlmConfigError, LlmRequestError
from .logging_system import (
    log_business,
    log_error,
    log_request,
    log_system,
    new_trace_id,
    sanitize_payload,
)
from .qa import CodebaseQA

WEB_DIR = Path(__file__).with_name("web")
WEB_INDEX_PATH = WEB_DIR / "index.html"
_PROJECT_ROOT = Path("/Users/songzuoqiang/Documents/agent/condex/codes")
_DOCS_DIR = _PROJECT_ROOT / "docs"
_DEFAULT_BG_PATH = _PROJECT_ROOT / "resources/img/橘子洲头.png"
WEB_ASSET_PATHS = {
    "/assets/styles.css": WEB_DIR / "styles.css",
    "/assets/app.js": WEB_DIR / "app.js",
    "/assets/content-pages.css": WEB_DIR / "content-pages.css",
    "/assets/markdown-base.css": WEB_DIR / "markdown-base.css",
    "/assets/markdown-renderer.js": WEB_DIR / "markdown-renderer.js",
    "/assets/marked.esm.js": WEB_DIR / "marked.esm.js",
    "/assets/highlight.min.js": WEB_DIR / "highlight.min.js",
    "/assets/site-utils.js": WEB_DIR / "site-utils.js",
    "/assets/rain-effect.js": WEB_DIR / "rain-effect.js",
    "/assets/fonts/fonts.css": WEB_DIR / "fonts" / "fonts.css",
    "/assets/bg.png": _DEFAULT_BG_PATH,
}


def _list_docs(subdir: str | None = None) -> dict[str, Any]:
    files: list[dict[str, str]] = []
    seen: set[str] = set()

    def _scan_dir(directory: Path, rel_prefix: str = "") -> None:
        if not directory.exists():
            return
        for path in sorted(directory.iterdir()):
            if path.is_dir():
                _scan_dir(path, rel_prefix=f"{rel_prefix}{path.name}/")
            elif path.suffix.lower() == ".md":
                name = path.stem
                if name in seen:
                    continue
                seen.add(name)
                title = _extract_doc_title(path)
                files.append({"name": name, "title": title, "path": f"{rel_prefix}{path.name}"})

    if subdir:
        _scan_dir(_DOCS_DIR / subdir)
    else:
        _scan_dir(_DOCS_DIR)
        for path in sorted(_PROJECT_ROOT.iterdir()):
            if path.is_file() and path.suffix.lower() == ".md":
                name = path.stem
                if name in seen:
                    continue
                seen.add(name)
                title = _extract_doc_title(path)
                files.append({"name": name, "title": title, "path": path.name})

    return {"files": files}


def _extract_doc_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return path.stem
    for line in text.splitlines()[:10]:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
    return path.stem


def _read_doc(name: str) -> dict[str, Any]:
    candidates: list[Path] = [
        _DOCS_DIR / f"{name}.md",
        _PROJECT_ROOT / f"{name}.md",
    ]
    # Recursively search in docs subdirectories
    if _DOCS_DIR.exists():
        for path in _DOCS_DIR.rglob(f"{name}.md"):
            candidates.append(path)
    for path in candidates:
        if path.exists():
            try:
                content = path.read_text(encoding="utf-8")
            except Exception as exc:
                raise ApiError(HTTPStatus.INTERNAL_SERVER_ERROR, f"Failed to read doc: {exc}") from exc
            return {"name": name, "title": _extract_doc_title(path), "content": content}
    raise ApiError(HTTPStatus.NOT_FOUND, f"Document not found: {name}")


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
        agent_gateway: AgentGateway | None = None,
        default_db_path: str | Path | None = None,
        default_metadata_db_path: str | Path | None = None,
        default_table_db_path: str | Path | None = None,
    ) -> None:
        self.indexer = indexer or SQLiteIndexer()
        self.qa = qa or CodebaseQA(self.indexer)
        self.answerer = answerer or CodebaseAnswerer(self.qa)
        self.agent_gateway = agent_gateway or AgentGateway.from_env(indexer=self.indexer, qa=self.qa)
        self.default_db_path = str(default_db_path) if default_db_path else None
        self.default_metadata_db_path = str(default_metadata_db_path) if default_metadata_db_path else None
        self.default_table_db_path = str(default_table_db_path) if default_table_db_path else None

    def serve(self, host: str = "127.0.0.1", port: int = 8000) -> None:
        server = ThreadingHTTPServer((host, port), make_handler_class(self))
        log_system(
            "api_server_start",
            host=host,
            port=port,
            default_db_path=self.default_db_path,
            default_metadata_db_path=self.default_metadata_db_path,
            default_table_db_path=self.default_table_db_path,
        )
        try:
            print(f"USES Indexer API listening on http://{host}:{port}")
            server.serve_forever()
        finally:
            log_system(
                "api_server_stop",
                host=host,
                port=port,
                default_db_path=self.default_db_path,
                default_metadata_db_path=self.default_metadata_db_path,
                default_table_db_path=self.default_table_db_path,
            )
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
                "default_metadata_db_path": self.default_metadata_db_path,
                "default_table_db_path": self.default_table_db_path,
                "routes": [
                    "GET /",
                    "GET /ui",
                    "GET /health",
                    "GET /db-summary",
                    "POST /query",
                    "POST /evidence",
                    "POST /ask",
                    "POST /answer",
                    "GET /agent/providers",
                    "POST /agent/chat",
                    "POST /agent/analyze",
                    "POST /debug-bundle",
                    "POST /compare-debug-bundles",
                    "POST /compare-debug-bundle-panel",
                    "POST /compare-debug-bundle-panels",
                    "GET /list-debug-bundle-panel-baselines",
                    "GET /show-debug-bundle-panel-baseline-trend",
                    "GET /show-debug-bundle-panel-baseline",
                    "GET /list-debug-bundle-panel-release-workflows",
                    "GET /show-debug-bundle-panel-release-workflow",
                    "POST /save-debug-bundle-panel-baseline",
                    "POST /promote-debug-bundle-panel-baseline",
                    "POST /evaluate-debug-bundle-panel-promotion-gate",
                    "POST /run-debug-bundle-panel-release-workflow",
                    "POST /compare-debug-bundle-panel-release-workflows",
                    "POST /compare-debug-bundle-panel-baseline",
                    "POST /compare-debug-bundle-panel-latest-baseline",
                    "POST /delete-debug-bundle-panel-baseline",
                ],
            }

        if route == "/client-log" and method == "POST":
            payload = self._parse_json_body(body)
            level = str(payload.get("level") or "error")
            event = str(payload.get("event") or "frontend_event")
            context = dict(payload.get("context") or {}) if isinstance(payload.get("context"), dict) else {}
            if level.lower() in {"error", "fatal"}:
                log_error(event=event, message=str(payload.get("message") or event), context={"frontend": context})
            else:
                log_business(event=f"frontend_{event}", frontend=context)
            return HTTPStatus.OK, {"status": "logged"}

        if route == "/db-summary" and method == "GET":
            db_path = self._resolve_db_path(query_params.get("db_path", [None])[0])
            return HTTPStatus.OK, self.indexer.summarize_db(db_path)

        if route == "/docs" and method == "GET":
            doc_dir = query_params.get("dir", [None])[0]
            return HTTPStatus.OK, _list_docs(subdir=doc_dir)

        if route.startswith("/docs/") and method == "GET":
            doc_name = route[len("/docs/"):]
            return HTTPStatus.OK, _read_doc(doc_name)

        if route == "/query" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            query = self._require_string(payload, "query")
            limit = _coerce_int(payload.get("limit", 20), "limit")
            expand_downstream = bool(payload.get("expand_downstream", True))
            return HTTPStatus.OK, self.indexer.query_index(
                db_path, query, limit=limit,
                debug=bool(payload.get("debug", False)),
                expand_downstream=expand_downstream,
            )

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

        if route == "/agent/providers" and method == "GET":
            return HTTPStatus.OK, self.agent_gateway.list_providers()

        if route == "/agent/analyze" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            question = self._require_string(payload, "question")
            provider = payload.get("provider")
            if provider is not None and not isinstance(provider, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "provider must be a string")
            provider_override = payload.get("provider_override")
            if provider_override is not None and not isinstance(provider_override, dict):
                raise ApiError(HTTPStatus.BAD_REQUEST, "provider_override must be an object")
            try:
                result = self.agent_gateway.analyze(
                    db_path=db_path,
                    question=question,
                    provider_name=provider,
                    provider_override=provider_override if isinstance(provider_override, dict) else None,
                )
            except AgentConfigError as exc:
                raise ApiError(HTTPStatus.BAD_REQUEST, str(exc)) from exc
            except AgentRequestError as exc:
                raise ApiError(HTTPStatus.BAD_GATEWAY, str(exc)) from exc
            return HTTPStatus.OK, result

        if route == "/agent/chat" and method == "POST":
            payload = self._parse_json_body(body)
            db_path = self._resolve_db_path(payload.get("db_path"))
            metadata_db_path = self._resolve_optional_db_path(
                payload.get("metadata_db_path"),
                self.default_metadata_db_path,
                "metadata_db_path",
            )
            table_db_path = self._resolve_optional_db_path(
                payload.get("table_db_path"),
                self.default_table_db_path,
                "table_db_path",
            )
            message = self._require_string(payload, "message")
            provider = payload.get("provider")
            if provider is not None and not isinstance(provider, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "provider must be a string")
            history = payload.get("history")
            if history is not None and not isinstance(history, list):
                raise ApiError(HTTPStatus.BAD_REQUEST, "history must be a list")
            attachments = payload.get("attachments")
            if attachments is not None and not isinstance(attachments, list):
                raise ApiError(HTTPStatus.BAD_REQUEST, "attachments must be a list")
            provider_override = payload.get("provider_override")
            if provider_override is not None and not isinstance(provider_override, dict):
                raise ApiError(HTTPStatus.BAD_REQUEST, "provider_override must be an object")
            system_prompt = payload.get("system_prompt")
            if system_prompt is not None and not isinstance(system_prompt, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "system_prompt must be a string")
            try:
                result = self.agent_gateway.chat(
                    db_path=db_path,
                    metadata_db_path=metadata_db_path,
                    table_db_path=table_db_path,
                    message=message,
                    provider_name=provider,
                    history=history if isinstance(history, list) else None,
                    include_retrieval=bool(payload.get("include_retrieval", True)),
                    include_evidence=bool(payload.get("include_evidence", True)),
                    include_answer_draft=bool(payload.get("include_answer_draft", False)),
                    auto_retrieve=bool(payload.get("auto_retrieve", False)),
                    max_search_rounds=_coerce_int(payload.get("max_search_rounds", 4), "max_search_rounds"),
                    limit=_coerce_int(payload.get("limit", 6), "limit"),
                    context_window=_coerce_int(payload.get("context_window", 2), "context_window"),
                    related_limit=_coerce_int(payload.get("related_limit", 3), "related_limit"),
                    system_prompt=system_prompt,
                    attachments=attachments if isinstance(attachments, list) else None,
                    provider_override=provider_override if isinstance(provider_override, dict) else None,
                )
            except AgentConfigError as exc:
                raise ApiError(HTTPStatus.BAD_REQUEST, str(exc)) from exc
            except AgentRequestError as exc:
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

        if route == "/compare-debug-bundle-panel" and method == "POST":
            payload = self._parse_json_body(body)
            before_db_path = self._require_string(payload, "before_db_path")
            after_db_path = self._require_string(payload, "after_db_path")
            cases_path = self._require_string(payload, "cases_path")
            limit = _coerce_int(payload.get("limit", 6), "limit")
            context_window = _coerce_int(payload.get("context_window", 2), "context_window")
            related_limit = _coerce_int(payload.get("related_limit", 3), "related_limit")
            archive_dir = payload.get("archive_dir")
            if archive_dir is not None and not isinstance(archive_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "archive_dir must be a string")
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
                    max_changed_cases=_optional_nonnegative_int(payload.get("max_changed_cases"), "max_changed_cases"),
                    max_high_priority_cases=_optional_nonnegative_int(payload.get("max_high_priority_cases"), "max_high_priority_cases"),
                    max_verdict_counts=_coerce_named_int_mapping(payload.get("max_verdict_counts"), "max_verdict_counts"),
                    max_focus_area_counts=_coerce_named_int_mapping(payload.get("max_focus_area_counts"), "max_focus_area_counts"),
                ),
            )
            return HTTPStatus.OK, result

        if route == "/compare-debug-bundle-panels" and method == "POST":
            payload = self._parse_json_body(body)
            before_path = self._require_string(payload, "before_path")
            after_path = self._require_string(payload, "after_path")
            return HTTPStatus.OK, compare_debug_bundle_regression_panels(before_path, after_path)

        if route == "/list-debug-bundle-panel-baselines" and method == "GET":
            baseline_dir = query_params.get("baseline_dir", [None])[0]
            baseline_tag = query_params.get("baseline_tag", [None])[0]
            return HTTPStatus.OK, list_debug_bundle_regression_panel_baselines(baseline_dir=baseline_dir, baseline_tag=baseline_tag)

        if route == "/show-debug-bundle-panel-baseline" and method == "GET":
            baseline_name = query_params.get("baseline_name", [None])[0]
            if not baseline_name:
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_name is required")
            baseline_dir = query_params.get("baseline_dir", [None])[0]
            return HTTPStatus.OK, load_debug_bundle_regression_panel_baseline(baseline_name, baseline_dir=baseline_dir)

        if route == "/show-debug-bundle-panel-baseline-trend" and method == "GET":
            baseline_dir = query_params.get("baseline_dir", [None])[0]
            baseline_tag = query_params.get("baseline_tag", [None])[0]
            raw_limit = query_params.get("limit", [None])[0]
            limit = _coerce_int(raw_limit, "limit") if raw_limit is not None else None
            return HTTPStatus.OK, summarize_debug_bundle_regression_panel_baseline_trend(
                baseline_dir=baseline_dir,
                baseline_tag=baseline_tag,
                limit=limit,
            )

        if route == "/list-debug-bundle-panel-release-workflows" and method == "GET":
            workflow_dir = query_params.get("workflow_dir", [None])[0]
            baseline_tag = query_params.get("baseline_tag", [None])[0]
            status_filter = query_params.get("status", [None])[0]
            return HTTPStatus.OK, list_debug_bundle_regression_panel_release_workflows(
                workflow_dir=workflow_dir,
                baseline_tag=baseline_tag,
                status=status_filter,
            )

        if route == "/show-debug-bundle-panel-release-workflow" and method == "GET":
            workflow_path = query_params.get("workflow_path", [None])[0]
            if not workflow_path:
                raise ApiError(HTTPStatus.BAD_REQUEST, "workflow_path is required")
            return HTTPStatus.OK, load_debug_bundle_regression_panel_release_workflow(workflow_path)

        if route == "/save-debug-bundle-panel-baseline" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_name = self._require_string(payload, "baseline_name")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            baseline_notes = payload.get("baseline_notes")
            if baseline_notes is not None and not isinstance(baseline_notes, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_notes must be a string")
            baseline_tags = payload.get("baseline_tags")
            if baseline_tags is not None and (
                not isinstance(baseline_tags, list) or any(not isinstance(tag, str) for tag in baseline_tags)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_tags must be a list of strings")
            return HTTPStatus.OK, save_debug_bundle_regression_panel_baseline(
                panel_path,
                baseline_name,
                baseline_dir=baseline_dir,
                baseline_notes=baseline_notes,
                baseline_tags=baseline_tags,
            )

        if route == "/promote-debug-bundle-panel-baseline" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_name = self._require_string(payload, "baseline_name")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            baseline_notes = payload.get("baseline_notes")
            if baseline_notes is not None and not isinstance(baseline_notes, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_notes must be a string")
            baseline_tags = payload.get("baseline_tags")
            if baseline_tags is not None and (
                not isinstance(baseline_tags, list) or any(not isinstance(tag, str) for tag in baseline_tags)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_tags must be a list of strings")
            require_threshold_pass = bool(payload.get("require_threshold_pass", False))
            gate_baseline_tag = payload.get("gate_baseline_tag")
            if gate_baseline_tag is not None and not isinstance(gate_baseline_tag, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "gate_baseline_tag must be a string")
            blocked_latest_verdicts = payload.get("blocked_latest_verdicts")
            if blocked_latest_verdicts is not None and (
                not isinstance(blocked_latest_verdicts, list) or any(not isinstance(item, str) for item in blocked_latest_verdicts)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "blocked_latest_verdicts must be a list of strings")
            if require_threshold_pass or blocked_latest_verdicts:
                try:
                    result = guarded_promote_debug_bundle_regression_panel_baseline(
                        panel_path,
                        baseline_name,
                        baseline_dir=baseline_dir,
                        baseline_notes=baseline_notes,
                        baseline_tags=baseline_tags,
                        gate_baseline_tag=gate_baseline_tag,
                        require_threshold_pass=require_threshold_pass,
                        blocked_latest_verdicts=blocked_latest_verdicts,
                    )
                except ValueError as exc:
                    raise ApiError(HTTPStatus.BAD_REQUEST, str(exc)) from exc
                return HTTPStatus.OK, result
            return HTTPStatus.OK, promote_debug_bundle_regression_panel_baseline(
                panel_path,
                baseline_name,
                baseline_dir=baseline_dir,
                baseline_notes=baseline_notes,
                baseline_tags=baseline_tags,
            )

        if route == "/evaluate-debug-bundle-panel-promotion-gate" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            baseline_tag = payload.get("baseline_tag")
            if baseline_tag is not None and not isinstance(baseline_tag, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_tag must be a string")
            require_threshold_pass = bool(payload.get("require_threshold_pass", False))
            blocked_latest_verdicts = payload.get("blocked_latest_verdicts")
            if blocked_latest_verdicts is not None and (
                not isinstance(blocked_latest_verdicts, list) or any(not isinstance(item, str) for item in blocked_latest_verdicts)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "blocked_latest_verdicts must be a list of strings")
            return HTTPStatus.OK, evaluate_debug_bundle_regression_panel_promotion_gate(
                panel_path,
                baseline_dir=baseline_dir,
                baseline_tag=baseline_tag,
                require_threshold_pass=require_threshold_pass,
                blocked_latest_verdicts=blocked_latest_verdicts,
            )

        if route == "/run-debug-bundle-panel-release-workflow" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_name = self._require_string(payload, "baseline_name")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            baseline_notes = payload.get("baseline_notes")
            if baseline_notes is not None and not isinstance(baseline_notes, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_notes must be a string")
            baseline_tags = payload.get("baseline_tags")
            if baseline_tags is not None and (
                not isinstance(baseline_tags, list) or any(not isinstance(tag, str) for tag in baseline_tags)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_tags must be a list of strings")
            gate_baseline_tag = payload.get("gate_baseline_tag")
            if gate_baseline_tag is not None and not isinstance(gate_baseline_tag, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "gate_baseline_tag must be a string")
            require_threshold_pass = bool(payload.get("require_threshold_pass", False))
            blocked_latest_verdicts = payload.get("blocked_latest_verdicts")
            if blocked_latest_verdicts is not None and (
                not isinstance(blocked_latest_verdicts, list) or any(not isinstance(item, str) for item in blocked_latest_verdicts)
            ):
                raise ApiError(HTTPStatus.BAD_REQUEST, "blocked_latest_verdicts must be a list of strings")
            auto_promote = bool(payload.get("auto_promote", True))
            archive_dir = payload.get("archive_dir")
            if archive_dir is not None and not isinstance(archive_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "archive_dir must be a string")
            return HTTPStatus.OK, run_debug_bundle_regression_panel_release_workflow(
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

        if route == "/compare-debug-bundle-panel-release-workflows" and method == "POST":
            payload = self._parse_json_body(body)
            before_path = self._require_string(payload, "before_path")
            after_path = self._require_string(payload, "after_path")
            return HTTPStatus.OK, compare_debug_bundle_regression_panel_release_workflows(before_path, after_path)

        if route == "/compare-debug-bundle-panel-baseline" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_name = self._require_string(payload, "baseline_name")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            return HTTPStatus.OK, compare_debug_bundle_regression_panel_baseline(
                panel_path,
                baseline_name,
                baseline_dir=baseline_dir,
            )

        if route == "/compare-debug-bundle-panel-latest-baseline" and method == "POST":
            payload = self._parse_json_body(body)
            panel_path = self._require_string(payload, "panel_path")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            baseline_tag = payload.get("baseline_tag")
            if baseline_tag is not None and not isinstance(baseline_tag, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_tag must be a string")
            return HTTPStatus.OK, compare_debug_bundle_regression_panel_latest_baseline(
                panel_path,
                baseline_dir=baseline_dir,
                baseline_tag=baseline_tag,
            )

        if route == "/delete-debug-bundle-panel-baseline" and method == "POST":
            payload = self._parse_json_body(body)
            baseline_name = self._require_string(payload, "baseline_name")
            baseline_dir = payload.get("baseline_dir")
            if baseline_dir is not None and not isinstance(baseline_dir, str):
                raise ApiError(HTTPStatus.BAD_REQUEST, "baseline_dir must be a string")
            return HTTPStatus.OK, delete_debug_bundle_regression_panel_baseline(
                baseline_name,
                baseline_dir=baseline_dir,
            )

        if route in {"/query", "/evidence", "/ask", "/answer", "/agent/chat", "/agent/analyze", "/client-log", "/debug-bundle", "/compare-debug-bundles", "/compare-debug-bundle-panel", "/compare-debug-bundle-panels", "/save-debug-bundle-panel-baseline", "/promote-debug-bundle-panel-baseline", "/evaluate-debug-bundle-panel-promotion-gate", "/run-debug-bundle-panel-release-workflow", "/compare-debug-bundle-panel-release-workflows", "/compare-debug-bundle-panel-baseline", "/compare-debug-bundle-panel-latest-baseline", "/delete-debug-bundle-panel-baseline"} and method != "POST":
            raise ApiError(HTTPStatus.METHOD_NOT_ALLOWED, f"{route} only supports POST")

        if route in {"/agent/providers", "/list-debug-bundle-panel-baselines", "/show-debug-bundle-panel-baseline", "/show-debug-bundle-panel-baseline-trend", "/list-debug-bundle-panel-release-workflows", "/show-debug-bundle-panel-release-workflow", "/docs"} and method != "GET":
            raise ApiError(HTTPStatus.METHOD_NOT_ALLOWED, f"{route} only supports GET")

        raise ApiError(HTTPStatus.NOT_FOUND, f"Unknown route: {route}")

    def _resolve_db_path(self, explicit_db_path: str | None) -> str:
        db_path = explicit_db_path or self.default_db_path
        if not db_path:
            raise ApiError(HTTPStatus.BAD_REQUEST, "db_path is required")
        return db_path

    def _resolve_optional_db_path(
        self,
        explicit_db_path: object,
        default_db_path: str | None,
        key: str,
    ) -> str | None:
        if explicit_db_path is not None and not isinstance(explicit_db_path, str):
            raise ApiError(HTTPStatus.BAD_REQUEST, f"{key} must be a string")
        db_path = explicit_db_path or default_db_path
        if isinstance(db_path, str) and db_path.strip():
            return db_path.strip()
        return None

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
            self._write_common_headers(content_type="application/json; charset=utf-8", content_length=0)
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            return

        def _dispatch(self) -> None:
            trace_id = new_trace_id()
            started_at = time.perf_counter()
            static_asset = None
            if self.command == "GET":
                static_asset = _resolve_web_response(self.path)
            if static_asset is not None:
                status_code, content_type, payload = static_asset
                self.send_response(int(status_code))
                self._write_common_headers(content_type=content_type, content_length=len(payload))
                self.end_headers()
                self.wfile.write(payload)
                return

            body = None
            if self.command == "POST":
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length) if length > 0 else b""

            request_payload = _decode_request_body(body)
            error_payload = None
            try:
                status_code, payload = api.handle_request(self.command, self.path, body)
            except ApiError as exc:
                status_code = exc.status_code
                payload = {"error": exc.message}
                error_payload = {"type": "ApiError", "message": exc.message}
                log_error(
                    event="api_error",
                    message=exc.message,
                    trace_id=trace_id,
                    exc=exc,
                    context={"method": self.command, "path": self.path, "status_code": int(status_code)},
                )
            except Exception as exc:  # pragma: no cover
                status_code = HTTPStatus.INTERNAL_SERVER_ERROR
                payload = {"error": str(exc)}
                error_payload = {"type": exc.__class__.__name__, "message": str(exc)}
                log_error(
                    event="unhandled_api_error",
                    message=str(exc),
                    trace_id=trace_id,
                    exc=exc,
                    context={"method": self.command, "path": self.path, "status_code": int(status_code)},
                )

            encoded = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(int(status_code))
            self.send_header("X-Trace-Id", trace_id)
            self._write_common_headers(content_type="application/json; charset=utf-8", content_length=len(encoded))
            self.end_headers()
            self.wfile.write(encoded)
            elapsed_ms = (time.perf_counter() - started_at) * 1000.0
            log_request(
                trace_id=trace_id,
                method=self.command,
                path=self.path,
                status_code=int(status_code),
                elapsed_ms=elapsed_ms,
                request_payload=request_payload,
                response_payload=payload,
                client_ip=self.client_address[0] if self.client_address else None,
                user_agent=self.headers.get("User-Agent"),
                error=error_payload,
            )
            _log_business_route(
                trace_id=trace_id,
                method=self.command,
                path=self.path,
                status_code=int(status_code),
                elapsed_ms=elapsed_ms,
                request_payload=request_payload,
                response_payload=payload,
            )

        def _write_common_headers(self, *, content_type: str, content_length: int) -> None:
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(content_length))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Cache-Control", "no-store, max-age=0")

    return ApiHandler


def _decode_request_body(body: bytes | None) -> object:
    if not body:
        return None
    try:
        return json.loads(body.decode("utf-8"))
    except Exception:
        return {"raw_body": body.decode("utf-8", errors="replace")}


def _log_business_route(
    *,
    trace_id: str,
    method: str,
    path: str,
    status_code: int,
    elapsed_ms: float,
    request_payload: object,
    response_payload: object,
) -> None:
    route = urlparse(path).path
    if route in {"/health", "/docs"} or route.startswith("/docs/"):
        return
    if route == "/client-log":
        return
    request_dict = request_payload if isinstance(request_payload, dict) else {}
    response_dict = response_payload if isinstance(response_payload, dict) else {}
    event = {
        "/db-summary": "db_summary",
        "/query": "query_codebase",
        "/evidence": "assemble_evidence",
        "/ask": "ask_codebase",
        "/answer": "answer_codebase",
        "/agent/providers": "list_agent_providers",
        "/agent/chat": "agent_chat",
        "/debug-bundle": "debug_bundle",
        "/compare-debug-bundles": "compare_debug_bundles",
        "/compare-debug-bundle-panel": "compare_debug_bundle_panel",
        "/compare-debug-bundle-panels": "compare_debug_bundle_panels",
    }.get(route, route.strip("/").replace("-", "_") or "api_call")
    log_business(
        event,
        trace_id=trace_id,
        method=method,
        route=route,
        status_code=status_code,
        elapsed_ms=round(float(elapsed_ms), 3),
        db_path=request_dict.get("db_path") or request_dict.get("before_db_path") or request_dict.get("after_db_path"),
        query=request_dict.get("query") or request_dict.get("question") or request_dict.get("message"),
        options={
            key: request_dict.get(key)
            for key in ("limit", "context_window", "related_limit", "provider", "include_retrieval", "include_evidence", "include_answer_draft")
            if key in request_dict
        },
        result=sanitize_payload(
            {
                "response_kind": response_dict.get("response_kind"),
                "hit_count": response_dict.get("hit_count"),
                "evidence_count": response_dict.get("evidence_count"),
                "candidate_count": response_dict.get("candidate_count"),
                "answer_source": response_dict.get("answer_source"),
                "error": response_dict.get("error"),
            }
        ),
    )


def _coerce_int(value: Any, field_name: str) -> int:
    try:
        coerced = int(value)
    except (TypeError, ValueError) as exc:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be an integer") from exc
    if coerced <= 0:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be greater than 0")
    return coerced


def _optional_int(value: Any, field_name: str) -> int | None:
    if value is None:
        return None
    return _coerce_int(value, field_name)


def _optional_nonnegative_int(value: Any, field_name: str) -> int | None:
    if value is None:
        return None
    try:
        coerced = int(value)
    except (TypeError, ValueError) as exc:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be an integer") from exc
    if coerced < 0:
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be greater than or equal to 0")
    return coerced


def _coerce_named_int_mapping(value: Any, field_name: str) -> dict[str, int] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} must be an object")
    result: dict[str, int] = {}
    for key, raw_value in value.items():
        if not isinstance(key, str) or not key.strip():
            raise ApiError(HTTPStatus.BAD_REQUEST, f"{field_name} keys must be non-empty strings")
        result[key.strip()] = _optional_nonnegative_int(raw_value, f"{field_name}.{key}") or 0
    return result


def _resolve_web_response(path: str) -> tuple[int, str, bytes] | None:
    parsed = urlparse(path)
    route = parsed.path
    if route in {"", "/", "/ui"}:
        return _read_static_file(WEB_INDEX_PATH)
    if route == "/favicon.ico":
        return HTTPStatus.NO_CONTENT, "image/x-icon", b""
    asset_path = WEB_ASSET_PATHS.get(route)
    if asset_path is not None:
        return _read_static_file(asset_path)
    if route.startswith("/assets/fonts/"):
        font_name = route[len("/assets/fonts/"):]
        if ".." in font_name or "/" in font_name:
            return None
        font_path = WEB_DIR / "fonts" / font_name
        if font_path.exists():
            return _read_static_file(font_path)
    return None


def _read_static_file(path: Path) -> tuple[int, str, bytes]:
    if not path.exists():
        return HTTPStatus.NOT_FOUND, "text/plain; charset=utf-8", f"Not found: {path.name}".encode("utf-8")
    payload = path.read_bytes()
    content_type, _ = mimetypes.guess_type(path.name)
    if content_type is None:
        content_type = "application/octet-stream"
    if content_type.startswith("text/") or content_type in {"application/javascript", "application/json"}:
        content_type = f"{content_type}; charset=utf-8"
    return HTTPStatus.OK, content_type, payload
