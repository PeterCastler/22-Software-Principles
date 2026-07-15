# Single Responsibility Principle ↔ Unix Philosophy

Assessment status: Final publish; validated for freeze  
Primary classification: Overlap  
Secondary classifications: Reinforcement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Single Responsibility Principle governs module cohesion around reasons for change; Unix Philosophy governs component scope and composition interface.

## Interaction mechanism

Both seek cohesive units, but SRP tests reasons for change while Unix Philosophy additionally requires composable interfaces.

## Material consequence

A component keeps one recognizable purpose and emits output usable without importing its internal responsibilities.

## Context in which it applies

Applies when component scope is being chosen around coherent work.

## Counterexample or boundary

One cohesive compiler performs many internal operations without violating either principle.

## Worked example

**Starting condition:** Both seek cohesive units, but SRP tests reasons for change while Unix Philosophy additionally requires composable interfaces.

**Decision after applying both principles:** A component keeps one recognizable purpose and emits output usable without importing its internal responsibilities.

**Boundary check:** One cohesive compiler performs many internal operations without violating either principle.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A component keeps one recognizable purpose and emits output usable without importing its internal responsibilities.

## Evidence

Sources: S015; I016. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Both select cohesive component scope but use distinct tests, with Unix additionally requiring composability; a cohesive compiler with many internal operations correctly limits literal one-job readings.

## Independent review

Blind primary screen: **Overlap / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Overlap / Convergent**. Both select cohesive component scope but use distinct tests, with Unix additionally requiring composability; a cohesive compiler with many internal operations correctly limits literal one-job readings.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
