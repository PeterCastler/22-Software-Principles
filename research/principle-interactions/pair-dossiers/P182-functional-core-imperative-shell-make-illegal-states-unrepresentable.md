# Functional Core, Imperative Shell ↔ Make Illegal States Unrepresentable

Assessment status: Rejected after adversarial review  
Primary classification: Independence  
Secondary classifications: None  
Evidence grade: Unsupported  
Confidence: high

## Shared decision surface

Causally connected decisions: Functional Core, Imperative Shell governs placement of deterministic decisions and effects; Make Illegal States Unrepresentable governs representation and enforcement of stable invariants.

## Interaction mechanism

A pure core benefits from precise input and output values because impossible cases disappear from deterministic decision logic.

## Material consequence

No pair-specific, context-independent implementation or review consequence survived adversarial review.

## Context in which it applies

Applies when stable domain invariants can be represented before the core runs.

## Counterexample or boundary

Concurrent balance availability cannot be frozen into the core's input without preserving a transaction.

## Worked example

**Starting condition:** A pure core benefits from precise input and output values because impossible cases disappear from deterministic decision logic.

**Decision after applying both principles:** The core pattern-matches exhaustively over valid variants and returns an explicit domain outcome.

**Boundary check:** Concurrent balance availability cannot be frozen into the core's input without preserving a transaction.

## Resolution procedure

Not applicable: adversarial review found no publishable Tension or Conflict.

## Combined instruction

None. Apply each principle from its own canonical preconditions; do not infer a combined rule from this rejected pair.

## Evidence

Evidence grade: **Unsupported**. Precise types benefit deterministic and imperative code alike; a pure core neither causes nor requires illegal-state exclusion. The dossier offers generic type-safety benefit rather than a pair-specific mechanism. See the [source register](../source-register.md) for the sources that were tested.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **reject**; recommendation: **Independence / Unsupported**. Precise types benefit deterministic and imperative code alike; a pure core neither causes nor requires illegal-state exclusion. The dossier offers generic type-safety benefit rather than a pair-specific mechanism.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
