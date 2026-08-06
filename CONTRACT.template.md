# Consequential Design Contract

> Optional shared export only. Create this file when the user explicitly requests a
> collaborative artifact for consequential work. Keep it below 100 lines, replace
> every placeholder, and delete unused sections. It is not standing authority for
> later tasks unless an active instruction links it.

## Requirement

- Current complete outcome: `<observable result>`
- Decision surface: `<consequential choice this contract constrains>`

## Alternatives

- Conservative option: `<smallest adequate existing-shape option>`
- Proposed option: `<recommended option and lifecycle consequence>`
- Evidence: `<code, tests, trace, schema, or authoritative requirement>`
- Assumptions: `<facts not yet established>`

## Guidance

- Relevant principle or primary bundle: `<none, one principle, or B01-B06>`
- Boundary or counterexample: `<stopping condition that must remain visible>`

## Scope

- May change: `<files, components, data, or behavior>`
- Must preserve: `<public, data, security, accessibility, and operational contracts>`
- Non-goals: `<plausible work intentionally excluded>`

## Resolved Product Decisions

- `<Decision Gate question and user-owned answer, or "none">`

## Acceptance

- [ ] `<observable behavior or artifact>`
- [ ] `<regression or compatibility condition>`

## Verification

- Automated: `<exact commands and expected result>`
- Manual: `<focused check, or "none">`

## Forbidden

- NEVER broaden the requirement or add speculative capability.
- NEVER weaken a preserved contract to make verification pass.
- NEVER abstract predicted reuse without repeated evidence or an existing authority.
- NEVER delete behavior without proving it dead or semantically replaced.
- NEVER omit the selected guidance's boundary or counterexample.
- NEVER modify `<task-specific protected files, APIs, data, or behavior>`.
