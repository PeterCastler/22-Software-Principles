# Principle Interaction Guide

> **Dataset status:** frozen in research journal entry J-20260715-2115-10. Pair classifications are evidence-derived and predate all bundle analysis.

## Purpose and epistemic limits

This guide explains only the interactions that survived an exhaustive study of the 231 unordered pairs among the library’s 22 principles. It is intended for implementation and review decisions: each published entry states what decision surface the principles share, how one changes application of the other, what materially changes, and where the relationship stops.

It is not a compatibility score, a hierarchy of universally good practices, or permission to force every principle into a project. The 153 rejected pairs remain in the proof ledger and are omitted here because a generic similarity such as “both reduce complexity” is not a causal interaction. A relationship applies only when both canonical preconditions and the entry’s context hold.

The frozen dataset contains **78 published interactions**: 10 Direct, 67 Convergent, and 1 explicitly labeled Reasoned Inference. It contains no published Unsupported claim. No Conflict survived; the eight competing-pressure pairs are Tensions with resolution procedures.

## Canonical-profile method

Each principle was normalized before any pairing. Its profile records the primary problem, recommended action, decision object, preconditions, expected benefit, common over-application, limitations, and sources. This prevents slogans with similar tone from being treated as equivalent. The complete profiles are in [`canonical-profiles.md`](research/principle-interactions/canonical-profiles.md).

## Screening gates

Every pair was tested in this order:

1. **Shared Decision Surface:** the principles affect the same or causally connected decisions.
2. **Identifiable Mechanism:** one changes the conditions, cost, risk, timing, or outcome of applying the other.
3. **Material Consequence:** the interaction changes an implementation or review decision.
4. **Evidence:** a source-backed or explicitly inferred claim supports that mechanism.
5. **Counterexample:** a concrete case demonstrates the relationship’s boundary.

Failure of the first three gates normally produced Independence and rejection. Passing those gates created a research obligation, not a publication.

## Relationship taxonomy

- **Reinforcement:** Applying one strengthens the result sought by the other without changing either principle’s basic action.
- **Enablement:** One creates a precondition or usable mechanism that makes the other practicable.
- **Moderation:** One limits the timing, strength, scope, or over-application of the other.
- **Sequencing:** The interaction changes which action should occur first.
- **Complementary:** The principles govern different, causally connected parts of one engineering decision.
- **Overlap:** The principles cover part of the same decision surface; applying both may be partly redundant, but their tests remain distinct.
- **Tension:** The principles exert competing pressures that can be reconciled with an explicit stopping rule.
- **Conflict:** The principles require mutually exclusive actions under the same context and preconditions.
- **Independence:** No general pair-specific mechanism and material consequence passed the gates.

## Evidence grades and publication policy

- **Direct:** an authoritative source explicitly discusses the interaction or connects the two operational recommendations.
- **Convergent:** separate authoritative sources establish mechanisms that clearly interact.
- **Reasoned Inference:** the operational profiles yield a falsifiable mechanism with a concrete example and counterexample, but the source set does not establish convergence strongly enough.
- **Unsupported:** only analogy, generic benefits, or thematic similarity support the claim.

Publication required all first three gates plus Direct or Convergent evidence, or high-confidence Reasoned Inference with a counterexample and explicit independent-review agreement. Unsupported claims never publish. P227 is the sole published Reasoned Inference and is labeled as such below.

## Interaction overview

