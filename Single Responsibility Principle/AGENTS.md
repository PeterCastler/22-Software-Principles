# Purpose

- Maintain the project’s standalone reference on the Single Responsibility Principle and stakeholder-aligned change.

# Ownership

- `Single Responsibility Principle.md` owns the comprehensive chapter, including limits, review guidance, and sources.
- `definitions/` owns compact attributed source notes.
- `examples/` owns original or substantially transformed before/after examples.

# Local Contracts

- Keep the chapter, source notes, and examples consistent about the principle’s meaning and boundaries.
- Keep source notes traceable to their title, publisher or author, URL, and access context.
- Keep examples self-contained and clearly identified as synthesized material.

# Work Guidance

- Preserve the chapter as a standalone explanation rather than requiring readers to reconstruct it from other folders.
- Prefer paraphrase in source notes; do not turn them into page mirrors.
- Explain limits and misapplications alongside recommended practice.

# Verification

- From the repository root, run `shasum -a 256 -c research/principle-interactions/chapter-integrity.sha256` when a tracked chapter or its integrity record changes.

# Child DOX Index

- No child AGENTS.md files. `definitions/` and `examples/` remain governed by this document.
