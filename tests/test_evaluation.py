from __future__ import annotations

import json
from pathlib import Path

from tests.test_indexer import _build_sample_index
from uses_indexer.evaluation import RetrievalEvaluator


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
    assert report["cases"][0]["first_relevant_rank"] == 1
    assert report["cases"][0]["expectations"][0]["matched"] is True
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
