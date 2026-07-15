# Separation of Concerns ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: Complementary  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

Separating policy from infrastructure identifies the boundary; inversion makes the detail depend on the policy-owned contract.

## Material consequence

Vendor types stay outside and the core states only the capability it needs.

## Context in which it applies

Applies when stable policy and volatile detail have distinct change reasons.

## Counterexample or boundary

A stable local algorithm is not an infrastructure concern requiring an inverted interface.

## Worked example

**Starting condition:** Separating policy from infrastructure identifies the boundary; inversion makes the detail depend on the policy-owned contract.

**Decision after applying both principles:** Vendor types stay outside and the core states only the capability it needs.

**Boundary check:** A stable local algorithm is not an infrastructure concern requiring an inverted interface.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Vendor types stay outside and the core states only the capability it needs.

## Evidence

Sources: I008; S013; S031. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I008 explicitly moves from separation by responsibility to DIP as the correction for inward policy dependence, establishing the boundary and dependency-direction interaction directly.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I008 explicitly moves from separation by responsibility to DIP as the correction for inward policy dependence, establishing the boundary and dependency-direction interaction directly.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
