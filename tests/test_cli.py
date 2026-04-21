from __future__ import annotations

import json
from pathlib import Path

from tests.test_answering import StubLlm
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.cli import _discover_default_db, _parse_scoped_threshold_pairs, _parse_threshold_pairs
from uses_indexer.debug_bundle import (
    DebugBundlePanelThresholds,
    build_debug_bundle,
    build_debug_bundle_regression_panel,
    evaluate_debug_bundle_regression_panel_promotion_gate,
    run_debug_bundle_regression_panel_release_workflow,
    compare_debug_bundle_regression_panel_latest_baseline,
    compare_debug_bundle_regression_panel_baseline,
    compare_debug_bundle_regression_panels,
    compare_debug_bundles,
    delete_debug_bundle_regression_panel_baseline,
    evaluate_debug_bundle_regression_panel_thresholds,
    guarded_promote_debug_bundle_regression_panel_baseline,
    load_debug_bundle_regression_panel_baseline,
    load_debug_bundle_regression_panel_release_workflow,
    list_debug_bundle_regression_panel_baselines,
    list_debug_bundle_regression_panel_release_workflows,
    promote_debug_bundle_regression_panel_baseline,
    save_debug_bundle_regression_panel_baseline,
    summarize_debug_bundle_regression_panel_baseline_trend,
    write_debug_bundle_archive,
)
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


def test_parse_scoped_threshold_pairs_parses_values() -> None:
    assert _parse_scoped_threshold_pairs(["variable:5=1.0", "callers:3=0.8"]) == {
        "variable": {"5": 1.0},
        "callers": {"3": 0.8},
    }


