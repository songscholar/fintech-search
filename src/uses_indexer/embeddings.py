from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass


TOKEN_RE = re.compile(r"[\u4e00-\u9fff]+|[A-Za-z0-9_]+")


@dataclass(slots=True)
class EmbeddingInfo:
    provider: str
    model: str
    dimension: int


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
