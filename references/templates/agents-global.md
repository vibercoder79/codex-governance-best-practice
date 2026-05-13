# Global Codex Working Agreements

## Working style

- Read relevant files before changing them.
- Keep changes small, reviewable, and reversible.
- Prefer editing existing files over replacing them wholesale.
- Make assumptions explicit when they affect the result.
- For complex work, propose a short plan before implementation.

## Safety

- Never create, print, modify, commit, or expose secrets.
- Do not modify `.env`, private keys, credentials, production config, or deployment secrets unless explicitly asked and the risk is clear.
- Ask before adding new production dependencies.
- Ask before running destructive commands, migrations, deployments, force-pushes, or commands that change remote state.

## Verification

- Run the smallest relevant check first.
- If tests fail, investigate root cause instead of weakening tests.
- Before finishing, summarize changed files, checks performed, and remaining risks.

## Communication

- Be concise, technical, and direct.
- Prefer concrete diffs, commands, and rationale over generic explanation.
