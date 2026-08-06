# Workflow Reference

## Contents

- Classification
- Reconnaissance
- Ephemeral artifacts
- Decision Gate
- Implementation and reclassification
- Closeout and distillation
- Stale documentation

## Classification

Classify only after the smallest inspection that can reveal the real decision surface.

### Mechanical

Use Mechanical only when all are true:

- The requested outcome is explicit and has one established implementation path.
- The change is local and does not alter a public, data, security, compatibility, accessibility, or operational contract.
- No dependency, abstraction, representation, responsibility boundary, migration, or supported behavior is added or removed.
- The nearest relevant verification is known.

Examples include a literal correction, a specified rename with compiler coverage, a fixture update caused by an established output, or a formatter-generated change.

### Normal

Use Normal when implementation needs bounded judgment but remains local, reversible, and governed by an established design. Typical signals are a contained bug fix, a small behavior addition, or a local refactor whose preserved contract is known.

### Consequential

Use Consequential when any current decision concerns:

- a public API, persisted format, migration, compatibility promise, or supported recovery path;
- authorization, security policy, concurrency, transactions, or destructive behavior;
- a new production dependency, service, abstraction system, plugin point, or configuration language;
- movement of responsibility across modules or ownership boundaries;
- deletion or replacement whose liveness or semantic equivalence is uncertain;
- several adequate designs with materially different lifecycle obligations;
- an unfamiliar subsystem whose supported behavior is not yet established.

A task can move upward after inspection. Do not force a task downward to avoid process.

## Reconnaissance

Start with applicable instructions and the named target. Then, only as needed:

1. Locate the implementing symbol and its nearest concrete behavior.
2. Inspect direct callers or consumers that establish the supported contract.
3. Inspect focused tests, schemas, migration records, and authoritative documentation.
4. Search for existing primitives, conventions, and analogous decisions.
5. Broaden to dynamic registration, reflection, operations, or external consumers only when the proposed change depends on liveness or compatibility.

Stop when the classification, preserved contracts, and verification path are supported. Reconnaissance is evidence gathering, not permission for roaming cleanup.

## Ephemeral artifacts

Keep these structures in conversation. Do not create a file by default.

### Micro-brief

```text
Outcome: <observable result>
Scope: <allowed files, components, or behavior>
Preserve: <relevant contract>
Evidence: <code, test, trace, or requirement>
Verification: <focused check>
Forbidden: <one likely failure mode, only when useful>
```

### Design contract

```text
Requirement: <current complete requirement>
Decision surface: <the consequential choice>
Conservative option: <smallest adequate existing-shape option>
Proposed option: <recommended option and lifecycle consequence>
Evidence: <facts from code, tests, traces, or authoritative requirements>
Assumptions: <facts not yet established>
Guidance: <zero or one primary bundle; add another only for a distinct surface>
Boundary: <selected counterexample or stopping condition>
Scope / non-goals: <allowed perimeter and exclusions>
Acceptance: <observable success and preserved behavior>
Verification: <commands and focused manual checks>
Forbidden: <specific ways the task must not expand or weaken contracts>
```

## Decision Gate

A Decision Gate is an interruption, not a larger artifact tier. Use it from any stage only when:

- a consequential choice changes product behavior or an externally meaningful promise;
- repository evidence supports multiple possibilities or none;
- no safe reversible default preserves all plausible intentions; and
- proceeding would commit the project before the owner answers.

Do not gate on naming, local structure, principle choice, ordinary dependency mechanics, or another engineering question resolvable from evidence.

```text
Decision required

Question:
<smallest product-facing question>

Reason:
<why repository evidence cannot resolve it>

Evidence:
<concrete conflicting or missing facts>

Impact:
<user-visible, compatibility, operational, or irreversible consequence>

Recommendation:
<only when supportable; otherwise "No safe default">

Owner:
User

Work paused before:
<the first action that would commit to an answer>
```

Complete unaffected read-only reconnaissance before gating. Pause before mutation that assumes an answer.

## Implementation and reclassification

- Follow the active brief rather than applying principles as independent goals.
- Reclassify when implementation reveals a new contract, consumer, irreversible effect, or missing product decision.
- Use a specialist skill for its domain procedure; do not duplicate or weaken its checks.
- Keep incidental cleanup inside the touched execution path and stop when it requires new judgment.

## Closeout and distillation

Review:

1. Did the observable outcome and preserved contracts hold?
2. Did the diff stay within scope?
3. Were new abstractions, dependencies, configuration, or promises justified by current evidence?
4. Was deleted behavior proven dead or semantically replaced?
5. Did verification actually run, and what remains unverified?
6. Did any assumption become a fact that changes the design?

Promote knowledge only when all are true:

- It remains relevant beyond this task.
- Future work could make a wrong decision without it.
- It is stable enough to be a contract, workflow rule, or maintained explanation rather than speculation.
- An existing authoritative document or a clear durable owner exists.

Write only the distilled fact into the closest authority. Do not preserve the task narrative, rejected transient hypotheses, or the entire brief.

## Stale documentation

- Treat completed task briefs, copied plans, and unlinked contracts as historical evidence, not current authority.
- Prefer current code, tests, schemas, active requirements, and documents named by applicable instructions.
- When a stale document is in the task's scope, update or remove the contradicted text and its references.
- When it is outside scope, do not follow it silently; report the contradiction and continue from current authoritative evidence.
- Remove an ephemeral artifact created by the current task before closeout. Never delete unrelated user documentation merely because it appears old.
