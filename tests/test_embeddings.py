from __future__ import annotations

import json
from urllib import request

from uses_indexer.embeddings import (
    EmbeddingRequestError,
    EmbeddingConfigError,
    LocalHashedEmbedder,
    OpenAICompatibleEmbeddingConfig,
    OpenAICompatibleEmbedder,
    create_embedder_from_env,
)


EMBEDDING_ENV_VARS = (
    "USES_INDEXER_EMBEDDING_API_KEY",
    "USES_INDEXER_EMBEDDING_MODEL",
    "USES_INDEXER_EMBEDDING_BASE_URL",
    "USES_INDEXER_EMBEDDING_BATCH_SIZE",
    "USES_INDEXER_EMBEDDING_DIMENSIONS",
    "USES_INDEXER_EMBEDDING_TIMEOUT",
    "USES_INDEXER_EMBEDDING_CACHE_DB",
    "OPENAI_EMBEDDING_KEY",
    "OPENAI_EMBEDDING_NAME",
    "OPENAI_EMBEDDING_MODEL",
    "OPENAI_EMBEDDING_URL",
    "OPENAI_EMBEDDING_BATCH_SIZE",
    "OPENAI_EMBEDDING_DIMENSIONS",
    "OPENAI_EMBEDDING_TIMEOUT",
    "OPENAI_EMBEDDING_CACHE_DB",
    "OPENAI_API_KEY",
)


def clear_embedding_env(monkeypatch) -> None:
    for name in EMBEDDING_ENV_VARS:
        monkeypatch.delenv(name, raising=False)


def test_create_embedder_from_env_defaults_to_local_hash(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)

    embedder = create_embedder_from_env()

    assert isinstance(embedder, LocalHashedEmbedder)
    assert embedder.info.provider == "local-hash"


def test_create_embedder_from_env_uses_openai_compatible_config(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_DIMENSIONS", "1024")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "8")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BASE_URL", "https://example.test/v1/embeddings")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_TIMEOUT", "30")

    embedder = create_embedder_from_env()

    assert isinstance(embedder, OpenAICompatibleEmbedder)
    assert embedder.info.provider == "openai-compatible"
    assert embedder.info.model == "text-embedding-3-large"
    assert embedder.info.dimension == 1024
    assert embedder.config.batch_size == 8
    assert embedder.config.base_url == "https://example.test/v1/embeddings"
    assert embedder.config.timeout_seconds == 30.0


def test_create_embedder_from_env_accepts_openai_embedding_aliases(monkeypatch, tmp_path) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("OPENAI_EMBEDDING_KEY", "test-key")
    monkeypatch.setenv("OPENAI_EMBEDDING_NAME", "text-embedding-3-large")
    monkeypatch.setenv("OPENAI_EMBEDDING_URL", "https://example.test/v1")
    monkeypatch.setenv("OPENAI_EMBEDDING_BATCH_SIZE", "16")
    monkeypatch.setenv("OPENAI_EMBEDDING_DIMENSIONS", "3072")
    monkeypatch.setenv("OPENAI_EMBEDDING_TIMEOUT", "12.5")
    monkeypatch.setenv("OPENAI_EMBEDDING_CACHE_DB", str(tmp_path / "embedding-cache.db"))

    embedder = create_embedder_from_env()

    assert isinstance(embedder, OpenAICompatibleEmbedder)
    assert embedder.info.model == "text-embedding-3-large"
    assert embedder.info.dimension == 3072
    assert embedder.config.base_url == "https://example.test/v1/embeddings"
    assert embedder.config.batch_size == 16
    assert embedder.config.timeout_seconds == 12.5
    assert embedder.config.cache_db_path == str(tmp_path / "embedding-cache.db")


def test_openai_compatible_embedder_batches_requests(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "1")

    payloads: list[dict[str, object]] = []
    timeouts: list[float] = []

    class FakeResponse:
        def __init__(self, payload: dict[str, object]) -> None:
            self._payload = payload

        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, exc_type, exc, tb) -> None:
            return None

        def read(self) -> bytes:
            return json.dumps(self._payload).encode("utf-8")

    def fake_urlopen(req, timeout: float = 60.0):  # type: ignore[no-untyped-def]
        body = json.loads(req.data.decode("utf-8"))
        payloads.append(body)
        timeouts.append(timeout)
        inputs = body["input"]
        return FakeResponse(
            {
                "data": [
                    {"index": index, "embedding": [float(index + 1), float(len(text))]}
                    for index, text in enumerate(inputs)
                ]
            }
        )

    monkeypatch.setattr("uses_indexer.embeddings.request.urlopen", fake_urlopen)

    embedder = create_embedder_from_env()
    vectors = embedder.embed_texts(["abc", "abcdef"])

    assert isinstance(embedder, OpenAICompatibleEmbedder)
    assert len(payloads) == 2
    assert payloads[0]["input"] == ["abc"]
    assert payloads[1]["input"] == ["abcdef"]
    assert timeouts == [60.0, 60.0]
    assert vectors == [[1.0, 3.0], [1.0, 6.0]]
    assert embedder.info.dimension == 2


