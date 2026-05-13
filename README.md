# Codex Governance Best Practice

## Deutsch

Ein praxisorientiertes Starter-Repository fuer ein sauberes, auditierbares und konfliktarmes Codex-Setup.

Dieses Repository enthaelt einen wiederverwendbaren **Codex Skill** plus Templates, Rules, Hooks, Referenzen und Pruefskripte. Ziel ist ein klares Betriebsmodell: Welche Informationen gehoeren in `AGENTS.md`, welche in `config.toml`, welche in Skills, welche in Rules und welche in Hooks?

Die zentrale Idee: **`AGENTS.md` ist Router und Arbeitsvertrag, kein Handbuch fuer alles.** Wiederholbare Workflows gehoeren in Skills, technische Grenzen in Config/Rules/Hooks, laengere Methoden oder Frameworks in Referenzdokumente.

### Schnellstart

Global installieren geht auf zwei Arten. Details und Fehlerbehebung stehen im Installationshandbuch: [`docs/installation.de.md`](docs/installation.de.md).

**Variante 1: in einer Terminal-Session ausfuehren**

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

**Variante 2: Codex diesen Prompt geben**

```text
Installiere den Skill https://github.com/vibercoder79/codex-governance-best-practice global als ~/.codex/skills/codex-setup-checklist und pruefe danach, ob SKILL.md vorhanden ist.
```

Hinweis: Wenn Codex die globale Installation ausfuehrt, schreibt es nach `~/.codex/skills` und fragt je nach Sandbox/Approval nach Freigabe.

Projektlokal installieren:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

Projekt-Setup mit dem Skill installieren:

1. Oeffne Codex im Ziel-Repository.
2. Stelle sicher, dass der Skill global oder projektlokal installiert ist.
3. Gib Codex diesen Prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Das erzeugt oder aktualisiert typischerweise `AGENTS.md`, `.codex/config.toml`, `.codex/rules/default.rules`, optional Hooks, `PLANS.md` und `code_review.md`.

Bestehendes Setup auditieren:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Ausfuehrliche Anleitungen:

- Installation: [`docs/installation.de.md`](docs/installation.de.md)
- Nutzung und Modi: [`docs/usage.de.md`](docs/usage.de.md)
- Handbuch: [`docs/handbook.de.md`](docs/handbook.de.md)

### Wofuer der Skill gedacht ist

| Modus | Zweck | Typischer Prompt |
|---|---|---|
| `audit` | Bestehendes Codex-Setup pruefen | `Use the codex-setup-checklist skill to audit this repository.` |
| `global` | Persoenliche Codex-Defaults einrichten | `Use the codex-setup-checklist skill to set up my global Codex defaults.` |
| `project` | Best-Practice-Setup in einem Repo installieren | `Use the codex-setup-checklist skill to create a safe project-level Codex setup.` |
| `migrate-claude` | `CLAUDE.md` und Claude-Settings nach Codex uebertragen | `Use the codex-setup-checklist skill to migrate my Claude setup to Codex.` |
| `conflict-check` | Konflikte zwischen AGENTS, Skills, Rules, Hooks und Frameworks finden | `Use the codex-setup-checklist skill to check instruction conflicts.` |

### Was dieses Repository liefert

```text
.
├── README.md
├── SKILL.md
├── AGENTS.md
├── PLANS.md
├── code_review.md
├── docs/
│   ├── installation.de.md
│   ├── installation.en.md
│   ├── handbook.de.md
│   ├── handbook.en.md
│   ├── usage.de.md
│   ├── usage.en.md
│   └── diagrams/
├── references/
│   ├── checklist.yaml
│   ├── conflict-model.md
│   ├── openai-best-practices.md
│   └── templates/
├── scripts/
│   ├── audit_codex_setup.py
│   ├── detect_conflicts.py
│   ├── migrate_claude_to_codex.py
│   └── validate_rules.py
└── examples/
    └── audit-report.md
```

