#!/usr/bin/env python3
"""Detect common instruction conflicts in a Codex-enabled repo.

This is a heuristic scanner. It does not replace human review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List, Dict


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def collect_files(repo: Path) -> List[Path]:
    candidates = [repo / "AGENTS.md", repo / "AGENTS.override.md", repo / "CONVENTIONS.md", repo / "PLANS.md", repo / "code_review.md"]
    candidates.extend((repo / ".codex" / "skills").glob("*/SKILL.md") if (repo / ".codex" / "skills").exists() else [])
    candidates.extend((repo / ".codex" / "rules").glob("*.rules") if (repo / ".codex" / "rules").exists() else [])
    candidates.append(repo / ".codex" / "config.toml")
    candidates.append(repo / ".codex" / "hooks.json")
    return [p for p in candidates if p.exists()]


def scan(repo: Path) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []
    files = collect_files(repo)
    texts = {p: read(p) for p in files}

    def has(pattern: str, text: str) -> bool:
        return re.search(pattern, text, re.IGNORECASE | re.MULTILINE) is not None

    agents = texts.get(repo / "AGENTS.md", "")
    if agents and not has(r"conflict|precedence|priority", agents):
        findings.append({"severity": "medium", "area": "AGENTS.md", "finding": "No explicit conflict/precedence section found."})

    if has(r"always\s+install|install\s+dependencies\s+automatically", "\n".join(texts.values())) and has(r"ask\s+before\s+adding\s+.*depend", "\n".join(texts.values())):
        findings.append({"severity": "high", "area": "dependencies", "finding": "Potential conflict: automatic dependency installation vs approval requirement."})

    if has(r"danger-full-access", "\n".join(texts.values())):
        findings.append({"severity": "high", "area": "sandbox", "finding": "danger-full-access is referenced. Confirm this is not a default policy."})

    if has(r"approval_policy\s*=\s*[\"']never[\"']", "\n".join(texts.values())):
        findings.append({"severity": "high", "area": "approval", "finding": "approval_policy = never found. Confirm this is intentional and controlled."})

    if has(r"network_access\s*=\s*true", "\n".join(texts.values())):
        findings.append({"severity": "high", "area": "network", "finding": "Shell network access is enabled. Confirm threat model and need."})

    if (repo / ".codex" / "hooks.json").exists() and has(r"\[hooks\.", texts.get(repo / ".codex" / "config.toml", "")):
        findings.append({"severity": "medium", "area": "hooks", "finding": "Same project layer appears to use hooks.json and inline TOML hooks."})

    if has(r"full\s+framework|entire\s+handbook|load\s+all", agents):
        findings.append({"severity": "medium", "area": "context", "finding": "AGENTS.md may be pulling too much framework context into every task."})

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Detect Codex instruction conflicts")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    findings = scan(Path(args.repo).resolve())
    if not findings:
        print("No obvious instruction conflicts found.")
        return 0
    print("# Potential Codex Instruction Conflicts\n")
    print("| Severity | Area | Finding |")
    print("|---|---|---|")
    for f in findings:
        print(f"| {f['severity']} | {f['area']} | {f['finding']} |")
    return 1 if any(f["severity"] == "high" for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