| ID | Pair | Primary relationship | Secondary | Evidence | Full dossier |
|---|---|---|---|---|---|
| P001 | KISS ↔ YAGNI | Reinforcement | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P001-kiss-yagni.md) |
| P002 | KISS ↔ DRY | Moderation | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P002-kiss-dry.md) |
| P003 | KISS ↔ Rule of Three | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P003-kiss-rule-of-three.md) |
| P004 | KISS ↔ Occam's Razor | Overlap | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P004-kiss-occam-s-razor.md) |
| P005 | KISS ↔ Principle of Least Power | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P005-kiss-principle-of-least-power.md) |
| P006 | KISS ↔ Separation of Concerns | Moderation | Tension | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P006-kiss-separation-of-concerns.md) |
| P009 | KISS ↔ Convention over Configuration | Moderation | Reinforcement; Tension | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P009-kiss-convention-over-configuration.md) |
| P012 | KISS ↔ Negative Code | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P012-kiss-negative-code.md) |
| P013 | KISS ↔ Dead Code Elimination | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P013-kiss-dead-code-elimination.md) |
| P014 | KISS ↔ Refactoring Toward Primitives | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P014-kiss-refactoring-toward-primitives.md) |
| P015 | KISS ↔ Dependency Inversion Principle | Tension | Moderation | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P015-kiss-dependency-inversion-principle.md) |
| P016 | KISS ↔ Data-Driven Design | Moderation | Tension | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P016-kiss-data-driven-design.md) |
| P017 | KISS ↔ Make Illegal States Unrepresentable | Tension | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P017-kiss-make-illegal-states-unrepresentable.md) |
| P022 | YAGNI ↔ DRY | Moderation | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P022-yagni-dry.md) |
| P023 | YAGNI ↔ Rule of Three | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P023-yagni-rule-of-three.md) |
| P024 | YAGNI ↔ Occam's Razor | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P024-yagni-occam-s-razor.md) |
| P035 | YAGNI ↔ Dependency Inversion Principle | Moderation | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P035-yagni-dependency-inversion-principle.md) |
| P036 | YAGNI ↔ Data-Driven Design | Moderation | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P036-yagni-data-driven-design.md) |
| P042 | DRY ↔ Rule of Three | Moderation | Sequencing | Direct | [Dossier](research/principle-interactions/pair-dossiers/P042-dry-rule-of-three.md) |
| P045 | DRY ↔ Separation of Concerns | Complementary | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P045-dry-separation-of-concerns.md) |
| P046 | DRY ↔ Single Responsibility Principle | Moderation | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P046-dry-single-responsibility-principle.md) |
| P048 | DRY ↔ Convention over Configuration | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P048-dry-convention-over-configuration.md) |
| P055 | DRY ↔ Data-Driven Design | Enablement | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P055-dry-data-driven-design.md) |
| P056 | DRY ↔ Make Illegal States Unrepresentable | Enablement | Reinforcement | Direct | [Dossier](research/principle-interactions/pair-dossiers/P056-dry-make-illegal-states-unrepresentable.md) |
| P057 | DRY ↔ Parse, Don't Validate | Enablement | Reinforcement | Direct | [Dossier](research/principle-interactions/pair-dossiers/P057-dry-parse-don-t-validate.md) |
| P065 | Rule of Three ↔ Composition over Inheritance | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P065-rule-of-three-composition-over-inheritance.md) |
| P066 | Rule of Three ↔ Convention over Configuration | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P066-rule-of-three-convention-over-configuration.md) |
| P072 | Rule of Three ↔ Dependency Inversion Principle | Moderation | Sequencing | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P072-rule-of-three-dependency-inversion-principle.md) |
| P073 | Rule of Three ↔ Data-Driven Design | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P073-rule-of-three-data-driven-design.md) |
| P079 | Occam's Razor ↔ Principle of Least Power | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P079-occam-s-razor-principle-of-least-power.md) |
| P088 | Occam's Razor ↔ Refactoring Toward Primitives | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P088-occam-s-razor-refactoring-toward-primitives.md) |
| P106 | Principle of Least Power ↔ Data-Driven Design | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P106-principle-of-least-power-data-driven-design.md) |
| P107 | Principle of Least Power ↔ Make Illegal States Unrepresentable | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P107-principle-of-least-power-make-illegal-states-unrepresentable.md) |
| P112 | Separation of Concerns ↔ Single Responsibility Principle | Overlap | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P112-separation-of-concerns-single-responsibility-principle.md) |
| P113 | Separation of Concerns ↔ Composition over Inheritance | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P113-separation-of-concerns-composition-over-inheritance.md) |
| P115 | Separation of Concerns ↔ Unix Philosophy | Reinforcement | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P115-separation-of-concerns-unix-philosophy.md) |
| P116 | Separation of Concerns ↔ Functional Core, Imperative Shell | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P116-separation-of-concerns-functional-core-imperative-shell.md) |
| P120 | Separation of Concerns ↔ Dependency Inversion Principle | Enablement | Complementary | Direct | [Dossier](research/principle-interactions/pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md) |
| P123 | Separation of Concerns ↔ Parse, Don't Validate | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P123-separation-of-concerns-parse-don-t-validate.md) |
| P124 | Separation of Concerns ↔ Tell, Don't Ask | Tension | Moderation | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P124-separation-of-concerns-tell-don-t-ask.md) |
| P125 | Separation of Concerns ↔ Law of Demeter | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P125-separation-of-concerns-law-of-demeter.md) |
| P129 | Single Responsibility Principle ↔ Unix Philosophy | Overlap | Reinforcement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P129-single-responsibility-principle-unix-philosophy.md) |
| P134 | Single Responsibility Principle ↔ Dependency Inversion Principle | Complementary | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P134-single-responsibility-principle-dependency-inversion-principle.md) |
| P138 | Single Responsibility Principle ↔ Tell, Don't Ask | Tension | Moderation | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P138-single-responsibility-principle-tell-don-t-ask.md) |
| P142 | Composition over Inheritance ↔ Unix Philosophy | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P142-composition-over-inheritance-unix-philosophy.md) |
| P147 | Composition over Inheritance ↔ Dependency Inversion Principle | Complementary | Enablement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P147-composition-over-inheritance-dependency-inversion-principle.md) |
| P152 | Composition over Inheritance ↔ Law of Demeter | Moderation | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P152-composition-over-inheritance-law-of-demeter.md) |
| P158 | Convention over Configuration ↔ Refactoring Toward Primitives | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P158-convention-over-configuration-refactoring-toward-primitives.md) |
| P159 | Convention over Configuration ↔ Dependency Inversion Principle | Tension | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P159-convention-over-configuration-dependency-inversion-principle.md) |
| P166 | Unix Philosophy ↔ Functional Core, Imperative Shell | Complementary | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P166-unix-philosophy-functional-core-imperative-shell.md) |
| P169 | Unix Philosophy ↔ Refactoring Toward Primitives | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P169-unix-philosophy-refactoring-toward-primitives.md) |
| P171 | Unix Philosophy ↔ Data-Driven Design | Enablement | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P171-unix-philosophy-data-driven-design.md) |
| P173 | Unix Philosophy ↔ Parse, Don't Validate | Sequencing | Complementary | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P173-unix-philosophy-parse-don-t-validate.md) |
| P180 | Functional Core, Imperative Shell ↔ Dependency Inversion Principle | Complementary | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P180-functional-core-imperative-shell-dependency-inversion-principle.md) |
| P183 | Functional Core, Imperative Shell ↔ Parse, Don't Validate | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P183-functional-core-imperative-shell-parse-don-t-validate.md) |
| P187 | Negative Code ↔ Dead Code Elimination | Overlap | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P187-negative-code-dead-code-elimination.md) |
| P188 | Negative Code ↔ Refactoring Toward Primitives | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P188-negative-code-refactoring-toward-primitives.md) |
| P191 | Negative Code ↔ Make Illegal States Unrepresentable | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P191-negative-code-make-illegal-states-unrepresentable.md) |
| P192 | Negative Code ↔ Parse, Don't Validate | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P192-negative-code-parse-don-t-validate.md) |
| P195 | Negative Code ↔ Boy Scout Rule | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P195-negative-code-boy-scout-rule.md) |
| P199 | Dead Code Elimination ↔ Make Illegal States Unrepresentable | Sequencing | Enablement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P199-dead-code-elimination-make-illegal-states-unrepresentable.md) |
| P200 | Dead Code Elimination ↔ Parse, Don't Validate | Sequencing | Enablement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P200-dead-code-elimination-parse-don-t-validate.md) |
| P203 | Dead Code Elimination ↔ Boy Scout Rule | Complementary | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P203-dead-code-elimination-boy-scout-rule.md) |
| P204 | Refactoring Toward Primitives ↔ Dependency Inversion Principle | Tension | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P204-refactoring-toward-primitives-dependency-inversion-principle.md) |
| P206 | Refactoring Toward Primitives ↔ Make Illegal States Unrepresentable | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P206-refactoring-toward-primitives-make-illegal-states-unrepresentable.md) |
| P207 | Refactoring Toward Primitives ↔ Parse, Don't Validate | Enablement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P207-refactoring-toward-primitives-parse-don-t-validate.md) |
| P209 | Refactoring Toward Primitives ↔ Law of Demeter | Tension | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P209-refactoring-toward-primitives-law-of-demeter.md) |
| P212 | Dependency Inversion Principle ↔ Make Illegal States Unrepresentable | Complementary | Reinforcement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P212-dependency-inversion-principle-make-illegal-states-unrepresentable.md) |
| P213 | Dependency Inversion Principle ↔ Parse, Don't Validate | Sequencing | Enablement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P213-dependency-inversion-principle-parse-don-t-validate.md) |
| P215 | Dependency Inversion Principle ↔ Law of Demeter | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P215-dependency-inversion-principle-law-of-demeter.md) |
| P217 | Data-Driven Design ↔ Make Illegal States Unrepresentable | Enablement | Reinforcement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P217-data-driven-design-make-illegal-states-unrepresentable.md) |
| P218 | Data-Driven Design ↔ Parse, Don't Validate | Sequencing | Enablement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P218-data-driven-design-parse-don-t-validate.md) |
| P219 | Data-Driven Design ↔ Tell, Don't Ask | Tension | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P219-data-driven-design-tell-don-t-ask.md) |
| P222 | Make Illegal States Unrepresentable ↔ Parse, Don't Validate | Enablement | — | Direct | [Dossier](research/principle-interactions/pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md) |
| P223 | Make Illegal States Unrepresentable ↔ Tell, Don't Ask | Complementary | Reinforcement | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P223-make-illegal-states-unrepresentable-tell-don-t-ask.md) |
| P226 | Parse, Don't Validate ↔ Tell, Don't Ask | Sequencing | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P226-parse-don-t-validate-tell-don-t-ask.md) |
| P227 | Parse, Don't Validate ↔ Law of Demeter | Complementary | — | Reasoned Inference | [Dossier](research/principle-interactions/pair-dossiers/P227-parse-don-t-validate-law-of-demeter.md) |
| P229 | Tell, Don't Ask ↔ Law of Demeter | Reinforcement | — | Convergent | [Dossier](research/principle-interactions/pair-dossiers/P229-tell-don-t-ask-law-of-demeter.md) |

## Published interaction dossiers

The entries below are compact decision records. The linked pair dossiers contain the worked example, source IDs, blind-screen results, adversarial verdict, and journal references.

## Reinforcement

Applying one strengthens the result sought by the other without changing either principle’s basic action.

### P001 · KISS ↔ YAGNI

**Evidence:** Direct.  
**Mechanism:** Deferring unneeded capability prevents the extra mechanisms whose lifecycle cost KISS would otherwise have to remove.  
**Decision consequence:** A design review can reject an option, extension point, or compatibility path before it becomes carrying complexity.  
**Boundary:** A current accessibility or recovery requirement is not speculative, even if it adds substantial structure.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P001-kiss-yagni.md)

### P003 · KISS ↔ Rule of Three

**Evidence:** Convergent.  
**Mechanism:** The Rule of Three supplies an evidence threshold that keeps KISS from mistaking speculative generality for necessary structure.  
**Decision consequence:** Early cases remain direct; abstraction is introduced only after concrete variation shows what structure is justified.  
**Boundary:** A published protocol already defines one authority, so waiting for three local copies would add risk.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P003-kiss-rule-of-three.md)

### P005 · KISS ↔ Principle of Least Power

