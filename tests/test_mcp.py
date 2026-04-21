from __future__ import annotations

import io
import json
from pathlib import Path

from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.embeddings import LocalHashedEmbedder
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.mcp_server import CodebaseMcpServer
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


def _build_server(tmp_path: Path) -> tuple[CodebaseMcpServer, Path]:
    source_dir = tmp_path / "src"
    source_dir.mkdir()
    (source_dir / "AF_SAMPLE.uftatomfunction").write_text(SAMPLE_XML, encoding="utf-8")
    (source_dir / "LS_FLOW.uftservice").write_text(CALLER_XML, encoding="utf-8")

    db_path = tmp_path / "index.db"
    indexer = SQLiteIndexer(embedder=LocalHashedEmbedder())
    indexer.build_index(source_dir, db_path)
    qa = CodebaseQA(indexer)
    answerer = CodebaseAnswerer(qa=qa, llm=StubLlm())
    server = CodebaseMcpServer(indexer=indexer, qa=qa, answerer=answerer, default_db_path=db_path)
    return server, db_path


def test_initialize_and_tool_listing(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)

    initialize = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {"protocolVersion": "2025-11-25"},
        }
    )
    assert initialize is not None
    assert initialize["result"]["serverInfo"]["name"] == "uses-indexer-mcp"

    listed = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/list",
        }
    )
    assert listed is not None
    tools = listed["result"]["tools"]
    assert any(tool["name"] == "answer_codebase" for tool in tools)
    assert any(tool["name"] == "debug_bundle" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundles" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundle_panel" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundle_panels" for tool in tools)
    assert any(tool["name"] == "save_debug_bundle_panel_baseline" for tool in tools)
    assert any(tool["name"] == "list_debug_bundle_panel_baselines" for tool in tools)
    assert any(tool["name"] == "show_debug_bundle_panel_baseline_trend" for tool in tools)
    assert any(tool["name"] == "show_debug_bundle_panel_baseline" for tool in tools)
    assert any(tool["name"] == "list_debug_bundle_panel_release_workflows" for tool in tools)
    assert any(tool["name"] == "show_debug_bundle_panel_release_workflow" for tool in tools)
    assert any(tool["name"] == "evaluate_debug_bundle_panel_promotion_gate" for tool in tools)
    assert any(tool["name"] == "promote_debug_bundle_panel_baseline" for tool in tools)
    assert any(tool["name"] == "run_debug_bundle_panel_release_workflow" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundle_panel_release_workflows" for tool in tools)
    assert any(tool["name"] == "delete_debug_bundle_panel_baseline" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundle_panel_baseline" for tool in tools)
    assert any(tool["name"] == "compare_debug_bundle_panel_latest_baseline" for tool in tools)


def test_tool_call_returns_grounded_answer(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "answer_codebase",
                "arguments": {
                    "question": "证券代码获取的逻辑在哪里",
                    "evidence_limit": 2,
                },
            },
        }
    )

    assert response is not None
    result = response["result"]
    assert result["isError"] is False
    structured = result["structuredContent"]
    assert structured["final_answer"]["source"] in {"draft", "draft_fallback", "llm"}
    assert structured["evidence_count"] >= 1
    assert structured["response_kind"] == "answer"


def test_tool_call_returns_debug_bundle(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "debug_bundle",
                "arguments": {
                    "question": "证券代码获取的逻辑在哪里",
                    "limit": 2,
                },
            },
        }
    )

    assert response is not None
    result = response["result"]
    assert result["isError"] is False
    structured = result["structuredContent"]
    assert structured["bundle_kind"] == "debug_bundle"
    assert structured["query"]["response_kind"] == "query"
    assert structured["evidence"]["response_kind"] == "evidence"
    assert structured["answer"]["response_kind"] == "answer"


def test_tool_call_compares_debug_bundles(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)
    before_bundle = {
        "db_path": "/tmp/before.db",
        "question": "证券代码获取的逻辑在哪里",
        "bundle_kind": "debug_bundle",
        "query": {"hit_count": 1, "candidate_count": 2, "hits": [], "debug": {"query_analysis": {"query_type": "callers"}}},
        "evidence": {"evidence_count": 1, "evidence": []},
        "answer": {"answer_source": "draft", "draft_answer": {"text": "a"}, "final_answer": {"text": "a"}},
    }
    after_bundle = {
        "db_path": "/tmp/after.db",
        "question": "证券代码获取的逻辑在哪里",
        "bundle_kind": "debug_bundle",
        "query": {"hit_count": 3, "candidate_count": 4, "hits": [], "debug": {"query_analysis": {"query_type": "callers"}}},
        "evidence": {"evidence_count": 2, "evidence": []},
        "answer": {"answer_source": "llm", "draft_answer": {"text": "b"}, "final_answer": {"text": "b"}},
    }
    before_path = tmp_path / "before_bundle.json"
    after_path = tmp_path / "after_bundle.json"
    before_path.write_text(json.dumps(before_bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    after_path.write_text(json.dumps(after_bundle, ensure_ascii=False, indent=2), encoding="utf-8")

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 5,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundles",
                "arguments": {
                    "before_path": str(before_path),
                    "after_path": str(after_path),
                },
            },
        }
    )

    assert response is not None
    result = response["result"]
    assert result["isError"] is False
    structured = result["structuredContent"]
    assert structured["bundle_kind"] == "debug_bundle_comparison"
    assert structured["summary"]["query_hit_count"]["delta"] == 2
    assert structured["summary"]["answer_source"]["changed"] is True


