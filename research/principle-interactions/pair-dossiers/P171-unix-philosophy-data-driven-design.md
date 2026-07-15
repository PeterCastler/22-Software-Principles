# Unix Philosophy ↔ Data-Driven Design

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: Unix Philosophy governs component scope and composition interface; Data-Driven Design governs representation of regular variation as data or control flow.

## Interaction mechanism

Stable data interfaces let focused tools operate through one general algorithm rather than embedding a flag and branch for every case.

## Material consequence

Behavior variation moves into inspectable data consumable by several composable stages.

## Context in which it applies

Applies when components share a standard representation and cases are regular.

## Counterexample or boundary

A hidden callback language inside configuration undermines simple composable interfaces.

## Worked example

**Starting condition:** Stable data interfaces let focused tools operate through one general algorithm rather than embedding a flag and branch for every case.

**Decision after applying both principles:** Behavior variation moves into inspectable data consumable by several composable stages.

**Boundary check:** A hidden callback language inside configuration undermines simple composable interfaces.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Behavior variation moves into inspectable data consumable by several composable stages.

## Evidence

Sources: I015; I016. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I015 is an explicit Data-Driven Programming chapter within the Unix design synthesis and I016 names the Rule of Representation, satisfying Direct interaction evidence.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Independence / reject**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I015 is an explicit Data-Driven Programming chapter within the Unix design synthesis and I016 names the Rule of Representation, satisfying Direct interaction evidence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
