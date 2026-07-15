# Functional Core, Imperative Shell ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Functional Core, Imperative Shell governs placement of deterministic decisions and effects; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

The imperative shell acquires and parses raw input before invoking a core whose signatures require trusted values.

## Material consequence

Parsing errors remain at the boundary and pure domain rules contain no transport casts or repeated structural checks.

## Context in which it applies

Applies when raw external input feeds deterministic domain decisions.

## Counterexample or boundary

A decision that depends on locked database state may need parsing and decision inside one transactional shell.

## Worked example

**Starting condition:** The imperative shell acquires and parses raw input before invoking a core whose signatures require trusted values.

**Decision after applying both principles:** Parsing errors remain at the boundary and pure domain rules contain no transport casts or repeated structural checks.

**Boundary check:** A decision that depends on locked database state may need parsing and decision inside one transactional shell.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Parsing errors remain at the boundary and pure domain rules contain no transport casts or repeated structural checks.

## Evidence

Sources: I007; I012. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The shell's acquisition of raw input and the core's trusted signature create a concrete parse-before-decision sequence; transactional state is a valid exception.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. The shell's acquisition of raw input and the core's trusted signature create a concrete parse-before-decision sequence; transactional state is a valid exception.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
