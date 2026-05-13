#!/usr/bin/env python3
"""Lightweight static validation for Codex .rules files.

For real execution-policy validation, use:
  codex execpolicy check --pretty --rules <file> -- <command>
"""

from __future__ import annotations

import argparse
from pathlib import Path


def validate(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    issues: list[str] = []
    if "prefix_rule" not in text:
        issues.append("No prefix_rule entries found.")
    if "decision" not in text:
        issues.append("No decision field found.")
    if "justification" not in text:
        issues.append("No justification field found.")
    if "match" not in text:
        issues.append("No match examples found.")
    if text.count("(") != text.count(")"):
        issues.append("Unbalanced parentheses detected.")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate .rules files")
    parser.add_argument("paths", nargs="+", help="Rules files to validate")
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
