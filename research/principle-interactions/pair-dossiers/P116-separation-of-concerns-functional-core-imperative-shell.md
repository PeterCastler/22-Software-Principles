# Separation of Concerns ↔ Functional Core, Imperative Shell

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Functional Core, Imperative Shell governs placement of deterministic decisions and effects.

## Interaction mechanism

The core/shell pattern instantiates separation by isolating deterministic decisions from external effects.

## Material consequence

Policy can be tested with values while the shell owns I/O, retries, and operational failure handling.

## Context in which it applies

Applies when a workflow mixes substantial domain decisions with effects.

## Counterexample or boundary

A tiny effect-only adapter has no meaningful pure core to extract.

## Worked example

**Starting condition:** The core/shell pattern instantiates separation by isolating deterministic decisions from external effects.

**Decision after applying both principles:** Policy can be tested with values while the shell owns I/O, retries, and operational failure handling.

**Boundary check:** A tiny effect-only adapter has no meaningful pure core to extract.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Policy can be tested with values while the shell owns I/O, retries, and operational failure handling.

## Evidence

Sources: I012; S013. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Functional Core, Imperative Shell is a specific instance of separating decisions from effects, not something independently enabled by generic separation. The pair therefore reinforces the same boundary.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Reinforcement / Convergent**. Functional Core, Imperative Shell is a specific instance of separating decisions from effects, not something independently enabled by generic separation. The pair therefore reinforces the same boundary.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
