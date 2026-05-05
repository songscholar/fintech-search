"""Skill tools — expose SkillManager operations as agent-callable tools.

Registers a ToolSource with prefix "skill__" so the agent loop can
list, search, install, uninstall, and invoke skills via function calling.
Mirrors Claude Code's SkillTool architecture.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .skill_manager import SkillManager
from .tool_registry import ToolSource

SKILL_TOOL_DEFINITIONS = [
    {
        "name": "list_skills",
        "description": "List all available skills (local and installed remote). Skills provide specialized prompts and workflows.",
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
    },
    {
        "name": "search_skills",
        "description": "Search the remote skill registry for skills matching a query. Returns skill metadata.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "install_skill",
        "description": "Install a skill from the remote registry. Skills provide specialized prompts and workflows.",
        "parameters": {
            "type": "object",
            "properties": {
                "skill_id": {"type": "string", "description": "Skill ID to install"},
            },
            "required": ["skill_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "uninstall_skill",
        "description": "Uninstall a previously installed remote skill. Local skills cannot be uninstalled.",
        "parameters": {
            "type": "object",
            "properties": {
                "skill_id": {"type": "string", "description": "Skill ID to uninstall"},
            },
            "required": ["skill_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "invoke_skill",
        "description": "Invoke an installed skill. Returns the skill's prompt content expanded with arguments. The content is injected into the conversation as instructions for you to follow.",
        "parameters": {
            "type": "object",
            "properties": {
                "skill": {"type": "string", "description": "Skill ID to invoke"},
                "args": {"type": "string", "description": "Arguments to pass to the skill (replaces $ARGUMENTS placeholder)"},
            },
            "required": ["skill"],
            "additionalProperties": False,
        },
    },
]


def _substitute_arguments(content: str, args: str) -> str:
    """Replace $ARGUMENTS and $0, $1, ... placeholders in skill content."""
    if not args:
        return content
    # $ARGUMENTS -> full args string
    content = content.replace("$ARGUMENTS", args)
    # $0, $1, ... -> split args
    parts = args.split()
    for i, part in enumerate(parts):
        content = content.replace(f"${i}", part)
    return content


def _parse_frontmatter_body(content: str) -> str:
    """Strip YAML frontmatter, return body only."""
    fm_match = re.match(r"^---\s*\n([\s\S]*?)---\s*\n?", content)
    if fm_match:
        return content[fm_match.end():]
    return content


async def _execute_skill_tool(
    skill_manager: SkillManager,
    name: str,
    arguments: dict[str, Any],
) -> tuple[str, bool]:
    if name == "list_skills":
        skills = skill_manager.list_skills()
        if not skills:
            return "No skills available.", False
        lines = []
        for s in skills:
            desc = s.get("description", "")[:100]
            src = s.get("source", "local")
            lines.append(f"- {s['id']} ({src}): {desc}")
        return "\n".join(lines), False

    if name == "search_skills":
        query = arguments.get("query", "")
        if not query:
            return "Missing required parameter: query", True
        results = await skill_manager.search_remote(query)
        if not results:
            return "No skills found matching your query.", False
        lines = []
        for r in results:
            sid = r.get("id", r.get("name", "unknown"))
            desc = r.get("description", "")[:100]
            lines.append(f"- {sid}: {desc}")
        return "\n".join(lines), False

    if name == "install_skill":
        skill_id = arguments.get("skill_id", "")
        if not skill_id:
            return "Missing required parameter: skill_id", True
        result = await skill_manager.install_skill(skill_id)
        if result.get("ok"):
            return f"Skill '{skill_id}' installed successfully. Status: {result.get('status', 'installed')}", False
        return f"Failed to install skill '{skill_id}': {result.get('error', 'unknown error')}", True

    if name == "uninstall_skill":
        skill_id = arguments.get("skill_id", "")
        if not skill_id:
            return "Missing required parameter: skill_id", True
        result = skill_manager.uninstall_skill(skill_id)
        if result.get("ok"):
            return f"Skill '{skill_id}' uninstalled successfully.", False
        return f"Failed to uninstall skill '{skill_id}': {result.get('error', 'unknown error')}", True

    if name == "invoke_skill":
        skill_id = arguments.get("skill", "")
        args = arguments.get("args", "")
        if not skill_id:
            return "Missing required parameter: skill", True
        content = skill_manager.get_skill_content(skill_id)
        if content is None:
            return f"Skill not found: {skill_id}", True
        # Strip frontmatter, get body
        body = _parse_frontmatter_body(content)
        # Substitute arguments
        body = _substitute_arguments(body, args)
        # Replace ${SKILL_DIR}
        skill = skill_manager.get_skill(skill_id)
        if skill:
            body = body.replace("${SKILL_DIR}", skill.get("path", ""))
        return body, False

    return f"Unknown skill tool: {name}", True


def create_skill_tool_source(skill_manager: SkillManager) -> ToolSource:
    """Create a ToolSource for skill operations, to be registered in ToolRegistry."""

    async def _dispatch(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
        return await _execute_skill_tool(skill_manager, name, arguments)

    return ToolSource(
        name="skill",
        prefix="skill__",
        definitions=SKILL_TOOL_DEFINITIONS,
        execute=_dispatch,
        requires_confirmation={"install_skill", "uninstall_skill"},
    )
