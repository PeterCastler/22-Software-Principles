# Principle Interaction Research Journal

This is an append-only work log. Later corrections are recorded as new entries that cite the entry being corrected; earlier entries are not rewritten.

## J-20260715-1825-01

Phase: Study initialization

Objective: Establish the research boundary, artifact locations, catalog order, and a baseline that protects the existing principle chapters.

Sources and searches:

- Root `README.md`, including its 22-entry catalog and current statement of precedence.
- All 22 standalone principle chapters and the 22 definition/source-note files were inventoried.
- `git status --short` was inspected before research began.

Work performed:

- Confirmed that the catalog contains 22 principles, implying 231 unique unordered pairs (`22 × 21 ÷ 2`).
- Confirmed that every principle directory contains one standalone chapter, one definition/source note, and one example.
- Recorded SHA-256 hashes for the 22 standalone chapters before interaction-study edits.
- Created the research directory and empty `pair-dossiers/` directory.
- Confirmed that the existing tree is untracked; this study will preserve all existing principle-titled chapters and ignore unrelated `.DS_Store` files.

Findings:

- The root README already contains a provisional "practical order of precedence." It predates this study and will not be treated as interaction evidence. The final interaction guide will be derived independently; any inconsistency will be logged rather than silently forcing the evidence to match the README.
- Existing definition files are compact attributed paraphrases rather than source mirrors, so profile construction must use both those notes and the standalone chapters, with authoritative-source verification where needed.

Rejected or downgraded claims: None; no interaction claims have been screened.

Classification changes: None.

Artifacts updated:

- `research/principle-interactions/research-journal.md`
- `research/principle-interactions/pair-dossiers/` (directory only)

Next step: Read the complete standalone chapters and source notes, register their sources, and construct the 22 operational canonical profiles. No pair screening or bundle work will begin before profiles are complete.

## J-20260715-1840-02

Phase: Phase 1 — source reading and profile normalization

Objective: Read the complete local corpus and verify an authoritative source for each profile before writing operational definitions.

Sources and searches:

- Read all 22 standalone principle chapters in full.
- Read all 22 files under the principle `definitions/` directories in full.
- Opened and checked the authoritative pages behind the chapters, including the originating or canonical sources for YAGNI, DRY, Separation of Concerns, SRP, Convention over Configuration, Unix Philosophy, Functional Core/Imperative Shell, Negative Code, Dead Code Elimination, Least Power, Parse Don't Validate, Law of Demeter, and the principal explanatory sources for the remaining principles.
- The Art of Unix Programming data-driven-programming URL produced a web-reader error; the local attributed source note and chapter remain available, and the source will be registered with that limitation rather than represented as freshly extracted.

Work performed:

- Compared each chapter's definition, application method, failure modes, and limits to its definition/source note.
- Reduced each principle to an operational decision object: the concrete thing a practitioner chooses, changes, removes, or locates.
- Distinguished scope-related concepts that are often conflated: KISS (adequate design complexity), YAGNI (timing of capability), DRY (authority for knowledge), Rule of Three (timing of abstraction), Negative Code (net removal as progress), and Dead Code Elimination (liveness-based deletion).
- Confirmed that "primary source" quality varies by principle. The source register will identify source role rather than falsely label all sources primary.

Findings:

- Every catalog entry can be expressed as an operational profile without relying on its slogan alone.
- Several chapters explicitly contain their own guardrails against likely cross-principle over-application; those guardrails belong in the profiles as limitations, not yet as pair classifications.
- The online Make Illegal States Unrepresentable source explicitly links to Parse, Don't Validate and describes a parse step as an implementation mechanism. This is source evidence to retain for later pair screening, but no pair disposition has yet been assigned.
- Fowler's YAGNI source explicitly says YAGNI is enabled by and enables a malleable codebase. This is retained as profile context; later classification will still apply the five gates.

Rejected or downgraded claims:

- The README's existing precedence list was not used to define any profile or relationship.
- KISS and Occam's Razor were not normalized as synonyms: KISS is a design adequacy rule; Occam's Razor is a comparison rule among equally adequate explanations or solutions.
- Negative Code and Dead Code Elimination were not normalized as synonyms: the former evaluates productive net deletion; the latter requires evidence that a behavior or artifact is unobservable within the supported boundary.

