# KISS ↔ Negative Code

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Negative Code governs net removal of owned machinery while preserving contract.

## Interaction mechanism

A contract-preserving deletion pass directly reduces the concepts and obligations KISS counts.

## Material consequence

After correctness is established, redundant layers, wrappers, options, and obsolete perimeter artifacts can be removed.

## Context in which it applies

Applies when evidence shows an implementation slice is replaceable or redundant.

## Counterexample or boundary

Compressing readable code into a clever one-liner reduces lines but not whole-system complexity.

## Worked example

**Starting condition:** A contract-preserving deletion pass directly reduces the concepts and obligations KISS counts.

**Decision after applying both principles:** After correctness is established, redundant layers, wrappers, options, and obsolete perimeter artifacts can be removed.

**Boundary check:** Compressing readable code into a clever one-liner reduces lines but not whole-system complexity.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

After correctness is established, redundant layers, wrappers, options, and obsolete perimeter artifacts can be removed.

## Evidence

Sources: I020; S001. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Contract-preserving removal directly reduces concepts and obligations counted by KISS; the code-golf counterexample distinguishes deletion from genuine simplification.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Contract-preserving removal directly reduces concepts and obligations counted by KISS; the code-golf counterexample distinguishes deletion from genuine simplification.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
