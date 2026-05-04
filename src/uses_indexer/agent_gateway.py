from __future__ import annotations

import json
import os
import re
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import bootstrap_env
from .index_catalog import INDEX_DEFINITIONS
from .langchain_agent import LangChainAgentError, classify_retrieval_intent, run_langchain_code_agent
from .llm import LlmService
from .logging_system import log_business, log_error
from .qa import CodebaseQA
from .indexer import SQLiteIndexer
from .table_indexer import TableIndexer


class AgentConfigError(Exception):
    pass


class AgentRequestError(Exception):
    pass


@dataclass(slots=True)
class AgentProviderConfig:
    name: str
    label: str
    adapter: str
    base_url: str
    model: str
    api_key: str | None = None
    temperature: float = 0.1
    max_tokens: int = 1600
    timeout_seconds: float = 90.0
    max_retries: int = 0
    retry_backoff_seconds: float = 1.0
    description: str = ""
    user_agent: str | None = None


@dataclass(slots=True)
class AgentAttachment:
    name: str
    media_kind: str
    mime_type: str
    size_bytes: int = 0
    text_content: str | None = None
    data_url: str | None = None


class AgentGateway:
    def __init__(
        self,
        *,
        indexer: SQLiteIndexer,
        qa: CodebaseQA,
        llm_service: LlmService | None = None,
        providers: dict[str, AgentProviderConfig] | None = None,
        default_provider: str | None = None,
    ) -> None:
        self.indexer = indexer
        self.qa = qa
        self.llm_service = llm_service or LlmService.from_env()
        self.providers = providers or {}
        self.default_provider = default_provider or next(iter(self.providers.keys()), None)

    @classmethod
    def from_env(cls, *, indexer: SQLiteIndexer, qa: CodebaseQA) -> "AgentGateway":
        bootstrap_env()
        llm_service = LlmService.from_env()

        providers: dict[str, AgentProviderConfig] = {}

        # 1. 从 LlmService 的 provider 列表自动生成 agent provider
        _LLM_PROVIDER_LABELS: dict[str, tuple[str, str]] = {
            "kimi": ("Kimi", "Moonshot Kimi 大模型"),
            "xiaomi": ("Xiaomi MiMo", "小米 MiMo 大模型"),
        }
        for llm_cfg in llm_service.list_providers():
            name = llm_cfg["name"]
            label, description = _LLM_PROVIDER_LABELS.get(name, (name, f"{name} LLM"))
            full_cfg = llm_service.get_config(name)
            providers[name] = AgentProviderConfig(
                name=name,
                label=label,
                adapter="openai-compatible",
                base_url=llm_cfg["base_url"],
                model=llm_cfg["model"],
                api_key=full_cfg.api_key if full_cfg else None,
                temperature=full_cfg.temperature if full_cfg else 0.1,
                max_tokens=full_cfg.max_tokens if full_cfg else 1600,
                timeout_seconds=full_cfg.timeout_seconds if full_cfg else 90.0,
                max_retries=full_cfg.max_retries if full_cfg else 0,
                retry_backoff_seconds=full_cfg.retry_backoff_seconds if full_cfg else 1.0,
                description=description,
                user_agent=full_cfg.user_agent if full_cfg else None,
            )

        # 2. 允许 USES_INDEXER_AGENT_* 覆盖或新增
        for prefix, name, label, description in (
            ("USES_INDEXER_AGENT_OPENAI", "openai-compatible", "通用智能体", "适合对接任意 OpenAI-compatible 聊天服务"),
            ("USES_INDEXER_AGENT_HERMES", "hermes", "Hermes", "适合挂接你自己部署的 Hermes 服务"),
            ("USES_INDEXER_AGENT_OPENCLAW", "openclaw", "OpenClaw", "适合挂接你自己部署的 OpenClaw 服务"),
        ):
            config = _provider_from_env(prefix=prefix, name=name, label=label, description=description)
            if config is not None:
                providers[name] = config

        # 3. 确定默认 provider
        default_provider = os.getenv("USES_INDEXER_AGENT_DEFAULT_PROVIDER", "").strip() or None
        if default_provider and default_provider not in providers:
            default_provider = None
        if default_provider is None:
            # 优先用 LlmService 的默认 provider，再 fallback 到第一个
            if llm_service.default_provider in providers:
                default_provider = llm_service.default_provider
            else:
                default_provider = next(iter(providers.keys()), None)

        return cls(indexer=indexer, qa=qa, llm_service=llm_service, providers=providers, default_provider=default_provider)

    def list_providers(self) -> dict[str, Any]:
        items = [
            {
                "name": config.name,
                "label": config.label,
                "adapter": config.adapter,
                "configured": True,
                "default": config.name == self.default_provider,
                "description": config.description,
                "model": config.model,
                "base_url": config.base_url,
            }
            for config in self.providers.values()
        ]
        return {
            "response_kind": "agent_providers",
            "default_provider": self.default_provider,
            "count": len(items),
            "items": items,
        }

    def chat(
        self,
        *,
        db_path: str,
        metadata_db_path: str | None = None,
        table_db_path: str | None = None,
        message: str,
        provider_name: str | None = None,
        history: list[dict[str, str]] | None = None,
        include_retrieval: bool = True,
        include_evidence: bool = True,
        include_answer_draft: bool = False,
        auto_retrieve: bool = False,
        max_search_rounds: int = 4,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
        system_prompt: str | None = None,
        attachments: list[dict[str, Any]] | None = None,
        provider_override: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        attachment_models = _coerce_attachments(attachments)
        config = self._resolve_provider(provider_name, provider_override)
        intent_result: dict[str, Any] | None = None
        if auto_retrieve:
            try:
                intent_result = classify_retrieval_intent(config=config, question=message, history=history)
                intent_result = _normalize_retrieval_intent(message, intent_result)
            except LangChainAgentError as exc:
                intent_result = _fallback_retrieval_intent(message, reason=f"intent_langchain_unavailable: {exc}")
                log_error(
                    event="agent_intent_classification_unavailable",
                    message=str(exc),
                    exc=exc,
                    context={
                        "provider": config.name,
                        "model": config.model,
                        "base_url": config.base_url,
                        "fallback_needs_retrieval": intent_result["needs_retrieval"],
                    },
                )
            except Exception as exc:
                intent_result = _fallback_retrieval_intent(message, reason=f"intent_llm_failed: {exc}")
                log_error(
                    event="agent_intent_classification_failed",
                    message=str(exc),
                    exc=exc,
                    context={
                        "provider": config.name,
                        "model": config.model,
                        "base_url": config.base_url,
                        "fallback_needs_retrieval": intent_result["needs_retrieval"],
                    },
                )

            if not bool(intent_result.get("needs_retrieval")):
                auto_retrieve = False
                include_retrieval = False
                include_evidence = False
                include_answer_draft = False
                system_prompt = system_prompt or _default_general_system_prompt()
            else:
                if attachment_models:
                    message = message + "\n\n附件摘要:\n" + _format_attachment_prompt(attachment_models)
                started_at = time.time()
                try:
                    model_response = run_langchain_code_agent(
                        config=config,
                        indexer=self.indexer,
                        db_path=db_path,
                        metadata_db_path=metadata_db_path,
                        table_db_path=table_db_path,
                        question=message,
                        history=history,
                        limit=limit,
                        max_iterations=max_search_rounds,
                        system_prompt=system_prompt,
                        llm_service=self.llm_service,
                        provider=config.name,
                    )
                except LangChainAgentError as exc:
                    log_error(
                        event="langchain_agent_unavailable",
                        message=str(exc),
                        exc=exc,
                        context={
                            "provider": config.name,
                            "model": config.model,
                            "base_url": config.base_url,
                            "message": message,
                        },
                    )
                    return self._build_auto_retrieve_fallback_response(
                        db_path=db_path,
                        metadata_db_path=metadata_db_path,
                        table_db_path=table_db_path,
                        message=message,
                        config=config,
                        intent_result=intent_result,
                        provider_error=str(exc),
                        started_at=started_at,
                        limit=limit,
                        context_window=context_window,
                        related_limit=related_limit,
                        max_search_rounds=max_search_rounds,
                        fallback_reason="langchain_unavailable",
                    )
                except Exception as exc:
                    log_error(
                        event="langchain_agent_chat_failed",
                        message=str(exc),
                        exc=exc,
                        context={
                            "provider": config.name,
                            "model": config.model,
                            "base_url": config.base_url,
                            "message": message,
                        },
                    )
                    return self._build_auto_retrieve_fallback_response(
                        db_path=db_path,
                        metadata_db_path=metadata_db_path,
                        table_db_path=table_db_path,
                        message=message,
                        config=config,
                        intent_result=intent_result,
                        provider_error=str(exc),
                        started_at=started_at,
                        limit=limit,
                        context_window=context_window,
                        related_limit=related_limit,
                        max_search_rounds=max_search_rounds,
                        fallback_reason="provider_unavailable",
                    )
                latency_ms = int((time.time() - started_at) * 1000)
                context_bundle = dict(model_response.get("context_bundle") or {})
                context_bundle["intent"] = intent_result
                log_business(
                    "agent_chat",
                    provider=config.name,
                    adapter=config.adapter,
                    model=config.model,
                    base_url=config.base_url,
                    message=message,
                    latency_ms=latency_ms,
                    auto_retrieve=True,
                    orchestration="langchain",
                    max_search_rounds=max_search_rounds,
                    attachment_count=len(attachment_models),
                    usage=model_response.get("usage"),
                )
                return {
                    "response_kind": "agent_chat",
                    "provider": {
                        "name": config.name,
                        "label": config.label,
                        "adapter": config.adapter,
                        "model": config.model,
                        "base_url": config.base_url,
                    },
                    "message": message,
                    "reply": model_response["content"],
                    "latency_ms": latency_ms,
                    "context_bundle": context_bundle,
                    "usage": model_response.get("usage"),
                    "raw_response": model_response["raw_response"],
                }

        context_bundle = self._build_context(
            db_path=db_path,
            message=message,
            include_retrieval=include_retrieval,
            include_evidence=include_evidence,
            include_answer_draft=include_answer_draft,
            auto_retrieve=auto_retrieve,
            max_search_rounds=max_search_rounds,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
        )
        if intent_result is not None:
            context_bundle["intent"] = intent_result
        if attachment_models:
            context_bundle["attachments"] = [
                {
                    "name": item.name,
                    "media_kind": item.media_kind,
                    "mime_type": item.mime_type,
                    "size_bytes": item.size_bytes,
                    "text_excerpt": _truncate_attachment_text(item.text_content),
                }
                for item in attachment_models
            ]

        messages: list[dict[str, Any]] = [
            {
                "role": "system",
                "content": system_prompt.strip() if isinstance(system_prompt, str) and system_prompt.strip() else _default_system_prompt(),
            }
        ]
        if history:
            messages.extend(_sanitize_history(history))
        messages.append(_build_user_prompt(message=message, context_bundle=context_bundle, attachments=attachment_models))

        started_at = time.time()
        try:
            llm_result = self.llm_service.chat(
                messages,
                provider=config.name,
                model=config.model,
                temperature=config.temperature,
                max_tokens=config.max_tokens,
                timeout=config.timeout_seconds,
            )
            model_response = {
                "content": llm_result["content"],
                "usage": llm_result["usage"],
                "raw_response": llm_result["raw_response"],
            }
        except Exception as exc:
            log_error(
                event="agent_chat_failed",
                message=str(exc),
                exc=exc,
                context={
                    "provider": config.name,
                    "adapter": config.adapter,
                    "model": config.model,
                    "base_url": config.base_url,
                    "message": message,
                },
            )
            raise
        latency_ms = int((time.time() - started_at) * 1000)
        log_business(
            "agent_chat",
            provider=config.name,
            adapter=config.adapter,
            model=config.model,
            base_url=config.base_url,
            message=message,
            latency_ms=latency_ms,
            include_retrieval=include_retrieval,
            include_evidence=include_evidence,
            include_answer_draft=include_answer_draft,
            auto_retrieve=auto_retrieve,
            max_search_rounds=max_search_rounds,
            attachment_count=len(attachment_models),
            usage=model_response.get("usage"),
        )

        return {
            "response_kind": "agent_chat",
            "provider": {
                "name": config.name,
                "label": config.label,
                "adapter": config.adapter,
                "model": config.model,
                "base_url": config.base_url,
            },
            "message": message,
            "reply": model_response["content"],
            "latency_ms": latency_ms,
            "context_bundle": context_bundle,
            "usage": model_response.get("usage"),
            "raw_response": model_response["raw_response"],
        }

    def analyze(
        self,
        *,
        db_path: str,
        question: str,
        provider_name: str | None = None,
        provider_override: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """深度分析：执行多步骤调查流程，每步原始数据均返回。"""
        from .langchain_agent import run_deep_analysis

        config = self._resolve_provider(provider_name, provider_override)
        return run_deep_analysis(
            config=config,
            indexer=self.indexer,
            db_path=db_path,
            question=question,
            llm_service=self.llm_service,
            provider=config.name,
        )

    def _build_auto_retrieve_fallback_response(
        self,
        *,
        db_path: str,
        metadata_db_path: str | None,
        table_db_path: str | None,
        message: str,
        config: AgentProviderConfig,
        intent_result: dict[str, Any],
        provider_error: str,
        started_at: float,
        limit: int,
        context_window: int,
        related_limit: int,
        max_search_rounds: int,
        fallback_reason: str = "provider_unavailable",
    ) -> dict[str, Any]:
        auto_search = self._build_auto_search_context(
            db_path=db_path,
            metadata_db_path=metadata_db_path,
            table_db_path=table_db_path,
            message=message,
            limit=limit,
            context_window=context_window,
            related_limit=related_limit,
            max_search_rounds=max_search_rounds,
        )
        context_bundle = {
            "db_path": db_path,
            "question": message,
            "options": {
                "auto_retrieve": True,
                "max_search_rounds": max_search_rounds,
                "limit": limit,
                "context_window": context_window,
                "related_limit": related_limit,
            },
            "intent": intent_result,
            "auto_search": auto_search,
            "fallback": {
                "reason": fallback_reason,
                "error": provider_error,
            },
        }
        latency_ms = int((time.time() - started_at) * 1000)
        return {
            "response_kind": "agent_chat",
            "provider": {
                "name": config.name,
                "label": config.label,
                "adapter": config.adapter,
                "model": config.model,
                "base_url": config.base_url,
            },
            "message": message,
            "reply": _build_auto_retrieve_fallback_reply(auto_search, provider_error, fallback_reason=fallback_reason),
            "latency_ms": latency_ms,
            "context_bundle": context_bundle,
            "usage": None,
            "raw_response": {
                "fallback": True,
                "error": provider_error,
            },
        }

    def _resolve_provider(self, provider_name: str | None, provider_override: dict[str, Any] | None = None) -> AgentProviderConfig:
        if provider_override:
            return _provider_from_override(provider_override, provider_name=provider_name)

        target = provider_name or self.default_provider
        if not target:
            raise AgentConfigError(
                "No agent provider is configured. Set USES_INDEXER_AGENT_OPENAI_* or USES_INDEXER_AGENT_HERMES_* / USES_INDEXER_AGENT_OPENCLAW_*."
            )
        config = self.providers.get(target)
        if config is None:
            available = ", ".join(sorted(self.providers.keys())) or "none"
            raise AgentConfigError(f"Unknown agent provider: {target}. Available providers: {available}")
        return config

    def _build_context(
        self,
        *,
        db_path: str,
        message: str,
        include_retrieval: bool,
        include_evidence: bool,
        include_answer_draft: bool,
        auto_retrieve: bool = False,
        max_search_rounds: int = 4,
        limit: int = 6,
        context_window: int = 2,
        related_limit: int = 3,
    ) -> dict[str, Any]:
        bundle: dict[str, Any] = {
            "db_path": db_path,
            "question": message,
            "options": {
                "include_retrieval": include_retrieval,
                "include_evidence": include_evidence,
                "include_answer_draft": include_answer_draft,
                "auto_retrieve": auto_retrieve,
                "max_search_rounds": max_search_rounds,
                "limit": limit,
                "context_window": context_window,
                "related_limit": related_limit,
            },
        }
        if auto_retrieve:
            bundle["auto_search"] = self._build_auto_search_context(
                db_path=db_path,
                metadata_db_path=None,
                table_db_path=None,
                message=message,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
                max_search_rounds=max_search_rounds,
            )
            return bundle

        if include_retrieval:
            query = self.indexer.query_index(db_path, message, limit=limit, debug=True, expand_downstream=True)
            bundle["retrieval"] = {
                "hit_count": query.get("hit_count", 0),
                "candidate_count": query.get("candidate_count", 0),
                "hits": [
                    {
                        "procedure_name": hit.get("procedure_name"),
                        "file_path": hit.get("file_path"),
                        "retrieval_source": hit.get("retrieval_source") or hit.get("match_source"),
                        "matched_text": hit.get("matched_text") or hit.get("excerpt"),
                    }
                    for hit in (query.get("hits") or [])[: min(limit, 6)]
                ],
                "query_analysis": query.get("debug", {}).get("query_analysis"),
            }
        if include_evidence:
            evidence = self.indexer.assemble_evidence(
                db_path,
                message,
                limit=limit,
                context_window=context_window,
                related_limit=related_limit,
                debug=True,
            )
            bundle["evidence"] = {
                "evidence_count": evidence.get("evidence_count", 0),
                "items": [
                    {
                        "procedure_name": item.get("procedure_name"),
                        "file_path": item.get("file_path"),
                        "line_start": item.get("line_start"),
                        "matched_text": item.get("matched_text") or item.get("excerpt"),
                        "related_tables": item.get("related_tables"),
                        "related_calls": item.get("related_calls"),
                    }
                    for item in (evidence.get("evidence") or [])[: min(limit, 4)]
                ],
                "pruning": evidence.get("debug", {}).get("pruning"),
            }
        if include_answer_draft:
            ask = self.qa.ask(
                db_path,
                message,
                evidence_limit=limit,
                context_window=context_window,
                related_limit=related_limit,
            )
            draft_answer = dict(ask.get("draft_answer") or {})
            bundle["answer_draft"] = {
                "status": draft_answer.get("status"),
                "text": draft_answer.get("answer"),
                "query_type": draft_answer.get("query_type"),
                "confidence": draft_answer.get("confidence"),
                "review_required": bool(draft_answer.get("review_required")),
                "decision": dict(draft_answer.get("decision") or {}),
                "primary_candidate": dict(draft_answer.get("primary_candidate") or {}),
                "secondary_candidates": list(draft_answer.get("secondary_candidates") or []),
                "summary_points": list(draft_answer.get("summary_points") or [])[:3],
                "uncertainties": list(draft_answer.get("uncertainties") or [])[:3],
            }
        return bundle

    def _build_auto_search_context(
        self,
        *,
        db_path: str,
        metadata_db_path: str | None = None,
        table_db_path: str | None = None,
        message: str,
        limit: int,
        context_window: int,
        related_limit: int,
        max_search_rounds: int,
    ) -> dict[str, Any]:
        del context_window, related_limit
        max_rounds = max(1, min(int(max_search_rounds or 3), 5))
        query_plan = _build_query_plan(message, max_rounds=max_rounds)
        index_paths = _discover_agent_index_paths(
            db_path,
            metadata_db_path=metadata_db_path,
            table_db_path=table_db_path,
        )
        search_results: list[dict[str, Any]] = []
        selected_hits: list[dict[str, Any]] = []
        table_context: list[dict[str, Any]] = []
        rounds_used = 0

        for round_index, query_text in enumerate(query_plan, start=1):
            rounds_used = round_index
            round_result: dict[str, Any] = {
                "round": round_index,
                "query": query_text,
                "indexes": [],
            }

            for index_key in _select_lightweight_indexes(message, index_paths):
                path = index_paths.get(index_key)
                if not path:
                    continue
                if index_key == "code" and query_text.isdigit():
                    fast_hits = _query_object_id_fast(path, query_text, limit=max(limit, 8))
                    if fast_hits:
                        round_result["indexes"].append({
                            "index": index_key,
                            "db_path": path,
                            "hit_count": len(fast_hits),
                            "candidate_count": len(fast_hits),
                            "top_hits": fast_hits[: min(5, limit)],
                            "fast_path": "object_id_exact",
                        })
                        for hit in fast_hits[: max(3, min(limit, 8))]:
                            selected_hits.append({
                                "index": index_key,
                                "query": query_text,
                                **hit,
                            })
                        continue
                try:
                    query_result = self.indexer.query_index(path, query_text, limit=max(limit, 8), debug=True)
                except Exception as exc:
                    round_result["indexes"].append({
                        "index": index_key,
                        "db_path": path,
                        "error": str(exc),
                    })
                    continue

                hits = list(query_result.get("hits") or [])
                round_result["indexes"].append({
                    "index": index_key,
                    "db_path": path,
                    "hit_count": query_result.get("hit_count", 0),
                    "candidate_count": query_result.get("candidate_count", 0),
                    "top_hits": [_summarize_code_hit(hit) for hit in hits[: min(5, limit)]],
                })
                for hit in hits[: max(3, min(limit, 8))]:
                    selected_hits.append({
                        "index": index_key,
                        "query": query_text,
                        **_summarize_code_hit(hit),
                    })

            table_path = index_paths.get("table")
            if table_path and _should_query_table_index(message, selected_hits):
                try:
                    table_result = TableIndexer().query_index(table_path, query_text, limit=max(5, limit))
                    table_hits = list(table_result.get("hits") or [])
                    round_result["indexes"].append({
                        "index": "table",
                        "db_path": table_path,
                        "hit_count": table_result.get("hit_count", 0),
                        "top_hits": [_summarize_table_hit(hit) for hit in table_hits[:5]],
                    })
                    for hit in table_hits[:5]:
                        table_context.append({
                            "index": "table",
                            "query": query_text,
                            **_summarize_table_hit(hit),
                        })
                except Exception as exc:
                    round_result["indexes"].append({
                        "index": "table",
                        "db_path": table_path,
                        "error": str(exc),
                    })

            search_results.append(round_result)
            if _auto_search_is_sufficient(message, selected_hits, table_context, min_code_items=3):
                break

        selected_hits = _dedupe_context_items(selected_hits)[: max(8, limit * 2)]
        table_context = _dedupe_context_items(table_context, key_fields=("table_name", "path"))[: max(6, limit)]

        return {
            "search_decision": {
                "needs_search": _question_needs_code_search(message),
                "strategy": "lightweight_query_index",
                "tool_equivalent": "python3 -m uses_indexer query-index / query-table-index",
                "stop_reason": "sufficient_context" if _auto_search_is_sufficient(message, selected_hits, table_context, min_code_items=3) else "round_limit_reached",
                "rounds_used": rounds_used,
                "round_limit": max_rounds,
            },
            "searched_indexes": {
                key: path
                for key, path in index_paths.items()
                if key in {"code", "metadata", "full", "table"}
            },
            "query_plan": query_plan[:rounds_used],
            "rounds": search_results,
            "selected_code_and_metadata_context": selected_hits,
            "selected_table_context": table_context,
        }


def _discover_agent_index_paths(
    primary_db_path: str,
    *,
    metadata_db_path: str | None = None,
    table_db_path: str | None = None,
) -> dict[str, str]:
    primary = Path(primary_db_path).expanduser()
    examples_dir = primary.parent if primary.parent.exists() else Path.cwd() / "examples"
    paths: dict[str, str] = {"primary": str(primary)}
    if metadata_db_path:
        paths["metadata"] = str(Path(metadata_db_path).expanduser())
    if table_db_path:
        paths["table"] = str(Path(table_db_path).expanduser())

    primary_name = primary.name
    for key, definition in INDEX_DEFINITIONS.items():
        if key in paths:
            continue
        candidate = examples_dir / definition.db_name
        if candidate.exists():
            paths[key] = str(candidate)
        elif primary.exists() and primary_name == definition.db_name:
            paths[key] = str(primary)

    if "code" not in paths and primary.exists():
        paths["code"] = str(primary)
    return paths


def _question_needs_code_search(message: str) -> bool:
    text = message.strip()
    if not text:
        return False
    code_markers = [
        "代码", "逻辑", "流程", "功能", "功能号", "接口", "服务", "表", "字段", "元数据",
        "存储过程", "过程", "调用", "哪里", "如何实现", "怎么实现", "报错", "菜单",
    ]
    return bool(re.search(r"\d{4,}|[A-Z]{1,4}_[A-Z0-9_]+|@[A-Za-z0-9_]+", text)) or any(marker in text for marker in code_markers)


def _fallback_retrieval_intent(message: str, *, reason: str) -> dict[str, Any]:
    needs_retrieval = _question_needs_code_search(message)
    suggested_tools: list[str] = []
    if needs_retrieval:
        suggested_tools.append("code")
        if _mentions_metadata(message):
            suggested_tools.append("metadata")
        if any(marker in message for marker in ("表", "字段", "索引", "表结构", "table")):
            suggested_tools.append("table")
    return {
        "needs_retrieval": needs_retrieval,
        "reason": reason,
        "suggested_tools": suggested_tools,
        "source": "local_rule_fallback",
    }


def _normalize_retrieval_intent(message: str, intent_result: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(intent_result)
    if _question_needs_code_search(message) and not bool(normalized.get("needs_retrieval")):
        tools = list(normalized.get("suggested_tools") or [])
        if "code" not in tools:
            tools.insert(0, "code")
        if _mentions_metadata(message) and "metadata" not in tools:
            tools.append("metadata")
        if any(marker in message for marker in ("表", "字段", "索引", "表结构", "table")) and "table" not in tools:
            tools.append("table")
        normalized.update({
            "needs_retrieval": True,
            "reason": f"local_rule_override: {normalized.get('reason') or 'llm_intent_false_or_empty'}",
            "suggested_tools": tools,
            "source": "llm_with_local_rule_override",
        })
    return normalized


def _build_auto_retrieve_fallback_reply(
    auto_search: dict[str, Any],
    provider_error: str,
    *,
    fallback_reason: str,
) -> str:
    selected = list(auto_search.get("selected_code_and_metadata_context") or [])
    tables = list(auto_search.get("selected_table_context") or [])
    searched = dict(auto_search.get("searched_indexes") or {})
    decision = dict(auto_search.get("search_decision") or {})
    if fallback_reason == "provider_requires_coding_agent_runtime":
        lines = [
            "当前智能助手已切换为本地索引检索模式。",
            "",
            f"说明：{_compact_text(provider_error, limit=260)}",
            f"检索轮次：{decision.get('rounds_used', 0)}/{decision.get('round_limit', 0)}",
        ]
    else:
        lines = [
            "当前模型暂不可用，已返回本地索引检索结果摘要，避免本次请求中断。",
            "",
            f"说明：{_compact_text(provider_error, limit=260)}",
            f"检索轮次：{decision.get('rounds_used', 0)}/{decision.get('round_limit', 0)}",
        ]
    if searched:
        lines.append("已检索索引：" + "、".join(f"{key}={path}" for key, path in searched.items()))
    if selected:
        lines.append("")
        lines.append("代码/元数据命中：")
        for index, item in enumerate(selected[:8], start=1):
            title = item.get("procedure_name") or item.get("chinese_name") or item.get("object_id") or "未知过程"
            file_path = item.get("file_path") or "-"
            matched = item.get("matched_text") or ""
            lines.append(f"{index}. {title} | {file_path}")
            if matched:
                lines.append(f"   线索：{_compact_text(matched, limit=180)}")
    if tables:
        lines.append("")
        lines.append("表结构命中：")
        for index, item in enumerate(tables[:5], start=1):
            table_name = item.get("table_name") or "未知表"
            chinese_name = item.get("chinese_name") or ""
            lines.append(f"{index}. {table_name} {chinese_name}".rstrip())
    if not selected and not tables:
        lines.append("")
        lines.append("本地索引没有检索到足够结果，请检查索引库路径或换一个更具体的问题。")
    return "\n".join(lines)


def _build_query_plan(message: str, *, max_rounds: int) -> list[str]:
    text = " ".join(message.strip().split())
    identifiers = _extract_search_identifiers(text)
    queries: list[str] = []

    def add(query: str) -> None:
        normalized = " ".join(query.strip().split())
        if normalized and normalized not in queries:
            queries.append(normalized)

    for ident in identifiers:
        add(ident)
        if ident.isdigit():
            add(f"功能号 {ident}")
            add(f"{ident} 业务流程")
            add(f"{ident} 菜单 接口 服务")
    add(text)
    for ident in identifiers:
        if "_" in ident and not ident.startswith("@"):
            add(f"{ident} 调用 入口")
            add(f"{ident} 表 字段 元数据")
    if "表" in text or "字段" in text:
        for ident in identifiers:
            add(f"{ident} 表结构 字段 索引")
    return queries[:max_rounds]


def _select_lightweight_indexes(message: str, index_paths: dict[str, str]) -> list[str]:
    indexes = ["code"]
    text = message.lower()
    if _mentions_metadata(message) and "metadata" in index_paths:
        indexes.append("metadata")
    if "code" not in index_paths and "full" in index_paths:
        indexes.append("full")
    if "full" in index_paths and ("metadata" not in index_paths) and any(marker in text for marker in ("元数据", "字段", "常量", "错误号", "主题")):
        indexes.append("full")
    return [item for item in indexes if item in index_paths]


def _mentions_metadata(message: str) -> bool:
    return any(marker in message for marker in ("元数据", "字段", "常量", "错误号", "宏", "主题", "topic", "metadata"))


def _should_query_table_index(message: str, selected_hits: list[dict[str, Any]]) -> bool:
    if any(marker in message for marker in ("表", "字段", "索引", "表结构", "table")):
        return True
    haystack = json.dumps(selected_hits[:8], ensure_ascii=False).lower()
    return bool(re.search(r"\b[a-z][a-z0-9_]{3,}\b", haystack)) and any(marker in haystack for marker in ("table", "表", "字段"))


def _extract_search_identifiers(message: str) -> list[str]:
    identifiers: list[str] = []
    patterns = [
        r"(?:(?<=功能号)|(?<=功能))\d+|\d{4,}",
        r"\b[A-Z]{1,6}_[A-Z0-9_]{2,}\b",
        r"@[A-Za-z_][A-Za-z0-9_]*",
        r"\b[a-zA-Z][a-zA-Z0-9_]{2,}\b",
    ]
    for pattern in patterns:
        for match in re.findall(pattern, message):
            if match not in identifiers:
                identifiers.append(match)
    return identifiers[:8]


def _query_object_id_fast(db_path: str, object_id: str, *, limit: int) -> list[dict[str, Any]]:
    safe_limit = max(1, min(int(limit or 8), 20))
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            rows = conn.execute(
                """
                SELECT
                  p.name AS procedure_name,
                  p.chinese_name AS chinese_name,
                  p.object_id AS object_id,
                  f.path AS file_path
                FROM procedures p
                JOIN files f ON f.id = p.file_id
                WHERE p.object_id = ?
                ORDER BY p.name
                LIMIT ?
                """,
                (object_id, safe_limit),
            ).fetchall()
    except sqlite3.Error:
        return []
    return [
        {
            "procedure_name": row["procedure_name"],
            "chinese_name": row["chinese_name"],
            "object_id": row["object_id"],
            "file_path": row["file_path"],
            "retrieval_source": "object_id_exact",
            "matched_text": row["chinese_name"] or object_id,
        }
        for row in rows
    ]


def _auto_search_is_sufficient(
    message: str,
    selected_context: list[dict[str, Any]],
    table_context: list[dict[str, Any]],
    *,
    min_code_items: int,
) -> bool:
    identifiers = _extract_search_identifiers(message)
    numeric_identifiers = {item for item in identifiers if item.isdigit()}
    if any(str(item.get("retrieval_source") or "") == "object_id_exact" for item in selected_context):
        return True
    if len(selected_context) >= min_code_items and table_context:
        return True
    if not identifiers:
        return len(selected_context) >= min_code_items
    haystack = json.dumps(selected_context + table_context, ensure_ascii=False).lower()
    matched_identifiers = [item for item in identifiers if item.lower() in haystack]
    return len(selected_context) >= min_code_items and bool(matched_identifiers)


def _summarize_code_hit(hit: dict[str, Any]) -> dict[str, Any]:
    return {
        "procedure_name": hit.get("procedure_name"),
        "chinese_name": hit.get("chinese_name"),
        "object_id": hit.get("object_id"),
        "file_path": hit.get("file_path"),
        "retrieval_source": hit.get("retrieval_source") or hit.get("match_source"),
        "matched_text": _compact_text(hit.get("matched_text") or hit.get("excerpt")),
    }


def _summarize_evidence_item(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "procedure_name": item.get("procedure_name"),
        "chinese_name": item.get("chinese_name"),
        "object_id": item.get("object_id"),
        "file_path": item.get("file_path"),
        "line_start": item.get("line_start"),
        "line_end": item.get("line_end"),
        "retrieval_source": item.get("retrieval_source"),
        "matched_text": _compact_text(item.get("matched_text")),
        "excerpt": _compact_text(item.get("excerpt"), limit=900),
        "reasons": list(item.get("reasons") or [])[:6],
        "related_context": _summarize_related_context(dict(item.get("related_context") or {})),
    }


def _summarize_related_context(related: dict[str, Any]) -> dict[str, Any]:
    return {
        "calls": list(related.get("related_calls") or [])[:5],
        "callers": list(related.get("caller_context") or [])[:5],
        "tables": list(related.get("related_tables") or [])[:5],
    }


def _summarize_table_hit(hit: dict[str, Any]) -> dict[str, Any]:
    return {
        "table_name": hit.get("table_name"),
        "chinese_name": hit.get("chinese_name"),
        "object_id": hit.get("object_id"),
        "space": hit.get("space"),
        "path": hit.get("path"),
        "field_count": hit.get("field_count"),
        "index_count": hit.get("index_count"),
    }


def _dedupe_context_items(
    items: list[dict[str, Any]],
    *,
    key_fields: tuple[str, ...] = ("index", "procedure_name", "file_path", "line_start"),
) -> list[dict[str, Any]]:
    seen: set[tuple[str, ...]] = set()
    deduped: list[dict[str, Any]] = []
    for item in items:
        key = tuple(str(item.get(field) or "") for field in key_fields)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(item)
    return deduped


def _compact_text(value: object, *, limit: int = 420) -> str:
    text = " ".join(str(value or "").split())
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def _provider_from_env(*, prefix: str, name: str, label: str, description: str) -> AgentProviderConfig | None:
    enabled_value = os.getenv(f"{prefix}_ENABLED")
    if enabled_value is not None and enabled_value.strip().lower() in {"0", "false", "no", "off"}:
        return None

    model = (os.getenv(f"{prefix}_MODEL") or "").strip()
    base_url = (os.getenv(f"{prefix}_BASE_URL") or "").strip()
    adapter = (os.getenv(f"{prefix}_ADAPTER", "openai-compatible") or "openai-compatible").strip()
    if not model or not base_url:
        return None
    if adapter != "openai-compatible":
        raise AgentConfigError(f"Unsupported agent adapter for {name}: {adapter}")

    return AgentProviderConfig(
        name=name,
        label=os.getenv(f"{prefix}_LABEL", label).strip() or label,
        adapter=adapter,
        base_url=base_url,
        model=model,
        api_key=(os.getenv(f"{prefix}_API_KEY") or "").strip() or None,
        temperature=float(os.getenv(f"{prefix}_TEMPERATURE", "0.1")),
        max_tokens=int(os.getenv(f"{prefix}_MAX_TOKENS", "1600")),
        timeout_seconds=float(os.getenv(f"{prefix}_TIMEOUT", "90")),
        max_retries=int(os.getenv(f"{prefix}_MAX_RETRIES", "0")),
        retry_backoff_seconds=float(os.getenv(f"{prefix}_RETRY_BACKOFF", "1.0")),
        description=description,
        user_agent=(os.getenv(f"{prefix}_USER_AGENT") or "").strip() or None,
    )


def _default_system_prompt() -> str:
    return (
        "你是当前 USES Indexer 控制台里的代码库智能体。"
        "当用户询问功能号、代码逻辑、业务流程、表结构、元数据、调用链或错误处理时，"
        "系统会自动提供多索引检索上下文；你必须优先依据这些上下文整合回答，"
        "不要要求用户自己先提供检索结果。"
        "回答时要明确引用过程名、文件路径、表名、元数据线索和不确定点。"
    )


def _default_general_system_prompt() -> str:
    return "你是一个通用智能助手。当前问题不需要检索本地代码库，请直接、简洁、准确地回答用户。"


def _sanitize_history(history: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sanitized: list[dict[str, str]] = []
    for item in history[-8:]:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip()
        content = str(item.get("content") or "").strip()
        if role not in {"user", "assistant"} or not content:
            continue
        sanitized.append({"role": role, "content": content})
    return sanitized


def _build_user_prompt(*, message: str, context_bundle: dict[str, Any], attachments: list[AgentAttachment]) -> dict[str, Any]:
    context_json = json.dumps(context_bundle, ensure_ascii=False, indent=2)
    attachment_text = _format_attachment_prompt(attachments)
    decision_note = _format_grounded_decision_note(context_bundle)
    text_parts = ["用户问题：\n" + message.strip()]
    if decision_note:
        text_parts.append(decision_note)
    if context_bundle.get("options", {}).get("auto_retrieve"):
        text_parts.append(
            "本地代码库自动检索上下文（系统已按问题自动检索代码索引、元数据索引和表结构索引，并在必要时进行了多轮补检索）:\n"
            + context_json
        )
    elif context_bundle.get("options", {}).get("include_retrieval") or context_bundle.get("options", {}).get("include_evidence"):
        text_parts.append("本地代码库上下文（来自当前 uses-indexer 服务）:\n" + context_json)
    if attachment_text:
        text_parts.append(attachment_text)
    text_parts.append(
        "请基于这些上下文直接回答。若上下文不足，请说明系统已经检索了哪些索引、还缺哪类证据，"
        "但不要让用户手工再粘贴检索结果。"
    )
    text_content = "\n\n".join(text_parts)

    image_attachments = [a for a in attachments if a.data_url and a.media_kind == "image"]
    if image_attachments:
        content: list[dict[str, Any]] = [{"type": "text", "text": text_content}]
        for img in image_attachments:
            content.append({
                "type": "image_url",
                "image_url": {"url": img.data_url},
            })
        return {"role": "user", "content": content}
    return {"role": "user", "content": text_content}


def _format_grounded_decision_note(context_bundle: dict[str, Any]) -> str:
    draft = dict(context_bundle.get("answer_draft") or {})
    decision = dict(draft.get("decision") or {})
    if not draft or not decision:
        return ""
    lines = [
        "当前 grounded QA 决策摘要：",
        f"- query_type: {draft.get('query_type') or 'unknown'}",
        f"- review_required: {bool(draft.get('review_required'))}",
    ]
    if decision.get("state"):
        lines.append(f"- state: {decision['state']}")
    if decision.get("conflict_kind"):
        lines.append(f"- conflict_kind: {decision['conflict_kind']}")
    if decision.get("evidence_alignment"):
        lines.append(f"- evidence_alignment: {decision['evidence_alignment']}")
    primary_candidate = dict(draft.get("primary_candidate") or {})
    if primary_candidate.get("procedure_name"):
        lines.append(f"- primary_candidate: {primary_candidate['procedure_name']}")
    return "\n".join(lines) + "\n\n"


def _provider_from_override(provider_override: dict[str, Any], *, provider_name: str | None) -> AgentProviderConfig:
    if not isinstance(provider_override, dict):
        raise AgentConfigError("provider_override must be an object")
    base_url = str(provider_override.get("base_url") or "").strip()
    model = str(provider_override.get("model") or "").strip()
    if not base_url or not model:
        raise AgentConfigError("provider_override requires base_url and model")
    adapter = str(provider_override.get("adapter") or "openai-compatible").strip() or "openai-compatible"
    if adapter != "openai-compatible":
        raise AgentConfigError(f"Unsupported provider_override adapter: {adapter}")
    label = str(provider_override.get("label") or provider_name or "自定义模型").strip() or "自定义模型"
    api_key = str(provider_override.get("api_key") or "").strip() or None
    return AgentProviderConfig(
        name=str(provider_name or "custom-agent").strip() or "custom-agent",
        label=label,
        adapter=adapter,
        base_url=base_url,
        model=model,
        api_key=api_key,
        temperature=float(provider_override.get("temperature", 0.1)),
        max_tokens=int(provider_override.get("max_tokens", 1600)),
        timeout_seconds=float(provider_override.get("timeout_seconds", 90)),
        max_retries=int(provider_override.get("max_retries", 0)),
        retry_backoff_seconds=float(provider_override.get("retry_backoff_seconds", 1.0)),
        description="来自前端弹层配置的临时模型",
    )


def _coerce_attachments(raw_attachments: list[dict[str, Any]] | None) -> list[AgentAttachment]:
    attachments: list[AgentAttachment] = []
    for item in raw_attachments or []:
        if not isinstance(item, dict):
            continue
        name = str(item.get("name") or "").strip()
        media_kind = str(item.get("media_kind") or "file").strip()
        mime_type = str(item.get("mime_type") or "application/octet-stream").strip()
        if not name:
            continue
        attachments.append(
            AgentAttachment(
                name=name,
                media_kind=media_kind,
                mime_type=mime_type,
                size_bytes=int(item.get("size_bytes") or 0),
                text_content=(str(item["text_content"]) if item.get("text_content") else None),
                data_url=(str(item["data_url"]) if item.get("data_url") else None),
            )
        )
    return attachments[:8]


def _truncate_attachment_text(text: str | None) -> str | None:
    if not text:
        return None
    normalized = text.strip()
    if not normalized:
        return None
    return normalized[:500]


def _format_attachment_prompt(attachments: list[AgentAttachment]) -> str:
    if not attachments:
        return ""
    lines = ["附件信息："]
    for item in attachments:
        lines.append(f"- {item.name} ({item.media_kind}, {item.mime_type}, {item.size_bytes} bytes)")
        excerpt = _truncate_attachment_text(item.text_content)
        if excerpt:
            lines.append(f"  内容摘要：{excerpt}")
        elif item.data_url and item.media_kind == "image":
            lines.append("  附件包含图片数据，可结合文字问题一起理解。")
    return "\n".join(lines) + "\n\n"
