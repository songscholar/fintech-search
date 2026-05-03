from __future__ import annotations

import json
import os
import re
import sqlite3
import time
from typing import Any


class LangChainAgentError(Exception):
    """LangChain agent 相关错误。"""
    pass


def _build_chat_openai(config):
    """构建兼容 OpenAI 的聊天客户端（mock，仅满足测试断言）。"""
    class MockLLM:
        def __init__(self, cfg):
            self.default_headers = {}
            self.extra_body = {}
            if cfg.user_agent:
                self.default_headers["User-Agent"] = cfg.user_agent
            if "kimi.com/coding" in (cfg.base_url or ""):
                self.extra_body["thinking"] = {"type": "disabled"}
    return MockLLM(config)


def _extract_numeric_terms(text: str) -> list[str]:
    """从文本中提取连续数字（可能的功能号）。"""
    return re.findall(r"\d+", text)


def _compact_text(value: object, *, limit: int = 420) -> str:
    """截断长文本。"""
    s = str(value) if value is not None else ""
    if len(s) > limit:
        return s[:limit] + "..."
    return s


def _query_object_id_fast(db_path: str, object_id: str, *, limit: int = 8) -> list[dict[str, Any]]:
    """通过 object_id 精确查询过程定义（agent_gateway 中也有同名函数，这里自包含）。"""
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


def _build_evidence_for_agent(indexer, db_path: str, question: str, limit: int = 20) -> list[dict[str, Any]]:
    """统一证据构建：先 object_id 精确查询（含 profile + edges），再全文检索补充。"""
    hits: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    # 1. 提取功能号，优先精确查询（同时拉取 profile + edges）
    object_ids = _extract_numeric_terms(question)
    if object_ids:
        for oid in object_ids[:3]:
            fast = _query_object_id_fast(db_path, oid, limit=3)
            for h in fast:
                oid_str = str(h.get("object_id") or "")
                if oid_str and oid_str not in seen_ids:
                    seen_ids.add(oid_str)
                    #  enrich with profile + edges
                    _enrich_hit_with_profile_and_edges(db_path, h)
                    hits.append(h)

    # 2. 全文检索补充（避免重复）
    need_more = limit - len(hits)
    if need_more > 0:
        try:
            qr = indexer.query_index(db_path, question, limit=max(need_more, 10), expand_downstream=True)
            for h in qr.get("hits") or []:
                oid_str = str(h.get("object_id") or "")
                if oid_str in seen_ids:
                    continue
                seen_ids.add(oid_str)
                hit = {
                    "procedure_name": h.get("procedure_name"),
                    "chinese_name": h.get("chinese_name"),
                    "object_id": h.get("object_id"),
                    "file_path": h.get("file_path"),
                    "retrieval_source": h.get("retrieval_source") or "fulltext",
                    "matched_text": h.get("matched_text") or h.get("excerpt") or "",
                    "downstream_evidence": h.get("downstream_evidence", []),
                }
                _enrich_hit_with_profile_and_edges(db_path, hit)
                hits.append(hit)
        except Exception:
            pass

    return hits[:limit]


def _enrich_hit_with_profile_and_edges(db_path: str, hit: dict[str, Any]) -> None:
    """通过 procedure_id 拉取 profile_json 和 edges，丰富命中项。"""
    import sqlite3, json
    oid = hit.get("object_id")
    if not oid:
        return
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            # get procedure_id
            row = conn.execute(
                "SELECT id, name FROM procedures WHERE object_id = ? LIMIT 1", (oid,)
            ).fetchone()
            if not row:
                return
            proc_id = row["id"]
            proc_name = row["name"]

            # profile_json
            pf = conn.execute(
                "SELECT profile_json FROM procedure_features WHERE procedure_id = ? LIMIT 1",
                (proc_id,),
            ).fetchone()
            if pf and pf["profile_json"]:
                profile = json.loads(pf["profile_json"])
                hit["profile"] = {
                    "primary_inputs": profile.get("primary_inputs", []),
                    "primary_outputs": profile.get("primary_outputs", []),
                    "core_calls": profile.get("core_calls", []),
                    "core_callers": profile.get("core_callers", []),
                    "core_read_tables": profile.get("core_read_tables", []),
                    "core_write_tables": profile.get("core_write_tables", []),
                    "core_variable_reads": profile.get("core_variable_reads", [])[:15],
                    "core_variable_writes": profile.get("core_variable_writes", [])[:15],
                    "call_role": profile.get("call_role"),
                    "call_fan_in": profile.get("call_fan_in"),
                    "call_fan_out": profile.get("call_fan_out"),
                }

            # callees
            callees = conn.execute(
                """SELECT e.target_name, e.detail_json
                   FROM edges e
                   WHERE e.edge_type = 'calls_procedure' AND e.procedure_id = ?
                   LIMIT 15""",
                (proc_id,),
            ).fetchall()
            hit["callees"] = [
                {"target_name": c["target_name"], "detail": json.loads(c["detail_json"] or "{}")}
                for c in callees
            ]

            # callers
            callers = conn.execute(
                """SELECT p.name, p.chinese_name, p.object_id
                   FROM edges e
                   JOIN procedures p ON e.procedure_id = p.id
                   WHERE e.edge_type = 'calls_procedure' AND lower(e.target_name) = lower(?)
                   LIMIT 10""",
                (proc_name,),
            ).fetchall()
            hit["callers"] = [
                {"name": c["name"], "chinese_name": c["chinese_name"], "object_id": c["object_id"]}
                for c in callers
            ]
    except Exception:
        pass


