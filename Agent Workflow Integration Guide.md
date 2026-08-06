# Agent Workflow Integration Guide

## Purpose

This guide explains how [`$minimal-design`](.agents/skills/minimal-design/SKILL.md) filters software decisions, how its automatic recall is reinforced, and where temporary reasoning or durable knowledge belongs. The skill applies the least justified process rather than making every software request perform architecture work.

The standalone principle chapters remain authoritative for definitions, application methods, limits, and sources. The [Principle Interaction Guide](Principle%20Interaction%20Guide.md) remains authoritative for pair relationships, evidence grades, and validated bundles. This document concerns packaging and workflow integration only.

## Placement decision

| File | Use it for | Do not use it for |
|---|---|---|
| `AGENTS.md` | Stable instructions that should govern nearly every task in a repository or subtree. | Long explanations, conditional checklists, or all 22 principles copied wholesale. |
| `SKILL.md` | A conditionally activated procedure with a recognizable trigger, sequence, checks, and linked references. | Passive background reading or unconditional project policy. |
| `CONTRACT.md` | An explicitly requested shared export of one consequential task's current design contract. | A mandatory artifact, reusable policy, or unchanged input to later tasks. |
| `CONTRACTS.md` | A durable catalog of several named API, schema, security, migration, compatibility, or subsystem contracts. | A pluralized task brief or a substitute for the current task's `CONTRACT.md`. |

Use this test:

1. If the rule remains true for almost every task in a subtree, put a concise operational form in the nearest `AGENTS.md`.
2. If application requires a trigger, diagnostic method, tools, or specialized sequence, put the method in a `SKILL.md` and link its supporting references.
3. If applicability depends on current evidence, risk, scope, or a counterexample, keep it in the current conversation by default; export `CONTRACT.md` only when the user requests a shared artifact.
4. If several durable external or domain promises must be named and maintained together, document them in `CONTRACTS.md` and make the owning `AGENTS.md` say when they must be consulted.

Repository, platform, safety, and applicable `AGENTS.md` instructions remain authoritative. A skill or task contract may specialize or narrow them but must not weaken them.

## Decision-filtration workflow

The skill routes each software-changing, debugging, architectural, or review request through the following sequence:

1. **Prompt triage:** a clearly mechanical request does not load principle research.
2. **Mechanical inspection:** inspect applicable instructions, the named location, and the nearest relevant test or contract. Fast-exit if no design-bearing evidence appears.
3. **Targeted reconnaissance:** for uncertain work, inspect relevant symbols, the nearest implementation, direct callers, tests, contracts, and conventions. Broaden only when evidence requires it.
4. **Final classification:** Mechanical work proceeds directly; Normal work uses an ephemeral micro-brief; Consequential work uses an ephemeral design contract.
5. **Implementation:** follow the active brief while language-, framework-, security-, testing-, and artifact-specific skills retain control of their procedures.
6. **Closeout:** review the diff, brief, unplanned changes, and verification evidence, then distill durable knowledge.

“No principle or bundle applies” is a valid and preferred result. Use at most one primary bundle unless evidence establishes two distinct decision surfaces. The routing formats and loading rules live in the skill's [workflow reference](.agents/skills/minimal-design/references/workflow.md).

## Decision Gate

A Decision Gate is an interruption, not a fourth and larger document tier. Use it only when a consequential choice changes user-visible behavior, compatibility, data retention, destructive migration, supported platforms, operational policy, or a comparable product promise; repository evidence cannot determine the answer; and no safe reversible default exists.

Ask the smallest product-facing question and pause before the first action that would commit to an answer. Reversible technical choices, ordinary implementation details, design-principle selection, and engineering trade-offs remain agent responsibilities.

## Temporary and durable artifacts

Keep micro-briefs and design contracts in conversation. Use [CONTRACT.template.md](CONTRACT.template.md) only when the user explicitly requests a collaborative export for consequential work, and keep that export below 100 lines. A previous brief or contract is non-authoritative unless current instructions link it.

Promote a learned fact only when all four conditions hold:

