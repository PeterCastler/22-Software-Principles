# Composition over Inheritance ↔ Refactoring Toward Primitives

Assessment status: Rejected after adversarial review  
Primary classification: Independence  
Secondary classifications: None  
Evidence grade: Unsupported  
Confidence: high

## Shared decision surface

Causally connected decisions: Composition over Inheritance governs reuse and variation mechanism; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

A standard adapter or platform capability can serve as a composed collaborator and eliminate a custom subclass family.

## Material consequence

No pair-specific, context-independent implementation or review consequence survived adversarial review.

## Context in which it applies

Applies when the primitive matches one independent behavior axis.

## Counterexample or boundary

Wrapping every standard call in a custom strategy preserves rather than removes machinery.

## Worked example

**Starting condition:** A standard adapter or platform capability can serve as a composed collaborator and eliminate a custom subclass family.

**Decision after applying both principles:** The team reuses the primitive directly or through one policy-bearing adapter instead of maintaining inheritance machinery.

**Boundary check:** Wrapping every standard call in a custom strategy preserves rather than removes machinery.

## Resolution procedure

Not applicable: adversarial review found no publishable Tension or Conflict.

## Combined instruction

None. Apply each principle from its own canonical preconditions; do not infer a combined rule from this rejected pair.

## Evidence

Evidence grade: **Unsupported**. A platform primitive can happen to serve as a collaborator, but that does not generally enable composition or eliminate inheritance. The proposed adapter example is a tactic-specific coincidence. See the [source register](../source-register.md) for the sources that were tested.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Independence / reject**.

Adversarial verdict: **reject**; recommendation: **Independence / Unsupported**. A platform primitive can happen to serve as a collaborator, but that does not generally enable composition or eliminate inheritance. The proposed adapter example is a tactic-specific coincidence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
