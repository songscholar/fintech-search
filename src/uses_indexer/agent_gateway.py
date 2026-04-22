from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any
from urllib import error, request

from .config import bootstrap_env
from .qa import CodebaseQA
from .indexer import SQLiteIndexer


class AgentConfigError(Exception):
    pass


class AgentRequestError(Exception):
    pass


@dataclass(slots=True)
class AgentProviderConfig:
    name: str
    label: str
    adapter: str
    base_url: str
    model: str
    api_key: str | None = None
    temperature: float = 0.1
    max_tokens: int = 1600
    timeout_seconds: float = 90.0
    max_retries: int = 0
    retry_backoff_seconds: float = 1.0
    description: str = ""


class AgentGateway:
    def __init__(
        self,
        *,
        indexer: SQLiteIndexer,
        qa: CodebaseQA,
        providers: dict[str, AgentProviderConfig] | None = None,
        default_provider: str | None = None,
    ) -> None:
        self.indexer = indexer
        self.qa = qa
        self.providers = providers or {}
        self.default_provider = default_provider or next(iter(self.providers.keys()), None)

    @classmethod
    def from_env(cls, *, indexer: SQLiteIndexer, qa: CodebaseQA) -> "AgentGateway":
        bootstrap_env()
        providers: dict[str, AgentProviderConfig] = {}
        for prefix, name, label, description in (
            ("USES_INDEXER_AGENT_OPENAI", "openai-compatible", "通用智能体", "适合对接任意 OpenAI-compatible 聊天服务"),
            ("USES_INDEXER_AGENT_HERMES", "hermes", "Hermes", "适合挂接你自己部署的 Hermes 服务"),
            ("USES_INDEXER_AGENT_OPENCLAW", "openclaw", "OpenClaw", "适合挂接你自己部署的 OpenClaw 服务"),
        ):
            config = _provider_from_env(prefix=prefix, name=name, label=label, description=description)
            if config is not None:
                providers[name] = config

        default_provider = os.getenv("USES_INDEXER_AGENT_DEFAULT_PROVIDER", "").strip() or None
        if default_provider and default_provider not in providers:
            default_provider = next(iter(providers.keys()), None)
        if default_provider is None:
            default_provider = next(iter(providers.keys()), None)

        return cls(indexer=indexer, qa=qa, providers=providers, default_provider=default_provider)

    def list_providers(self) -> dict[str, Any]:
        items = [
            {
                "name": config.name,
                "label": config.label,
                "adapter": config.adapter,
                "configured": True,
                "default": config.name == self.default_provider,
                "description": config.description,
                "model": config.model,
                "base_url": config.base_url,
            }
            for config in self.providers.values()
        ]
        return {
            "response_kind": "agent_providers",
            "default_provider": self.default_provider,
            "count": len(items),
            "items": items,
        }

    def chat(
        self,
        *,
        db_path: str,
        message: str,
        provider_name: str | None = None,
        history: list[dict[str, str]] | None = None,
        include_retrieval: bool = True,
        include_evidence: bool = True,
        include_answer_draft: bool = False,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
        system_prompt: str | None = None,
    ) -> dict[str, Any]:
        config = self._resolve_provider(provider_name)
        context_bundle = self._build_context(
            db_path=db_path,
            message=message,
            include_retrieval=include_retrieval,
            include_evidence=include_evidence,
            include_answer_draft=include_answer_draft,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
        )

        messages: list[dict[str, str]] = [
            {
                "role": "system",
                "content": system_prompt.strip() if isinstance(system_prompt, str) and system_prompt.strip() else _default_system_prompt(),
            }
        ]
        if history:
            messages.extend(_sanitize_history(history))
        messages.append(
            {
                "role": "user",
                "content": _build_user_prompt(message=message, context_bundle=context_bundle),
            }
        )

        started_at = time.time()
        model_response = _complete_openai_compatible(config, messages)
        latency_ms = int((time.time() - started_at) * 1000)

        return {
            "response_kind": "agent_chat",
            "provider": {
                "name": config.name,
                "label": config.label,
                "adapter": config.adapter,
                "model": config.model,
                "base_url": config.base_url,
            },
            "message": message,
            "reply": model_response["content"],
            "latency_ms": latency_ms,
            "context_bundle": context_bundle,
            "usage": model_response.get("usage"),
            "raw_response": model_response["raw_response"],
        }

    def _resolve_provider(self, provider_name: str | None) -> AgentProviderConfig:
        target = provider_name or self.default_provider
        if not target:
            raise AgentConfigError(
                "No agent provider is configured. Set USES_INDEXER_AGENT_OPENAI_* or USES_INDEXER_AGENT_HERMES_* / USES_INDEXER_AGENT_OPENCLAW_*."
            )
        config = self.providers.get(target)
        if config is None:
            available = ", ".join(sorted(self.providers.keys())) or "none"
            raise AgentConfigError(f"Unknown agent provider: {target}. Available providers: {available}")
        return config

    def _build_context(
        self,
        *,
        db_path: str,
        message: str,
        include_retrieval: bool,
        include_evidence: bool,
        include_answer_draft: bool,
        limit: int,
        context_window: int,
        related_limit: int,
    ) -> dict[str, Any]:
        bundle: dict[str, Any] = {
            "db_path": db_path,
            "question": message,
            "options": {
                "include_retrieval": include_retrieval,
                "include_evidence": include_evidence,
                "include_answer_draft": include_answer_draft,
                "limit": limit,
                "context_window": context_window,
                "related_limit": related_limit,
            },
        }
        if include_retrieval:
            query = self.indexer.query_index(db_path, message, limit=limit, debug=True)
            bundle["retrieval"] = {
                "hit_count": query.get("hit_count", 0),
                "candidate_count": query.get("candidate_count", 0),
                "hits": [
                    {
                        "procedure_name": hit.get("procedure_name"),
                        "file_path": hit.get("file_path"),
                        "retrieval_source": hit.get("retrieval_source") or hit.get("match_source"),
                        "matched_text": hit.get("matched_text") or hit.get("excerpt"),
                    }
                    for hit in (query.get("hits") or [])[: min(limit, 6)]
                ],
                "query_analysis": query.get("debug", {}).get("query_analysis"),
            }
        if include_evidence:
            evidence = self.indexer.assemble_evidence(
                db_path,
                message,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
                debug=True,
            )
            bundle["evidence"] = {
                "evidence_count": evidence.get("evidence_count", 0),
                "items": [
                    {
                        "procedure_name": item.get("procedure_name"),
                        "file_path": item.get("file_path"),
                        "line_start": item.get("line_start"),
                        "matched_text": item.get("matched_text") or item.get("excerpt"),
                        "related_tables": item.get("related_tables"),
                        "related_calls": item.get("related_calls"),
                    }
                    for item in (evidence.get("evidence") or [])[: min(limit, 4)]
                ],
                "pruning": evidence.get("debug", {}).get("pruning"),
            }
        if include_answer_draft:
            ask = self.qa.ask(
                db_path,
                message,
                evidence_limit=limit,
                context_window=context_window,
                related_limit=related_limit,
            )
            bundle["answer_draft"] = {
                "status": ask.get("draft_answer", {}).get("status"),
                "text": ask.get("draft_answer", {}).get("text"),
            }
        return bundle


