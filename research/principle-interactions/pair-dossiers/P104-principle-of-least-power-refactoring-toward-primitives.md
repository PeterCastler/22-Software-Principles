# Principle of Least Power ↔ Refactoring Toward Primitives

Assessment status: Rejected after adversarial review  
Primary classification: Independence  
Secondary classifications: None  
Evidence grade: Unsupported  
Confidence: high

## Shared decision surface

Causally connected decisions: Principle of Least Power governs expressive power of the chosen mechanism; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

Existing primitives often provide constrained semantics—schema, constraint, native element, standard query—that replace arbitrary custom code.

## Material consequence

No pair-specific, context-independent implementation or review consequence survived adversarial review.

## Context in which it applies

Applies when the platform primitive fully supplies the required semantics.

## Counterexample or boundary

A regular expression is not an adequate primitive for a nested grammar that requires a parser.

## Worked example

**Starting condition:** Existing primitives often provide constrained semantics—schema, constraint, native element, standard query—that replace arbitrary custom code.

**Decision after applying both principles:** The team chooses the least expressive matching primitive before a script, callback framework, or bespoke implementation.

**Boundary check:** A regular expression is not an adequate primitive for a nested grammar that requires a parser.

## Resolution procedure

Not applicable: adversarial review found no publishable Tension or Conflict.

## Combined instruction

None. Apply each principle from its own canonical preconditions; do not infer a combined rule from this rejected pair.

## Evidence

Evidence grade: **Unsupported**. The claim that primitives are often constrained is contingent coincidence: existing capabilities may be more expressive, and Least Power may favor a custom declarative form. Neither principle causally changes the other's decision. See the [source register](../source-register.md) for the sources that were tested.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Independence / reject**.

Adversarial verdict: **reject**; recommendation: **Independence / Unsupported**. The claim that primitives are often constrained is contingent coincidence: existing capabilities may be more expressive, and Least Power may favor a custom declarative form. Neither principle causally changes the other's decision.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
