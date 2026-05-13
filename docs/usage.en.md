# Usage and Modes

## English

This page explains the different ways to use the `codex-setup-checklist` skill.

## 1. Install a Best-Practice Setup

Use this mode when a repository does not yet have a clean Codex setup.

Prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Typical output:

- `AGENTS.md` with working rules, safety boundaries, and definition of done
- `.codex/config.toml` with conservative defaults
- `.codex/rules/default.rules` for command governance
- optionally `.codex/hooks.json`
- optionally `PLANS.md` and `code_review.md`

## 2. Audit Mode

Use this mode when you want to know whether an existing Codex setup is safe and consistent.

Prompt:

```text
Use the codex-setup-checklist skill to audit this repository.
```

The skill checks:

- global and project config
- `AGENTS.md` and override files
- rules and hooks
- skill metadata
- conflict handling
- review and planning files

## 3. Global Codex Setup

Use this mode for personal defaults below `~/.codex/`.

Prompt:

```text
Use the codex-setup-checklist skill to set up my global Codex defaults.
```

Typical output:

- `~/.codex/config.toml`
- `~/.codex/AGENTS.md`
- `~/.codex/rules/default.rules`
- optionally `~/.codex/hooks.json`

## 4. Claude-to-Codex Migration

Use this mode when a project already uses `CLAUDE.md`, `.claude/settings.json`, `.claudeignore`, Claude hooks, or Claude commands.

Prompt:

```text
Use the codex-setup-checklist skill to migrate my Claude setup to Codex.
```

The skill maps content as follows:

| Claude element | Codex target |
|---|---|
| `CLAUDE.md` | `AGENTS.md` or skill reference |
| `.claude/settings.json` | `.codex/config.toml` |
| `.claudeignore` | sandbox, rules, or `.gitignore` |
| Claude hooks | Codex hooks |
| Claude commands | skills or scripts |

## 5. Conflict Check

Use this mode when you suspect that several instruction layers work against each other.

Prompt:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

The skill looks especially for conflicts between:

- user prompt
- global `AGENTS.md`
- project-level `AGENTS.md`
- skills
- framework or methodology documents
- rules
- hooks

## Recommended Order

For a new team or repository:

1. Run `audit` to understand the current state.
2. Use `project` to install the best-practice setup.
3. Run `conflict-check` if existing frameworks or old AI rules are present.
4. Use `migrate-claude` if Claude files exist.
5. Run the validation scripts.

## Deutsche Kurzfassung

Diese englische Nutzungsanleitung erklaert die Modi des Skills `codex-setup-checklist`.

Die vollstaendige deutsche Anleitung findest du unter [`usage.de.md`](usage.de.md).

Hauptmodi:

- `audit`: bestehendes Codex-Setup pruefen.
- `global`: persoenliche Defaults unter `~/.codex/` einrichten.
- `project`: Best-Practice-Setup in einem Repository installieren.
- `migrate-claude`: Claude-Dateien nach Codex migrieren.
- `conflict-check`: Konflikte zwischen Anweisungsebenen erkennen.