Classification changes: None; exhaustive pair screening has not begun.

Artifacts updated:

- `research/principle-interactions/research-journal.md`

Next step: Write and completeness-check all 22 canonical profiles and the source register. Pair screening remains prohibited until that check passes.

## J-20260715-1905-03

Phase: Phase 1 — canonical profiles complete

Objective: Finish and validate the operational profile set that will constrain both pair screens.

Sources and searches:

- Sources S001–S044 in `source-register.md`.
- The 22 standalone chapters and their 22 local definition notes.

Work performed:

- Authored all canonical profile fields for all 22 principles in README catalog order.
- Registered source role, supported claims, and verification limitations instead of treating every reference as equally primary.
- Ran field-count validation over the profile file.

Findings:

- Exactly 22 profiles exist.
- Each of the nine required field labels occurs exactly 22 times.
- Each decision object names an assessable engineering choice rather than repeating a slogan.
- The profiles preserve important scope distinctions: timing, authority, representation, liveness, component boundary, expressive power, and cleanup scope are different decision objects even where their benefits all include lower complexity.

Rejected or downgraded claims:

- The data-driven-programming page remains registered with a web-reader limitation; it is adequate for the profile because the complete local attributed note was available, but it cannot alone establish Direct interaction evidence until the underlying text is successfully inspected.
- The recent 2026 API-replacement paper is registered but not yet treated as interaction evidence; direct examination is required if a pair dossier depends on it.

Classification changes: None; pair screening starts only after this entry.

Artifacts updated:

- `research/principle-interactions/canonical-profiles.md`
- `research/principle-interactions/source-register.md`
- `research/principle-interactions/research-journal.md`

Next step: Generate the canonical 231-pair list in README order and perform the primary screen using only the profiles. Do not consult bundle hypotheses or create dossiers during the initial screen.

## J-20260715-1920-04

Phase: Phase 2 — primary exhaustive screening

Objective: Apply the first three screening gates to every unordered pair using only the canonical operational profiles.

Sources and searches:

- `canonical-profiles.md` only.
- README catalog order only for pair ordering.
- No interaction web searches and no bundle hypotheses.

Work performed:

- Generated all 231 unordered combinations in catalog order, identified as P001–P231.
- Compared the two decision objects for each pair, then tested for a causal mechanism and a material implementation or review consequence.
- Wrote a concrete counterexample or boundary for every pair that passed the first three gates.
- Rejected pairs when a relationship required unspecified project context rather than following from the profiles.
- Kept the completed primary screen outside the shared research tree temporarily so the independent reviewer cannot encounter its rationales before completing the blind screen.

Findings:

- 89 pairs passed the first three gates as initial research candidates.
- 142 pairs failed the shared-surface, mechanism, or material-consequence test and were provisionally classified `Independence` / `reject`.
- Every candidate remains `uncertain`, `medium` confidence, and `Reasoned Inference` at this phase. None is approved for publication.
- No profile pair justified `Conflict` at initial screening. Several justified `Tension`, because their competing pressures can be reconciled by scope, evidence, or boundary choice.

Rejected or downgraded claims:

- Generic statements such as “both improve maintainability” and “both reduce complexity” were not accepted as mechanisms.
- A possible interaction in one imagined refactoring was rejected when neither profile changed the other's general decision.
- Candidate status was not treated as evidence; the initial evidence label is explicitly only `Reasoned Inference` pending research.

Classification changes: 89 pairs moved from unassessed to `uncertain`; 142 moved from unassessed to `reject` / `Independence`.

Artifacts updated:

- Sealed primary-screen draft at `/private/tmp/primary-screening.csv` (to be copied to `pair-screening.csv` after blind review).
- `research/principle-interactions/research-journal.md`

Next step: Give the independent reviewer only `canonical-profiles.md`, the README catalog order, and a blank 231-pair task. The reviewer must not read this journal, the source register, or any primary-screen artifact.

## J-20260715-1935-05

Phase: Phase 3 — independent screening and candidate-set construction

Objective: Validate the blind independent ledger, unseal the primary ledger, and compute the research set without averaging disagreements away.

Sources and searches:

