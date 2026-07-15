# Make Illegal States Unrepresentable ↔ Law of Demeter

Assessment status: Rejected after targeted research  
Primary classification: Independence  
Secondary classifications: None  
Evidence grade: Unsupported  
Confidence: medium

## Shared decision surface

Causally connected decisions: Make Illegal States Unrepresentable governs representation and enforcement of stable invariants; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

The screened hypothesis was: Rejected hypothesis: Hiding mutable internals and exposing stable capabilities prevents callers from bypassing constructors or assembling invalid nested state. Targeted research did not support it as a general interaction beyond project-specific circumstances.

## Material consequence

No general material consequence was established. The candidate remains useful only as a warning not to infer a relationship from thematic similarity.

## Context in which it applies

A project-specific interaction may exist, but no general mechanism survived the evidence and counterexample tests.

## Counterexample or boundary

Transparent immutable sum-type data may be safely pattern-matched by its legitimate consumer.

## Worked example

**Candidate hypothesis:** Hiding mutable internals and exposing stable capabilities prevents callers from bypassing constructors or assembling invalid nested state.

**Observed boundary:** Transparent immutable sum-type data may be safely pattern-matched by its legitimate consumer.

Because the result depends on additional project facts not present in either canonical profile, the example does not generalize into a publishable relationship.

## Resolution procedure

Not applicable: no publishable Tension or Conflict was established.

## Combined instruction

None. Apply each principle from its own canonical preconditions; do not infer a combined rule from this rejected pair.

## Evidence

Evidence grade: **Unsupported**. The candidate arose from at least one operational screen, but the targeted source set did not establish that applying one principle generally changes the cost, risk, timing, or outcome of the other. Thematic similarity is insufficient. See the [source register](../source-register.md).

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Independence / reject**. The research pass rejected the hypothesis rather than averaging the two screens.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
