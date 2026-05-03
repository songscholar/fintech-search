"""Agent loop runner — multi-turn tool execution with SSE event generation.

The agent loop drives a conversation with an LLM that can invoke tools
from the dynamic ToolRegistry (builtin tools, internal MCP, external MCP, etc).
Each iteration:
  1. Send messages (including tool definitions) to the LLM
  2. If the LLM requests tool calls, execute them via ToolRegistry
  3. Feed tool results back to the LLM
  4. Repeat until the LLM returns text-only or max iterations reached
"""

from __future__ import annotations

import asyncio
import json
import threading
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, AsyncGenerator, Generator
from urllib import error, request

from .agent_gateway import AgentProviderConfig
from .logging_system import log_business, log_error
from .tool_registry import ToolRegistry


@dataclass(slots=True)
class AgentLoopConfig:
    max_iterations: int = 10
    max_tool_calls_per_iteration: int = 5
    tool_timeout_seconds: float = 30.0


@dataclass(slots=True)
class ToolCallEvent:
    call_id: str
    tool_name: str
    arguments: dict[str, Any]
    event_type: str = "tool_use"


@dataclass(slots=True)
class ToolResultEvent:
    call_id: str
    tool_name: str
    result: str
    is_error: bool
    latency_ms: int
    event_type: str = "tool_result"


@dataclass(slots=True)
class TextEvent:
    content: str
    event_type: str = "text"


@dataclass(slots=True)
class ThinkingEvent:
    content: str
    event_type: str = "thinking"


@dataclass(slots=True)
class DoneEvent:
    total_iterations: int
    total_tool_calls: int
    event_type: str = "done"


@dataclass(slots=True)
class ErrorEvent:
    message: str
    event_type: str = "error"


@dataclass(slots=True)
class ConfirmationRequiredEvent:
    call_id: str
    tool_name: str
    arguments: dict[str, Any]
    event_type: str = "tool_confirmation_required"


AgentEvent = (
    ToolCallEvent
    | ToolResultEvent
    | TextEvent
    | ThinkingEvent
    | DoneEvent
    | ErrorEvent
    | ConfirmationRequiredEvent
)

_CONFIRMATION_TIMEOUT_SECONDS = 120.0


class ConfirmationManager:
    """Thread-safe confirmation gate for tool calls.

    The agent loop thread calls `request_confirmation()` which blocks
    until the HTTP handler thread calls `resolve_confirmation()` or
    the timeout expires. Auto-allow rules bypass the block.
    """

    def __init__(self) -> None:
        self._pending: dict[str, _PendingConfirmation] = {}
        self._auto_rules: dict[str, str] = {}  # tool_name -> "allow" | "deny"
        self._lock = threading.Lock()

    def set_auto_rules(self, rules: dict[str, str]) -> None:
        with self._lock:
            self._auto_rules = dict(rules)

    def request_confirmation(self, call_id: str, tool_name: str, arguments: dict[str, Any]) -> str:
        """Block until user confirms. Returns 'allow' or 'deny'."""
        with self._lock:
            rule = self._auto_rules.get(tool_name)
            if rule in ("allow", "deny"):
                return rule

        event = threading.Event()
        pending = _PendingConfirmation(event=event, decision=None)
        with self._lock:
            self._pending[call_id] = pending

        event.wait(timeout=_CONFIRMATION_TIMEOUT_SECONDS)

        with self._lock:
            self._pending.pop(call_id, None)
            decision = pending.decision

        return decision or "deny"

    def resolve_confirmation(self, call_id: str, decision: str) -> bool:
        """Called by the POST /agent/tool-confirm endpoint. Returns True if found."""
        if decision == "allow_always":
            decision = "allow"

        with self._lock:
            pending = self._pending.get(call_id)
            if pending is None:
                return False
            pending.decision = decision if decision in ("allow", "deny") else "deny"
            pending.event.set()

        return True


