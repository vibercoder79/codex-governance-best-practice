#!/usr/bin/env python3
"""Lightweight static validation for Codex .rules files.

DE: Leichtgewichtige statische Validierung fuer Codex-.rules-Dateien.

For real execution-policy validation, use:
  codex execpolicy check --pretty --rules <file> -- <command>
DE: Fuer echte Execution-Policy-Validierung nutze denselben codex execpolicy check.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if "prefix_rule" not in text:
        issues.append("EN: No prefix_rule entries found. DE: Keine prefix_rule-Eintraege gefunden.")
    if "decision" not in text:
        issues.append("EN: No decision field found. DE: Kein decision-Feld gefunden.")
    if "justification" not in text:
        issues.append("EN: No justification field found. DE: Kein justification-Feld gefunden.")
    if "match" not in text:
        issues.append("EN: No match examples found. DE: Keine match-Beispiele gefunden.")
    if text.count("(") != text.count(")"):
        issues.append("EN: Unbalanced parentheses detected. DE: Unausgeglichene Klammern erkannt.")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate .rules files / .rules-Dateien validieren")
    parser.add_argument("paths", nargs="+", help="Rules files to validate / Zu validierende Rules-Dateien")
    args = parser.parse_args()
    exit_code = 0
    for p in map(Path, args.paths):
        issues = validate(p)
        if issues:
            exit_code = 1
            print(f"{p}: FAIL")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"{p}: OK")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
