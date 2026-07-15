# KISS ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: Moderation  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

A policy-owned boundary can simplify change around a volatile detail, but unjustified interfaces and containers add indirection.

## Material consequence

The implementation either uses a minimal domain-shaped function boundary or keeps a stable detail direct.

## Context in which it applies

Applies when policy is coupled to a demonstrably volatile or external detail.

## Counterexample or boundary

A fixed internal helper with no boundary role is simpler when called directly.

## Worked example

**Starting condition:** A policy-owned boundary can simplify change around a volatile detail, but unjustified interfaces and containers add indirection.

**Decision after applying both principles:** The implementation either uses a minimal domain-shaped function boundary or keeps a stable detail direct.

**Boundary check:** A fixed internal helper with no boundary role is simpler when called directly.

## Resolution procedure

First establish a present policy/volatility boundary. If none exists, keep the dependency direct. If it exists, introduce the narrowest policy-owned contract and do not add a container or provider hierarchy unless composition actually requires it.

## Combined instruction

The implementation either uses a minimal domain-shaped function boundary or keeps a stable detail direct.

## Evidence

Sources: I010; S001. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution is sound: establish real volatility first, then use the narrowest policy-owned boundary; otherwise keep the stable detail direct.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution is sound: establish real volatility first, then use the narrowest policy-owned boundary; otherwise keep the stable detail direct.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
