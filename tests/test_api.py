from __future__ import annotations

import json
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest

from uses_indexer.agent_gateway import AgentGateway, AgentProviderConfig, _build_query_plan, _normalize_retrieval_intent, _query_object_id_fast
from uses_indexer.api import ApiError, CodebaseApi, make_handler_class
from uses_indexer.answering import CodebaseAnswerer
from uses_indexer.indexer import SQLiteIndexer
from uses_indexer.langchain_agent import (
    LangChainAgentError,
    _build_chat_openai,
    _build_evidence_context,
    _query_code_like_index,
)
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


class StubAgentGateway:
    def list_providers(self) -> dict[str, object]:
        return {
            "response_kind": "agent_providers",
            "default_provider": "hermes",
            "count": 1,
            "items": [
                {
                    "name": "hermes",
                    "label": "Hermes",
                    "adapter": "openai-compatible",
                    "configured": True,
                    "default": True,
                    "description": "stub provider",
                    "model": "stub-hermes",
                    "base_url": "http://agent.local/chat",
                }
            ],
        }

    def chat(self, **kwargs: object) -> dict[str, object]:
        return {
            "response_kind": "agent_chat",
            "provider": {
                "name": str(kwargs.get("provider_name") or "hermes"),
                "label": "Hermes",
                "adapter": "openai-compatible",
                "model": "stub-hermes",
                "base_url": "http://agent.local/chat",
            },
            "message": kwargs.get("message"),
            "reply": "stub agent reply",
            "latency_ms": 12,
            "context_bundle": {
                "db_path": kwargs.get("db_path"),
                "metadata_db_path": kwargs.get("metadata_db_path"),
                "table_db_path": kwargs.get("table_db_path"),
                "question": kwargs.get("message"),
            },
            "raw_response": {"choices": []},
        }


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
    api = CodebaseApi(
        indexer=indexer,
        qa=qa,
        answerer=answerer,
        agent_gateway=StubAgentGateway(),
        default_db_path=db_path,
    )
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

    status, providers = api.handle_request("GET", "/agent/providers")
    assert status == 200
    assert providers["response_kind"] == "agent_providers"
    assert providers["items"][0]["name"] == "hermes"

    status, agent = api.handle_request(
        "POST",
        "/agent/chat",
        json.dumps({"message": "帮我解释当前失败路径", "provider": "hermes", "limit": 2}).encode("utf-8"),
    )
    assert status == 200
    assert agent["response_kind"] == "agent_chat"
    assert agent["reply"] == "stub agent reply"

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


def test_agent_chat_uses_default_metadata_and_table_indexes(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)
    metadata_db = tmp_path / "metadata.db"
    table_db = tmp_path / "table.db"
    api.default_metadata_db_path = str(metadata_db)
    api.default_table_db_path = str(table_db)

    status, result = api.handle_request(
        "POST",
        "/agent/chat",
        json.dumps({"message": "功能号 333002 包含哪些业务流程"}).encode("utf-8"),
    )

    assert status == 200
    context = dict(result["context_bundle"])
    assert context["metadata_db_path"] == str(metadata_db)
    assert context["table_db_path"] == str(table_db)


