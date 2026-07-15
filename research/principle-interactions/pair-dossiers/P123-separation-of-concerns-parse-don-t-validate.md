# Separation of Concerns ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

A parsing boundary separates untrusted transport representation from trusted domain decisions and supplies the value crossing that boundary.

## Material consequence

Effects decode and parse before domain behavior, which no longer accepts raw request or SDK types.

## Context in which it applies

Applies when raw external data would otherwise leak into domain logic.

## Counterexample or boundary

Internal values produced entirely inside a trusted module need no redundant parsing layer.

## Worked example

**Starting condition:** A parsing boundary separates untrusted transport representation from trusted domain decisions and supplies the value crossing that boundary.

**Decision after applying both principles:** Effects decode and parse before domain behavior, which no longer accepts raw request or SDK types.

**Boundary check:** Internal values produced entirely inside a trusted module need no redundant parsing layer.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Effects decode and parse before domain behavior, which no longer accepts raw request or SDK types.

## Evidence

Sources: S013; I007. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Parsing creates and preserves a raw-to-trusted concern boundary, reinforcing separation. Separation of Concerns itself does not impose the proposed parse-before-domain sequence.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Reinforcement / Convergent**. Parsing creates and preserves a raw-to-trusted concern boundary, reinforcing separation. Separation of Concerns itself does not impose the proposed parse-before-domain sequence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
