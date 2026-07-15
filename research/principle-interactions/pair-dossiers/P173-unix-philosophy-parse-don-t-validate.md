# Unix Philosophy ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: Complementary  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Unix Philosophy governs component scope and composition interface; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

Composable external formats require a parser stage before focused domain transformations can rely on their structure.

## Material consequence

One boundary component turns bytes, lines, or JSON into trusted values; later stages remain simpler.

## Context in which it applies

Applies when a pipeline crosses from open external data into domain operations.

## Counterexample or boundary

A pipeline that intentionally treats each line as opaque text needs no richer domain parse.

## Worked example

**Starting condition:** Composable external formats require a parser stage before focused domain transformations can rely on their structure.

**Decision after applying both principles:** One boundary component turns bytes, lines, or JSON into trusted values; later stages remain simpler.

**Boundary check:** A pipeline that intentionally treats each line as opaque text needs no richer domain parse.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

One boundary component turns bytes, lines, or JSON into trusted values; later stages remain simpler.

## Evidence

Sources: I007; I016. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: At an open pipeline boundary, parsing must precede trusted domain transformation; an intentionally opaque text stage is a concrete case where the sequence does not apply.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. At an open pipeline boundary, parsing must precede trusted domain transformation; an intentionally opaque text stage is a concrete case where the sequence does not apply.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
