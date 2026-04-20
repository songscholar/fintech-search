from __future__ import annotations

import os
from pathlib import Path

from uses_indexer.constants import (
    JSON_RPC_VERSION,
    MCP_PROTOCOL_VERSION,
    READ_ACTIONS,
    VECTOR_SIMILARITY_THRESHOLD,
)
from uses_indexer.embeddings import OpenAICompatibleEmbedder
from uses_indexer.llm import OpenAICompatibleLlm


def test_embedder_can_bootstrap_from_dotenv(monkeypatch, tmp_path: Path) -> None:
    env_path = tmp_path / ".env"
    env_path.write_text(
        "\n".join(
            [
                "USES_INDEXER_EMBEDDING_API_KEY=test-key",
                "USES_INDEXER_EMBEDDING_MODEL=text-embedding-3-large",
                "USES_INDEXER_EMBEDDING_BATCH_SIZE=7",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("USES_INDEXER_EMBEDDING_API_KEY", raising=False)
    monkeypatch.delenv("USES_INDEXER_EMBEDDING_MODEL", raising=False)
    monkeypatch.delenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", raising=False)
    monkeypatch.delenv("USES_INDEXER_ENV_FILE", raising=False)

    try:
        embedder = OpenAICompatibleEmbedder.from_env()

        assert embedder is not None
        assert embedder.config.api_key == "test-key"
        assert embedder.config.model == "text-embedding-3-large"
        assert embedder.config.batch_size == 7
    finally:
        for name in (
            "USES_INDEXER_EMBEDDING_API_KEY",
            "USES_INDEXER_EMBEDDING_MODEL",
            "USES_INDEXER_EMBEDDING_BATCH_SIZE",
        ):
            os.environ.pop(name, None)


def test_llm_can_bootstrap_from_dotenv(monkeypatch, tmp_path: Path) -> None:
    env_path = tmp_path / ".env"
    env_path.write_text(
        "\n".join(
            [
                "USES_INDEXER_LLM_API_KEY=test-key",
                "USES_INDEXER_LLM_MODEL=gpt-4.1-mini",
                "USES_INDEXER_LLM_MAX_TOKENS=900",
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("USES_INDEXER_LLM_API_KEY", raising=False)
    monkeypatch.delenv("USES_INDEXER_LLM_MODEL", raising=False)
    monkeypatch.delenv("USES_INDEXER_LLM_MAX_TOKENS", raising=False)
    monkeypatch.delenv("USES_INDEXER_ENV_FILE", raising=False)

    try:
        llm = OpenAICompatibleLlm.from_env()

        assert llm.is_configured() is True
        assert llm.config is not None
        assert llm.config.api_key == "test-key"
        assert llm.config.model == "gpt-4.1-mini"
        assert llm.config.max_tokens == 900
    finally:
        for name in (
            "USES_INDEXER_LLM_API_KEY",
            "USES_INDEXER_LLM_MODEL",
            "USES_INDEXER_LLM_MAX_TOKENS",
        ):
            os.environ.pop(name, None)


def test_runtime_constants_are_centralized() -> None:
    assert "获取记录" in READ_ACTIONS
    assert VECTOR_SIMILARITY_THRESHOLD == 0.05
    assert JSON_RPC_VERSION == "2.0"
    assert MCP_PROTOCOL_VERSION == "2025-11-25"
