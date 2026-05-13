# Nutzung und Modi

## Deutsch

Diese Seite erklaert, wie der Skill `codex-setup-checklist` unterschiedlich genutzt werden kann.

## 1. Best-Practice-Setup installieren

Nutze diesen Modus, wenn ein Repository noch kein sauberes Codex-Setup hat.

Prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Typisches Ergebnis:

- `AGENTS.md` mit Arbeitsregeln, Sicherheitsgrenzen und Definition of Done
- `.codex/config.toml` mit konservativen Defaults
- `.codex/rules/default.rules` fuer Kommando-Governance
- optional `.codex/hooks.json`
- optional `PLANS.md` und `code_review.md`

## 2. Audit-Modus

Nutze diesen Modus, wenn du wissen willst, ob ein bestehendes Codex-Setup sicher und konsistent ist.

Prompt:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Der Skill prueft unter anderem:

- globale und projektbezogene Config
- `AGENTS.md` und Override-Dateien
- Rules und Hooks
- Skill-Metadaten
- Konfliktlogik
- Review- und Planungsdateien

## 3. Globales Codex-Setup

Nutze diesen Modus fuer persoenliche Defaults unter `~/.codex/`.

Prompt:

```text
Use the codex-setup-checklist skill to set up my global Codex defaults.
```

Typisches Ergebnis:

- `~/.codex/config.toml`
- `~/.codex/AGENTS.md`
- `~/.codex/rules/default.rules`
- optional `~/.codex/hooks.json`

## 4. Claude-zu-Codex-Migration

Nutze diesen Modus, wenn ein Projekt bereits `CLAUDE.md`, `.claude/settings.json`, `.claudeignore`, Claude Hooks oder Claude Commands nutzt.

Prompt:

```text
Use the codex-setup-checklist skill to migrate my Claude setup to Codex.
```

Der Skill ordnet Inhalte so zu:

| Claude-Element | Codex-Ziel |
|---|---|
| `CLAUDE.md` | `AGENTS.md` oder Skill-Referenz |
| `.claude/settings.json` | `.codex/config.toml` |
| `.claudeignore` | Sandbox, Rules oder `.gitignore` |
| Claude Hooks | Codex Hooks |
| Claude Commands | Skills oder Scripts |

## 5. Konfliktpruefung

Nutze diesen Modus, wenn du vermutest, dass mehrere Anweisungsebenen gegeneinander arbeiten.

Prompt:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

Der Skill achtet besonders auf Konflikte zwischen:

- User Prompt
- globalem `AGENTS.md`
- projektbezogenem `AGENTS.md`
- Skills
- Framework- oder Methoden-Dokumenten
- Rules
- Hooks

## Empfohlene Reihenfolge

Fuer ein neues Team oder Repository:

1. `audit` ausfuehren, um den Ausgangszustand zu verstehen.
2. `project` nutzen, um das Best-Practice-Setup zu installieren.
3. `conflict-check` ausfuehren, wenn bestehende Frameworks oder alte KI-Regeln vorhanden sind.
4. `migrate-claude` nutzen, falls Claude-Dateien existieren.
5. Validierungsskripte laufen lassen.

## English Summary

This German usage guide explains the supported modes of the `codex-setup-checklist` skill.

For the full English guide, see [`usage.en.md`](usage.en.md).

Main modes:

- `audit`: check an existing Codex setup.
- `global`: set up personal defaults below `~/.codex/`.
- `project`: install a best-practice setup in a repository.
- `migrate-claude`: migrate Claude-style files to Codex.
- `conflict-check`: detect conflicts between instruction layers.
