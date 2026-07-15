# Separation of Concerns ↔ Unix Philosophy

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Unix Philosophy governs component scope and composition interface.

## Interaction mechanism

Focused components with stable composable interfaces are an operational form of separating coherent work while preserving recombination.

## Material consequence

A component exposes reusable data rather than absorbing every adjacent transformation.

## Context in which it applies

Applies when a workflow contains coherent stages that can exchange a stable representation.

## Counterexample or boundary

A transaction that must succeed atomically may be clearer and safer as one cohesive component.

## Worked example

**Starting condition:** Focused components with stable composable interfaces are an operational form of separating coherent work while preserving recombination.

**Decision after applying both principles:** A component exposes reusable data rather than absorbing every adjacent transformation.

**Boundary check:** A transaction that must succeed atomically may be clearer and safer as one cohesive component.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A component exposes reusable data rather than absorbing every adjacent transformation.

## Evidence

Sources: I016; S013. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I016 explicitly states the Unix Rule of Separation within the connected Unix design rules, so focused composable components directly operationalize separation.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Direct**. I016 explicitly states the Unix Rule of Separation within the connected Unix design rules, so focused composable components directly operationalize separation.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
