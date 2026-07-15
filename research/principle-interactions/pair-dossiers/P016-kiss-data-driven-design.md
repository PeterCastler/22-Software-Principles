# KISS ↔ Data-Driven Design

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: Tension  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Data-Driven Design governs representation of regular variation as data or control flow.

## Interaction mechanism

A table can simplify regular branches, but a generic interpreter or callback-filled configuration can hide more complexity than direct control flow.

## Material consequence

The reviewer chooses a typed lookup only for regular cases and leaves irregular algorithms in code.

## Context in which it applies

Applies when cases share one algorithm and vary along inspectable dimensions.

## Counterexample or boundary

Three unrelated algorithms do not become simpler when stored as callbacks in a table.

## Worked example

**Starting condition:** A table can simplify regular branches, but a generic interpreter or callback-filled configuration can hide more complexity than direct control flow.

**Decision after applying both principles:** The reviewer chooses a typed lookup only for regular cases and leaves irregular algorithms in code.

**Boundary check:** Three unrelated algorithms do not become simpler when stored as callbacks in a table.

## Resolution procedure

First test whether the cases share one stable algorithm and vary along regular dimensions. If yes, use one typed table and direct interpreter. If not, retain explicit control flow; do not resolve irregularity by adding callbacks, a rule engine, or an embedded language.

## Combined instruction

The reviewer chooses a typed lookup only for regular cases and leaves irregular algorithms in code.

## Evidence

Sources: I015; S001. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: KISS materially moderates the data-versus-control-flow choice by rejecting both callback-filled tables and sprawling regular branches; irregular algorithms stop the interaction.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Moderation / Convergent**. KISS materially moderates the data-versus-control-flow choice by rejecting both callback-filled tables and sprawling regular branches; irregular algorithms stop the interaction.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
