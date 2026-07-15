# Rule of Three ↔ Composition over Inheritance

Assessment status: Final publish; validated for freeze  
Primary classification: Sequencing  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Rule of Three governs timing and scope of abstraction; Composition over Inheritance governs reuse and variation mechanism.

## Interaction mechanism

Multiple concrete variants reveal independent axes of behavior and whether composition will reduce subclass combinations.

## Material consequence

The team keeps early behavior direct, then composes the smallest stable varying functions when the axes are observed.

## Context in which it applies

Applies when a strategy hierarchy is proposed from a single implementation.

## Counterexample or boundary

A framework-mandated composition point is already a stable external contract.

## Worked example

**Starting condition:** Multiple concrete variants reveal independent axes of behavior and whether composition will reduce subclass combinations.

**Decision after applying both principles:** The team keeps early behavior direct, then composes the smallest stable varying functions when the axes are observed.

**Boundary check:** A framework-mandated composition point is already a stable external contract.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The team keeps early behavior direct, then composes the smallest stable varying functions when the axes are observed.

## Evidence

Sources: I004; I011. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Concrete variants reveal independent axes before composition is introduced, yielding a specific sequence and a subclass-combination consequence; an external composition contract is a valid exception.

## Independent review

Blind primary screen: **Sequencing / uncertain**. Blind independent screen: **Sequencing / uncertain**.

Adversarial verdict: **accept**; recommendation: **Sequencing / Convergent**. Concrete variants reveal independent axes before composition is introduced, yielding a specific sequence and a subclass-combination consequence; an external composition contract is a valid exception.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
