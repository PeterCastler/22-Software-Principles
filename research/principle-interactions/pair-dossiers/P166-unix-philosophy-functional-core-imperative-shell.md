# Unix Philosophy ↔ Functional Core, Imperative Shell

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Unix Philosophy governs component scope and composition interface; Functional Core, Imperative Shell governs placement of deterministic decisions and effects.

## Interaction mechanism

Unix-style value streams and focused stages support a deterministic core, while the shell owns process and I/O effects.

## Material consequence

Pure transformations can be composed and tested separately from file, network, and diagnostic handling.

## Context in which it applies

Applies when a tool contains meaningful transformations plus external interaction.

## Counterexample or boundary

A simple pass-through command with only I/O has no useful functional core.

## Worked example

**Starting condition:** Unix-style value streams and focused stages support a deterministic core, while the shell owns process and I/O effects.

**Decision after applying both principles:** Pure transformations can be composed and tested separately from file, network, and diagnostic handling.

**Boundary check:** A simple pass-through command with only I/O has no useful functional core.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Pure transformations can be composed and tested separately from file, network, and diagnostic handling.

## Evidence

Sources: I012; I016. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Focused value-oriented stages and a core/shell effect boundary perform distinct complementary work; an I/O-only pass-through command correctly lacks a useful core.

## Independent review

Blind primary screen: **Complementary / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **accept**; recommendation: **Complementary / Convergent**. Focused value-oriented stages and a core/shell effect boundary perform distinct complementary work; an I/O-only pass-through command correctly lacks a useful core.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