def test_tool_call_builds_debug_bundle_panel(tmp_path: Path) -> None:
    server, db_path = _build_server(tmp_path)
    cases_path = tmp_path / "panel_cases.json"
    cases_path.write_text(
        json.dumps({"cases": [{"question": "证券代码获取的逻辑在哪里"}]}, ensure_ascii=False),
        encoding="utf-8",
    )

    response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 6,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panel",
                "arguments": {
                    "before_db_path": str(db_path),
                    "after_db_path": str(db_path),
                    "cases_path": str(cases_path),
                    "max_changed_cases": 0,
                },
            },
        }
    )

    assert response is not None
    result = response["result"]
    assert result["isError"] is False
    structured = result["structuredContent"]
    assert structured["bundle_kind"] == "debug_bundle_regression_panel"
    assert structured["case_count"] == 1
    assert structured["thresholds"]["status"] == "pass"


def test_tool_call_manages_debug_bundle_panel_baselines(tmp_path: Path) -> None:
    server, db_path = _build_server(tmp_path)
    cases_path = tmp_path / "panel_cases.json"
    cases_path.write_text(
        json.dumps({"cases": [{"question": "证券代码获取的逻辑在哪里"}]}, ensure_ascii=False),
        encoding="utf-8",
    )

    panel_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 7,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panel",
                "arguments": {
                    "before_db_path": str(db_path),
                    "after_db_path": str(db_path),
                    "cases_path": str(cases_path),
                },
            },
        }
    )
    assert panel_response is not None
    panel = panel_response["result"]["structuredContent"]

    panel_dir = tmp_path / "panel_archive"
    panel_dir.mkdir()
    (panel_dir / "panel.json").write_text(json.dumps(panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (panel_dir / "panel.md").write_text(str(panel.get("markdown_summary") or ""), encoding="utf-8")
    (panel_dir / "panel_summary.json").write_text(json.dumps({"summary": panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    save_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 8,
            "method": "tools/call",
            "params": {
                "name": "save_debug_bundle_panel_baseline",
                "arguments": {
                    "panel_path": str(panel_dir),
                    "baseline_name": "mcp baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "baseline_notes": "mcp smoke baseline",
                    "baseline_tags": ["mcp", "smoke"],
                },
            },
        }
    )
    assert save_response is not None
    assert save_response["result"]["structuredContent"]["baseline_slug"] == "mcp-baseline"
    assert save_response["result"]["structuredContent"]["baseline_tags"] == ["mcp", "smoke"]

    list_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 9,
            "method": "tools/call",
            "params": {
                "name": "list_debug_bundle_panel_baselines",
                "arguments": {"baseline_dir": str(tmp_path / "baseline_store"), "baseline_tag": "mcp"},
            },
        }
    )
    assert list_response is not None
    assert list_response["result"]["structuredContent"]["count"] == 1

    show_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 10,
            "method": "tools/call",
            "params": {
                "name": "show_debug_bundle_panel_baseline",
                "arguments": {
                    "baseline_name": "mcp baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                },
            },
        }
    )
    assert show_response is not None
    assert show_response["result"]["structuredContent"]["baseline_notes"] == "mcp smoke baseline"

    promote_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 11,
            "method": "tools/call",
            "params": {
                "name": "promote_debug_bundle_panel_baseline",
                "arguments": {
                    "panel_path": str(panel_dir),
                    "baseline_name": "mcp active baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "baseline_notes": "promoted after mcp review",
                    "baseline_tags": ["mcp", "active"],
                },
            },
        }
    )
    assert promote_response is not None
    assert promote_response["result"]["structuredContent"]["bundle_kind"] == "debug_bundle_regression_panel_baseline_promoted"

    failed_panel_dir = tmp_path / "failed_panel_archive"
    failed_panel_dir.mkdir()
    failed_panel = json.loads(json.dumps(panel, ensure_ascii=False))
    failed_panel["thresholds"] = {"status": "fail", "failed_count": 1, "checks": []}
    (failed_panel_dir / "panel.json").write_text(json.dumps(failed_panel, ensure_ascii=False, indent=2), encoding="utf-8")
    (failed_panel_dir / "panel.md").write_text(str(failed_panel.get("markdown_summary") or ""), encoding="utf-8")
    (failed_panel_dir / "panel_summary.json").write_text(json.dumps({"summary": failed_panel["summary"]}, ensure_ascii=False, indent=2), encoding="utf-8")

    gate_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 12,
            "method": "tools/call",
            "params": {
                "name": "evaluate_debug_bundle_panel_promotion_gate",
                "arguments": {
                    "panel_path": str(failed_panel_dir),
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "require_threshold_pass": True,
                },
            },
        }
    )
    assert gate_response is not None
    assert gate_response["result"]["structuredContent"]["status"] == "fail"

    workflow_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 13,
            "method": "tools/call",
            "params": {
                "name": "run_debug_bundle_panel_release_workflow",
                "arguments": {
                    "panel_path": str(panel_dir),
                    "baseline_name": "mcp workflow baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "baseline_notes": "workflow promotion",
                    "baseline_tags": ["mcp", "workflow"],
                    "gate_baseline_tag": "mcp",
                    "require_threshold_pass": True,
                    "blocked_latest_verdicts": ["possible_regression"],
                    "auto_promote": True,
                    "archive_dir": str(tmp_path / "workflow_archive"),
                },
            },
        }
    )
    assert workflow_response is not None
    assert workflow_response["result"]["structuredContent"]["status"] == "promoted"
    assert Path(workflow_response["result"]["structuredContent"]["archive"]["files"]["workflow"]).exists()

    workflow_list_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 14,
            "method": "tools/call",
            "params": {
                "name": "list_debug_bundle_panel_release_workflows",
                "arguments": {
                    "workflow_dir": str(tmp_path / "workflow_archive"),
                    "baseline_tag": "mcp",
                    "status": "promoted",
                },
            },
        }
    )
    assert workflow_list_response is not None
    assert workflow_list_response["result"]["structuredContent"]["count"] == 1

    workflow_show_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 15,
            "method": "tools/call",
            "params": {
                "name": "show_debug_bundle_panel_release_workflow",
                "arguments": {
                    "workflow_path": str(tmp_path / "workflow_archive"),
                },
            },
        }
    )
    assert workflow_show_response is not None
    assert workflow_show_response["result"]["structuredContent"]["status"] == "promoted"

    workflow_compare_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 16,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panel_release_workflows",
                "arguments": {
                    "before_path": str(tmp_path / "workflow_archive"),
                    "after_path": str(tmp_path / "workflow_archive"),
                },
            },
        }
    )
    assert workflow_compare_response is not None
    assert workflow_compare_response["result"]["structuredContent"]["bundle_kind"] == "debug_bundle_regression_panel_release_workflow_comparison"

    trend_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 17,
            "method": "tools/call",
            "params": {
                "name": "show_debug_bundle_panel_baseline_trend",
                "arguments": {
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "baseline_tag": "mcp",
                },
            },
        }
    )
    assert trend_response is not None
    assert trend_response["result"]["structuredContent"]["bundle_kind"] == "debug_bundle_regression_panel_baseline_trend"

    compare_saved_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 18,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panel_baseline",
                "arguments": {
                    "panel_path": str(panel_dir),
                    "baseline_name": "mcp baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                },
            },
        }
    )
    assert compare_saved_response is not None
    assert compare_saved_response["result"]["structuredContent"]["baseline"]["baseline_slug"] == "mcp-baseline"

    compare_latest_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 19,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panel_latest_baseline",
                "arguments": {
                    "panel_path": str(panel_dir),
                    "baseline_dir": str(tmp_path / "baseline_store"),
                    "baseline_tag": "mcp",
                },
            },
        }
    )
    assert compare_latest_response is not None
    assert compare_latest_response["result"]["structuredContent"]["baseline"]["selection"] == "latest"

    compare_panels_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 20,
            "method": "tools/call",
            "params": {
                "name": "compare_debug_bundle_panels",
                "arguments": {
                    "before_path": str(panel_dir),
                    "after_path": str(panel_dir),
                },
            },
        }
    )
    assert compare_panels_response is not None
    assert compare_panels_response["result"]["structuredContent"]["bundle_kind"] == "debug_bundle_regression_panel_comparison"

    delete_response = server.handle_message(
        {
            "jsonrpc": "2.0",
            "id": 20,
            "method": "tools/call",
            "params": {
                "name": "delete_debug_bundle_panel_baseline",
                "arguments": {
                    "baseline_name": "mcp baseline",
                    "baseline_dir": str(tmp_path / "baseline_store"),
                },
            },
        }
    )
    assert delete_response is not None
    assert delete_response["result"]["structuredContent"]["deleted"] is True


def test_stdio_serve_writes_jsonrpc_lines(tmp_path: Path) -> None:
    server, _ = _build_server(tmp_path)
    input_stream = io.StringIO(
        "\n".join(
            [
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {"protocolVersion": "2025-11-25"},
                    },
                    ensure_ascii=False,
                ),
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 2,
                        "method": "tools/call",
                        "params": {
                            "name": "query_codebase",
                            "arguments": {"query": "证券代码获取", "limit": 2},
                        },
                    },
                    ensure_ascii=False,
                ),
            ]
        )
        + "\n"
    )
    output_stream = io.StringIO()

    server.serve(input_stream=input_stream, output_stream=output_stream)

    lines = [json.loads(line) for line in output_stream.getvalue().splitlines() if line.strip()]
    assert len(lines) == 2
    assert lines[0]["result"]["serverInfo"]["version"] == "0.2.0"
    assert lines[1]["result"]["structuredContent"]["hit_count"] >= 1
    assert lines[1]["result"]["structuredContent"]["response_kind"] == "query"
