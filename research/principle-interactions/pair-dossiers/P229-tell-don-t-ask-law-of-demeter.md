# Tell, Don't Ask ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Tell, Don't Ask governs ownership of state-dependent decisions and transitions; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

Both replace external knowledge of nested state with a meaningful operation on the nearest owner; Tell, Don't Ask focuses on decision ownership and Demeter on structural knowledge.

## Material consequence

A caller requests `withdraw` or `pay` rather than retrieving nested fields, deciding, and mutating them.

## Context in which it applies

Applies when a caller navigates another component's internals to enforce that component's invariant.

## Counterexample or boundary

A renderer reading a plain immutable address is a legitimate query and needs no forwarding command.

## Worked example

**Starting condition:** Both replace external knowledge of nested state with a meaningful operation on the nearest owner; Tell, Don't Ask focuses on decision ownership and Demeter on structural knowledge.

**Decision after applying both principles:** A caller requests `withdraw` or `pay` rather than retrieving nested fields, deciding, and mutating them.

**Boundary check:** A renderer reading a plain immutable address is a legitimate query and needs no forwarding command.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

A caller requests `withdraw` or `pay` rather than retrieving nested fields, deciding, and mutating them.

## Evidence

Sources: S039; S041; S042. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Both replace caller knowledge of nested mutable state with a meaningful nearest-owner operation, while legitimate rendering of immutable values is a clear counterexample.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Both replace caller knowledge of nested mutable state with a meaningful nearest-owner operation, while legitimate rendering of immutable values is a clear counterexample.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
