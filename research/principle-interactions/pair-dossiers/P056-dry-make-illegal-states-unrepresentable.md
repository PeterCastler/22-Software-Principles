# DRY ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: Reinforcement  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: DRY governs authority for changing knowledge; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

Deriving dependent values instead of storing synchronized copies removes both duplicated authority and the illegal state in which copies disagree.

## Material consequence

The data model stores one source value and calculates its dependent flags, counts, or totals.

## Context in which it applies

Applies when multiple stored fields represent one derivable fact.

## Counterexample or boundary

Intentional denormalization for measured performance may require transactional synchronization rather than deletion.

## Worked example

**Starting condition:** Deriving dependent values instead of storing synchronized copies removes both duplicated authority and the illegal state in which copies disagree.

**Decision after applying both principles:** The data model stores one source value and calculates its dependent flags, counts, or totals.

**Boundary check:** Intentional denormalization for measured performance may require transactional synchronization rather than deletion.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The data model stores one source value and calculates its dependent flags, counts, or totals.

## Evidence

Sources: I007; S005; S035. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I007 explicitly states that duplicated mutable data creates the illegal out-of-sync state and recommends a single source of truth; Direct evidence and the denormalization boundary both hold.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I007 explicitly states that duplicated mutable data creates the illegal out-of-sync state and recommends a single source of truth; Direct evidence and the denormalization boundary both hold.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
