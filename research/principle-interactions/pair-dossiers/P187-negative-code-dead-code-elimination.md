# Negative Code ↔ Dead Code Elimination

Assessment status: Final publish; validated for freeze  
Primary classification: Overlap  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Negative Code governs net removal of owned machinery while preserving contract; Dead Code Elimination governs liveness within the supported system boundary.

## Interaction mechanism

Liveness proof identifies a class of safe deletion; Negative Code supplies the broader outcome test and requires removing the obsolete perimeter.

## Material consequence

Once behavior is proven unobservable, its flags, tests, configuration, docs, and dependencies are deleted coherently.

## Context in which it applies

Applies when a candidate appears unused but the supported boundary must be established.

## Counterexample or boundary

Replacing live custom code with a primitive is Negative Code but not Dead Code Elimination.

## Worked example

**Starting condition:** Liveness proof identifies a class of safe deletion; Negative Code supplies the broader outcome test and requires removing the obsolete perimeter.

**Decision after applying both principles:** Once behavior is proven unobservable, its flags, tests, configuration, docs, and dependencies are deleted coherently.

**Boundary check:** Replacing live custom code with a primitive is Negative Code but not Dead Code Elimination.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Once behavior is proven unobservable, its flags, tests, configuration, docs, and dependencies are deleted coherently.

## Evidence

Sources: S027; I017; I020. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: DCE is the liveness-proven subset of Negative Code, while Negative Code also covers replacement of live machinery. That set relationship is primarily Overlap, not Enablement.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Overlap / uncertain**.

Adversarial verdict: **downgrade**; recommendation: **Overlap / Convergent**. DCE is the liveness-proven subset of Negative Code, while Negative Code also covers replacement of live machinery. That set relationship is primarily Overlap, not Enablement.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
