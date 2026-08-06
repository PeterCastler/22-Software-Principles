# Combination Boundaries

## Contents

- Precedence and evidence
- Supported tension resolutions
- Common misapplications
- Rejected bundle shapes
- Absence of a relationship

## Precedence and evidence

Apply these controls before any principle:

1. Preserve correctness, security, and explicit current requirements.
2. Hold candidate designs to the same complete adequacy standard.
3. Require each principle's current preconditions; benefits or shared vocabulary are not preconditions.
4. Prefer no principle, one principle, or one validated bundle in that order.
5. Keep a selected counterexample visible as the stopping rule.
6. Use two bundles only for two distinct decision surfaces and resolve their shared principles once.
7. Treat an absent pair relationship as no generic interaction, not as a prohibition on project-specific evidence.

The accepted study contains Reinforcement, Enablement, Moderation, Sequencing, Complementary, Overlap, and Tension. It found no general Conflict. Do not convert scoped tension into a universal contradiction or universal compatibility.

## Supported tension resolutions

### KISS ↔ Separation of Concerns — P006

Introduce the cheapest boundary that yields meaningful independence. Keep one cohesive invariant together when splitting only adds navigation and contracts.

### KISS ↔ Convention over Configuration — P009

Use a transparent convention for the routine case. Switch to explicit configuration when discovery, exceptions, or precedence become harder to understand than direct declaration.

### KISS ↔ Data-Driven Design — P016

Use one typed table for a stable shared algorithm with regular cases. Keep irregular algorithms as direct code and reject callback-filled configuration.

### KISS ↔ Dependency Inversion Principle — P015

Establish a present policy or volatility boundary first. If none exists, keep the dependency direct; if one exists, add only the narrowest policy-owned capability.

### KISS ↔ Make Illegal States Unrepresentable — P017

Compare invalid combinations and downstream branches removed with representational burden added. Encode stable high-value invariants using the least elaborate adequate representation.

### Separation of Concerns ↔ Tell, Don't Ask — P124

Keep invariant-sensitive behavior with its state owner while persistence, presentation, and orchestration remain outside. Do not add forwarding layers merely to preserve folders.

### Single Responsibility Principle ↔ Tell, Don't Ask — P138

Let the demonstrated actor set the module boundary, then keep that actor's invariant behavior with its data. Exclude storage, rendering, and cross-aggregate workflow owned elsewhere.

### Convention over Configuration ↔ Dependency Inversion Principle — P159

Use convention only at the composition edge while keeping policy ownership, dependency direction, lifetime, and failure behavior inspectable. Use explicit construction when inference obscures them.

### Refactoring Toward Primitives ↔ Dependency Inversion Principle — P204

Call a fitting platform primitive directly. Add an adapter only when it narrows volatile, irrelevant, or incompatible semantics into a stable application contract; delete mirror wrappers.

### Refactoring Toward Primitives ↔ Law of Demeter — P209

Use a stable flat primitive directly. Add a narrow capability only when callers would otherwise traverse a volatile object graph; do not duplicate the entire primitive API.

### Data-Driven Design ↔ Tell, Don't Ask — P219

Keep stable stateless mappings in data. Keep transitions depending on private mutable state as owner operations; the operation may consult the table without moving its invariant into configuration.

## Common misapplications

- **All principles at once:** conditional guidance becomes permanent noise. Route the smallest applicable set.
- **KISS as short code:** compare whole-lifecycle concepts and obligations, not characters.
- **YAGNI as omission:** current quality, compatibility, security, and irreversible-risk requirements remain current.
- **DRY from textual similarity:** centralize only one changing fact with one owner.
- **Rule of Three as arithmetic:** repeated count supplies evidence, not an automatic extraction command.
- **Separation or SRP as file multiplication:** boundaries require independent rules, actors, or change.
- **Composition everywhere:** fixed behavior and genuine subtypes do not need strategies.
- **Convention as magic:** keep discovery, precedence, lifetime, and exceptions inspectable.
- **DIP for every dependency:** stable helpers and mock-only seams normally stay direct.
- **Data-driven callbacks:** arbitrary executable rows are a rules engine, not constrained data.
- **Precise types as total validation:** authorization, freshness, concurrent state, and resources remain use-time facts.
- **Tell Don't Ask or Demeter as getter bans:** transparent queries and values remain legitimate.
- **Negative Code or dead-code elimination by line count:** prove semantic preservation and supported liveness.
- **Boy Scout Rule as roaming authority:** stop at the touched path or when cleanup requires new judgment.

## Rejected bundle shapes

### R01 — Universal anti-bloat super-bundle

Do not merge local abstraction timing with policy architecture under “reduce bloat.” Use B01 for local evidence-led design or B06 for a demonstrated volatile boundary.

### R02 — Put all behavior in data and objects

Do not combine stateless data policy and state-owned transitions without a domain-specific placement rule. Use B02 for regular stateless variation or B05 for contextual commands.

### R03 — Primitive-first architecture

Do not decide between direct primitive use and an adapter without evidence about provider volatility and object-graph leakage.

### R04 — Cleanup trio

Negative Code, dead-code elimination, and bounded cleanup alone omit adequacy and replacement evidence. Use B04.

### R05 — Layered domain object bundle

Separation, SRP, and Tell Don't Ask have tensions dependent on concrete infrastructure, actors, and invariants. Do not derive a generic layered placement rule.

### R06 — Convention-driven dependency architecture

Do not combine convention, DIP, and Rule of Three generically. A specific framework must first prove that discovery preserves inspectable ownership, lifetime, and failures.

## Absence of a relationship

The frozen ledger rejected 153 of 231 pairs, including 55 researched Unsupported hypotheses and 98 pairs with no general shared decision surface. Do not manufacture a pair-specific mechanism merely because two principles both mention simplicity, maintainability, reuse, testability, or lower coupling. Project evidence may justify applying both independently; it does not create a reusable interaction rule.
