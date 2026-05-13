#!/usr/bin/env python3
"""Generate a conservative Claude-to-Codex migration plan.

This script does not write Codex files. It reads common Claude files and prints
where their content likely belongs in a Codex setup.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def exists(repo: Path, rel: str) -> bool:
    return (repo / rel).exists()


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan migration from Claude setup to Codex setup")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()

    mappings = []
    if exists(repo, "CLAUDE.md"):
        mappings.append(("CLAUDE.md", "AGENTS.md", "Durable repository guidance; keep concise and move long workflows into skills."))
    if exists(repo, ".claude/settings.json"):
        mappings.append((".claude/settings.json", ".codex/config.toml", "Technical defaults: model, approval, sandbox, hooks feature flags."))
    if exists(repo, ".claudeignore"):
        mappings.append((".claudeignore", ".gitignore / sandbox policy / AGENTS.md do-not rules", "Sensitive paths and generated files need Codex equivalents."))
    if (repo / ".claude").exists():
        mappings.append((".claude/hooks or commands", ".codex/hooks.json / .codex/rules / .codex/skills", "Classify deterministic checks as hooks, command policy as rules, workflows as skills."))

    print("# Claude to Codex Migration Plan\n")
    if not mappings:
        print("No common Claude setup files found.")
        return 0
    print("| Source | Codex target | Note |")
    print("|---|---|---|")
    for src, target, note in mappings:
        print(f"| `{src}` | `{target}` | {note} |")
    print("\n## Recommended next step\n")
    print("Create a draft AGENTS.md and .codex/config.toml, then run audit_codex_setup.py and detect_conflicts.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
