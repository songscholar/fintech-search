from __future__ import annotations

import json
from pathlib import Path

from .indexer import SQLiteIndexer


DEFAULT_TOP_K = (1, 3, 5, 10)


class RetrievalEvaluator:
    def __init__(self, indexer: SQLiteIndexer | None = None) -> None:
        self.indexer = indexer or SQLiteIndexer()

    def evaluate(
        self,
        db_path: str | Path,
        cases_path: str | Path,
        *,
        limit: int = 10,
        top_k: tuple[int, ...] = DEFAULT_TOP_K,
    ) -> dict[str, object]:
        cases = _load_cases(cases_path)
        normalized_top_k = tuple(sorted({k for k in top_k if k > 0 and k <= limit}))
        if not normalized_top_k:
            normalized_top_k = (limit,)

        case_results = [
            self._evaluate_case(db_path, case, limit=limit, top_k=normalized_top_k)
            for case in cases
        ]

        return {
            "db_path": str(db_path),
            "cases_path": str(cases_path),
            "case_count": len(case_results),
            "limit": limit,
            "top_k": list(normalized_top_k),
            "summary": _summarize_case_results(case_results, top_k=normalized_top_k),
            "cases": case_results,
        }

    def _evaluate_case(
        self,
        db_path: str | Path,
        case: dict[str, object],
        *,
        limit: int,
        top_k: tuple[int, ...],
    ) -> dict[str, object]:
        question = str(case["question"])
        expected = _normalize_expected(case.get("expected", {}))
        query_result = self.indexer.query_index(db_path, question, limit=limit)
        hits = list(query_result["hits"])
        expectations = _flatten_expectations(expected)
        match_details = [
            _match_expectation(expectation, hits)
            for expectation in expectations
        ]

        first_rank = min(
            (int(detail["first_rank"]) for detail in match_details if detail["matched"]),
            default=None,
        )

        pass_at_k = {
            str(k): any(
                bool(detail["matched"]) and int(detail["first_rank"]) <= k
                for detail in match_details
            )
            for k in top_k
        }
        recall_at_k = {
            str(k): _matched_count_at_k(match_details, k) / max(len(expectations), 1)
            for k in top_k
        }

        return {
            "id": case.get("id") or question,
            "question": question,
            "tags": list(case.get("tags", [])),
            "expected_count": len(expectations),
            "matched_count": sum(1 for detail in match_details if detail["matched"]),
            "first_relevant_rank": first_rank,
            "pass_at_k": pass_at_k,
            "recall_at_k": recall_at_k,
            "expectations": match_details,
            "top_hits": [
                {
                    "rank": hit["rank"],
                    "hit_type": hit["hit_type"],
                    "match_source": hit["match_source"],
                    "procedure_name": hit["procedure_name"],
                    "file_path": hit["file_path"],
                    "line_start": hit["line_start"],
                    "line_end": hit["line_end"],
                    "matched_text": hit["matched_text"],
                    "reasons": hit["reasons"],
                }
                for hit in hits[: min(5, limit)]
            ],
            "retrieval": {
                "candidate_count": query_result["candidate_count"],
                "hit_count": query_result["hit_count"],
                "vector_status": query_result["vector_status"],
            },
        }


