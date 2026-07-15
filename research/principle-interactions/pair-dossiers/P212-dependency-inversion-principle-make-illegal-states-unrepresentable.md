# Dependency Inversion Principle ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: Reinforcement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dependency Inversion Principle governs contract ownership and source-dependency direction; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A policy-owned boundary can accept and return precise domain values, preventing vendor request shapes from widening the core's state space.

## Material consequence

The outer adapter converts detail-specific values into variants whose invariants the policy understands.

## Context in which it applies

Applies when external detail types admit states irrelevant or invalid to domain policy.

## Counterexample or boundary

A passthrough adapter that preserves the entire vendor response provides no representational protection.

## Worked example

**Starting condition:** A policy-owned boundary can accept and return precise domain values, preventing vendor request shapes from widening the core's state space.

**Decision after applying both principles:** The outer adapter converts detail-specific values into variants whose invariants the policy understands.

**Boundary check:** A passthrough adapter that preserves the entire vendor response provides no representational protection.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The outer adapter converts detail-specific values into variants whose invariants the policy understands.

## Evidence

Sources: I008; I010; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A domain-owned port with precise values specifically prevents vendor states from widening policy's representable space; a passthrough adapter falsifies the mechanism.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Complementary / Convergent**. A domain-owned port with precise values specifically prevents vendor states from widening policy's representable space; a passthrough adapter falsifies the mechanism.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
