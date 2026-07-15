# KISS ↔ Refactoring Toward Primitives

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

An adequate existing primitive can remove custom implementation, tests, glue, and edge-case obligations from the whole design.

## Material consequence

The team chooses direct platform use when its exact semantics cost less than continuing to own custom machinery.

## Context in which it applies

Applies when a primitive matches the required contract and support baseline.

## Counterexample or boundary

A heavy dependency for a clear ten-line local function increases total complexity.

## Worked example

**Starting condition:** An adequate existing primitive can remove custom implementation, tests, glue, and edge-case obligations from the whole design.

**Decision after applying both principles:** The team chooses direct platform use when its exact semantics cost less than continuing to own custom machinery.

**Boundary check:** A heavy dependency for a clear ten-line local function increases total complexity.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The team chooses direct platform use when its exact semantics cost less than continuing to own custom machinery.

## Evidence

Sources: S001; I013; I014. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A contract-equivalent primitive can remove custom machinery and lifecycle load; semantic mismatch or dependency weight is a concrete counterexample rather than generic reuse praise.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. A contract-equivalent primitive can remove custom machinery and lifecycle load; semantic mismatch or dependency weight is a concrete counterexample rather than generic reuse praise.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
