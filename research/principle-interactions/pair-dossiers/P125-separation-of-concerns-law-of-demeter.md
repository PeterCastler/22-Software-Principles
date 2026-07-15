# Separation of Concerns ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

A real concern boundary is undermined when callers navigate its internal object graph; meaningful near-neighbor operations preserve the separation.

## Material consequence

Callers depend on the boundary's capability or plain boundary value rather than nested implementation structure.

## Context in which it applies

Applies when one concern reaches through another's internal ownership chain.

## Counterexample or boundary

A renderer traversing a transparent immutable view model is not crossing a hidden concern boundary.

## Worked example

**Starting condition:** A real concern boundary is undermined when callers navigate its internal object graph; meaningful near-neighbor operations preserve the separation.

**Decision after applying both principles:** Callers depend on the boundary's capability or plain boundary value rather than nested implementation structure.

**Boundary check:** A renderer traversing a transparent immutable view model is not crossing a hidden concern boundary.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Callers depend on the boundary's capability or plain boundary value rather than nested implementation structure.

## Evidence

Sources: S013; S041. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Object-graph navigation can bypass a real concern boundary, and a meaningful near-neighbor capability materially restores it; transparent immutable view data is a valid boundary.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Object-graph navigation can bypass a real concern boundary, and a meaningful near-neighbor capability materially restores it; transparent immutable view data is a valid boundary.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
