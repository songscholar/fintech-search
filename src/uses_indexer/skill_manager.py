"""Skill Manager — manages local and remote skills.

Skills are self-contained capabilities defined by a SKILL.md file.
They can come from:
  1. Local `skills/` directory (bundled with the project)
  2. Remote registry (downloaded and cached locally)
  3. MCP server resources (discovered from connected servers)

The manager provides unified discovery, listing, install/uninstall,
and search across all sources.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import zipfile
from pathlib import Path
from typing import Any
from urllib import request, error, parse as urlparse

from .logging_system import log_error, log_system

_PROJECT_ROOT = Path("/Users/songzuoqiang/Documents/agent/condex/codes")
_LOCAL_SKILLS_DIR = _PROJECT_ROOT / "skills"
_CACHE_DIR = _PROJECT_ROOT / ".cache" / "skills"

_REGISTRY_URL = os.environ.get("USES_INDEXER_SKILLS_REGISTRY_URL", "")


class SkillManager:
    """Manages local and remote skills."""

    def __init__(
        self,
        local_skills_dir: Path | None = None,
        cache_dir: Path | None = None,
    ) -> None:
        self.local_dir = local_skills_dir or _LOCAL_SKILLS_DIR
        self.cache_dir = cache_dir or _CACHE_DIR
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def list_skills(self) -> list[dict[str, Any]]:
        """Return all available skills (local + cached)."""
        skills: list[dict[str, Any]] = []
        seen: set[str] = set()

        # Local skills
        if self.local_dir.is_dir():
            for skill_dir in sorted(self.local_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.is_file():
                    continue
                name = skill_dir.name
                if name in seen:
                    continue
                seen.add(name)
                skills.append(self._parse_skill(name, skill_md, source="local"))

        # Cached (installed remote) skills
        if self.cache_dir.is_dir():
            for skill_dir in sorted(self.cache_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.is_file():
                    continue
                name = skill_dir.name
                if name in seen:
                    continue
                seen.add(name)
                skills.append(self._parse_skill(name, skill_md, source="remote"))

        return skills

    def get_skill(self, skill_id: str) -> dict[str, Any] | None:
        """Get a specific skill by ID. Returns None if not found."""
        for skill in self.list_skills():
            if skill["id"] == skill_id:
                return skill
        return None

    def get_skill_content(self, skill_id: str) -> str | None:
        """Get the SKILL.md content for a skill. Returns None if not found."""
        skill = self.get_skill(skill_id)
        if not skill:
            return None
        return skill.get("content")

    def _parse_skill(self, name: str, skill_md: Path, source: str) -> dict[str, Any]:
        """Parse SKILL.md to extract metadata and content."""
        try:
            raw = skill_md.read_text(encoding="utf-8")
        except Exception:
            raw = ""

        # Parse YAML frontmatter
        frontmatter: dict[str, Any] = {}
        body = raw
        fm_match = re.match(r"^---\s*\n([\s\S]*?)---\s*\n?", raw)
        if fm_match:
            try:
                import yaml
                frontmatter = yaml.safe_load(fm_match.group(1)) or {}
            except Exception:
                frontmatter = {}
            body = raw[fm_match.end():]

        title = frontmatter.get("name", name)
        description = frontmatter.get("description", "")
        commands: list[str] = []

        if not description:
            # Fallback: extract from first paragraph after title
            parts = body.split("\n\n")
            for part in parts[:3]:
                text = part.strip()
                if text and not text.startswith("#") and not text.startswith("```"):
                    description = text[:200]
                    break

        # Extract command triggers
        for match in re.finditer(r"(?:命令|Command|Trigger|触发)[：:]?\s*`?/(\S+)`?", body, re.IGNORECASE):
            commands.append(match.group(1))

        return {
            "id": name,
            "title": title,
            "description": description[:200],
            "commands": commands,
            "source": source,
            "path": str(skill_md.parent),
            "content": body,
        }

    async def search_remote(self, query: str) -> list[dict[str, Any]]:
        """Search the remote registry for skills. Returns empty list if no registry configured."""
        if not _REGISTRY_URL:
            return []

        url = f"{_REGISTRY_URL.rstrip('/')}/skills?q={urlparse.quote_plus(query)}"
        req = request.Request(url, headers={"User-Agent": "UsesIndexer/1.0"})
        try:
            with request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as exc:
            log_error(
                event="skill_search_failed",
                message=str(exc),
                exc=exc,
                context={"query": query},
            )
            return []

        results = data if isinstance(data, list) else data.get("results", [])
        return results[:20]

    async def install_skill(self, skill_id: str) -> dict[str, Any]:
        """Install a skill from the remote registry."""
        if not _REGISTRY_URL:
            return {"ok": False, "error": "No skills registry configured"}

        # Check if already installed
        target_dir = self.cache_dir / skill_id
        if target_dir.exists():
            return {"ok": True, "skill_id": skill_id, "status": "already_installed"}

        # Download skill info
        info_url = f"{_REGISTRY_URL.rstrip('/')}/skills/{urlparse.quote_plus(skill_id)}"
        req = request.Request(info_url, headers={"User-Agent": "UsesIndexer/1.0"})
        try:
            with request.urlopen(req, timeout=10) as resp:
                info = json.loads(resp.read().decode("utf-8"))
        except error.HTTPError as exc:
            return {"ok": False, "error": f"Skill not found: {exc.code}"}
        except Exception as exc:
            return {"ok": False, "error": f"Download failed: {exc}"}

        # Create skill directory and write SKILL.md
        target_dir.mkdir(parents=True, exist_ok=True)
        skill_content = info.get("content", info.get("skill_md", ""))
        if skill_content:
            (target_dir / "SKILL.md").write_text(skill_content, encoding="utf-8")

        log_system(event="skill_installed", context={"skill_id": skill_id})
        return {"ok": True, "skill_id": skill_id, "status": "installed"}

    def uninstall_skill(self, skill_id: str) -> dict[str, Any]:
        """Uninstall a cached (remote) skill. Local skills cannot be uninstalled."""
        target_dir = self.cache_dir / skill_id
        if not target_dir.exists():
            return {"ok": False, "error": f"Skill '{skill_id}' not found in cache"}

        # Only allow uninstalling cached skills, not local ones
        local_path = self.local_dir / skill_id
        if local_path.exists():
            return {"ok": False, "error": f"Skill '{skill_id}' is a local skill and cannot be uninstalled"}

        shutil.rmtree(target_dir)
        log_system(event="skill_uninstalled", context={"skill_id": skill_id})
        return {"ok": True, "skill_id": skill_id}
