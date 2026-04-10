from __future__ import annotations

import hashlib
import json
import math
import os
import re
from dataclasses import dataclass
from typing import Protocol
from urllib import error, request


TOKEN_RE = re.compile(r"[\u4e00-\u9fff]+|[A-Za-z0-9_]+")


class EmbeddingConfigError(Exception):
    pass


class EmbeddingRequestError(Exception):
    pass


@dataclass(slots=True)
class EmbeddingInfo:
    provider: str
    model: str
    dimension: int


class Embedder(Protocol):
    @property
    def info(self) -> EmbeddingInfo:
        ...

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        ...


class LocalHashedEmbedder:
    def __init__(self, dimension: int = 256) -> None:
        self.dimension = dimension

    @property
    def info(self) -> EmbeddingInfo:
        return EmbeddingInfo(
            provider="local-hash",
            model=f"local-hash-{self.dimension}",
            dimension=self.dimension,
        )

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        return [self._embed_one(text) for text in texts]

    def _embed_one(self, text: str) -> list[float]:
        vector = [0.0] * self.dimension
        for feature, weight in _iter_features(text):
            digest = hashlib.md5(feature.encode("utf-8")).digest()
            bucket = int.from_bytes(digest[:4], "little") % self.dimension
            sign = 1.0 if digest[4] % 2 == 0 else -1.0
            vector[bucket] += sign * weight

        norm = math.sqrt(sum(value * value for value in vector))
        if norm <= 1e-12:
            return vector
        return [value / norm for value in vector]


@dataclass(slots=True)
class OpenAICompatibleEmbeddingConfig:
    api_key: str
    model: str
    base_url: str = "https://api.openai.com/v1/embeddings"
    batch_size: int = 32
    dimensions: int | None = None
    timeout_seconds: float = 60.0


class OpenAICompatibleEmbedder:
    def __init__(self, config: OpenAICompatibleEmbeddingConfig) -> None:
        self.config = config
        self._dimension: int | None = config.dimensions

    @classmethod
    def from_env(cls) -> "OpenAICompatibleEmbedder | None":
        api_key = (
            os.getenv("USES_INDEXER_EMBEDDING_API_KEY")
            or os.getenv("OPENAI_EMBEDDING_KEY")
            or os.getenv("OPENAI_API_KEY")
        )
        model = (
            os.getenv("USES_INDEXER_EMBEDDING_MODEL")
            or os.getenv("OPENAI_EMBEDDING_NAME")
            or os.getenv("OPENAI_EMBEDDING_MODEL")
        )
        if not api_key or not model:
            return None

        base_url = _normalize_embedding_base_url(
            os.getenv("USES_INDEXER_EMBEDDING_BASE_URL")
            or os.getenv("OPENAI_EMBEDDING_URL")
            or "https://api.openai.com/v1/embeddings"
        )
        batch_size = _parse_positive_int_env(
            "USES_INDEXER_EMBEDDING_BATCH_SIZE",
            default=32,
            aliases=("OPENAI_EMBEDDING_BATCH_SIZE",),
        )
        dimensions = _parse_positive_int_env(
            "USES_INDEXER_EMBEDDING_DIMENSIONS",
            default=None,
            aliases=("OPENAI_EMBEDDING_DIMENSIONS",),
        )
        timeout_seconds = _parse_positive_float_env(
            "USES_INDEXER_EMBEDDING_TIMEOUT",
            default=60.0,
            aliases=("OPENAI_EMBEDDING_TIMEOUT",),
        )

        return cls(
            OpenAICompatibleEmbeddingConfig(
                api_key=api_key,
                model=model,
                base_url=base_url,
                batch_size=batch_size,
                dimensions=dimensions,
                timeout_seconds=timeout_seconds,
            )
        )

    @property
    def info(self) -> EmbeddingInfo:
        return EmbeddingInfo(
            provider="openai-compatible",
            model=self.config.model,
            dimension=self._dimension or (self.config.dimensions or 0),
        )

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []

        results: list[list[float]] = []
        batch_size = max(self.config.batch_size, 1)
        for start in range(0, len(texts), batch_size):
            batch = texts[start : start + batch_size]
            results.extend(self._embed_batch(batch))
        return results

    def _embed_batch(self, texts: list[str]) -> list[list[float]]:
        payload: dict[str, object] = {
            "model": self.config.model,
            "input": texts,
        }
        if self.config.dimensions is not None:
            payload["dimensions"] = self.config.dimensions

        http_request = request.Request(
            self.config.base_url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config.api_key}",
            },
            method="POST",
        )

        try:
            with request.urlopen(http_request, timeout=self.config.timeout_seconds) as response:
                raw = response.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise EmbeddingRequestError(f"Embedding request failed with status {exc.code}: {detail}") from exc
        except error.URLError as exc:
            raise EmbeddingRequestError(f"Embedding request failed: {exc.reason}") from exc

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise EmbeddingRequestError("Embedding response was not valid JSON") from exc

        data = parsed.get("data")
        if not isinstance(data, list) or not data:
            raise EmbeddingRequestError("Embedding response did not contain data")

        vectors_by_index: dict[int, list[float]] = {}
        for item in data:
            if not isinstance(item, dict):
                continue
            index = item.get("index")
            embedding = item.get("embedding")
            if not isinstance(index, int) or not isinstance(embedding, list):
                continue
            vector = [float(value) for value in embedding]
            vectors_by_index[index] = vector
            if self._dimension is None:
                self._dimension = len(vector)

        vectors: list[list[float]] = []
        for index in range(len(texts)):
            vector = vectors_by_index.get(index)
            if vector is None:
                raise EmbeddingRequestError(f"Embedding response missing vector for index {index}")
            vectors.append(vector)
        return vectors


