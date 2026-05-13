# Code Review Checklist / Code-Review-Checkliste

## Deutsch

### Scope

- Passt die Aenderung zur angefragten Aufgabe?
- Bleiben nicht betroffene Dateien unberuehrt?
- Ist der Diff klein genug, um ihn sinnvoll zu reviewen?

### Korrektheit

- Sind Edge Cases beruecksichtigt?
- Wurden Tests ergaenzt oder aktualisiert, wo es sinnvoll ist?
- Beschreiben bestehende Tests weiterhin das gewuenschte Verhalten?

### Security

- Keine Secrets, Tokens oder Credentials hinzugefuegt.
- Keine unsichere Shell-Ausfuehrung oder unkontrollierter Netzwerkzugriff eingefuehrt.
- Keine Dependency ohne klare Begruendung hinzugefuegt.

### Wartbarkeit

- Passt die Aenderung zur bestehenden Architektur?
- Sind Namen und Grenzen klar?
- Ist die Komplexitaet gerechtfertigt?

### Verifikation

- Tests ausgefuehrt:
- Lint ausgefuehrt:
- Build ausgefuehrt:
- Manuelle Validierung:

### Restrisiken

Liste, was noch unsicher bleibt.

## English

### Scope

- Does the change match the requested task?
- Are unrelated files untouched?
- Is the diff small enough to review?

### Correctness

- Are edge cases handled?
- Are tests added or updated where useful?
- Do existing tests still express the intended behavior?

### Security

- No secrets, tokens, or credentials added.
- No unsafe shell execution or uncontrolled network access introduced.
- No dependency added without clear rationale.

### Maintainability

- Does the change fit the existing architecture?
- Are names and boundaries clear?
- Is complexity justified?

### Verification

- Tests run:
- Lint run:
- Build run:
- Manual validation:

### Residual risks

List anything that remains uncertain.
