# Negative Code ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Negative Code governs net removal of owned machinery while preserving contract; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

Parsing once preserves evidence that makes downstream casts, validators, and impossible-case branches removable.

## Material consequence

The deletion follows signature changes so raw values cannot bypass the parser.

## Context in which it applies

Applies when repeated structural validation follows a boundary check that currently discards evidence.

## Counterexample or boundary

Rate limits and concurrent uniqueness remain necessary after structural parsing.

## Worked example

**Starting condition:** Parsing once preserves evidence that makes downstream casts, validators, and impossible-case branches removable.

**Decision after applying both principles:** The deletion follows signature changes so raw values cannot bypass the parser.

**Boundary check:** Rate limits and concurrent uniqueness remain necessary after structural parsing.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The deletion follows signature changes so raw values cannot bypass the parser.

## Evidence

Sources: I007; I020. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: A parser result carried in signatures makes repeated structural validators and casts safely removable, while use-time limits remain valid counterexamples.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. A parser result carried in signatures makes repeated structural validators and casts safely removable, while use-time limits remain valid counterexamples.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
