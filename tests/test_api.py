from __future__ import annotations

import json
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest

from uses_indexer.api import ApiError, CodebaseApi, make_handler_class
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.qa import CodebaseQA


SAMPLE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Function xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="AF_测试_样例" objectId="1">
  <inputParameters id="stock_code" uuid="u1"/>
  <outputParameters id="row_count" uuid="u2"/>
  <code><![CDATA[
  [AF_系统参数公用_证券代码获取][][usps_stkcode = @usps_stkcode]
  [获取记录][uses_fund_real(idx_x)][fund_account = @fund_account]
  @row_count = 1;
  ]]></code>
</business:Function>
"""

CALLER_XML = """<?xml version="1.0" encoding="UTF-8"?>
<business:Service xmlns:business="http://www.hundsun.com/ares/studio/uft/business/1.0.0" chineseName="LS_测试_入口" objectId="2">
  <inputParameters id="fund_account" uuid="u3"/>
  <outputParameters id="row_count" uuid="u4"/>
  <code><![CDATA[
  [AF_SAMPLE][][row_count = @row_count]
  [获取字段][uses_fund_real(idx_x)][fund_account = @fund_account]
  ]]></code>
</business:Service>
"""


class StubLlm:
    def is_configured(self) -> bool:
        return False

    def complete(self, *, system_prompt: str, user_prompt: str) -> dict[str, object]:
        raise AssertionError("complete should not be called when is_configured is false")


def _build_api(tmp_path: Path) -> tuple[CodebaseApi, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer()
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm())
    api = CodebaseApi(indexer=indexer, qa=qa, answerer=answerer, default_db_path=db_path)
    return api, db_path


def test_api_handle_request_routes(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)

    status, health = api.handle_request("GET", "/health")
    assert status == 200
    assert health["status"] == "ok"

    status, summary = api.handle_request("GET", "/db-summary")
    assert status == 200
    assert summary["files"] == 2
    assert summary["response_kind"] == "db_summary"

    status, query = api.handle_request(
        "POST",
        "/query",
        json.dumps({"query": "证券代码获取", "limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert query["hit_count"] >= 1
    assert query["response_kind"] == "query"

    status, ask = api.handle_request(
        "POST",
        "/ask",
        json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert ask["draft_answer"]["status"] == "ok"
    assert ask["response_kind"] == "ask"

    status, answer = api.handle_request(
        "POST",
        "/answer",
        json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert answer["final_answer"]["source"] in {"draft", "draft_fallback", "llm"}
    assert answer["response_kind"] == "answer"

    status, bundle = api.handle_request(
        "POST",
        "/debug-bundle",
        json.dumps({"question": "证券代码获取的逻辑在哪里", "limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert bundle["bundle_kind"] == "debug_bundle"
    assert bundle["query"]["response_kind"] == "query"
    assert bundle["evidence"]["response_kind"] == "evidence"
    assert bundle["answer"]["response_kind"] == "answer"

    before_path = tmp_path / "before_bundle.json"
    after_path = tmp_path / "after_bundle.json"
    before_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    mutated_bundle = json.loads(json.dumps(bundle, ensure_ascii=False))
    mutated_bundle["query"]["hit_count"] = bundle["query"]["hit_count"] + 1
    mutated_bundle["answer"]["final_answer"]["text"] = "changed answer"
    after_path.write_text(json.dumps(mutated_bundle, ensure_ascii=False, indent=2), encoding="utf-8")

    status, comparison = api.handle_request(
        "POST",
        "/compare-debug-bundles",
        json.dumps({"before_path": str(before_path), "after_path": str(after_path)}).encode("utf-8"),
    )
    assert status == 200
    assert comparison["bundle_kind"] == "debug_bundle_comparison"
    assert comparison["summary"]["query_hit_count"]["delta"] == 1
    assert comparison["answer"]["final_answer_changed"] is True

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
    status, panel = api.handle_request(
        "POST",
        "/compare-debug-bundle-panel",
        json.dumps(
            {
                "before_db_path": str(api.default_db_path),
                "after_db_path": str(api.default_db_path),
                "cases_path": str(cases_path),
                "max_changed_cases": 0,
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert panel["bundle_kind"] == "debug_bundle_regression_panel"
    assert panel["case_count"] == 1
    assert panel["thresholds"]["status"] == "pass"

    panel_archive = tmp_path / "panel_archive"
    panel_archive.mkdir()
    (panel_archive / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_archive / "panel.md").write_text(str(panel.get("markdown_summary") or ""), encoding="utf-8")
    (panel_archive / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    status, saved = api.handle_request(
        "POST",
        "/save-debug-bundle-panel-baseline",
        json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_name": "smoke baseline",
                "baseline_dir": str(tmp_path / "baseline_store"),
                "baseline_notes": "smoke compare baseline",
                "baseline_tags": ["smoke", "nightly"],
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert saved["baseline_slug"] == "smoke-baseline"
    assert saved["baseline_tags"] == ["nightly", "smoke"]

    status, baselines = api.handle_request(
        "GET",
        f"/list-debug-bundle-panel-baselines?baseline_dir={tmp_path / 'baseline_store'}&baseline_tag=smoke",
    )
    assert status == 200
    assert baselines["count"] == 1
    assert baselines["items"][0]["baseline_notes"] == "smoke compare baseline"

    status, shown = api.handle_request(
        "GET",
        f"/show-debug-bundle-panel-baseline?baseline_dir={tmp_path / 'baseline_store'}&baseline_name=smoke baseline",
    )
    assert status == 200
    assert shown["baseline_tags"] == ["nightly", "smoke"]

    status, promoted = api.handle_request(
        "POST",
        "/promote-debug-bundle-panel-baseline",
        json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_name": "active smoke",
                "baseline_dir": str(tmp_path / "baseline_store"),
                "baseline_notes": "promoted after smoke pass",
                "baseline_tags": ["smoke", "active"],
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert promoted["bundle_kind"] == "debug_bundle_regression_panel_baseline_promoted"
    assert promoted["promotion_source"] == str(panel_archive)

    failed_panel_archive = tmp_path / "failed_panel_archive"
    failed_panel_archive.mkdir()
    failed_panel = json.loads(json.dumps(panel, ensure_ascii=False))
    failed_panel["thresholds"] = {"status": "fail", "failed_count": 1, "checks": []}
    (failed_panel_archive / "panel.json").write_text(json.dumps(failed_panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (failed_panel_archive / "panel.md").write_text(str(failed_panel.get("markdown_summary") or ""), encoding="utf-8")
    (failed_panel_archive / "panel_summary.json").write_text(json.dumps({"summary": failed_panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    with pytest.raises(ApiError) as exc_info:
        api.handle_request(
            "POST",
            "/promote-debug-bundle-panel-baseline",
            json.dumps(
                {
                    "panel_path": str(failed_panel_archive),
                    "baseline_name": "blocked smoke",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "require_threshold_pass": True,
                }
            ).encode("utf-8"),
        )
    assert exc_info.value.status_code == 400

    status, gate = api.handle_request(
        "POST",
        "/evaluate-debug-bundle-panel-promotion-gate",
        json.dumps(
            {
                "panel_path": str(failed_panel_archive),
                "baseline_dir": str(tmp_path / "baseline_store"),
                "require_threshold_pass": True,
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert gate["status"] == "fail"

    status, workflow = api.handle_request(
        "POST",
        "/run-debug-bundle-panel-release-workflow",
        json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_name": "workflow smoke",
                "baseline_dir": str(tmp_path / "baseline_store"),
                "baseline_notes": "workflow promotion",
                "baseline_tags": ["smoke", "workflow"],
                "gate_baseline_tag": "smoke",
                "require_threshold_pass": True,
                "blocked_latest_verdicts": ["possible_regression"],
                "auto_promote": True,
                "archive_dir": str(tmp_path / "workflow_archive"),
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert workflow["status"] == "promoted"
    assert Path(workflow["archive"]["files"]["workflow"]).exists()

    status, workflow_list = api.handle_request(
        "GET",
        f"/list-debug-bundle-panel-release-workflows?workflow_dir={tmp_path / 'workflow_archive'}&baseline_tag=smoke&status=promoted",
    )
    assert status == 200
    assert workflow_list["count"] == 1

    status, shown_workflow = api.handle_request(
        "GET",
        f"/show-debug-bundle-panel-release-workflow?workflow_path={tmp_path / 'workflow_archive'}",
    )
    assert status == 200
    assert shown_workflow["status"] == "promoted"

    status, workflow_compare = api.handle_request(
        "POST",
        "/compare-debug-bundle-panel-release-workflows",
        json.dumps(
            {
                "before_path": str(tmp_path / "workflow_archive"),
                "after_path": str(tmp_path / "workflow_archive"),
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert workflow_compare["bundle_kind"] == "debug_bundle_regression_panel_release_workflow_comparison"

    status, trend = api.handle_request(
        "GET",
        f"/show-debug-bundle-panel-baseline-trend?baseline_dir={tmp_path / 'baseline_store'}&baseline_tag=smoke",
    )
    assert status == 200
    assert trend["bundle_kind"] == "debug_bundle_regression_panel_baseline_trend"
    assert trend["baseline_count"] == 3

    status, compared = api.handle_request(
        "POST",
        "/compare-debug-bundle-panels",
        json.dumps({"before_path": str(panel_archive), "after_path": str(panel_archive)}).encode("utf-8"),
    )
    assert status == 200
    assert compared["bundle_kind"] == "debug_bundle_regression_panel_comparison"

    status, baseline_compare = api.handle_request(
        "POST",
        "/compare-debug-bundle-panel-baseline",
        json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_name": "smoke baseline",
                "baseline_dir": str(tmp_path / "baseline_store"),
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert baseline_compare["baseline"]["baseline_slug"] == "smoke-baseline"

    status, latest_compare = api.handle_request(
        "POST",
        "/compare-debug-bundle-panel-latest-baseline",
        json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_dir": str(tmp_path / "baseline_store"),
                "baseline_tag": "smoke",
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert latest_compare["baseline"]["selection"] == "latest"

    status, deleted = api.handle_request(
        "POST",
        "/delete-debug-bundle-panel-baseline",
        json.dumps(
            {
                "baseline_name": "smoke baseline",
                "baseline_dir": str(tmp_path / "baseline_store"),
            }
        ).encode("utf-8"),
    )
    assert status == 200
    assert deleted["deleted"] is True


def test_http_server_serves_json(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler_class(api))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        host, port = server.server_address
        conn = HTTPConnection(host, port, timeout=5)

        conn.request("GET", "/health")
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["service"] == "uses-indexer-api"

        payload = json.dumps({"question": "证券代码获取的逻辑在哪里", "evidence_limit": 2})
        conn.request("POST", "/ask", body=payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["evidence_count"] >= 1
        assert "prompt_package" in body

        conn.request("POST", "/answer", body=payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert "final_answer" in body

        panel_cases = tmp_path / "http_panel_cases.json"
        panel_cases.write_text(
            json.dumps({"cases": [{"question": "证券代码获取的逻辑在哪里"}]}, ensure_ascii=False),
            encoding="utf-8",
        )
        panel_payload = json.dumps(
            {
                "before_db_path": str(api.default_db_path),
                "after_db_path": str(api.default_db_path),
                "cases_path": str(panel_cases),
            }
        )
        conn.request("POST", "/compare-debug-bundle-panel", body=panel_payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["bundle_kind"] == "debug_bundle_regression_panel"

        panel_archive = tmp_path / "http_panel_archive"
        panel_archive.mkdir()
        (panel_archive / "panel.json").write_text(json.dumps(body, ensure_ascii=False, indent=2), encoding="utf-8")
        (panel_archive / "panel.md").write_text(str(body.get("markdown_summary") or ""), encoding="utf-8")
        (panel_archive / "panel_summary.json").write_text(json.dumps({"summary": body["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

        baseline_payload = json.dumps(
            {
                "panel_path": str(panel_archive),
                "baseline_name": "http baseline",
                "baseline_dir": str(tmp_path / "http_baselines"),
            }
        )
        conn.request("POST", "/save-debug-bundle-panel-baseline", body=baseline_payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["baseline_slug"] == "http-baseline"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()