def test_agent_gateway_context_bundle_exposes_grounded_decision(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(indexer=api.indexer, qa=api.qa, providers={})

    bundle = gateway._build_context(
        db_path=str(db_path),
        message="@fund_account 变量链路",
        include_retrieval=True,
        include_evidence=True,
        include_answer_draft=True,
        limit=4,
        context_window=1,
        related_limit=2,
    )

    draft = dict(bundle["answer_draft"])
    assert draft["text"]
    assert draft["query_type"] in {"variable_flow", "variable_read", "variable_write"}
    assert isinstance(draft["decision"], dict)
    assert draft["decision"]["evidence_alignment"] in {"aligned", "divergent", "partial"}
    assert "primary_candidate" in draft


def test_agent_gateway_auto_search_context_runs_without_manual_retrieval(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(indexer=api.indexer, qa=api.qa, providers={})

    bundle = gateway._build_context(
        db_path=str(db_path),
        message="功能号 333002 包含哪些业务流程",
        include_retrieval=False,
        include_evidence=False,
        include_answer_draft=False,
        auto_retrieve=True,
        max_search_rounds=2,
        limit=3,
        context_window=1,
        related_limit=1,
    )

    auto_search = dict(bundle["auto_search"])
    assert auto_search["search_decision"]["needs_search"] is True
    assert auto_search["search_decision"]["rounds_used"] >= 1
    assert auto_search["query_plan"]
    assert "selected_code_and_metadata_context" in auto_search


def test_agent_gateway_auto_search_prioritizes_embedded_feature_number() -> None:
    plan = _build_query_plan("功能号333002包含哪些业务流程？", max_rounds=3)

    assert plan[0] == "333002"
    assert "功能号 333002" in plan


def test_agent_gateway_object_id_fast_path(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)

    hits = _query_object_id_fast(str(db_path), "1", limit=3)

    assert hits
    assert hits[0]["object_id"] == "1"
    assert hits[0]["procedure_name"] == "AF_SAMPLE"


def test_agent_gateway_auto_search_stops_after_exact_object_id_hit(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(indexer=api.indexer, qa=api.qa, providers={})

    auto_search = gateway._build_auto_search_context(
        db_path=str(db_path),
        message="功能号1包含哪些业务流程",
        limit=2,
        context_window=1,
        related_limit=1,
        max_search_rounds=3,
    )

    assert auto_search["search_decision"]["rounds_used"] == 1
    assert auto_search["search_decision"]["stop_reason"] == "sufficient_context"
    assert auto_search["rounds"][0]["indexes"][0]["fast_path"] == "object_id_exact"


def test_agent_gateway_chat_uses_langchain_when_auto_retrieve(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="http://agent.local/v1/chat/completions",
                model="stub-model",
                api_key="stub-key",
            )
        },
        default_provider="openai-compatible",
    )
    called = {}

    def fake_langchain_agent(**kwargs):
        called.update(kwargs)
        return {
            "content": "langchain answer",
            "usage": None,
            "raw_response": {"intermediate_steps": []},
            "context_bundle": {"agent": "langchain_tool_calling_agent"},
        }

    monkeypatch.setattr(
        "uses_indexer.agent_gateway.classify_retrieval_intent",
        lambda **kwargs: {"needs_retrieval": True, "reason": "business question", "suggested_tools": ["code"]},
    )
    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain_agent)
    result = gateway.chat(
        db_path=str(db_path),
        metadata_db_path=str(tmp_path / "metadata.db"),
        table_db_path=str(tmp_path / "table.db"),
        message="功能号 333002 包含哪些业务流程",
        provider_name="openai-compatible",
        auto_retrieve=True,
        max_search_rounds=2,
    )

    assert result["reply"] == "langchain answer"
    assert result["context_bundle"]["agent"] == "langchain_tool_calling_agent"
    assert called["max_iterations"] == 2
    assert called["metadata_db_path"] == str(tmp_path / "metadata.db")
    assert called["table_db_path"] == str(tmp_path / "table.db")


def test_agent_gateway_auto_retrieve_skips_tools_for_general_chat(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="http://agent.local/v1/chat/completions",
                model="stub-model",
                api_key="stub-key",
            )
        },
        default_provider="openai-compatible",
    )
    langchain_called = {"value": False}

    monkeypatch.setattr(
        "uses_indexer.agent_gateway.classify_retrieval_intent",
        lambda **kwargs: {"needs_retrieval": False, "reason": "general chat", "suggested_tools": []},
    )

    def fake_langchain_agent(**kwargs):
        langchain_called["value"] = True
        raise AssertionError("langchain tools should not run for general chat")

    def fake_complete(config, messages):
        assert "通用智能助手" in messages[0]["content"]
        return {"content": "general answer", "usage": None, "raw_response": {"choices": []}}

    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain_agent)
    monkeypatch.setattr("uses_indexer.agent_gateway._complete_openai_compatible", fake_complete)

    result = gateway.chat(
        db_path=str(db_path),
        message="你好，帮我写一句问候语",
        provider_name="openai-compatible",
        auto_retrieve=True,
    )

    assert result["reply"] == "general answer"
    assert result["context_bundle"]["intent"]["needs_retrieval"] is False
    assert langchain_called["value"] is False


