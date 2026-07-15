# Convention over Configuration ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Convention over Configuration governs routine defaults versus explicit exceptions; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

Convention can reduce composition wiring, but hidden dependency resolution obscures DIP's ownership, lifetime, and source direction.

## Material consequence

The composition remains inspectable even if standard conventions discover adapters.

## Context in which it applies

Applies when a framework convention auto-wires policy and details.

## Counterexample or boundary

Explicit construction is preferable when inferred resolution makes errors and lifetimes hard to trace.

## Worked example

**Starting condition:** Convention can reduce composition wiring, but hidden dependency resolution obscures DIP's ownership, lifetime, and source direction.

**Decision after applying both principles:** The composition remains inspectable even if standard conventions discover adapters.

**Boundary check:** Explicit construction is preferable when inferred resolution makes errors and lifetimes hard to trace.

## Resolution procedure

Use convention at the composition edge for routine discovery, while keeping the policy-owned contract and dependency direction explicit. Switch to explicit construction when resolution, lifetime, or failure behavior becomes hard to inspect.

## Combined instruction

The composition remains inspectable even if standard conventions discover adapters.

## Evidence

Sources: I008; I009; I019. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution is coherent: use convention only at the composition edge while retaining explicit policy ownership, lifetimes, and dependency direction; switch to explicit wiring when inspection fails.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution is coherent: use convention only at the composition edge while retaining explicit policy ownership, lifetimes, and dependency direction; switch to explicit wiring when inspection fails.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
