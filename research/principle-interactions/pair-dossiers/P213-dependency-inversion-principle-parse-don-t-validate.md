# Dependency Inversion Principle ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: Enablement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dependency Inversion Principle governs contract ownership and source-dependency direction; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

An infrastructure adapter parses vendor or transport data into the trusted values required by the policy-owned contract.

## Material consequence

Invalid external responses fail at the adapter and cannot leak raw SDK types into the core.

## Context in which it applies

Applies when the external detail returns weaker data than policy requires.

## Counterexample or boundary

An already typed in-process collaborator may need inversion but no parsing step.

## Worked example

**Starting condition:** An infrastructure adapter parses vendor or transport data into the trusted values required by the policy-owned contract.

**Decision after applying both principles:** Invalid external responses fail at the adapter and cannot leak raw SDK types into the core.

**Boundary check:** An already typed in-process collaborator may need inversion but no parsing step.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Invalid external responses fail at the adapter and cannot leak raw SDK types into the core.

## Evidence

Sources: I007; I010. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: An outer adapter must parse weak vendor data before satisfying a policy-owned precise contract; an already typed collaborator correctly needs inversion without parsing.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. An outer adapter must parse weak vendor data before satisfying a policy-owned precise contract; an already typed collaborator correctly needs inversion without parsing.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
