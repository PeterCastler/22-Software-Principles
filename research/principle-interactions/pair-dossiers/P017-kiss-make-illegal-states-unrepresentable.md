# KISS ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A precise representation removes downstream branches, but elaborate type machinery can cost more understanding than the invalid states it excludes.

## Material consequence

The model encodes only high-value stable invariants with the least elaborate adequate type or constructor.

## Context in which it applies

Applies when many consumers otherwise handle the same impossible combinations.

## Counterexample or boundary

A single local range check may be clearer than a novel advanced type encoding.

## Worked example

**Starting condition:** A precise representation removes downstream branches, but elaborate type machinery can cost more understanding than the invalid states it excludes.

**Decision after applying both principles:** The model encodes only high-value stable invariants with the least elaborate adequate type or constructor.

**Boundary check:** A single local range check may be clearer than a novel advanced type encoding.

## Resolution procedure

Compare the branches and invalid combinations removed with the representational burden added. Encode only stable, high-value invariants, using the least elaborate type or constructor that closes the relevant construction path.

## Combined instruction

The model encodes only high-value stable invariants with the least elaborate adequate type or constructor.

## Evidence

Sources: S001; I007; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension is real and resolved by comparing removed invalid-state branches with added representational burden; the single-check case is a valid stopping rule.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension is real and resolved by comparing removed invalid-state branches with added representational burden; the single-check case is a valid stopping rule.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
