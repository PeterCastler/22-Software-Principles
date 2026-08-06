# Minimal Design

This repository's primary deliverable is [`$minimal-design`](.agents/skills/minimal-design/SKILL.md), a portable Codex decision-filtration skill for software work. Its observable job is to apply the least justified amount of design process, keep engineering choices with the agent, surface only unresolved product choices to the user, and preserve only knowledge future developers truly need.

The 22 software principles, six validated bundles, interaction boundaries, tension resolutions, and rejected combinations are reasoning substrate rather than 22 standing rules. Their completed study is in the [Principle Interaction Guide](Principle%20Interaction%20Guide.md), with its proof ledger under [`research/principle-interactions/`](research/principle-interactions/).

## Runtime shape

1. Trigger broadly for software creation, change, debugging, refactoring, deletion, migration, architecture, or review.
2. Fast-exit after narrow inspection when the task is genuinely mechanical.
3. For uncertain work, inspect the nearest implementation, direct consumers, tests, contracts, and conventions before classifying it.
4. Work directly for Mechanical tasks, keep a short ephemeral micro-brief for Normal tasks, and keep an ephemeral design contract for Consequential tasks.
5. Interrupt with a Decision Gate only when repository evidence cannot resolve a consequential product choice and no safe reversible default exists.
6. Close by reviewing the implementation and verification evidence, then distill only stable knowledge that has a clear authoritative owner.

Briefs and design contracts stay in conversation by default. The [contract template](CONTRACT.template.md) is an optional export for consequential work when the user explicitly wants a shared file; it is not a mandatory repository artifact. Old task briefs are historical evidence, not current authority, unless active instructions link them.

Use the [Agent Workflow Integration Guide](Agent%20Workflow%20Integration%20Guide.md) for the full routing model, Decision Gate boundary, durable-promotion test, and interaction with `AGENTS.md`, specialist skills, and durable contracts.

## Install in another Codex environment

Installation is one-time per Codex environment; account-level synchronization is not assumed. Ask Codex:

```text
Use $skill-installer to install minimal-design from PeterCastler/miniCode at .agents/skills/minimal-design.
```

Start a new Codex session after installation. For a stronger backup trigger, optionally copy the concise [`global-agents-activation.md`](.agents/skills/minimal-design/assets/global-agents-activation.md) block into that machine's global `AGENTS.md`. The standalone package is the v1 source of truth; a plugin wrapper is intentionally deferred until managed public distribution or updating is needed.

## What “minimal” means here

Minimal code is the smallest complete solution that remains correct, secure, readable, testable, and easy to change. Line count is only weak evidence. A short expression that hides control flow can be harder to maintain than a few direct statements; a small interface can be more expensive than a little local duplication. The useful target is **minimum justified complexity**.

Each principle directory contains:

- `definitions/`: compact, attributed research notes. These are paraphrases, not page mirrors.
- `examples/`: original or substantially transformed before/after examples.
- `<Principle>.md`: a comprehensive standalone chapter with its definition, rationale, application method, worked example, limits, review checklist, agentic-coding guidance, and sources.

## Catalog

| Principle | Primary pressure it applies |
|---|---|
| [KISS](KISS/KISS.md) | Prefer the clearest adequate design. |
| [YAGNI](YAGNI/YAGNI.md) | Do not pay today for speculative capability. |
| [DRY](DRY/DRY.md) | Give changing knowledge one authority. |
| [Rule of Three](Rule%20of%20Three/Rule%20of%20Three.md) | Wait for evidence before abstracting repetition. |
| [Occam's Razor](Occam's%20Razor/Occam's%20Razor.md) | Prefer fewer unsupported assumptions and moving parts. |
| [Principle of Least Power](Principle%20of%20Least%20Power/Principle%20of%20Least%20Power.md) | Use the least expressive mechanism that suffices. |
| [Separation of Concerns](Separation%20of%20Concerns/Separation%20of%20Concerns.md) | Keep independently changing kinds of work apart. |
| [Single Responsibility Principle](Single%20Responsibility%20Principle/Single%20Responsibility%20Principle.md) | Group code that changes for the same stakeholder reason. |
| [Composition over Inheritance](Composition%20over%20Inheritance/Composition%20over%20Inheritance.md) | Combine independent behavior instead of multiplying subclasses. |
| [Convention over Configuration](Convention%20over%20Configuration/Convention%20over%20Configuration.md) | Make the ordinary case work from shared defaults. |
| [Unix Philosophy](Unix%20Philosophy/Unix%20Philosophy.md) | Build focused, composable tools with simple interfaces. |
| [Functional Core, Imperative Shell](Functional%20Core,%20Imperative%20Shell/Functional%20Core,%20Imperative%20Shell.md) | Keep decisions pure and effects at the boundary. |
| [Negative Code](Negative%20Code/Negative%20Code.md) | Treat safe deletion as progress. |
| [Dead Code Elimination](Dead%20Code%20Elimination/Dead%20Code%20Elimination.md) | Remove behavior and artifacts that cannot matter. |
| [Refactoring Toward Primitives](Refactoring%20Toward%20Primitives/Refactoring%20Toward%20Primitives.md) | Replace custom machinery with trusted existing capabilities. |
| [Dependency Inversion Principle](Dependency%20Inversion%20Principle/Dependency%20Inversion%20Principle.md) | Keep policy independent of volatile details when variation is real. |
| [Data-Driven Design](Data-Driven%20Design/Data-Driven%20Design.md) | Encode regular variation as data instead of repeated control flow. |
| [Make Illegal States Unrepresentable](Make%20Illegal%20States%20Unrepresentable/Make%20Illegal%20States%20Unrepresentable.md) | Use representations that exclude invalid combinations. |
| [Parse, Don't Validate](Parse,%20Don't%20Validate/Parse,%20Don't%20Validate.md) | Turn uncertain input into trusted domain data once. |
| [Tell, Don't Ask](Tell,%20Don't%20Ask/Tell,%20Don't%20Ask.md) | Put behavior beside the state and rules it needs. |
| [Law of Demeter](Law%20of%20Demeter/Law%20of%20Demeter.md) | Limit knowledge of collaborators' internals. |
| [Boy Scout Rule](Boy%20Scout%20Rule/Boy%20Scout%20Rule.md) | Make small, bounded improvements while changing code. |

## A practical order of precedence

When principles pull in different directions, use this order as a starting point:

1. Correctness, security, and explicit current requirements.
2. KISS and YAGNI: avoid introducing the need for cleanup.
3. Precise data models and boundary parsing: remove invalid cases and repeated checks.
4. Direct platform primitives and conventions: reuse solved behavior.
5. DRY only for duplicated knowledge; use the Rule of Three when the abstraction is uncertain.
6. Architectural boundaries only where responsibilities or rates of change are genuinely distinct.
7. Deletion and local cleanup after behavior is protected by tests or other evidence.

## Source and licensing policy

The source notes record titles, authors or publishers, URLs, access dates, and compact paraphrases of relevant ideas. They deliberately do not reproduce complete articles, book chapters, or source examples. Code examples in this library are original syntheses unless a file explicitly states otherwise.

Research last verified: 2026-07-15.
