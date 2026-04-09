from __future__ import annotations

import json
import shutil
from pathlib import Path


PLUGIN_NAME = "uses-codebase-plugin"
SKILL_NAME = "uses-codebase-search"


class CodexIntegrationInstaller:
    def __init__(
        self,
        *,
        repo_root: str | Path | None = None,
        home_root: str | Path | None = None,
        codex_home: str | Path | None = None,
    ) -> None:
        self.repo_root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[2]
        self.home_root = Path(home_root) if home_root else Path.home()
        self.codex_home = Path(codex_home) if codex_home else self.home_root / ".codex"

    def install(self, *, force: bool = False) -> dict[str, object]:
        plugin_source = self.repo_root / "plugins" / PLUGIN_NAME
        skill_source = self.repo_root / "skills" / SKILL_NAME

        if not plugin_source.exists():
            raise FileNotFoundError(f"Plugin source does not exist: {plugin_source}")
        if not skill_source.exists():
            raise FileNotFoundError(f"Skill source does not exist: {skill_source}")

        plugin_target = self.home_root / "plugins" / PLUGIN_NAME
        skill_target = self.codex_home / "skills" / SKILL_NAME
        marketplace_path = self.home_root / ".agents" / "plugins" / "marketplace.json"

        plugin_action = self._install_symlink(plugin_source, plugin_target, force=force)
        skill_action = self._install_symlink(skill_source, skill_target, force=force)
        marketplace_action = self._ensure_marketplace_entry(marketplace_path)

        return {
            "repo_root": str(self.repo_root),
            "plugin": {
                "source": str(plugin_source),
                "target": str(plugin_target),
                "action": plugin_action,
            },
            "skill": {
                "source": str(skill_source),
                "target": str(skill_target),
                "action": skill_action,
            },
            "marketplace": {
                "path": str(marketplace_path),
                "action": marketplace_action,
                "plugin_name": PLUGIN_NAME,
            },
        }

    def _install_symlink(self, source: Path, target: Path, *, force: bool) -> str:
        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() or target.is_symlink():
            if target.is_symlink() and target.resolve() == source.resolve():
                return "already_linked"
            if not force:
                raise FileExistsError(f"Target already exists: {target}")
            self._remove_existing(target)

        target.symlink_to(source, target_is_directory=True)
        return "linked"

    def _ensure_marketplace_entry(self, marketplace_path: Path) -> str:
        marketplace_path.parent.mkdir(parents=True, exist_ok=True)

        if marketplace_path.exists():
            data = json.loads(marketplace_path.read_text(encoding="utf-8"))
            action = "updated"
        else:
            data = {
                "name": "songscholar-local",
                "interface": {
                    "displayName": "Song Scholar Local Plugins"
                },
                "plugins": [],
            }
            action = "created"

        if not isinstance(data.get("plugins"), list):
            data["plugins"] = []

        entry = {
            "name": PLUGIN_NAME,
            "source": {
                "source": "local",
                "path": f"./plugins/{PLUGIN_NAME}",
            },
            "policy": {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
            },
            "category": "Productivity",
        }

        plugins = [plugin for plugin in data["plugins"] if plugin.get("name") != PLUGIN_NAME]
        plugins.append(entry)
        data["plugins"] = plugins

        marketplace_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return action

    def _remove_existing(self, target: Path) -> None:
        if target.is_symlink() or target.is_file():
            target.unlink()
            return
        shutil.rmtree(target)
