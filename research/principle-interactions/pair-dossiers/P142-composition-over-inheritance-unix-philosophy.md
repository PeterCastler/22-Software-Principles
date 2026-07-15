# Composition over Inheritance ↔ Unix Philosophy

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Composition over Inheritance governs reuse and variation mechanism; Unix Philosophy governs component scope and composition interface.

## Interaction mechanism

Both build larger behavior by combining replaceable focused parts rather than enlarging one hierarchy or tool.

## Material consequence

Variation is expressed as small ordinary functions or components joined through stable values.

## Context in which it applies

Applies when several focused behaviors must be combined in different ways.

## Counterexample or boundary

Splitting a cohesive in-process algorithm into processes adds serialization and failure cost.

## Worked example

**Starting condition:** Both build larger behavior by combining replaceable focused parts rather than enlarging one hierarchy or tool.

**Decision after applying both principles:** Variation is expressed as small ordinary functions or components joined through stable values.

**Boundary check:** Splitting a cohesive in-process algorithm into processes adds serialization and failure cost.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Variation is expressed as small ordinary functions or components joined through stable values.

## Evidence

Sources: I011; I016. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Unix composition of focused tools and composition of focused behavior share an operational assembly surface, with process fragmentation serving as a material counterexample.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Unix composition of focused tools and composition of focused behavior share an operational assembly surface, with process fragmentation serving as a material counterexample.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
