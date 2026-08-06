# Operational Principle Cards

## Contents

KISS; YAGNI; DRY; Rule of Three; Occam's Razor; Principle of Least Power; Separation of Concerns; Single Responsibility Principle; Composition over Inheritance; Convention over Configuration; Unix Philosophy; Functional Core, Imperative Shell; Negative Code; Dead Code Elimination; Refactoring Toward Primitives; Dependency Inversion Principle; Data-Driven Design; Make Illegal States Unrepresentable; Parse, Don't Validate; Tell, Don't Ask; Law of Demeter; Boy Scout Rule.

## KISS

- **Apply when:** comparing complete designs with different concepts, states, dependencies, paths, or operating obligations.
- **Decide:** which adequate mechanism has the lowest whole-lifecycle complexity.
- **Do:** state the complete requirement and remove mechanisms not justified by a current constraint.
- **Stop:** do not equate simple with short, omit required quality, or reject structure that isolates real change or risk.

## YAGNI

- **Apply when:** capability, flexibility, compatibility, or an extension point has only a presumed future consumer.
- **Decide:** whether the capability is required now or safely deferrable.
- **Do:** implement the current complete requirement and record future ideas outside running design.
- **Stop:** current nonfunctional requirements and high-reversal-cost public, data, regulated, or hardware decisions are not speculative.

## DRY

- **Apply when:** several representations may encode one changing fact or intent.
- **Decide:** whether they share meaning, ownership, and reason to change.
- **Do:** give genuinely shared knowledge one narrow authority and derive other forms when worthwhile.
- **Stop:** similar syntax with independent owners is not duplication of knowledge; derivation tooling can cost more than local copies.

## Rule of Three

- **Apply when:** an abstraction is proposed from a few concrete cases.
- **Decide:** whether repeated evidence reveals stable common meaning and variation.
- **Do:** keep early cases local, compare them, then extract the smallest stable concept.
- **Stop:** three is not automatic, and an already-authoritative protocol or high-risk rule may justify earlier centralization.

## Occam's Razor

- **Apply when:** choosing among explanations or solutions that satisfy the same evidence and requirements.
- **Decide:** which candidate relies on fewer unsupported assumptions and entities.
- **Do:** test the cheaper adequate explanation first and add entities only when evidence warrants them.
- **Stop:** parsimony is not proof; rare high-impact risks and unequal adequacy require separate treatment.

## Principle of Least Power

- **Apply when:** choosing between data, declarations, schemas, queries, templates, callbacks, scripts, plugins, or general code.
- **Decide:** the least expressive mechanism that remains adequate and comprehensible.
- **Do:** prefer constrained representation before arbitrary execution.
- **Stop:** do not contort stateful workflows or rich recovery into an underpowered pseudo-language.

## Separation of Concerns

- **Apply when:** policy, effects, presentation, authorization, data, or operations have different rules, owners, or rates of change.
- **Decide:** the cheapest boundary that creates meaningful independence.
- **Do:** isolate coherent decisions and recombine through visible values or contracts.
- **Stop:** do not multiply layers, files, or services when one invariant and one owner keep the work cohesive.

## Single Responsibility Principle

- **Apply when:** a module responds to demonstrated changes requested by different actors or business functions.
- **Decide:** the cohesive ownership boundary.
- **Do:** group changes for the same reason and separate independently owned responsibilities.
- **Stop:** responsibility is not method count; avoid speculative actors, tiny classes, and fragmented cohesive algorithms.

## Composition over Inheritance

- **Apply when:** independent behavior varies and reuse does not require genuine subtype semantics.
- **Decide:** whether fixed code, functions, collaborators, composition, or inheritance best represents variation.
- **Do:** compose the lightest focused behaviors near the assembly boundary.
- **Stop:** retain inheritance for real subtypes and framework contracts; do not invent strategies for fixed behavior.

## Convention over Configuration

- **Apply when:** repeated ordinary choices can follow a discoverable shared default.
- **Decide:** which defaults are stable and which exceptions need explicit configuration.
- **Do:** make the normal case work without repeated declarations and keep override precedence visible.
- **Stop:** do not hide domain policy, lifetime, resolution, or dominant exceptions behind naming magic.

## Unix Philosophy

- **Apply when:** designing CLI tools, pipelines, automation, services, or composable component interfaces.
- **Decide:** the focused responsibility and simple interchange contract.
- **Do:** use standard formats, explicit streams, meaningful exit behavior, and reliable existing tools.
- **Stop:** do not split cohesive application logic into processes or force opaque internal values through text.

