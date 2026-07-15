# Parse, Don't Validate ↔ Tell, Don't Ask

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Parse, Don't Validate governs conversion of raw input into trusted domain values; Tell, Don't Ask governs ownership of state-dependent decisions and transitions.

## Interaction mechanism

Parsing establishes a trusted command value before Tell, Don't Ask hands it to the component that owns the stateful invariant.

## Material consequence

The boundary rejects malformed input; the domain operation then decides contextual acceptance without rechecking structure.

## Context in which it applies

Applies when an external request triggers a state-dependent command.

## Counterexample or boundary

A pure reporting query may use a parsed filter without issuing any domain command.

## Worked example

**Starting condition:** Parsing establishes a trusted command value before Tell, Don't Ask hands it to the component that owns the stateful invariant.

**Decision after applying both principles:** The boundary rejects malformed input; the domain operation then decides contextual acceptance without rechecking structure.

**Boundary check:** A pure reporting query may use a parsed filter without issuing any domain command.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The boundary rejects malformed input; the domain operation then decides contextual acceptance without rechecking structure.

## Evidence

Sources: I007; S039. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Parsing establishes structural trust before the state owner evaluates contextual validity, with reporting queries correctly stopping the command sequence.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. Parsing establishes structural trust before the state owner evaluates contextual validity, with reporting queries correctly stopping the command sequence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