def test_parse_named_int_pairs_parses_values() -> None:
    from uses_indexer.cli import _parse_named_int_pairs

    assert _parse_named_int_pairs(["possible_regression=0", "retrieval=2"]) == {
        "possible_regression": 0,
        "retrieval": 2,
    }


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

    bundle = build_debug_bundle(
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

    archive = write_debug_bundle_archive(bundle, tmp_path / "bundle_archive")
    assert Path(archive["files"]["bundle"]).exists()
    assert Path(archive["files"]["summary"]).exists()
    assert Path(archive["files"]["query"]).exists()
    assert Path(archive["files"]["evidence"]).exists()
    assert Path(archive["files"]["answer"]).exists()
    summary = json.loads(Path(archive["files"]["summary"]).read_text(encoding="utf-8"))
    assert summary["bundle_kind"] == "debug_bundle_summary"
    assert summary["question"] == "证券代码获取的逻辑在哪里"
    assert summary["response_kinds"]["query"] == "query"


def test_compare_debug_bundles_reports_differences(tmp_path: Path) -> None:
    before_bundle = {
        "db_path": "/tmp/before.db",
        "question": "证券代码获取的逻辑在哪里",
        "bundle_kind": "debug_bundle",
        "query": {
            "hit_count": 1,
            "candidate_count": 2,
            "hits": [
                {
                    "rank": 1,
                    "procedure_name": "AF_BEFORE",
                    "file_path": "/tmp/AF_BEFORE.uftatomfunction",
                    "line_start": 10,
                    "line_end": 12,
                    "match_source": "fts_chunk",
                    "retrieval_source": "fts_chunk",
                    "matched_text": "before hit",
                }
            ],
            "debug": {"query_analysis": {"query_type": "callers"}, "metadata": {"trace_id": "trace-before"}},
        },
        "evidence": {
            "evidence_count": 1,
            "evidence": [
                {
                    "rank": 1,
                    "procedure_name": "AF_BEFORE",
                    "file_path": "/tmp/AF_BEFORE.uftatomfunction",
                    "line_start": 10,
                    "line_end": 12,
                    "matched_text": "before evidence",
                }
            ],
            "debug": {"metadata": {"trace_id": "evidence-before"}},
        },
        "answer": {
            "answer_source": "draft",
            "draft_answer": {"text": "before draft"},
            "final_answer": {"text": "before final"},
        },
    }
    after_bundle = {
        "db_path": "/tmp/after.db",
        "question": "证券代码获取的逻辑在哪里",
        "bundle_kind": "debug_bundle",
        "query": {
            "hit_count": 2,
            "candidate_count": 4,
            "hits": [
                {
                    "rank": 1,
                    "procedure_name": "AF_AFTER",
                    "file_path": "/tmp/AF_AFTER.uftatomfunction",
                    "line_start": 20,
                    "line_end": 24,
                    "match_source": "relation_procedure_feature",
                    "retrieval_source": "relation_procedure_feature",
                    "matched_text": "after hit",
                }
            ],
            "debug": {"query_analysis": {"query_type": "callers"}, "metadata": {"trace_id": "trace-after"}},
        },
        "evidence": {
            "evidence_count": 2,
            "evidence": [
                {
                    "rank": 1,
                    "procedure_name": "AF_AFTER",
                    "file_path": "/tmp/AF_AFTER.uftatomfunction",
                    "line_start": 20,
                    "line_end": 24,
                    "matched_text": "after evidence",
                }
            ],
            "debug": {"metadata": {"trace_id": "evidence-after"}},
        },
        "answer": {
            "answer_source": "llm",
            "draft_answer": {"text": "after draft"},
            "final_answer": {"text": "after final"},
        },
    }

    before_path = tmp_path / "before_bundle.json"
    after_dir = tmp_path / "after_archive"
    before_path.write_text(json.dumps(before_bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    write_debug_bundle_archive(after_bundle, after_dir)

    comparison = compare_debug_bundles(before_path, after_dir)

    assert comparison["bundle_kind"] == "debug_bundle_comparison"
    assert comparison["review_summary"]["verdict"] == "behavior_changed"
    assert comparison["review_summary"]["focus_area"] == "retrieval"
    assert comparison["markdown_summary"].startswith("# Debug Bundle Comparison")
    assert comparison["summary"]["query_hit_count"]["delta"] == 1
    assert comparison["summary"]["candidate_count"]["delta"] == 2
    assert comparison["summary"]["answer_source"]["changed"] is True
    assert comparison["query"]["top_hit_changed"] is True
    assert comparison["evidence"]["top_evidence_changed"] is True
    assert comparison["answer"]["final_answer_changed"] is True
    assert "db_path_changed" in comparison["warnings"]


def test_build_debug_bundle_regression_panel_summarizes_cases(tmp_path: Path) -> None:
    before_src = tmp_path / "before_src"
    after_src = tmp_path / "after_src"
    before_src.mkdir()
    after_src.mkdir()
    sample_xml = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  ]]></code>
</business:Function>
"""
    changed_xml = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  ]]></code>
</business:Function>
"""
    (before_src / "AF_SAMPLE.uftatomfunction").write_text(sample_xml, encoding="utf-8")
    (after_src / "AF_SAMPLE.uftatomfunction").write_text(changed_xml, encoding="utf-8")

    before_db = tmp_path / "before.db"
    after_db = tmp_path / "after.db"
    indexer = SQLiteIndexer()
    indexer.build_index(before_src, before_db)
    indexer.build_index(after_src, after_db)

    cases_path = tmp_path / "panel_cases.json"
    cases_path.write_text(
        json.dumps(
            {
                "cases": [
                    {
                        "id": "stock-code",
                        "question": "证券代码获取的逻辑在哪里",
                        "tags": ["call_chain"],
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm(None))

    panel = build_debug_bundle_regression_panel(
        indexer=indexer,
        answerer=answerer,
        before_db_path=str(before_db),
        after_db_path=str(after_db),
        cases_path=cases_path,
        limit=3,
        context_window=1,
        related_limit=1,
        archive_dir=tmp_path / "panel_archive",
    )

    assert panel["bundle_kind"] == "debug_bundle_regression_panel"
    assert panel["case_count"] == 1
    assert panel["summary"]["changed_case_count"] == 1
    assert panel["summary"]["verdict_counts"]["behavior_changed"] == 1
    assert sum(panel["summary"]["priority_counts"].values()) == 1
    assert panel["archive_manifest"][0]["case_id"] == "stock-code"
    assert panel["markdown_summary"].startswith("# Debug Bundle Regression Panel")

    threshold_report = evaluate_debug_bundle_regression_panel_thresholds(
        panel,
        DebugBundlePanelThresholds(
            max_changed_cases=0,
            max_high_priority_cases=1,
            max_verdict_counts={"behavior_changed": 0},
            max_focus_area_counts={"retrieval": 0},
        ),
    )
    assert threshold_report["status"] == "fail"
    assert threshold_report["failed_count"] >= 2


def test_compare_debug_bundle_regression_panels_reports_panel_deltas(tmp_path: Path) -> None:
    before_panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/before.db",
        "after_db_path": "/tmp/before.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 2,
        "summary": {
            "changed_case_count": 1,
            "stable_case_count": 1,
            "verdict_counts": {"behavior_changed": 1, "stable": 1},
            "priority_counts": {"medium": 1, "low": 1},
            "focus_area_counts": {"retrieval": 1, "stable": 1},
            "high_priority_cases": [],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "behavior_changed", "priority": "medium", "focus_area": "retrieval"}},
            {"case_id": "c2", "question_text": "q2", "review_summary": {"verdict": "stable", "priority": "low", "focus_area": "stable"}},
        ],
    }
    after_panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/after.db",
        "after_db_path": "/tmp/after.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 2,
        "summary": {
            "changed_case_count": 2,
            "stable_case_count": 0,
            "verdict_counts": {"possible_regression": 1, "behavior_changed": 1},
            "priority_counts": {"high": 1, "medium": 1},
            "focus_area_counts": {"retrieval": 2},
            "high_priority_cases": [{"case_id": "c1", "question": "q1", "verdict": "possible_regression", "focus_area": "retrieval"}],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "possible_regression", "priority": "high", "focus_area": "retrieval"}},
            {"case_id": "c2", "question_text": "q2", "review_summary": {"verdict": "behavior_changed", "priority": "medium", "focus_area": "retrieval"}},
        ],
    }
    before_dir = tmp_path / "before_panel"
    after_dir = tmp_path / "after_panel"
    before_dir.mkdir()
    after_dir.mkdir()
    (before_dir / "panel.json").write_text(json.dumps(before_panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (after_dir / "panel.json").write_text(json.dumps(after_panel, ensure_ascii=False, indent=2), encoding="utf-8")

    comparison = compare_debug_bundle_regression_panels(before_dir, after_dir)

    assert comparison["bundle_kind"] == "debug_bundle_regression_panel_comparison"
    assert comparison["summary"]["changed_case_count"]["delta"] == 1
    assert comparison["summary"]["verdict_counts_delta"]["possible_regression"] == 1
    assert comparison["review_summary"]["verdict"] == "possible_regression"
    assert comparison["markdown_summary"].startswith("# Debug Bundle Regression Panel Comparison")


def test_save_list_and_compare_debug_bundle_panel_baselines(tmp_path: Path) -> None:
    before_panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/before.db",
        "after_db_path": "/tmp/before.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {
            "changed_case_count": 0,
            "stable_case_count": 1,
            "verdict_counts": {"stable": 1},
            "priority_counts": {"low": 1},
            "focus_area_counts": {"stable": 1},
            "high_priority_cases": [],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "stable", "priority": "low", "focus_area": "stable"}},
        ],
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    after_panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/after.db",
        "after_db_path": "/tmp/after.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {
            "changed_case_count": 1,
            "stable_case_count": 0,
            "verdict_counts": {"possible_regression": 1},
            "priority_counts": {"high": 1},
            "focus_area_counts": {"retrieval": 1},
            "high_priority_cases": [{"case_id": "c1", "question": "q1", "verdict": "possible_regression", "focus_area": "retrieval"}],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "possible_regression", "priority": "high", "focus_area": "retrieval"}},
        ],
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    panel_dir = tmp_path / "panel_archive"
    baseline_dir = tmp_path / "baseline_store"
    panel_dir.mkdir()
    (panel_dir / "panel.json").write_text(json.dumps(before_panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_dir / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
    (panel_dir / "panel_summary.json").write_text(json.dumps({"summary": before_panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    saved = save_debug_bundle_regression_panel_baseline(panel_dir, "release candidate", baseline_dir=baseline_dir)
    assert saved["baseline_slug"] == "release-candidate"
    assert Path(saved["files"]["baseline"]).exists()

    listed = list_debug_bundle_regression_panel_baselines(baseline_dir=baseline_dir)
    assert listed["count"] == 1
    assert listed["items"][0]["baseline_name"] == "release candidate"

    current_dir = tmp_path / "current_panel"
    current_dir.mkdir()
    (current_dir / "panel.json").write_text(json.dumps(after_panel, ensure_ascii=False, indent=2), encoding="utf-8")

    comparison = compare_debug_bundle_regression_panel_baseline(current_dir, "release candidate", baseline_dir=baseline_dir)
    assert comparison["bundle_kind"] == "debug_bundle_regression_panel_comparison"
    assert comparison["baseline"]["baseline_slug"] == "release-candidate"
    assert comparison["review_summary"]["verdict"] == "possible_regression"


def test_baseline_metadata_latest_compare_and_delete(tmp_path: Path) -> None:
    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/a.db",
        "after_db_path": "/tmp/b.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {
            "changed_case_count": 0,
            "stable_case_count": 1,
            "verdict_counts": {"stable": 1},
            "priority_counts": {"low": 1},
            "focus_area_counts": {"stable": 1},
            "high_priority_cases": [],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "stable", "priority": "low", "focus_area": "stable"}},
        ],
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    panel_dir = tmp_path / "panel_archive"
    baseline_dir = tmp_path / "baseline_store"
    current_dir = tmp_path / "current_panel"
    panel_dir.mkdir()
    current_dir.mkdir()
    for target in (panel_dir, current_dir):
        (target / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
        (target / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
        (target / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    saved = save_debug_bundle_regression_panel_baseline(
        panel_dir,
        "nightly stable",
        baseline_dir=baseline_dir,
        baseline_notes="nightly smoke baseline",
        baseline_tags=["nightly", "smoke"],
    )
    assert saved["baseline_tags"] == ["nightly", "smoke"]

    listed = list_debug_bundle_regression_panel_baselines(baseline_dir=baseline_dir, baseline_tag="nightly")
    assert listed["count"] == 1
    assert listed["items"][0]["baseline_notes"] == "nightly smoke baseline"

    loaded = load_debug_bundle_regression_panel_baseline("nightly stable", baseline_dir=baseline_dir)
    assert loaded["baseline_notes"] == "nightly smoke baseline"
    assert loaded["baseline_tags"] == ["nightly", "smoke"]

    latest_comparison = compare_debug_bundle_regression_panel_latest_baseline(
        current_dir,
        baseline_dir=baseline_dir,
        baseline_tag="nightly",
    )
    assert latest_comparison["baseline"]["selection"] == "latest"
    assert latest_comparison["baseline"]["baseline_slug"] == "nightly-stable"

    deleted = delete_debug_bundle_regression_panel_baseline("nightly stable", baseline_dir=baseline_dir)
    assert deleted["deleted"] is True
    assert not (baseline_dir / "nightly-stable").exists()


def test_baseline_trend_summarizes_tagged_history(tmp_path: Path) -> None:
    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/a.db",
        "after_db_path": "/tmp/b.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {
            "changed_case_count": 0,
            "stable_case_count": 1,
            "verdict_counts": {"stable": 1},
            "priority_counts": {"low": 1},
            "focus_area_counts": {"stable": 1},
            "high_priority_cases": [],
        },
        "cases": [
            {"case_id": "c1", "question_text": "q1", "review_summary": {"verdict": "stable", "priority": "low", "focus_area": "stable"}},
        ],
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    baseline_dir = tmp_path / "baseline_store"
    first_dir = tmp_path / "panel_one"
    second_dir = tmp_path / "panel_two"
    for target, changed_count in ((first_dir, 0), (second_dir, 2)):
        payload = dict(panel)
        payload["summary"] = dict(panel["summary"])
        payload["summary"]["changed_case_count"] = changed_count
        payload["summary"]["verdict_counts"] = {"possible_regression": changed_count} if changed_count else {"stable": 1}
        target.mkdir()
        (target / "panel.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        (target / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
        (target / "panel_summary.json").write_text(json.dumps({"summary": payload["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    save_debug_bundle_regression_panel_baseline(first_dir, "release-1", baseline_dir=baseline_dir, baseline_tags=["release"])
    save_debug_bundle_regression_panel_baseline(second_dir, "release-2", baseline_dir=baseline_dir, baseline_tags=["release"])

    trend = summarize_debug_bundle_regression_panel_baseline_trend(baseline_dir=baseline_dir, baseline_tag="release")
    assert trend["bundle_kind"] == "debug_bundle_regression_panel_baseline_trend"
    assert trend["baseline_count"] == 2
    assert trend["latest"]["baseline_slug"] == "release-2"
    assert trend["summary"]["overall_changed_case_delta"]["delta"] == 2
    assert trend["markdown_summary"].startswith("# Debug Bundle Panel Baseline Trend")


def test_promote_baseline_records_promotion_source(tmp_path: Path) -> None:
    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/a.db",
        "after_db_path": "/tmp/b.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {
            "changed_case_count": 0,
            "stable_case_count": 1,
            "verdict_counts": {"stable": 1},
            "priority_counts": {"low": 1},
            "focus_area_counts": {"stable": 1},
            "high_priority_cases": [],
        },
        "cases": [],
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    panel_dir = tmp_path / "panel_archive"
    baseline_dir = tmp_path / "baseline_store"
    panel_dir.mkdir()
    (panel_dir / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_dir / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
    (panel_dir / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    promoted = promote_debug_bundle_regression_panel_baseline(
        panel_dir,
        "release-active",
        baseline_dir=baseline_dir,
        baseline_notes="promoted after gate pass",
        baseline_tags=["release", "active"],
    )
    assert promoted["bundle_kind"] == "debug_bundle_regression_panel_baseline_promoted"
    assert promoted["promotion_source"] == str(panel_dir)
    assert promoted["baseline_tags"] == ["active", "release"]


def test_promotion_gate_blocks_missing_threshold_pass(tmp_path: Path) -> None:
    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/a.db",
        "after_db_path": "/tmp/b.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {"changed_case_count": 0, "stable_case_count": 1},
        "cases": [],
        "thresholds": {"status": "fail", "failed_count": 1, "checks": []},
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    panel_dir = tmp_path / "panel_archive"
    panel_dir.mkdir()
    (panel_dir / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_dir / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
    (panel_dir / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    gate = evaluate_debug_bundle_regression_panel_promotion_gate(
        panel_dir,
        require_threshold_pass=True,
    )
    assert gate["status"] == "fail"
    assert gate["failed_count"] == 1

    try:
        guarded_promote_debug_bundle_regression_panel_baseline(
            panel_dir,
            "blocked baseline",
            baseline_dir=tmp_path / "baseline_store",
            require_threshold_pass=True,
        )
    except ValueError as exc:
        assert "Promotion gate failed" in str(exc)
    else:
        raise AssertionError("guarded promote should fail when threshold gate does not pass")


def test_release_workflow_promotes_when_gate_passes(tmp_path: Path) -> None:
    panel = {
        "bundle_kind": "debug_bundle_regression_panel",
        "before_db_path": "/tmp/a.db",
        "after_db_path": "/tmp/b.db",
        "cases_path": "/tmp/cases.json",
        "case_count": 1,
        "summary": {"changed_case_count": 0, "stable_case_count": 1},
        "cases": [],
        "thresholds": {"status": "pass", "failed_count": 0, "checks": []},
        "markdown_summary": "# Debug Bundle Regression Panel\n",
    }
    panel_dir = tmp_path / "panel_archive"
    baseline_dir = tmp_path / "baseline_store"
    panel_dir.mkdir()
    (panel_dir / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_dir / "panel.md").write_text("# Debug Bundle Regression Panel\n", encoding="utf-8")
    (panel_dir / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    workflow = run_debug_bundle_regression_panel_release_workflow(
        panel_dir,
        "release-candidate",
        baseline_dir=baseline_dir,
        baseline_notes="workflow promote",
        baseline_tags=["release"],
        gate_baseline_tag="release",
        require_threshold_pass=True,
        blocked_latest_verdicts=["possible_regression"],
        auto_promote=True,
        archive_dir=tmp_path / "workflow_archive",
    )
    assert workflow["bundle_kind"] == "debug_bundle_regression_panel_release_workflow"
    assert workflow["status"] == "promoted"
    assert workflow["promoted"]["baseline_slug"] == "release-candidate"
    assert workflow["markdown_summary"].startswith("# Debug Bundle Panel Release Workflow")
    assert Path(workflow["archive"]["files"]["workflow"]).exists()
    assert Path(workflow["archive"]["files"]["gate"]).exists()

    listed = list_debug_bundle_regression_panel_release_workflows(
        workflow_dir=tmp_path / "workflow_archive_root",
        baseline_tag="release",
        status="promoted",
    )
    assert listed["count"] == 0

    archived_workflow = run_debug_bundle_regression_panel_release_workflow(
        panel_dir,
        "release-candidate-archived",
        baseline_dir=baseline_dir,
        baseline_notes="workflow promote archived",
        baseline_tags=["release"],
        gate_baseline_tag="release",
        require_threshold_pass=True,
        blocked_latest_verdicts=["possible_regression"],
        auto_promote=True,
        archive_dir=tmp_path / "workflow_archive_root" / "release_candidate_archived",
    )
    listed = list_debug_bundle_regression_panel_release_workflows(
        workflow_dir=tmp_path / "workflow_archive_root",
        baseline_tag="release",
        status="promoted",
    )
    assert listed["count"] == 1
    loaded = load_debug_bundle_regression_panel_release_workflow(
        tmp_path / "workflow_archive_root" / "release_candidate_archived"
    )
    assert loaded["status"] == "promoted"
    assert loaded["baseline_name"] == archived_workflow["baseline_name"]
