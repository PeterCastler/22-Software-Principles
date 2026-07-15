# DRY ↔ Separation of Concerns

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: DRY governs authority for changing knowledge; Separation of Concerns governs logical boundaries between kinds of decisions.

## Interaction mechanism

DRY pulls one fact toward one authority, while separation keeps independently changing knowledge apart even when implementations look the same.

## Material consequence

The design centralizes only cross-boundary facts that truly share ownership and leaves coincidental duplication local.

## Context in which it applies

Applies when similar code appears in concerns owned by different actors or rates of change.

## Counterexample or boundary

One schema consumed by UI and API is shared knowledge and may legitimately generate both representations.

## Worked example

**Starting condition:** DRY pulls one fact toward one authority, while separation keeps independently changing knowledge apart even when implementations look the same.

**Decision after applying both principles:** The design centralizes only cross-boundary facts that truly share ownership and leaves coincidental duplication local.

**Boundary check:** One schema consumed by UI and API is shared knowledge and may legitimately generate both representations.

## Resolution procedure

Use reason-for-change as the authority test. Centralize a fact only when all consumers should change together; otherwise keep separately owned representations even when their current text matches.

## Combined instruction

The design centralizes only cross-boundary facts that truly share ownership and leaves coincidental duplication local.

## Evidence

Sources: I002; S005; S013. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Correctly applied DRY centralizes one owned fact while Separation of Concerns separates facts with independent ownership; those tests partition cases rather than exert opposing pressures.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Complementary / Convergent**. Correctly applied DRY centralizes one owned fact while Separation of Concerns separates facts with independent ownership; those tests partition cases rather than exert opposing pressures.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
