from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass, field
from typing import Any
from urllib import error, request

from .config import bootstrap_env
from .logging_system import log_business, log_error


class LlmConfigError(Exception):
    pass


class LlmRequestError(Exception):
    pass


# ---------------------------------------------------------------------------
# Provider config
# ---------------------------------------------------------------------------

_PROVIDER_ENV_PREFIXES: dict[str, str] = {
    "kimi": "KIMI_LLM",
    "xiaomi": "XIAOMI_LLM",
}

_PROVIDER_DEFAULT_MODELS: dict[str, str] = {
    "kimi": "kimi-k2",
    "xiaomi": "mimo-v2.5-pro",
}


@dataclass(slots=True)
class LlmProviderConfig:
    name: str
    api_key: str
    model: str
    base_url: str
    temperature: float = 0.1
    max_tokens: int = 1200
    timeout_seconds: float = 180.0
    max_retries: int = 0
    retry_backoff_seconds: float = 1.0
    user_agent: str | None = None


def _load_provider_config(name: str) -> LlmProviderConfig | None:
    """Load a single provider config from env by provider name (e.g. 'kimi')."""
    prefix = _PROVIDER_ENV_PREFIXES.get(name)
    if not prefix:
        return None

    api_key = os.getenv(f"{prefix}_API_KEY", "").strip()
    base_url = os.getenv(f"{prefix}_BASE_URL", "").strip()
    model = os.getenv(f"{prefix}_MODEL", "").strip() or _PROVIDER_DEFAULT_MODELS.get(name, "")

    if not api_key or not base_url:
        return None

    return LlmProviderConfig(
        name=name,
        api_key=api_key,
        model=model,
        base_url=base_url,
        temperature=float(os.getenv(f"{prefix}_TEMPERATURE", "0.1")),
        max_tokens=int(os.getenv(f"{prefix}_MAX_TOKENS", "1200")),
        timeout_seconds=float(os.getenv(f"{prefix}_TIMEOUT", "180")),
        max_retries=int(os.getenv(f"{prefix}_MAX_RETRIES", "0")),
        retry_backoff_seconds=float(os.getenv(f"{prefix}_RETRY_BACKOFF", "1.0")),
        user_agent=os.getenv(f"{prefix}_USER_AGENT") or None,
    )


# ---------------------------------------------------------------------------
# LlmService — unified entry point
# ---------------------------------------------------------------------------

