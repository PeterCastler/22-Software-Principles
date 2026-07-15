# YAGNI ↔ Rule of Three

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: YAGNI governs timing of capability and extensibility; Rule of Three governs timing and scope of abstraction.

## Interaction mechanism

Both defer abstraction until concrete need exists; repeated cases provide the missing evidence for current reuse.

## Material consequence

The second case may remain local and the third triggers comparison rather than automatic generalization.

## Context in which it applies

Applies when future variation is predicted but not yet observed.

## Counterexample or boundary

Immediate extraction can be justified when a security invariant already has one defined authority.

## Worked example

**Starting condition:** Both defer abstraction until concrete need exists; repeated cases provide the missing evidence for current reuse.

**Decision after applying both principles:** The second case may remain local and the third triggers comparison rather than automatic generalization.

**Boundary check:** Immediate extraction can be justified when a security invariant already has one defined authority.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The second case may remain local and the third triggers comparison rather than automatic generalization.

## Evidence

Sources: I001; I004; S003. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Both govern abstraction timing and repeated cases supply present-need evidence; an already authoritative security rule correctly permits earlier extraction.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Both govern abstraction timing and repeated cases supply present-need evidence; an already authoritative security rule correctly permits earlier extraction.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
