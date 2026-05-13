# Codex Setup Audit

- Overall status: Amber
- Findings: 4

## Findings

| Severity | Area | Finding | Recommendation |
|---|---|---|---|
| high | project config | Missing `.codex/config.toml` | Create project config from `references/templates/config-project.toml`. |
| medium | project instructions | `AGENTS.md` lacks conflict handling | Add neutral precedence section. |
| medium | project rules | No `.codex/rules/default.rules` | Add rules for destructive commands, dependency changes, git push, downloads, and deployment. |
| low | project planning | Missing `PLANS.md` | Add plan template for long-running work. |

## Suggested next step

Apply high-severity recommendations first, then rerun the audit.
