# Composition over Inheritance ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Composition over Inheritance governs reuse and variation mechanism; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

Composition can create deep collaborator graphs; Law of Demeter prevents consumers from depending on the assembly's internal chain.

## Material consequence

The composer exposes a cohesive capability and keeps nested collaborators private.

## Context in which it applies

Applies when a composed object graph would otherwise be navigated by callers.

## Counterexample or boundary

A transparent pipeline of returned immutable values is not harmful graph navigation.

## Worked example

**Starting condition:** Composition can create deep collaborator graphs; Law of Demeter prevents consumers from depending on the assembly's internal chain.

**Decision after applying both principles:** The composer exposes a cohesive capability and keeps nested collaborators private.

**Boundary check:** A transparent pipeline of returned immutable values is not harmful graph navigation.

## Resolution procedure

Use composition for an observed variation axis, inject or store the immediate capability, and avoid navigation through the collaborator. If delegation only creates a train wreck around a fixed relationship, retain the simpler direct structure.

## Combined instruction

The composer exposes a cohesive capability and keeps nested collaborators private.

## Evidence

Sources: I011; S041; S042. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Composition does not pressure callers to expose or traverse the collaborator graph, so no genuine Tension exists. Demeter instead moderates how a composed object exposes its assembly.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Moderation / Convergent**. Composition does not pressure callers to expose or traverse the collaborator graph, so no genuine Tension exists. Demeter instead moderates how a composed object exposes its assembly.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
