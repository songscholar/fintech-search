from __future__ import annotations

import json

from uses_indexer.embeddings import (
    EmbeddingConfigError,
    LocalHashedEmbedder,
    OpenAICompatibleEmbedder,
    create_embedder_from_env,
)


def test_create_embedder_from_env_defaults_to_local_hash(monkeypatch) -> None:
    monkeypatch.delenv("USES_INDEXER_EMBEDDING_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("USES_INDEXER_EMBEDDING_MODEL", raising=False)

    embedder = create_embedder_from_env()

    assert isinstance(embedder, LocalHashedEmbedder)
    assert embedder.info.provider == "local-hash"


def test_create_embedder_from_env_uses_openai_compatible_config(monkeypatch) -> None:
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_DIMENSIONS", "1024")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "8")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BASE_URL", "https://example.test/v1/embeddings")

    embedder = create_embedder_from_env()

    assert isinstance(embedder, OpenAICompatibleEmbedder)
    assert embedder.info.provider == "openai-compatible"
    assert embedder.info.model == "text-embedding-3-large"
    assert embedder.info.dimension == 1024
    assert embedder.config.batch_size == 8
    assert embedder.config.base_url == "https://example.test/v1/embeddings"


def test_openai_compatible_embedder_batches_requests(monkeypatch) -> None:
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "1")

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

    def fake_urlopen(req, timeout: int = 60):  # type: ignore[no-untyped-def]
        body = json.loads(req.data.decode("utf-8"))
        payloads.append(body)
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
    assert vectors == [[1.0, 3.0], [1.0, 6.0]]
    assert embedder.info.dimension == 2


def test_create_embedder_from_env_rejects_invalid_batch_size(monkeypatch) -> None:
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_API_KEY", "test-key")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_MODEL", "text-embedding-3-large")
    monkeypatch.setenv("USES_INDEXER_EMBEDDING_BATCH_SIZE", "0")

    try:
        create_embedder_from_env()
    except EmbeddingConfigError as exc:
        assert "USES_INDEXER_EMBEDDING_BATCH_SIZE" in str(exc)
    else:
        raise AssertionError("Expected EmbeddingConfigError")
