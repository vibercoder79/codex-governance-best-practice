# Codex Instruction Conflict Model

## Goal

Prevent silent conflicts between persistent guidance, project rules, task-specific skills, framework documents, hooks, rules, and user prompts.

## Core principle

Do not make `AGENTS.md` a second framework. Use it as a router and durable working agreement.

## Recommended precedence

1. Safety, security, secrets, sandbox, approval, and destructive-action rules.
2. Explicit user instructions for the current task, unless they violate safety or repository constraints.
3. Project-specific `AGENTS.md` instructions over global `AGENTS.md` instructions.
4. Explicitly invoked skills define the task-specific workflow.
5. Framework documents define method, terminology, and delivery logic.
6. Hooks and rules are enforcement mechanisms and are not optional guidance.

## Conflict examples

### AGENTS.md vs Skill

- AGENTS.md says: "Never add dependencies without approval."
- Skill says: "Install required packages."
- Resolution: ask before adding dependencies.

### Framework vs Repository

- Framework says: "Run full test suite before completion."
- Repository AGENTS.md says: "Run the smallest relevant test first; full suite only before release."
- Resolution: follow repository testing expectation unless the user requests release readiness.

### User prompt vs Safety

- User says: "Run deployment now."
- Rules say deployment requires approval or is forbidden.
- Resolution: stop, explain the safety gate, request explicit approval if allowed by policy.

### Hook vs Workflow

- Skill asks Codex to modify files.
- Stop hook requires summary and verification evidence.
- Resolution: perform workflow, then satisfy stop hook requirements.

## AGENTS.md template section

```markdown
## Instruction precedence and conflict handling

This repository may use AGENTS.md files, Codex skills, framework documents, rules, hooks, MCP tools, and user-provided task instructions.

Use the following precedence:

1. Safety, security, secrets, sandbox, approval, and destructive-action rules always take priority.
2. Explicit user instructions for the current task take priority over generic workflow preferences, unless they violate safety or repository rules.
3. Repository-specific AGENTS.md instructions take priority over global AGENTS.md instructions.
4. Explicitly invoked skills define the task-specific workflow.
5. Framework documents define method and terminology, but must not override safety, approval, build, test, or repository constraints.
6. Hooks and rules are enforcement mechanisms, not optional guidance.

If instructions conflict:
- Do not silently choose one.
- State the conflict briefly.
- Follow the safest non-destructive path.
- Ask for approval only if the task cannot proceed safely without a decision.
```