@dataclass(slots=True)
class _PendingConfirmation:
    event: threading.Event
    decision: str | None


_SYSTEM_PROMPT_CODEBASE = (
    "你是 USES Indexer 智能体，具备代码库检索和通用工具能力。"
    "你可以调用以下类别的工具：\n"
    "- 业务分析（analyze__ 前缀）：业务知识深度分析，包括功能号、代码流程、表结构、调用链等。"
    "当用户询问业务相关问题时，必须优先使用 analyze__business_query 工具，不要使用其他工具替代。\n"
    "- 代码库检索（uses__ 前缀）：检索代码库、组装证据、查询数据库摘要、元数据、调试包等\n"
    "- 文件操作（builtin__ 前缀）：读取本地文件、列出目录、搜索文件内容\n"
    "- 网络检索（builtin__ 前缀）：搜索互联网、获取网页内容\n"
    "- 命令执行（builtin__ 前缀）：执行 shell 命令\n"
    "- 外部服务（其他前缀）：已连接的 MCP 服务器提供的工具\n"
    "请根据用户问题，自主决定是否需要调用工具以及调用哪些工具。"
    "如果问题涉及功能号、代码逻辑、业务流程、表结构、元数据、调用链，必须使用 analyze__business_query。"
    "如果需要查最新信息、技术文档、网络资源，使用网络检索工具。"
    "如果需要查看本地文件或执行命令，使用对应的内置工具。"
    "回答时请明确引用过程名、文件路径、表名等线索。"
)

_SYSTEM_PROMPT_GENERAL = (
    "你是一个通用智能助手，具备联网检索、文件操作和命令执行能力。"
    "你可以调用内置工具来搜索互联网、获取网页内容、读取本地文件、列出目录、搜索文件、执行命令等。"
    "当用户的问题需要最新信息或外部资源时，请主动使用网络检索工具。"
    "请直接、简洁、准确地回答问题。"
)


