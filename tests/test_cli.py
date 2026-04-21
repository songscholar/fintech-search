from __future__ import annotations

from pathlib import Path

from tests.test_answering import StubLlm
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.cli import _build_debug_bundle, _discover_default_db, _parse_threshold_pairs
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.qa import CodebaseQA


def test_discover_default_db_prefers_full_root_index(tmp_path: Path) -> None:
    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    full_root_db = examples_dir / "business_code_index.db"
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


def test_parse_threshold_pairs_parses_values() -> None:
    assert _parse_threshold_pairs(["1=0.8", "5=0.95"]) == {"1": 0.8, "5": 0.95}


def test_build_debug_bundle_collects_query_evidence_and_answer(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(
        """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  ]]></code>
</business:Function>
""",
        encoding="utf-8",
    )
    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm(None))

    bundle = _build_debug_bundle(
        indexer=indexer,
        answerer=answerer,
        db_path=str(db_path),
        question="证券代码获取的逻辑在哪里",
        limit=3,
        context_window=1,
        related_limit=1,
    )

    assert bundle["bundle_kind"] == "debug_bundle"
    assert bundle["query"]["response_kind"] == "query"
    assert bundle["query"]["debug"]["schema"] == "uses_indexer.debug.retrieval"
    assert bundle["evidence"]["response_kind"] == "evidence"
    assert bundle["evidence"]["debug"]["schema"] == "uses_indexer.debug.evidence"
    assert bundle["answer"]["response_kind"] == "answer"
