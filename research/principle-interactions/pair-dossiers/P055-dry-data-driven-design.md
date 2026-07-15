# DRY ↔ Data-Driven Design

Assessment status: Final publish; validated for freeze  
Primary classification: Enablement  
Secondary classifications: None  
Evidence grade: Direct  
Confidence: high

## Shared decision surface

Causally connected decisions: DRY governs authority for changing knowledge; Data-Driven Design governs representation of regular variation as data or control flow.

## Interaction mechanism

A typed table can become the single authority for a regular case set, with code, types, or documentation derived from it.

## Material consequence

Adding or changing a case edits one data representation instead of synchronized branches and key lists.

## Context in which it applies

Applies when cases share one algorithm and the table can own their valid key set.

## Counterexample or boundary

A table plus a separately maintained enum duplicates authority rather than resolving it.

## Worked example

**Starting condition:** A typed table can become the single authority for a regular case set, with code, types, or documentation derived from it.

**Decision after applying both principles:** Adding or changing a case edits one data representation instead of synchronized branches and key lists.

**Boundary check:** A table plus a separately maintained enum duplicates authority rather than resolving it.

## Resolution procedure

No conflict resolution is required. Apply the interaction only while both canonical preconditions hold; the counterexample is the stopping rule.

## Combined instruction

Adding or changing a case edits one data representation instead of synchronized branches and key lists.

## Evidence

Sources: I015; S005. See the [source register](../source-register.md). The final grade is **Direct**: an authoritative source explicitly connects the two operational recommendations.

Adversarial finding: I015 explicitly presents data representation as a single point of knowledge replacing scattered logic, so a typed case table can directly enable DRY.

## Independent review

Blind primary screen: **Enablement / uncertain**. Blind independent screen: **Enablement / uncertain**.

Adversarial verdict: **accept**; recommendation: **Enablement / Direct**. I015 explicitly presents data representation as a single point of knowledge replacing scattered logic, so a typed case table can directly enable DRY.

## Journal references

- J-20260715-1920-04 — primary profile-only screening
- J-20260715-1935-05 — blind-screen comparison and candidate-set construction
- J-20260715-1950-06 — targeted research source batch
- J-20260715-2050-09 — adversarial review and reconciliation
