# KISS ↔ Separation of Concerns

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: Tension  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: KISS governs overall implementation and lifecycle complexity; Separation of Concerns governs logical boundaries between kinds of decisions.

## Interaction mechanism

A boundary can reduce entanglement but also adds concepts, navigation, and contracts; KISS requires the separation to repay that cost.

## Material consequence

The implementation uses the cheapest meaningful boundary and avoids forwarding layers or unnecessary services.

## Context in which it applies

Applies when concerns change independently, but several possible boundary strengths exist.

## Counterexample or boundary

Splitting one cohesive invariant across files increases complexity without independent change benefit.

## Worked example

**Starting condition:** A boundary can reduce entanglement but also adds concepts, navigation, and contracts; KISS requires the separation to repay that cost.

**Decision after applying both principles:** The implementation uses the cheapest meaningful boundary and avoids forwarding layers or unnecessary services.

**Boundary check:** Splitting one cohesive invariant across files increases complexity without independent change benefit.

## Resolution procedure

First prove that the concerns have independent reasons or rates of change. If they do not, keep the cohesive implementation together. If they do, introduce the cheapest boundary that isolates them, then remove forwarding layers whose only purpose is architectural symmetry.

## Combined instruction

The implementation uses the cheapest meaningful boundary and avoids forwarding layers or unnecessary services.

## Evidence

Sources: I002; I008; S013. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The boundary decision is shared and KISS materially limits separation strength to the cheapest boundary that repays integration cost; the cohesive-invariant counterexample is specific.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Moderation / Convergent**. The boundary decision is shared and KISS materially limits separation strength to the cheapest boundary that repays integration cost; the cohesive-invariant counterexample is specific.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