- it remains relevant beyond the completed task;
- future work could make a wrong decision without it;
- it is stable enough to be policy or maintained documentation rather than speculation; and
- an existing authoritative document or clear new owner exists.

Write only the distilled fact into the nearest authority. Update or remove stale documentation when it is in scope and contradicted by evidence; otherwise ignore it as authority and report the contradiction.

Create `CONTRACTS.md` only when a durable boundary owns multiple independently named commitments. Each entry should identify its owner, consumers, compatibility promise, permitted changes, verification, and deprecation path.

## Recommended global operating rail

A root `AGENTS.md` normally needs only a short rail derived from the principles:

- implement the current complete requirement and preserve explicit contracts;
- inspect applicable instructions, conventions, and existing capabilities before designing;
- prefer the clearest adequate solution and avoid speculative capability;
- require evidence before introducing an abstraction or deleting behavior;
- keep incidental cleanup bounded to the touched path;
- preserve unrelated user work and verify changes proportionately to risk;
- update the nearest durable documentation when ownership or workflow changes.

These clauses are a candidate shape, not text to copy blindly. Project-specific safety, architecture, data, operational, and regulatory rules take precedence.

## When to use child `AGENTS.md` files

Place specialized principle guidance in a child `AGENTS.md` when a folder is a durable boundary with its own domain, technology, ownership, risk, or verification method. Typical examples include:

- input adapters that always parse untrusted data into precise domain values;
- a domain core that owns invariants and excludes vendor types;
- CLI packages that must preserve stream and exit-code conventions;
- generated, vendored, or migration-frozen folders where cleanup rules differ;
- regulated modules with explicit state, audit, or compatibility contracts.

Prefer the closest applicable child instruction over broad root rules. Do not create a child file for a temporary task or repeat parent guidance without a local specialization.

## Recall and portable installation

The public package lives at [`.agents/skills/minimal-design/`](.agents/skills/minimal-design/). Its broad frontmatter description is the primary automatic trigger and `policy.allow_implicit_invocation` is enabled. The optional [`global-agents-activation.md`](.agents/skills/minimal-design/assets/global-agents-activation.md) block is a backup instruction for a root or global `AGENTS.md`; it reinforces invocation, fast exit, re-entry on new evidence, Decision Gate ownership, and closeout distillation without duplicating the skill.

Install the GitHub path `PeterCastler/miniCode/.agents/skills/minimal-design` with `$skill-installer` once in each Codex environment, then start a new session. Account-level automatic syncing is not assumed. The standalone skill remains the v1 source of truth; defer a plugin wrapper until public distribution or managed updating justifies one.

## Trigger evaluation

The durable [36-case golden set](evaluation/trigger-cases.jsonl) covers 12 design-bearing software prompts, 8 mechanical fast exits, 8 software-adjacent negatives, and 8 non-software or competing-domain negatives. It includes four product-ambiguity Decision Gates paired with engineering-only controls.

Forward tests use fresh disposable Codex sessions and repositories below `evaluation/.tmp/`. Test metadata-only invocation first; retest only false negatives and borderline cases with the activation asset. Record the skill hash, model, Codex version, date, scoring method, and asset presence. Change one metadata field or instruction region per cycle, for at most three focused cycles.

Acceptance requires at least 11/12 design activations, 7/8 correct mechanical activations and fast exits, no more than 1/8 software-adjacent captures, no non-software captures, valid gates for every product-owned ambiguity, no gates for engineering controls, no persisted brief or contract in any fixture, and no non-software false positive introduced by the activation asset.

## Principle-by-principle integration

### 1. [KISS](KISS/KISS.md)

**Agent workflow:** Establish the smallest complete outcome, compare adequate designs by lifecycle complexity, and finish by removing newly introduced concepts that do not improve correctness, security, readability, testing, or operation.

**Separate `SKILL.md`:** Usually include KISS in an evidence-led design or review skill. A standalone skill is useful for greenfield architecture, prototypes, internal tools, or over-engineered systems.

