"""MCP management tools — expose McpClientManager operations as agent-callable tools.

Registers a ToolSource with prefix "mcp_mgmt__" so the agent loop can
list, connect, disconnect, and reconnect MCP servers via function calling.
Mirrors Claude Code's MCP management capabilities.
"""

from __future__ import annotations

import asyncio
from typing import Any

from .mcp_client_manager import McpClientManager, McpServerConfig
from .tool_registry import ToolSource

MCP_TOOL_DEFINITIONS = [
    {
        "name": "list_mcp_servers",
        "description": "List all MCP servers (connected, disconnected, errored). Shows server name, transport, status, and tool count.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "name": "connect_mcp_server",
        "description": "Connect to a new MCP server at runtime. For stdio transport: provide command and args. For SSE transport: provide url. The server's tools will be automatically discovered and registered.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Server name identifier (used as tool prefix)"},
                "transport": {"type": "string", "enum": ["stdio", "sse"], "description": "Transport type"},
                "command": {"type": "string", "description": "Command to run for stdio transport (e.g. 'python3')"},
                "args": {"type": "array", "items": {"type": "string"}, "description": "Arguments for the stdio command"},
                "env": {"type": "object", "description": "Environment variables for stdio transport"},
                "url": {"type": "string", "description": "Server URL for SSE transport"},
                "headers": {"type": "object", "description": "HTTP headers for SSE transport"},
            },
            "required": ["name", "transport"],
            "additionalProperties": False,
        },
    },
    {
        "name": "disconnect_mcp_server",
        "description": "Disconnect a connected MCP server. Its tools will be unregistered from the agent.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Server name to disconnect"},
            },
            "required": ["name"],
            "additionalProperties": False,
        },
    },
    {
        "name": "reconnect_mcp_server",
        "description": "Reconnect a disconnected or errored MCP server.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Server name to reconnect"},
            },
            "required": ["name"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list_mcp_tools",
        "description": "List all tools provided by a specific MCP server.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "Server name"},
            },
            "required": ["name"],
            "additionalProperties": False,
        },
    },
]


async def _execute_mcp_tool(
    mcp_manager: McpClientManager,
    name: str,
    arguments: dict[str, Any],
) -> tuple[str, bool]:
    if name == "list_mcp_servers":
        servers = mcp_manager.list_servers()
        if not servers:
            return "No MCP servers configured.", False
        lines = []
        for s in servers:
            status = s.get("status", "unknown")
            transport = s.get("transport", "?")
            tool_count = s.get("tool_count", 0)
            error = s.get("error", "")
            line = f"- {s['name']} ({transport}, {status}, {tool_count} tools)"
            if error:
                line += f" [error: {error}]"
            lines.append(line)
        return "\n".join(lines), False

    if name == "connect_mcp_server":
        server_name = arguments.get("name", "")
        transport = arguments.get("transport", "")
        if not server_name or not transport:
            return "Missing required parameters: name and transport", True
        if transport not in ("stdio", "sse"):
            return f"Invalid transport: {transport}. Must be 'stdio' or 'sse'.", True
        config = McpServerConfig(
            name=server_name,
            transport=transport,
            command=arguments.get("command"),
            args=arguments.get("args"),
            env=arguments.get("env"),
            url=arguments.get("url"),
            headers=arguments.get("headers"),
            enabled=True,
            auto_restart=True,
        )
        await mcp_manager.connect_server(config)
        state = mcp_manager._servers.get(server_name)
        tool_count = state.tool_count if state else 0
        return f"Connected to MCP server '{server_name}' ({transport}). {tool_count} tools discovered.", False

    if name == "disconnect_mcp_server":
        server_name = arguments.get("name", "")
        if not server_name:
            return "Missing required parameter: name", True
        await mcp_manager.disconnect_server(server_name)
        return f"Disconnected MCP server '{server_name}'.", False

    if name == "reconnect_mcp_server":
        server_name = arguments.get("name", "")
        if not server_name:
            return "Missing required parameter: name", True
        await mcp_manager.reconnect_server(server_name)
        state = mcp_manager._servers.get(server_name)
        tool_count = state.tool_count if state else 0
        return f"Reconnected MCP server '{server_name}'. {tool_count} tools available.", False

    if name == "list_mcp_tools":
        server_name = arguments.get("name", "")
        if not server_name:
            return "Missing required parameter: name", True
        source = mcp_manager._registry.get_source(server_name)
        if source is None:
            return f"MCP server '{server_name}' not found or not connected.", True
        tools = source.definitions
        if not tools:
            return f"MCP server '{server_name}' has no tools.", False
        lines = []
        for d in tools:
            func = d.get("function", d)
            tname = func.get("name", "")
            desc = func.get("description", "")[:80]
            lines.append(f"- {tname}: {desc}")
        return "\n".join(lines), False

    return f"Unknown MCP tool: {name}", True


def create_mcp_tool_source(mcp_manager: McpClientManager) -> ToolSource:
    """Create a ToolSource for MCP management, to be registered in ToolRegistry."""

    async def _dispatch(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
        return await _execute_mcp_tool(mcp_manager, name, arguments)

    return ToolSource(
        name="mcp_mgmt",
        prefix="mcp_mgmt__",
        definitions=MCP_TOOL_DEFINITIONS,
        execute=_dispatch,
        requires_confirmation={"connect_mcp_server", "disconnect_mcp_server"},
    )
