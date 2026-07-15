# Negative Code ↔ Refactoring Toward Primitives

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Negative Code governs net removal of owned machinery while preserving contract; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

A matching primitive is a mechanism for producing negative code by making custom implementation and glue redundant.

## Material consequence

After characterization, the change deletes the replaced implementation while retaining application-contract tests.

## Context in which it applies

Applies when the primitive matches semantics and costs less to own.

## Counterexample or boundary

Adding a large dependency may reduce local lines while increasing total obligations.

## Worked example

**Starting condition:** A matching primitive is a mechanism for producing negative code by making custom implementation and glue redundant.

**Decision after applying both principles:** After characterization, the change deletes the replaced implementation while retaining application-contract tests.

**Boundary check:** Adding a large dependency may reduce local lines while increasing total obligations.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

After characterization, the change deletes the replaced implementation while retaining application-contract tests.

## Evidence

Sources: I013; I014; I020. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A contract-matching primitive specifically makes the custom implementation and glue removable, directly enabling negative code; dependency weight limits false line-count wins.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. A contract-matching primitive specifically makes the custom implementation and glue removable, directly enabling negative code; dependency weight limits false line-count wins.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
