# KISS ↔ YAGNI

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; YAGNI governs timing of capability and extensibility.

## Interaction mechanism

Deferring unneeded capability prevents the extra mechanisms whose lifecycle cost KISS would otherwise have to remove.

## Material consequence

A design review can reject an option, extension point, or compatibility path before it becomes carrying complexity.

## Context in which it applies

Applies when a proposed mechanism exists only for a presumed future consumer.

## Counterexample or boundary

A current accessibility or recovery requirement is not speculative, even if it adds substantial structure.

## Worked example

**Starting condition:** Deferring unneeded capability prevents the extra mechanisms whose lifecycle cost KISS would otherwise have to remove.

**Decision after applying both principles:** A design review can reject an option, extension point, or compatibility path before it becomes carrying complexity.

**Boundary check:** A current accessibility or recovery requirement is not speculative, even if it adds substantial structure.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A design review can reject an option, extension point, or compatibility path before it becomes carrying complexity.

## Evidence

Sources: I001; S003. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I001 explicitly treats YAGNI as simple design and explains that deferred capability avoids current complexity; the current-requirement counterexample correctly stops the claim.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Direct**. I001 explicitly treats YAGNI as simple design and explains that deferred capability avoids current complexity; the current-requirement counterexample correctly stops the claim.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
