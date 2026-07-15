# Convention over Configuration ↔ Refactoring Toward Primitives

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Convention over Configuration governs routine defaults versus explicit exceptions; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

Framework and ecosystem primitives often embody conventions that make repetitive local configuration unnecessary.

## Material consequence

The project follows the primitive's established discovery and naming defaults and retains explicit exceptions only.

## Context in which it applies

Applies when a maintained platform convention covers the dominant case.

## Counterexample or boundary

Opaque framework inference with many overrides can cost more than direct configuration.

## Worked example

**Starting condition:** Framework and ecosystem primitives often embody conventions that make repetitive local configuration unnecessary.

**Decision after applying both principles:** The project follows the primitive's established discovery and naming defaults and retains explicit exceptions only.

**Boundary check:** Opaque framework inference with many overrides can cost more than direct configuration.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The project follows the primitive's established discovery and naming defaults and retains explicit exceptions only.

## Evidence

Sources: I019; I013. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: When a maintained platform primitive embodies a stable convention, adopting it can remove custom discovery and configuration; opaque inference with dominant overrides is a specific counterexample.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. When a maintained platform primitive embodies a stable convention, adopting it can remove custom discovery and configuration; opaque inference with dominant overrides is a specific counterexample.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
