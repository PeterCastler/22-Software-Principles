# Data-Driven Design ↔ Make Illegal States Unrepresentable

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: Reinforcement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Data-Driven Design governs representation of regular variation as data or control flow; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A table can own the valid key set and derive a precise type, removing unknown-key states and duplicated enums.

## Material consequence

Construction validates rows and trusted lookups become exhaustive over the table-derived keys.

## Context in which it applies

Applies when the table is the authoritative finite case set.

## Counterexample or boundary

User-defined runtime keys cannot be made a closed compile-time union and still require error handling.

## Worked example

**Starting condition:** A table can own the valid key set and derive a precise type, removing unknown-key states and duplicated enums.

**Decision after applying both principles:** Construction validates rows and trusted lookups become exhaustive over the table-derived keys.

**Boundary check:** User-defined runtime keys cannot be made a closed compile-time union and still require error handling.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Construction validates rows and trusted lookups become exhaustive over the table-derived keys.

## Evidence

Sources: I007; I015; S035. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: When a table is the authoritative finite case set, derived precise keys can remove unknown-key states and duplicated enums; user-defined runtime keys defeat closure.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. When a table is the authoritative finite case set, derived precise keys can remove unknown-key states and duplicated enums; user-defined runtime keys defeat closure.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