- Independent reviewer used only `canonical-profiles.md` and README catalog order, by explicit task restriction.
- No web research was permitted during independent screening.

Work performed:

- A separate subagent independently generated and screened all 231 pairs without access to the primary rationales, journal, source register, or web sources.
- Validated both CSVs have the same headers, 231 IDs, principle order, and unordered pair identities.
- Copied the sealed primary result into `pair-screening.csv` only after the independent result was complete.
- Computed the union of pairs passing the first three gates in either screen and every classification disagreement.

Findings:

- Primary screen: 89 candidates, 142 rejects.
- Independent screen: 124 candidates, 107 rejects.
- Candidate intersection: 80 pairs.
- Primary-only candidates: 9 pairs.
- Independent-only candidates: 44 pairs.
- Candidate union: 133 pairs.
- Disposition disagreements: 53 pairs.
- Primary-taxonomy disagreements: 86 pairs.
- All classification disagreements are contained in the 133-pair candidate union; there are no rejected/rejected disagreements outside the research set.
- Neither reviewer proposed `Conflict`. This remains an empirical result of screening, not a prohibition on a later evidence-based conflict finding.

Rejected or downgraded claims:

- Reviewer agreement is not treated as source evidence.
- A majority or union rule does not publish a relationship; the union only determines which pairs receive targeted research and dossiers.
- The independent review's larger candidate set will not automatically override the primary screen's more conservative gate decisions.

Classification changes: None are final. The 133-pair union is promoted to targeted research; the remaining 98 pairs remain rejected unless new evidence discovered during candidate research directly reopens one.

Artifacts updated:

- `research/principle-interactions/pair-screening.csv`
- `research/principle-interactions/independent-screening.csv`
- `research/principle-interactions/research-journal.md`

Next step: Research the 133-pair union in topical batches. For each pair, seek explicit interaction discussion, real refactorings or authoritative examples, and failure cases; create a dossier and downgrade any mechanism that is not supported.

## J-20260715-1950-06

Phase: Phase 4 — targeted interaction research, source batch 1

Objective: Test the candidate mechanisms against explicit interaction discussions, worked refactorings, authoritative examples, and stated failure boundaries before assigning final evidence grades.

Sources and searches:

- Searched the Martin Fowler corpus for YAGNI, simple design, duplication, present-day design, dependency inversion, refactoring, and explicit failure costs.
- Examined W3C material on the Rule of Least Power, including a concrete XML Schema design choice and a clarification about inadequate declarative languages.
- Examined Alexis King’s originating Parse, Don’t Validate essay and the Functional Software Architecture treatment of illegal states.
- Examined Microsoft architecture and dependency-injection guidance for separation, dependency direction, responsibility, composition roots, and complexity costs.
- Examined worked sources for composition over inheritance and Functional Core, Imperative Shell.
- Examined the 2022 and 2026 API-replacement studies, LLVM/source-level dead-code material, Rails convention guidance, the Unix data-driven chapter, and the Atkinson negative-code case.
- Registered I001–I020 in `source-register.md` with explicit use limits.

Work performed:

- Mapped source passages to mechanisms rather than to shared vocabulary.
- Distinguished explicit interaction evidence from convergence between separate operational definitions.
- Collected boundary evidence at the same time as supporting evidence: wrong abstractions, awkward declarative encodings, DI-container overhead, subclass rigidity, convention opacity, semantic mismatch in APIs, and irregular domains for tables.
- Reopened the original Unix data-driven page successfully; this removes the access limitation recorded in J-20260715-1905-03 without deleting that earlier journal entry.
- Began grouping the 133 candidates by evidence-bearing decision surface so that every candidate still receives an individual verdict and dossier.

Findings:

- Direct interaction evidence exists for a limited set of pair mechanisms: simple design/YAGNI, simplicity/duplication, DRY/Rule of Three, YAGNI/DIP, SRP/DIP, Parse/illegal states, DRY/parsed representations, Unix/data-driven representation, and Least Power/declarative representation.
- Several broad “minimalism” pairings have only convergent evidence. They must not be upgraded to Direct merely because a source lists both desired qualities.
- DIP and composition can reduce policy coupling while adding adapters, abstractions, and wiring. Their relationship with KISS, YAGNI, Negative Code, or platform primitives is therefore usually Moderation or Tension, not simple Reinforcement.
- Separation mechanisms are material when they isolate different rates or reasons for change. Splitting code solely to make functions smaller is outside the supported mechanism.
- Data-driven designs are supported where behavior varies regularly and an interpreter is stable; irregular behavior is a counterexample, not an invitation to encode a second programming language in configuration.

