# Installation und Nutzung

## Deutsch

Diese Anleitung richtet sich an Nutzer, die den Skill `codex-setup-checklist` installieren und in Codex verwenden wollen.

Der Skill hilft dabei, Codex-Setups zu prüfen, sichere Projekt-Defaults zu erzeugen, bestehende Claude-Konfigurationen nach Codex zu übertragen und Konflikte zwischen `AGENTS.md`, Skills, Rules, Hooks und Framework-Dokumenten sichtbar zu machen.

Die verschiedenen Nutzungsarten sind separat beschrieben in [`usage.de.md`](usage.de.md). Die englische Fassung dieser Datei liegt unter [`installation.en.md`](installation.en.md).

## Voraussetzungen

- Codex ist lokal eingerichtet.
- Du kannst Dateien in deinem Codex-Konfigurationsordner schreiben.
- Optional: `git`, wenn du das Repository direkt von GitHub klonen willst.

Der persönliche Codex-Ordner liegt normalerweise hier:

```text
~/.codex/
```

Skills werden in diesem Ordner unter `skills/` abgelegt:

```text
~/.codex/skills/
```

## Terminal oder Codex?

Du hast zwei Wege:

1. **Selbst im Terminal ausfuehren:** Kopiere die Befehle aus dieser Anleitung in dein Terminal.
2. **Codex installieren lassen:** Gib Codex einen Prompt, der die globale Installation ausdruecklich erlaubt.

Beispiel-Prompt fuer Codex:

```text
Installiere den Skill https://github.com/vibercoder79/codex-governance-best-practice global als ~/.codex/skills/codex-setup-checklist und pruefe danach, ob SKILL.md vorhanden ist.
```

Hinweis: Bei der globalen Installation schreibt Codex ausserhalb des aktuellen Repositories nach `~/.codex/skills`. Je nach Sandbox- und Approval-Einstellung muss Codex dafuer eine Freigabe anfragen. Das ist erwartbar.

## Variante A: Global installieren

Diese Variante ist empfohlen, wenn du den Skill in mehreren Repositories verwenden willst.

Die folgenden Befehle fuehrst du im Terminal aus, wenn du die Installation selbst machen willst:

1. Skill-Ordner anlegen:

```bash
mkdir -p ~/.codex/skills
```

2. Repository direkt in den Skill-Zielordner klonen:

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
```

3. Prüfen, ob die Skill-Datei vorhanden ist:

```bash
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

Danach kann Codex den Skill in jedem Projekt verwenden.

Wenn der Zielordner bereits existiert, nutze den Update-Weg weiter unten (`cd ~/.codex/skills/codex-setup-checklist` und `git pull`). Entferne oder ersetze bestehende Ordner nur bewusst.

## Variante B: Projektlokal installieren

Diese Variante ist sinnvoll, wenn der Skill nur für ein bestimmtes Repository gelten soll.

Führe die Befehle im Ziel-Repository aus:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

Danach liegt der Skill direkt im Projekt:

```text
.codex/skills/codex-setup-checklist/SKILL.md
```

## Variante C: Als Vorlage verwenden

Diese Variante ist sinnvoll, wenn du ein eigenes internes Governance-Repository daraus ableiten willst.

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git
cd codex-governance-best-practice
```

Passe danach die Templates, Rules, Hooks und Referenzdokumente an deine Organisation an.

## Nutzung in Codex

Nach der Installation kannst du den Skill direkt im Prompt ansprechen.

Best-Practice-Setup fuer ein Repository installieren:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Setup eines Repositories prüfen:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Sichere Projektkonfiguration erzeugen:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Claude-Konfiguration nach Codex migrieren:

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md and .claude/settings.json setup to Codex.
```

Konflikte zwischen Anweisungsebenen prüfen:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

Mehr Beispiele und Entscheidungshilfe findest du in [`usage.de.md`](usage.de.md).

## Typische Ergebnisse

Je nach Aufgabe erstellt oder prüft der Skill unter anderem:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/rules/default.rules`
- `.codex/hooks.json`
- `PLANS.md`
- `code_review.md`
- bestehende Claude-Dateien wie `CLAUDE.md` oder `.claude/settings.json`

Der Skill soll bestehende Dateien zuerst lesen, Änderungen gezielt vorschlagen und keine Secrets ausgeben oder speichern.

## Aktualisieren

Wenn du den Skill global installiert hast:

```bash
cd ~/.codex/skills/codex-setup-checklist
git pull
```

Wenn du ihn projektlokal installiert hast:

```bash
cd .codex/skills/codex-setup-checklist
git pull
```

Wenn du den Skill nicht per `git clone`, sondern per Kopie installiert hast, ersetze den Ordner durch eine neue Kopie des Repositories.

## Deinstallieren

Globale Installation entfernen:

```bash
rm -rf ~/.codex/skills/codex-setup-checklist
```

Projektlokale Installation entfernen:

```bash
rm -rf .codex/skills/codex-setup-checklist
```

## Fehlerbehebung

Wenn Codex den Skill nicht findet:

- Prüfe, ob `SKILL.md` direkt im Skill-Ordner liegt.
- Prüfe den Ordnernamen: empfohlen ist `codex-setup-checklist`.
- Starte Codex neu, falls Skills nur beim Session-Start geladen werden.
- Achte darauf, dass der Skill nicht versehentlich eine zusätzliche Unterordner-Ebene hat, zum Beispiel `codex-setup-checklist/codex-governance-best-practice/SKILL.md`.

Wenn Git nicht verfügbar ist, lade das Repository als ZIP von GitHub herunter und entpacke es in den gewünschten Skill-Ordner.

## English Summary

This German installation guide explains how to install and use the `codex-setup-checklist` skill.

For the full English guide, see [`installation.en.md`](installation.en.md).

Short version:

Run in the terminal:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

Or ask Codex:

```text
Install the skill https://github.com/vibercoder79/codex-governance-best-practice globally as ~/.codex/skills/codex-setup-checklist and then verify that SKILL.md exists.
```

Then use:

```text
Use the codex-setup-checklist skill to audit this repository.
```
