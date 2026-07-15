# Composition over Inheritance ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: Enablement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Composition over Inheritance governs reuse and variation mechanism; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

DIP defines the policy-owned boundary and composition supplies the concrete detail at the application edge without inheritance.

## Material consequence

A small function or object is passed to policy; no container or base class is required.

## Context in which it applies

Applies when a real volatile detail must be assembled behind a stable policy contract.

## Counterexample or boundary

Composing a fixed helper solely for mockability adds no inversion value.

## Worked example

**Starting condition:** DIP defines the policy-owned boundary and composition supplies the concrete detail at the application edge without inheritance.

**Decision after applying both principles:** A small function or object is passed to policy; no container or base class is required.

**Boundary check:** Composing a fixed helper solely for mockability adds no inversion value.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A small function or object is passed to policy; no container or base class is required.

## Evidence

Sources: I010; I011. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: DIP defines the policy-owned contract while composition supplies the outer implementation without a base class; a fixed mock-only helper correctly stops the interaction.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Complementary / Convergent**. DIP defines the policy-owned contract while composition supplies the outer implementation without a base class; a fixed mock-only helper correctly stops the interaction.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