Rejected or downgraded claims:

- Dependency injection examples are not treated as automatic proof of Dependency Inversion; I009 is used only for wiring cost and the SRP diagnostic it explicitly states.
- The appearance of two principles in one architecture article is not Direct evidence unless the article explains how one changes application of the other.
- The 2026 API study supports the existence and prevalence of API-replacement refactorings, but not the claim that every replacement is simpler or safer.
- Generic “both reduce complexity” explanations remain unsupported.
- No source in this batch established mutually exclusive recommendations under identical preconditions; no candidate is promoted to Conflict.

Classification changes: None frozen. Source-backed provisional grades and dispositions will be assigned pair by pair in the dossier pass.

Artifacts updated:

- `research/principle-interactions/source-register.md`
- `research/principle-interactions/research-journal.md`

Next step: Author one dossier for every material or disputed pair, including rejected candidates, and create a conservative proposed-final ledger for adversarial review. Do not begin bundle analysis.

## J-20260715-2015-07

Phase: Phase 4 — pair dossier and proposed-decision pass

Objective: Give every material or disputed pair an inspectable assessment, then expose the proposed publications to adversarial review.

Sources and searches:

- Used I001–I020 and the relevant canonical sources S001–S044.
- Reused the two blind screens only as hypotheses and counterexample prompts; reviewer agreement was not counted as evidence.
- No bundle candidates or desired groupings were consulted.

Work performed:

- Authored 133 pair dossiers: one for every pair that passed the first three gates in either blind screen or had a classification disagreement.
- Assigned each proposed publication a source list, evidence grade, concrete counterexample, material decision consequence, and combined instruction.
- Added explicit resolution procedures for all proposed Tension entries.
- Downgraded 51 researched candidates to `Unsupported` / `reject` because the available material did not establish a general mechanism beyond project-specific coincidence.
- Updated `pair-screening.csv` as a proposed-final primary ledger; it is not frozen and remains subject to adversarial review and reconciliation.

Findings:

- Proposed publications: 82.
- Proposed evidence distribution: 13 Direct, 69 Convergent, 0 Reasoned Inference, and 0 Unsupported publications.
- Proposed taxonomy distribution: 19 Reinforcement, 19 Enablement, 10 Moderation, 12 Sequencing, 7 Complementary, 3 Overlap, 12 Tension, and 0 Conflict.
- All 82 proposed publications pass the first three gates and link to a dossier.
- The larger number of Convergent grades is deliberate: most sources establish compatible operational mechanisms without explicitly naming both catalog labels.

Rejected or downgraded claims:

- Fifty-one researched hypotheses were rejected rather than filled with generic relationship prose.
- No Reasoned Inference was provisionally published, avoiding reliance on reviewer agreement where authoritative convergence is available or the claim should be rejected.
- `Conflict` remains empty because every supported competing pressure has a context-sensitive resolution; none requires mutually exclusive actions under identical preconditions.

Classification changes: 82 candidates provisionally moved to `publish`; 51 researched candidates moved to `Independence` / `Unsupported` / `reject`. These are reviewable proposals, not frozen decisions.

Artifacts updated:

- `research/principle-interactions/pair-screening.csv`
- `research/principle-interactions/pair-dossiers/` (133 dossiers)
- `research/principle-interactions/research-journal.md`

Next step: Have the original blind reviewer challenge every proposed publication, with special attention to Direct grades, generic convergence, taxonomy choice, and counterexamples. Reconcile every objection before freezing.

## J-20260715-2025-08

Phase: Proof-of-work integrity checkpoint during adversarial review

Objective: Make the existing-chapter preservation check independently reproducible while the reviewer evaluates the proposed dataset.

Sources and searches:

- Enumerated the 22 standalone chapter paths at repository depth two.
- Computed SHA-256 digests for those files only; research artifacts and examples were excluded.