**Task contract:** Name the current outcome and forbid unjustified wrappers, factories, extension points, fallback modes, services, configuration, or compatibility layers.

**Global/local `AGENTS.md`:** Apply a concise minimum-justified-complexity rule almost everywhere. Clarify that simple means adequate across the lifecycle, not shortest source code.

### 2. [YAGNI](YAGNI/YAGNI.md)

**Agent workflow:** Separate current requirements from plausible future requirements. Report future possibilities without encoding them unless an existing contract requires them.

**Separate `SKILL.md`:** Package with scope control and evidence-led design for product iteration, migrations, greenfield systems, and platform work.

**Task contract:** Make non-goals explicit and name future providers, formats, platforms, modes, or extension systems that must not be introduced.

**Global/local `AGENTS.md`:** Use as a broad default in iterative and maintenance projects, with explicit exceptions for published protocols, compatibility, security invariants, and regulated requirements.

### 3. [DRY](DRY/DRY.md)

**Agent workflow:** Identify duplicated knowledge, its owner, and whether all occurrences must change together. Do not infer shared meaning from similar text alone.

**Separate `SKILL.md`:** A semantic-duplication audit skill benefits monorepos and systems where policy spans code, schemas, configuration, tests, and documentation.

**Task contract:** Name the duplicated fact, its new authority, consumers, and boundaries. Forbid abstractions that join independently changing domains.

**Global/local `AGENTS.md`:** Use where canonical schemas, constants, generated artifacts, or policies matter. State "one authority per changing fact," not "deduplicate all code."

### 4. [Rule of Three](Rule%20of%20Three/Rule%20of%20Three.md)

**Agent workflow:** Preserve early duplication while comparing real cases. Around the third occurrence, inspect semantics, variation, and ownership before extracting an abstraction.

**Separate `SKILL.md`:** Useful for legacy refactoring, component libraries, evolving domains, and repositories accumulating generic agent-created helpers.

**Task contract:** List the concrete occurrences, stable common behavior, relevant differences, owner, and narrow extraction scope.

**Global/local `AGENTS.md`:** Apply in greenfield and evolving domains as an evidence rule rather than a numeric law. Allow immediate centralization of an already-authoritative protocol, security, or regulated rule.

### 5. [Occam's Razor](Occam's%20Razor/Occam's%20Razor.md)

**Agent workflow:** Rank explanations by evidence, test the least assumption-heavy adequate explanation first, and compare only designs that satisfy the same requirements.

**Separate `SKILL.md`:** A strong standalone diagnostic or architecture-comparison skill for incidents, flaky systems, performance investigations, and platform selection.

**Task contract:** Record supported assumptions, rejected hypotheses or architectures, escalation evidence, and the stopping rule.

**Global/local `AGENTS.md`:** Useful in troubleshooting and small-to-medium systems. Preserve explicit attention to high-impact security and data-integrity risks.

### 6. [Principle of Least Power](Principle%20of%20Least%20Power/Principle%20of%20Least%20Power.md)

**Agent workflow:** Consider direct values, constrained types, schemas, tables, queries, and static configuration before scripts, callbacks, plugins, or interpreters.

**Separate `SKILL.md`:** Useful for configuration design, policy systems, DSLs, automation, build infrastructure, and security review.

**Task contract:** Specify the permitted expressiveness, why it suffices, and which executable mechanisms are forbidden.

**Global/local `AGENTS.md`:** Strong in security-sensitive, infrastructure, declarative, and supply-chain projects. Require a concrete missing capability before choosing a more powerful mechanism.

### 7. [Separation of Concerns](Separation%20of%20Concerns/Separation%20of%20Concerns.md)

**Agent workflow:** Identify independently changing work, introduce the smallest useful boundary, and keep the resulting execution path easy to trace.

**Separate `SKILL.md`:** Useful for backend, ETL, and UI refactors that must separate policy, I/O, presentation, authorization, or telemetry.

**Task contract:** Define the concerns, their owners, allowed dependency direction, and any layers or modules that are intentionally unnecessary.

