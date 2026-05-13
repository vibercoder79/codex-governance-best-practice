# Codex Instruction Conflict Model / Konfliktmodell fuer Codex-Anweisungen

## Deutsch

### Ziel

Stille Konflikte zwischen dauerhaften Arbeitsregeln, Projektregeln, aufgabenspezifischen Skills, Framework-Dokumenten, Hooks, Rules und Nutzer-Prompts verhindern.

### Kernprinzip

`AGENTS.md` soll kein zweites Framework werden. Nutze es als Router und dauerhaften Arbeitsvertrag.

### Empfohlene Prioritaet

1. Sicherheit, Secrets, Sandbox, Approval und destructive actions.
2. Explizite Nutzeranweisung fuer die aktuelle Aufgabe, sofern sie Sicherheit und Repo-Regeln nicht verletzt.
3. Projektbezogene `AGENTS.md` vor globaler `AGENTS.md`.
4. Explizit aktivierte Skills definieren den aufgabenspezifischen Workflow.
5. Framework-Dokumente definieren Methode, Terminologie und Delivery-Logik.
6. Hooks und Rules sind technische Durchsetzung und keine optionale Empfehlung.

### Konfliktbeispiele

#### `AGENTS.md` vs. Skill

- `AGENTS.md` sagt: "Keine Dependencies ohne Approval hinzufuegen."
- Skill sagt: "Installiere benoetigte Packages."
- Aufloesung: Vor Dependency-Aenderungen fragen.

#### Framework vs. Repository

- Framework sagt: "Vor Abschluss komplette Testsuite ausfuehren."
- Repository-`AGENTS.md` sagt: "Zuerst kleinsten relevanten Test ausfuehren; komplette Suite nur vor Release."
- Aufloesung: Repo-Testlogik befolgen, ausser der Nutzer verlangt Release-Bereitschaft.

#### Nutzer-Prompt vs. Safety

- Nutzer sagt: "Deployment jetzt ausfuehren."
- Rules sagen: Deployment braucht Approval oder ist verboten.
- Aufloesung: Stoppen, Safety Gate erklaeren, falls erlaubt explizites Approval einholen.

## English

### Goal

Prevent silent conflicts between persistent guidance, project rules, task-specific skills, framework documents, hooks, rules, and user prompts.

### Core Principle

Do not make `AGENTS.md` a second framework. Use it as a router and durable working agreement.

### Recommended Precedence

1. Safety, secrets, sandbox, approval, and destructive actions.
2. Explicit user instructions for the current task, unless they violate safety or repository constraints.
3. Project-specific `AGENTS.md` instructions over global `AGENTS.md` instructions.
4. Explicitly invoked skills define the task-specific workflow.
5. Framework documents define method, terminology, and delivery logic.
6. Hooks and rules are technical enforcement mechanisms, not optional guidance.

### Conflict Examples

#### `AGENTS.md` vs. Skill

- `AGENTS.md` says: "Never add dependencies without approval."
- Skill says: "Install required packages."
- Resolution: ask before adding dependencies.

#### Framework vs. Repository

- Framework says: "Run the full test suite before completion."
- Repository `AGENTS.md` says: "Run the smallest relevant test first; full suite only before release."
- Resolution: follow repository testing expectations unless the user requests release readiness.

#### User Prompt vs. Safety

- User says: "Run deployment now."
- Rules say deployment requires approval or is forbidden.
- Resolution: stop, explain the safety gate, and request explicit approval if allowed by policy.