Work performed:

- Added `chapter-integrity.sha256` containing the current digest and repository-relative path for every standalone chapter.
- Checked the current work log against J-20260715-1825-01.

Findings:

- Exactly 22 standalone chapters were hashed.
- No task action has written to a principle-titled chapter; all study writes have been confined to `research/principle-interactions/`.

Rejected or downgraded claims:

- Correction to J-20260715-1825-01: that entry says the baseline hashes were recorded, but the digest values themselves were not persisted in an artifact at initialization. This entry does not pretend the new file is a time-traveling baseline. It creates a reproducible mid-study checkpoint, and final QA will recompute it. The earlier statement remains in place under the append-only policy.

Classification changes: None.

Artifacts updated:

- `research/principle-interactions/chapter-integrity.sha256`
- `research/principle-interactions/research-journal.md`

Next step: Complete adversarial review, reconcile all blind-screen and evidence-review disagreements, then recompute the chapter digests during final QA.

## J-20260715-2050-09

Phase: Phase 5 — adversarial review and reconciliation

Objective: Challenge every proposed publication, resolve all blind-screen and evidence-review disagreements, and produce one complete pre-freeze decision set.

Sources and searches:

- The original independent reviewer re-read all 82 proposed publications, their dossiers, canonical profiles, both screening ledgers, and the source register.
- The reviewer rechecked the principal authoritative sources for evolutionary design, abstraction timing, dependency direction, representation/parsing, Unix/data-driven design, replacement/deletion, conventions, and functional core/imperative shell.
- Full row-level findings and rechecked URLs are in `adversarial-review.md`.

Work performed:

- Independently adjudicated all 82 proposed publication IDs exactly once.
- Accepted 66 proposals unchanged, downgraded or reclassified 12, and rejected 4.
- Applied the reviewer’s evidence-based corrections after checking that each rationale matched the canonical profiles and dossier counterexample.
- Reconciled all 86 unique blind-screen classification/disposition disagreements in `review-reconciliation.md`.
- Updated all affected dossiers with the adversarial verdict and final pre-freeze evidence grade.

Findings:

- Final pre-freeze publications: 78; rejects: 153; uncertain: 0.
- Evidence among publications: 10 Direct, 67 Convergent, and 1 Reasoned Inference.
- P227 is the sole Reasoned Inference. It remains high-confidence, has a concrete counterexample, is visibly labeled, and was explicitly accepted by the independent adversarial reviewer at that lower grade.
- Taxonomy among publications: 22 Reinforcement, 13 Enablement, 11 Moderation, 11 Sequencing, 9 Complementary, 4 Overlap, 8 Tension, 0 Conflict.
- All eight final Tensions retain a concrete stopping test and resolution procedure.

Rejected or downgraded claims:

- P104, P146, P182, and P189 were rejected because a primitive, type, collaborator, or abstraction could incidentally participate in both principles without one principle changing the other’s decision.
- P002, P106, and P134 lost Direct status because the sources did not explicitly establish the exact pair mechanism.
- Apparent Tensions P045, P046, and P152 were reclassified as Complementary or Moderation because correct scope tests partition or constrain the decisions rather than create opposing pressures.
- P187 was reclassified as Overlap because Dead Code Elimination is a liveness-proven subset of the broader Negative Code outcome.
- P227 was downgraded from Convergent to Reasoned Inference because its plausible mechanism is not explicitly or separately established by the sources.

Classification changes: 4 proposed publications moved to `Independence` / `Unsupported` / `reject`; 12 publications changed taxonomy or evidence grade; 66 remained unchanged. No disagreement remains unresolved.

Artifacts updated:

- `research/principle-interactions/adversarial-review.md`
- `research/principle-interactions/review-reconciliation.md`
- `research/principle-interactions/pair-screening.csv`
- `research/principle-interactions/pair-dossiers/`
- `research/principle-interactions/research-journal.md`

Next step: Run the full pre-freeze validation: ledger identity/order, enums, gates, evidence policy, dossier completeness, reconciliation coverage, source IDs, links, and Markdown structure. Freeze only if every check passes.

## J-20260715-2115-10