**Evidence:** Convergent.  
**Mechanism:** Choosing a less expressive adequate mechanism removes possible behaviors and side effects from the design KISS asks maintainers to understand.  
**Decision consequence:** A static mapping, schema, native element, or query can replace a callback, script, or plugin system.  
**Boundary:** A stateful recovery workflow may be clearer as ordinary code than as an overgrown declarative language.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P005-kiss-principle-of-least-power.md)

### P012 · KISS ↔ Negative Code

**Evidence:** Convergent.  
**Mechanism:** A contract-preserving deletion pass directly reduces the concepts and obligations KISS counts.  
**Decision consequence:** After correctness is established, redundant layers, wrappers, options, and obsolete perimeter artifacts can be removed.  
**Boundary:** Compressing readable code into a clever one-liner reduces lines but not whole-system complexity.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P012-kiss-negative-code.md)

### P013 · KISS ↔ Dead Code Elimination

**Evidence:** Convergent.  
**Mechanism:** Proven-dead behavior creates complexity without any supported outcome, so its removal is unambiguously consistent with KISS.  
**Decision consequence:** The change deletes false choices, branches, flags, and dependent artifacts after liveness analysis.  
**Boundary:** A rarely used disaster-recovery path is live even when static search finds no callers.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P013-kiss-dead-code-elimination.md)

### P014 · KISS ↔ Refactoring Toward Primitives

**Evidence:** Convergent.  
**Mechanism:** An adequate existing primitive can remove custom implementation, tests, glue, and edge-case obligations from the whole design.  
**Decision consequence:** The team chooses direct platform use when its exact semantics cost less than continuing to own custom machinery.  
**Boundary:** A heavy dependency for a clear ten-line local function increases total complexity.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P014-kiss-refactoring-toward-primitives.md)

### P023 · YAGNI ↔ Rule of Three

**Evidence:** Convergent.  
**Mechanism:** Both defer abstraction until concrete need exists; repeated cases provide the missing evidence for current reuse.  
**Decision consequence:** The second case may remain local and the third triggers comparison rather than automatic generalization.  
**Boundary:** Immediate extraction can be justified when a security invariant already has one defined authority.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P023-yagni-rule-of-three.md)

### P024 · YAGNI ↔ Occam's Razor

**Evidence:** Convergent.  
**Mechanism:** Presumptive capability rests on unsupported future assumptions that Occam's comparison asks designers not to multiply.  
**Decision consequence:** An architecture option loses when its extra components are justified only by forecast consumers rather than current evidence.  
**Boundary:** A contracted future migration with an irreversible schema deadline is current evidence, not unsupported speculation.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P024-yagni-occam-s-razor.md)

### P048 · DRY ↔ Convention over Configuration

**Evidence:** Convergent.  
**Mechanism:** A convention makes one shared default authoritative instead of duplicating the same routine choice in many configuration files.  
**Decision consequence:** Repeated configuration is removed and exceptional values remain explicit at their point of ownership.  
**Boundary:** Different regulatory settings are independent policy and should not be collapsed into a naming convention.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P048-dry-convention-over-configuration.md)

### P079 · Occam's Razor ↔ Principle of Least Power

**Evidence:** Convergent.  
**Mechanism:** Among adequate mechanisms, the less expressive option commonly introduces fewer unsupported behaviors and assumptions.  
**Decision consequence:** A constrained data or query mechanism wins when arbitrary code supplies no required capability.  
**Boundary:** A weaker language requiring a hidden custom interpreter introduces more entities and is not the parsimonious choice.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P079-occam-s-razor-principle-of-least-power.md)

### P088 · Occam's Razor ↔ Refactoring Toward Primitives

**Evidence:** Convergent.  
**Mechanism:** A matching platform primitive can satisfy the same contract with fewer project-owned assumptions and moving parts.  
**Decision consequence:** The design removes custom machinery after verifying that the primitive is adequate across edge cases and lifecycle cost.  
**Boundary:** A platform API with incompatible errors and lock-in is not an equally adequate simpler account.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P088-occam-s-razor-refactoring-toward-primitives.md)

### P106 · Principle of Least Power ↔ Data-Driven Design

**Evidence:** Convergent.  
**Mechanism:** Moving regular variation from executable branches into validated data reduces expressive power while keeping the decision space visible.  
**Decision consequence:** A typed table replaces repeated control flow only where one algorithm interprets all rows.  
**Boundary:** A callback-filled rules table is still executable behavior and gains no least-power advantage.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P106-principle-of-least-power-data-driven-design.md)

### P107 · Principle of Least Power ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A representation that cannot express invalid combinations has less power in exactly the domain dimension that creates defensive work.  
**Decision consequence:** The implementation chooses a constrained sum type, set, map, or constructor over a broad bag of optional fields.  
**Boundary:** Encoding a mutable remote fact in a static type overclaims what the representation can guarantee.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P107-principle-of-least-power-make-illegal-states-unrepresentable.md)

### P115 · Separation of Concerns ↔ Unix Philosophy

**Evidence:** Direct.  
**Mechanism:** Focused components with stable composable interfaces are an operational form of separating coherent work while preserving recombination.  
**Decision consequence:** A component exposes reusable data rather than absorbing every adjacent transformation.  
**Boundary:** A transaction that must succeed atomically may be clearer and safer as one cohesive component.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P115-separation-of-concerns-unix-philosophy.md)

### P116 · Separation of Concerns ↔ Functional Core, Imperative Shell

**Evidence:** Convergent.  
**Mechanism:** The core/shell pattern instantiates separation by isolating deterministic decisions from external effects.  
**Decision consequence:** Policy can be tested with values while the shell owns I/O, retries, and operational failure handling.  
**Boundary:** A tiny effect-only adapter has no meaningful pure core to extract.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P116-separation-of-concerns-functional-core-imperative-shell.md)

### P123 · Separation of Concerns ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** A parsing boundary separates untrusted transport representation from trusted domain decisions and supplies the value crossing that boundary.  
**Decision consequence:** Effects decode and parse before domain behavior, which no longer accepts raw request or SDK types.  
**Boundary:** Internal values produced entirely inside a trusted module need no redundant parsing layer.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P123-separation-of-concerns-parse-don-t-validate.md)

### P125 · Separation of Concerns ↔ Law of Demeter

**Evidence:** Convergent.  
**Mechanism:** A real concern boundary is undermined when callers navigate its internal object graph; meaningful near-neighbor operations preserve the separation.  
**Decision consequence:** Callers depend on the boundary's capability or plain boundary value rather than nested implementation structure.  
**Boundary:** A renderer traversing a transparent immutable view model is not crossing a hidden concern boundary.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P125-separation-of-concerns-law-of-demeter.md)

### P142 · Composition over Inheritance ↔ Unix Philosophy

**Evidence:** Convergent.  
**Mechanism:** Both build larger behavior by combining replaceable focused parts rather than enlarging one hierarchy or tool.  
**Decision consequence:** Variation is expressed as small ordinary functions or components joined through stable values.  
**Boundary:** Splitting a cohesive in-process algorithm into processes adds serialization and failure cost.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P142-composition-over-inheritance-unix-philosophy.md)

### P158 · Convention over Configuration ↔ Refactoring Toward Primitives

**Evidence:** Convergent.  
**Mechanism:** Framework and ecosystem primitives often embody conventions that make repetitive local configuration unnecessary.  
**Decision consequence:** The project follows the primitive's established discovery and naming defaults and retains explicit exceptions only.  
**Boundary:** Opaque framework inference with many overrides can cost more than direct configuration.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P158-convention-over-configuration-refactoring-toward-primitives.md)

### P169 · Unix Philosophy ↔ Refactoring Toward Primitives

**Evidence:** Convergent.  
**Mechanism:** The Unix emphasis on composing existing focused tools makes a reliable platform utility a preferred replacement for a monolithic custom feature.  
**Decision consequence:** A stage is implemented with a standard tool or format and can still be replaced independently.  
**Boundary:** An ad hoc `awk` split is not adequate for CSV fields containing quotes and newlines.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P169-unix-philosophy-refactoring-toward-primitives.md)

### P215 · Dependency Inversion Principle ↔ Law of Demeter