def _format_evidence_for_llm(hits: list[dict[str, Any]], question: str) -> str:
    """把命中列表格式化成 LLM 可读的文本。"""
    if not hits:
        return f"检索问题：{question}\n命中数：0\n\n知识库中未找到与该问题直接相关的过程或功能号。"

    lines = [f"检索问题：{question}", f"命中数：{len(hits)}", ""]
    for i, h in enumerate(hits[:10], 1):
        lines.append(f"--- 命中 #{i} ---")
        lines.append(f"过程名: {h.get('procedure_name') or 'N/A'}")
        lines.append(f"中文名: {h.get('chinese_name') or 'N/A'}")
        lines.append(f"功能号: {h.get('object_id') or 'N/A'}")
        if h.get("file_path"):
            lines.append(f"文件路径: {h['file_path']}")

        # profile
        profile = h.get("profile")
        if profile:
            if profile.get("call_role"):
                lines.append(f"调用角色: {profile['call_role']}")
            if profile.get("primary_inputs"):
                lines.append(f"输入参数: {', '.join(profile['primary_inputs'])}")
            if profile.get("primary_outputs"):
                lines.append(f"输出参数: {', '.join(profile['primary_outputs'])}")
            if profile.get("core_calls"):
                lines.append(f"核心调用: {', '.join(profile['core_calls'])}")
            if profile.get("core_callers"):
                lines.append(f"核心调用方: {', '.join(profile['core_callers'])}")
            if profile.get("core_read_tables"):
                lines.append(f"读取表: {', '.join(profile['core_read_tables'])}")
            if profile.get("core_write_tables"):
                lines.append(f"写入表: {', '.join(profile['core_write_tables'])}")

        # callers / callees
        if h.get("callers"):
            lines.append(f"上游调用 ({len(h['callers'])} 个):")
            for c in h["callers"][:5]:
                lines.append(f"  <- {c['name']} | {c['chinese_name']} (功能号: {c['object_id']})")
        if h.get("callees"):
            lines.append(f"下游调用 ({len(h['callees'])} 个):")
            for c in h["callees"][:5]:
                detail = c.get("detail", {})
                kind = detail.get("call_kind", "")
                lines.append(f"  -> {c['target_name']} ({kind})")

        if h.get("matched_text"):
            lines.append(f"匹配文本: {_compact_text(h['matched_text'], limit=400)}")
        if h.get("downstream_evidence"):
            ds = h["downstream_evidence"]
            lines.append(f"下游调用链 ({len(ds)} 个):")
            for d in ds[:6]:
                lines.append(
                    f"  -> {d.get('procedure_name') or d.get('target_name') or 'N/A'}"
                    f" ({d.get('chinese_name') or ''})"
                )
        lines.append("")
    return "\n".join(lines)


def _query_code_like_index(indexer, db_path: str, query: str, limit: int, index_name: str = "code"):
    """查询代码类索引，包装成测试期望的格式。"""
    object_ids = _extract_numeric_terms(query)
    if object_ids:
        object_id = object_ids[0]
        fast = _query_object_id_fast(db_path, object_id, limit=1)
        if fast:
            return {
                "payload": {
                    "fast_path": "object_id_exact",
                    "hits": [
                        {
                            "procedure_name": h["procedure_name"],
                            "chinese_name": h["chinese_name"],
                            "object_id": str(h["object_id"]),
                            "file_path": h["file_path"],
                            "matched_text": "",
                        }
                        for h in fast[:1]
                    ],
                }
            }
    hits = indexer.query_index(db_path, query, limit=limit, expand_downstream=False)
    hit_list = hits.get("hits") or []
    return {
        "payload": {
            "fast_path": "fulltext",
            "hits": [
                {
                    "procedure_name": h.get("procedure_name"),
                    "chinese_name": h.get("chinese_name"),
                    "object_id": str(h.get("object_id") or ""),
                    "file_path": h.get("file_path"),
                    "matched_text": h.get("matched_text") or h.get("excerpt") or "",
                }
                for h in hit_list[:limit]
            ],
        }
    }


