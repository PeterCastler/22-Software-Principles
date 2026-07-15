# Dead Code Elimination ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: Enablement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dead Code Elimination governs liveness within the supported system boundary; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A stronger representation can prove formerly defensive branches unreachable, after which liveness analysis supports deletion.

## Material consequence

The change first closes construction paths, then removes branches and tests for states no longer representable.

## Context in which it applies

Applies when all supported constructors exclude the old state.

## Counterexample or boundary

Legacy database rows may keep the defensive branch live until migration completes.

## Worked example

**Starting condition:** A stronger representation can prove formerly defensive branches unreachable, after which liveness analysis supports deletion.

**Decision after applying both principles:** The change first closes construction paths, then removes branches and tests for states no longer representable.

**Boundary check:** Legacy database rows may keep the defensive branch live until migration completes.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The change first closes construction paths, then removes branches and tests for states no longer representable.

## Evidence

Sources: S027; I007; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Closing all supported construction paths can make old defensive branches unreachable, after which DCE applies; legacy persisted rows correctly keep them live.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. Closing all supported construction paths can make old defensive branches unreachable, after which DCE applies; legacy persisted rows correctly keep them live.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
