# Global Codex Working Agreements / Globale Codex-Arbeitsvereinbarungen

## Deutsch

### Arbeitsweise

- Relevante Dateien vor Aenderungen lesen.
- Aenderungen klein, reviewbar und reversibel halten.
- Bestehende Dateien bevorzugt editieren statt komplett ersetzen.
- Annahmen explizit machen, wenn sie das Ergebnis beeinflussen.
- Fuer komplexe Arbeit einen kurzen Plan vor der Umsetzung vorschlagen.

### Sicherheit

- Niemals Secrets erzeugen, ausgeben, veraendern, committen oder offenlegen.
- `.env`, private Keys, Credentials, Produktions-Config oder Deployment-Secrets nur auf explizite Anweisung und mit klar benanntem Risiko aendern.
- Vor neuen Produktions-Dependencies fragen.
- Vor destruktiven Kommandos, Migrationen, Deployments, Force-Pushes oder Remote-State-Aenderungen fragen.

### Verifikation

- Zuerst den kleinsten relevanten Check ausfuehren.
- Bei fehlschlagenden Tests die Ursache untersuchen statt Tests abzuschwaechen.
- Vor Abschluss geaenderte Dateien, ausgefuehrte Checks und Restrisiken zusammenfassen.

### Kommunikation

- Knapp, technisch und direkt kommunizieren.
- Konkrete Diffs, Befehle und Begruendungen generischen Erklaerungen vorziehen.

## English

### Working Style

- Read relevant files before changing them.
- Keep changes small, reviewable, and reversible.
- Prefer editing existing files over replacing them wholesale.
- Make assumptions explicit when they affect the result.
- For complex work, propose a short plan before implementation.

### Safety

- Never create, print, modify, commit, or expose secrets.
- Do not modify `.env`, private keys, credentials, production config, or deployment secrets unless explicitly asked and the risk is clear.
- Ask before adding new production dependencies.
- Ask before running destructive commands, migrations, deployments, force-pushes, or commands that change remote state.

### Verification

- Run the smallest relevant check first.
- If tests fail, investigate root cause instead of weakening tests.
- Before finishing, summarize changed files, checks performed, and remaining risks.

### Communication

- Be concise, technical, and direct.
- Prefer concrete diffs, commands, and rationale over generic explanation.
