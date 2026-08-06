# Evaluation

## Purpose

- Own reproducible validation and implicit-trigger evaluation for the portable `minimal-design` skill.

## Ownership

- `trigger-cases.jsonl` is the durable golden prompt set.
- `validate_skill.py` checks package structure and golden-set invariants without third-party dependencies.
- `run_trigger_eval.py` runs fresh disposable Codex CLI sessions and writes only temporary raw evidence below `.tmp/`.
- Versioned result reports summarize a specific skill hash and host configuration; they are evidence, not timeless claims.

## Local Contracts

- Keep all disposable repositories and raw transcripts below `evaluation/.tmp/`.
- Natural evaluation prompts must not name the skill or disclose their expected classification.
- Test metadata-only recall before testing the optional activation asset.
- Change one metadata field or instruction region per tuning cycle and preserve comparable before/after scores.
- Never treat response wording alone as explicit activation evidence when the host exposes a skill event.
- Do not write a micro-brief or design contract into a fixture repository.

## Work Guidance

- Keep the 36-case category counts and acceptance thresholds defined in `trigger-cases.jsonl` and the project integration guide.
- Record skill hash, model, Codex version, date, activation-asset presence, and scoring method in every result report.
- Delete temporary fixtures after results have been summarized; never delete versioned evaluation inputs or reports as cleanup.

## Verification

- `python3 evaluation/validate_skill.py`
- `python3 evaluation/run_trigger_eval.py --dry-run`
- Official skill validation uses `quick_validate.py` from the installed `skill-creator` package with an interpreter that already provides PyYAML.

## Child DOX Index
