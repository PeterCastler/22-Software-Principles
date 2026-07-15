# YAGNI ↔ Dependency Inversion Principle

Assessment status: Final publish; validated for freeze  
Primary classification: Moderation  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: YAGNI governs timing of capability and extensibility; Dependency Inversion Principle governs contract ownership and source-dependency direction.

## Interaction mechanism

YAGNI prevents DIP boundaries invented for hypothetical providers; DIP remains justified for an existing volatile detail or policy isolation need.

## Material consequence

The implementation uses a direct dependency or the narrowest present boundary based on demonstrated volatility.

## Context in which it applies

Applies when an abstraction is proposed solely because another implementation might arrive.

## Counterexample or boundary

An unstable vendor SDK already leaking into core policy creates a current inversion need.

## Worked example

**Starting condition:** YAGNI prevents DIP boundaries invented for hypothetical providers; DIP remains justified for an existing volatile detail or policy isolation need.

**Decision after applying both principles:** The implementation uses a direct dependency or the narrowest present boundary based on demonstrated volatility.

**Boundary check:** An unstable vendor SDK already leaking into core policy creates a current inversion need.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The implementation uses a direct dependency or the narrowest present boundary based on demonstrated volatility.

## Evidence

Sources: I010; S003. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I010 explicitly discusses YAGNI while applying SRP or DIP factoring, warning against speculative design; this satisfies Direct evidence for the moderation.

## Independent review

Blind primary screen: **Moderation / uncertain**. Blind independent screen: **Moderation / uncertain**.

Adversarial verdict: **accept**; recommendation: **Moderation / Direct**. I010 explicitly discusses YAGNI while applying SRP or DIP factoring, warning against speculative design; this satisfies Direct evidence for the moderation.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