## Functional Core, Imperative Shell

- **Apply when:** deterministic policy is materially mixed with I/O or other effects.
- **Decide:** which values and decisions can cross a pure/effectful boundary.
- **Do:** acquire effects at the edge, run deterministic policy on values, then perform resulting effects.
- **Stop:** keep lock-dependent, transactional decisions together; do not perform a purity rewrite for simple effect-only CRUD.

## Negative Code

- **Apply when:** behavior can be preserved with less project-owned machinery.
- **Decide:** whether deletion reduces lifecycle obligations rather than only line count.
- **Do:** protect the contract, remove superseded code and glue, and verify semantic coverage.
- **Stop:** code golf, hidden dependency weight, or deletion of supported behavior is not progress.

## Dead Code Elimination

- **Apply when:** behavior or artifacts may be unobservable within a defined supported boundary.
- **Decide:** liveness across direct calls, registration, reflection, flags, config, APIs, migrations, and operations.
- **Do:** prove the whole slice dead, respect deprecation, then remove implementation and perimeter.
- **Stop:** a single search cannot disprove dynamic, external, rare recovery, or compatibility consumers.

## Refactoring Toward Primitives

- **Apply when:** custom parsing, scheduling, caching, concurrency, serialization, authentication, or similar machinery may duplicate an existing capability.
- **Decide:** whether a repository, language, platform, or approved dependency primitive matches the exact contract economically.
- **Do:** verify semantics and supported versions, adopt the primitive, and remove obsolete glue.
- **Stop:** avoid wrappers that merely rename APIs and dependencies whose weight exceeds the clear local implementation.

## Dependency Inversion Principle

- **Apply when:** stable policy depends on a demonstrated volatile provider or irrelevant external detail.
- **Decide:** whether a narrow policy-owned capability materially reduces coupling.
- **Do:** express the contract in domain language, adapt at the edge, and assemble explicitly.
- **Stop:** call stable internal helpers directly; do not add interfaces, containers, or provider hierarchies for imagined variation or mocks alone.

## Data-Driven Design

- **Apply when:** several cases share one stable algorithm with regular variation.
- **Decide:** whether a typed table and one interpreter express the variation more directly than repeated branches.
- **Do:** define one inspectable data authority with a clear schema and update path.
- **Stop:** keep genuinely different algorithms in code; callbacks in configuration create a covert rules engine.

## Make Illegal States Unrepresentable

- **Apply when:** contradictory flags, optional combinations, invalid transitions, or repeated guards reflect stable state invariants.
- **Decide:** which high-value invalid combinations can be excluded at construction.
- **Do:** use the least elaborate adequate union, enum, set, map, derived value, or smart constructor.
- **Stop:** runtime authorization, freshness, resources, and concurrent facts remain mutable; a local check may be clearer than advanced type machinery.

## Parse, Don't Validate

- **Apply when:** weak external values enter a domain that needs precise trusted data.
- **Decide:** the boundary, accepted forms, normalization, error form, and trusted output representation.
- **Do:** parse once into the needed value and propagate that representation inward.
- **Stop:** retain authorization, concurrency, freshness, availability, and resource checks; do not build a parser framework for one small object.

## Tell, Don't Ask

- **Apply when:** callers repeatedly query state, decide an invariant-sensitive transition, then mutate the owner.
- **Decide:** the nearest state owner and meaningful domain command.
- **Do:** place the transition with its state and return an explicit outcome.
- **Stop:** queries, rendering, analytics, and transparent immutable values remain legitimate; avoid vague commands and anemic forwarding.

## Law of Demeter

- **Apply when:** callers traverse nested collaborator, request, repository, ORM, or vendor graphs.
- **Decide:** whether to pass a plain value or expose the smallest meaningful near-neighbor operation.
- **Do:** limit knowledge of volatile ownership structure while keeping cost and failure visible.
- **Stop:** do not count dots mechanically or replace transparent value access with forests of forwarding methods.

## Boy Scout Rule

- **Apply when:** a safe adjacent improvement lies on the execution path already being changed.
- **Decide:** whether cleanup is behavior-preserving, bounded, and supported by current understanding.
- **Do:** make the small improvement and verify it with the task.
- **Stop:** separate work that needs new product, architecture, operational, or repository-wide judgment; exclude generated, vendored, frozen, and mirrored files.
