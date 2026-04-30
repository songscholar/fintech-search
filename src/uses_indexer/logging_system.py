from __future__ import annotations

import json
import os
import platform
import socket
import sys
import threading
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


LOG_SCHEMA_VERSION = "1.0"
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_LOG_ROOT = _PROJECT_ROOT / "log"
_LOCK = threading.Lock()
_REDACTED = "[REDACTED]"
_TRUNCATED = "[TRUNCATED]"
_SENSITIVE_KEYWORDS = (
    "api_key",
    "apikey",
    "authorization",
    "auth",
    "token",
    "secret",
    "password",
    "passwd",
    "credential",
    "cookie",
    "set-cookie",
    "data_url",
    "base64",
)


def new_trace_id() -> str:
    return str(uuid4())


def log_request(
    *,
    trace_id: str,
    method: str,
    path: str,
    status_code: int,
    elapsed_ms: float,
    request_payload: Any = None,
    response_payload: Any = None,
    client_ip: str | None = None,
    user_agent: str | None = None,
    error: Any = None,
) -> None:
    _write(
        "requests",
        {
            "event": "http_request",
            "trace_id": trace_id,
            "method": method,
            "path": path,
            "status_code": int(status_code),
            "elapsed_ms": round(float(elapsed_ms), 3),
            "client_ip": client_ip,
            "user_agent": user_agent,
            "request": sanitize_payload(request_payload),
            "response": summarize_response(response_payload),
            "error": sanitize_payload(error) if error else None,
        },
    )


def log_error(
    *,
    event: str,
    message: str,
    trace_id: str | None = None,
    exc: BaseException | None = None,
    context: dict[str, Any] | None = None,
) -> None:
    payload: dict[str, Any] = {
        "event": event,
        "trace_id": trace_id,
        "message": message,
        "context": sanitize_payload(context or {}),
    }
    if exc is not None:
        payload["exception"] = {
            "type": exc.__class__.__name__,
            "message": str(exc),
            "traceback": traceback.format_exception(type(exc), exc, exc.__traceback__),
        }
    _write("errors", payload)


def log_system(event: str, **fields: Any) -> None:
    _write(
        "system",
        {
            "event": event,
            "process": {
                "pid": os.getpid(),
                "python": sys.version.split()[0],
                "platform": platform.platform(),
                "hostname": socket.gethostname(),
            },
            **sanitize_mapping(fields),
        },
    )


def log_business(event: str, *, trace_id: str | None = None, **fields: Any) -> None:
    _write(
        "business",
        {
            "event": event,
            "trace_id": trace_id,
            **sanitize_mapping(fields),
        },
    )


def log_sql_event(event: str, *, trace_id: str | None = None, **fields: Any) -> None:
    _write(
        "sql",
        {
            "event": event,
            "trace_id": trace_id,
            **sanitize_mapping(fields),
        },
    )


def sanitize_payload(value: Any, *, max_string: int | None = None, max_items: int | None = None) -> Any:
    max_string = max_string if max_string is not None else _max_string_length()
    max_items = max_items if max_items is not None else _max_collection_items()
    return _sanitize(value, max_string=max_string, max_items=max_items, depth=0)


def summarize_response(value: Any) -> Any:
    if isinstance(value, dict):
        summary = {
            "response_kind": value.get("response_kind"),
            "keys": sorted(str(key) for key in value.keys())[:40],
        }
        for key in (
            "status",
            "service",
            "hit_count",
            "evidence_count",
            "candidate_count",
            "answer_source",
            "provider",
            "model",
            "latency_ms",
        ):
            if key in value:
                summary[key] = sanitize_payload(value.get(key), max_string=600, max_items=20)
        if "final_answer" in value and isinstance(value["final_answer"], dict):
            final_answer = value["final_answer"]
            summary["final_answer"] = {
                "source": final_answer.get("source"),
                "tier": final_answer.get("tier"),
                "confidence": sanitize_payload(final_answer.get("confidence"), max_string=300, max_items=10),
                "text_excerpt": sanitize_payload(final_answer.get("text"), max_string=800, max_items=10),
            }
        if "error" in value:
            summary["error"] = sanitize_payload(value.get("error"), max_string=800, max_items=10)
        return summary
    return sanitize_payload(value, max_string=1000, max_items=20)


def sanitize_mapping(fields: dict[str, Any]) -> dict[str, Any]:
    return {str(key): sanitize_payload(value) for key, value in fields.items()}


def _sanitize(value: Any, *, max_string: int, max_items: int, depth: int) -> Any:
    if depth > 8:
        return _TRUNCATED
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, bytes):
        return f"<bytes:{len(value)}>"
    if isinstance(value, str):
        if _looks_like_large_encoded_value(value):
            return f"{_TRUNCATED}:{len(value)} chars"
        return value if len(value) <= max_string else value[:max_string] + f"...({_TRUNCATED}:{len(value)} chars)"
    if isinstance(value, dict):
        items = list(value.items())
        result: dict[str, Any] = {}
        for key, item in items[:max_items]:
            key_text = str(key)
            if _is_sensitive_key(key_text):
                result[key_text] = _REDACTED
            else:
                result[key_text] = _sanitize(item, max_string=max_string, max_items=max_items, depth=depth + 1)
        if len(items) > max_items:
            result["_truncated_items"] = len(items) - max_items
        return result
    if isinstance(value, (list, tuple, set)):
        items = list(value)
        result = [_sanitize(item, max_string=max_string, max_items=max_items, depth=depth + 1) for item in items[:max_items]]
        if len(items) > max_items:
            result.append({"_truncated_items": len(items) - max_items})
        return result
    return str(value)


def _write(category: str, payload: dict[str, Any]) -> None:
    if not _logging_enabled():
        return
    event = {
        "schema": f"uses_indexer.log.{category}",
        "schema_version": LOG_SCHEMA_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    try:
        root = _log_root()
        directory = root / category
        directory.mkdir(parents=True, exist_ok=True)
        path = directory / f"{datetime.now().strftime('%Y-%m-%d')}.jsonl"
        line = json.dumps(event, ensure_ascii=False, sort_keys=True)
        with _LOCK:
            with path.open("a", encoding="utf-8") as file:
                file.write(line)
                file.write("\n")
    except Exception:
        # Logging must never break indexing, API calls, or CLI execution.
        return


def _logging_enabled() -> bool:
    return os.getenv("USES_INDEXER_LOG_ENABLED", "1").strip().lower() not in {"0", "false", "no", "off"}


def _log_root() -> Path:
    configured = os.getenv("USES_INDEXER_LOG_DIR", "").strip()
    return Path(configured).expanduser() if configured else _DEFAULT_LOG_ROOT


def _max_string_length() -> int:
    return _int_env("USES_INDEXER_LOG_MAX_STRING", 4000)


def _max_collection_items() -> int:
    return _int_env("USES_INDEXER_LOG_MAX_ITEMS", 80)


def _int_env(name: str, default: int) -> int:
    try:
        return max(int(os.getenv(name, str(default))), 1)
    except ValueError:
        return default


def _is_sensitive_key(key: str) -> bool:
    normalized = key.replace("-", "_").lower()
    return any(keyword in normalized for keyword in _SENSITIVE_KEYWORDS)


def _looks_like_large_encoded_value(value: str) -> bool:
    if value.startswith("data:"):
        return True
    if len(value) < 1200:
        return False
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\n\r")
    sample = value[:1200]
    return sum(1 for char in sample if char in alphabet) / len(sample) > 0.95
