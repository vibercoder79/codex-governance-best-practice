# Code Review Checklist

## Scope

- Does the change match the requested task?
- Are unrelated files untouched?
- Is the diff small enough to review?

## Correctness

- Are edge cases handled?
- Are tests added or updated where useful?
- Do existing tests still express the intended behavior?

## Security

- No secrets, tokens, or credentials added.
- No unsafe shell execution or uncontrolled network access introduced.
- No dependency added without clear rationale.

## Maintainability

- Does the change fit the existing architecture?
- Are names and boundaries clear?
- Is complexity justified?

## Verification

- Tests run:
- Lint run:
- Build run:
- Manual validation:

## Residual risks

List anything that remains uncertain.