def _provider_from_env(*, prefix: str, name: str, label: str, description: str) -> AgentProviderConfig | None:
    enabled_value = os.getenv(f"{prefix}_ENABLED")
    if enabled_value is not None and enabled_value.strip().lower() in {"0", "false", "no", "off"}:
        return None

    model = (os.getenv(f"{prefix}_MODEL") or "").strip()
    base_url = (os.getenv(f"{prefix}_BASE_URL") or "").strip()
    adapter = (os.getenv(f"{prefix}_ADAPTER", "openai-compatible") or "openai-compatible").strip()
    if not model or not base_url:
        return None
    if adapter != "openai-compatible":
        raise AgentConfigError(f"Unsupported agent adapter for {name}: {adapter}")

    return AgentProviderConfig(
        name=name,
        label=os.getenv(f"{prefix}_LABEL", label).strip() or label,
        adapter=adapter,
        base_url=base_url,
        model=model,
        api_key=(os.getenv(f"{prefix}_API_KEY") or "").strip() or None,
        temperature=float(os.getenv(f"{prefix}_TEMPERATURE", "0.1")),
        max_tokens=int(os.getenv(f"{prefix}_MAX_TOKENS", "1600")),
        timeout_seconds=float(os.getenv(f"{prefix}_TIMEOUT", "90")),
        max_retries=int(os.getenv(f"{prefix}_MAX_RETRIES", "0")),
        retry_backoff_seconds=float(os.getenv(f"{prefix}_RETRY_BACKOFF", "1.0")),
        description=description,
    )


