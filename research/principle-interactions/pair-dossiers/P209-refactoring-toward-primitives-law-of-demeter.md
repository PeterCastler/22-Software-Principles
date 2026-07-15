# Refactoring Toward Primitives ↔ Law of Demeter

Assessment status: Final publish; validated for freeze  
Primary classification: Tension  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Refactoring Toward Primitives governs replacement of custom code by existing capabilities; Law of Demeter governs knowledge of collaborators' internal structure.

## Interaction mechanism

Directly reaching through a framework or SDK object graph uses primitives but couples callers to internal structure; a narrow adapter can be justified.

## Material consequence

The design exposes only the stable capability or plain value while avoiding a wrapper that mirrors the whole primitive API.

## Context in which it applies

Applies when the primitive's nested ownership structure is volatile or leaks into many callers.

## Counterexample or boundary

Direct use of a stable flat standard value API creates no train-wreck dependency.

## Worked example

**Starting condition:** Directly reaching through a framework or SDK object graph uses primitives but couples callers to internal structure; a narrow adapter can be justified.

**Decision after applying both principles:** The design exposes only the stable capability or plain value while avoiding a wrapper that mirrors the whole primitive API.

**Boundary check:** Direct use of a stable flat standard value API creates no train-wreck dependency.

## Resolution procedure

Use a stable flat primitive directly. Introduce a narrow adapter only when callers would otherwise traverse a volatile object graph, and expose a capability or plain value rather than duplicating the whole primitive API.

## Combined instruction

The design exposes only the stable capability or plain value while avoiding a wrapper that mirrors the whole primitive API.

## Evidence

Sources: I013; S041. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: The Tension resolution is coherent: use flat stable primitives directly, adding only a narrow capability boundary when callers would otherwise traverse a volatile graph.

## Independent review

Blind primary screen: **Tension / uncertain**. Blind independent screen: **Tension / uncertain**.

Adversarial verdict: **accept**; recommendation: **Tension / Convergent**. The Tension resolution is coherent: use flat stable primitives directly, adding only a narrow capability boundary when callers would otherwise traverse a volatile graph.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
