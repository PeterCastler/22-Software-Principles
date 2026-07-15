# Rule of Three ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: Sequencing  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Rule of Three governs timing and scope of abstraction; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

Repeated implementations can evidence variation, but one current volatile boundary can justify inversion earlier; the rule prevents interface-per-class ritual.

## Material consequence

The team bases inversion on observed volatility or multiple implementations rather than an arbitrary count.

## Context in which it applies

Applies when a policy-owned interface is proposed without demonstrated boundary value.

## Counterexample or boundary

One external payment SDK can justify a boundary because its vendor types already infect stable policy.

## Worked example

**Starting condition:** Repeated implementations can evidence variation, but one current volatile boundary can justify inversion earlier; the rule prevents interface-per-class ritual.

**Decision after applying both principles:** The team bases inversion on observed volatility or multiple implementations rather than an arbitrary count.

**Boundary check:** One external payment SDK can justify a boundary because its vendor types already infect stable policy.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The team bases inversion on observed volatility or multiple implementations rather than an arbitrary count.

## Evidence

Sources: I004; I010. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Rule of Three moderates ceremonial inversion without imposing a literal count when one real volatile boundary exists; the payment-SDK counterexample preserves that qualification.

## Independent review

Blind primary screen: **Moderation / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Moderation / Convergent**. The Rule of Three moderates ceremonial inversion without imposing a literal count when one real volatile boundary exists; the payment-SDK counterexample preserves that qualification.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