class LlmService:
    """Unified LLM call entry point. Routes to different providers based on config."""

    def __init__(
        self,
        providers: dict[str, LlmProviderConfig],
        default_provider: str,
    ) -> None:
        self._providers = providers
        self._default_provider = default_provider

    @classmethod
    def from_env(cls, provider: str | None = None) -> "LlmService":
        bootstrap_env()
        default = provider or os.getenv("USES_INDEXER_LLM_PROVIDER", "kimi").strip() or "kimi"

        providers: dict[str, LlmProviderConfig] = {}
        for name in _PROVIDER_ENV_PREFIXES:
            cfg = _load_provider_config(name)
            if cfg is not None:
                providers[name] = cfg

        if default not in providers:
            # Fallback: pick the first available provider
            if providers:
                default = next(iter(providers))
            else:
                # No provider configured at all — return empty service
                return cls({}, default)

        return cls(providers, default)

    @property
    def default_provider(self) -> str:
        return self._default_provider

    def is_configured(self, provider: str | None = None) -> bool:
        name = provider or self._default_provider
        return name in self._providers

    def list_providers(self) -> list[dict[str, Any]]:
        return [
            {
                "name": cfg.name,
                "model": cfg.model,
                "base_url": cfg.base_url,
                "default": cfg.name == self._default_provider,
            }
            for cfg in self._providers.values()
        ]

    def get_config(self, provider: str | None = None) -> LlmProviderConfig | None:
        name = provider or self._default_provider
        return self._providers.get(name)

    def chat(
        self,
        messages: list[dict[str, Any]],
        *,
        provider: str | None = None,
        model: str | None = None,
        temperature: float | None = None,
        max_tokens: int | None = None,
        timeout: float | None = None,
        tools: list[dict[str, Any]] | None = None,
        response_format: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Unified LLM call. Returns {content, tool_calls, usage, raw_response}."""
        name = provider or self._default_provider
        cfg = self._providers.get(name)
        if cfg is None:
            raise LlmConfigError(
                f"LLM provider '{name}' is not configured. "
                f"Available: {list(self._providers.keys())}. "
                f"Set {name.upper()}_LLM_API_KEY and {name.upper()}_LLM_BASE_URL in .env."
            )

        # Apply overrides
        effective_model = model or cfg.model
        effective_temperature = temperature if temperature is not None else cfg.temperature
        effective_max_tokens = max_tokens if max_tokens is not None else cfg.max_tokens
        effective_timeout = timeout if timeout is not None else cfg.timeout_seconds
        effective_timeout = 1800000

        payload: dict[str, Any] = {
            "model": effective_model,
            "temperature": effective_temperature,
            "max_tokens": effective_max_tokens,
            "messages": messages,
        }
        if tools:
            payload["tools"] = tools
        if response_format:
            payload["response_format"] = response_format

        headers: dict[str, str] = {"Content-Type": "application/json"}
        if cfg.api_key:
            headers["Authorization"] = f"Bearer {cfg.api_key}"
        if cfg.user_agent:
            headers["User-Agent"] = cfg.user_agent

        http_request = request.Request(
            cfg.base_url,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        started_at = time.perf_counter()
        try:
            raw = _perform_request(http_request, cfg, effective_timeout)
        except Exception as exc:
            log_error(
                event="llm_request_failed",
                message=str(exc),
                exc=exc,
                context={"provider": name, "model": effective_model, "base_url": cfg.base_url},
            )
            raise

        parsed = json.loads(raw)
        content = _extract_content(parsed)
        tool_calls = _extract_tool_calls(parsed)

        if not content and not tool_calls:
            exc = LlmRequestError("LLM response did not contain assistant content or tool calls")
            log_error(
                event="llm_empty_response",
                message=str(exc),
                exc=exc,
                context={"provider": name, "model": effective_model, "base_url": cfg.base_url},
            )
            raise exc

        latency_ms = int((time.perf_counter() - started_at) * 1000)
        log_business(
            "llm_chat",
            provider=name,
            model=effective_model,
            base_url=cfg.base_url,
            latency_ms=latency_ms,
            prompt_chars=sum(len(str(m.get("content", ""))) for m in messages),
            response_chars=len(content or ""),
            has_tool_calls=bool(tool_calls),
            usage=parsed.get("usage"),
        )

        return {
            "provider": name,
            "model": effective_model,
            "base_url": cfg.base_url,
            "content": content,
            "tool_calls": tool_calls,
            "usage": parsed.get("usage"),
            "raw_response": parsed,
        }


# ---------------------------------------------------------------------------
# HTTP request with retry
# ---------------------------------------------------------------------------

def _perform_request(
    http_request: request.Request,
    cfg: LlmProviderConfig,
    timeout: float | None = None,
) -> str:
    effective_timeout = timeout if timeout is not None else cfg.timeout_seconds
    attempts = cfg.max_retries + 1
    last_error: Exception | None = None

    for attempt in range(1, attempts + 1):
        try:
            with request.urlopen(http_request, timeout=effective_timeout) as resp:
                return resp.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = LlmRequestError(f"LLM request failed with status {exc.code}: {detail}")
        except error.URLError as exc:
            last_error = LlmRequestError(f"LLM request failed: {exc.reason}")
        except TimeoutError as exc:
            last_error = LlmRequestError(f"LLM request timed out: {exc}")

        if attempt < attempts:
            time.sleep(cfg.retry_backoff_seconds * attempt)

    if last_error is not None:
        raise last_error
    raise LlmRequestError("LLM request failed for an unknown reason")


# ---------------------------------------------------------------------------
# Response parsing
# ---------------------------------------------------------------------------

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

    # Standard content field
    content = message.get("content")
    if isinstance(content, str) and content.strip():
        return content.strip()

    # Kimi-style reasoning_content fallback
    reasoning = message.get("reasoning_content")
    if isinstance(reasoning, str) and reasoning.strip():
        return reasoning.strip()

    # List-of-text-parts format
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text" and isinstance(item.get("text"), str):
                text_parts.append(item["text"])
        return "\n".join(part.strip() for part in text_parts if part.strip())

    return ""


def _extract_tool_calls(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract tool calls from OpenAI-format response."""
    choices = payload.get("choices")
    if not isinstance(choices, list) or not choices:
        return []

    first = choices[0]
    if not isinstance(first, dict):
        return []

    message = first.get("message")
    if not isinstance(message, dict):
        return []

    raw_calls = message.get("tool_calls")
    if not isinstance(raw_calls, list):
        return []

    result: list[dict[str, Any]] = []
    for tc in raw_calls:
        if not isinstance(tc, dict):
            continue
        func = tc.get("function")
        if not isinstance(func, dict):
            continue
        name = func.get("name", "")
        raw_args = func.get("arguments", "{}")
        if isinstance(raw_args, str):
            try:
                args = json.loads(raw_args)
            except (json.JSONDecodeError, TypeError):
                args = {}
        elif isinstance(raw_args, dict):
            args = raw_args
        else:
            args = {}
        result.append({
            "id": tc.get("id", ""),
            "name": name,
            "arguments": args,
        })

    return result


# ---------------------------------------------------------------------------
# Backward-compatible wrappers (deprecated)
# ---------------------------------------------------------------------------

@dataclass(slots=True)
class OpenAICompatibleConfig:
    api_key: str
    model: str
    base_url: str = "https://api.openai.com/v1/chat/completions"
    temperature: float = 0.1
    max_tokens: int = 1200
    timeout_seconds: float = 60.0
    max_retries: int = 0
    retry_backoff_seconds: float = 1.0
    provider: str = "openai-compatible"
    user_agent: str | None = None


class OpenAICompatibleLlm:
    """Deprecated: use LlmService instead."""

    def __init__(self, config: OpenAICompatibleConfig | None = None) -> None:
        self.config = config

    @classmethod
    def from_env(cls) -> "OpenAICompatibleLlm":
        bootstrap_env()
        api_key = os.getenv("USES_INDEXER_LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
        model = os.getenv("USES_INDEXER_LLM_MODEL")
        base_url = os.getenv("USES_INDEXER_LLM_BASE_URL", "https://api.openai.com/v1/chat/completions")
        temperature = float(os.getenv("USES_INDEXER_LLM_TEMPERATURE", "0.1"))
        max_tokens = int(os.getenv("USES_INDEXER_LLM_MAX_TOKENS", "1200"))
        timeout_seconds = float(os.getenv("USES_INDEXER_LLM_TIMEOUT", "60"))
        max_retries = int(os.getenv("USES_INDEXER_LLM_MAX_RETRIES", "0"))
        retry_backoff_seconds = float(os.getenv("USES_INDEXER_LLM_RETRY_BACKOFF", "1.0"))
        user_agent = os.getenv("USES_INDEXER_LLM_USER_AGENT")

        if not api_key or not model:
            return cls(None)

        return cls(
            OpenAICompatibleConfig(
                api_key=api_key,
                model=model,
                base_url=base_url,
                temperature=temperature,
                max_tokens=max_tokens,
                timeout_seconds=timeout_seconds,
                max_retries=max_retries,
                retry_backoff_seconds=retry_backoff_seconds,
                provider="openai-compatible",
                user_agent=user_agent,
            )
        )

    def is_configured(self) -> bool:
        return self.config is not None

    def complete(self, *, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        if not self.config:
            raise LlmConfigError(
                "LLM is not configured. Set USES_INDEXER_LLM_API_KEY and USES_INDEXER_LLM_MODEL."
            )

        service = LlmService(
            providers={
                self.config.provider: LlmProviderConfig(
                    name=self.config.provider,
                    api_key=self.config.api_key,
                    model=self.config.model,
                    base_url=self.config.base_url,
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                    timeout_seconds=self.config.timeout_seconds,
                    max_retries=self.config.max_retries,
                    retry_backoff_seconds=self.config.retry_backoff_seconds,
                    user_agent=self.config.user_agent,
                )
            },
            default_provider=self.config.provider,
        )

        result = service.chat(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        return {
            "provider": result["provider"],
            "model": result["model"],
            "base_url": result["base_url"],
            "content": result["content"],
            "raw_response": result["raw_response"],
        }