def create_embedder_from_env() -> Embedder:
    external = OpenAICompatibleEmbedder.from_env()
    if external is not None:
        return external
    return LocalHashedEmbedder()


def dot_similarity(left: list[float], right: list[float]) -> float:
    return sum(a * b for a, b in zip(left, right))


def _iter_features(text: str) -> list[tuple[str, float]]:
    features: list[tuple[str, float]] = []
    for raw_token in TOKEN_RE.findall(text):
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            features.extend(_chinese_features(raw_token))
            continue
        features.extend(_latin_features(raw_token.lower()))
    return features


def _chinese_features(token: str) -> list[tuple[str, float]]:
    features: list[tuple[str, float]] = [(token, 2.5)]
    max_ngram = min(len(token), 4)
    for size in range(2, max_ngram + 1):
        weight = 1.0 + (size - 2) * 0.35
        for index in range(0, len(token) - size + 1):
            features.append((token[index : index + size], weight))
    return features


def _latin_features(token: str) -> list[tuple[str, float]]:
    features: list[tuple[str, float]] = [(token, 2.0)]
    if "_" in token:
        for part in token.split("_"):
            if len(part) >= 2:
                features.append((part, 1.3))
    if len(token) >= 4:
        for index in range(0, len(token) - 2):
            features.append((token[index : index + 3], 0.8))
    return features


def _parse_positive_int_env(name: str, default: int | None, aliases: tuple[str, ...] = ()) -> int | None:
    selected_name, raw = _get_env_with_name(name, *aliases)
    if raw is None:
        return default

    try:
        value = int(raw)
    except ValueError as exc:
        raise EmbeddingConfigError(f"{selected_name} must be an integer, got {raw!r}") from exc

    if value <= 0:
        raise EmbeddingConfigError(f"{selected_name} must be greater than 0, got {value}")
    return value


def _parse_positive_float_env(name: str, default: float, aliases: tuple[str, ...] = ()) -> float:
    selected_name, raw = _get_env_with_name(name, *aliases)
    if raw is None:
        return default

    try:
        value = float(raw)
    except ValueError as exc:
        raise EmbeddingConfigError(f"{selected_name} must be a number, got {raw!r}") from exc

    if value <= 0:
        raise EmbeddingConfigError(f"{selected_name} must be greater than 0, got {value}")
    return value


def _get_env_with_name(*names: str) -> tuple[str | None, str | None]:
    for name in names:
        raw = os.getenv(name)
        if raw is not None and raw != "":
            return name, raw
    return None, None


def _normalize_embedding_base_url(raw_url: str) -> str:
    url = raw_url.strip().rstrip("/")
    if url.endswith("/embeddings"):
        return url
    return f"{url}/embeddings"
