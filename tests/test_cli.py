from __future__ import annotations

from pathlib import Path

from uses_indexer.cli import _discover_default_db


def test_discover_default_db_prefers_full_root_index(tmp_path: Path) -> None:
    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    full_root_db = examples_dir / "agent_code_index.db"
    subset_db = examples_dir / "uses_codes_index.db"
    full_root_db.write_text("", encoding="utf-8")
    subset_db.write_text("", encoding="utf-8")

    assert _discover_default_db(tmp_path) == str(full_root_db)


def test_discover_default_db_falls_back_to_subset_index(tmp_path: Path) -> None:
    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    subset_db = examples_dir / "uses_codes_index.db"
    subset_db.write_text("", encoding="utf-8")

    assert _discover_default_db(tmp_path) == str(subset_db)


def test_discover_default_db_returns_none_when_missing(tmp_path: Path) -> None:
    assert _discover_default_db(tmp_path) is None
