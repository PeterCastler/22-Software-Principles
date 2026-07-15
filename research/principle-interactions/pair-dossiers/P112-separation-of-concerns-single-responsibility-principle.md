# Separation of Concerns ↔ Single Responsibility Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Overlap  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Single Responsibility Principle governs module cohesion around reasons for change.

## Interaction mechanism

Both separate independently changing work; SRP sharpens the boundary test by identifying the actor or business reason for change.

## Material consequence

A module split is justified by distinct stakeholders rather than verbs or technical layers alone.

## Context in which it applies

Applies when a module mixes decisions with independent change reasons.

## Counterexample or boundary

Several operations for one cohesive pricing actor remain one responsibility despite different verbs.

## Worked example

**Starting condition:** Both separate independently changing work; SRP sharpens the boundary test by identifying the actor or business reason for change.

**Decision after applying both principles:** A module split is justified by distinct stakeholders rather than verbs or technical layers alone.

**Boundary check:** Several operations for one cohesive pricing actor remain one responsibility despite different verbs.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A module split is justified by distinct stakeholders rather than verbs or technical layers alone.

## Evidence

Sources: S013; S015; I002. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Both govern boundaries for independently changing work, while SRP narrows the test to actor or business reason; the cohesive multi-operation module properly limits the overlap.

## Independent review

Blind primary screen: **Overlap / uncertain**. Blind independent screen: **Overlap / uncertain**.

Adversarial verdict: **accept**; recommendation: **Overlap / Convergent**. Both govern boundaries for independently changing work, while SRP narrows the test to actor or business reason; the cohesive multi-operation module properly limits the overlap.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