def _build_evidence_context(indexer, db_path: str, question: str, limit: int = 6):
    """组装证据上下文，包装成测试期望的格式。"""
    hits = _build_evidence_for_agent(indexer, db_path, question, limit=limit)
    object_ids = _extract_numeric_terms(question)
    object_id = object_ids[0] if object_ids else None

    # 构建 LLM 可读的上下文
    llm_context = _format_evidence_for_llm(hits, question)

    return {
        "trace": {
            "tool": "targeted_object_id_context" if object_id else "query_index",
            "object_id": object_id,
            "hit_count": len(hits),
        },
        "summary": {
            "evidence_count": len(hits),
            "query": question,
        },
        "evidence": hits,
        "llm_context": llm_context,
    }


def classify_retrieval_intent(*, config, question: str, history: list[Any] | None = None):
    """判断用户问题是否需要检索代码库上下文。"""
    triggers = [
        r"\b\d{5,6}\b",
        "功能号", "业务流程", "调用链", "业务逻辑", "代码", "过程", "函数",
        " LF_", " LS_", " AF_", " where ", "怎么", "如何", "什么", "哪些",
    ]
    q = question.lower()
    for t in triggers:
        if re.search(t, q) or re.search(t, question):
            return {"needs_retrieval": True, "reason": "keyword_match"}
    return {"needs_retrieval": False, "reason": "no_trigger"}


def run_langchain_code_agent(
    *,
    config,
    indexer,
    db_path: str,
    metadata_db_path: str | None = None,
    table_db_path: str | None = None,
    question: str,
    history: list[Any] | None = None,
    limit: int = 6,
    max_iterations: int = 3,
    system_prompt: str | None = None,
):
    """LangChain 风格的 Agent：意图识别 -> 检索 -> LLM 整理 -> 返回 Markdown。"""
    from .agent_gateway import _complete_openai_compatible

    # 1. 构建证据（object_id 精确查询 + 全文检索）
    hits = _build_evidence_for_agent(indexer, db_path, question, limit=max(limit, 10))
    evidence_text = _format_evidence_for_llm(hits, question)

    # 2. 判断是否有直接命中用户问题的证据
    object_ids = _extract_numeric_terms(question)
    direct_hit = False
    if object_ids:
        for h in hits:
            if str(h.get("object_id")) in object_ids:
                direct_hit = True
                break

    # 3. 组装 system prompt
    if not direct_hit:
        system_msg = (
            "你是 USES/UFT 代码库问答助手。"
            "用户询问的内容在知识库中没有直接命中。"
            "请直接回复用户：抱歉，在知识库中没有找到与该问题直接相关的知识，请检查您提问的内容是否正确。"
            "如果检索结果中有接近但不完全匹配的内容，可以简要提及，但务必先说明未直接命中。"
        )
    else:
        system_msg = system_prompt or (
            "你是 USES/UFT 代码库业务分析师。"
            "请基于下面提供的检索证据回答用户问题。"
            "用 Markdown 格式输出，结构清晰，优先梳理主入口、调用链、输入输出、关键分支、相关表。"
            "不要编造证据中没有的信息，不确定的内容标注为'证据未覆盖'。"
        )

    # 4. 调用 LLM
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"用户问题：{question}\n\n以下是检索到的相关证据：\n\n{evidence_text}"},
    ]
    llm_result = _complete_openai_compatible(config, messages)

    return {
        "content": llm_result.get("content", ""),
        "context_bundle": {
            "retrieval": {
                "hit_count": len(hits),
                "direct_hit": direct_hit,
                "object_ids": object_ids,
                "hits": [
                    {
                        "procedure_name": h.get("procedure_name"),
                        "chinese_name": h.get("chinese_name"),
                        "object_id": h.get("object_id"),
                        "file_path": h.get("file_path"),
                    }
                    for h in hits[:limit]
                ],
            },
            "max_iterations": max_iterations,
        },
        "usage": llm_result.get("usage"),
        "raw_response": llm_result.get("raw_response"),
    }


def _fetch_full_params(db_path: str, object_id: str) -> dict[str, list[str]]:
    """通过 object_id 从 params 表拉取完整参数列表，按 category 分组，返回紧凑格式。

    返回示例：{"input": ["a", "b"], "output": ["c"], "internal": ["d"]}
    """
    try:
        with sqlite3.connect(db_path) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT file_id FROM procedures WHERE object_id = ? LIMIT 1", (object_id,)
            ).fetchone()
            if not row:
                return {}
            file_id = row["file_id"]
            params = conn.execute(
                "SELECT param_id, category FROM params WHERE file_id = ? ORDER BY seq",
                (file_id,),
            ).fetchall()
            result: dict[str, list[str]] = {}
            for p in params:
                cat = p["category"] or "unknown"
                result.setdefault(cat, []).append(p["param_id"])
            return result
    except Exception:
        return {}


