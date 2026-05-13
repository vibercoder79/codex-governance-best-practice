# Codex Governance Best Practice

## Deutsch

Ein praxisorientiertes Starter-Repository fuer ein sauberes, auditierbares und konfliktarmes Codex-Setup.

Dieses Repository enthaelt einen wiederverwendbaren **Codex Skill** plus Templates, Rules, Hooks, Referenzen und Pruefskripte. Ziel ist ein klares Betriebsmodell: Welche Informationen gehoeren in `AGENTS.md`, welche in `config.toml`, welche in Skills, welche in Rules und welche in Hooks?

Die zentrale Idee: **`AGENTS.md` ist Router und Arbeitsvertrag, kein Handbuch fuer alles.** Wiederholbare Workflows gehoeren in Skills, technische Grenzen in Config/Rules/Hooks, laengere Methoden oder Frameworks in Referenzdokumente.

### Schnellstart

Global installieren:

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git
mkdir -p ~/.codex/skills
cp -R codex-governance-best-practice ~/.codex/skills/codex-setup-checklist
```

Projektlokal installieren:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

Skill in Codex nutzen:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Ausfuehrliche Anleitungen:

- Installation: [`docs/installation.de.md`](docs/installation.de.md)
- Nutzung und Modi: [`docs/usage.de.md`](docs/usage.de.md)

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
│   ├── usage.de.md
│   └── usage.en.md
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

Install globally:

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git
mkdir -p ~/.codex/skills
cp -R codex-governance-best-practice ~/.codex/skills/codex-setup-checklist
```

Install per project:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

Use the skill in Codex:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Detailed guides:

- Installation: [`docs/installation.en.md`](docs/installation.en.md)
- Usage and modes: [`docs/usage.en.md`](docs/usage.en.md)

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
│   ├── usage.de.md
│   └── usage.en.md
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
