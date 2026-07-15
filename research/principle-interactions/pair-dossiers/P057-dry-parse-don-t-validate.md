# DRY ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: Reinforcement  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: DRY governs authority for changing knowledge; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

Parsing once creates one boundary authority for structural facts instead of repeating validators throughout the domain.

## Material consequence

Downstream functions accept the trusted value and redundant structural checks are removed.

## Context in which it applies

Applies when the same stable input invariant is checked at several internal call sites.

## Counterexample or boundary

Authorization can change after parsing and remains a use-time check rather than duplicated parsing knowledge.

## Worked example

**Starting condition:** Parsing once creates one boundary authority for structural facts instead of repeating validators throughout the domain.

**Decision after applying both principles:** Downstream functions accept the trusted value and redundant structural checks are removed.

**Boundary check:** Authorization can change after parsing and remains a use-time check rather than duplicated parsing knowledge.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Downstream functions accept the trusted value and redundant structural checks are removed.

## Evidence

Sources: I007; S005. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I007 explicitly contrasts shotgun repeated validation with one parsing boundary that preserves proof, directly supporting removal of duplicate structural checks.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I007 explicitly contrasts shotgun repeated validation with one parsing boundary that preserves proof, directly supporting removal of duplicate structural checks.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
