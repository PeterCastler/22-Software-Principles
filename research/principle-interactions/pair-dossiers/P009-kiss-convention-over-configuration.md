# KISS ↔ Convention over Configuration

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: Reinforcement; Tension  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Convention over Configuration governs routine defaults versus explicit exceptions.

## Interaction mechanism

A discoverable convention removes repetitive configuration, while KISS prevents convention from becoming hidden magic or a complex precedence system.

## Material consequence

The common path uses one predictable default and only real exceptions remain explicit.

## Context in which it applies

Applies when most instances make the same routine choice.

## Counterexample or boundary

When exceptions dominate or policy is important, explicit configuration is simpler than inference.

## Worked example

**Starting condition:** A discoverable convention removes repetitive configuration, while KISS prevents convention from becoming hidden magic or a complex precedence system.

**Decision after applying both principles:** The common path uses one predictable default and only real exceptions remain explicit.

**Boundary check:** When exceptions dominate or policy is important, explicit configuration is simpler than inference.

## Resolution procedure

Use convention only for a stable, dominant, discoverable common case. Keep significant policy and real exceptions explicit. If the convention requires multiple precedence levels or most callers override it, replace the inference with direct configuration.

## Combined instruction

The common path uses one predictable default and only real exceptions remain explicit.

## Evidence

Sources: I019; S001. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Convention removes routine configuration while KISS limits hidden discovery and exception precedence; the proposed moderation and exception-dominance boundary are operational.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Moderation / Convergent**. Convention removes routine configuration while KISS limits hidden discovery and exception precedence; the proposed moderation and exception-dominance boundary are operational.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
