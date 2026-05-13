#!/usr/bin/env python3
"""Generate a conservative Claude-to-Codex migration plan.

DE: Erzeugt einen konservativen Migrationsplan von Claude nach Codex.

This script does not write Codex files. It reads common Claude files and prints
where their content likely belongs in a Codex setup.
DE: Dieses Script schreibt keine Codex-Dateien. Es liest typische Claude-Dateien
und zeigt, wohin deren Inhalte in einem Codex-Setup gehoeren.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def exists(repo: Path, rel: str) -> bool:
    return (repo / rel).exists()


def main() -> int:
    parser = argparse.ArgumentParser(description="Plan migration from Claude setup to Codex setup / Migration von Claude-Setup zu Codex-Setup planen")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo).resolve()

    mappings = []
    if exists(repo, "CLAUDE.md"):
        mappings.append(("CLAUDE.md", "AGENTS.md", "EN: Durable repository guidance; keep concise and move long workflows into skills. DE: Dauerhafte Repo-Guidance; knapp halten und lange Workflows in Skills verschieben."))
    if exists(repo, ".claude/settings.json"):
        mappings.append((".claude/settings.json", ".codex/config.toml", "EN: Technical defaults: model, approval, sandbox, hooks feature flags. DE: Technische Defaults: Modell, Approval, Sandbox, Hook-Feature-Flags."))
    if exists(repo, ".claudeignore"):
        mappings.append((".claudeignore", ".gitignore / sandbox policy / AGENTS.md do-not rules", "EN: Sensitive paths and generated files need Codex equivalents. DE: Sensitive Pfade und generierte Dateien brauchen Codex-Aequivalente."))
    if (repo / ".claude").exists():
        mappings.append((".claude/hooks or commands", ".codex/hooks.json / .codex/rules / .codex/skills", "EN: Classify deterministic checks as hooks, command policy as rules, workflows as skills. DE: Deterministische Checks als Hooks, Kommando-Policy als Rules, Workflows als Skills klassifizieren."))

    print("# Claude to Codex Migration Plan / Claude-zu-Codex-Migrationsplan\n")
    if not mappings:
        print("No common Claude setup files found. / Keine typischen Claude-Setup-Dateien gefunden.")
        return 0
    print("| Source / Quelle | Codex target / Codex-Ziel | Note / Hinweis |")
    print("|---|---|---|")
    for src, target, note in mappings:
        print(f"| `{src}` | `{target}` | {note} |")
    print("\n## Recommended next step / Empfohlener naechster Schritt\n")
    print("EN: Create a draft AGENTS.md and .codex/config.toml, then run audit_codex_setup.py and detect_conflicts.py.")
    print("DE: Erstelle Entwuerfe fuer AGENTS.md und .codex/config.toml, danach audit_codex_setup.py und detect_conflicts.py ausfuehren.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