Phase: Phase 6 — pre-freeze validation and interaction-dataset freeze

Objective: Prove the reconciled interaction dataset satisfies every freeze precondition, then close pair classification before any guide or bundle authoring.

Sources and searches:

- No new research sources. This phase used the catalog, both 231-row ledgers, the sealed initial primary screen, 133 dossiers, the adversarial review, reconciliation record, source register, canonical profiles, journal, and chapter-integrity checkpoint.

Work performed:

- Validated both ledgers contain the same 231 catalog-ordered unordered pairs, with P001–P231, no duplicates, and no self-pairs.
- Validated the requested CSV schema and every gate, taxonomy, evidence, confidence, and disposition enum.
- Validated all 78 publications pass the first three gates, have an allowed evidence grade, cite a complete dossier, and contain a counterexample.
- Validated all eight Tension dossiers contain a substantive resolution procedure.
- Validated P227 is the only Reasoned Inference, is high-confidence, has a counterexample, is visibly labeled, and has explicit independent-review acceptance.
- Validated all 86 blind-screen disagreements and all 16 adversarial changes are recorded in reconciliation artifacts.
- Validated exactly 22 complete profiles, 133 required dossiers, 64 registered source IDs, balanced Markdown fences, resolving local links, and unchanged chapter-integrity digests.
- Confirmed neither `Principle Interaction Guide.md` nor `bundle-assessments.md` existed during validation.

Findings:

- Validation result: PASS.
- Frozen publications: 78. Frozen rejects: 153. Frozen uncertain entries: 0.
- Frozen evidence: 10 Direct, 67 Convergent, 1 Reasoned Inference, 0 Unsupported publications.
- Frozen taxonomy: 22 Reinforcement, 13 Enablement, 11 Moderation, 11 Sequencing, 9 Complementary, 4 Overlap, 8 Tension, 0 Conflict.
- The empty Conflict category is an evidence result: all supported competing pressures can be reconciled by precondition, scope, order, or boundary choice.

Rejected or downgraded claims:

- No new claims changed during validation. Validation errors in the first checker run were checker defects: profile fields are plain-text labels rather than bold labels, and percent-encoded README paths required URL decoding. The checker was corrected and rerun; no research artifact was changed to satisfy a faulty check.

Classification changes: None during validation.

Artifacts updated:

- `research/principle-interactions/pair-dossiers/` (status labels mechanically marked validated for freeze)
- `research/principle-interactions/research-journal.md`

**Dataset freeze declaration:** As of this entry, the gate results, primary and secondary taxonomies, evidence grades, confidence values, dispositions, counterexamples, and pair mechanisms in `pair-screening.csv` are frozen. They must not change unless the freeze is explicitly reopened in a later append-only journal entry. Bundle analysis begins only after this declaration and may not modify the frozen relationships.

Next step: Author and verify the core `Principle Interaction Guide.md` from frozen `publish` rows only, without bundle content. After that guide passes a dataset-match check, derive bundles as a separate final analytical step.

## J-20260715-2140-11

Phase: Phase 7 — core guide authoring and frozen-dataset verification

Objective: Author the relationship and conflict portions of the guide from frozen publications only, with no bundle content, then prove an exact dataset match.

Sources and searches:

- Consumed the frozen `pair-screening.csv`, complete published dossiers, canonical profiles, reconciliation record, and source register.
- No new pair research and no bundle hypotheses.

Work performed:

- Created root-level `Principle Interaction Guide.md` with purpose and epistemic limits, canonical-profile method, gates, taxonomy, evidence policy, a 78-row overview, and compact entries grouped under all relationship categories.
- Included a resolution procedure in every Tension entry and an explicit inference notice for P227.
- Added coverage/proof links and a source section while leaving rejected pairs in the ledger rather than manufacturing guide prose for them.
- Ran a guide-to-ledger verifier before creating any bundle artifact.

Findings:

- Core-guide verification result: PASS.
- The overview contains exactly the frozen 78 publish IDs once each.
- The grouped dossier sections contain exactly those same 78 IDs once each, under the taxonomy recorded in the frozen CSV.
- Every evidence grade, mechanism, material consequence, and counterexample matches the frozen row.
- All eight Tensions include resolutions; P227 includes the required visible Reasoned Inference notice.
- The verified core guide contains no bundle heading or bundle recommendation.

