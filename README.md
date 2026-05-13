# Codex Governance Best Practice

Ein praxisorientiertes Starter-Repository für ein sauberes, auditierbares und konfliktarmes Codex-Setup.

Dieses Repository enthält einen **Codex Skill** plus Templates, Rules, Hooks und Prüfskripte. Ziel ist nicht, Codex mit möglichst vielen Regeln zu überladen. Ziel ist ein klares Betriebsmodell: Welche Informationen gehören in `AGENTS.md`, welche in `config.toml`, welche in Skills, welche in Rules und welche in Hooks?

Genau diese Trennung entscheidet später darüber, ob Codex zuverlässig arbeitet oder ob sich Prompt-Regeln, Framework-Dokumente, Skill-Anweisungen und technische Sicherheitsgrenzen gegenseitig widersprechen.

---

## 1. Warum dieses Repository existiert

Viele Codex-Setups scheitern nicht an fehlender Intelligenz des Modells, sondern an unsauberen Arbeitsanweisungen:

- zu lange `AGENTS.md`-Dateien
- vermischte Projektregeln und Workflow-Beschreibungen
- unklare Sicherheitsgrenzen
- zu offene Sandbox- oder Netzwerkfreigaben
- fehlende Regeln für gefährliche Kommandos
- nicht dokumentierte Konflikte zwischen Skills, Frameworks und Repo-Konventionen
- keine klare Definition, wann eine Aufgabe wirklich abgeschlossen ist

Dieses Repository stellt dafür eine belastbare Grundstruktur bereit.

Der Ansatz ist bewusst modular:

| Ebene | Aufgabe | Typische Datei |
|---|---|---|
| Dauerhafte Arbeitsregeln | Wie Codex in diesem Umfeld grundsätzlich arbeiten soll | `AGENTS.md` |
| Technische Konfiguration | Modell, Reasoning, Sandbox, Approval, Web Search, Features | `config.toml` |
| Harte Kommando-Governance | Was Codex ausführen darf, was Approval braucht, was verboten ist | `.rules` |
| Deterministische Prüfungen | Checks vor/nach Tool-Nutzung oder am Ende einer Aufgabe | Hooks |
| Wiederverwendbare Workflows | Schrittfolgen für Setup, Audit, Migration, Review etc. | `SKILL.md` |
| Methoden-/Framework-Wissen | Begriffe, Prozessmodelle, Delivery-Logik | `CONVENTIONS.md`, Framework-Dokumente |
| Längere Arbeitspläne | Mehrschrittige Umsetzung mit Statusführung | `PLANS.md` |
| Review-Standard | Einheitliche Qualitätssicherung vor Abschluss | `code_review.md` |

Die zentrale Idee: **`AGENTS.md` ist ein Router und Arbeitsvertrag, kein Handbuch für alles.**

---

## 2. Grundverständnis: Wie Codex Anweisungen verarbeitet

Codex kann verschiedene Anweisungsschichten gleichzeitig berücksichtigen. Genau deshalb braucht ein gutes Setup eine klare Ordnung.

### 2.1 `AGENTS.md`

`AGENTS.md` enthält dauerhafte Anweisungen für Codex. Diese Datei wird automatisch als Kontext berücksichtigt, wenn Codex in einem Repository arbeitet.

Typische Inhalte:

- Repo-Struktur
- Build-, Test- und Lint-Kommandos
- Coding-Konventionen
- Sicherheitsregeln
- Definition of Done
- Umgang mit Secrets und produktiven Systemen
- Konfliktlogik zwischen User Prompt, Skills, Rules, Hooks und Framework-Dokumenten

Nicht ideal für `AGENTS.md`:

- komplette Framework-Handbücher
- lange Prozessbeschreibungen
- grosse Checklisten
- komplette Architekturentscheidungen
- ausführliche Tutorials
- alles, was nur für einzelne Aufgaben relevant ist

Warum? Weil `AGENTS.md` automatisch geladen wird. Je grösser und unspezifischer die Datei wird, desto mehr Kontext verbraucht sie und desto höher wird das Risiko widersprüchlicher Regeln.

### 2.2 `config.toml`

`config.toml` steuert technische Codex-Defaults.

Typische Inhalte:

- Modellwahl
- Reasoning Effort
- Sandbox-Modus
- Approval Policy
- Web Search Policy
- erlaubte schreibbare Pfade
- Shell-Environment-Policy
- Feature Flags, z. B. Hooks oder Multi-Agent-Funktionen

Es gibt zwei wichtige Orte:

```text
~/.codex/config.toml       # persönliche, globale Defaults
.codex/config.toml         # projektbezogene Defaults
```

Die globale Config beschreibt deine persönliche Arbeitsweise. Die Projekt-Config beschreibt, was in einem konkreten Repo gelten soll.

### 2.3 Rules

Rules sind harte Entscheidungsregeln für Kommandos. Sie beantworten Fragen wie:

- Darf Codex `rm -rf` ausführen?
- Muss `npm install` vorher bestätigt werden?
- Ist `git push --force` verboten?
- Darf ein Deployment-Kommando laufen?

Rules sind besonders wichtig, weil reine Prompt-Regeln weich sind. Eine Rule ist expliziter und prüfbarer.

### 2.4 Hooks

Hooks sind deterministische Prüfungen an bestimmten Punkten im Codex-Lebenszyklus.

Beispiele:

- vor einem Shell-Kommando prüfen, ob es gefährlich ist
- nach einer Änderung automatisch Linting oder Tests anstossen
- am Ende prüfen, ob eine Zusammenfassung und Verifikation vorhanden sind

Hooks sind mächtig, sollten aber bewusst eingesetzt werden. Zu viele Hooks machen ein Setup schwerfällig. Zu wenige Hooks lassen Governance nur im Prompt stehen.

### 2.5 Skills

Skills sind wiederverwendbare Workflows. Ein Skill besteht mindestens aus einer `SKILL.md`. Zusätzlich kann er Referenzmaterial, Templates und Skripte enthalten.

Ein Skill eignet sich für Aufgaben wie:

- Codex-Setup auditieren
- Claude-Setup nach Codex migrieren
- AGENTS.md erzeugen
- Rules validieren
- Konflikte zwischen Instruction-Layern erkennen
- ein Projekt nach einem definierten Prozess aufsetzen

Dieses Repository ist selbst als Skill gedacht: **`codex-setup-checklist`**.

### 2.6 Framework-Dokumente

Framework-Dokumente beschreiben Methode, Sprache, Phasen und Lieferlogik. Sie sollten nicht direkt mit Sicherheitsregeln oder Repo-Konventionen vermischt werden.

Gute Trennung:

```text
AGENTS.md        → dauerhafte Leitplanken
SKILL.md         → wiederverwendbarer Workflow
Rules/Hooks      → technische Durchsetzung
Framework Docs   → Methode und Terminologie
```

---

## 3. Was dieses Repository liefert

Dieses Repository enthält:

```text
.
├── README.md
├── SKILL.md
├── AGENTS.md
├── PLANS.md
├── code_review.md
├── .codex/
│   ├── config.toml
│   ├── rules/
│   │   └── default.rules
│   └── skills/
├── references/
│   ├── checklist.yaml
│   ├── conflict-model.md
│   ├── openai-best-practices.md
│   └── templates/
│       ├── agents-global.md
│       ├── agents-project.md
│       ├── config-global.toml
│       ├── config-project.toml
│       ├── hooks.json
│       ├── rules-default.rules
│       ├── PLANS.md
│       └── code_review.md
├── scripts/
│   ├── audit_codex_setup.py
│   ├── detect_conflicts.py
│   ├── migrate_claude_to_codex.py
│   └── validate_rules.py
├── examples/
│   └── audit-report.md
└── .github/
    └── workflows/
        └── validate.yml
```

---

## 4. Die wichtigsten Dateien erklärt

### `SKILL.md`

Die zentrale Skill-Datei.

Sie enthält:

- Name und Beschreibung des Skills
- Einsatzbereich
- unterstützte Modi
- Arbeitsregeln
- Audit-Logik
- Migrationslogik
- Konfliktprüfung
- Output-Format

Codex nutzt die Metadaten am Anfang der Datei, um zu entscheiden, wann dieser Skill relevant ist.

Typische Prompts:

```text
Use the codex-setup-checklist skill to audit this repository.
```