class AgentLoopRunner:
    def __init__(
        self,
        *,
        gateway_config: AgentProviderConfig,
        tool_registry: ToolRegistry,
        config: AgentLoopConfig | None = None,
        confirmation_manager: ConfirmationManager | None = None,
    ) -> None:
        self.config = config or AgentLoopConfig()
        self.gateway_config = gateway_config
        self.tool_registry = tool_registry
        self.confirmation_manager = confirmation_manager
        self._tools_requiring_confirmation = self._collect_confirmation_tools()

    def _collect_confirmation_tools(self) -> set[str]:
        """Collect full tool names that require confirmation from all sources."""
        names: set[str] = set()
        for source in self.tool_registry._sources.values():
            for d in source.definitions:
                raw_name = d.get("function", d).get("name", "")
                if raw_name in source.requires_confirmation:
                    full_name = f"{source.prefix}{raw_name}"
                    names.add(full_name)
        return names

    def _get_non_codebase_definitions(self) -> list[dict[str, Any]]:
        """Get tool definitions excluding codebase-specific tools (uses__ and analyze__ prefix)."""
        all_defs = self.tool_registry.get_all_definitions()
        return [d for d in all_defs if not (
            d.get("function", {}).get("name", "").startswith("uses__")
            or d.get("function", {}).get("name", "").startswith("analyze__")
        )]

    def run(
        self,
        user_message: str,
        history: list[dict[str, str]] | None = None,
        context_mode: str = "codebase",
        system_prompt_override: str | None = None,
    ) -> Generator[dict[str, Any], None, None]:
        """Yield SSE event dicts until done."""
        use_codebase_tools = context_mode == "codebase"
        system_prompt = system_prompt_override or (
            _SYSTEM_PROMPT_CODEBASE if use_codebase_tools else _SYSTEM_PROMPT_GENERAL
        )

        messages: list[dict[str, Any]] = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(_sanitize_history(history))
        messages.append({"role": "user", "content": user_message})

        # Codebase mode: all tools; General mode: builtin + external MCP only
        if use_codebase_tools:
            tool_definitions = self.tool_registry.get_all_definitions()
        else:
            tool_definitions = self._get_non_codebase_definitions()
        openai_tools = tool_definitions if tool_definitions else None

        total_tool_calls = 0
        supports_function_calling = True

        for iteration in range(1, self.config.max_iterations + 1):
            try:
                if supports_function_calling and openai_tools:
                    llm_response = _call_llm_with_tools(
                        self.gateway_config, messages, openai_tools
                    )
                else:
                    llm_response = _call_llm_plain(self.gateway_config, messages)
            except Exception as exc:
                log_error(
                    event="agent_loop_llm_call_failed",
                    message=str(exc),
                    exc=exc,
                    context={"iteration": iteration, "provider": self.gateway_config.name},
                )
                yield _event_to_dict(ErrorEvent(message=f"LLM 调用失败: {exc}"))
                return

            # Check if LLM wants to call tools
            tool_calls = _extract_tool_calls(llm_response)
            text_content = _extract_text_content(llm_response)

            if text_content and not tool_calls:
                yield _event_to_dict(TextEvent(content=text_content))
                yield _event_to_dict(DoneEvent(
                    total_iterations=iteration,
                    total_tool_calls=total_tool_calls,
                ))
                return

            # Emit thinking/text if present alongside tool calls
            if text_content:
                yield _event_to_dict(ThinkingEvent(content=text_content))

            # Add assistant message with tool calls to conversation
            assistant_msg = _build_assistant_message(llm_response, tool_calls)
            messages.append(assistant_msg)

            # Execute each tool call
            for tc in tool_calls[:self.config.max_tool_calls_per_iteration]:
                call_id = tc["id"] or f"call_{uuid.uuid4().hex[:8]}"
                tool_name = tc["name"]
                arguments = tc["arguments"]

                yield _event_to_dict(ToolCallEvent(
                    call_id=call_id,
                    tool_name=tool_name,
                    arguments=arguments,
                ))

                # Check if this tool requires confirmation
                needs_confirm = (
                    tool_name in self._tools_requiring_confirmation
                    and self.confirmation_manager is not None
                )
                if needs_confirm:
                    yield _event_to_dict(ConfirmationRequiredEvent(
                        call_id=call_id,
                        tool_name=tool_name,
                        arguments=arguments,
                    ))
                    decision = self.confirmation_manager.request_confirmation(
                        call_id, tool_name, arguments,
                    )
                    if decision == "deny":
                        yield _event_to_dict(ToolResultEvent(
                            call_id=call_id,
                            tool_name=tool_name,
                            result="用户拒绝了工具调用",
                            is_error=True,
                            latency_ms=0,
                        ))
                        messages.append({
                            "role": "tool",
                            "tool_call_id": call_id,
                            "content": "用户拒绝了工具调用",
                        })
                        continue

                started_at = time.time()
                try:
                    result_text, is_error = self._execute_tool(tool_name, arguments)
                except Exception as exc:
                    result_text = f"工具执行异常: {exc}"
                    is_error = True
                latency_ms = int((time.time() - started_at) * 1000)

                yield _event_to_dict(ToolResultEvent(
                    call_id=call_id,
                    tool_name=tool_name,
                    result=result_text,
                    is_error=is_error,
                    latency_ms=latency_ms,
                ))

                # Add tool result to conversation
                messages.append({
                    "role": "tool",
                    "tool_call_id": call_id,
                    "content": result_text,
                })
                total_tool_calls += 1

            # Short-circuit: if analyze__business_query was called, its report is already
            # the final answer. Skip the second LLM round to avoid context-window
            # truncation and re-summarization.
            for tc in tool_calls[:self.config.max_tool_calls_per_iteration]:
                if tc["name"] == "analyze__business_query":
                    for msg in messages:
                        if msg.get("role") == "tool" and msg.get("tool_call_id") == tc["id"]:
                            content = msg.get("content", "")
                            if content and content.startswith("【以下报告"):
                                yield _event_to_dict(TextEvent(content=content))
                                yield _event_to_dict(DoneEvent(
                                    total_iterations=iteration,
                                    total_tool_calls=total_tool_calls,
                                ))
                                return
                            break
                    break

        # Max iterations reached — ask LLM for a final text answer
        try:
            final_response = _call_llm_plain(self.gateway_config, messages)
            final_text = _extract_text_content(final_response)
            if final_text:
                yield _event_to_dict(TextEvent(content=final_text))
        except Exception as exc:
            log_error(
                event="agent_loop_final_call_failed",
                message=str(exc),
                exc=exc,
                context={"provider": self.gateway_config.name},
            )

        yield _event_to_dict(DoneEvent(
            total_iterations=self.config.max_iterations,
            total_tool_calls=total_tool_calls,
        ))

    def _execute_tool(self, tool_name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
        """Execute a tool via ToolRegistry. Returns (result_text, is_error)."""
        coro = self.tool_registry.execute_tool(tool_name, arguments)
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop is not None and loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
                future = pool.submit(asyncio.run, coro)
                return future.result(timeout=self.config.tool_timeout_seconds)

        return asyncio.run(coro)

    async def _execute_tool_async(self, tool_name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
        """Async version of _execute_tool for use in async contexts."""
        return await self.tool_registry.execute_tool(tool_name, arguments)

    async def run_async(
        self,
        user_message: str,
        history: list[dict[str, str]] | None = None,
        context_mode: str = "codebase",
        system_prompt_override: str | None = None,
    ) -> AsyncGenerator[dict[str, Any], None]:
        """Async variant of run() for use in async contexts (e.g. MCP client)."""
        use_codebase_tools = context_mode == "codebase"
        system_prompt = system_prompt_override or (
            _SYSTEM_PROMPT_CODEBASE if use_codebase_tools else _SYSTEM_PROMPT_GENERAL
        )

        messages: list[dict[str, Any]] = [{"role": "system", "content": system_prompt}]
        if history:
            messages.extend(_sanitize_history(history))
        messages.append({"role": "user", "content": user_message})

        if use_codebase_tools:
            tool_definitions = self.tool_registry.get_all_definitions()
        else:
            tool_definitions = self._get_non_codebase_definitions()
        openai_tools = tool_definitions if tool_definitions else None

        total_tool_calls = 0
        supports_function_calling = True

        for iteration in range(1, self.config.max_iterations + 1):
            try:
                if supports_function_calling and openai_tools:
                    llm_response = _call_llm_with_tools(
                        self.gateway_config, messages, openai_tools
                    )
                else:
                    llm_response = _call_llm_plain(self.gateway_config, messages)
            except Exception as exc:
                log_error(
                    event="agent_loop_llm_call_failed",
                    message=str(exc),
                    exc=exc,
                    context={"iteration": iteration, "provider": self.gateway_config.name},
                )
                yield _event_to_dict(ErrorEvent(message=f"LLM 调用失败: {exc}"))
                return

            tool_calls = _extract_tool_calls(llm_response)
            text_content = _extract_text_content(llm_response)

            if text_content and not tool_calls:
                yield _event_to_dict(TextEvent(content=text_content))
                yield _event_to_dict(DoneEvent(
                    total_iterations=iteration,
                    total_tool_calls=total_tool_calls,
                ))
                return

            if text_content:
                yield _event_to_dict(ThinkingEvent(content=text_content))

            assistant_msg = _build_assistant_message(llm_response, tool_calls)
            messages.append(assistant_msg)

            for tc in tool_calls[:self.config.max_tool_calls_per_iteration]:
                call_id = tc["id"] or f"call_{uuid.uuid4().hex[:8]}"
                tool_name = tc["name"]
                arguments = tc["arguments"]

                yield _event_to_dict(ToolCallEvent(
                    call_id=call_id,
                    tool_name=tool_name,
                    arguments=arguments,
                ))

                needs_confirm = (
                    tool_name in self._tools_requiring_confirmation
                    and self.confirmation_manager is not None
                )
                if needs_confirm:
                    yield _event_to_dict(ConfirmationRequiredEvent(
                        call_id=call_id,
                        tool_name=tool_name,
                        arguments=arguments,
                    ))
                    decision = self.confirmation_manager.request_confirmation(
                        call_id, tool_name, arguments,
                    )
                    if decision == "deny":
                        yield _event_to_dict(ToolResultEvent(
                            call_id=call_id,
                            tool_name=tool_name,
                            result="用户拒绝了工具调用",
                            is_error=True,
                            latency_ms=0,
                        ))
                        messages.append({
                            "role": "tool",
                            "tool_call_id": call_id,
                            "content": "用户拒绝了工具调用",
                        })
                        continue

                started_at = time.time()
                try:
                    result_text, is_error = await self._execute_tool_async(tool_name, arguments)
                except Exception as exc:
                    result_text = f"工具执行异常: {exc}"
                    is_error = True
                latency_ms = int((time.time() - started_at) * 1000)

                yield _event_to_dict(ToolResultEvent(
                    call_id=call_id,
                    tool_name=tool_name,
                    result=result_text,
                    is_error=is_error,
                    latency_ms=latency_ms,
                ))

                messages.append({
                    "role": "tool",
                    "tool_call_id": call_id,
                    "content": result_text,
                })
                total_tool_calls += 1

        try:
            final_response = _call_llm_plain(self.gateway_config, messages)
            final_text = _extract_text_content(final_response)
            if final_text:
                yield _event_to_dict(TextEvent(content=final_text))
        except Exception as exc:
            log_error(
                event="agent_loop_final_call_failed",
                message=str(exc),
                exc=exc,
                context={"provider": self.gateway_config.name},
            )

        yield _event_to_dict(DoneEvent(
            total_iterations=self.config.max_iterations,
            total_tool_calls=total_tool_calls,
        ))


def _call_llm_with_tools(
    config: AgentProviderConfig,
    messages: list[dict[str, Any]],
    tools: list[dict[str, Any]],
) -> dict[str, Any]:
    """Call LLM with OpenAI function calling tools parameter."""
    payload: dict[str, Any] = {
        "model": config.model,
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
        "messages": messages,
        "tools": tools,
    }
    return _perform_llm_request(config, payload)


def _call_llm_plain(
    config: AgentProviderConfig,
    messages: list[dict[str, Any]],
) -> dict[str, Any]:
    """Call LLM without tools (text-only)."""
    payload: dict[str, Any] = {
        "model": config.model,
        "temperature": config.temperature,
        "max_tokens": config.max_tokens,
        "messages": messages,
    }
    return _perform_llm_request(config, payload)


def _perform_llm_request(
    config: AgentProviderConfig,
    payload: dict[str, Any],
) -> dict[str, Any]:
    """Execute an HTTP request to the LLM and return parsed JSON response."""
    headers = {"Content-Type": "application/json"}
    if config.api_key:
        headers["Authorization"] = f"Bearer {config.api_key}"
    if config.user_agent:
        headers["User-Agent"] = config.user_agent

    http_request = request.Request(
        config.base_url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )

    attempts = config.max_retries + 1
    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with request.urlopen(http_request, timeout=config.timeout_seconds) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw)
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            last_error = RuntimeError(f"LLM request failed with status {exc.code}: {detail}")
        except error.URLError as exc:
            last_error = RuntimeError(f"LLM request failed: {exc.reason}")
        except TimeoutError as exc:
            last_error = RuntimeError(f"LLM request timed out: {exc}")
        if attempt < attempts:
            time.sleep(config.retry_backoff_seconds * attempt)

    if last_error is not None:
        raise last_error
    raise RuntimeError("LLM request failed for an unknown reason")


def _extract_tool_calls(response: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract tool calls from OpenAI-format LLM response."""
    choices = response.get("choices", [])
    if not choices:
        return []
    message = choices[0].get("message", {})
    raw_calls = message.get("tool_calls", [])
    if not isinstance(raw_calls, list):
        return []
    calls = []
    for tc in raw_calls:
        if not isinstance(tc, dict):
            continue
        func = tc.get("function", {})
        name = func.get("name", "")
        if not name:
            continue
        args_str = func.get("arguments", "{}")
        try:
            arguments = json.loads(args_str) if isinstance(args_str, str) else args_str
        except json.JSONDecodeError:
            arguments = {"_raw_args": args_str}
        calls.append({
            "id": tc.get("id", ""),
            "name": name,
            "arguments": arguments,
        })
    return calls


def _extract_text_content(response: dict[str, Any]) -> str:
    """Extract text content from OpenAI-format LLM response."""
    choices = response.get("choices", [])
    if not choices:
        return ""
    message = choices[0].get("message", {})
    content = message.get("content")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text = item.get("text", "")
                if text:
                    parts.append(text.strip())
        return "\n".join(parts).strip()
    return ""


def _build_assistant_message(
    response: dict[str, Any],
    tool_calls: list[dict[str, Any]],
) -> dict[str, Any]:
    """Build the assistant message to append to conversation history."""
    choices = response.get("choices", [])
    raw_message = choices[0].get("message", {}) if choices else {}
    msg: dict[str, Any] = {"role": "assistant", "content": raw_message.get("content") or ""}
    # Preserve reasoning_content for models with thinking mode (e.g. DeepSeek)
    reasoning = raw_message.get("reasoning_content")
    if reasoning:
        msg["reasoning_content"] = reasoning
    if tool_calls:
        msg["tool_calls"] = [
            {
                "id": tc["id"],
                "type": "function",
                "function": {
                    "name": tc["name"],
                    "arguments": json.dumps(tc["arguments"], ensure_ascii=False),
                },
            }
            for tc in tool_calls
        ]
    return msg


def _event_to_dict(event: AgentEvent) -> dict[str, Any]:
    """Convert an AgentEvent to an SSE-friendly dict."""
    if isinstance(event, ToolCallEvent):
        return {
            "type": "tool_use",
            "call_id": event.call_id,
            "tool_name": event.tool_name,
            "arguments": event.arguments,
        }
    if isinstance(event, ToolResultEvent):
        return {
            "type": "tool_result",
            "call_id": event.call_id,
            "tool_name": event.tool_name,
            "result": event.result,
            "is_error": event.is_error,
            "latency_ms": event.latency_ms,
        }
    if isinstance(event, TextEvent):
        return {"type": "text", "content": event.content}
    if isinstance(event, ThinkingEvent):
        return {"type": "thinking", "content": event.content}
    if isinstance(event, DoneEvent):
        return {
            "type": "done",
            "total_iterations": event.total_iterations,
            "total_tool_calls": event.total_tool_calls,
        }
    if isinstance(event, ErrorEvent):
        return {"type": "error", "message": event.message}
    if isinstance(event, ConfirmationRequiredEvent):
        return {
            "type": "tool_confirmation_required",
            "call_id": event.call_id,
            "tool_name": event.tool_name,
            "arguments": event.arguments,
        }
    return {"type": "unknown"}


def _sanitize_history(history: list[dict[str, str]]) -> list[dict[str, Any]]:
    """Keep only user/assistant messages, truncate to last 8."""
    sanitized: list[dict[str, Any]] = []
    for item in history[-8:]:
        if not isinstance(item, dict):
            continue
        role = str(item.get("role") or "").strip()
        content = str(item.get("content") or "").strip()
        if role not in {"user", "assistant"} or not content:
            continue
        sanitized.append({"role": role, "content": content})
    return sanitized
