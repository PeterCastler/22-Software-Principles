# Separation of Concerns ↔ Composition over Inheritance

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Separation of Concerns governs logical boundaries between kinds of decisions; Composition over Inheritance governs reuse and variation mechanism.

## Interaction mechanism

Once independent variation axes are separated, composition can recombine them without subclassing every combination.

## Material consequence

Format, destination, filtering, or policy remain focused behaviors assembled at one explicit boundary.

## Context in which it applies

Applies when two or more behavior axes vary independently.

## Counterexample or boundary

If behavior never varies, separated strategy objects add wiring without enabling useful composition.

## Worked example

**Starting condition:** Once independent variation axes are separated, composition can recombine them without subclassing every combination.

**Decision after applying both principles:** Format, destination, filtering, or policy remain focused behaviors assembled at one explicit boundary.

**Boundary check:** If behavior never varies, separated strategy objects add wiring without enabling useful composition.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Format, destination, filtering, or policy remain focused behaviors assembled at one explicit boundary.

## Evidence

Sources: S013; I011. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Separating observed variation axes enables their recombination without subclass multiplication; fixed behavior is a concrete counterexample to adding strategies.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Convergent**. Separating observed variation axes enables their recombination without subclass multiplication; fixed behavior is a concrete counterexample to adding strategies.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