**Global/local `AGENTS.md`:** Apply in multi-domain or effects-heavy systems, preferably through concrete child rules. Do not require template-generated controller, service, and repository layers.

### 8. [Single Responsibility Principle](Single%20Responsibility%20Principle/Single%20Responsibility%20Principle.md)

**Agent workflow:** Identify which actor or business function requests each kind of change and split only responsibilities with genuinely different change reasons.

**Separate `SKILL.md`:** Useful for responsibility mapping in enterprise systems, monorepos, organizational boundaries, and large modules with unclear ownership.

**Task contract:** Name the actor, responsibility, included changes, and responsibilities that must remain elsewhere.

**Global/local `AGENTS.md`:** Best in long-lived, multi-team, or regulated domains and usually more precise in domain-level child files than at the root.

### 9. [Composition over Inheritance](Composition%20over%20Inheritance/Composition%20over%20Inheritance.md)

**Agent workflow:** Prefer functions, delegates, components, and narrow structural contracts for independent behavior. Retain inheritance for genuine subtypes or framework requirements.

**Separate `SKILL.md`:** Useful for OO redesign, GUI frameworks, plugin systems, games, simulations, and hierarchy-heavy legacy code.

**Task contract:** Define the demonstrated variation axes, permitted components, and framework inheritance that must be preserved.

**Global/local `AGENTS.md`:** Apply in OO subtrees with recurring hierarchy problems. Do not impose it on functional or data-oriented code where inheritance is not a decision surface.

### 10. [Convention over Configuration](Convention%20over%20Configuration/Convention%20over%20Configuration.md)

**Agent workflow:** Discover repository and framework conventions before introducing layouts or configuration. Configure only meaningful exceptions and make precedence visible.

**Separate `SKILL.md`:** A strong fit for repository onboarding, scaffolding, convention auditing, and framework-specific project creation.

**Task contract:** List the conventions followed and the exact exception that justifies additional configuration.

**Global/local `AGENTS.md`:** Appropriate for monorepos, framework applications, and scaffolded projects. Document stable naming, locations, discovery, and commands without hiding domain policy in naming magic.

### 11. [Unix Philosophy](Unix%20Philosophy/Unix%20Philosophy.md)

**Agent workflow:** Prefer focused tools, standard formats, composable interfaces, explicit streams, meaningful exit codes, and reliable existing utilities.

**Separate `SKILL.md`:** A strong standalone workflow for CLI design, developer tools, automation, build systems, and data pipelines.

**Task contract:** Specify stdin, stdout, stderr, exit codes, formats, idempotence, and composition expectations.

**Global/local `AGENTS.md`:** Apply to CLI, ETL, operations, and automation repositories or command-oriented subtrees. Do not split cohesive application logic into processes merely to appear Unix-like.

### 12. [Functional Core, Imperative Shell](Functional%20Core,%20Imperative%20Shell/Functional%20Core,%20Imperative%20Shell.md)

**Agent workflow:** Acquire effects at the edge, parse external values, run deterministic policy on plain values, and perform resulting effects in the shell.

**Separate `SKILL.md`:** Useful for services, event handlers, serverless functions, ETL, calculations, and effect-heavy code that is difficult to test.

**Task contract:** Identify effect boundaries, pure inputs and outputs, transaction requirements, and decisions that must remain within a transactional shell.

**Global/local `AGENTS.md`:** Apply where deterministic policy is materially mixed with I/O. Avoid mandatory purity rewrites for simple CRUD or tightly transactional work.

### 13. [Negative Code](Negative%20Code/Negative%20Code.md)

**Agent workflow:** Treat deletion and simplification as implementation options, prove semantic coverage, remove obsolete implementation and glue, and verify preserved behavior.

**Separate `SKILL.md`:** Useful for simplification campaigns, post-migration cleanup, dependency reduction, and mature systems with accumulated machinery.

**Task contract:** Name deletion candidates, preserved behavior, replacement evidence, verification, and a prohibition on compression for appearance.

**Global/local `AGENTS.md`:** Useful in mature or legacy repositories only when paired with evidence and bounded scope requirements.

