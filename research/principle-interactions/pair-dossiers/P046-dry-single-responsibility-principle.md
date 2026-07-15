# DRY ↔ Single Responsibility Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: DRY governs authority for changing knowledge; Single Responsibility Principle governs module cohesion around reasons for change.

## Interaction mechanism

SRP's reasons-for-change test determines whether repeated code is one shared responsibility or two independent authorities.

## Material consequence

A deduplication is accepted only when all callers should change for the same actor and business reason.

## Context in which it applies

Applies when candidate copies sit in modules with possibly different responsible actors.

## Counterexample or boundary

Identical age and page-size constants remain separate because their actors and change reasons differ.

## Worked example

**Starting condition:** SRP's reasons-for-change test determines whether repeated code is one shared responsibility or two independent authorities.

**Decision after applying both principles:** A deduplication is accepted only when all callers should change for the same actor and business reason.

**Boundary check:** Identical age and page-size constants remain separate because their actors and change reasons differ.

## Resolution procedure

Identify the actor and reason for change before extracting. Share the knowledge only when the callers answer to the same actor; retain local duplication when their policies can diverge independently.

## Combined instruction

A deduplication is accepted only when all callers should change for the same actor and business reason.

## Evidence

Sources: I002; S005; S015. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: SRP's actor and reason-for-change test limits when DRY may create an authority. Because DRY already excludes independently owned facts, the relation is moderation, not genuine Tension.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Moderation / Convergent**. SRP's actor and reason-for-change test limits when DRY may create an authority. Because DRY already excludes independently owned facts, the relation is moderation, not genuine Tension.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
