# Single Responsibility Principle ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Single Responsibility Principle governs module cohesion around reasons for change; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

SRP identifies policy and infrastructure as different responsibilities; DIP controls dependency direction across the resulting boundary.

## Material consequence

The policy module owns a narrow contract and the infrastructure module implements it.

## Context in which it applies

Applies when policy and volatile detail change for different actors or reasons.

## Counterexample or boundary

Splitting a stable local helper and adding an interface creates responsibilities that did not exist.

## Worked example

**Starting condition:** SRP identifies policy and infrastructure as different responsibilities; DIP controls dependency direction across the resulting boundary.

**Decision after applying both principles:** The policy module owns a narrow contract and the infrastructure module implements it.

**Boundary check:** Splitting a stable local helper and adding an interface creates responsibilities that did not exist.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The policy module owns a narrow contract and the infrastructure module implements it.

## Evidence

Sources: I008; I009; I010; S015; S031. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: I008 and I010 discuss responsibility decomposition and DIP together, but do not explicitly establish SRP's actor-based test as the cause of DIP direction. The complementary mechanism remains convergently supported.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Complementary / Convergent**. I008 and I010 discuss responsibility decomposition and DIP together, but do not explicitly establish SRP's actor-based test as the cause of DIP direction. The complementary mechanism remains convergently supported.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
