from __future__ import annotations

import json
from pathlib import Path

from uses_indexer.integration import CodexIntegrationInstaller


def _build_fake_repo(tmp_path: Path) -> Path:
    repo_root = tmp_path / "repo"
    plugin_root = repo_root / "plugins" / "uses-codebase-plugin" / ".codex-plugin"
    plugin_root.mkdir(parents=True)
    (plugin_root / "plugin.json").write_text('{"name":"uses-codebase-plugin"}\n', encoding="utf-8")

    skill_root = repo_root / "skills" / "uses-codebase-search"
    skill_root.mkdir(parents=True)
    (skill_root / "SKILL.md").write_text("# skill\n", encoding="utf-8")
    return repo_root


def test_install_creates_symlinks_and_marketplace(tmp_path: Path) -> None:
    repo_root = _build_fake_repo(tmp_path)
    home_root = tmp_path / "home"
    codex_home = home_root / ".codex"

    installer = CodexIntegrationInstaller(
        repo_root=repo_root,
        home_root=home_root,
        codex_home=codex_home,
    )

    result = installer.install()

    plugin_target = Path(result["plugin"]["target"])
    skill_target = Path(result["skill"]["target"])
    marketplace_path = Path(result["marketplace"]["path"])

    assert plugin_target.is_symlink()
    assert skill_target.is_symlink()
    assert plugin_target.resolve() == (repo_root / "plugins" / "uses-codebase-plugin").resolve()
    assert skill_target.resolve() == (repo_root / "skills" / "uses-codebase-search").resolve()

    marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    assert marketplace["plugins"][0]["name"] == "uses-codebase-plugin"


def test_install_is_idempotent_when_symlink_already_exists(tmp_path: Path) -> None:
    repo_root = _build_fake_repo(tmp_path)
    home_root = tmp_path / "home"
    codex_home = home_root / ".codex"

    installer = CodexIntegrationInstaller(
        repo_root=repo_root,
        home_root=home_root,
        codex_home=codex_home,
    )

    first = installer.install()
    second = installer.install()

    assert first["plugin"]["action"] == "linked"
    assert second["plugin"]["action"] == "already_linked"