**Evidence:** Convergent.  
**Mechanism:** Both prevent policy from knowing low-level structure: DIP controls source direction and Law of Demeter controls graph navigation through the contract.  
**Decision consequence:** The policy asks for a narrow domain capability rather than traversing an injected SDK or repository object.  
**Boundary:** An injected vendor interface still violates the mechanism if policy navigates vendor-specific response graphs.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P215-dependency-inversion-principle-law-of-demeter.md)

### P229 · Tell, Don't Ask ↔ Law of Demeter

**Evidence:** Convergent.  
**Mechanism:** Both replace external knowledge of nested state with a meaningful operation on the nearest owner; Tell, Don't Ask focuses on decision ownership and Demeter on structural knowledge.  
**Decision consequence:** A caller requests `withdraw` or `pay` rather than retrieving nested fields, deciding, and mutating them.  
**Boundary:** A renderer reading a plain immutable address is a legitimate query and needs no forwarding command.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P229-tell-don-t-ask-law-of-demeter.md)

## Enablement

One creates a precondition or usable mechanism that makes the other practicable.

### P055 · DRY ↔ Data-Driven Design

**Evidence:** Direct.  
**Mechanism:** A typed table can become the single authority for a regular case set, with code, types, or documentation derived from it.  
**Decision consequence:** Adding or changing a case edits one data representation instead of synchronized branches and key lists.  
**Boundary:** A table plus a separately maintained enum duplicates authority rather than resolving it.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P055-dry-data-driven-design.md)

### P056 · DRY ↔ Make Illegal States Unrepresentable

**Evidence:** Direct.  
**Mechanism:** Deriving dependent values instead of storing synchronized copies removes both duplicated authority and the illegal state in which copies disagree.  
**Decision consequence:** The data model stores one source value and calculates its dependent flags, counts, or totals.  
**Boundary:** Intentional denormalization for measured performance may require transactional synchronization rather than deletion.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P056-dry-make-illegal-states-unrepresentable.md)

### P057 · DRY ↔ Parse, Don't Validate

**Evidence:** Direct.  
**Mechanism:** Parsing once creates one boundary authority for structural facts instead of repeating validators throughout the domain.  
**Decision consequence:** Downstream functions accept the trusted value and redundant structural checks are removed.  
**Boundary:** Authorization can change after parsing and remains a use-time check rather than duplicated parsing knowledge.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P057-dry-parse-don-t-validate.md)

### P113 · Separation of Concerns ↔ Composition over Inheritance

**Evidence:** Convergent.  
**Mechanism:** Once independent variation axes are separated, composition can recombine them without subclassing every combination.  
**Decision consequence:** Format, destination, filtering, or policy remain focused behaviors assembled at one explicit boundary.  
**Boundary:** If behavior never varies, separated strategy objects add wiring without enabling useful composition.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P113-separation-of-concerns-composition-over-inheritance.md)

### P120 · Separation of Concerns ↔ Dependency Inversion Principle

**Evidence:** Direct.  
**Mechanism:** Separating policy from infrastructure identifies the boundary; inversion makes the detail depend on the policy-owned contract.  
**Decision consequence:** Vendor types stay outside and the core states only the capability it needs.  
**Boundary:** A stable local algorithm is not an infrastructure concern requiring an inverted interface.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md)

### P171 · Unix Philosophy ↔ Data-Driven Design

**Evidence:** Direct.  
**Mechanism:** Stable data interfaces let focused tools operate through one general algorithm rather than embedding a flag and branch for every case.  
**Decision consequence:** Behavior variation moves into inspectable data consumable by several composable stages.  
**Boundary:** A hidden callback language inside configuration undermines simple composable interfaces.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P171-unix-philosophy-data-driven-design.md)

### P188 · Negative Code ↔ Refactoring Toward Primitives

**Evidence:** Convergent.  
**Mechanism:** A matching primitive is a mechanism for producing negative code by making custom implementation and glue redundant.  
**Decision consequence:** After characterization, the change deletes the replaced implementation while retaining application-contract tests.  
**Boundary:** Adding a large dependency may reduce local lines while increasing total obligations.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P188-negative-code-refactoring-toward-primitives.md)

### P191 · Negative Code ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A precise representation can make defensive branches, synchronized fields, and impossible-case tests unnecessary.  
**Decision consequence:** After construction is controlled, the change removes only checks and state copies now proven impossible.  
**Boundary:** Checks for current authorization remain live because the type cannot prove a mutable external fact.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P191-negative-code-make-illegal-states-unrepresentable.md)

### P192 · Negative Code ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** Parsing once preserves evidence that makes downstream casts, validators, and impossible-case branches removable.  
**Decision consequence:** The deletion follows signature changes so raw values cannot bypass the parser.  
**Boundary:** Rate limits and concurrent uniqueness remain necessary after structural parsing.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P192-negative-code-parse-don-t-validate.md)

### P206 · Refactoring Toward Primitives ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** Sets, maps, database constraints, discriminated unions, and standard constructors can enforce invariants with less custom validation machinery.  
**Decision consequence:** The design selects a primitive whose native semantics exclude the invalid state and deletes redundant enforcement.  
**Boundary:** A database uniqueness constraint does not by itself model a recoverable domain error for the caller.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P206-refactoring-toward-primitives-make-illegal-states-unrepresentable.md)

### P207 · Refactoring Toward Primitives ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** A standard parser, schema, or framework decoder can construct the trusted value and replace handwritten checking.  
**Decision consequence:** The team verifies error, normalization, and compatibility semantics before deleting the custom validator.  
**Boundary:** A generic JSON parse does not establish domain ranges and is insufficient by itself.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P207-refactoring-toward-primitives-parse-don-t-validate.md)

### P217 · Data-Driven Design ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A table can own the valid key set and derive a precise type, removing unknown-key states and duplicated enums.  
**Decision consequence:** Construction validates rows and trusted lookups become exhaustive over the table-derived keys.  
**Boundary:** User-defined runtime keys cannot be made a closed compile-time union and still require error handling.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P217-data-driven-design-make-illegal-states-unrepresentable.md)

### P222 · Make Illegal States Unrepresentable ↔ Parse, Don't Validate

**Evidence:** Direct.  
**Mechanism:** Parsing is the construction mechanism that turns weak external values into the precise representation whose illegal states are excluded.  
**Decision consequence:** Raw data is checked once, the trusted constructor is controlled, and internal functions require the resulting type.  
**Boundary:** Current inventory cannot be permanently proven by parsing and still requires transactional checking.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md)

## Moderation

One limits the timing, strength, scope, or over-application of the other.

### P002 · KISS ↔ DRY

**Evidence:** Convergent.  
**Mechanism:** DRY can remove coordinated authorities, but KISS rejects a shared abstraction when its indirection costs more than the duplication it removes.  
**Decision consequence:** The reviewer must choose between a narrow authority and intentionally separate local copies instead of deduplicating by appearance.  
**Boundary:** Two identical literals owned by independent policies should remain separate despite textual duplication.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P002-kiss-dry.md)

### P006 · KISS ↔ Separation of Concerns

**Evidence:** Convergent.  
**Mechanism:** A boundary can reduce entanglement but also adds concepts, navigation, and contracts; KISS requires the separation to repay that cost.  
**Decision consequence:** The implementation uses the cheapest meaningful boundary and avoids forwarding layers or unnecessary services.  
**Boundary:** Splitting one cohesive invariant across files increases complexity without independent change benefit.  
**Resolution:** First prove that the concerns have independent reasons or rates of change. If they do not, keep the cohesive implementation together. If they do, introduce the cheapest boundary that isolates them, then remove forwarding layers whose only purpose is architectural symmetry.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P006-kiss-separation-of-concerns.md)

### P009 · KISS ↔ Convention over Configuration

**Evidence:** Convergent.  
**Mechanism:** A discoverable convention removes repetitive configuration, while KISS prevents convention from becoming hidden magic or a complex precedence system.  
**Decision consequence:** The common path uses one predictable default and only real exceptions remain explicit.  
**Boundary:** When exceptions dominate or policy is important, explicit configuration is simpler than inference.  
**Resolution:** Use convention only for a stable, dominant, discoverable common case. Keep significant policy and real exceptions explicit. If the convention requires multiple precedence levels or most callers override it, replace the inference with direct configuration.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P009-kiss-convention-over-configuration.md)

