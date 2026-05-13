---
name: codex-setup-checklist
description: Interactive Codex setup, audit, and governance bootstrap for AGENTS.md, ~/.codex/config.toml, .codex/config.toml, rules, hooks, skills, sandbox/approval policy, and Claude-to-Codex migration. Trigger when the user asks to set up Codex, audit Codex, create AGENTS.md, configure config.toml, add rules/hooks, migrate Claude.md, or check conflicts between Codex instructions and skills.
---

# Codex Setup Checklist Skill

## Purpose

Guide the user through a safe, repeatable Codex setup. The skill covers:

- global Codex configuration
- project-level Codex configuration
- AGENTS.md guidance
- rules and hooks
- skill installation and metadata hygiene
- conflict handling across instruction layers
- optional migration from Claude-style configuration

This skill is not a generic coding workflow and not a product-development framework. Keep the scope tight: Codex setup, audit, governance, and migration.

## Core operating rules

1. Inspect before writing.
2. Do not overwrite existing files without showing what will change.
3. Prefer merge/patch over full replacement.
4. Never print, create, modify, or commit secrets.
5. Do not loosen sandbox, approval, or network restrictions unless the user explicitly asks and the risk is stated.
6. Keep AGENTS.md concise. Put task-specific process into skills, references, PLANS.md, or code_review.md.
7. If instruction layers conflict, report the conflict and follow the safest non-destructive path.

## Supported modes

When the user does not specify a mode, ask one concise question or infer the safest mode from context.

### `audit`

Use when the user asks to check an existing Codex setup.

Steps:

1. Identify scope: global, project, or both.
2. Inspect relevant files:
   - `~/.codex/config.toml`
   - `~/.codex/AGENTS.md`
   - `~/.codex/AGENTS.override.md`
   - `~/.codex/rules/*.rules`
   - `~/.codex/hooks.json`
   - `AGENTS.md`
   - `AGENTS.override.md`
   - `.codex/config.toml`
   - `.codex/rules/*.rules`
   - `.codex/hooks.json`
   - `.codex/skills/*/SKILL.md`
   - `PLANS.md`
   - `code_review.md`
3. Run `python3 scripts/audit_codex_setup.py --scope project --repo .` when the script is available.
4. Summarise findings by severity:
   - Critical: unsafe or conflicting setup
   - High: likely to reduce result quality or safety
   - Medium: useful improvement
   - Low: cosmetic or documentation hygiene
5. Provide exact file-level recommendations.

### `global`

Use when setting up personal Codex defaults.

Create or update:

- `~/.codex/config.toml`
- `~/.codex/AGENTS.md`
- `~/.codex/rules/default.rules`
- optionally `~/.codex/hooks.json`

Recommended defaults:

- `approval_policy = "on-request"`
- `sandbox_mode = "workspace-write"`
- `sandbox_workspace_write.network_access = false`
- `model_reasoning_effort = "high"`
- `plan_mode_reasoning_effort = "high"`
- `web_search = "cached"`
- `project_doc_max_bytes = 65536`
- shell environment policy excludes tokens, keys, and secrets

### `project`

Use when setting up a repository.

Create or update:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/rules/default.rules`
- `.codex/hooks.json`
- `.codex/hooks/*.py` when needed
- optional `PLANS.md`
- optional `code_review.md`

Do not turn AGENTS.md into a full framework document. It should cover:

- repository layout
- build/test/lint commands
- engineering conventions
- safety/do-not rules
- definition of done
- conflict handling
- references to skills and framework docs

### `migrate-claude`

Use when the user has `CLAUDE.md`, `.claude/settings.json`, `.claudeignore`, Claude hooks, or Claude commands.

Migration approach:

1. Read Claude files.
2. Classify content:
   - durable guidance → AGENTS.md
   - technical defaults → config.toml
   - command restrictions → rules
   - deterministic lifecycle behavior → hooks
   - repeatable workflow → skill
   - ignored files / sensitive paths → sandbox/rules/gitignore guidance
3. Produce a migration plan.
4. Only write files after showing the mapping.
5. Preserve the original Claude files unless the user explicitly asks to remove them.

### `conflict-check`

Use when the user asks whether AGENTS.md, skills, framework docs, hooks, or rules may conflict.

Inspect:

- AGENTS hierarchy
- project_doc_fallback_filenames
- override files
- skill metadata and skill instructions
- rules decisions
- hook locations
- framework references
- PLANS.md and code_review.md

Conflict precedence to recommend:

1. Safety, security, secrets, sandbox, approval, and destructive-action rules.
2. Explicit user instructions for the current task, unless unsafe.
3. Project-specific AGENTS.md instructions over global AGENTS.md instructions.
4. Explicitly invoked skills for task-specific workflow.
5. Framework documents for method and terminology only.
6. Rules and hooks as enforcement mechanisms.

If a task cannot satisfy all layers, stop and report the conflict.

## Output format

For audits, use:

```markdown
# Codex Setup Audit

## Summary

- Overall status: Green / Amber / Red
- Main risk:
- Recommended next action:

## Findings

| Severity | Area | Finding | Recommendation |
|---|---|---|---|

## Proposed changes

## Commands to verify

## Residual risks
```

For setup generation, use:

```markdown
# Proposed Codex Setup

## Files to create/update

## Decisions made

## Files

<file-by-file summary>

## Verification
```

## Reference files

Use these templates when generating files:

- `references/templates/agents-global.md`
- `references/templates/agents-project.md`
- `references/templates/config-global.toml`
- `references/templates/config-project.toml`
- `references/templates/rules-default.rules`
- `references/templates/hooks.json`
- `references/templates/PLANS.md`
- `references/templates/code_review.md`

Use these scripts where useful:

- `scripts/audit_codex_setup.py`
- `scripts/detect_conflicts.py`
- `scripts/validate_rules.py`
- `scripts/migrate_claude_to_codex.py`
