# Make Illegal States Unrepresentable ↔ Tell, Don't Ask

Assessment status: Final publish; validated for freeze  
Primary classification: Complementary  
Secondary classifications: Reinforcement  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Make Illegal States Unrepresentable governs representation and enforcement of stable invariants; Tell, Don't Ask governs ownership of state-dependent decisions and transitions.

## Interaction mechanism

Precise types constrain static states while domain commands control legal transitions so callers cannot construct invalid combinations by mutation.

## Material consequence

The owner exposes meaningful operations that return a valid next variant instead of public setters for correlated fields.

## Context in which it applies

Applies when the invariant spans state plus allowed transitions.

## Counterexample or boundary

An immutable report value needs no command API when it cannot be mutated into an illegal state.

## Worked example

**Starting condition:** Precise types constrain static states while domain commands control legal transitions so callers cannot construct invalid combinations by mutation.

**Decision after applying both principles:** The owner exposes meaningful operations that return a valid next variant instead of public setters for correlated fields.

**Boundary check:** An immutable report value needs no command API when it cannot be mutated into an illegal state.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The owner exposes meaningful operations that return a valid next variant instead of public setters for correlated fields.

## Evidence

Sources: S035; S039. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Precise representations constrain static states while owner commands constrain transitions, producing distinct complementary protections; immutable report values need no command API.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Complementary / uncertain**.

Adversarial verdict: **accept**; recommendation: **Complementary / Convergent**. Precise representations constrain static states while owner commands constrain transitions, producing distinct complementary protections; immutable report values need no command API.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
