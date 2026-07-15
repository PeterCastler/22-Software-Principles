# Refactoring Toward Primitives ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Refactoring Toward Primitives governs replacement of custom code by existing capabilities; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

A standard parser, schema, or framework decoder can construct the trusted value and replace handwritten checking.

## Material consequence

The team verifies error, normalization, and compatibility semantics before deleting the custom validator.

## Context in which it applies

Applies when the primitive's output can represent the precise internal contract.

## Counterexample or boundary

A generic JSON parse does not establish domain ranges and is insufficient by itself.

## Worked example

**Starting condition:** A standard parser, schema, or framework decoder can construct the trusted value and replace handwritten checking.

**Decision after applying both principles:** The team verifies error, normalization, and compatibility semantics before deleting the custom validator.

**Boundary check:** A generic JSON parse does not establish domain ranges and is insufficient by itself.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The team verifies error, normalization, and compatibility semantics before deleting the custom validator.

## Evidence

Sources: I007; I013. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A standard parser or decoder can construct the precise trusted value and replace handwritten checks, subject to exact normalization and error semantics.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. A standard parser or decoder can construct the precise trusted value and replace handwritten checks, subject to exact normalization and error semantics.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
