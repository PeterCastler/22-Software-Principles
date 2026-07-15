# Dead Code Elimination ↔ Boy Scout Rule

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dead Code Elimination governs liveness within the supported system boundary; Boy Scout Rule governs scope and timing of incidental local cleanup.

## Interaction mechanism

The Boy Scout Rule scopes dead-code removal to the touched path, while DCE supplies the evidence threshold for calling it dead.

## Material consequence

A local flag or branch is removed only after dynamic, external, and rollback uses are checked proportionately.

## Context in which it applies

Applies when a suspected dead artifact is adjacent to current work and its liveness can be established.

## Counterexample or boundary

A repository-wide unused-export sweep is separate work, not incidental cleanup.

## Worked example

**Starting condition:** The Boy Scout Rule scopes dead-code removal to the touched path, while DCE supplies the evidence threshold for calling it dead.

**Decision after applying both principles:** A local flag or branch is removed only after dynamic, external, and rollback uses are checked proportionately.

**Boundary check:** A repository-wide unused-export sweep is separate work, not incidental cleanup.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A local flag or branch is removed only after dynamic, external, and rollback uses are checked proportionately.

## Evidence

Sources: S027; I017; S043. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: DCE supplies the liveness proof and Boy Scout supplies incidental scope and timing; neither enables the other, so Complementary better captures the two distinct controls.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Complementary / Convergent**. DCE supplies the liveness proof and Boy Scout supplies incidental scope and timing; neither enables the other, so Complementary better captures the two distinct controls.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
