# Purpose

- Maintain repository-local agent skills that package the project’s validated guidance for portable use.

# Ownership

- `skills/minimal-design/` owns the self-contained decision-filtration skill, its routed references, UI metadata, and reusable activation asset.
- This document owns packaging and maintenance rules for repository-local agent resources.

# Local Contracts

- Keep every packaged skill portable; it must not depend on absolute paths or files outside its own folder at runtime.
- Keep skill metadata, workflow instructions, references, and assets aligned with the root library and frozen interaction conclusions.
- Keep research provenance in the root library; package only the operational knowledge needed by an executing agent.

# Work Guidance

- Preserve progressive disclosure: metadata triggers, `SKILL.md` routes, and references supply detail only when needed.
- Do not include DOX instructions in the skill’s product identity or runtime guidance.
- Do not add scripts when instructions and existing Codex capabilities suffice.

# Verification

- Run the skill-creator `quick_validate.py` against each changed skill.
- Run the repository evaluation checks documented by `evaluation/AGENTS.md` when trigger, routing, or decision behavior changes.

# Child DOX Index

- No child AGENTS.md files. `skills/minimal-design/` remains governed by this document.
