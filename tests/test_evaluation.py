from __future__ import annotations

import json
from pathlib import Path

from tests.test_indexer import _build_sample_index
from uses_indexer.evaluation import EvaluationThresholds, RetrievalEvaluator, compare_eval_reports, evaluate_thresholds


def test_retrieval_evaluator_reports_pass_at_k_and_recall(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)
    cases_path = tmp_path / "cases.json"
    cases_path.write_text(
        json.dumps(
            {
                "cases": [
                    {
                        "id": "variable-write",
                        "question": "@deep_flag 在哪里赋值",
                        "tags": ["variable"],
                        "expected": {
                            "procedures": ["AF_DEEP"],
                            "texts": ["@deep_flag"],
                            "line_ranges": [
                                {
                                    "path_contains": "AF_DEEP.uftatomfunction",
                                    "start": 8,
                                    "end": 10,
                                }
                            ],
                        },
                    },
                    {
                        "id": "table-write",
                        "question": "uses_deep_table 在哪里更新",
                        "tags": ["table_write"],
                        "expected": {
                            "procedures": ["AF_DEEP"],
                            "tables": ["uses_deep_table"],
                        },
                    },
                    {
                        "id": "call-chain",
                        "question": "AF_DEEP 被谁调用",
                        "tags": ["call_chain"],
                        "expected": {
                            "procedures": ["AF_SAMPLE"],
                            "texts": ["AF_DEEP"],
                        },
                    },
                    {
                        "id": "failure-flow",
                        "question": "查询失败在哪里处理",
                        "tags": ["failure"],
                        "expected": {
                            "procedures": ["AF_SAMPLE"],
                            "texts": ["处理失败"],
                        },
                    },
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    evaluator = RetrievalEvaluator(indexer)
    report = evaluator.evaluate(db_path, cases_path, limit=5, top_k=(1, 3, 5))

    assert report["case_count"] == 4
    assert report["summary"]["pass_at_k"]["5"] == 1.0
    assert report["summary"]["matched_cases"] == 4
    assert report["summary"]["evidence_coverage"] == 7 / 8
    assert report["summary"]["top_hit_expectation_coverage"] == 19 / 24
    assert report["summary"]["top_three_expectation_coverage"] == 19 / 24
    assert report["summary"]["avg_candidate_count"] >= 4.0
    assert report["summary"]["avg_evidence_count"] >= 1.0
    assert report["summary"]["avg_feature_rerank_hit_count"] >= 1.0
    assert report["summary"]["by_tag"]["variable"]["matched_cases"] == 1
    assert report["summary"]["by_tag"]["variable"]["evidence_coverage"] == 1.0
    assert report["summary"]["by_query_type"]["variable_write"]["matched_cases"] == 1
    assert report["summary"]["by_query_type"]["callers"]["matched_cases"] == 1
    assert report["cases"][0]["first_relevant_rank"] == 1
    assert report["cases"][0]["expectations"][0]["matched"] is True
    assert report["cases"][0]["evidence"]["coverage"] == 1.0
    assert report["cases"][0]["retrieval"]["top_hit_expectation_coverage"] == 2 / 3
    assert report["cases"][0]["retrieval"]["query_type"] == "variable_write"
    assert report["cases"][0]["top_hits"]


def test_retrieval_evaluator_accepts_plain_case_list(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)
    cases_path = tmp_path / "cases.json"
    cases_path.write_text(
        json.dumps(
            [
                {
                    "question": "uses_dynamic_table 在哪里删除",
                    "expected": {
                        "procedures": ["AF_DEEP"],
                        "texts": ["uses_dynamic_table"],
                    },
                }
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    report = RetrievalEvaluator(indexer).evaluate(db_path, cases_path, limit=5)

    assert report["case_count"] == 1
    assert report["summary"]["pass_at_k"]["5"] == 1.0
    assert report["summary"]["by_tag"]["untagged"]["matched_cases"] == 1


def test_compare_eval_reports_marks_unchanged_cases(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)
    cases_path = tmp_path / "cases.json"
    cases_path.write_text(
        json.dumps(
            [
                {
                    "id": "dynamic-table",
                    "question": "uses_dynamic_table 在哪里删除",
                    "expected": {
                        "procedures": ["AF_DEEP"],
                        "texts": ["uses_dynamic_table"],
                    },
                }
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    report = RetrievalEvaluator(indexer).evaluate(db_path, cases_path, limit=5, top_k=(1, 3, 5))
    before_path = tmp_path / "before.json"
    after_path = tmp_path / "after.json"
    before_path.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")
    after_path.write_text(json.dumps(report, ensure_ascii=False), encoding="utf-8")

    comparison = compare_eval_reports(before_path, after_path)

    assert comparison["case_change_counts"]["unchanged"] == 1
    assert comparison["case_change_counts"]["improved"] == 0
    assert comparison["summary_delta"]["pass_at_k"]["5"] == 0.0


def test_compare_eval_reports_marks_case_regressions(tmp_path: Path) -> None:
    before = {
        "top_k": [1, 3, 5],
        "summary": {
            "pass_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "expectation_recall_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "mean_first_relevant_rank": 1.0,
            "matched_cases": 1,
        },
        "cases": [
            {
                "id": "case-1",
                "question": "q",
                "first_relevant_rank": 1,
                "matched_count": 1,
                "expected_count": 1,
                "pass_at_k": {"1": True, "3": True, "5": True},
                "recall_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
                "top_hits": [{"rank": 1, "procedure_name": "AF_BEFORE"}],
            }
        ],
    }
    after = {
        "top_k": [1, 3, 5],
        "summary": {
            "pass_at_k": {"1": 0.0, "3": 1.0, "5": 1.0},
            "expectation_recall_at_k": {"1": 0.0, "3": 1.0, "5": 1.0},
            "mean_first_relevant_rank": 3.0,
            "matched_cases": 1,
        },
        "cases": [
            {
                "id": "case-1",
                "question": "q",
                "first_relevant_rank": 3,
                "matched_count": 1,
                "expected_count": 1,
                "pass_at_k": {"1": False, "3": True, "5": True},
                "recall_at_k": {"1": 0.0, "3": 1.0, "5": 1.0},
                "top_hits": [{"rank": 1, "procedure_name": "AF_AFTER"}],
            }
        ],
    }
    before_path = tmp_path / "before.json"
    after_path = tmp_path / "after.json"
    before_path.write_text(json.dumps(before, ensure_ascii=False), encoding="utf-8")
    after_path.write_text(json.dumps(after, ensure_ascii=False), encoding="utf-8")

    comparison = compare_eval_reports(before_path, after_path)

    assert comparison["case_change_counts"]["regressed"] == 1
    assert comparison["cases"][0]["change"] == "regressed"
    assert comparison["summary_delta"]["pass_at_k"]["1"] == -1.0
    assert comparison["summary_delta"]["mean_first_relevant_rank"]["delta"] == 2.0


def test_compare_eval_reports_tracks_quality_metric_deltas(tmp_path: Path) -> None:
    before = {
        "top_k": [1, 3, 5],
        "summary": {
            "pass_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "expectation_recall_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "mean_first_relevant_rank": 1.0,
            "matched_cases": 1,
            "evidence_coverage": 1.0,
            "top_hit_expectation_coverage": 1.0,
            "top_three_expectation_coverage": 1.0,
            "avg_candidate_count": 5.0,
            "avg_evidence_count": 2.0,
        },
        "cases": [],
    }
    after = {
        "top_k": [1, 3, 5],
        "summary": {
            "pass_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "expectation_recall_at_k": {"1": 1.0, "3": 1.0, "5": 1.0},
            "mean_first_relevant_rank": 1.0,
            "matched_cases": 1,
            "evidence_coverage": 0.5,
            "top_hit_expectation_coverage": 0.25,
            "top_three_expectation_coverage": 0.75,
            "avg_candidate_count": 8.0,
            "avg_evidence_count": 4.0,
        },
        "cases": [],
    }
    before_path = tmp_path / "before_quality.json"
    after_path = tmp_path / "after_quality.json"
    before_path.write_text(json.dumps(before, ensure_ascii=False), encoding="utf-8")
    after_path.write_text(json.dumps(after, ensure_ascii=False), encoding="utf-8")

    comparison = compare_eval_reports(before_path, after_path)

    assert comparison["summary_delta"]["evidence_coverage"]["delta"] == -0.5
    assert comparison["summary_delta"]["top_hit_expectation_coverage"]["delta"] == -0.75
    assert comparison["summary_delta"]["avg_candidate_count"]["delta"] == 3.0


def test_evaluate_thresholds_reports_failures(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)
    cases_path = tmp_path / "threshold_cases.json"
    cases_path.write_text(
        json.dumps(
            [
                {
                    "question": "@deep_flag 在哪里赋值",
                    "expected": {"procedures": ["AF_DEEP"], "texts": ["@deep_flag"]},
                }
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    report = RetrievalEvaluator(indexer).evaluate(db_path, cases_path, limit=5, top_k=(1, 3, 5))

    threshold_report = evaluate_thresholds(
        report,
        EvaluationThresholds(
            min_pass_at_k={"1": 1.0},
            min_evidence_coverage=1.1,
            min_top_hit_expectation_coverage=1.0,
        ),
    )

    assert threshold_report["status"] == "fail"
    assert threshold_report["failed_count"] >= 1
    assert any(item["metric"] == "evidence_coverage" and item["passed"] is False for item in threshold_report["checks"])


def test_evaluate_thresholds_supports_tag_and_query_type_guards(tmp_path: Path) -> None:
    indexer, db_path = _build_sample_index(tmp_path)
    cases_path = tmp_path / "scoped_threshold_cases.json"
    cases_path.write_text(
        json.dumps(
            {
                "cases": [
                    {
                        "question": "AF_DEEP 被谁调用",
                        "tags": ["call_chain"],
                        "expected": {"procedures": ["AF_SAMPLE"], "texts": ["AF_DEEP"]},
                    }
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    report = RetrievalEvaluator(indexer).evaluate(db_path, cases_path, limit=5, top_k=(1, 3, 5))

    threshold_report = evaluate_thresholds(
        report,
        EvaluationThresholds(
            min_tag_pass_at_k={"call_chain": {"5": 1.0}},
            min_query_type_pass_at_k={"callers": {"5": 1.0}},
        ),
    )

    assert threshold_report["status"] == "pass"
    assert any(item["metric"] == "by_tag.call_chain.pass_at_k.5" and item["passed"] is True for item in threshold_report["checks"])
    assert any(item["metric"] == "by_query_type.callers.pass_at_k.5" and item["passed"] is True for item in threshold_report["checks"])
