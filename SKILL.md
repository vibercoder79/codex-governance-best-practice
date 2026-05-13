---
name: codex-setup-checklist
description: Interactive bilingual Codex setup, audit, and governance bootstrap for AGENTS.md, ~/.codex/config.toml, .codex/config.toml, rules, hooks, skills, sandbox/approval policy, and Claude-to-Codex migration. Trigger when the user asks to set up Codex, install Codex best practices, audit Codex, create AGENTS.md, configure config.toml, add rules/hooks, migrate CLAUDE.md, or check conflicts between Codex instructions and skills.
---

# Codex Setup Checklist Skill

## Deutsch

### Zweck

Dieser Skill fuehrt Nutzer durch ein sicheres, wiederholbares Codex-Setup. Er deckt ab:

- globale Codex-Konfiguration
- projektbezogene Codex-Konfiguration
- `AGENTS.md`-Guidance
- Rules und Hooks
- Skill-Installation und Skill-Metadaten
- Konfliktbehandlung zwischen Anweisungsebenen
- optionale Migration von Claude-Strukturen nach Codex

Der Skill ist kein allgemeiner Coding-Workflow und kein Produktentwicklungs-Framework. Der Scope bleibt bewusst eng: Codex-Setup, Audit, Governance und Migration.

### Kernregeln

1. Erst lesen, dann schreiben.
2. Bestehende Dateien nicht ohne sichtbare Aenderungsabsicht ueberschreiben.
3. Merge/Patch statt Vollersetzung bevorzugen.
4. Niemals Secrets ausgeben, erzeugen, veraendern oder committen.
5. Sandbox, Approval oder Netzwerkzugriff nicht lockern, ausser der Nutzer fordert es explizit und das Risiko ist benannt.
6. `AGENTS.md` knapp halten. Aufgabenbezogene Prozesse gehoeren in Skills, Referenzen, `PLANS.md` oder `code_review.md`.
7. Bei Konflikten zwischen Anweisungsebenen den Konflikt melden und den sichersten nicht-destruktiven Pfad waehlen.

### Unterstuetzte Modi

Wenn kein Modus genannt wird, frage eine knappe Rueckfrage oder leite den sichersten Modus aus dem Kontext ab.

#### `audit`

Prueft ein bestehendes Codex-Setup.

Typischer Prompt:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Prueft unter anderem globale und projektbezogene Config, `AGENTS.md`, Rules, Hooks, Skills, `PLANS.md` und `code_review.md`. Wenn das Script vorhanden ist, nutze:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
```

#### `global`

Richtet persoenliche Codex-Defaults ein, typischerweise unter `~/.codex/`.

Typischer Prompt:

```text
Use the codex-setup-checklist skill to set up my global Codex defaults.
```

Erstellt oder aktualisiert:

- `~/.codex/config.toml`
- `~/.codex/AGENTS.md`
- `~/.codex/rules/default.rules`
- optional `~/.codex/hooks.json`

#### `project`

Installiert ein Best-Practice-Setup in einem Repository.

Typischer Prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Erstellt oder aktualisiert:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/rules/default.rules`
- `.codex/hooks.json`
- optional `.codex/hooks/*.py`
- optional `PLANS.md`
- optional `code_review.md`

#### `migrate-claude`

Migriert bestehende Claude-Code-Strukturen nach Codex.