### P016 · KISS ↔ Data-Driven Design

**Evidence:** Convergent.  
**Mechanism:** A table can simplify regular branches, but a generic interpreter or callback-filled configuration can hide more complexity than direct control flow.  
**Decision consequence:** The reviewer chooses a typed lookup only for regular cases and leaves irregular algorithms in code.  
**Boundary:** Three unrelated algorithms do not become simpler when stored as callbacks in a table.  
**Resolution:** First test whether the cases share one stable algorithm and vary along regular dimensions. If yes, use one typed table and direct interpreter. If not, retain explicit control flow; do not resolve irregularity by adding callbacks, a rule engine, or an embedded language.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P016-kiss-data-driven-design.md)

### P022 · YAGNI ↔ DRY

**Evidence:** Convergent.  
**Mechanism:** YAGNI blocks abstractions built for predicted reuse, while DRY still requires one authority for duplicated knowledge that already changes together.  
**Decision consequence:** The team distinguishes present duplicated authority from hypothetical future similarity before extracting.  
**Boundary:** A tax threshold already repeated in two production paths is present knowledge, not future capability.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P022-yagni-dry.md)

### P035 · YAGNI ↔ Dependency Inversion Principle

**Evidence:** Direct.  
**Mechanism:** YAGNI prevents DIP boundaries invented for hypothetical providers; DIP remains justified for an existing volatile detail or policy isolation need.  
**Decision consequence:** The implementation uses a direct dependency or the narrowest present boundary based on demonstrated volatility.  
**Boundary:** An unstable vendor SDK already leaking into core policy creates a current inversion need.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P035-yagni-dependency-inversion-principle.md)

### P036 · YAGNI ↔ Data-Driven Design

**Evidence:** Convergent.  
**Mechanism:** YAGNI rejects generic rule engines and remote configuration built for imagined cases while allowing a direct table for current regular variation.  
**Decision consequence:** The solution encodes only present rows and one current algorithm, without speculative expression features.  
**Boundary:** Five current status mappings can justify a typed local table without any future hypothesis.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P036-yagni-data-driven-design.md)

### P042 · DRY ↔ Rule of Three

**Evidence:** Direct.  
**Mechanism:** The Rule of Three distinguishes proven duplicated knowledge from coincidental repeated syntax before DRY introduces shared authority.  
**Decision consequence:** The team compares meaning, ownership, and reasons for change, then extracts only the stable common fact.  
**Boundary:** A formally defined protocol field should have one authority even before three handwritten copies exist.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P042-dry-rule-of-three.md)

### P046 · DRY ↔ Single Responsibility Principle

**Evidence:** Convergent.  
**Mechanism:** SRP's reasons-for-change test determines whether repeated code is one shared responsibility or two independent authorities.  
**Decision consequence:** A deduplication is accepted only when all callers should change for the same actor and business reason.  
**Boundary:** Identical age and page-size constants remain separate because their actors and change reasons differ.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P046-dry-single-responsibility-principle.md)

### P072 · Rule of Three ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** Repeated implementations can evidence variation, but one current volatile boundary can justify inversion earlier; the rule prevents interface-per-class ritual.  
**Decision consequence:** The team bases inversion on observed volatility or multiple implementations rather than an arbitrary count.  
**Boundary:** One external payment SDK can justify a boundary because its vendor types already infect stable policy.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P072-rule-of-three-dependency-inversion-principle.md)

### P152 · Composition over Inheritance ↔ Law of Demeter

**Evidence:** Convergent.  
**Mechanism:** Composition can create deep collaborator graphs; Law of Demeter prevents consumers from depending on the assembly's internal chain.  
**Decision consequence:** The composer exposes a cohesive capability and keeps nested collaborators private.  
**Boundary:** A transparent pipeline of returned immutable values is not harmful graph navigation.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P152-composition-over-inheritance-law-of-demeter.md)

## Sequencing

The interaction changes which action should occur first.

### P065 · Rule of Three ↔ Composition over Inheritance

**Evidence:** Convergent.  
**Mechanism:** Multiple concrete variants reveal independent axes of behavior and whether composition will reduce subclass combinations.  
**Decision consequence:** The team keeps early behavior direct, then composes the smallest stable varying functions when the axes are observed.  
**Boundary:** A framework-mandated composition point is already a stable external contract.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P065-rule-of-three-composition-over-inheritance.md)

### P066 · Rule of Three ↔ Convention over Configuration

**Evidence:** Convergent.  
**Mechanism:** Observed repeated choices supply evidence for selecting a dominant convention; designing the convention before examples predicts the wrong default and exceptions.  
**Decision consequence:** Teams inventory real variants first, then standardize the common case and retain narrow overrides.  
**Boundary:** An ecosystem framework convention can be adopted immediately because evidence exists outside the repository.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P066-rule-of-three-convention-over-configuration.md)

### P073 · Rule of Three ↔ Data-Driven Design

**Evidence:** Convergent.  
**Mechanism:** Several regular branches reveal the common algorithm and varying dimensions needed for a table.  
**Decision consequence:** Cases are laid side by side before extracting one typed data representation and lookup.  
**Boundary:** A published protocol mapping can provide the stable case set before three local branches exist.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P073-rule-of-three-data-driven-design.md)

### P173 · Unix Philosophy ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** Composable external formats require a parser stage before focused domain transformations can rely on their structure.  
**Decision consequence:** One boundary component turns bytes, lines, or JSON into trusted values; later stages remain simpler.  
**Boundary:** A pipeline that intentionally treats each line as opaque text needs no richer domain parse.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P173-unix-philosophy-parse-don-t-validate.md)

### P183 · Functional Core, Imperative Shell ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** The imperative shell acquires and parses raw input before invoking a core whose signatures require trusted values.  
**Decision consequence:** Parsing errors remain at the boundary and pure domain rules contain no transport casts or repeated structural checks.  
**Boundary:** A decision that depends on locked database state may need parsing and decision inside one transactional shell.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P183-functional-core-imperative-shell-parse-don-t-validate.md)

### P195 · Negative Code ↔ Boy Scout Rule

**Evidence:** Convergent.  
**Mechanism:** The Boy Scout Rule provides a bounded task context for small evidence-backed deletions rather than broad cleanup campaigns.  
**Decision consequence:** An agent removes a redundant branch or wrapper in the touched path and verifies it with the main change.  
**Boundary:** Deleting an unfamiliar cross-system fallback during an unrelated UI task exceeds the cleanup scope.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P195-negative-code-boy-scout-rule.md)

### P199 · Dead Code Elimination ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A stronger representation can prove formerly defensive branches unreachable, after which liveness analysis supports deletion.  
**Decision consequence:** The change first closes construction paths, then removes branches and tests for states no longer representable.  
**Boundary:** Legacy database rows may keep the defensive branch live until migration completes.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P199-dead-code-elimination-make-illegal-states-unrepresentable.md)

### P200 · Dead Code Elimination ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** Once every entry path parses to a trusted value, downstream structural validation can become unreachable or unobservable.  
**Decision consequence:** The team verifies there is no raw bypass and removes the newly dead validation path.  
**Boundary:** A public API that still accepts the raw type keeps its validation live.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P200-dead-code-elimination-parse-don-t-validate.md)

### P213 · Dependency Inversion Principle ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** An infrastructure adapter parses vendor or transport data into the trusted values required by the policy-owned contract.  
**Decision consequence:** Invalid external responses fail at the adapter and cannot leak raw SDK types into the core.  
**Boundary:** An already typed in-process collaborator may need inversion but no parsing step.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P213-dependency-inversion-principle-parse-don-t-validate.md)

### P218 · Data-Driven Design ↔ Parse, Don't Validate

