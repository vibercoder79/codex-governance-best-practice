# OpenAI Codex Best-Practice Notes / OpenAI-Codex-Best-Practice-Notizen

Diese Datei fasst die praktischen Annahmen zusammen, auf denen der Skill basiert. Pruefe policy-sensible Aenderungen immer gegen die aktuelle OpenAI-Codex-Dokumentation.

This file captures the practical assumptions used by the skill. Verify policy-sensitive changes against the current OpenAI Codex documentation.

## AGENTS.md

Deutsch:

- Codex liest `AGENTS.md`, bevor die Arbeit beginnt.
- Globale Guidance liegt normalerweise unter `~/.codex`.
- Projekt-Guidance wird vom Projekt-Root bis zum aktuellen Arbeitsverzeichnis beruecksichtigt.
- Dateien naeher am aktuellen Verzeichnis haben hoehere Relevanz, weil sie spaeter im kombinierten Prompt erscheinen.
- `AGENTS.override.md` wird auf derselben Ebene vor `AGENTS.md` gelesen.
- Die Instruction-Groesse wird durch `project_doc_max_bytes` begrenzt.
- `AGENTS.md` sollte praktisch und knapp bleiben.

English:

- Codex reads `AGENTS.md` before work starts.
- Global guidance usually lives under `~/.codex`.
- Project-level guidance is discovered from the project root down to the current working directory.
- Files closer to the current directory have higher relevance because they appear later in the combined prompt.
- `AGENTS.override.md` is read before `AGENTS.md` at the same level.
- Instruction loading is capped by `project_doc_max_bytes`.
- Keep `AGENTS.md` practical and concise.

## Config

Deutsch:

- User-Config liegt in `~/.codex/config.toml`.
- Projekt-Config liegt in `.codex/config.toml`.
- Projektbezogene `.codex/`-Layer laden nur, wenn das Projekt als vertrauenswuerdig gilt.
- CLI-Flags und explizite Config-Overrides haben Vorrang vor Config-Dateien.
- Projekt-Config hat Vorrang vor User-Config.

English:

- User config lives in `~/.codex/config.toml`.
- Project config lives in `.codex/config.toml`.
- Project-scoped `.codex/` layers only load when the project is trusted.
- CLI flags and explicit config overrides win over config files.
- Project config has higher precedence than user config.

## Skills

Deutsch:

- Ein Skill ist ein Ordner mit einer Pflichtdatei `SKILL.md` und optionalen Ordnern `scripts/`, `references/` und `assets/`.
- `SKILL.md` braucht `name` und `description` im Frontmatter.
- Codex sieht zunaechst Skill-Name, Beschreibung und Pfad; volle Anweisungen werden erst bei Aktivierung geladen.
- Skill-Beschreibungen sollten Triggerbegriffe und Grenzen frueh nennen.

English:

- A skill is a directory with a required `SKILL.md` file and optional `scripts/`, `references/`, and `assets/` folders.
- `SKILL.md` must include `name` and `description` metadata.
- Codex initially sees the skill name, description, and path; full instructions are loaded only when Codex activates the skill.
- Skill descriptions should front-load trigger terms and boundaries.

## Rules and Hooks / Rules und Hooks

Deutsch:

- Rules liegen in `rules/*.rules` neben einer aktiven Config-Ebene.
- Rules steuern, welche Kommandos Codex ausserhalb der Sandbox ausfuehren darf.
- Hooks sind sinnvoll fuer deterministische Checks, Prompt-Scanning und Stop-Time-Validierung.
- Verwende pro Config-Ebene moeglichst nur eine Hook-Repraesentation.

English:

- Rules live in `rules/*.rules` next to an active config layer.
- Rules control which commands Codex can run outside the sandbox.
- Hooks are useful for deterministic checks, prompt scanning, and stop-time validation.
- Prefer one hook representation per config layer.

## Recommended Setup Stance / Empfohlene Setup-Haltung

Deutsch:

- Konservativer Default: `approval_policy = "on-request"` und `sandbox_mode = "workspace-write"`.
- Shell-Netzwerkzugriff fuer lokale Arbeit standardmaessig deaktivieren.
- Web Search bewusst nutzen statt breiten Shell-Netzwerkzugriff zu erlauben.
- Secrets aus der geerbten Shell-Umgebung ausschliessen.
- Framework-Dokumente als Methodenreferenzen behandeln, nicht als hoehere Anweisungsebene.

English:

- Conservative default: `approval_policy = "on-request"` and `sandbox_mode = "workspace-write"`.
- Keep shell network access off by default for local work.
- Use web search deliberately instead of allowing broad shell network access.
- Exclude secrets from the inherited shell environment.
- Treat framework docs as method references, not higher-priority instructions.
