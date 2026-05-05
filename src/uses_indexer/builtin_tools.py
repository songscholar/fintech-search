"""Built-in tools: file operations, web search/fetch, command execution.

These tools provide the agent with basic capabilities similar to Claude Code:
- Read/write local files
- List directories and search files
- Search the web and fetch URLs
- Execute shell commands (with safety controls)
"""

from __future__ import annotations

import asyncio
import fnmatch
import json
import os
import re
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any
from urllib import request, error, parse as urlparse

from .tool_registry import ToolSource

_PROJECT_ROOT = Path("/Users/songzuoqiang/Documents/agent/condex/codes")
_HOME = Path.home()

_ALLOWED_READ_PREFIXES = [str(_PROJECT_ROOT), str(_HOME)]
_ALLOWED_WRITE_PREFIXES = [str(_PROJECT_ROOT), str(_HOME)]

_SAFE_COMMANDS = {
    "ls", "cat", "head", "tail", "grep", "find", "wc", "sort", "uniq",
    "git", "diff", "echo", "pwd", "whoami", "which", "type",
    "file", "stat", "du", "df", "env", "printenv", "date",
    "python3", "python", "pip", "pip3",
    "node", "npm", "npx",
    "curl", "wget",
}

_DDG_LITE_URL = "https://lite.duckduckgo.com/lite/"
_SEARXNG_URL = os.environ.get("USES_INDEXER_SEARXNG_URL", "")


def _validate_path(path: str, *, write: bool = False) -> Path:
    """Validate that a path is within allowed boundaries."""
    resolved = Path(path).expanduser().resolve()
    prefixes = _ALLOWED_WRITE_PREFIXES if write else _ALLOWED_READ_PREFIXES
    allowed_str = os.environ.get("USES_INDEXER_ALLOWED_PATHS", "")
    if allowed_str:
        prefixes = allowed_str.split(":")
    if not any(str(resolved).startswith(p) for p in prefixes):
        raise PermissionError(f"Path '{path}' is outside allowed boundaries")
    return resolved


def _truncate(text: str, limit: int = 8000) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + f"\n... [truncated, {len(text)} total chars]"


# ========================================================================
# File Tools
# ========================================================================

FILE_TOOL_DEFINITIONS = [
    {
        "name": "read_file",
        "description": "Read the contents of a local file. Returns text content with line numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to read"},
                "offset": {"type": "integer", "description": "Starting line number (1-based)", "minimum": 1},
                "limit": {"type": "integer", "description": "Maximum number of lines to return", "minimum": 1, "maximum": 500},
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "write_file",
        "description": "Write content to a local file. Creates parent directories if needed. Requires confirmation.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to write"},
                "content": {"type": "string", "description": "Content to write"},
            },
            "required": ["path", "content"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list_directory",
        "description": "List files and subdirectories in a directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Directory path to list"},
                "pattern": {"type": "string", "description": "Glob pattern to filter filenames (e.g. '*.py')"},
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "search_files",
        "description": "Search for files by name pattern and optionally by content.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "Root directory to search"},
                "pattern": {"type": "string", "description": "Glob pattern for filenames (e.g. '*.py')"},
                "content_query": {"type": "string", "description": "Text or regex to search within file contents"},
                "max_results": {"type": "integer", "description": "Maximum number of results", "minimum": 1, "maximum": 50},
            },
            "required": ["path", "pattern"],
            "additionalProperties": False,
        },
    },
    {
        "name": "edit_file",
        "description": "Edit a file by replacing exact text. The old_text must match exactly. Use for surgical edits without rewriting the whole file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File path to edit"},
                "old_text": {"type": "string", "description": "Exact text to find and replace (must match uniquely)"},
                "new_text": {"type": "string", "description": "Replacement text"},
            },
            "required": ["path", "old_text", "new_text"],
            "additionalProperties": False,
        },
    },
    {
        "name": "delete_file",
        "description": "Delete a file or empty directory. Requires confirmation.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string", "description": "File or directory path to delete"},
                "recursive": {"type": "boolean", "description": "If true, delete directory and all contents (default false)"},
            },
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "move_file",
        "description": "Move or rename a file or directory. Requires confirmation.",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {"type": "string", "description": "Source path"},
                "destination": {"type": "string", "description": "Destination path"},
            },
            "required": ["source", "destination"],
            "additionalProperties": False,
        },
    },
    {
        "name": "copy_file",
        "description": "Copy a file or directory. Creates parent directories if needed.",
        "parameters": {
            "type": "object",
            "properties": {
                "source": {"type": "string", "description": "Source path"},
                "destination": {"type": "string", "description": "Destination path"},
            },
            "required": ["source", "destination"],
            "additionalProperties": False,
        },
    },
]