Rejected or downgraded claims:

- No rejected pair was promoted into the guide for narrative completeness.
- The empty Conflict section states the evidence result rather than inventing a conflict to populate the taxonomy.

Classification changes: None. The frozen dataset was read, not modified.

Artifacts updated:

- `Principle Interaction Guide.md` (core, no bundles)
- `research/principle-interactions/research-journal.md`

Next step: Begin Phase 8. Construct candidate bundles only from the frozen published graph, record both accepted and rejected candidates in a newly created `bundle-assessments.md`, then append only accepted bundles to the already-verified guide.

## J-20260715-2210-12

Phase: Phase 8 — post-freeze bundle derivation

Objective: Derive narrowly useful principle bundles from the frozen publication graph without changing any relationship to make a desired grouping work.

Sources and searches:

- Frozen `pair-screening.csv` and the pair dossiers cited by candidate graph edges.
- The bundle acceptance rules specified for this study.
- No new pair research and no pre-freeze grouping hypothesis.

Work performed:

- Constructed 12 candidate bundles from connected regions of the frozen graph.
- Evaluated each candidate for one objective, 3–6 members, published connectivity, sequence coverage, unresolved Tension/Conflict, Overlap-only membership, instruction redundancy, counterexample, and dossier traceability.
- Recorded six accepted and six rejected candidates in `bundle-assessments.md`.
- Appended only the six accepted bundles to the already-verified core guide.
- Ran a graph validator over all accepted memberships and cited edges.

Findings:

- Accepted: B01 Evidence-led minimal design; B02 Constrained data for regular variation; B03 Trusted functional boundary; B04 Evidence-backed deletion; B05 Encapsulated domain commands; B06 Minimal policy-owned architecture.
- Every accepted bundle has 3–6 members, a connected published graph, at least one non-Overlap edge, no internal frozen Tension or Conflict, an application order, a concise combined instruction, a counterexample, and enough cited dossiers to connect all members.
- B05 visibly preserves P227 at Reasoned Inference; bundle membership does not upgrade its evidence.
- B03 explicitly avoids relying on P182, a hypothesis rejected during adversarial review.

Rejected or downgraded claims:

- R01 was too broad and mixed local abstraction timing with architecture-boundary decisions.
- R02 could not generically resolve the frozen Data-Driven Design/Tell, Don’t Ask Tension and tried to rely on rejected P182.
- R03 left two primitive-versus-boundary Tensions unresolved without project volatility facts.
- R04 was dominated by the accepted deletion bundle and relied too heavily on Overlap.
- R05 connected mainly through Overlap and unresolved placement Tensions.
- R06 depended on framework-specific resolution of convention versus inspectable dependency ownership.

Classification changes: None. Bundle analysis read the frozen graph and did not modify `pair-screening.csv`.

Artifacts updated:

- `research/principle-interactions/bundle-assessments.md`
- `Principle Interaction Guide.md` (validated bundles appended)
- `research/principle-interactions/research-journal.md`

Next step: Link the guide from README and run final QA across the entire artifact set, including frozen hashes, chapter integrity, source URLs, local links, fences, bundle graph rules, and guide-to-ledger identity.

## J-20260715-2245-13

Phase: Final QA and handoff

Objective: Verify every acceptance criterion after bundle append and README integration, without reopening the frozen interaction dataset.

Sources and searches:

- All local study artifacts and the root README.
- Live HTTP resolution check for all 52 unique URLs in `source-register.md`.
- The frozen dataset and chapter SHA-256 manifests.

Work performed:

- Linked `Principle Interaction Guide.md` and the proof directory from README.
- Revalidated the final guide’s 78 overview rows and 78 compact interaction entries against the frozen ledger.
- Revalidated all six accepted and six rejected bundle assessments and the six guide bundles.
- Checked both 231-row ledgers, enums, publication gates, evidence policy, profile counts, dossier counts and sections, disagreement coverage, inference labeling, local links, Markdown fences, source-ID references, and chapter hashes.
- Added `dataset-freeze.sha256` for the final primary ledger, independent ledger, and canonical profiles; all three digests pass.
- Performed live URL checks. Fifty unique source URLs returned HTTP 200. Baeldung and O’Reilly returned HTTP 403 access controls rather than missing-page errors. No source returned 404, 5xx, DNS failure, or TLS failure after correcting the Unix source URLs to the official HTTP endpoints and updating Microsoft’s redirected dependency-injection URL.
- Audited secondary Tension labels as well as primary Tensions. P006, P009, and P016 retained their frozen secondary label and now have substantive resolution procedures in both dossier and guide; no classification, mechanism, evidence grade, disposition, or counterexample changed.