**Evidence:** Convergent.  
**Mechanism:** External strings must be parsed into valid table keys or validated rule data before the shared interpreter can assume completeness.  
**Decision consequence:** The lookup accepts a precise key and has no internal unknown-status branch.  
**Boundary:** A table used only with compiler-generated internal keys needs no runtime parser.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P218-data-driven-design-parse-don-t-validate.md)

### P226 · Parse, Don't Validate ↔ Tell, Don't Ask

**Evidence:** Convergent.  
**Mechanism:** Parsing establishes a trusted command value before Tell, Don't Ask hands it to the component that owns the stateful invariant.  
**Decision consequence:** The boundary rejects malformed input; the domain operation then decides contextual acceptance without rechecking structure.  
**Boundary:** A pure reporting query may use a parsed filter without issuing any domain command.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P226-parse-don-t-validate-tell-don-t-ask.md)

## Complementary

The principles govern different, causally connected parts of one engineering decision.

### P045 · DRY ↔ Separation of Concerns

**Evidence:** Convergent.  
**Mechanism:** DRY pulls one fact toward one authority, while separation keeps independently changing knowledge apart even when implementations look the same.  
**Decision consequence:** The design centralizes only cross-boundary facts that truly share ownership and leaves coincidental duplication local.  
**Boundary:** One schema consumed by UI and API is shared knowledge and may legitimately generate both representations.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P045-dry-separation-of-concerns.md)

### P134 · Single Responsibility Principle ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** SRP identifies policy and infrastructure as different responsibilities; DIP controls dependency direction across the resulting boundary.  
**Decision consequence:** The policy module owns a narrow contract and the infrastructure module implements it.  
**Boundary:** Splitting a stable local helper and adding an interface creates responsibilities that did not exist.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P134-single-responsibility-principle-dependency-inversion-principle.md)

### P147 · Composition over Inheritance ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** DIP defines the policy-owned boundary and composition supplies the concrete detail at the application edge without inheritance.  
**Decision consequence:** A small function or object is passed to policy; no container or base class is required.  
**Boundary:** Composing a fixed helper solely for mockability adds no inversion value.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P147-composition-over-inheritance-dependency-inversion-principle.md)

### P166 · Unix Philosophy ↔ Functional Core, Imperative Shell

**Evidence:** Convergent.  
**Mechanism:** Unix-style value streams and focused stages support a deterministic core, while the shell owns process and I/O effects.  
**Decision consequence:** Pure transformations can be composed and tested separately from file, network, and diagnostic handling.  
**Boundary:** A simple pass-through command with only I/O has no useful functional core.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P166-unix-philosophy-functional-core-imperative-shell.md)

### P180 · Functional Core, Imperative Shell ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** The shell supplies effectful details through policy-shaped capabilities, letting the core avoid vendor dependencies.  
**Decision consequence:** The application edge composes adapters while deterministic policy accepts only domain values or narrow functions.  
**Boundary:** A pure calculation with no external detail needs neither an adapter nor inversion.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P180-functional-core-imperative-shell-dependency-inversion-principle.md)

### P203 · Dead Code Elimination ↔ Boy Scout Rule

**Evidence:** Convergent.  
**Mechanism:** The Boy Scout Rule scopes dead-code removal to the touched path, while DCE supplies the evidence threshold for calling it dead.  
**Decision consequence:** A local flag or branch is removed only after dynamic, external, and rollback uses are checked proportionately.  
**Boundary:** A repository-wide unused-export sweep is separate work, not incidental cleanup.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P203-dead-code-elimination-boy-scout-rule.md)

### P212 · Dependency Inversion Principle ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A policy-owned boundary can accept and return precise domain values, preventing vendor request shapes from widening the core's state space.  
**Decision consequence:** The outer adapter converts detail-specific values into variants whose invariants the policy understands.  
**Boundary:** A passthrough adapter that preserves the entire vendor response provides no representational protection.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P212-dependency-inversion-principle-make-illegal-states-unrepresentable.md)

### P223 · Make Illegal States Unrepresentable ↔ Tell, Don't Ask

**Evidence:** Convergent.  
**Mechanism:** Precise types constrain static states while domain commands control legal transitions so callers cannot construct invalid combinations by mutation.  
**Decision consequence:** The owner exposes meaningful operations that return a valid next variant instead of public setters for correlated fields.  
**Boundary:** An immutable report value needs no command API when it cannot be mutated into an illegal state.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P223-make-illegal-states-unrepresentable-tell-don-t-ask.md)

### P227 · Parse, Don't Validate ↔ Law of Demeter

**Evidence:** Reasoned Inference.  
**Mechanism:** Passing one parsed domain value avoids both raw-shape leakage and navigation through a request or SDK object graph.  
**Decision consequence:** The caller extracts and parses the needed value at the boundary, then collaborators accept that value directly.  
**Boundary:** A parser itself legitimately traverses the raw syntax tree it owns at the boundary.  
**Inference notice:** This mechanism is a high-confidence operational inference, not a Direct or Convergent source claim; the independent adversarial reviewer accepted the concrete mechanism and counterexample.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P227-parse-don-t-validate-law-of-demeter.md)

## Overlap

The principles cover part of the same decision surface; applying both may be partly redundant, but their tests remain distinct.

### P004 · KISS ↔ Occam's Razor

**Evidence:** Convergent.  
**Mechanism:** Both compare adequate choices by unnecessary complexity, while Occam specifically tests unsupported assumptions and KISS counts implementation and lifecycle mechanisms.  
**Decision consequence:** The same candidate can be rejected both for unsupported premises and for unjustified maintenance obligations.  
**Boundary:** A shorter design that omits a required audit trail is not adequate and is favored by neither principle.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P004-kiss-occam-s-razor.md)

### P112 · Separation of Concerns ↔ Single Responsibility Principle

**Evidence:** Convergent.  
**Mechanism:** Both separate independently changing work; SRP sharpens the boundary test by identifying the actor or business reason for change.  
**Decision consequence:** A module split is justified by distinct stakeholders rather than verbs or technical layers alone.  
**Boundary:** Several operations for one cohesive pricing actor remain one responsibility despite different verbs.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P112-separation-of-concerns-single-responsibility-principle.md)

### P129 · Single Responsibility Principle ↔ Unix Philosophy

**Evidence:** Convergent.  
**Mechanism:** Both seek cohesive units, but SRP tests reasons for change while Unix Philosophy additionally requires composable interfaces.  
**Decision consequence:** A component keeps one recognizable purpose and emits output usable without importing its internal responsibilities.  
**Boundary:** One cohesive compiler performs many internal operations without violating either principle.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P129-single-responsibility-principle-unix-philosophy.md)

### P187 · Negative Code ↔ Dead Code Elimination

**Evidence:** Convergent.  
**Mechanism:** Liveness proof identifies a class of safe deletion; Negative Code supplies the broader outcome test and requires removing the obsolete perimeter.  
**Decision consequence:** Once behavior is proven unobservable, its flags, tests, configuration, docs, and dependencies are deleted coherently.  
**Boundary:** Replacing live custom code with a primitive is Negative Code but not Dead Code Elimination.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P187-negative-code-dead-code-elimination.md)

## Tension

The principles exert competing pressures that can be reconciled with an explicit stopping rule.

### P015 · KISS ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** A policy-owned boundary can simplify change around a volatile detail, but unjustified interfaces and containers add indirection.  
**Decision consequence:** The implementation either uses a minimal domain-shaped function boundary or keeps a stable detail direct.  
**Boundary:** A fixed internal helper with no boundary role is simpler when called directly.  
**Resolution:** First establish a present policy/volatility boundary. If none exists, keep the dependency direct. If it exists, introduce the narrowest policy-owned contract and do not add a container or provider hierarchy unless composition actually requires it.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P015-kiss-dependency-inversion-principle.md)

### P017 · KISS ↔ Make Illegal States Unrepresentable

**Evidence:** Convergent.  
**Mechanism:** A precise representation removes downstream branches, but elaborate type machinery can cost more understanding than the invalid states it excludes.  
**Decision consequence:** The model encodes only high-value stable invariants with the least elaborate adequate type or constructor.  
**Boundary:** A single local range check may be clearer than a novel advanced type encoding.  
**Resolution:** Compare the branches and invalid combinations removed with the representational burden added. Encode only stable, high-value invariants, using the least elaborate type or constructor that closes the relevant construction path.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P017-kiss-make-illegal-states-unrepresentable.md)