```text
Use the codex-setup-checklist skill to create a safe Codex setup for this project.
```

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md setup to Codex.
```

### `AGENTS.md`

Die Repo-spezifischen Arbeitsanweisungen für Codex.

Diese Datei ist bewusst nicht als komplettes Handbuch gedacht. Sie definiert:

- Arbeitsweise
- Sicherheitsgrenzen
- Setup-Konventionen
- Definition of Done
- Konfliktbehandlung
- Umgang mit Skills und Templates

Faustregel: Wenn eine Anweisung immer gelten soll, gehört sie eher in `AGENTS.md`. Wenn sie nur für einen bestimmten Workflow gilt, gehört sie eher in einen Skill.

### `.codex/config.toml`

Projektbezogene Codex-Konfiguration.

Diese Datei setzt sichere Defaults für dieses Repository, unter anderem:

- `approval_policy = "on-request"`
- `sandbox_mode = "workspace-write"`
- `network_access = false`
- `model_reasoning_effort = "high"`
- `plan_mode_reasoning_effort = "high"`
- `project_doc_max_bytes = 65536`
- aktivierte Feature Flags, falls benötigt

Damit wird Codex arbeitsfähig, ohne zu viele Rechte zu bekommen.

### `.codex/rules/default.rules`

Projektbezogene Rules für Kommando-Governance.

Die Datei enthält Beispiele für:

- blockierte destructive commands
- approval-pflichtige Dependency-Änderungen
- verbotene Force-Pushes
- vorsichtige Behandlung von Deployment-Kommandos

Diese Rules sind Templates. Sie sollten je Projekt angepasst werden.

### `references/checklist.yaml`

Die maschinenlesbare Prüfliste für den Skill.

Sie beschreibt, welche Punkte bei einem Codex-Setup geprüft werden sollen:

- globale Config
- Projekt-Config
- AGENTS-Dateien
- Sandbox
- Approval
- Network Policy
- Web Search
- Rules
- Hooks
- Skills
- Konfliktmodell
- Review-Prozess

Diese Datei ist die Grundlage für Audit-Logik und spätere Erweiterungen.

### `references/conflict-model.md`

Das Konfliktmodell.

Es beantwortet:

- Was passiert, wenn User Prompt und `AGENTS.md` kollidieren?
- Was passiert, wenn ein Skill etwas anderes sagt als das Repo?
- Wann haben Rules oder Hooks Vorrang?
- Wann soll Codex stoppen und den Konflikt melden?

Empfohlene Priorität:

1. Sicherheit, Secrets, Sandbox, Approval, destructive actions
2. explizite User-Anweisung für die aktuelle Aufgabe, sofern sicher
3. repo-spezifische `AGENTS.md` vor globaler `AGENTS.md`
4. explizit aktivierter Skill für den konkreten Workflow
5. Framework-Dokumente für Methode und Terminologie
6. Rules und Hooks als technische Durchsetzung

### `references/openai-best-practices.md`

Zusammenfassung der wichtigsten Codex-Best-Practice-Prinzipien, auf die dieses Repository ausgerichtet ist.

Die Datei ist bewusst kompakt gehalten. Sie soll keine OpenAI-Dokumentation ersetzen, sondern die Designentscheidungen dieses Repos erklären.

### `references/templates/`

Vorlagen für typische Zielzustände.

Enthalten sind:

| Datei | Zweck |
|---|---|
| `agents-global.md` | Vorlage für `~/.codex/AGENTS.md` |
| `agents-project.md` | Vorlage für ein Projekt-`AGENTS.md` |
| `config-global.toml` | Vorlage für `~/.codex/config.toml` |
| `config-project.toml` | Vorlage für `.codex/config.toml` |
| `rules-default.rules` | Vorlage für `.codex/rules/default.rules` |
| `hooks.json` | Beispielhafte Hook-Konfiguration |
| `PLANS.md` | Vorlage für längere Arbeitspläne |
| `code_review.md` | Vorlage für Review-Kriterien |

### `scripts/audit_codex_setup.py`

Audit-Script für ein bestehendes Codex-Setup.

Beispiel:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
```

Oder für globale Prüfung:

```bash
python3 scripts/audit_codex_setup.py --scope global --repo .
```