def test_agent_gateway_auto_retrieve_falls_back_when_intent_llm_fails(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="http://agent.local/v1/chat/completions",
                model="stub-model",
                api_key="stub-key",
            )
        },
        default_provider="openai-compatible",
    )
    called = {}

    def fake_intent(**kwargs):
        raise RuntimeError("403 access_terminated_error")

    def fake_langchain_agent(**kwargs):
        called.update(kwargs)
        return {
            "content": "fallback intent still reached langchain",
            "usage": None,
            "raw_response": {"intermediate_steps": []},
            "context_bundle": {"agent": "langchain_tool_calling_agent"},
        }

    monkeypatch.setattr("uses_indexer.agent_gateway.classify_retrieval_intent", fake_intent)
    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain_agent)

    result = gateway.chat(
        db_path=str(db_path),
        message="功能号 333002 包含哪些业务流程",
        provider_name="openai-compatible",
        auto_retrieve=True,
    )

    assert result["reply"] == "fallback intent still reached langchain"
    assert result["context_bundle"]["intent"]["source"] == "local_rule_fallback"
    assert result["context_bundle"]["intent"]["needs_retrieval"] is True
    assert called["question"] == "功能号 333002 包含哪些业务流程"


def test_agent_gateway_local_rule_overrides_false_llm_intent() -> None:
    intent = _normalize_retrieval_intent(
        "功能号333002包含哪些业务流程？",
        {"needs_retrieval": False, "reason": "", "suggested_tools": [], "raw": ""},
    )

    assert intent["needs_retrieval"] is True
    assert intent["source"] == "llm_with_local_rule_override"
    assert "code" in intent["suggested_tools"]


def test_agent_gateway_auto_retrieve_returns_local_summary_when_langchain_llm_fails(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="http://agent.local/v1/chat/completions",
                model="stub-model",
                api_key="stub-key",
            )
        },
        default_provider="openai-compatible",
    )

    monkeypatch.setattr(
        "uses_indexer.agent_gateway.classify_retrieval_intent",
        lambda **kwargs: {"needs_retrieval": True, "reason": "business question", "suggested_tools": ["code"]},
    )

    def fake_langchain_agent(**kwargs):
        raise RuntimeError("403 access_terminated_error")

    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain_agent)

    result = gateway.chat(
        db_path=str(db_path),
        message="证券代码获取的逻辑在哪里",
        provider_name="openai-compatible",
        auto_retrieve=True,
    )

    assert result["response_kind"] == "agent_chat"
    assert "当前模型暂不可用" in result["reply"]
    assert "access_terminated_error" in result["reply"]
    assert result["context_bundle"]["fallback"]["reason"] == "provider_unavailable"
    assert result["raw_response"]["fallback"] is True


def test_agent_gateway_auto_retrieve_returns_local_summary_when_langchain_missing(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="http://agent.local/v1/chat/completions",
                model="stub-model",
                api_key="stub-key",
            )
        },
        default_provider="openai-compatible",
    )

    monkeypatch.setattr(
        "uses_indexer.agent_gateway.classify_retrieval_intent",
        lambda **kwargs: {"needs_retrieval": True, "reason": "business question", "suggested_tools": ["code"]},
    )

    def fake_langchain_agent(**kwargs):
        raise LangChainAgentError("LangChain is required")

    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain_agent)

    result = gateway.chat(
        db_path=str(db_path),
        message="证券代码获取的逻辑在哪里",
        provider_name="openai-compatible",
        auto_retrieve=True,
    )

    assert "当前模型暂不可用" in result["reply"]
    assert "LangChain is required" in result["reply"]
    assert result["raw_response"]["fallback"] is True