### 14. [Dead Code Elimination](Dead%20Code%20Elimination/Dead%20Code%20Elimination.md)

**Agent workflow:** Establish liveness across direct calls, reflection, registration, flags, configuration, scripts, public APIs, migrations, and operations before removing the whole dead slice.

**Separate `SKILL.md`:** One of the strongest standalone candidates because feature retirement and liveness investigations have distinctive evidence and deprecation steps.

**Task contract:** Define the liveness boundary, supported consumers, deprecation obligations, removal perimeter, and broad verification.

**Global/local `AGENTS.md`:** Useful in long-lived services and feature-flag-heavy projects. Require flag lifecycle discipline and forbid declaring code dead from a single search.

### 15. [Refactoring Toward Primitives](Refactoring%20Toward%20Primitives/Refactoring%20Toward%20Primitives.md)

**Agent workflow:** Search the repository, language, platform, and approved dependencies before writing custom machinery. Verify exact semantics and remove superseded glue.

**Separate `SKILL.md`:** Useful for API replacement, library evaluation, framework migration, and replacement of custom parsing, scheduling, caching, or concurrency code.

**Task contract:** Name the primitive, semantic-equivalence requirements, supported versions, dependency cost, wrapper policy, and old implementation to remove.

**Global/local `AGENTS.md`:** Strong in platform-rich or security-sensitive systems, especially for cryptography, serialization, and authentication, while retaining dependency-cost judgment.

### 16. [Dependency Inversion Principle](Dependency%20Inversion%20Principle/Dependency%20Inversion%20Principle.md)

**Agent workflow:** Prove volatility or external coupling, define a narrow capability in domain vocabulary, implement its adapter at the edge, and assemble it explicitly.

**Separate `SKILL.md`:** Useful for vendor integrations, multiple providers, hardware or filesystem boundaries, test seams, and durable domain cores.

**Task contract:** Record volatility evidence, the policy-owned interface, dependency direction, composition point, and forbidden vendor-type leakage.

**Global/local `AGENTS.md`:** Appropriate in long-lived, multi-provider, infrastructure-heavy, or regulated systems. Apply it to meaningful core boundaries rather than every helper.

### 17. [Data-Driven Design](Data-Driven%20Design/Data-Driven%20Design.md)

**Agent workflow:** Detect a stable shared algorithm with regular variation, represent cases in the simplest typed table, and operate through one inspectable interpreter.

**Separate `SKILL.md`:** Useful for state machines, protocol mappings, localization, routing, pricing, permissions, and repetitive regular branches.

**Task contract:** Define the row schema, authority, ownership, update path, parsing rules, and prohibition on arbitrary callbacks or covert rules engines.

**Global/local `AGENTS.md`:** Suitable for mapping-heavy, compiler, protocol, catalog, or workflow repositories. Do not globalize it where cases contain genuinely different algorithms.

### 18. [Make Illegal States Unrepresentable](Make%20Illegal%20States%20Unrepresentable/Make%20Illegal%20States%20Unrepresentable.md)

**Agent workflow:** Model the state space before adding checks. Prefer unions, precise enums, sets, maps, derived values, and narrow constructors over contradictory flags and optional combinations.

**Separate `SKILL.md`:** A strong domain-modeling, API-schema, state-machine, or type-driven refactoring workflow.

**Task contract:** Enumerate legal states and transitions, construction paths, serialization compatibility, and runtime facts that remain externally mutable.

**Global/local `AGENTS.md`:** Strong in finance, healthcare, security, safety-critical systems, and typed domain cores. Scope it carefully around transient UI state and external facts.

### 19. [Parse, Don't Validate](Parse,%20Don't%20Validate/Parse,%20Don't%20Validate.md)

**Agent workflow:** Parse uncertain input at system boundaries into precise internal values, return structured errors, and retain checks for authorization, concurrency, freshness, and resources.

**Separate `SKILL.md`:** Useful for APIs, CLI arguments, configuration, file ingestion, messaging, and data import.

**Task contract:** Specify the trust boundary, accepted forms, normalization, rejection behavior, error taxonomy, and trusted output type.

