# Dependency Inversion Principle ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Dependency Inversion Principle governs contract ownership and source-dependency direction; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

Both prevent policy from knowing low-level structure: DIP controls source direction and Law of Demeter controls graph navigation through the contract.

## Material consequence

The policy asks for a narrow domain capability rather than traversing an injected SDK or repository object.

## Context in which it applies

Applies when policy currently depends on nested structure owned by a volatile detail.

## Counterexample or boundary

An injected vendor interface still violates the mechanism if policy navigates vendor-specific response graphs.

## Worked example

**Starting condition:** Both prevent policy from knowing low-level structure: DIP controls source direction and Law of Demeter controls graph navigation through the contract.

**Decision after applying both principles:** The policy asks for a narrow domain capability rather than traversing an injected SDK or repository object.

**Boundary check:** An injected vendor interface still violates the mechanism if policy navigates vendor-specific response graphs.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The policy asks for a narrow domain capability rather than traversing an injected SDK or repository object.

## Evidence

Sources: I010; S041; S042. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: DIP controls source dependency while Demeter controls graph knowledge through the boundary, jointly preventing policy from traversing volatile detail structure.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. DIP controls source dependency while Demeter controls graph knowledge through the boundary, jointly preventing policy from traversing volatile detail structure.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