def test_agent_gateway_tries_kimi_coding_provider_with_user_agent(tmp_path: Path, monkeypatch) -> None:
    api, db_path = _build_api(tmp_path)
    gateway = AgentGateway(
        indexer=api.indexer,
        qa=api.qa,
        providers={
            "openai-compatible": AgentProviderConfig(
                name="openai-compatible",
                label="通用智能体",
                adapter="openai-compatible",
                base_url="https://api.kimi.com/coding/v1/chat/completions",
                model="kimi-for-coding",
                api_key="stub-key",
                user_agent="claude-code/0.1.0",
            )
        },
        default_provider="openai-compatible",
    )
    called = {}

    def fake_intent(**kwargs):
        assert kwargs["config"].user_agent == "claude-code/0.1.0"
        return {"needs_retrieval": True, "reason": "business question", "suggested_tools": ["code"]}

    def fake_langchain(**kwargs):
        called.update(kwargs)
        assert kwargs["config"].user_agent == "claude-code/0.1.0"
        return {
            "content": "kimi answered",
            "usage": None,
            "raw_response": {"messages": []},
            "context_bundle": {"agent": "langchain_tool_calling_agent"},
        }

    monkeypatch.setattr("uses_indexer.agent_gateway.classify_retrieval_intent", fake_intent)
    monkeypatch.setattr("uses_indexer.agent_gateway.run_langchain_code_agent", fake_langchain)

    result = gateway.chat(
        db_path=str(db_path),
        message="功能号1包含哪些业务流程",
        provider_name="openai-compatible",
        auto_retrieve=True,
        max_search_rounds=1,
    )

    assert result["response_kind"] == "agent_chat"
    assert result["reply"] == "kimi answered"
    assert called["config"].user_agent == "claude-code/0.1.0"


def test_langchain_chat_openai_uses_provider_user_agent() -> None:
    llm = _build_chat_openai(
        AgentProviderConfig(
            name="openai-compatible",
            label="通用智能体",
            adapter="openai-compatible",
            base_url="https://api.kimi.com/coding/v1/chat/completions",
            model="kimi-for-coding",
            api_key="stub-key",
            user_agent="claude-code/0.1.0",
        )
    )

    assert llm.default_headers["User-Agent"] == "claude-code/0.1.0"
    assert llm.extra_body["thinking"] == {"type": "disabled"}


def test_langchain_code_tool_uses_object_id_fast_path(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)

    result = _query_code_like_index(
        indexer=api.indexer,
        db_path=str(db_path),
        query="功能号1包含哪些业务流程",
        limit=3,
        index_name="code",
    )

    assert result["payload"]["fast_path"] == "object_id_exact"
    assert result["payload"]["hits"][0]["object_id"] == "1"


def test_langchain_builds_assemble_evidence_context(tmp_path: Path) -> None:
    api, db_path = _build_api(tmp_path)

    result = _build_evidence_context(
        indexer=api.indexer,
        db_path=str(db_path),
        question="帮我回答一下功能1包含了哪些业务流程",
        limit=3,
    )

    assert result is not None
    assert result["trace"]["tool"] == "targeted_object_id_context"
    assert result["trace"]["object_id"] == "1"
    assert int(result["summary"]["evidence_count"]) >= 1
    assert "AF_SAMPLE" in result["llm_context"]


def test_http_server_serves_json(tmp_path: Path) -> None:
    api, _ = _build_api(tmp_path)
    server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler_class(api))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        host, port = server.server_address
        conn = HTTPConnection(host, port, timeout=5)

        conn.request("GET", "/")
        response = conn.getresponse()
        body = response.read().decode("utf-8")
        assert response.status == 200
        assert "USES Indexer Console" in body
        assert response.getheader("Content-Type", "").startswith("text/html")

        conn.request("GET", "/assets/styles.css")
        response = conn.getresponse()
        body = response.read().decode("utf-8")
        assert response.status == 200
        assert ":root" in body
        assert response.getheader("Content-Type", "").startswith("text/css")

        conn.request("GET", "/assets/app.js")
        response = conn.getresponse()
        body = response.read().decode("utf-8")
        assert response.status == 200
        assert "initializeConsole" in body

        conn.request("GET", "/favicon.ico")
        response = conn.getresponse()
        body = response.read()
        assert response.status == 204
        assert body == b""

        conn.request("GET", "/health")
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["service"] == "uses-indexer-api"

        conn.request("GET", "/agent/providers")
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["response_kind"] == "agent_providers"

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

        agent_payload = json.dumps({"message": "请解释失败路径", "provider": "hermes"})
        conn.request("POST", "/agent/chat", body=agent_payload, headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["response_kind"] == "agent_chat"

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
