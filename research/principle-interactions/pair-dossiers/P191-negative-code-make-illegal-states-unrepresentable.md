# Negative Code ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Negative Code governs net removal of owned machinery while preserving contract; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A precise representation can make defensive branches, synchronized fields, and impossible-case tests unnecessary.

## Material consequence

After construction is controlled, the change removes only checks and state copies now proven impossible.

## Context in which it applies

Applies when many consumers defend against stable illegal combinations.

## Counterexample or boundary

Checks for current authorization remain live because the type cannot prove a mutable external fact.

## Worked example

**Starting condition:** A precise representation can make defensive branches, synchronized fields, and impossible-case tests unnecessary.

**Decision after applying both principles:** After construction is controlled, the change removes only checks and state copies now proven impossible.

**Boundary check:** Checks for current authorization remain live because the type cannot prove a mutable external fact.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

After construction is controlled, the change removes only checks and state copies now proven impossible.

## Evidence

Sources: I007; I020; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Controlled precise construction can make repeated impossible-state guards and synchronized fields removable; mutable authorization correctly remains live.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. Controlled precise construction can make repeated impossible-state guards and synchronized fields removable; mutable authorization correctly remains live.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
