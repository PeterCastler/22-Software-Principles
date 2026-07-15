# Negative Code ↔ Dependency Inversion Principle

Assessment status: Rejected after adversarial review  
Primary classification: Independence  
Secondary classifications: None  
Evidence grade: Unsupported  
Confidence: high

## Shared decision surface

Causally connected decisions: Negative Code governs net removal of owned machinery while preserving contract; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

A one-use interface may look deletable, yet a policy-owned boundary can remain valuable when it isolates real volatility.

## Material consequence

No pair-specific, context-independent implementation or review consequence survived adversarial review.

## Context in which it applies

Applies when an abstraction has one implementation and its boundary role is disputed.

## Counterexample or boundary

A one-implementation adapter shielding core policy from a volatile vendor is not redundant.

## Worked example

**Starting condition:** A one-use interface may look deletable, yet a policy-owned boundary can remain valuable when it isolates real volatility.

**Decision after applying both principles:** The reviewer deletes forwarding abstractions but preserves the narrow boundary whose responsibility is demonstrable.

**Boundary check:** A one-implementation adapter shielding core policy from a volatile vendor is not redundant.

## Resolution procedure

Not applicable: adversarial review found no publishable Tension or Conflict.

## Combined instruction

None. Apply each principle from its own canonical preconditions; do not infer a combined rule from this rejected pair.

## Evidence

Evidence grade: **Unsupported**. Negative Code's deletion test applies to every abstraction; a one-implementation DIP boundary is merely one counterexample to careless deletion, not a unique causal interaction between the principles. See the [source register](../source-register.md) for the sources that were tested.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Independence / reject**.

Adversarial verdict: **reject**; recommendation: **Independence / Unsupported**. Negative Code's deletion test applies to every abstraction; a one-implementation DIP boundary is merely one counterexample to careless deletion, not a unique causal interaction between the principles.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
