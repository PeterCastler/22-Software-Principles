# DOX framework

- DOX is highly performant AGENTS.md hierarchy installed here
- Agent must follow DOX instructions across any edits

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees
- Work products, source materials, instructions, records, assets, and durable docs must stay understandable from the nearest applicable AGENTS.md plus every parent AGENTS.md above it

## Read Before Editing

1. Read the root AGENTS.md
2. Identify every file or folder you expect to touch
3. Walk from the repository root to each target path
4. Read every AGENTS.md found along each route
5. If a parent AGENTS.md lists a child AGENTS.md whose scope contains the path, read that child and continue from there
6. Use the nearest AGENTS.md as the local contract and parent docs for repo-wide rules
7. If docs conflict, the closer doc controls local work details, but no child doc may weaken DOX

Do not rely on memory. Re-read the applicable DOX chain in the current session before editing.

## Update After Editing

Every meaningful change requires a DOX pass before the task is done.

Update the closest owning AGENTS.md when a change affects:

- purpose, scope, ownership, or responsibilities
- durable structure, contracts, workflows, or operating rules
- required inputs, outputs, permissions, constraints, side effects, or artifacts
- user preferences about behavior, communication, process, organization, or quality
- AGENTS.md creation, deletion, move, rename, or index contents

Update parent docs when parent-level structure, ownership, workflow, or child index changes. Update child docs when parent changes alter local rules. Remove stale or contradictory text immediately. Small edits that do not change behavior or contracts may leave docs unchanged, but the DOX pass still must happen.

## Hierarchy

- Root AGENTS.md is the DOX rail: project-wide instructions, global preferences, durable workflow rules, and the top-level Child DOX Index
- Child AGENTS.md files own domain-specific instructions and their own Child DOX Index
- Each parent explains what its direct children cover and what stays owned by the parent
- The closer a doc is to the work, the more specific and practical it must be

## Child Doc Shape

- Create a child AGENTS.md when a folder becomes a durable boundary with its own purpose, rules, responsibilities, workflow, materials, or quality standards
- Work Guidance must reflect the current standards of the project or user instructions; if there are no specific standards or instructions yet, leave it empty
- Verification must reflect an existing check; if no verification framework exists yet, leave it empty and update it when one exists

Default section order:
- Purpose
- Ownership
- Local Contracts
- Work Guidance
- Verification
- Child DOX Index

## Style

- Keep docs concise, current, and operational
- Document stable contracts, not diary entries
- Put broad rules in parent docs and concrete details in child docs
- Prefer direct bullets with explicit names
- Do not duplicate rules across many files unless each scope needs a local version
- Delete stale notes instead of explaining history
- Trim obvious statements, repeated rules, misplaced detail, and warnings for risks that no longer exist

## Closeout

1. Re-check changed paths against the DOX chain
2. Update nearest owning docs and any affected parents or children
3. Refresh every affected Child DOX Index
4. Remove stale or contradictory text
5. Run existing verification when relevant
6. Report any docs intentionally left unchanged and why

## User Preferences

When the user requests a durable behavior change, record it here or in the relevant child AGENTS.md

## Child DOX Index

- Root-owned files cover the library overview, cross-principle guide, repository-wide templates, and repository configuration.
- [Boy Scout Rule/AGENTS.md](Boy%20Scout%20Rule/AGENTS.md) — bounded incremental cleanup.
- [Composition over Inheritance/AGENTS.md](Composition%20over%20Inheritance/AGENTS.md) — behavior assembly through composition.
- [Convention over Configuration/AGENTS.md](Convention%20over%20Configuration/AGENTS.md) — shared defaults and explicit overrides.
- [DRY/AGENTS.md](DRY/AGENTS.md) — duplicated knowledge and authority.
- [Data-Driven Design/AGENTS.md](Data-Driven%20Design/AGENTS.md) — regular variation represented as data.
- [Dead Code Elimination/AGENTS.md](Dead%20Code%20Elimination/AGENTS.md) — evidence-backed removal.
- [Dependency Inversion Principle/AGENTS.md](Dependency%20Inversion%20Principle/AGENTS.md) — policy-owned dependency boundaries.
- [Functional Core, Imperative Shell/AGENTS.md](Functional%20Core,%20Imperative%20Shell/AGENTS.md) — pure decisions and effectful boundaries.
- [KISS/AGENTS.md](KISS/AGENTS.md) — minimum justified complexity.
- [Law of Demeter/AGENTS.md](Law%20of%20Demeter/AGENTS.md) — limited structural knowledge.
- [Make Illegal States Unrepresentable/AGENTS.md](Make%20Illegal%20States%20Unrepresentable/AGENTS.md) — precise domain representations.
- [Negative Code/AGENTS.md](Negative%20Code/AGENTS.md) — safe complexity reduction.
- [Occam's Razor/AGENTS.md](Occam's%20Razor/AGENTS.md) — removal of unsupported complexity.
- [Parse, Don't Validate/AGENTS.md](Parse,%20Don't%20Validate/AGENTS.md) — trusted values at boundaries.
- [Principle of Least Power/AGENTS.md](Principle%20of%20Least%20Power/AGENTS.md) — minimally expressive mechanisms.
- [Refactoring Toward Primitives/AGENTS.md](Refactoring%20Toward%20Primitives/AGENTS.md) — trusted primitives in place of custom machinery.
- [Rule of Three/AGENTS.md](Rule%20of%20Three/AGENTS.md) — evidence-timed abstraction.
- [Separation of Concerns/AGENTS.md](Separation%20of%20Concerns/AGENTS.md) — independently changing concerns.
- [Single Responsibility Principle/AGENTS.md](Single%20Responsibility%20Principle/AGENTS.md) — stakeholder-aligned responsibility.
- [Tell, Don't Ask/AGENTS.md](Tell,%20Don't%20Ask/AGENTS.md) — behavior and state ownership.
- [Unix Philosophy/AGENTS.md](Unix%20Philosophy/AGENTS.md) — focused composable tools.
- [YAGNI/AGENTS.md](YAGNI/AGENTS.md) — avoidance of speculative capability.
- [research/AGENTS.md](research/AGENTS.md) — evidence, screening, reconciliation, dossiers, and integrity records.
