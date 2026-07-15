# Parse, Don't Validate ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Reasoned Inference  
Confidence: high

## Shared decision surface

Causally connected decisions: Parse, Don't Validate governs conversion of raw input into trusted domain values; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

Passing one parsed domain value avoids both raw-shape leakage and navigation through a request or SDK object graph.

## Material consequence

The caller extracts and parses the needed value at the boundary, then collaborators accept that value directly.

## Context in which it applies

Applies when domain code currently reaches through transport structures to retrieve weak input.

## Counterexample or boundary

A parser itself legitimately traverses the raw syntax tree it owns at the boundary.

## Worked example

**Starting condition:** Passing one parsed domain value avoids both raw-shape leakage and navigation through a request or SDK object graph.

**Decision after applying both principles:** The caller extracts and parses the needed value at the boundary, then collaborators accept that value directly.

**Boundary check:** A parser itself legitimately traverses the raw syntax tree it owns at the boundary.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The caller extracts and parses the needed value at the boundary, then collaborators accept that value directly.

## Evidence

Sources: I007; S041. See the [source register](../source-register.md). The final grade is **Reasoned Inference**: the operational profiles produce a falsifiable mechanism with a concrete counterexample, and the independent adversarial reviewer explicitly accepted publication at this lower grade.

Adversarial finding: The mechanism is plausible only when raw transport graph leakage and weak input coincide; I007 and the Demeter sources do not explicitly discuss their interaction, so Convergent overstates the evidence.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Complementary / Reasoned Inference**. The mechanism is plausible only when raw transport graph leakage and weak input coincide; I007 and the Demeter sources do not explicitly discuss their interaction, so Convergent overstates the evidence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