### P124 · Separation of Concerns ↔ Tell, Don't Ask

**Evidence:** Convergent.  
**Mechanism:** Tell, Don't Ask moves invariant behavior toward its data owner, while separation prevents that owner from absorbing unrelated persistence, presentation, or workflow.  
**Decision consequence:** The domain operation owns one transition and returns an outcome for an outer orchestrator.  
**Boundary:** Moving HTML rendering into an account object merely because it has data violates concern separation.  
**Resolution:** Separate infrastructure and presentation at real boundaries, but keep state-dependent invariant behavior with the state owner. Do not create forwarding layers merely to preserve a folder-level separation.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P124-separation-of-concerns-tell-don-t-ask.md)

### P138 · Single Responsibility Principle ↔ Tell, Don't Ask

**Evidence:** Convergent.  
**Mechanism:** Tell, Don't Ask pulls invariant behavior into its owner, while SRP limits that owner to behavior serving its cohesive actor.  
**Decision consequence:** A domain object owns its state transition but not unrelated persistence, reporting, or cross-aggregate workflow.  
**Boundary:** An invoice should own pricing invariants but need not own database storage or HTML rendering.  
**Resolution:** Let the actor/reason-for-change test establish the module boundary; within that boundary, place invariant-preserving behavior with its data. Split only behavior owned by a genuinely different actor.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P138-single-responsibility-principle-tell-don-t-ask.md)

### P159 · Convention over Configuration ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** Convention can reduce composition wiring, but hidden dependency resolution obscures DIP's ownership, lifetime, and source direction.  
**Decision consequence:** The composition remains inspectable even if standard conventions discover adapters.  
**Boundary:** Explicit construction is preferable when inferred resolution makes errors and lifetimes hard to trace.  
**Resolution:** Use convention at the composition edge for routine discovery, while keeping the policy-owned contract and dependency direction explicit. Switch to explicit construction when resolution, lifetime, or failure behavior becomes hard to inspect.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P159-convention-over-configuration-dependency-inversion-principle.md)

### P204 · Refactoring Toward Primitives ↔ Dependency Inversion Principle

**Evidence:** Convergent.  
**Mechanism:** Primitive-first favors direct platform use, while DIP may justify an adapter when the primitive is volatile or leaks irrelevant detail into policy.  
**Decision consequence:** The implementation uses the primitive directly unless a narrower stable domain contract removes real coupling.  
**Boundary:** A wrapper that only renames `JSON.stringify` adds indirection without inversion value.  
**Resolution:** Use the platform primitive directly by default. Add an adapter only when it narrows volatile, irrelevant, or incompatible semantics into a stable application contract; delete wrappers that only mirror or rename the primitive.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P204-refactoring-toward-primitives-dependency-inversion-principle.md)

### P209 · Refactoring Toward Primitives ↔ Law of Demeter

**Evidence:** Convergent.  
**Mechanism:** Directly reaching through a framework or SDK object graph uses primitives but couples callers to internal structure; a narrow adapter can be justified.  
**Decision consequence:** The design exposes only the stable capability or plain value while avoiding a wrapper that mirrors the whole primitive API.  
**Boundary:** Direct use of a stable flat standard value API creates no train-wreck dependency.  
**Resolution:** Use a stable flat primitive directly. Introduce a narrow adapter only when callers would otherwise traverse a volatile object graph, and expose a capability or plain value rather than duplicating the whole primitive API.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P209-refactoring-toward-primitives-law-of-demeter.md)

### P219 · Data-Driven Design ↔ Tell, Don't Ask

**Evidence:** Convergent.  
**Mechanism:** A central table places regular policy outside an object's methods, while Tell, Don't Ask places state-dependent invariant transitions with their owner.  
**Decision consequence:** Static mappings remain data-driven; transitions that require private mutable state remain domain operations, possibly consulting a table.  
**Boundary:** A status-to-label map is presentation data and does not belong inside the state-owning object.  
**Resolution:** Keep stable, stateless mappings in data. Keep transitions that depend on private mutable state as operations on the state owner; the operation may consult the table without moving the invariant itself into configuration.  
[Full assessment and evidence](research/principle-interactions/pair-dossiers/P219-data-driven-design-tell-don-t-ask.md)

## Conflict

The principles require mutually exclusive actions under the same context and preconditions.

No Conflict was published. Research found competing pressures, but every supported case could be reconciled by scope, precondition, order, or boundary choice. Treating those cases as absolute contradictions would erase the conditions under which each principle is valid.

## Coverage and proof of work

All 231 pairs remain auditable even though rejected and independent pairs do not receive filler prose in this guide.

- [Canonical profiles](research/principle-interactions/canonical-profiles.md)
- [Final 231-pair ledger](research/principle-interactions/pair-screening.csv)
- [Blind independent 231-pair ledger](research/principle-interactions/independent-screening.csv)
- [Adversarial review of all 82 proposed publications](research/principle-interactions/adversarial-review.md)
- [Review reconciliation](research/principle-interactions/review-reconciliation.md)
- [Source register](research/principle-interactions/source-register.md)
- [Chronological research journal](research/principle-interactions/research-journal.md)
- [Chapter-integrity checkpoint](research/principle-interactions/chapter-integrity.sha256)
- [Pair dossiers](research/principle-interactions/pair-dossiers/)

## Sources

Pair-level citations use source IDs in each dossier. Provenance, role, supported claims, and source limitations are recorded in the [source register](research/principle-interactions/source-register.md). The interaction study relies most heavily on:

