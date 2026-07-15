# Single Responsibility Principle ↔ Tell, Don't Ask

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: Moderation  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Single Responsibility Principle governs module cohesion around reasons for change; Tell, Don't Ask governs ownership of state-dependent decisions and transitions.

## Interaction mechanism

Tell, Don't Ask pulls invariant behavior into its owner, while SRP limits that owner to behavior serving its cohesive actor.

## Material consequence

A domain object owns its state transition but not unrelated persistence, reporting, or cross-aggregate workflow.

## Context in which it applies

Applies when behavior can access the data but may serve a different responsibility.

## Counterexample or boundary

An invoice should own pricing invariants but need not own database storage or HTML rendering.

## Worked example

**Starting condition:** Tell, Don't Ask pulls invariant behavior into its owner, while SRP limits that owner to behavior serving its cohesive actor.

**Decision after applying both principles:** A domain object owns its state transition but not unrelated persistence, reporting, or cross-aggregate workflow.

**Boundary check:** An invoice should own pricing invariants but need not own database storage or HTML rendering.

## Resolution procedure

Let the actor/reason-for-change test establish the module boundary; within that boundary, place invariant-preserving behavior with its data. Split only behavior owned by a genuinely different actor.

## Combined instruction

A domain object owns its state transition but not unrelated persistence, reporting, or cross-aggregate workflow.

## Evidence

Sources: S015; S039. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution is sound: SRP sets the actor boundary and Tell, Don't Ask places only that actor's invariant behavior with the state, excluding storage and rendering.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution is sound: SRP sets the actor boundary and Tell, Don't Ask places only that actor's invariant behavior with the state, excluding storage and rendering.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
