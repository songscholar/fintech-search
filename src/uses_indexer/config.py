from __future__ import annotations

import os
from pathlib import Path


PROJECT_ENV_FILE_NAME = ".env"
_DOTENV_CACHE: set[str] = set()


def bootstrap_env(start_dir: str | Path | None = None, *, override: bool = False) -> str | None:
    explicit = os.getenv("USES_INDEXER_ENV_FILE")
    candidate = Path(explicit).expanduser() if explicit else _discover_env_file(start_dir)
    if candidate is None or not candidate.exists():
        return None

    cache_key = f"{candidate.resolve()}::{override}"
    if cache_key in _DOTENV_CACHE:
        return str(candidate)

    load_dotenv(candidate, override=override)
    _DOTENV_CACHE.add(cache_key)
    return str(candidate)


def load_dotenv(path: str | Path, *, override: bool = False) -> None:
    env_path = Path(path).expanduser()
    if not env_path.exists():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export ") :].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        name = key.strip()
        if not name:
            continue
        parsed = _parse_env_value(value.strip())
        if override or name not in os.environ:
            os.environ[name] = parsed


def _discover_env_file(start_dir: str | Path | None) -> Path | None:
    current = Path(start_dir or Path.cwd()).expanduser().resolve()
    for candidate_dir in (current, *current.parents):
        candidate = candidate_dir / PROJECT_ENV_FILE_NAME
        if candidate.exists():
            return candidate
    return None


def _parse_env_value(raw: str) -> str:
    if not raw:
        return ""
    if raw[:1] == raw[-1:] and raw[:1] in {"'", '"'} and len(raw) >= 2:
        unwrapped = raw[1:-1]
        if raw.startswith('"'):
            return bytes(unwrapped, "utf-8").decode("unicode_escape")
        return unwrapped

    comment_index = raw.find(" #")
    if comment_index >= 0:
        raw = raw[:comment_index]
    return raw.strip()
