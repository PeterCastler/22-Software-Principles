# Dead Code Elimination ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: Enablement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dead Code Elimination governs liveness within the supported system boundary; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

Once every entry path parses to a trusted value, downstream structural validation can become unreachable or unobservable.

## Material consequence

The team verifies there is no raw bypass and removes the newly dead validation path.

## Context in which it applies

Applies when one parser dominates all supported calls into the trusted domain.

## Counterexample or boundary

A public API that still accepts the raw type keeps its validation live.

## Worked example

**Starting condition:** Once every entry path parses to a trusted value, downstream structural validation can become unreachable or unobservable.

**Decision after applying both principles:** The team verifies there is no raw bypass and removes the newly dead validation path.

**Boundary check:** A public API that still accepts the raw type keeps its validation live.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The team verifies there is no raw bypass and removes the newly dead validation path.

## Evidence

Sources: S027; I007. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: When every entry path parses into a trusted type, downstream malformed-structure branches can become unreachable; any raw public bypass defeats the sequence.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. When every entry path parses into a trusted type, downstream malformed-structure branches can become unreachable; any raw public bypass defeats the sequence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
