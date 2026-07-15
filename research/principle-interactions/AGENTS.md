# Purpose

- Maintain the reproducible study of how the project’s software principles reinforce, sequence, constrain, or conflict with one another.

# Ownership

- `canonical-profiles.md` defines the operational baseline for each principle.
- `pair-screening.csv` and `independent-screening.csv` record primary and blind pair classifications.
- `pair-dossiers/` owns the published evidence dossiers for accepted or adjudicated interactions.
- `research-journal.md`, `adversarial-review.md`, and `review-reconciliation.md` own the decision trail.
- `source-register.md`, `bundle-assessments.md`, and the SHA-256 manifests own sources, derived bundles, and integrity checks.

# Local Contracts

- Keep pair IDs, principle names, dispositions, dossier paths, and journal references aligned across all artifacts.
- Maintain the distinction between sourced evidence, reasoned inference, counterexamples, and context-dependent conclusions.
- Update an integrity manifest whenever an intentional change alters a file covered by that manifest.
- Do not publish a dossier or bundle conclusion that is unsupported by the screenings and reconciliation record.

# Work Guidance

- Preserve stable CSV schemas and dossier section structure unless the research workflow itself changes.
- Record decision-changing research work in the journal and reconcile independent or adversarial disagreements explicitly.
- Keep rejected relationships and boundary cases visible where they are required to explain the final disposition.

# Verification

- From the repository root, run `shasum -a 256 -c research/principle-interactions/dataset-freeze.sha256`.
- From the repository root, run `shasum -a 256 -c research/principle-interactions/chapter-integrity.sha256`.

# Child DOX Index

- [pair-dossiers/AGENTS.md](pair-dossiers/AGENTS.md) — published pair-level interaction analyses and their required evidence structure.
