from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any
from urllib import error, request


class LlmConfigError(Exception):
    pass


class LlmRequestError(Exception):
    pass


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


class OpenAICompatibleLlm:
    def __init__(self, config: OpenAICompatibleConfig | None = None) -> None:
        self.config = config

    @classmethod
    def from_env(cls) -> "OpenAICompatibleLlm":
        provider = os.getenv("USES_INDEXER_LLM_PROVIDER", "openai-compatible").strip() or "openai-compatible"
        api_key = os.getenv("USES_INDEXER_LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
        model = os.getenv("USES_INDEXER_LLM_MODEL")
        base_url = os.getenv("USES_INDEXER_LLM_BASE_URL", "https://api.openai.com/v1/chat/completions")
        temperature = float(os.getenv("USES_INDEXER_LLM_TEMPERATURE", "0.1"))
        max_tokens = int(os.getenv("USES_INDEXER_LLM_MAX_TOKENS", "1200"))
        timeout_seconds = float(os.getenv("USES_INDEXER_LLM_TIMEOUT", "60"))
        max_retries = int(os.getenv("USES_INDEXER_LLM_MAX_RETRIES", "0"))
        retry_backoff_seconds = float(os.getenv("USES_INDEXER_LLM_RETRY_BACKOFF", "1.0"))

        if not api_key or not model:
            return cls(None)
        if provider != "openai-compatible":
            raise LlmConfigError(f"Unsupported USES_INDEXER_LLM_PROVIDER: {provider}")

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
                provider=provider,
            )
        )

    def is_configured(self) -> bool:
        return self.config is not None

    def complete(self, *, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        if not self.config:
            raise LlmConfigError(
                "LLM is not configured. Set USES_INDEXER_LLM_API_KEY and USES_INDEXER_LLM_MODEL."
            )

        payload = {
            "model": self.config.model,
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        }

        http_request = request.Request(
            self.config.base_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}",
            },
            method="POST",
        )

        raw = self._perform_request(http_request)

        parsed = json.loads(raw)
        content = _extract_content(parsed)
        if not content:
            raise LlmRequestError("LLM response did not contain assistant content")

        return {
            "provider": self.config.provider,
            "model": self.config.model,
            "base_url": self.config.base_url,
            "content": content,
            "raw_response": parsed,
        }

    def _perform_request(self, http_request: request.Request) -> str:
        if not self.config:
            raise LlmConfigError("LLM is not configured.")

        attempts = self.config.max_retries + 1
        last_error: Exception | None = None
        for attempt in range(1, attempts + 1):
            try:
                with request.urlopen(http_request, timeout=self.config.timeout_seconds) as response:
                    return response.read().decode("utf-8")
            except error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")
                last_error = LlmRequestError(f"LLM request failed with status {exc.code}: {detail}")
            except error.URLError as exc:
                last_error = LlmRequestError(f"LLM request failed: {exc.reason}")
            except TimeoutError as exc:
                last_error = LlmRequestError(f"LLM request timed out: {exc}")

            if attempt < attempts:
                time.sleep(self.config.retry_backoff_seconds * attempt)

        if last_error is not None:
            raise last_error
        raise LlmRequestError("LLM request failed for an unknown reason")


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
                text_parts.append(item["text"])
        return "\n".join(part.strip() for part in text_parts if part.strip())

    return ""
