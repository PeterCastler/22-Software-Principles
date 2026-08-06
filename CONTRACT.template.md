# Task Contract

> Generate `CONTRACT.md` from this template immediately before implementation.
> One task only; fewer than 100 lines; remove every placeholder and unused section.

## Objective

- Outcome: `<one observable result>`
- Current requirement: `<what must be true now>`

## Scope

- May change: `<files, components, or behavior>`
- Must preserve: `<public, data, security, accessibility, and operational contracts>`
- Non-goals: `<plausible work that is intentionally excluded>`

## Decisions

- Relevant bundle clause(s): `<B01-B06, only when their preconditions hold>`
- Evidence: `<current code, tests, issue, trace, or authoritative requirement>`
- Boundary or counterexample: `<why the selected guidance applies here>`

## Acceptance

- [ ] `<observable behavior or artifact>`
- [ ] `<regression or compatibility condition>`

## Verification

- Automated: `<exact commands and expected result>`
- Manual: `<focused check, or "none">`

## Forbidden

- NEVER broaden the objective or add speculative capability.
- NEVER rewrite an entire file when a surgical edit can satisfy the contract.
- NEVER abstract predicted reuse; require repeated evidence unless one authoritative
  protocol, security invariant, or regulated rule already exists.
- NEVER delete behavior from line count or a single reference search; prove it dead
  or prove its replacement semantically adequate.
- NEVER weaken a preserved contract to make verification pass.
- NEVER apply a bundle clause while omitting its boundary or counterexample.
- NEVER modify `<task-specific protected files, APIs, data, or behavior>`.
