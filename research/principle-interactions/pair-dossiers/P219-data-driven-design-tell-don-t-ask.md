# Data-Driven Design ↔ Tell, Don't Ask

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Data-Driven Design governs representation of regular variation as data or control flow; Tell, Don't Ask governs ownership of state-dependent decisions and transitions.

## Interaction mechanism

A central table places regular policy outside an object's methods, while Tell, Don't Ask places state-dependent invariant transitions with their owner.

## Material consequence

Static mappings remain data-driven; transitions that require private mutable state remain domain operations, possibly consulting a table.

## Context in which it applies

Applies when a proposed table would contain stateful transition callbacks or bypass invariant ownership.

## Counterexample or boundary

A status-to-label map is presentation data and does not belong inside the state-owning object.

## Worked example

**Starting condition:** A central table places regular policy outside an object's methods, while Tell, Don't Ask places state-dependent invariant transitions with their owner.

**Decision after applying both principles:** Static mappings remain data-driven; transitions that require private mutable state remain domain operations, possibly consulting a table.

**Boundary check:** A status-to-label map is presentation data and does not belong inside the state-owning object.

## Resolution procedure

Keep stable, stateless mappings in data. Keep transitions that depend on private mutable state as operations on the state owner; the operation may consult the table without moving the invariant itself into configuration.

## Combined instruction

Static mappings remain data-driven; transitions that require private mutable state remain domain operations, possibly consulting a table.

## Evidence

Sources: I015; S039. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution genuinely separates stateless regular mappings from state-owner transitions, allowing an owner operation to consult data without moving its invariant into callbacks.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution genuinely separates stateless regular mappings from state-owner transitions, allowing an owner operation to consult data without moving its invariant into callbacks.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
