# Principle of Least Power ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Principle of Least Power governs expressive power of the chosen mechanism; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A representation that cannot express invalid combinations has less power in exactly the domain dimension that creates defensive work.

## Material consequence

The implementation chooses a constrained sum type, set, map, or constructor over a broad bag of optional fields.

## Context in which it applies

Applies when stable illegal combinations can be excluded by an ordinary representation.

## Counterexample or boundary

Encoding a mutable remote fact in a static type overclaims what the representation can guarantee.

## Worked example

**Starting condition:** A representation that cannot express invalid combinations has less power in exactly the domain dimension that creates defensive work.

**Decision after applying both principles:** The implementation chooses a constrained sum type, set, map, or constructor over a broad bag of optional fields.

**Boundary check:** Encoding a mutable remote fact in a static type overclaims what the representation can guarantee.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The implementation chooses a constrained sum type, set, map, or constructor over a broad bag of optional fields.

## Evidence

Sources: S011; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A representation excluding invalid combinations is less powerful along the exact harmful state dimension, with advanced or mutable-fact encodings as concrete limits.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. A representation excluding invalid combinations is less powerful along the exact harmful state dimension, with advanced or mutable-fact encodings as concrete limits.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