- [Is Design Dead? — Martin Fowler](https://martinfowler.com/articles/designDead.html)
- [Continuous Design — Martin Fowler](https://www.martinfowler.com/ieeeSoftware/continuousDesign.pdf)
- [Beck Design Rules — Martin Fowler](https://martinfowler.com/bliki/BeckDesignRules.html)
- [The Rule of Three — Nicolas Carlo](https://understandlegacycode.com/blog/refactoring-rule-of-three/)
- [The Rule of Least Power — W3C TAG](https://www.w3.org/2001/tag/doc/leastPower.html)
- [Parse, don’t validate — Alexis King](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Common web application architectures — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures)
- [DIP in the Wild — Brett Schuchert](https://martinfowler.com/articles/dipInTheWild.html)
- [Simplify Your Code: Functional Core, Imperative Shell — Google Testing Blog](https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html)
- [Don’t Reinvent the Wheel: Towards Automatic Replacement of Custom Implementations with APIs](https://arxiv.org/abs/2208.07624)
- [Data-Driven Programming — The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/ch09s01.html)
- [Basics of the Unix Philosophy — The Art of Unix Programming](http://www.catb.org/esr/writings/taoup/html/ch01s06.html)
- [Remove Dead Code — Refactoring.com](https://refactoring.com/catalog/removeDeadCode.html)
- [The Ruby on Rails Doctrine](https://rubyonrails.org/doctrine#convention-over-configuration)
- [-2000 Lines of Code — Andy Hertzfeld](https://www.folklore.org/Negative_2000_Lines_Of_Code.html)

## Validated principle bundles

These bundles were derived only after the 78-edge interaction dataset was frozen and the bundle-free core guide passed verification. Each has one objective, three to six principles, a connected graph of published non-Overlap relationships, no unresolved Tension or Conflict, an application order, a counterexample, and dossier traceability. Accepted and rejected candidates are documented in [bundle assessments](research/principle-interactions/bundle-assessments.md).

Use a bundle's text block only as a candidate clause in a task-specific `CONTRACT.md`, generated immediately before implementation. Select the smallest applicable set, retain its counterexample as a boundary check, add task-specific acceptance and `Forbidden` sections, and keep the complete contract below 100 lines. Do not concatenate this catalog into standing repository instructions.

### B01 · Evidence-led minimal design

**Objective:** Deliver the smallest present solution while preventing premature or wrongly scoped abstraction.  
**Principles:** KISS; YAGNI; Rule of Three; DRY.  
**Order:** Establish the complete present requirement; implement the clearest adequate direct design; observe repeated cases; centralize only stable knowledge with one owner.  
**Evidence graph:** [P001](research/principle-interactions/pair-dossiers/P001-kiss-yagni.md), [P003](research/principle-interactions/pair-dossiers/P003-kiss-rule-of-three.md), [P022](research/principle-interactions/pair-dossiers/P022-yagni-dry.md), [P042](research/principle-interactions/pair-dossiers/P042-dry-rule-of-three.md).

```text
Implement only the current complete requirement using the clearest adequate design.
Do not add extension points for predicted reuse. Leave early duplication local until
repeated cases reveal one stable, jointly owned fact; then give that fact one authority.
```

**Counterexample:** A published protocol, security invariant, or regulated rule already has one authoritative definition; centralize it immediately rather than waiting for three local copies.

### B02 · Constrained data for regular variation

**Objective:** Replace repeated regular branching with one inspectable, trusted, minimally expressive data representation.  
**Principles:** Rule of Three; Data-Driven Design; DRY; Principle of Least Power; Parse, Don't Validate; Make Illegal States Unrepresentable.  
**Order:** Prove regularity from real cases; define one table and interpreter; keep the row format declarative; parse external rows and keys into precise values before use.  
**Evidence graph:** [P073](research/principle-interactions/pair-dossiers/P073-rule-of-three-data-driven-design.md), [P055](research/principle-interactions/pair-dossiers/P055-dry-data-driven-design.md), [P106](research/principle-interactions/pair-dossiers/P106-principle-of-least-power-data-driven-design.md), [P218](research/principle-interactions/pair-dossiers/P218-data-driven-design-parse-don-t-validate.md), [P217](research/principle-interactions/pair-dossiers/P217-data-driven-design-make-illegal-states-unrepresentable.md), [P222](research/principle-interactions/pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md).

```text
Use a table only after real cases reveal one stable algorithm with regular variation.
Make the table the single authority, keep its format declarative, and parse untrusted
rows or keys once into precise valid values before the shared interpreter runs.
```

**Counterexample:** The cases are genuinely different algorithms, or the proposed table stores arbitrary callbacks. Keep direct code.

### B03 · Trusted functional boundary

**Objective:** Convert weak external effects into trusted domain values before deterministic policy executes.  
**Principles:** Separation of Concerns; Functional Core, Imperative Shell; Dependency Inversion Principle; Parse, Don't Validate; Make Illegal States Unrepresentable.  
**Order:** Acquire effects in the shell; parse in the adapter; call policy with precise values and narrow capabilities; perform the resulting effects in the shell.  
**Evidence graph:** [P116](research/principle-interactions/pair-dossiers/P116-separation-of-concerns-functional-core-imperative-shell.md), [P120](research/principle-interactions/pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md), [P180](research/principle-interactions/pair-dossiers/P180-functional-core-imperative-shell-dependency-inversion-principle.md), [P183](research/principle-interactions/pair-dossiers/P183-functional-core-imperative-shell-parse-don-t-validate.md), [P213](research/principle-interactions/pair-dossiers/P213-dependency-inversion-principle-parse-don-t-validate.md), [P212](research/principle-interactions/pair-dossiers/P212-dependency-inversion-principle-make-illegal-states-unrepresentable.md), [P222](research/principle-interactions/pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md).

```text
Keep I/O and vendor details in the shell. Parse their weak values at the adapter into
precise domain types, invoke deterministic policy through domain-shaped contracts,
then perform the resulting effects at the boundary.
```

**Counterexample:** A decision requires a database lock and current transactional state; keep acquisition, validation, and decision within one transactional shell.

### B04 · Evidence-backed deletion

**Objective:** Remove project-owned machinery safely and within the scope of current work.  
**Principles:** KISS; Negative Code; Dead Code Elimination; Refactoring Toward Primitives; Boy Scout Rule.  
**Order:** Protect the contract; prove behavior dead or a primitive semantically adequate; delete the implementation and obsolete perimeter; keep incidental cleanup within the touched path.  
**Evidence graph:** [P012](research/principle-interactions/pair-dossiers/P012-kiss-negative-code.md), [P013](research/principle-interactions/pair-dossiers/P013-kiss-dead-code-elimination.md), [P014](research/principle-interactions/pair-dossiers/P014-kiss-refactoring-toward-primitives.md), [P187](research/principle-interactions/pair-dossiers/P187-negative-code-dead-code-elimination.md), [P188](research/principle-interactions/pair-dossiers/P188-negative-code-refactoring-toward-primitives.md), [P195](research/principle-interactions/pair-dossiers/P195-negative-code-boy-scout-rule.md), [P203](research/principle-interactions/pair-dossiers/P203-dead-code-elimination-boy-scout-rule.md).

```text
Within the touched path, preserve the current contract and remove only machinery proven
dead or made redundant by an exact existing primitive. Delete the obsolete perimeter too,
and stop when cleanup requires unbounded investigation outside the task.
```

**Counterexample:** A rarely executed recovery path remains operationally supported, or a large dependency would replace a small clear local function.

### B05 · Encapsulated domain commands

**Objective:** Turn weak input into a valid command and let the nearest state owner enforce the contextual transition without leaking object graphs.  
**Principles:** Parse, Don't Validate; Make Illegal States Unrepresentable; Tell, Don't Ask; Law of Demeter.  
**Order:** Parse a precise command; pass it directly to the nearest state owner; let the owner decide contextual validity and transition; return an explicit domain outcome.  
**Evidence graph:** [P222](research/principle-interactions/pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md), [P223](research/principle-interactions/pair-dossiers/P223-make-illegal-states-unrepresentable-tell-don-t-ask.md), [P226](research/principle-interactions/pair-dossiers/P226-parse-don-t-validate-tell-don-t-ask.md), [P227 — Reasoned Inference](research/principle-interactions/pair-dossiers/P227-parse-don-t-validate-law-of-demeter.md), [P229](research/principle-interactions/pair-dossiers/P229-tell-don-t-ask-law-of-demeter.md).

```text
Parse raw input into a precise command at the boundary, pass that command directly to
the nearest state owner, and let the owner enforce the contextual transition. Do not
make domain code traverse request, repository, or SDK object graphs to reconstruct it.
```

**Counterexample:** A renderer reads an immutable report value, or a parser traverses the syntax tree it owns; do not create forwarding commands merely to eliminate getters.

### B06 · Minimal policy-owned architecture

**Objective:** Isolate a demonstrated volatile detail behind the smallest cohesive, policy-owned, composable boundary.  
**Principles:** Separation of Concerns; Single Responsibility Principle; Composition over Inheritance; Dependency Inversion Principle; Law of Demeter.  
**Order:** Prove an independent actor or rate of change; define the narrow policy-owned capability; compose the adapter at the edge; keep the collaborator graph private.  
**Evidence graph:** [P112](research/principle-interactions/pair-dossiers/P112-separation-of-concerns-single-responsibility-principle.md), [P113](research/principle-interactions/pair-dossiers/P113-separation-of-concerns-composition-over-inheritance.md), [P120](research/principle-interactions/pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md), [P134](research/principle-interactions/pair-dossiers/P134-single-responsibility-principle-dependency-inversion-principle.md), [P147](research/principle-interactions/pair-dossiers/P147-composition-over-inheritance-dependency-inversion-principle.md), [P152](research/principle-interactions/pair-dossiers/P152-composition-over-inheritance-law-of-demeter.md), [P215](research/principle-interactions/pair-dossiers/P215-dependency-inversion-principle-law-of-demeter.md).

```text
Introduce an architectural boundary only for a demonstrated independent change or volatile
detail. Define the smallest policy-owned capability, compose its adapter at the edge, and
keep both the provider API and collaborator graph out of the policy.
```

**Counterexample:** A fixed internal helper has no external detail, independent actor, or variation axis. Call it directly.