Findings:

- Final structural QA: PASS.
- Frozen-manifest verification: PASS.
- Bundle graph/acceptance verification: PASS.
- Exactly 22 profiles, 231 primary rows, 231 independent rows, 133 researched dossiers, 78 publications, 153 rejects, 0 uncertain rows, 6 accepted bundles, and 6 rejected bundle candidates exist.
- All 11 primary-or-secondary Tension records shown in the guide have resolution procedures; no Conflict is published.
- The 22 standalone principle chapters match the integrity checkpoint. No principle-titled chapter was edited.
- The worktree remains entirely untracked as it was at initialization; pre-existing `.DS_Store` files were not modified or removed.

Rejected or downgraded claims:

- HTTP 403 was not misreported as a broken citation: both affected hosts deliberately restrict automated access, while the registered URLs remain valid.
- No bundle or README wording was allowed to alter a frozen pair decision.

Classification changes: None after J-20260715-2115-10. The frozen dataset digest is `431ae08c2e1c491b3f38538d8300dcf141947fb87ca037d1f322a4dcf05c133c`.

Artifacts updated:

- `README.md`
- `Principle Interaction Guide.md`
- `research/principle-interactions/bundle-assessments.md`
- `research/principle-interactions/dataset-freeze.sha256`
- `research/principle-interactions/source-register.md` (URL resolution corrections only)
- `research/principle-interactions/pair-dossiers/P006-kiss-separation-of-concerns.md`
- `research/principle-interactions/pair-dossiers/P009-kiss-convention-over-configuration.md`
- `research/principle-interactions/pair-dossiers/P016-kiss-data-driven-design.md`
- `research/principle-interactions/research-journal.md`

Next step: Study complete. Any later `AGENTS.md` authoring should consume the validated bundle instructions without silently broadening their objectives or dropping their counterexamples.

## J-20260715-2317-14

Phase: Post-study operational handoff update

Objective: Apply the supplied 2026 consensus checklist to the way this library is consumed without reopening or reclassifying the frozen interaction research.

Work performed:

- Replaced the README's planned static `AGENTS.md` distillation with a task-specific `CONTRACT.md` workflow.
- Added a reusable contract template capped below 100 lines.
- Required any downstream `SKILL.md` packaging to stay below 100 lines and move background material into linked references.
- Required explicit objective, scope, non-goals, acceptance evidence, verification, and a dedicated `Forbidden` section.
- Framed validated bundle instructions as candidate contract clauses and required their counterexamples to remain visible as boundary checks.
- Preserved the journal's earlier `AGENTS.md` sentence as historical, append-only evidence; this entry supersedes that handoff direction.

Operational decision:

- Generate a fresh `CONTRACT.md` immediately before each implementation task.
- Use the smallest applicable set of validated bundle clauses; do not concatenate the library into standing repository instructions.
- Remove aspirational prose and keep only statements that constrain a decision or make completion observable.
- Keep any derived `SKILL.md` focused on actionable routing and decision rules; link to this library for supporting research.
- State likely failure modes as strict negative constraints, including protected files, APIs, data, and behavior.
- Keep the complete contract below 100 lines and do not carry it forward as passive guidance for another task.

Research status: Unchanged. No profile, pair classification, evidence grade, bundle membership, counterexample, dataset, or integrity-tracked principle chapter was modified.

Artifacts updated:

- `README.md`
- `CONTRACT.template.md`
- `Principle Interaction Guide.md`
- `research/principle-interactions/bundle-assessments.md`
- `research/principle-interactions/research-journal.md`

Next step: For the next implementation task, generate `CONTRACT.md` from the template only after the task's current evidence and boundaries are known.