async def _execute_file_tool(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _execute_file_tool_sync, name, arguments)


def _execute_file_tool_sync(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    try:
        if name == "read_file":
            return _read_file(arguments)
        if name == "write_file":
            return _write_file(arguments)
        if name == "list_directory":
            return _list_directory(arguments)
        if name == "search_files":
            return _search_files(arguments)
        if name == "edit_file":
            return _edit_file(arguments)
        if name == "delete_file":
            return _delete_file(arguments)
        if name == "move_file":
            return _move_file(arguments)
        if name == "copy_file":
            return _copy_file(arguments)
    except PermissionError as exc:
        return str(exc), True
    except FileNotFoundError as exc:
        return f"File not found: {exc}", True
    except Exception as exc:
        return f"File tool error: {exc}", True
    return f"Unknown file tool: {name}", True


def _read_file(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"])
    if not path.is_file():
        return f"Not a file: {path}", True
    offset = int(args.get("offset", 1))
    limit = int(args.get("limit", 200))
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        return f"Cannot read file: {exc}", True
    lines = text.splitlines()
    selected = lines[offset - 1 : offset - 1 + limit]
    numbered = [f"{i + offset:6d} | {line}" for i, line in enumerate(selected)]
    result = "\n".join(numbered)
    if len(lines) > offset - 1 + limit:
        result += f"\n... [{len(lines) - offset + 1 - limit} more lines]"
    return _truncate(result), False


def _write_file(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"], write=True)
    content = args.get("content", "")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"Wrote {len(content)} chars to {path}", False


def _list_directory(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"])
    if not path.is_dir():
        return f"Not a directory: {path}", True
    pattern = args.get("pattern", "*")
    entries = sorted(path.iterdir())
    matched = [e for e in entries if fnmatch.fnmatch(e.name, pattern)]
    if len(matched) > 200:
        matched = matched[:200]
    lines = []
    for entry in matched:
        kind = "DIR " if entry.is_dir() else "FILE"
        size = ""
        if entry.is_file():
            try:
                size = f" ({entry.stat().st_size:,} bytes)"
            except OSError:
                pass
        lines.append(f"{kind}  {entry.name}{size}")
    result = "\n".join(lines)
    return _truncate(result) if result else "Empty directory", False


def _search_files(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"])
    pattern = args.get("pattern", "*")
    content_query = args.get("content_query", "")
    max_results = int(args.get("max_results", 20))
    matches = []
    for root, _dirs, files in os.walk(path):
        for fname in files:
            if fnmatch.fnmatch(fname, pattern):
                fpath = Path(root) / fname
                if content_query:
                    try:
                        text = fpath.read_text(encoding="utf-8", errors="ignore")
                        if content_query.lower() in text.lower() or re.search(content_query, text, re.IGNORECASE):
                            matches.append(str(fpath))
                    except Exception:
                        continue
                else:
                    matches.append(str(fpath))
                if len(matches) >= max_results:
                    break
        if len(matches) >= max_results:
            break
    result = "\n".join(matches)
    return _truncate(result) if result else "No matches found", False


def _edit_file(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"], write=True)
    if not path.is_file():
        return f"Not a file: {path}", True
    old_text = args["old_text"]
    new_text = args["new_text"]
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:
        return f"Cannot read file: {exc}", True
    count = content.count(old_text)
    if count == 0:
        return "old_text not found in file", True
    if count > 1:
        return f"old_text found {count} times — must be unique for surgical edit", True
    content = content.replace(old_text, new_text, 1)
    path.write_text(content, encoding="utf-8")
    return f"Edited {path}: replaced {len(old_text)} chars with {len(new_text)} chars", False


def _delete_file(args: dict[str, Any]) -> tuple[str, bool]:
    path = _validate_path(args["path"], write=True)
    recursive = args.get("recursive", False)
    if not path.exists():
        return f"Path does not exist: {path}", True
    if path.is_file():
        path.unlink()
        return f"Deleted file: {path}", False
    if path.is_dir():
        if recursive:
            shutil.rmtree(path)
            return f"Deleted directory recursively: {path}", False
        try:
            path.rmdir()
            return f"Deleted empty directory: {path}", False
        except OSError:
            return f"Directory not empty. Use recursive=true to delete with contents: {path}", True
    return f"Unknown path type: {path}", True


def _move_file(args: dict[str, Any]) -> tuple[str, bool]:
    src = _validate_path(args["source"], write=True)
    dst = _validate_path(args["destination"], write=True)
    if not src.exists():
        return f"Source does not exist: {src}", True
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    return f"Moved {src} -> {dst}", False


def _copy_file(args: dict[str, Any]) -> tuple[str, bool]:
    src = _validate_path(args["source"])
    dst = _validate_path(args["destination"], write=True)
    if not src.exists():
        return f"Source does not exist: {src}", True
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        shutil.copy2(str(src), str(dst))
        return f"Copied file {src} -> {dst}", False
    if src.is_dir():
        shutil.copytree(str(src), str(dst))
        return f"Copied directory {src} -> {dst}", False
    return f"Unknown source type: {src}", True


# ========================================================================
# Web Tools
# ========================================================================

WEB_TOOL_DEFINITIONS = [
    {
        "name": "web_search",
        "description": "Search the web using DuckDuckGo or a configured SearXNG instance. Returns search results with titles, URLs, and snippets.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query"},
                "max_results": {"type": "integer", "description": "Maximum number of results", "minimum": 1, "maximum": 20},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
    {
        "name": "web_fetch",
        "description": "Fetch a URL and return its content as text. HTML pages are converted to a readable text summary. Requires confirmation for non-HTTPS URLs.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "URL to fetch"},
                "max_chars": {"type": "integer", "description": "Maximum characters to return", "minimum": 500, "maximum": 50000},
            },
            "required": ["url"],
            "additionalProperties": False,
        },
    },
]


async def _execute_web_tool(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _execute_web_tool_sync, name, arguments)


def _execute_web_tool_sync(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    try:
        if name == "web_search":
            return _web_search(arguments)
        if name == "web_fetch":
            return _web_fetch(arguments)
    except Exception as exc:
        return f"Web tool error: {exc}", True
    return f"Unknown web tool: {name}", True


def _web_search(args: dict[str, Any]) -> tuple[str, bool]:
    query = args["query"]
    max_results = int(args.get("max_results", 8))
    if _SEARXNG_URL:
        return _search_searxng(query, max_results)
    return _search_ddg_lite(query, max_results)


def _search_searxng(query: str, max_results: int) -> tuple[str, bool]:
    url = f"{_SEARXNG_URL.rstrip('/')}/search?q={urlparse.quote_plus(query)}&format=json"
    try:
        req = request.Request(url, headers={"User-Agent": "UsesIndexer/1.0"})
        with request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as exc:
        return _search_ddg_lite(query, max_results)
    results = data.get("results", [])[:max_results]
    if not results:
        return "No search results found", False
    lines = []
    for i, r in enumerate(results, 1):
        title = r.get("title", "")
        link = r.get("url", "")
        snippet = r.get("content", "")
        lines.append(f"{i}. {title}\n   {link}\n   {snippet}")
    return _truncate("\n\n".join(lines)), False


def _search_ddg_lite(query: str, max_results: int) -> tuple[str, bool]:
    data = urlparse.urlencode({"q": query, "kl": "cn-zh"}).encode("utf-8")
    req = request.Request(
        _DDG_LITE_URL,
        data=data,
        headers={"User-Agent": "Mozilla/5.0 (compatible; UsesIndexer/1.0)"},
    )
    try:
        with request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return _search_bing(query, max_results)
    results = []
    link_pattern = re.compile(r'<a[^>]*class="result-link"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', re.DOTALL)
    snippet_pattern = re.compile(r'<td[^>]*class="result-snippet"[^>]*>(.*?)</td>', re.DOTALL)
    links = link_pattern.findall(html)
    snippets = snippet_pattern.findall(html)
    for i, (url, title) in enumerate(links[:max_results]):
        title_clean = re.sub(r"<[^>]+>", "", title).strip()
        snippet = re.sub(r"<[^>]+>", "", snippets[i]).strip() if i < len(snippets) else ""
        results.append(f"{i + 1}. {title_clean}\n   {url}\n   {snippet}")
    if not results:
        return _search_bing(query, max_results)
    return _truncate("\n\n".join(results)), False


def _search_bing(query: str, max_results: int) -> tuple[str, bool]:
    url = f"https://www.bing.com/search?q={urlparse.quote_plus(query)}&setlang=zh-CN"
    req = request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    })
    try:
        with request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except Exception as exc:
        return f"Search failed: {exc}", True
    results = []
    block_pattern = re.compile(r'<li class="b_algo"[^>]*>(.*?)</li>', re.DOTALL)
    link_pattern = re.compile(r'<a[^>]*href="(https?://[^"]+)"[^>]*>(.*?)</a>', re.DOTALL)
    snippet_pattern = re.compile(r'<p[^>]*>(.*?)</p>', re.DOTALL)
    for block in block_pattern.findall(html)[:max_results]:
        links = link_pattern.findall(block)
        snippets = snippet_pattern.findall(block)
        if links:
            url, title = links[0]
            title_clean = re.sub(r"<[^>]+>", "", title).strip()
            snippet = re.sub(r"<[^>]+>", "", snippets[0]).strip() if snippets else ""
            snippet = re.sub(r"&ensp;|&#0183;|&nbsp;", " ", snippet)
            results.append(f"{len(results) + 1}. {title_clean}\n   {url}\n   {snippet}")
    if not results:
        return "No search results found", False
    return _truncate("\n\n".join(results)), False


def _web_fetch(args: dict[str, Any]) -> tuple[str, bool]:
    url = args["url"]
    max_chars = int(args.get("max_chars", 10000))
    req = request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; UsesIndexer/1.0)"})
    try:
        with request.urlopen(req, timeout=20) as resp:
            raw = resp.read()
            content_type = resp.headers.get("Content-Type", "")
    except error.HTTPError as exc:
        return f"HTTP {exc.code}: {exc.reason}", True
    except Exception as exc:
        return f"Fetch failed: {exc}", True
    if "text/" in content_type or "json" in content_type or "xml" in content_type:
        text = raw.decode("utf-8", errors="replace")
        if "html" in content_type.lower():
            text = _html_to_text(text)
        return _truncate(text, limit=max_chars), False
    return f"Binary content ({content_type}, {len(raw)} bytes)", False


def _html_to_text(html: str) -> str:
    text = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</?p[^>]*>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<h[1-6][^>]*>", "\n## ", text, flags=re.IGNORECASE)
    text = re.sub(r"</h[1-6]>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<li[^>]*>", "\n- ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"&quot;", '"', text)
    text = re.sub(r"&#39;", "'", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ========================================================================
# Command Tools
# ========================================================================

COMMAND_TOOL_DEFINITIONS = [
    {
        "name": "run_command",
        "description": "Execute a shell command. Read-only commands (ls, cat, grep, git status, etc.) are auto-approved; others require confirmation. Runs in the project directory by default.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "Shell command to execute"},
                "cwd": {"type": "string", "description": "Working directory (defaults to project root)"},
                "timeout": {"type": "integer", "description": "Timeout in seconds (default 30)", "minimum": 1, "maximum": 120},
            },
            "required": ["command"],
            "additionalProperties": False,
        },
    },
]


async def _execute_command_tool(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _execute_command_tool_sync, name, arguments)


def _execute_command_tool_sync(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    if name != "run_command":
        return f"Unknown command tool: {name}", True
    command = arguments.get("command", "")
    if not command:
        return "Empty command", True
    cwd = arguments.get("cwd", str(_PROJECT_ROOT))
    try:
        cwd_path = _validate_path(cwd)
    except PermissionError:
        cwd_path = _PROJECT_ROOT
    timeout = int(arguments.get("timeout", 30))
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=str(cwd_path),
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout}s", True
    except Exception as exc:
        return f"Command failed: {exc}", True
    output = result.stdout
    if result.stderr:
        output += ("\nSTDERR:\n" + result.stderr) if output else ("STDERR:\n" + result.stderr)
    if result.returncode != 0:
        output += f"\n[Exit code: {result.returncode}]"
    return _truncate(output) if output else "(no output)", result.returncode != 0


# ========================================================================
# ToolSource factory functions
# ========================================================================


def create_builtin_file_source() -> ToolSource:
    return ToolSource(
        name="builtin",
        prefix="builtin__",
        definitions=FILE_TOOL_DEFINITIONS + WEB_TOOL_DEFINITIONS + COMMAND_TOOL_DEFINITIONS,
        execute=_execute_builtin_tool,
        requires_confirmation={"write_file", "edit_file", "delete_file", "move_file", "web_fetch", "run_command"},
    )


async def _execute_builtin_tool(name: str, arguments: dict[str, Any]) -> tuple[str, bool]:
    if name in ("read_file", "write_file", "list_directory", "search_files", "edit_file", "delete_file", "move_file", "copy_file"):
        return await _execute_file_tool(name, arguments)
    if name in ("web_search", "web_fetch"):
        return await _execute_web_tool(name, arguments)
    if name == "run_command":
        return await _execute_command_tool(name, arguments)
    return f"Unknown builtin tool: {name}", True


def is_safe_command(command: str) -> bool:
    """Check if a command is in the auto-approve whitelist."""
    stripped = command.strip()
    if not stripped:
        return False
    first_token = stripped.split()[0]
    base = Path(first_token).name
    return base in _SAFE_COMMANDS