**Global/local `AGENTS.md`:** Appropriate in input-heavy and security-sensitive systems, often through child instructions for adapters, controllers, or ingestion.

### 20. [Tell, Don't Ask](Tell,%20Don't%20Ask/Tell,%20Don't%20Ask.md)

**Agent workflow:** Detect repeated query-decide-mutate sequences, move invariant-preserving transitions to the nearest state owner, and return explicit domain outcomes.

**Separate `SKILL.md`:** Useful for rich domain models, transactional aggregates, workflow engines, and encapsulation refactors.

**Task contract:** Name the command, state owner, invariant, contextual checks, outcome, and transaction semantics.

**Global/local `AGENTS.md`:** Apply to domain-model subtrees, not universally to reporting, rendering, analytics, or transparent value processing.

### 21. [Law of Demeter](Law%20of%20Demeter/Law%20of%20Demeter.md)

**Agent workflow:** Treat long object navigation as a review signal, distinguish transparent values from nested ownership, and pass needed values or expose the smallest meaningful operation.

**Separate `SKILL.md`:** Useful for coupling reviews in ORM-, SDK-, framework-, and object-graph-heavy systems.

**Task contract:** Define allowed collaborators, prohibit leaking request, repository, or vendor graphs, and preserve visible cost and error behavior.

**Global/local `AGENTS.md`:** Valuable at layered, plugin, SDK, and domain boundaries. Reject mechanical dot counting and forests of forwarding methods.

### 22. [Boy Scout Rule](Boy%20Scout%20Rule/Boy%20Scout%20Rule.md)

**Agent workflow:** Make only small adjacent improvements on the touched execution path, preserve behavior, and separate cleanup once it requires materially new judgment.

**Separate `SKILL.md`:** Usually part of maintenance or evidence-backed deletion. A standalone closeout skill may inspect only the changed area for safe local cleanup.

**Task contract:** Define the touched path and cleanup budget; forbid repository-wide formatting, incidental dependency upgrades, public-API redesign, and unrelated refactoring.

**Global/local `AGENTS.md`:** A strong global maintenance rule with strict scope controls. Exclude generated, vendored, migration-frozen, or externally mirrored files where local cleanup is inappropriate.

## Common misplacements and counterexamples

- **All principles in root `AGENTS.md`:** Conditional design guidance becomes permanent noise and conflicting slogans. Keep the root rail short and move specialized rules closer to their decision surface.
- **A handbook-sized `SKILL.md`:** Passive research crowds out actionable routing. Keep the skill concise and link to the chapters and interaction guide.
- **A mandatory or reusable `CONTRACT.md`:** Writing every transient decision into the repository creates stale authority. Keep reasoning ephemeral; export a fresh consequential contract only when collaboration requires it.
- **`CONTRACTS.md` as a policy dump:** Durable contracts need named owners, consumers, compatibility promises, verification, and deprecation paths; otherwise use ordinary documentation.
- **DRY from textual similarity:** Coincidentally similar code may have different owners. Centralize only one changing fact.
- **Rule of Three as arithmetic:** Three occurrences do not prove one abstraction; one authoritative protocol may justify centralization before three.
- **Separation or SRP as file multiplication:** More files, layers, interfaces, or services do not prove independent responsibilities.
- **DIP for every dependency:** A fixed internal helper with no volatility or policy boundary should normally be called directly.
- **Data-driven design as callbacks in configuration:** If cases contain different algorithms or arbitrary executable behavior, keep direct code.
- **Precise types as total validation:** Types do not permanently prove authorization, freshness, concurrent state, or resource availability.
- **Tell Don't Ask or Law of Demeter as getter bans:** Queries over transparent values remain legitimate; avoid vague commands and forwarding forests.
- **Negative Code or dead-code elimination by line count:** Preserve supported recovery paths, dynamic registrations, public contracts, and behavior not disproven by evidence.
- **Boy Scout Rule as roaming authority:** Incidental cleanup stops at the touched path or when it requires new product, architecture, or operational judgment.
