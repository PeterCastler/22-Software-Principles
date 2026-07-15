# Refactoring Toward Primitives ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Refactoring Toward Primitives governs replacement of custom code by existing capabilities; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

Sets, maps, database constraints, discriminated unions, and standard constructors can enforce invariants with less custom validation machinery.

## Material consequence

The design selects a primitive whose native semantics exclude the invalid state and deletes redundant enforcement.

## Context in which it applies

Applies when an existing type, collection, or storage constraint matches the invariant.

## Counterexample or boundary

A database uniqueness constraint does not by itself model a recoverable domain error for the caller.

## Worked example

**Starting condition:** Sets, maps, database constraints, discriminated unions, and standard constructors can enforce invariants with less custom validation machinery.

**Decision after applying both principles:** The design selects a primitive whose native semantics exclude the invalid state and deletes redundant enforcement.

**Boundary check:** A database uniqueness constraint does not by itself model a recoverable domain error for the caller.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The design selects a primitive whose native semantics exclude the invalid state and deletes redundant enforcement.

## Evidence

Sources: I013; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A matching set, union, constructor, or storage constraint can replace custom enforcement while excluding the invalid state; error-semantics mismatch is a material counterexample.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. A matching set, union, constructor, or storage constraint can replace custom enforcement while excluding the invalid state; error-semantics mismatch is a material counterexample.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