### Empfohlener Zielzustand fuer produktive Repositories

```text
AGENTS.md
.codex/config.toml
.codex/rules/default.rules
PLANS.md
code_review.md
```

Optional:

```text
.codex/hooks.json
.codex/hooks/pre_tool_use_guard.py
.codex/hooks/stop_summary_check.py
.codex/skills/<skill-name>/SKILL.md
```

### Validierung

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```

## English

A practical starter repository for a clean, auditable, low-conflict Codex setup.

This repository contains a reusable **Codex skill** plus templates, rules, hooks, references, and validation scripts. The goal is a clear operating model: what belongs in `AGENTS.md`, what belongs in `config.toml`, what belongs in skills, and what belongs in rules or hooks?

The core idea: **`AGENTS.md` is a router and working agreement, not a handbook for everything.** Repeatable workflows belong in skills, technical boundaries belong in config/rules/hooks, and longer methods or frameworks belong in reference documents.

### Quick Start

There are two ways to install globally. Details and troubleshooting are in the installation handbook: [`docs/installation.en.md`](docs/installation.en.md).

**Option 1: run this in a terminal session**

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

**Option 2: give Codex this prompt**

```text
Install the skill https://github.com/vibercoder79/codex-governance-best-practice globally as ~/.codex/skills/codex-setup-checklist and then verify that SKILL.md exists.
```

Note: If Codex performs the global installation, it writes to `~/.codex/skills` and may request permission depending on sandbox/approval settings.

Install per project:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

Install the project setup with the skill:

1. Open Codex in the target repository.
2. Make sure the skill is installed globally or project-locally.
3. Give Codex this prompt:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

This typically creates or updates `AGENTS.md`, `.codex/config.toml`, `.codex/rules/default.rules`, optional hooks, `PLANS.md`, and `code_review.md`.

Audit an existing setup:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Detailed guides:

- Installation: [`docs/installation.en.md`](docs/installation.en.md)
- Usage and modes: [`docs/usage.en.md`](docs/usage.en.md)
- Handbook: [`docs/handbook.en.md`](docs/handbook.en.md)

### What the Skill Is For

| Mode | Purpose | Typical prompt |
|---|---|---|
| `audit` | Check an existing Codex setup | `Use the codex-setup-checklist skill to audit this repository.` |
| `global` | Set up personal Codex defaults | `Use the codex-setup-checklist skill to set up my global Codex defaults.` |
| `project` | Install a best-practice setup in a repository | `Use the codex-setup-checklist skill to create a safe project-level Codex setup.` |
| `migrate-claude` | Migrate `CLAUDE.md` and Claude settings to Codex | `Use the codex-setup-checklist skill to migrate my Claude setup to Codex.` |
| `conflict-check` | Detect conflicts between AGENTS, skills, rules, hooks, and frameworks | `Use the codex-setup-checklist skill to check instruction conflicts.` |

### What This Repository Provides

```text
.
├── README.md
├── SKILL.md
├── AGENTS.md
├── PLANS.md
├── code_review.md
├── docs/
│   ├── installation.de.md
│   ├── installation.en.md
│   ├── handbook.de.md
│   ├── handbook.en.md
│   ├── usage.de.md
│   ├── usage.en.md
│   └── diagrams/
├── references/
│   ├── checklist.yaml
│   ├── conflict-model.md
│   ├── openai-best-practices.md
│   └── templates/
├── scripts/
│   ├── audit_codex_setup.py
│   ├── detect_conflicts.py
│   ├── migrate_claude_to_codex.py
│   └── validate_rules.py
└── examples/
    └── audit-report.md
```

### Recommended Target State for Production Repositories

```text
AGENTS.md
.codex/config.toml
.codex/rules/default.rules
PLANS.md
code_review.md
```

Optional:

```text
.codex/hooks.json
.codex/hooks/pre_tool_use_guard.py
.codex/hooks/stop_summary_check.py
.codex/skills/<skill-name>/SKILL.md
```

### Validation

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```
