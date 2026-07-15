# Data-Driven Design ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: Enablement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Data-Driven Design governs representation of regular variation as data or control flow; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

External strings must be parsed into valid table keys or validated rule data before the shared interpreter can assume completeness.

## Material consequence

The lookup accepts a precise key and has no internal unknown-status branch.

## Context in which it applies

Applies when untrusted input selects or supplies table-driven behavior.

## Counterexample or boundary

A table used only with compiler-generated internal keys needs no runtime parser.

## Worked example

**Starting condition:** External strings must be parsed into valid table keys or validated rule data before the shared interpreter can assume completeness.

**Decision after applying both principles:** The lookup accepts a precise key and has no internal unknown-status branch.

**Boundary check:** A table used only with compiler-generated internal keys needs no runtime parser.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The lookup accepts a precise key and has no internal unknown-status branch.

## Evidence

Sources: I007; I015. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Untrusted selectors or rule rows must be parsed before the shared table interpreter can assume valid keys and schema; compiler-generated keys remove the need.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. Untrusted selectors or rule rows must be parsed before the shared table interpreter can assume valid keys and schema; compiler-generated keys remove the need.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
