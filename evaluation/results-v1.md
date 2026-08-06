# Minimal Design Trigger Evaluation · v1

## Run identity

- Date: 2026-08-06
- Skill hash: `9d5353dde5e079fc988b4464ceb5dea8c1653c0c0504bb3f2116f02df2f9adda`
- Model: `gpt-5.6-sol`
- Host: `codex-cli 0.147.0-alpha.1.2`
- Scoring: explicit skill-name/path evidence in JSONL events, labeled brief and Decision Gate structures, reference-read commands, and fixture artifact inspection
- Metadata mode: repository-local skill package, no activation asset
- Asset mode: the same package plus `assets/global-agents-activation.md` as root `AGENTS.md`

The current 36-case set was evaluated on the recorded skill hash. Thirty-four cases come from the final full run; D06 and D12 were rerun after correcting their synthetic fixture conditions without changing the skill. D02 and D07 were rescored after evidence justified a lower classification or no principle. Raw transcripts and disposable repositories stayed under ignored `evaluation/.tmp/` and are not durable authority.

## Acceptance results

| Requirement | Result | Threshold | Status |
|---|---:|---:|---|
| Design-bearing activation | 12/12 | at least 11/12 | Pass |
| Mechanical activation and fast exit | 8/8 | at least 7/8 | Pass |
| Software-adjacent false positives | 0/8 | at most 1/8 | Pass |
| Non-software captures | 0/8 | 0/8 | Pass |
| Product-owned Decision Gates | 4/4 | 4/4 | Pass |
| Engineering-control Decision Gates | 0/4 | 0/4 | Pass |
| Persisted briefs or contracts | 0/36 | 0/36 | Pass |
| Activation-asset boundary sample | 5/5 correct | no new non-software false positive | Pass |

All eight mechanical cases read only `SKILL.md`, the named implementation surface, and local verification evidence; none loaded workflow, principle, bundle, or boundary references. The four product cases gated on public API compatibility, supported macOS versions, irreversible name-data migration, and old-client endpoint compatibility. The matched engineering controls made their technical decisions autonomously.

## Focused tuning record

1. **Decision Gate instruction:** the first compatibility pilot activated but paraphrased the interruption. Requiring the exact workflow template produced every labeled field, `Owner: User`, and `No safe default` when evidence supported neither direction.
2. **Ephemeral artifact instruction:** the first security control made the correct autonomous change but omitted its consequential artifact. Requiring labeled workflow fields produced the full design contract before mutation.
3. **Frontmatter exclusion:** the first 36-case metadata run captured two read-only repository status/inventory prompts. Excluding status, inventory, navigation, and orientation without diagnosis, review, or change reduced the final count to zero while preserving the design, mechanical, and non-software controls.

The activation asset was then checked separately against a product gate, a mechanical edit, both former repository false positives, and a non-software prompt. All five retained their expected behavior.

## Residual observations

- D12 performed the correct review, kept eligibility in the domain owner, and did not ask the user an engineering question, but it presented an unlabeled `Review frame` instead of the prescribed consequential design-contract fields. Audited end-to-end behavior was therefore 35/36 even though every explicit acceptance threshold passed.
- Reference minimization was directionally strong but not deterministic. Some consequential runs searched a broader reference file before selecting one principle, and one security run inspected bundle and boundary references before ultimately using a single principle. Mechanical fast exits were consistently precise.
- No evaluated prompt selected a whole bundle after reconnaissance; the narrow synthetic surfaces were adequately governed by zero or one principle. Bundle representation and accepted-edge integrity are covered structurally, not claimed as runtime bundle coverage by this set.
- Forward testing is model- and host-sensitive. This report is evidence for the recorded hash and versions, not a permanent performance guarantee.
