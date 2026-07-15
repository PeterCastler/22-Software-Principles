# Unix Philosophy ↔ Refactoring Toward Primitives

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Unix Philosophy governs component scope and composition interface; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

The Unix emphasis on composing existing focused tools makes a reliable platform utility a preferred replacement for a monolithic custom feature.

## Material consequence

A stage is implemented with a standard tool or format and can still be replaced independently.

## Context in which it applies

Applies when existing tools handle the input contract and error semantics.

## Counterexample or boundary

An ad hoc `awk` split is not adequate for CSV fields containing quotes and newlines.

## Worked example

**Starting condition:** The Unix emphasis on composing existing focused tools makes a reliable platform utility a preferred replacement for a monolithic custom feature.

**Decision after applying both principles:** A stage is implemented with a standard tool or format and can still be replaced independently.

**Boundary check:** An ad hoc `awk` split is not adequate for CSV fields containing quotes and newlines.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A stage is implemented with a standard tool or format and can still be replaced independently.

## Evidence

Sources: I013; I016. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Unix's explicit reuse-and-composition pressure supplies candidate existing capabilities, while primitive refactoring verifies contract fit and removes custom machinery.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Unix's explicit reuse-and-composition pressure supplies candidate existing capabilities, while primitive refactoring verifies contract fit and removes custom machinery.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
