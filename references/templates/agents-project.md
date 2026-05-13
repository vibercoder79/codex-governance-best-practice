# Repository Instructions / Repository-Anweisungen

## Deutsch

### Repository-Struktur

- `src/` enthaelt Anwendungscode.
- `tests/` enthaelt automatisierte Tests.
- `docs/` enthaelt Architektur-, Produkt- und Betriebsdokumentation.
- `.codex/` enthaelt Codex-spezifische Konfiguration, Hooks, Rules und optionale projektlokale Skills.
- Generierte Dateien nur bearbeiten, wenn die Aufgabe es ausdruecklich verlangt.

Passe diesen Abschnitt an die echte Repository-Struktur an, bevor du dich darauf verlaesst.

### Build, Test und Lint

Ersetze diese Befehle durch die tatsaechlichen Projektbefehle:

```bash
npm install
npm run lint
npm test
npm run build
```

### Engineering-Regeln

- Betroffene Dateien vor Aenderungen lesen.
- Aenderungen eng am Nutzerwunsch halten.
- Bestehende Architektur bewahren, ausser die Aufgabe verlangt Refactoring.
- Keine neuen Frameworks ohne Zustimmung einfuehren.
- Keine Produktions-Dependencies ohne Zustimmung hinzufuegen.
- Tests nicht abschwaechen, nur damit eine Aenderung durchlaeuft.

### Sicherheit

- Niemals Secrets, Tokens, Keys oder Credentials offenlegen.
- Produktive Deployment-Konfiguration nur auf explizite Anweisung aendern.
- Vor Migrationen, Deployments, destruktiven Kommandos oder Remote-State-Aenderungen fragen.
- Netzwerkzugriff bewusst behandeln, nicht als Default.

### Konfliktbehandlung

Prioritaet:

1. Sicherheit, Secrets, Sandbox, Approval und destructive actions.
2. Explizite Nutzeranweisung fuer die aktuelle Aufgabe, sofern sicher.
3. Repository-spezifische `AGENTS.md` vor globaler `AGENTS.md`.
4. Explizit aktivierte Skills fuer den konkreten Workflow.
5. Framework-Dokumente fuer Methode und Terminologie.
6. Hooks und Rules als technische Durchsetzung.

### Done bedeutet

Vor Abschluss liefern:

- Zusammenfassung der geaenderten Dateien.
- Verifikation inklusive Tests, Lint, Build oder Begruendung, warum nicht ausgefuehrt.
- Restrisiken, Annahmen oder Follow-ups.

## English

### Repository Layout

- `src/` contains application code.
- `tests/` contains automated tests.
- `docs/` contains architecture, product, and operational documentation.
- `.codex/` contains Codex-specific configuration, hooks, rules, and optional project-local skills.
- Do not edit generated files unless the task explicitly requires it.

Update this section to match the real repository structure before relying on it.

### Build, Test, and Lint

Replace these commands with the actual project commands:

```bash
npm install
npm run lint
npm test
npm run build
```

### Engineering Rules

- Read affected files before editing.
- Keep changes scoped to the user request.
- Preserve existing architecture unless the task explicitly asks for refactoring.
- Do not introduce new frameworks without approval.
- Do not add production dependencies without approval.
- Do not weaken tests to make a change pass.

### Security

- Never expose secrets, tokens, keys, or credentials.
- Do not modify production deployment config unless explicitly requested.
- Ask before running migrations, deployment commands, destructive commands, or commands that modify remote state.
- Treat network access as deliberate, not default.

### Conflict Handling

Precedence:

1. Safety, secrets, sandbox, approval, and destructive actions.
2. Explicit user instructions for the current task, when safe.
3. Repository-specific `AGENTS.md` instructions over global `AGENTS.md` instructions.
4. Explicitly invoked skills for the concrete workflow.
5. Framework documents for method and terminology.
6. Hooks and rules as technical enforcement.

### Done Means

Before finishing, provide:

- Summary of changed files.
- Verification performed, including tests, lint, build, or reason not run.
- Residual risks, assumptions, or follow-up items.
