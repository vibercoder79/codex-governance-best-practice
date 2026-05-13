# Repository Instructions

## Repository layout

- `src/` contains application code.
- `tests/` contains automated tests.
- `docs/` contains architecture, product, and operational documentation.
- `.codex/` contains Codex-specific configuration, hooks, rules, and optional project-local skills.
- Do not edit generated files unless the task explicitly requires it.

Update this section to match the real repository structure before relying on it.

## Build, test, and lint

Replace these commands with the actual project commands:

```bash
npm install
npm run lint
npm test
npm run build
```

## Engineering rules

- Read affected files before editing.
- Keep changes scoped to the user request.
- Preserve existing architecture unless the task explicitly asks for refactoring.
- Do not introduce new frameworks without approval.
- Do not add production dependencies without approval.
- Do not weaken tests to make a change pass.

## Security and safety

- Never expose secrets, tokens, keys, or credentials.
- Do not modify production deployment config unless explicitly requested.
- Ask before running migrations, deployment commands, destructive commands, or commands that modify remote state.
- Treat network access as deliberate, not default.

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

## Done means

Before finishing, provide:

- Summary of changed files.
- Verification performed, including tests, lint, build, or reason not run.
- Any residual risks, assumptions, or follow-up items.
