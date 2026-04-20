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
        evidence_result = self.indexer.assemble_evidence(db_path, question, limit=min(5, limit))
        hits = list(query_result["hits"])
        evidence_blocks = list(evidence_result["evidence"])
        expectations = _flatten_expectations(expected)
        match_details = [
            _match_expectation(expectation, hits)
            for expectation in expectations
        ]
        evidence_match_details = [
            _match_expectation_against_evidence(expectation, evidence_blocks)
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
            "evidence": {
                "evidence_count": evidence_result["evidence_count"],
                "matched_count": sum(1 for detail in evidence_match_details if detail["matched"]),
                "coverage": sum(1 for detail in evidence_match_details if detail["matched"]) / max(len(expectations), 1),
                "expectations": evidence_match_details,
                "top_evidence": [
                    {
                        "rank": block["rank"],
                        "procedure_name": block["procedure_name"],
                        "file_path": block["file_path"],
                        "line_start": block["line_start"],
                        "line_end": block["line_end"],
                        "matched_text": block["matched_text"],
                    }
                    for block in evidence_blocks[: min(3, len(evidence_blocks))]
                ],
            },
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


def compare_eval_reports(before_path: str | Path, after_path: str | Path) -> dict[str, object]:
    before = _load_report(before_path)
    after = _load_report(after_path)
    before_cases = _cases_by_id(before)
    after_cases = _cases_by_id(after)
    case_ids = sorted(set(before_cases) | set(after_cases))
    top_k = _report_top_k(before, after)

    case_deltas = [
        _compare_case(case_id, before_cases.get(case_id), after_cases.get(case_id), top_k=top_k)
        for case_id in case_ids
    ]

    return {
        "before_path": str(before_path),
        "after_path": str(after_path),
        "case_count": {
            "before": len(before_cases),
            "after": len(after_cases),
        },
        "top_k": list(top_k),
        "summary_delta": _compare_summaries(before.get("summary", {}), after.get("summary", {}), top_k=top_k),
        "case_change_counts": {
            "improved": sum(1 for item in case_deltas if item["change"] == "improved"),
            "regressed": sum(1 for item in case_deltas if item["change"] == "regressed"),
            "unchanged": sum(1 for item in case_deltas if item["change"] == "unchanged"),
            "added": sum(1 for item in case_deltas if item["change"] == "added"),
            "removed": sum(1 for item in case_deltas if item["change"] == "removed"),
        },
        "cases": case_deltas,
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


def _load_report(path: str | Path) -> dict[str, object]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Evaluation report must be a JSON object.")
    if not isinstance(data.get("cases"), list):
        raise ValueError("Evaluation report is missing a 'cases' list.")
    return data


def _cases_by_id(report: dict[str, object]) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for item in report.get("cases", []):
        if not isinstance(item, dict):
            continue
        case_id = str(item.get("id") or item.get("question") or "")
        if case_id:
            result[case_id] = item
    return result


def _report_top_k(*reports: dict[str, object]) -> tuple[int, ...]:
    values: set[int] = set()
    for report in reports:
        for item in report.get("top_k", []):
            parsed = _as_int(item)
            if parsed is not None and parsed > 0:
                values.add(parsed)
        summary = report.get("summary", {})
        if isinstance(summary, dict):
            for metric_name in ("pass_at_k", "expectation_recall_at_k"):
                metric = summary.get(metric_name, {})
                if isinstance(metric, dict):
                    for key in metric:
                        parsed = _as_int(key)
                        if parsed is not None and parsed > 0:
                            values.add(parsed)
    return tuple(sorted(values)) or DEFAULT_TOP_K


def _compare_summaries(before: object, after: object, *, top_k: tuple[int, ...]) -> dict[str, object]:
    before_summary = before if isinstance(before, dict) else {}
    after_summary = after if isinstance(after, dict) else {}
    result: dict[str, object] = {}
    for metric_name in ("pass_at_k", "expectation_recall_at_k"):
        before_metric = before_summary.get(metric_name, {})
        after_metric = after_summary.get(metric_name, {})
        result[metric_name] = {
            str(k): _round_delta(
                _metric_value(after_metric, k) - _metric_value(before_metric, k)
            )
            for k in top_k
        }

    before_mean_rank = _as_float(before_summary.get("mean_first_relevant_rank"))
    after_mean_rank = _as_float(after_summary.get("mean_first_relevant_rank"))
    result["mean_first_relevant_rank"] = {
        "before": before_mean_rank,
        "after": after_mean_rank,
        "delta": _nullable_delta(after_mean_rank, before_mean_rank),
    }
    result["matched_cases"] = {
        "before": _as_int(before_summary.get("matched_cases")),
        "after": _as_int(after_summary.get("matched_cases")),
        "delta": _nullable_int_delta(
            _as_int(after_summary.get("matched_cases")),
            _as_int(before_summary.get("matched_cases")),
        ),
    }
    return result


def _compare_case(
    case_id: str,
    before: dict[str, object] | None,
    after: dict[str, object] | None,
    *,
    top_k: tuple[int, ...],
) -> dict[str, object]:
    if before is None:
        return {
            "id": case_id,
            "question": after.get("question") if after else None,
            "change": "added",
            "before": None,
            "after": _case_snapshot(after, top_k=top_k),
        }
    if after is None:
        return {
            "id": case_id,
            "question": before.get("question"),
            "change": "removed",
            "before": _case_snapshot(before, top_k=top_k),
            "after": None,
        }

    before_snapshot = _case_snapshot(before, top_k=top_k)
    after_snapshot = _case_snapshot(after, top_k=top_k)
    return {
        "id": case_id,
        "question": after.get("question") or before.get("question"),
        "change": _classify_case_change(before_snapshot, after_snapshot, top_k=top_k),
        "before": before_snapshot,
        "after": after_snapshot,
    }


def _case_snapshot(case: dict[str, object] | None, *, top_k: tuple[int, ...]) -> dict[str, object] | None:
    if case is None:
        return None
    return {
        "first_relevant_rank": _as_int(case.get("first_relevant_rank")),
        "matched_count": _as_int(case.get("matched_count")) or 0,
        "expected_count": _as_int(case.get("expected_count")) or 0,
        "pass_at_k": {
            str(k): bool(_metric_value(case.get("pass_at_k", {}), k))
            for k in top_k
        },
        "recall_at_k": {
            str(k): _metric_value(case.get("recall_at_k", {}), k)
            for k in top_k
        },
        "top_hit": _top_hit_snapshot(case),
    }


def _top_hit_snapshot(case: dict[str, object]) -> dict[str, object] | None:
    top_hits = case.get("top_hits", [])
    if not isinstance(top_hits, list) or not top_hits:
        return None
    top_hit = top_hits[0]
    if not isinstance(top_hit, dict):
        return None
    return {
        "rank": top_hit.get("rank"),
        "hit_type": top_hit.get("hit_type"),
        "match_source": top_hit.get("match_source"),
        "procedure_name": top_hit.get("procedure_name"),
        "file_path": top_hit.get("file_path"),
        "matched_text": top_hit.get("matched_text"),
    }


def _classify_case_change(
    before: dict[str, object] | None,
    after: dict[str, object] | None,
    *,
    top_k: tuple[int, ...],
) -> str:
    if before is None:
        return "added"
    if after is None:
        return "removed"

    cutoff = str(max(top_k))
    before_pass = bool(before["pass_at_k"].get(cutoff))
    after_pass = bool(after["pass_at_k"].get(cutoff))
    if after_pass and not before_pass:
        return "improved"
    if before_pass and not after_pass:
        return "regressed"

    before_recall = float(before["recall_at_k"].get(cutoff, 0.0))
    after_recall = float(after["recall_at_k"].get(cutoff, 0.0))
    if after_recall > before_recall:
        return "improved"
    if after_recall < before_recall:
        return "regressed"

    before_rank = _case_rank_score(before["first_relevant_rank"])
    after_rank = _case_rank_score(after["first_relevant_rank"])
    if after_rank < before_rank:
        return "improved"
    if after_rank > before_rank:
        return "regressed"

    return "unchanged"


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


def _match_expectation_against_evidence(expectation: dict[str, object], evidence_blocks: list[dict[str, object]]) -> dict[str, object]:
    kind = str(expectation["kind"])
    value = expectation["value"]
    for block in evidence_blocks:
        if _evidence_matches(kind, value, block):
            return {
                "kind": kind,
                "value": value,
                "matched": True,
                "first_rank": int(block["rank"]),
                "matched_evidence": {
                    "rank": block["rank"],
                    "procedure_name": block["procedure_name"],
                    "file_path": block["file_path"],
                    "line_start": block["line_start"],
                    "line_end": block["line_end"],
                    "matched_text": block["matched_text"],
                },
            }

    return {
        "kind": kind,
        "value": value,
        "matched": False,
        "first_rank": None,
        "matched_evidence": None,
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


def _evidence_matches(kind: str, value: object, block: dict[str, object]) -> bool:
    if kind == "procedure":
        return _contains(str(block.get("procedure_name") or ""), str(value))
    if kind == "path":
        return _contains(str(block.get("file_path") or ""), str(value))
    if kind == "text":
        haystack = " ".join(
            [
                str(block.get("matched_text") or ""),
                str(block.get("excerpt") or ""),
                " ".join(str(reason) for reason in block.get("reasons", [])),
            ]
        )
        return _contains(haystack, str(value))
    if kind == "line_range":
        if not isinstance(value, dict):
            return False
        path_contains = str(value.get("path_contains") or "")
        if path_contains and not _contains(str(block.get("file_path") or ""), path_contains):
            return False
        expected_start = _as_int(value.get("start"))
        expected_end = _as_int(value.get("end"))
        hit_start = _as_int(block.get("line_start"))
        hit_end = _as_int(block.get("line_end"))
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


def _as_float(value: object) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _metric_value(metric: object, k: int) -> float:
    if not isinstance(metric, dict):
        return 0.0
    value = metric.get(str(k), metric.get(k, 0.0))
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    parsed = _as_float(value)
    return parsed if parsed is not None else 0.0


def _nullable_delta(after: float | None, before: float | None) -> float | None:
    if after is None or before is None:
        return None
    return _round_delta(after - before)


def _nullable_int_delta(after: int | None, before: int | None) -> int | None:
    if after is None or before is None:
        return None
    return after - before


def _round_delta(value: float) -> float:
    return round(value, 6)


def _case_rank_score(value: object) -> int:
    parsed = _as_int(value)
    if parsed is None:
        return 1_000_000
    return parsed


def _matched_count_at_k(match_details: list[dict[str, object]], k: int) -> int:
    return sum(
        1
        for detail in match_details
        if detail["matched"] and int(detail["first_rank"]) <= k
    )


def _summarize_by_tag(
    case_results: list[dict[str, object]],
    *,
    top_k: tuple[int, ...],
) -> dict[str, object]:
    grouped: dict[str, list[dict[str, object]]] = {}
    for case in case_results:
        tags = case.get("tags", [])
        normalized_tags = tags if isinstance(tags, list) and tags else ["untagged"]
        for tag in normalized_tags:
            grouped.setdefault(str(tag), []).append(case)

    return {
        tag: _summarize_case_results(tag_cases, top_k=top_k, include_by_tag=False)
        for tag, tag_cases in sorted(grouped.items())
    }


def _summarize_case_results(
    case_results: list[dict[str, object]],
    *,
    top_k: tuple[int, ...],
    include_by_tag: bool = True,
) -> dict[str, object]:
    case_count = len(case_results)
    if case_count == 0:
        return {
            "pass_at_k": {str(k): 0.0 for k in top_k},
            "expectation_recall_at_k": {str(k): 0.0 for k in top_k},
            "mean_first_relevant_rank": None,
            "matched_cases": 0,
            "evidence_coverage": 0.0,
            "by_tag": {} if include_by_tag else None,
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
        "evidence_coverage": (
            sum(float(case["evidence"]["coverage"]) for case in case_results) / case_count
        ),
        "by_tag": _summarize_by_tag(case_results, top_k=top_k) if include_by_tag else None,
    }
