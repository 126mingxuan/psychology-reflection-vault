#!/usr/bin/env python3
"""Install the Psychology Reflection skill from this repository."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import shutil
from pathlib import Path


SKILL_NAME = "psychology-reflection"
AGENT_TARGETS = {
    "codex": Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    / "skills"
    / SKILL_NAME,
    "claude-code": Path.home() / ".claude" / "skills" / SKILL_NAME,
}


def copytree_clean(src: Path, dst: Path) -> None:
    def ignore(_: str, names: list[str]) -> set[str]:
        return {
            name
            for name in names
            if name in {".DS_Store", "__pycache__"} or name.endswith(".pyc")
        }

    shutil.copytree(src, dst, ignore=ignore)


def install_skill(source: Path, target: Path, no_backup: bool) -> Path | None:
    target = target.expanduser().resolve()
    target.parent.mkdir(parents=True, exist_ok=True)

    backup_path = None
    if target.exists():
        if no_backup:
            shutil.rmtree(target)
        else:
            timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
            backup_path = target.with_name(f"{target.name}.backup-{timestamp}")
            shutil.move(str(target), str(backup_path))

    copytree_clean(source, target)
    return backup_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Install the Psychology Reflection skill for supported agents."
    )
    parser.add_argument(
        "--agent",
        choices=["codex", "claude-code", "all"],
        default="codex",
        help="Agent to install for. Defaults to codex.",
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=None,
        help="Custom skill installation target. Only valid when installing one agent.",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Replace an existing target without creating a timestamped backup.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    source = repo_root / "skill" / SKILL_NAME

    if not source.exists():
        raise SystemExit(f"Source skill not found: {source}")

    if args.target and args.agent == "all":
        raise SystemExit("--target cannot be used with --agent all")

    agents = ["codex", "claude-code"] if args.agent == "all" else [args.agent]

    for agent in agents:
        target = args.target or AGENT_TARGETS[agent]
        backup_path = install_skill(source, target, args.no_backup)

        print(f"Installed {agent} skill: {SKILL_NAME}")
        print(f"Target: {target.expanduser().resolve()}")
        if backup_path:
            print(f"Previous installation backed up to: {backup_path}")
        print()

    print("Use it in Codex with:")
    print("  Use $psychology-reflection to start a structured reflection session.")
    print()
    print("Use it in Claude Code with:")
    print("  /psychology-reflection start a structured reflection session")
    print()
    print("Keep private session notes in a local vault such as:")
    print("  ~/Documents/psychology-reflection")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
