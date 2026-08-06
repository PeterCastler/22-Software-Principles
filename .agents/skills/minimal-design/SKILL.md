---
name: minimal-design
description: Use for software-development requests that may create, modify, debug, refactor, delete, migrate, review, or architect code, tests, configuration, data models, dependencies, APIs, or durable technical documentation. Trigger broadly before implementation or review, even when a task appears small; triage and fast-exit truly mechanical work. Filter design decisions, surface only unresolved product decisions to the user, and distill durable knowledge after implementation. Do not use for non-software work, purely explanatory questions, or repository status, inventory, navigation, or orientation requests with no requested diagnosis, review, or change.
---

# Minimal Design

Filter decisions so software work uses only the code, process, human attention, and permanent documentation justified by current evidence.

## Route the work

1. Read the request and applicable repository instructions. Do not load principle references yet.
2. If the work appears mechanical, inspect only the named location, its nearest relevant test, and an explicit contract if one exists. Implement directly when the outcome is fully specified and no design-bearing signal appears.
3. Otherwise perform targeted reconnaissance: locate the implementation, direct callers, tests, contracts, and established conventions. Broaden only when evidence requires it.
4. Classify after reconnaissance:
   - **Mechanical:** make the direct change; create no reasoning artifact.
   - **Normal:** before mutation, state an ephemeral micro-brief in the conversation using the labels in `workflow.md`.
   - **Consequential:** before mutation, state an ephemeral design contract in the conversation using the labels in `workflow.md`, unless a Decision Gate pauses the work first.
5. Read [workflow.md](references/workflow.md) for classification, artifact formats, Decision Gates, closeout, and distillation whenever the task is Normal or Consequential. Keep the artifact compact, but do not replace its fields with unlabeled prose.

## Apply guidance proportionately

- Treat no principle or bundle as the preferred result when none changes the decision.
- For one decision surface, search [principles.md](references/principles.md) and read only the matching principle card.
- Before combining principles, read [bundles.md](references/bundles.md) and [boundaries.md](references/boundaries.md). Select at most one primary bundle unless evidence establishes two distinct decision surfaces.
- Preserve every selected principle's preconditions and stopping boundary. Do not infer an interaction absent from the accepted set.
- Let language-, framework-, security-, testing-, and artifact-specific skills control their specialized procedures. Use this skill around them as preflight, decision filter, and closeout.

## Use a Decision Gate only for product ownership

Interrupt before committing to a consequential choice when repository evidence cannot determine a user-visible, compatibility, data-retention, destructive-migration, supported-platform, operational-policy, or similarly product-owned decision and no safe reversible default exists.

Resolve reversible technical choices, implementation details, and principle selection autonomously. Ask the smallest product-facing question; never transfer software-engineering classification to the user. Before loading principle references, read the Decision Gate section of `workflow.md` and emit its template with every labeled field exactly; when neither direction has evidentiary support, write `No safe default` as the recommendation.

## Keep thinking ephemeral

- Do not write briefs or design contracts into the project unless the user explicitly requests a collaborative artifact.
- At closeout, review the diff, the active brief, unplanned changes, and verification evidence.
- Ask whether future developers could make a wrong decision without something learned here. Promote only the exact stable fact into its authoritative owner; discard the remaining scaffolding.
- Treat old task briefs as non-authoritative unless current instructions explicitly link them. Update or remove stale documentation only when it is in scope and contradicted by evidence; otherwise ignore it as authority and report it.

For projects that need a persistent backup trigger, reuse [global-agents-activation.md](assets/global-agents-activation.md).
