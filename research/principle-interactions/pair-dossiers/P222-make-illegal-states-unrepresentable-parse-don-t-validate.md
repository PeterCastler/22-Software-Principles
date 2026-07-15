# Make Illegal States Unrepresentable ↔ Parse, Don't Validate

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: Make Illegal States Unrepresentable governs representation and enforcement of stable invariants; Parse, Don't Validate governs conversion of raw input into trusted domain values.

## Interaction mechanism

Parsing is the construction mechanism that turns weak external values into the precise representation whose illegal states are excluded.

## Material consequence

Raw data is checked once, the trusted constructor is controlled, and internal functions require the resulting type.

## Context in which it applies

Applies when external inputs must enter a domain with stable representable invariants.

## Counterexample or boundary

Current inventory cannot be permanently proven by parsing and still requires transactional checking.

## Worked example

**Starting condition:** Parsing is the construction mechanism that turns weak external values into the precise representation whose illegal states are excluded.

**Decision after applying both principles:** Raw data is checked once, the trusted constructor is controlled, and internal functions require the resulting type.

**Boundary check:** Current inventory cannot be permanently proven by parsing and still requires transactional checking.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Raw data is checked once, the trusted constructor is controlled, and internal functions require the resulting type.

## Evidence

Sources: I007; S035. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I007 explicitly instructs parsing into the most precise representation and directly names making illegal states unrepresentable, satisfying Direct evidence.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I007 explicitly instructs parsing into the most precise representation and directly names making illegal states unrepresentable, satisfying Direct evidence.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
