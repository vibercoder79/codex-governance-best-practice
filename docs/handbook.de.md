# Handbuch: Codex-Governance verstehen

## Deutsch

Dieses Handbuch erklaert die Struktur hinter diesem Repository. Es soll Nutzern helfen zu verstehen, was der Skill `codex-setup-checklist` macht, warum die Dateien getrennt sind und wie ein gutes Codex-Projekt aufgebaut ist.

English summary: this handbook explains the Codex governance model, the role of each file, and how the checklist skill installs or audits that model. Full English version: [`handbook.en.md`](handbook.en.md).

## 1. Das Grundmodell

Codex arbeitet mit mehreren Anweisungsebenen. Ein gutes Setup trennt diese Ebenen bewusst:

![Codex Governance Map](diagrams/codex-governance-map.png)

| Ebene | Aufgabe | Typische Datei |
|---|---|---|
| Arbeitsvertrag | Dauerhafte Regeln fuer Zusammenarbeit | `AGENTS.md` |
| Runtime-Defaults | Sandbox, Approval, Reasoning, Web Search | `config.toml` |
| Kommando-Grenzen | Was erlaubt, verboten oder approval-pflichtig ist | `.rules` |
| Deterministische Checks | Pruefungen vor/nach Tool-Nutzung | Hooks |
| Wiederverwendbare Workflows | Audit, Setup, Migration, Konfliktpruefung | `SKILL.md` |
| Methode und Templates | Erklaerung, Beispiele, Zielzustaende | `references/`, `docs/` |

Die wichtigste Regel: `AGENTS.md` ist der Router, nicht das Handbuch fuer alles.

## 2. Welche Datei hat welche Aufgabe?

### `README.md`

Der Einstiegspunkt. Er erklaert kurz, wofuer das Repository da ist, wie man den Skill installiert und wo die Detaildokumentation liegt.

### `SKILL.md`

Die zentrale Skill-Datei. Codex liest zuerst Name und Beschreibung. Wenn der Nutzer den Skill aktiviert, liest Codex die volle Workflow-Anweisung.

### `AGENTS.md`

Die dauerhafte Arbeitsvereinbarung fuer dieses Repository. Sie beschreibt Struktur, Checks, Sicherheitsregeln, Konfliktlogik und Definition of Done.

### `PLANS.md`

Vorlage fuer laengere Arbeiten. Sie verhindert, dass mehrstufige Aufgaben unscharf werden.

### `code_review.md`

Review-Checkliste fuer Scope, Korrektheit, Security, Wartbarkeit und Verifikation.

### `docs/`

Nutzerorientierte Dokumentation: Installation, Nutzung, Handbuch und Diagramme.

### `references/`

Methodische Referenzen, Checklisten und Templates. Diese Dateien erklaeren die Logik hinter dem Setup und liefern wiederverwendbare Zielzustaende.

### `scripts/`

Pruef- und Migrationswerkzeuge. Sie machen Teile der Governance maschinell pruefbar.

## 3. Empfohlene Projektstruktur

Minimal:

```text
AGENTS.md
.codex/config.toml
PLANS.md
code_review.md
```

Produktiv:

```text
AGENTS.md
.codex/config.toml
.codex/rules/default.rules
PLANS.md
code_review.md
```

Erweitert:

```text
AGENTS.md
.codex/config.toml
.codex/rules/default.rules
.codex/hooks.json
.codex/hooks/pre_tool_use_guard.py
.codex/hooks/stop_summary_check.py
.codex/skills/<skill-name>/SKILL.md
PLANS.md
code_review.md
```

## 4. Wie der Skill genutzt wird

![Skill Modes Map](diagrams/skill-modes-map.png)

| Modus | Wann nutzen? | Ergebnis |
|---|---|---|
| `audit` | Bestehendes Setup pruefen | Befunde nach Schweregrad |
| `global` | Persoenliche Codex-Defaults einrichten | Dateien unter `~/.codex/` |
| `project` | Best-Practice-Setup in einem Repo installieren | `AGENTS.md`, `.codex/config.toml`, Rules, optional Hooks |
| `migrate-claude` | Claude-Strukturen uebertragen | Mapping von Claude-Dateien auf Codex-Dateien |
| `conflict-check` | Widersprueche erkennen | Konfliktliste und Prioritaetslogik |

## 5. Wie alles zusammenhaengt

Ein typischer Ablauf fuer ein bestehendes Repository:

1. `audit`: Ausgangszustand verstehen.
2. `project`: Best-Practice-Dateien installieren oder aktualisieren.
3. `conflict-check`: alte Regeln, Frameworks und Skills gegenpruefen.
4. `migrate-claude`: nur wenn Claude-Dateien vorhanden sind.
5. Validierung: Scripts laufen lassen und Audit erneut ausfuehren.

So wird aus einzelnen Dateien ein zusammenhaengendes Betriebsmodell.
