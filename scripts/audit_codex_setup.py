#!/usr/bin/env python3
"""Audit a Codex setup at global and/or project scope.

This script is intentionally conservative. It does not modify files.
It reports likely setup gaps and governance risks.
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}


def read_text(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except UnicodeDecodeError:
        return None


def read_toml(path: Path) -> Dict[str, Any]:
    if not path.exists() or tomllib is None:
        return {}
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"__parse_error__": str(exc)}


def add(findings: List[Dict[str, str]], severity: str, area: str, finding: str, recommendation: str) -> None:
    findings.append({
        "severity": severity,
        "area": area,
        "finding": finding,
        "recommendation": recommendation,
    })


def is_repo_root(path: Path) -> bool:
    return (path / ".git").exists() or (path / "AGENTS.md").exists() or (path / ".codex").exists()


def check_config(findings: List[Dict[str, str]], path: Path, scope: str) -> None:
    cfg = read_toml(path)
    if not path.exists():
        add(findings, "high", f"{scope} config", f"Missing {path}", "Create config.toml using the template in references/templates.")
        return
    if "__parse_error__" in cfg:
        add(findings, "critical", f"{scope} config", f"Cannot parse {path}: {cfg['__parse_error__']}", "Fix TOML syntax before relying on this config layer.")
        return

    approval = cfg.get("approval_policy")
    if approval not in {"on-request", "untrusted"}:
        add(findings, "high", f"{scope} config", f"approval_policy is {approval!r}", "Use 'on-request' as a safe default unless a stricter managed policy applies.")

    sandbox = cfg.get("sandbox_mode")
    if sandbox not in {"workspace-write", "read-only"}:
        add(findings, "high", f"{scope} config", f"sandbox_mode is {sandbox!r}", "Use 'workspace-write' or 'read-only' by default; avoid danger-full-access.")

    sw = cfg.get("sandbox_workspace_write", {}) if isinstance(cfg.get("sandbox_workspace_write", {}), dict) else {}
    if sw.get("network_access") is not False:
        add(findings, "high", f"{scope} config", "Shell network access is not explicitly disabled", "Set [sandbox_workspace_write].network_access = false by default.")

    if cfg.get("project_doc_max_bytes") is None:
        add(findings, "medium", f"{scope} config", "project_doc_max_bytes not set", "Consider 65536 for larger repos, especially with fallback docs.")
    elif isinstance(cfg.get("project_doc_max_bytes"), int) and cfg["project_doc_max_bytes"] < 65536:
        add(findings, "medium", f"{scope} config", f"project_doc_max_bytes is {cfg['project_doc_max_bytes']}", "Consider 65536 if AGENTS/fallback docs are larger than default.")

    features = cfg.get("features", {}) if isinstance(cfg.get("features", {}), dict) else {}
    hooks_json = path.parent / "hooks.json"
    has_inline_hooks = "hooks" in cfg
    if hooks_json.exists() and has_inline_hooks:
        add(findings, "medium", f"{scope} hooks", "Both hooks.json and inline hooks are configured in the same layer", "Prefer one hook representation per config layer.")
    if hooks_json.exists() and features.get("codex_hooks") is not True:
        add(findings, "medium", f"{scope} hooks", "hooks.json exists but codex_hooks feature flag is not enabled", "Add [features] codex_hooks = true.")

    env_policy = cfg.get("shell_environment_policy", {}) if isinstance(cfg.get("shell_environment_policy", {}), dict) else {}
    if scope == "global" and not env_policy:
        add(findings, "medium", f"{scope} config", "No shell_environment_policy found", "Exclude token/secret/key/password patterns from inherited shell environment.")


def check_agents(findings: List[Dict[str, str]], path: Path, scope: str) -> None:
    text = read_text(path)
    if text is None:
        add(findings, "high", f"{scope} instructions", f"Missing {path}", "Create AGENTS.md with concise durable guidance.")
        return
    if len(text.encode("utf-8")) > 65536:
        add(findings, "medium", f"{scope} instructions", f"{path} is larger than 64 KiB", "Split detailed workflows into skills/references and keep AGENTS.md concise.")
    lower = text.lower()
    if "conflict" not in lower and "precedence" not in lower:
        add(findings, "medium", f"{scope} instructions", f"{path} lacks explicit conflict handling", "Add a neutral precedence section for AGENTS, skills, framework docs, rules, hooks, and user instructions.")
    if "secret" not in lower and "credential" not in lower:
        add(findings, "medium", f"{scope} instructions", f"{path} lacks explicit secrets guidance", "Add rules preventing creation, exposure, or modification of secrets.")


def check_override(findings: List[Dict[str, str]], path: Path, scope: str) -> None:
    if path.exists():
        add(findings, "medium", f"{scope} instructions", f"Override file present: {path}", "Confirm this override is intentional; override files take precedence over AGENTS.md at the same level.")


def check_rules(findings: List[Dict[str, str]], rules_dir: Path, scope: str) -> None:
    if not rules_dir.exists():
        add(findings, "low", f"{scope} rules", f"Missing rules directory: {rules_dir}", "Add rules/default.rules when command governance is needed.")
        return
    rule_files = list(rules_dir.glob("*.rules"))
    if not rule_files:
        add(findings, "low", f"{scope} rules", f"No .rules files under {rules_dir}", "Add default.rules for destructive commands, dependency changes, git push, deployments, and downloads.")
        return
    for rf in rule_files:
        txt = read_text(rf) or ""
        if "prefix_rule" not in txt:
            add(findings, "medium", f"{scope} rules", f"{rf} has no prefix_rule entries", "Add prefix_rule entries or remove the empty rule file.")
        if "match" not in txt:
            add(findings, "low", f"{scope} rules", f"{rf} has no inline match tests", "Add match/not_match examples and validate with codex execpolicy check.")


def check_skills(findings: List[Dict[str, str]], skills_dir: Path, scope: str) -> None:
    if not skills_dir.exists():
        return
    for skill_md in skills_dir.glob("*/SKILL.md"):
        txt = read_text(skill_md) or ""
        if "name:" not in txt or "description:" not in txt:
            add(findings, "medium", f"{scope} skills", f"{skill_md} missing name or description metadata", "Add concise frontmatter with name and description.")
        desc_idx = txt.find("description:")
        if desc_idx >= 0:
            line = txt[desc_idx:].splitlines()[0]
            if len(line) > 500:
                add(findings, "low", f"{scope} skills", f"Long skill description in {skill_md}", "Front-load trigger terms and scope; keep description concise.")


def audit(scope: str, repo: Path, home: Path) -> List[Dict[str, str]]:
    findings: List[Dict[str, str]] = []

    if scope in {"global", "both"}:
        codex_home = home / ".codex"
        check_config(findings, codex_home / "config.toml", "global")
        check_agents(findings, codex_home / "AGENTS.md", "global")
        check_override(findings, codex_home / "AGENTS.override.md", "global")
        check_rules(findings, codex_home / "rules", "global")
        check_skills(findings, codex_home / "skills", "global")

    if scope in {"project", "both"}:
        check_config(findings, repo / ".codex" / "config.toml", "project")
        check_agents(findings, repo / "AGENTS.md", "project")
        check_override(findings, repo / "AGENTS.override.md", "project")
        check_rules(findings, repo / ".codex" / "rules", "project")
        check_skills(findings, repo / ".codex" / "skills", "project")
        if not (repo / "PLANS.md").exists():
            add(findings, "low", "project planning", "Missing PLANS.md", "Add PLANS.md for longer-running tasks.")
        if not (repo / "code_review.md").exists():
            add(findings, "low", "project review", "Missing code_review.md", "Add code_review.md for consistent review expectations.")

    findings.sort(key=lambda f: SEVERITY_ORDER.get(f["severity"], 99))
    return findings


def render_markdown(findings: List[Dict[str, str]]) -> str:
    status = "Green" if not findings else "Amber"
    if any(f["severity"] in {"critical", "high"} for f in findings):
        status = "Red"
    lines = ["# Codex Setup Audit", "", f"- Overall status: {status}", f"- Findings: {len(findings)}", "", "## Findings", "", "| Severity | Area | Finding | Recommendation |", "|---|---|---|---|"]
    for f in findings:
        lines.append(f"| {f['severity']} | {f['area']} | {f['finding']} | {f['recommendation']} |")
    lines += ["", "## Suggested next step", "", "Apply high-severity recommendations first, then rerun the audit."]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Codex setup")
    parser.add_argument("--scope", choices=["global", "project", "both"], default="project")
    parser.add_argument("--repo", default=".")
    parser.add_argument("--home", default=str(Path.home()))
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()

    findings = audit(args.scope, Path(args.repo).resolve(), Path(args.home).resolve())
    if args.format == "json":
        print(json.dumps({"findings": findings}, indent=2))
    else:
        print(render_markdown(findings))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