Typischer Prompt:

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md and .claude/settings.json setup to Codex.
```

Liest Claude-Dateien, klassifiziert Inhalte und mappt sie auf `AGENTS.md`, `config.toml`, Rules, Hooks oder Skills. Originaldateien bleiben erhalten, solange der Nutzer nichts anderes verlangt.

#### `conflict-check`

Prueft, ob `AGENTS.md`, Skills, Framework-Dokumente, Hooks oder Rules einander widersprechen.

Typischer Prompt:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

Empfohlene Prioritaet:

1. Sicherheit, Secrets, Sandbox, Approval und destructive actions.
2. Explizite Nutzeranweisung fuer die aktuelle Aufgabe, sofern sicher.
3. Projekt-`AGENTS.md` vor globalem `AGENTS.md`.
4. Explizit aktivierte Skills fuer den konkreten Workflow.
5. Framework-Dokumente fuer Methode und Terminologie.
6. Rules und Hooks als technische Durchsetzung.

## English

### Purpose

This skill guides users through a safe, repeatable Codex setup. It covers:

- global Codex configuration
- project-level Codex configuration
- `AGENTS.md` guidance
- rules and hooks
- skill installation and metadata hygiene
- conflict handling across instruction layers
- optional migration from Claude-style configuration

This skill is not a generic coding workflow and not a product-development framework. Keep the scope tight: Codex setup, audit, governance, and migration.

### Core Rules

1. Inspect before writing.
2. Do not overwrite existing files without making the intended change visible.
3. Prefer merge/patch over full replacement.
4. Never print, create, modify, or commit secrets.
5. Do not loosen sandbox, approval, or network restrictions unless the user explicitly asks and the risk is stated.
6. Keep `AGENTS.md` concise. Put task-specific process into skills, references, `PLANS.md`, or `code_review.md`.
7. If instruction layers conflict, report the conflict and follow the safest non-destructive path.

### Supported Modes

When the user does not specify a mode, ask one concise question or infer the safest mode from context.

#### `audit`

Checks an existing Codex setup.

Typical prompt:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Inspect global and project config, `AGENTS.md`, rules, hooks, skills, `PLANS.md`, and `code_review.md`. When available, run:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
```

#### `global`

Sets up personal Codex defaults, usually below `~/.codex/`.

Typical prompt:

```text
Use the codex-setup-checklist skill to set up my global Codex defaults.
```

Create or update:

- `~/.codex/config.toml`
- `~/.codex/AGENTS.md`
- `~/.codex/rules/default.rules`
- optionally `~/.codex/hooks.json`

#### `project`

Installs a best-practice setup in a repository.

Typical prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Create or update:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/rules/default.rules`
- `.codex/hooks.json`
- optionally `.codex/hooks/*.py`
- optionally `PLANS.md`
- optionally `code_review.md`

#### `migrate-claude`

Migrates existing Claude Code structures to Codex.

Typical prompt:

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md and .claude/settings.json setup to Codex.
```

Read Claude files, classify content, and map it to `AGENTS.md`, `config.toml`, rules, hooks, or skills. Preserve original files unless the user explicitly asks to remove them.

#### `conflict-check`

Checks whether `AGENTS.md`, skills, framework documents, hooks, or rules conflict.

Typical prompt:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

Recommended precedence:

1. Safety, secrets, sandbox, approval, and destructive actions.
2. Explicit user instruction for the current task, when safe.
3. Project `AGENTS.md` before global `AGENTS.md`.
4. Explicitly invoked skills for the concrete workflow.
5. Framework documents for method and terminology.
6. Rules and hooks as technical enforcement.

## Output Format

For audits / Fuer Audits:

```markdown
# Codex Setup Audit

## Summary / Zusammenfassung

- Overall status / Gesamtstatus: Green / Amber / Red
- Main risk / Hauptrisiko:
- Recommended next action / Empfohlener naechster Schritt:

## Findings / Befunde

| Severity | Area | Finding | Recommendation |
|---|---|---|---|

## Proposed changes / Vorgeschlagene Aenderungen

## Commands to verify / Pruefbefehle

## Residual risks / Restrisiken
```

For setup generation / Fuer Setup-Erzeugung:

```markdown
# Proposed Codex Setup / Vorgeschlagenes Codex-Setup

## Files to create/update / Dateien zum Erstellen oder Aktualisieren

## Decisions made / Getroffene Entscheidungen

## Files / Dateien

## Verification / Verifikation
```

## Reference Files / Referenzdateien

Use these templates when generating files / Nutze diese Templates beim Erzeugen von Dateien:

- `references/templates/agents-global.md`
- `references/templates/agents-project.md`
- `references/templates/config-global.toml`
- `references/templates/config-project.toml`
- `references/templates/rules-default.rules`
- `references/templates/hooks.json`
- `references/templates/PLANS.md`
- `references/templates/code_review.md`

Use these scripts where useful / Nutze diese Scripts, wo sinnvoll:

- `scripts/audit_codex_setup.py`
- `scripts/detect_conflicts.py`
- `scripts/validate_rules.py`
- `scripts/migrate_claude_to_codex.py`
