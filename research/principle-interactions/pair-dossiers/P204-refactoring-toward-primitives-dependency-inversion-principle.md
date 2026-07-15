# Refactoring Toward Primitives ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Refactoring Toward Primitives governs replacement of custom code by existing capabilities; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

Primitive-first favors direct platform use, while DIP may justify an adapter when the primitive is volatile or leaks irrelevant detail into policy.

## Material consequence

The implementation uses the primitive directly unless a narrower stable domain contract removes real coupling.

## Context in which it applies

Applies when a platform capability could be called directly but sits at a policy/detail boundary.

## Counterexample or boundary

A wrapper that only renames `JSON.stringify` adds indirection without inversion value.

## Worked example

**Starting condition:** Primitive-first favors direct platform use, while DIP may justify an adapter when the primitive is volatile or leaks irrelevant detail into policy.

**Decision after applying both principles:** The implementation uses the primitive directly unless a narrower stable domain contract removes real coupling.

**Boundary check:** A wrapper that only renames `JSON.stringify` adds indirection without inversion value.

## Resolution procedure

Use the platform primitive directly by default. Add an adapter only when it narrows volatile, irrelevant, or incompatible semantics into a stable application contract; delete wrappers that only mirror or rename the primitive.

## Combined instruction

The implementation uses the primitive directly unless a narrower stable domain contract removes real coupling.

## Evidence

Sources: I010; I013; I014. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution is sound: call a fitting primitive directly unless a real policy boundary requires semantic narrowing, and delete wrappers that only mirror it.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution is sound: call a fitting primitive directly unless a real policy boundary requires semantic narrowing, and delete wrappers that only mirror it.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