Das Script gibt Findings nach Schweregrad aus:

- `critical`
- `high`
- `medium`
- `low`
- `info`

### `scripts/detect_conflicts.py`

Prüft typische Konflikte zwischen:

- `AGENTS.md`
- `AGENTS.override.md`
- `.codex/config.toml`
- Rules
- Hooks
- Skills
- `PLANS.md`
- `code_review.md`

Beispiel:

```bash
python3 scripts/detect_conflicts.py --repo .
```

### `scripts/validate_rules.py`

Prüft Rule-Dateien auf einfache Struktur- und Plausibilitätsprobleme.

Beispiel:

```bash
python3 scripts/validate_rules.py .codex/rules/default.rules
```

Oder für das Template:

```bash
python3 scripts/validate_rules.py references/templates/rules-default.rules
```

### `scripts/migrate_claude_to_codex.py`

Hilft bei der Migration von Claude-Code-Strukturen nach Codex.

Typische Quellen:

- `CLAUDE.md`
- `.claude/settings.json`
- `.claudeignore`
- Claude Hooks
- Claude Commands

Die Migration folgt dieser Logik:

| Claude-Element | Codex-Ziel |
|---|---|
| `CLAUDE.md` | `AGENTS.md` oder Skill-Referenz |
| `.claude/settings.json` | `.codex/config.toml` |
| `.claudeignore` | Sandbox, Rules, `.gitignore`, Dokumentation |
| Claude Hooks | Codex Hooks |
| Claude Commands | Skills oder Scripts |

### `PLANS.md`

Arbeitsplan-Datei für längere Aufgaben.

Nützlich, wenn Codex nicht nur eine kleine Änderung macht, sondern mehrere Schritte koordinieren muss.

### `code_review.md`

Review-Standard für Änderungen.

Nützlich für:

- PR-Vorbereitung
- Abschlusskontrolle
- Security Review
- Testabdeckung
- Dokumentationsprüfung

### `.github/workflows/validate.yml`

GitHub Actions Workflow zur Basisvalidierung.

Er führt aus:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```

---

## 5. Installation als Codex Skill

### Variante A: Globaler persönlicher Skill

Geeignet, wenn du den Skill in mehreren Repositories nutzen willst.

```bash
mkdir -p ~/.codex/skills
cp -R codex-governance-best-practice ~/.codex/skills/codex-setup-checklist
```

Danach kannst du Codex in jedem Repo bitten:

```text
Use the codex-setup-checklist skill to audit this repo.
```

### Variante B: Projektlokaler Skill

Geeignet, wenn der Skill nur in einem bestimmten Repo verfügbar sein soll.

```bash
mkdir -p .codex/skills
cp -R codex-governance-best-practice .codex/skills/codex-setup-checklist
```

### Variante C: Als Vorlage kopieren

Geeignet, wenn du dieses Repository als Blueprint für ein eigenes internes Codex-Governance-Repo nutzen willst.

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git
cd codex-governance-best-practice
```

Dann Templates anpassen und in Ziel-Repos übernehmen.

---

## 6. Typische Nutzung

### Setup eines neuen Repositories prüfen

```text
Use the codex-setup-checklist skill to audit this repository and recommend a safe project-level Codex setup.
```

### Projekt-Setup erzeugen

```text
Use the codex-setup-checklist skill to create AGENTS.md, .codex/config.toml, .codex/rules/default.rules, PLANS.md, and code_review.md for this repo.
```

### Claude-Setup migrieren

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md and .claude/settings.json setup to Codex.
```

### Konflikte prüfen

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

---

## 7. Empfohlener Zielzustand für produktive Repos

Für ein normales Engineering-Repo würde ich mindestens diese Dateien anlegen:

```text
AGENTS.md
.codex/config.toml
.codex/rules/default.rules
PLANS.md
code_review.md
```

Optional, wenn du deterministische Prüfungen brauchst:

```text
.codex/hooks.json
.codex/hooks/pre_tool_use_guard.py
.codex/hooks/stop_summary_check.py
```

Optional, wenn du eigene wiederholbare Workflows hast:

```text
.codex/skills/<skill-name>/SKILL.md
```

---

## 8. Empfohlene Default-Policy

Für die meisten Repositories ist diese Policy ein guter Start:

```toml
approval_policy = "on-request"
sandbox_mode = "workspace-write"
model_reasoning_effort = "high"
plan_mode_reasoning_effort = "high"
model_reasoning_summary = "auto"
model_verbosity = "medium"
web_search = "cached"
project_doc_max_bytes = 65536