def _load_cases(path: str | Path) -> list[dict[str, object]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        raw_cases = data.get("cases")
    else:
        raw_cases = data

    if not isinstance(raw_cases, list):
        raise ValueError("Evaluation cases must be a list or an object with a 'cases' list.")

    cases: list[dict[str, object]] = []
    for index, item in enumerate(raw_cases, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Case #{index} must be an object.")
        if not item.get("question"):
            raise ValueError(f"Case #{index} is missing 'question'.")
        cases.append(item)
    return cases


def _normalize_expected(value: object) -> dict[str, object]:
    if value is None:
        return {}
    if not isinstance(value, dict):
        raise ValueError("'expected' must be an object.")
    return value


def _flatten_expectations(expected: dict[str, object]) -> list[dict[str, object]]:
    expectations: list[dict[str, object]] = []
    for key, kind in (
        ("procedures", "procedure"),
        ("paths", "path"),
        ("texts", "text"),
        ("tables", "text"),
    ):
        values = expected.get(key, [])
        if isinstance(values, str):
            values = [values]
        if not isinstance(values, list):
            raise ValueError(f"expected.{key} must be a string or list.")
        for value in values:
            expectations.append({"kind": kind, "value": str(value)})

    line_ranges = expected.get("line_ranges", [])
    if isinstance(line_ranges, dict):
        line_ranges = [line_ranges]
    if not isinstance(line_ranges, list):
        raise ValueError("expected.line_ranges must be an object or list.")
    for value in line_ranges:
        if not isinstance(value, dict):
            raise ValueError("Each line range expectation must be an object.")
        expectations.append({"kind": "line_range", "value": value})

    return expectations


def _match_expectation(expectation: dict[str, object], hits: list[dict[str, object]]) -> dict[str, object]:
    kind = str(expectation["kind"])
    value = expectation["value"]
    for hit in hits:
        if _hit_matches(kind, value, hit):
            return {
                "kind": kind,
                "value": value,
                "matched": True,
                "first_rank": int(hit["rank"]),
                "matched_hit": {
                    "rank": hit["rank"],
                    "procedure_name": hit["procedure_name"],
                    "file_path": hit["file_path"],
                    "line_start": hit["line_start"],
                    "line_end": hit["line_end"],
                    "matched_text": hit["matched_text"],
                    "match_source": hit["match_source"],
                },
            }

    return {
        "kind": kind,
        "value": value,
        "matched": False,
        "first_rank": None,
        "matched_hit": None,
    }


def _hit_matches(kind: str, value: object, hit: dict[str, object]) -> bool:
    if kind == "procedure":
        return _contains(str(hit.get("procedure_name") or ""), str(value))
    if kind == "path":
        return _contains(str(hit.get("file_path") or ""), str(value))
    if kind == "text":
        haystack = " ".join(
            [
                str(hit.get("matched_text") or ""),
                str(hit.get("match_source") or ""),
                " ".join(str(reason) for reason in hit.get("reasons", [])),
            ]
        )
        return _contains(haystack, str(value))
    if kind == "line_range":
        if not isinstance(value, dict):
            return False
        path_contains = str(value.get("path_contains") or "")
        if path_contains and not _contains(str(hit.get("file_path") or ""), path_contains):
            return False
        expected_start = _as_int(value.get("start"))
        expected_end = _as_int(value.get("end"))
        hit_start = _as_int(hit.get("line_start"))
        hit_end = _as_int(hit.get("line_end"))
        if expected_start is None or expected_end is None or hit_start is None or hit_end is None:
            return False
        return max(expected_start, hit_start) <= min(expected_end, hit_end)
    return False


def _contains(haystack: str, needle: str) -> bool:
    return needle.lower() in haystack.lower()


def _as_int(value: object) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _matched_count_at_k(match_details: list[dict[str, object]], k: int) -> int:
    return sum(
        1
        for detail in match_details
        if detail["matched"] and int(detail["first_rank"]) <= k
    )


def _summarize_case_results(case_results: list[dict[str, object]], *, top_k: tuple[int, ...]) -> dict[str, object]:
    case_count = len(case_results)
    if case_count == 0:
        return {
            "pass_at_k": {str(k): 0.0 for k in top_k},
            "expectation_recall_at_k": {str(k): 0.0 for k in top_k},
            "mean_first_relevant_rank": None,
            "matched_cases": 0,
        }

    pass_at_k = {
        str(k): sum(1 for case in case_results if case["pass_at_k"][str(k)]) / case_count
        for k in top_k
    }
    expectation_recall_at_k = {
        str(k): sum(float(case["recall_at_k"][str(k)]) for case in case_results) / case_count
        for k in top_k
    }
    first_ranks = [
        int(case["first_relevant_rank"])
        for case in case_results
        if case["first_relevant_rank"] is not None
    ]

    return {
        "pass_at_k": pass_at_k,
        "expectation_recall_at_k": expectation_recall_at_k,
        "mean_first_relevant_rank": (
            sum(first_ranks) / len(first_ranks) if first_ranks else None
        ),
        "matched_cases": len(first_ranks),
    }
