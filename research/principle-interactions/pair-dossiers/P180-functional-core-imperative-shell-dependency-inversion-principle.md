# Functional Core, Imperative Shell ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Functional Core, Imperative Shell governs placement of deterministic decisions and effects; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

The shell supplies effectful details through policy-shaped capabilities, letting the core avoid vendor dependencies.

## Material consequence

The application edge composes adapters while deterministic policy accepts only domain values or narrow functions.

## Context in which it applies

Applies when important policy currently imports or constructs an external effect detail.

## Counterexample or boundary

A pure calculation with no external detail needs neither an adapter nor inversion.

## Worked example

**Starting condition:** The shell supplies effectful details through policy-shaped capabilities, letting the core avoid vendor dependencies.

**Decision after applying both principles:** The application edge composes adapters while deterministic policy accepts only domain values or narrow functions.

**Boundary check:** A pure calculation with no external detail needs neither an adapter nor inversion.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The application edge composes adapters while deterministic policy accepts only domain values or narrow functions.

## Evidence

Sources: I008; I010; I012. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Core/shell placement separates policy from effects, while DIP shapes and points the capability boundary; pure calculations without effects correctly need neither.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **accept**; recommendation: **Complementary / Convergent**. Core/shell placement separates policy from effects, while DIP shapes and points the capability boundary; pure calculations without effects correctly need neither.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
