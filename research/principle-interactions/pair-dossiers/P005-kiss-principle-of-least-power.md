# KISS ↔ Principle of Least Power

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Principle of Least Power governs expressive power of the chosen mechanism.

## Interaction mechanism

Choosing a less expressive adequate mechanism removes possible behaviors and side effects from the design KISS asks maintainers to understand.

## Material consequence

A static mapping, schema, native element, or query can replace a callback, script, or plugin system.

## Context in which it applies

Applies when the complete requirement fits a constrained mechanism without contortion.

## Counterexample or boundary

A stateful recovery workflow may be clearer as ordinary code than as an overgrown declarative language.

## Worked example

**Starting condition:** Choosing a less expressive adequate mechanism removes possible behaviors and side effects from the design KISS asks maintainers to understand.

**Decision after applying both principles:** A static mapping, schema, native element, or query can replace a callback, script, or plugin system.

**Boundary check:** A stateful recovery workflow may be clearer as ordinary code than as an overgrown declarative language.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A static mapping, schema, native element, or query can replace a callback, script, or plugin system.

## Evidence

Sources: S001; S011; I006. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Less expressive adequate mechanisms remove possible behavior and analysis burden from the KISS complexity budget; an overgrown declarative workaround is a valid adequacy counterexample.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Less expressive adequate mechanisms remove possible behavior and analysis burden from the KISS complexity budget; an overgrown declarative workaround is a valid adequacy counterexample.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