def _default_system_prompt() -> str:
    return (
        "你是当前 USES Indexer 控制台里的代码库智能体。"
        "回答必须优先依据给定的本地代码检索上下文，明确指出不确定点，"
        "尽量引用过程名、文件路径、证据线索来支撑结论。"
    )


def _sanitize_history(history: list[dict[str, str]]) -> list[dict[str, str]]:
    sanitized: list[dict[str, str]] = []
    for item in history[-8:]:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip()
        content = str(item.get("content") or "").strip()
        if role not in {"user", "assistant"} or not content:
            continue
        sanitized.append({"role": role, "content": content})
    return sanitized


def _build_user_prompt(*, message: str, context_bundle: dict[str, Any]) -> str:
    context_json = json.dumps(context_bundle, ensure_ascii=False, indent=2)
    return (
        "用户问题：\n"
        f"{message.strip()}\n\n"
        "本地代码库上下文（来自当前 uses-indexer 服务）:\n"
        f"{context_json}\n\n"
        "请基于这些上下文回答。如果上下文还不够，请明确指出还缺什么。"
    )


def _complete_openai_compatible(config: AgentProviderConfig, messages: list[dict[str, str]]) -> dict[str, Any]:
    payload = {
        "model": config.model,
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
        "messages": messages,
    }
    headers = {"Content-Type": "application/json"}
    if config.api_key:
        headers["Authorization"] = f"Bearer {config.api_key}"

    http_request = request.Request(
        config.base_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    raw = _perform_request(http_request, config)
    parsed = json.loads(raw)
    content = _extract_content(parsed)
    if not content:
        raise AgentRequestError("Agent response did not contain assistant content")
    return {
        "content": content,
        "usage": parsed.get("usage"),
        "raw_response": parsed,
    }


def _perform_request(http_request: request.Request, config: AgentProviderConfig) -> str:
    attempts = config.max_retries + 1
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with request.urlopen(http_request, timeout=config.timeout_seconds) as response:
                return response.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = AgentRequestError(f"Agent request failed with status {exc.code}: {detail}")
        except error.URLError as exc:
            last_error = AgentRequestError(f"Agent request failed: {exc.reason}")
        except TimeoutError as exc:
            last_error = AgentRequestError(f"Agent request timed out: {exc}")
        if attempt < attempts:
            time.sleep(config.retry_backoff_seconds * attempt)
    if last_error is not None:
        raise last_error
    raise AgentRequestError("Agent request failed for an unknown reason")


def _extract_content(payload: dict[str, Any]) -> str:
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        return ""
    first = choices[0]
    if not isinstance(first, dict):
        return ""
    message = first.get("message")
    if not isinstance(message, dict):
        return ""
    content = message.get("content")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text" and isinstance(item.get("text"), str):
                text_parts.append(item["text"].strip())
        return "\n".join(part for part in text_parts if part)
    return ""
