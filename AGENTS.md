# Repository Instructions / Repository-Anweisungen

## Deutsch

### Repository-Struktur

- `docs/` enthaelt Nutzer-Dokumentation in Deutsch und Englisch.
- `references/` enthaelt methodische Referenzen, Checklisten und Templates.
- `scripts/` enthaelt Pruef- und Migrationsskripte.
- `examples/` enthaelt Beispielausgaben.
- `.codex/` kann Codex-spezifische Config, Hooks, Rules und projektlokale Skills enthalten.
- Generierte Dateien nur bearbeiten, wenn die Aufgabe es ausdruecklich verlangt.

### Build, Test und Lint

Dieses Repository ist primaer ein Dokumentations-, Template- und Script-Repository.

Relevante Checks:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```

### Engineering-Regeln

- Betroffene Dateien vor Aenderungen lesen.
- Aenderungen eng am Nutzerwunsch halten.
- Bestehende Struktur bewahren, ausser ein Refactoring ist explizit gewuenscht.
- Keine neuen Frameworks oder Produktions-Dependencies ohne Zustimmung einfuehren.
- Tests oder Pruefskripte nicht abschwaechen, nur damit eine Aenderung durchlaeuft.
- Human-facing Markdown- und Template-Dateien zweisprachig pflegen: Deutsch und Englisch.

### Security und Safety

- Niemals Secrets, Tokens, Keys oder Credentials ausgeben, schreiben oder committen.
- Produktive Deployment-Konfiguration nur auf explizite Anweisung aendern.
- Vor Migrationen, Deployments, destruktiven Kommandos oder Remote-Aenderungen Rueckfrage bzw. Approval einholen.
- Netzwerkzugriff bewusst und begruendet nutzen, nicht als Default.

### Konfliktbehandlung

Dieses Repository kann `AGENTS.md`, Codex Skills, Framework-Dokumente, Rules, Hooks, MCP-Tools und Nutzeranweisungen kombinieren.

Prioritaet:

1. Sicherheit, Secrets, Sandbox, Approval und destructive actions.
2. Explizite Nutzeranweisung fuer die aktuelle Aufgabe, sofern sicher.
3. Repository-spezifische `AGENTS.md` vor globaler `AGENTS.md`.
4. Explizit aktivierte Skills fuer den konkreten Workflow.
5. Framework-Dokumente fuer Methode und Terminologie.
6. Hooks und Rules als technische Durchsetzung.

Bei Konflikten:

- Konflikt kurz benennen.
- Sichersten nicht-destruktiven Pfad waehlen.
- Nur nachfragen, wenn die Aufgabe ohne Entscheidung nicht sicher fortgesetzt werden kann.

### Done bedeutet

Vor Abschluss liefern:

- Zusammenfassung der geaenderten Dateien.
- Verifikation inklusive Tests, Lint, Build oder Begruendung, warum nicht ausgefuehrt.
- Restrisiken, Annahmen oder sinnvolle Follow-ups.

## English

### Repository Layout

- `docs/` contains user documentation in German and English.
- `references/` contains method references, checklists, and templates.
- `scripts/` contains audit and migration scripts.
- `examples/` contains sample outputs.
- `.codex/` may contain Codex-specific config, hooks, rules, and project-local skills.
- Do not edit generated files unless the task explicitly requires it.

### Build, Test, and Lint

This repository is primarily a documentation, template, and script repository.

Relevant checks:

```bash
python3 scripts/audit_codex_setup.py --scope project --repo .
python3 scripts/validate_rules.py references/templates/rules-default.rules
python3 scripts/detect_conflicts.py --repo .
```

### Engineering Rules

- Read affected files before editing.
- Keep changes scoped to the user request.
- Preserve existing structure unless refactoring is explicitly requested.
- Do not introduce new frameworks or production dependencies without approval.
- Do not weaken tests or validation scripts to make a change pass.
- Keep human-facing Markdown and template files bilingual: German and English.

### Security and Safety

- Never expose, write, or commit secrets, tokens, keys, or credentials.
- Do not modify production deployment config unless explicitly requested.
- Ask or request approval before migrations, deployments, destructive commands, or remote-state changes.
- Treat network access as deliberate and justified, not default.

### Conflict Handling

This repository may combine `AGENTS.md`, Codex skills, framework documents, rules, hooks, MCP tools, and user instructions.

Precedence:

1. Safety, secrets, sandbox, approval, and destructive actions.
2. Explicit user instruction for the current task, when safe.
3. Repository-specific `AGENTS.md` over global `AGENTS.md`.
4. Explicitly invoked skills for the concrete workflow.
5. Framework documents for method and terminology.
6. Hooks and rules as technical enforcement.

If instructions conflict:

- State the conflict briefly.
- Follow the safest non-destructive path.
- Ask only if the task cannot proceed safely without a decision.

### Done Means

Before finishing, provide:

- Summary of changed files.
- Verification performed, including tests, lint, build, or reason not run.
- Residual risks, assumptions, or useful follow-up items.