def test_create_embedder_from_env_rejects_invalid_batch_size(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "0")

    try:
        create_embedder_from_env()
    except EmbeddingConfigError as exc:
        assert "USES_INDEXER_EMBEDDING_BATCH_SIZE" in str(exc)
    else:
        raise AssertionError("Expected EmbeddingConfigError")


def test_create_embedder_from_env_rejects_invalid_timeout_alias(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("OPENAI_EMBEDDING_KEY", "test-key")
    monkeypatch.setenv("OPENAI_EMBEDDING_NAME", "text-embedding-3-large")
    monkeypatch.setenv("OPENAI_EMBEDDING_TIMEOUT", "nope")

    try:
        create_embedder_from_env()
    except EmbeddingConfigError as exc:
        assert "OPENAI_EMBEDDING_TIMEOUT" in str(exc)
    else:
        raise AssertionError("Expected EmbeddingConfigError")


def test_openai_compatible_embedder_reuses_sqlite_cache(monkeypatch, tmp_path) -> None:
    clear_embedding_env(monkeypatch)
    monkeypatch.setenv("OPENAI_EMBEDDING_KEY", "test-key")
    monkeypatch.setenv("OPENAI_EMBEDDING_NAME", "text-embedding-3-large")
    monkeypatch.setenv("OPENAI_EMBEDDING_CACHE_DB", str(tmp_path / "embedding-cache.db"))

    payloads: list[dict[str, object]] = []

    class FakeResponse:
        def __init__(self, payload: dict[str, object]) -> None:
            self._payload = payload

        def __enter__(self) -> "FakeResponse":
            return self

        def __exit__(self, exc_type, exc, tb) -> None:
            return None

        def read(self) -> bytes:
            return json.dumps(self._payload).encode("utf-8")

    def fake_urlopen(req, timeout: float = 60.0):  # type: ignore[no-untyped-def]
        body = json.loads(req.data.decode("utf-8"))
        payloads.append(body)
        inputs = body["input"]
        return FakeResponse(
            {
                "data": [
                    {"index": index, "embedding": [float(len(text)), float(index + 1)]}
                    for index, text in enumerate(inputs)
                ]
            }
        )

    monkeypatch.setattr("uses_indexer.embeddings.request.urlopen", fake_urlopen)

    first_embedder = create_embedder_from_env()
    first_vectors = first_embedder.embed_texts(["abc", "abcdef"])

    second_embedder = create_embedder_from_env()
    second_vectors = second_embedder.embed_texts(["abc", "abcdef"])

    assert first_vectors == [[3.0, 1.0], [6.0, 2.0]]
    assert second_vectors == first_vectors
    assert len(payloads) == 1
    assert payloads[0]["input"] == ["abc", "abcdef"]
    assert first_embedder.info.dimension == 2
    assert second_embedder.info.dimension == 2


def test_openai_compatible_embedder_wraps_read_timeout(monkeypatch) -> None:
    clear_embedding_env(monkeypatch)

    class TimeoutResponse:
        def __enter__(self) -> "TimeoutResponse":
            return self

        def __exit__(self, exc_type, exc, tb) -> None:
            return None

        def read(self) -> bytes:
            raise TimeoutError("timed out")

    def fake_urlopen(req: request.Request, timeout: float = 60.0) -> TimeoutResponse:
        return TimeoutResponse()

    monkeypatch.setattr("uses_indexer.embeddings.request.urlopen", fake_urlopen)

    embedder = OpenAICompatibleEmbedder(
        OpenAICompatibleEmbeddingConfig(
            api_key="test-key",
            model="text-embedding-3-large",
            timeout_seconds=1.5,
        )
    )

    try:
        embedder.embed_texts(["abc"])
    except EmbeddingRequestError as exc:
        assert "timed out" in str(exc)
    else:
        raise AssertionError("Expected EmbeddingRequestError")
