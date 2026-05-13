# OpenAI Codex Best-Practice Notes

This file captures the practical assumptions used by the skill. Verify against current OpenAI Codex documentation before making policy-sensitive changes.

## AGENTS.md

- Codex reads `AGENTS.md` before work starts.
- Global guidance lives under the Codex home directory, usually `~/.codex`.
- Project-level guidance is discovered from the project root down to the current working directory.
- Files closer to the current directory override earlier guidance because they appear later in the combined prompt.
- `AGENTS.override.md` is read before `AGENTS.md` at the same level.
- Instruction loading is capped by `project_doc_max_bytes`; the default is commonly 32 KiB.
- Keep AGENTS.md practical and concise.

## Config

- User config lives in `~/.codex/config.toml`.
- Project config lives in `.codex/config.toml`.
- Project-scoped `.codex/` layers only load when the project is trusted.
- CLI flags and explicit config overrides win over config files.
- Project config has higher precedence than user config.

## Skills

- A skill is a directory with a required `SKILL.md` file and optional `scripts/`, `references/`, and `assets/` folders.
- `SKILL.md` must include `name` and `description` metadata.
- Codex initially sees the skill name, description, and path; full instructions are loaded only when Codex activates the skill.
- Skill descriptions should front-load trigger terms and boundaries.

## Rules

- Rules live in `rules/*.rules` next to an active config layer.
- Rules control which commands Codex can run outside the sandbox.
- `forbidden` beats `prompt`, which beats `allow` when multiple rules match.
- Use `match` and `not_match` examples as inline unit tests.
- Test with `codex execpolicy check`.

## Hooks

- Hooks require `[features] codex_hooks = true`.
- Hooks can be configured via `hooks.json` or inline `[hooks]` tables in `config.toml`.
- Prefer one hook representation per config layer.
- Matching hooks from multiple files can all run.
- Hooks are useful for deterministic checks, prompt scanning, and stop-time validation.

## Recommended setup stance

- Conservative default: `approval_policy = "on-request"` and `sandbox_mode = "workspace-write"`.
- Keep shell network access off by default for local work.
- Use web search deliberately rather than allowing broad shell network access.
- Exclude secrets from inherited shell environment.
- Treat framework docs as method references, not higher-priority instructions.
