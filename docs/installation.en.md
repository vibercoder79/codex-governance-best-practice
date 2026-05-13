# Installation and Usage

## English

This guide is for users who want to install and use the `codex-setup-checklist` skill in Codex.

The skill helps audit Codex setups, create safe project defaults, migrate existing Claude configuration to Codex, and detect conflicts between `AGENTS.md`, skills, rules, hooks, and framework documents.

The different usage modes are described separately in [`usage.en.md`](usage.en.md). The German version of this file is available at [`installation.de.md`](installation.de.md).

## Requirements

- Codex is installed locally.
- You can write files to your Codex configuration directory.
- Optional: `git`, if you want to clone the repository directly from GitHub.

The personal Codex directory is usually:

```text
~/.codex/
```

Skills are stored below `skills/`:

```text
~/.codex/skills/
```

## Terminal or Codex?

You have two options:

1. **Run the commands yourself in the terminal:** Copy the commands from this guide into your terminal.
2. **Ask Codex to install it:** Give Codex a prompt that explicitly allows the global installation.

Example prompt for Codex:

```text
Install the skill https://github.com/vibercoder79/codex-governance-best-practice globally as ~/.codex/skills/codex-setup-checklist and then verify that SKILL.md exists.
```

Note: Global installation writes outside the current repository into `~/.codex/skills`. Depending on sandbox and approval settings, Codex may need to request permission. That is expected.

## Option A: Install Globally

Use this option if you want to use the skill across multiple repositories.

Run the following commands in your terminal if you want to install it yourself:

1. Create the skills directory:

```bash
mkdir -p ~/.codex/skills
```

2. Clone the repository directly into the skill target folder:

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
```

3. Check that the skill file exists:

```bash
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

Codex can now use the skill in any project.

If the target folder already exists, use the update path below (`cd ~/.codex/skills/codex-setup-checklist` and `git pull`). Remove or replace existing folders only deliberately.

## Option B: Install Per Project

Use this option if the skill should only be available in one repository.

Run the commands inside the target repository:

```bash
mkdir -p .codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git .codex/skills/codex-setup-checklist
```

The skill will then live inside the project:

```text
.codex/skills/codex-setup-checklist/SKILL.md
```

## Option C: Use as a Template

Use this option if you want to derive your own internal governance repository from this project.

```bash
git clone https://github.com/vibercoder79/codex-governance-best-practice.git
cd codex-governance-best-practice
```

Then adapt the templates, rules, hooks, and reference documents to your organization.

## Using the Skill in Codex

After installation, invoke the skill directly in your prompt.

Install a best-practice setup for a repository:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Audit a repository setup:

```text
Use the codex-setup-checklist skill to audit this repository.
```

Create a safe project configuration:

```text
Use the codex-setup-checklist skill to create a safe project-level Codex setup for this repository.
```

Migrate Claude configuration to Codex:

```text
Use the codex-setup-checklist skill to migrate my CLAUDE.md and .claude/settings.json setup to Codex.
```

Check conflicts between instruction layers:

```text
Use the codex-setup-checklist skill to check conflicts between AGENTS.md, skills, rules, hooks, and framework docs.
```

For more examples and mode guidance, see [`usage.en.md`](usage.en.md).

## Typical Outputs

Depending on the task, the skill creates or checks files such as:

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/rules/default.rules`
- `.codex/hooks.json`
- `PLANS.md`
- `code_review.md`
- existing Claude files such as `CLAUDE.md` or `.claude/settings.json`

The skill is designed to read existing files first, propose targeted changes, and avoid printing or storing secrets.

## Updating

If you installed the skill globally:

```bash
cd ~/.codex/skills/codex-setup-checklist
git pull
```

If you installed it per project:

```bash
cd .codex/skills/codex-setup-checklist
git pull
```

If you installed the skill by copying files instead of using `git clone`, replace the folder with a fresh copy of the repository.

## Uninstalling

Remove a global installation:

```bash
rm -rf ~/.codex/skills/codex-setup-checklist
```

Remove a project-local installation:

```bash
rm -rf .codex/skills/codex-setup-checklist
```

## Troubleshooting

If Codex does not find the skill:

- Check that `SKILL.md` is directly inside the skill folder.
- Check the folder name: `codex-setup-checklist` is recommended.
- Restart Codex if skills are only loaded at session start.
- Make sure the skill was not copied with an extra nested folder, for example `codex-setup-checklist/codex-governance-best-practice/SKILL.md`.

If Git is not available, download the repository as a ZIP from GitHub and unpack it into the desired skill folder.

## Deutsche Kurzfassung

Diese englische Installationsanleitung erklaert, wie der Skill `codex-setup-checklist` installiert und genutzt wird.

Die vollstaendige deutsche Anleitung findest du unter [`installation.de.md`](installation.de.md).

Kurzversion:

Im Terminal:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/vibercoder79/codex-governance-best-practice.git ~/.codex/skills/codex-setup-checklist
test -f ~/.codex/skills/codex-setup-checklist/SKILL.md
```

Oder Codex darum bitten:

```text
Installiere den Skill https://github.com/vibercoder79/codex-governance-best-practice global als ~/.codex/skills/codex-setup-checklist und pruefe danach, ob SKILL.md vorhanden ist.
```

Danach nutzen:

```text
Use the codex-setup-checklist skill to audit this repository.
```
