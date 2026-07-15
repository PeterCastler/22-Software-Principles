# KISS ↔ DRY

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; DRY governs authority for changing knowledge.

## Interaction mechanism

DRY can remove coordinated authorities, but KISS rejects a shared abstraction when its indirection costs more than the duplication it removes.

## Material consequence

The reviewer must choose between a narrow authority and intentionally separate local copies instead of deduplicating by appearance.

## Context in which it applies

Applies when several representations may encode one changing fact, but extraction adds a new abstraction.

## Counterexample or boundary

Two identical literals owned by independent policies should remain separate despite textual duplication.

## Worked example

**Starting condition:** DRY can remove coordinated authorities, but KISS rejects a shared abstraction when its indirection costs more than the duplication it removes.

**Decision after applying both principles:** The reviewer must choose between a narrow authority and intentionally separate local copies instead of deduplicating by appearance.

**Boundary check:** Two identical literals owned by independent policies should remain separate despite textual duplication.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The reviewer must choose between a narrow authority and intentionally separate local copies instead of deduplicating by appearance.

## Evidence

Sources: I001; I003; S005. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: I001 and I003 explicitly place duplication inside simple-design criteria, but neither directly establishes the dossier's abstraction-cost moderation; the mechanism is still supported by converging simplicity and DRY evidence.

## Independent review

Blind primary screen: **Moderation / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Moderation / Convergent**. I001 and I003 explicitly place duplication inside simple-design criteria, but neither directly establishes the dossier's abstraction-cost moderation; the mechanism is still supported by converging simplicity and DRY evidence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
