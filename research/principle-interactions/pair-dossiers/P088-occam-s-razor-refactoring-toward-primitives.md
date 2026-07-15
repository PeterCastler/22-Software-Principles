# Occam's Razor ↔ Refactoring Toward Primitives

Assessment status: Final publish; validated for freeze  
Primary classification: Reinforcement  
Secondary classifications: None  
Evidence grade: Convergent  
Confidence: high

## Shared decision surface

Causally connected decisions: Occam's Razor governs selection among equally adequate designs or explanations; Refactoring Toward Primitives governs replacement of custom code by existing capabilities.

## Interaction mechanism

A matching platform primitive can satisfy the same contract with fewer project-owned assumptions and moving parts.

## Material consequence

The design removes custom machinery after verifying that the primitive is adequate across edge cases and lifecycle cost.

## Context in which it applies

Applies when custom and primitive-based implementations meet the same contract.

## Counterexample or boundary

A platform API with incompatible errors and lock-in is not an equally adequate simpler account.

## Worked example

**Starting condition:** A matching platform primitive can satisfy the same contract with fewer project-owned assumptions and moving parts.

**Decision after applying both principles:** The design removes custom machinery after verifying that the primitive is adequate across edge cases and lifecycle cost.

**Boundary check:** A platform API with incompatible errors and lock-in is not an equally adequate simpler account.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

The design removes custom machinery after verifying that the primitive is adequate across edge cases and lifecycle cost.

## Evidence

Sources: S009; I013; I014. See the [source register](../source-register.md). The final grade is **Convergent**: separate authoritative sources establish both sides of the stated, testable mechanism.

Adversarial finding: Contract-equivalent primitive use can remove project-owned entities and assumptions in Occam's comparison; incompatible errors or lock-in correctly defeat equal adequacy.

## Independent review

Blind primary screen: **Reinforcement / uncertain**. Blind independent screen: **Reinforcement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Reinforcement / Convergent**. Contract-equivalent primitive use can remove project-owned entities and assumptions in Occam's comparison; incompatible errors or lock-in correctly defeat equal adequacy.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