[sandbox_workspace_write]
network_access = false
writable_roots = []
exclude_tmpdir_env_var = true
exclude_slash_tmp = true
```

Interpretation:

- Codex darf im Workspace arbeiten.
- Codex bekommt nicht pauschal Netzwerkzugriff.
- Riskante Aktionen brauchen Approval.
- Reasoning ist hoch genug für anspruchsvolle Engineering-Arbeit.
- Projektanweisungen dürfen etwas grösser sein als der sehr knappe Default.

---

## 9. Konfliktlogik: Was gilt wann?

Dieses Repository empfiehlt folgende Grundregel:

```text
Sicherheit schlägt Workflow.
Repo-Regeln schlagen globale Präferenzen.
Explizit aktivierte Skills steuern den konkreten Ablauf.
Framework-Dokumente liefern Methode, aber keine Sicherheitsausnahmen.
Rules und Hooks sind technische Durchsetzung, nicht Dekoration.
```

Wenn Codex einen Konflikt erkennt, soll es nicht stillschweigend „irgendwie“ entscheiden.

Erwartetes Verhalten:

1. Konflikt kurz benennen.
2. Sichersten nicht-destruktiven Pfad wählen.
3. Keine Secrets ausgeben oder verändern.
4. Keine produktiven Änderungen ohne Approval.
5. Nur dann nachfragen, wenn die Aufgabe ohne Entscheidung nicht sicher fortgesetzt werden kann.

---

## 10. Anti-Patterns

Diese Muster sollte man vermeiden:

### 10.1 Riesige `AGENTS.md`

Problem: Codex lädt die Datei automatisch. Eine zu grosse Datei verbraucht Kontext und erzeugt Widersprüche.

Besser: `AGENTS.md` kurz halten, Workflows in Skills auslagern.

### 10.2 Skills als Regel-Ersatz verwenden

Problem: Skills sind Workflows, keine harte Security-Grenze.

Besser: Security-Grenzen in Rules, Hooks und Config abbilden.

### 10.3 Netzwerkzugriff pauschal aktivieren

Problem: Erhöht Risiko für Datenabfluss, Prompt Injection und unkontrollierte externe Abhängigkeiten.

Besser: Standardmässig deaktivieren und nur gezielt freigeben.

### 10.4 Framework in `AGENTS.md` kopieren

Problem: Methode, Sicherheitsregeln und Repo-Konventionen vermischen sich.

Besser: Framework als Skill-Familie oder Referenzdokument führen.

### 10.5 Keine Definition of Done

Problem: Codex beendet Aufgaben ohne Verifikation.

Besser: In `AGENTS.md` klar definieren, was am Ende berichtet werden muss:

- geänderte Dateien
- Tests/Lint/Build
- nicht geprüfte Punkte
- Risiken
- nächste sinnvolle Schritte

---

## 11. Validierung lokal ausführen

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```

Wenn alle Checks sauber laufen, ist das Scaffold technisch konsistent.

---

## 12. Entwicklungsstand

Aktueller Status: **v0.1 Scaffold**

Dieses Repository ist ein belastbarer Startpunkt, aber keine endgültige Organisationsrichtlinie. Vor produktiver Nutzung sollten die Templates an das jeweilige Team, die Toolchain, die Security-Vorgaben und die Deployment-Prozesse angepasst werden.

---

## 13. Kurzfassung

Dieses Repository hilft dabei, Codex so aufzusetzen, dass es nicht nur „funktioniert“, sondern verlässlich, sicher und nachvollziehbar arbeitet.

Die wichtigste Regel bleibt schlicht:

> `AGENTS.md` gibt die Leitplanken.  
> Skills führen Workflows aus.  
> Rules und Hooks setzen Grenzen durch.  
> Framework-Dokumente erklären die Methode.  
> `config.toml` definiert den technischen Betriebsmodus.

So bleibt Codex leistungsfähig, ohne unkontrolliert zu werden.
