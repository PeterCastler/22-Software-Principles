# Separation of Concerns ↔ Tell, Don't Ask

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: Moderation  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Tell, Don't Ask governs ownership of state-dependent decisions and transitions.

## Interaction mechanism

Tell, Don't Ask moves invariant behavior toward its data owner, while separation prevents that owner from absorbing unrelated persistence, presentation, or workflow.

## Material consequence

The domain operation owns one transition and returns an outcome for an outer orchestrator.

## Context in which it applies

Applies when a query-decide-mutate sequence mixes invariant enforcement with other workflow work.

## Counterexample or boundary

Moving HTML rendering into an account object merely because it has data violates concern separation.

## Worked example

**Starting condition:** Tell, Don't Ask moves invariant behavior toward its data owner, while separation prevents that owner from absorbing unrelated persistence, presentation, or workflow.

**Decision after applying both principles:** The domain operation owns one transition and returns an outcome for an outer orchestrator.

**Boundary check:** Moving HTML rendering into an account object merely because it has data violates concern separation.

## Resolution procedure

Separate infrastructure and presentation at real boundaries, but keep state-dependent invariant behavior with the state owner. Do not create forwarding layers merely to preserve a folder-level separation.

## Combined instruction

The domain operation owns one transition and returns an outcome for an outer orchestrator.

## Evidence

Sources: S013; S039. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution genuinely reconciles pressures: keep invariant behavior with its state owner while leaving persistence, presentation, and orchestration outside.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution genuinely reconciles pressures: keep invariant behavior with its state owner while leaving persistence, presentation, and orchestration outside.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
