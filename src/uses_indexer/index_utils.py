from __future__ import annotations

import json
import re
from pathlib import Path

from .constants import CHINESE_QUERY_SPLIT_RE, GENERIC_QUERY_TERMS, QUERY_TOKEN_RE
from .embeddings import Embedder


def maybe_int(value: object) -> int | None:
    if value is None:
        return None
    return int(value)


def embedder_batch_size(embedder: Embedder) -> int:
    config = getattr(embedder, "config", None)
    raw_batch_size = getattr(config, "batch_size", 512)
    try:
        batch_size = int(raw_batch_size)
    except (TypeError, ValueError):
        return 512
    return max(batch_size, 1)


def paths_match(left: str | Path, right: str | Path) -> bool:
    try:
        return Path(left).expanduser().resolve() == Path(right).expanduser().resolve()
    except OSError:
        return str(left) == str(right)


def json_dumps(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def json_loads_object(value: str) -> dict[str, object]:
    try:
        loaded = json.loads(value)
    except json.JSONDecodeError:
        return {}
    if isinstance(loaded, dict):
        return loaded
    return {}


def dedupe_strings(values: list[str]) -> list[str]:
    return list(dict.fromkeys(value for value in values if value))


def build_fts_query(query: str) -> str | None:
    tokens = tokenize_query(query)
    if not tokens:
        return None
    return " OR ".join(f"{token}*" if len(token) > 1 else token for token in tokens)


def tokenize_query(query: str) -> list[str]:
    tokens: list[str] = []
    seen: set[str] = set()

    for raw_token in QUERY_TOKEN_RE.findall(query):
        lowered = raw_token.lower()
        if re.fullmatch(r"[\u4e00-\u9fff]+", raw_token):
            fragments = [
                fragment.strip()
                for fragment in CHINESE_QUERY_SPLIT_RE.split(raw_token)
                if len(fragment.strip()) >= 2
            ]
            if not fragments:
                fragments = [raw_token]
            for fragment in fragments:
                if fragment in GENERIC_QUERY_TERMS:
                    continue
                if fragment not in seen:
                    seen.add(fragment)
                    tokens.append(fragment)
            continue

        if lowered not in seen:
            seen.add(lowered)
            tokens.append(lowered)

    return tokens


def merge_candidate(
    store: dict[tuple[object, ...], dict[str, object]],
    candidate: dict[str, object],
) -> None:
    key = (
        candidate["hit_type"],
        candidate["entity_id"],
        candidate["statement_id"],
        candidate["procedure_id"],
        candidate["matched_text"],
    )
    existing = store.get(key)
    if existing is None:
        candidate["matched_via"] = [candidate["retrieval_source"]]
        store[key] = candidate
        return

    matched_via = list(existing.get("matched_via", []))
    retrieval_source = str(candidate["retrieval_source"])
    if retrieval_source not in matched_via:
        matched_via.append(retrieval_source)
    existing["matched_via"] = matched_via

    if float(candidate["base_score"]) > float(existing["base_score"]):
        for field in ("matched_text", "match_source", "retrieval_source", "base_score", "source_rank"):
            existing[field] = candidate[field]

    search_text = str(existing.get("search_text") or "")
    incoming = str(candidate.get("search_text") or "")
    if incoming and incoming not in search_text:
        existing["search_text"] = f"{search_text}\n{incoming}".strip()
