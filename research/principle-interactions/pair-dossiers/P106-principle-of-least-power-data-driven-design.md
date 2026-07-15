# Principle of Least Power ↔ Data-Driven Design

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Principle of Least Power governs expressive power of the chosen mechanism; Data-Driven Design governs representation of regular variation as data or control flow.

## Interaction mechanism

Moving regular variation from executable branches into validated data reduces expressive power while keeping the decision space visible.

## Material consequence

A typed table replaces repeated control flow only where one algorithm interprets all rows.

## Context in which it applies

Applies when variation is regular and can be represented without arbitrary callbacks.

## Counterexample or boundary

A callback-filled rules table is still executable behavior and gains no least-power advantage.

## Worked example

**Starting condition:** Moving regular variation from executable branches into validated data reduces expressive power while keeping the decision space visible.

**Decision after applying both principles:** A typed table replaces repeated control flow only where one algorithm interprets all rows.

**Boundary check:** A callback-filled rules table is still executable behavior and gains no least-power advantage.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A typed table replaces repeated control flow only where one algorithm interprets all rows.

## Evidence

Sources: S011; I005; I015. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: I005 directly applies Least Power to declarative constraint choices, but it does not discuss regular case variation as Data-Driven Design. Data representation reinforces lower expressiveness; it does not enable the principle.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Reinforcement / Convergent**. I005 directly applies Least Power to declarative constraint choices, but it does not discuss regular case variation as Data-Driven Design. Data representation reinforces lower expressiveness; it does not enable the principle.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
