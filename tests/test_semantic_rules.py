from __future__ import annotations

from pathlib import Path

from tests.test_indexer import _build_call_semantic_index, _build_mc_publish_index
from uses_indexer.parser import UftDslParser
from uses_indexer.semantic_recovery import (
    SEMANTIC_RULE_REGISTRY,
    classify_call_semantics,
    classify_mc_publish,
    coerce_call_semantics,
    format_call_edge_label,
    format_mc_topic_label,
)


def test_call_semantic_rules_are_exposed_through_public_registry() -> None:
    assert SEMANTIC_RULE_REGISTRY["call.local"]["call_kind"] == "local_function_call"
    assert "LS->AF" in SEMANTIC_RULE_REGISTRY["call.local"]["rule_pairs"]
    assert SEMANTIC_RULE_REGISTRY["call.rpc"]["call_kind"] == "rpc_call"
    assert "AF->LS" in SEMANTIC_RULE_REGISTRY["call.rpc"]["rule_pairs"]
    assert SEMANTIC_RULE_REGISTRY["message.mc_publish"]["publish_modes"]["同步消息发布"] == "sync"


def test_public_call_semantic_helpers_classify_and_format() -> None:
    local = classify_call_semantics("LS_CALLER", "AF_TARGET")
    rpc = coerce_call_semantics({}, source_name="AF_CALLER", target_name="LS_REMOTE")

    assert local["call_kind"] == "local_function_call"
    assert local["call_rule"] == "LS->AF"
    assert rpc["call_kind"] == "rpc_call"
    assert format_call_edge_label({"procedure_name": "LS_REMOTE", **rpc}) == "LS_REMOTE(系统间RPC调用 AF->LS)"


def test_public_mc_publish_helpers_classify_and_format(tmp_path: Path) -> None:
    indexer, db_path = _build_mc_publish_index(tmp_path)
    summary = indexer.summarize_db(db_path)
    parsed = UftDslParser().parse_path(tmp_path / "mc_src" / "LS_MC_PUBLISH.uftservice")
    action_statement = next(
        statement
        for statement in parsed.statements
        if statement.kind == "action" and statement.name == "同步消息发布"
    )

    publish = classify_mc_publish(action_statement)

    assert publish is not None
    assert publish["publish_mode"] == "sync"
    assert publish["communication_kind"] == "cross_core_message_publish"
    assert format_mc_topic_label(publish) == "CNST_MC_UFT_PUBSYNC(消息中心主题发布 同步发布)"
    assert summary["semantic_rule_registry"]["message.mc_publish"]["actions"] == ["同步消息发布", "消息发布"]


def test_summary_exposes_semantic_rule_registry(tmp_path: Path) -> None:
    indexer, db_path = _build_call_semantic_index(tmp_path)

    summary = indexer.summarize_db(db_path)

    assert "semantic_rule_registry" in summary
    assert summary["semantic_rule_registry"]["call.local"]["label"] == "本地函数调用"