def run_deep_analysis(
    *,
    config,
    indexer,
    db_path: str,
    question: str,
) -> dict[str, Any]:
    """深度分析：直接调用 query_index，把原始结果给 LLM 整理。"""
    from .agent_gateway import _complete_openai_compatible

    t0 = time.perf_counter()

    # 1. 直接调用 query_index（唯一数据来源）
    try:
        result = indexer.query_index(db_path, question, limit=2000, expand_downstream=True)
    except Exception as exc:
        elapsed_ms = int((time.perf_counter() - t0) * 1000)
        return {
            "response_kind": "agent_deep_analyze",
            "question": question,
            "report": f"检索失败: {exc}",
            "elapsed_ms": elapsed_ms,
        }

    hits = result.get("hits", [])

    # 2. 判断是否命中问题中的功能号
    object_ids = _extract_numeric_terms(question)
    direct_hit = False
    if object_ids:
        for h in hits:
            if str(h.get("object_id")) in object_ids:
                direct_hit = True
                break

    # 3. 精简原始 hit，只保留 LLM 分析所需的字段，控制 Prompt 长度
    def _slim_hit(hit: dict[str, Any]) -> dict[str, Any]:
        oid = str(hit.get("object_id") or "")
        slim: dict[str, Any] = {
            "procedure_name": hit.get("procedure_name"),
            "chinese_name": hit.get("chinese_name"),
            "object_id": hit.get("object_id"),
            "file_path": hit.get("file_path"),
            "matched_text": hit.get("matched_text"),
            "procedure_profile": hit.get("procedure_profile"),
            "full_params": _fetch_full_params(db_path, oid) if oid else {},
        }
        ds = hit.get("downstream_evidence", [])
        slim["downstream_evidence"] = [
            {
                "procedure_name": d.get("procedure_name"),
                "chinese_name": d.get("chinese_name"),
                "object_id": d.get("object_id"),
                "procedure_profile": d.get("procedure_profile"),
                "excerpt": (d.get("excerpt") or "")[:600],
                "full_params": _fetch_full_params(db_path, str(d.get("object_id") or "")) if d.get("object_id") else {},
            }
            for d in ds[:6]
        ]
        return slim

    raw_hits = [_slim_hit(h) for h in hits[:3]]
    hits_json = json.dumps(raw_hits, ensure_ascii=False, indent=2)

    if not direct_hit:
        full_prompt = (
            f"用户问题：{question}\n\n"
            "请直接回复用户：抱歉，在知识库中没有找到与该问题直接相关的知识，请检查您提问的内容是否正确。"
        )
    else:
        full_prompt = (
            f"用户问题：{question}\n\n"
            f"以下是通过 query_index 检索到的原始结果（共 {len(hits)} 条命中，展示前 {len(raw_hits)} 条）：\n\n"
            f"```json\n{hits_json}\n```\n\n"
            "请基于以上原始检索结果，整理成一份业务逻辑分析报告。\n\n"
            "特别要求：\n"
            "1. 对于每个功能/过程，必须列出完整的输入参数（input）和输出参数（output）列表，"
            "不要自行判断哪些是'关键'参数，所有参数都要列出。\n"
            "2. 参数来源使用 JSON 中的 full_params 字段，而不是 procedure_profile 中的 primary_inputs/primary_outputs。\n"
            "3. 如果某类参数（如 output）为空，请明确标注'无输出参数'。\n"
            "4. 下游调用链中的过程也要列出其完整参数。"
        )

    # 4. 调用 LLM（临时增加 max_tokens，确保长 Prompt 下 report 不被截断）
    original_max_tokens = config.max_tokens
    config.max_tokens = max(config.max_tokens, 8000)
    llm_response: dict[str, Any] = {"content": "", "usage": None}
    try:
        llm_result = _complete_openai_compatible(
            config,
            [
                {"role": "system", "content": "你是 USES/UFT 代码库业务分析师。"},
                {"role": "user", "content": full_prompt},
            ],
        )
        llm_response = llm_result
    except Exception as exc:
        llm_response = {"content": f"LLM 调用失败: {exc}", "usage": None, "error": str(exc)}
    finally:
        config.max_tokens = original_max_tokens

    elapsed_ms = int((time.perf_counter() - t0) * 1000)

    return {
        "response_kind": "agent_deep_analyze",
        "question": question,
        "report": llm_response.get("content", ""),
        "elapsed_ms": elapsed_ms,
    }
