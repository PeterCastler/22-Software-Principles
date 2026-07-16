# Bundle Assessments

## Derivation rule

Bundle analysis began only after the interaction dataset was frozen in J-20260715-2115-10 and the bundle-free core guide passed verification in J-20260715-2140-11. Candidate membership was derived from the 78 frozen `publish` edges. No pair classification was changed to make a bundle connect.

An accepted bundle must have one engineering objective, contain three to six principles, form a connected graph of published relationships, document every applicable sequence, contain no unresolved Tension or Conflict, avoid members connected only through Overlap, provide a concise nonredundant instruction, state a counterexample, and cite the dossier edges that justify membership. A published edge does not mean its endpoints should always be bundled; the objective and all principle preconditions must also hold.

## Accepted bundles

### B01 — Evidence-led minimal design

**Objective:** Deliver the smallest present solution while preventing premature or wrongly scoped abstraction.

**Principles:** KISS; YAGNI; Rule of Three; DRY.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P001](./pair-dossiers/P001-kiss-yagni.md) | KISS ↔ YAGNI — Reinforcement | Keeps speculative capability out of the complexity budget. |
| [P003](./pair-dossiers/P003-kiss-rule-of-three.md) | KISS ↔ Rule of Three — Reinforcement | Requires concrete cases before adding a general mechanism. |
| [P022](./pair-dossiers/P022-yagni-dry.md) | YAGNI ↔ DRY — Moderation | Separates present duplicated authority from predicted reuse. |
| [P042](./pair-dossiers/P042-dry-rule-of-three.md) | DRY ↔ Rule of Three — Moderation, with Sequencing secondary | Delays extraction until meaning and ownership are understood. |

The graph is connected through non-Overlap edges and contains no frozen Tension or Conflict.

**Application order:**

1. State the complete present requirement and reject unsupported capability.
2. Implement the clearest adequate direct design.
3. Let early repeated shapes remain local while their meanings and variation emerge.
4. After repeated evidence, centralize only knowledge that has one owner and should change together.

**Candidate contract clause:**

```text
Implement only the current complete requirement using the clearest adequate design.
Do not add extension points for predicted reuse. Leave early duplication local until
repeated cases reveal one stable, jointly owned fact; then give that fact one authority.
```

**Counterexample:** A published protocol, security invariant, or regulated rule already has one authoritative definition. Centralize it immediately rather than waiting for three local copies.

**Decision:** Accepted. All four members contribute distinct actions to the objective; the sequencing guard prevents DRY from becoming speculative abstraction.

### B02 — Constrained data for regular variation

**Objective:** Replace repeated regular branching with one inspectable, trusted, minimally expressive data representation.

**Principles:** Rule of Three; Data-Driven Design; DRY; Principle of Least Power; Parse, Don't Validate; Make Illegal States Unrepresentable.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P073](./pair-dossiers/P073-rule-of-three-data-driven-design.md) | Rule of Three ↔ Data-Driven Design — Sequencing | Concrete cases reveal the stable algorithm and varying dimensions. |
| [P055](./pair-dossiers/P055-dry-data-driven-design.md) | DRY ↔ Data-Driven Design — Enablement | Makes the table the single authority for the case set. |
| [P106](./pair-dossiers/P106-principle-of-least-power-data-driven-design.md) | Least Power ↔ Data-Driven Design — Reinforcement | Keeps the representation declarative and analyzable. |
| [P218](./pair-dossiers/P218-data-driven-design-parse-don-t-validate.md) | Data-Driven Design ↔ Parse, Don't Validate — Sequencing | Parses untrusted selectors or rows before table use. |
| [P217](./pair-dossiers/P217-data-driven-design-make-illegal-states-unrepresentable.md) | Data-Driven Design ↔ Illegal States — Enablement | Closes the valid key/state set where the domain is finite. |
| [P222](./pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md) | Illegal States ↔ Parse, Don't Validate — Enablement | Constructs the precise trusted representation at the boundary. |

The graph is connected through Sequencing, Enablement, and Reinforcement; no member is connected only through Overlap, and there is no frozen Tension or Conflict inside the bundle.

**Application order:**

1. Lay out enough real cases to prove the variation is regular.
2. Define one table/schema and one stable interpreter; derive dependent artifacts from that authority.
3. Use the least expressive adequate row format instead of callbacks or an embedded language.
4. Parse external rows and keys once into closed, precise values before lookup or interpretation.

**Candidate contract clause:**

```text
Use a table only after real cases reveal one stable algorithm with regular variation.
Make the table the single authority, keep its format declarative, and parse untrusted
rows or keys once into precise valid values before the shared interpreter runs.
```

**Counterexample:** The cases are genuinely different algorithms, or the proposed table stores arbitrary callbacks. Keep direct code; a data-shaped programming language would hide rather than remove complexity.

**Decision:** Accepted. Every member changes a distinct part of the table decision: evidence, authority, expressive power, boundary trust, or valid state space.

### B03 — Trusted functional boundary

**Objective:** Convert weak external effects into trusted domain values before deterministic policy executes.

**Principles:** Separation of Concerns; Functional Core, Imperative Shell; Dependency Inversion Principle; Parse, Don't Validate; Make Illegal States Unrepresentable.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P116](./pair-dossiers/P116-separation-of-concerns-functional-core-imperative-shell.md) | Separation ↔ Functional Core/Shell — Reinforcement | Establishes the decision/effect boundary. |
| [P120](./pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md) | Separation ↔ DIP — Enablement | Points dependencies from effect details toward policy-owned contracts. |
| [P180](./pair-dossiers/P180-functional-core-imperative-shell-dependency-inversion-principle.md) | Functional Core/Shell ↔ DIP — Complementary | Places adapter composition in the shell and policy in the core. |
| [P183](./pair-dossiers/P183-functional-core-imperative-shell-parse-don-t-validate.md) | Functional Core/Shell ↔ Parse — Sequencing | Acquires and parses raw input before core decisions. |
| [P213](./pair-dossiers/P213-dependency-inversion-principle-parse-don-t-validate.md) | DIP ↔ Parse — Sequencing | Makes adapters construct values required by policy-owned contracts. |
| [P212](./pair-dossiers/P212-dependency-inversion-principle-make-illegal-states-unrepresentable.md) | DIP ↔ Illegal States — Complementary | Prevents vendor representations from widening the core's state space. |
| [P222](./pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md) | Illegal States ↔ Parse — Enablement | Produces the precise values consumed by policy. |

The graph is connected without relying on the rejected Functional Core/Shell ↔ Illegal States hypothesis; Parse and DIP supply the evidenced connections. It contains no frozen Tension or Conflict.

**Application order:**

1. Keep transport, file, clock, database, and network acquisition in the imperative shell.
2. Parse weak external values in adapters into precise domain values.
3. Call deterministic policy through domain-shaped inputs and narrow capabilities.
4. Interpret the policy result and perform effects in the shell.

**Candidate contract clause:**

```text
Keep I/O and vendor details in the shell. Parse their weak values at the adapter into
precise domain types, invoke deterministic policy through domain-shaped contracts,
then perform the resulting effects at the boundary.
```

**Counterexample:** A decision requires a database lock and current transactional state. Keep acquisition, validation, and decision within one transactional shell rather than pretending the state can be frozen into a pure input.

**Decision:** Accepted. The bundle uses only evidenced edges and does not revive P182, which adversarial review rejected.

### B04 — Evidence-backed deletion

**Objective:** Remove project-owned machinery safely and within the scope of current work.

**Principles:** KISS; Negative Code; Dead Code Elimination; Refactoring Toward Primitives; Boy Scout Rule.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P012](./pair-dossiers/P012-kiss-negative-code.md) | KISS ↔ Negative Code — Reinforcement | Treats contract-preserving removal as complexity reduction. |
| [P013](./pair-dossiers/P013-kiss-dead-code-elimination.md) | KISS ↔ DCE — Reinforcement | Removes complexity with no supported outcome. |
| [P014](./pair-dossiers/P014-kiss-refactoring-toward-primitives.md) | KISS ↔ Primitives — Reinforcement | Counts the whole-system cost of replacement. |
| [P187](./pair-dossiers/P187-negative-code-dead-code-elimination.md) | Negative Code ↔ DCE — Overlap | Identifies DCE as the liveness-proven deletion subset. |
| [P188](./pair-dossiers/P188-negative-code-refactoring-toward-primitives.md) | Negative Code ↔ Primitives — Enablement | Makes live custom implementation redundant after semantic verification. |
| [P195](./pair-dossiers/P195-negative-code-boy-scout-rule.md) | Negative Code ↔ Boy Scout — Sequencing | Bounds deletion to understood code touched by current work. |
| [P203](./pair-dossiers/P203-dead-code-elimination-boy-scout-rule.md) | DCE ↔ Boy Scout — Complementary | Combines liveness proof with incidental cleanup scope. |

The graph includes one Overlap edge but does not rely on Overlap for connectivity. It contains no frozen Tension or Conflict.

**Application order:**

1. Protect the current contract with proportionate tests, traces, or operational evidence.
2. Prove behavior dead or prove an existing primitive semantically adequate.
3. Delete the implementation and its obsolete flags, configuration, tests, documentation, and dependencies.
4. Keep incidental cleanup within the touched path; schedule unfamiliar system-wide removal separately.

**Candidate contract clause:**

```text
Within the touched path, preserve the current contract and remove only machinery proven
dead or made redundant by an exact existing primitive. Delete the obsolete perimeter too,
and stop when the cleanup would require unbounded investigation outside the task.
```

**Counterexample:** A rarely executed disaster-recovery path has no static callers but remains operationally supported, or a large dependency would replace a small clear local function. Do not delete or replace it on line-count evidence.

**Decision:** Accepted. The sequence distinguishes liveness proof, semantic replacement, whole-system simplicity, and bounded stewardship.

### B05 — Encapsulated domain commands

**Objective:** Turn weak input into a valid command and let the nearest state owner enforce the contextual transition without leaking object graphs.

**Principles:** Parse, Don't Validate; Make Illegal States Unrepresentable; Tell, Don't Ask; Law of Demeter.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P222](./pair-dossiers/P222-make-illegal-states-unrepresentable-parse-don-t-validate.md) | Illegal States ↔ Parse — Enablement | Constructs a valid command/value at the boundary. |
| [P223](./pair-dossiers/P223-make-illegal-states-unrepresentable-tell-don-t-ask.md) | Illegal States ↔ Tell, Don't Ask — Complementary | Constrains states and transitions through different mechanisms. |
| [P226](./pair-dossiers/P226-parse-don-t-validate-tell-don-t-ask.md) | Parse ↔ Tell, Don't Ask — Sequencing | Establishes structural trust before contextual acceptance. |
| [P227](./pair-dossiers/P227-parse-don-t-validate-law-of-demeter.md) | Parse ↔ Law of Demeter — Complementary, Reasoned Inference | Avoids passing weak transport graphs into domain code. |
| [P229](./pair-dossiers/P229-tell-don-t-ask-law-of-demeter.md) | Tell, Don't Ask ↔ Law of Demeter — Reinforcement | Replaces nested state inspection with a meaningful nearest-owner operation. |

The graph is connected through non-Overlap edges. P227 is visibly retained at its frozen Reasoned Inference grade; it is not silently upgraded. There is no frozen Tension or Conflict.

**Application order:**

1. Parse the raw request into a precise command value.
2. Pass that value directly to the nearest state owner rather than the transport object graph.
3. Let the owner decide contextual validity and perform or return a valid transition.
4. Return an explicit domain outcome; do not expose correlated setters or nested collaborators.

**Candidate contract clause:**

```text
Parse raw input into a precise command at the boundary, pass that command directly to
the nearest state owner, and let the owner enforce the contextual transition. Do not
make domain code traverse request, repository, or SDK object graphs to reconstruct it.
```

**Counterexample:** A renderer reads an immutable report value, or a parser traverses the syntax tree it owns. Queries and boundary parsing are legitimate; do not create forwarding commands merely to eliminate getters.

**Decision:** Accepted. The instruction preserves the qualifications in the Tell, Don't Ask and Law of Demeter sources and labels the inferred edge.

### B06 — Minimal policy-owned architecture

**Objective:** Isolate a demonstrated volatile detail behind the smallest cohesive, policy-owned, composable boundary.

**Principles:** Separation of Concerns; Single Responsibility Principle; Composition over Inheritance; Dependency Inversion Principle; Law of Demeter.

**Published interaction graph:**

| Edge | Relationship | Membership role |
|---|---|---|
| [P112](./pair-dossiers/P112-separation-of-concerns-single-responsibility-principle.md) | Separation ↔ SRP — Overlap | Uses actor/reason-for-change to sharpen the concern boundary. |
| [P113](./pair-dossiers/P113-separation-of-concerns-composition-over-inheritance.md) | Separation ↔ Composition — Enablement | Separates observed variation axes for independent assembly. |
| [P120](./pair-dossiers/P120-separation-of-concerns-dependency-inversion-principle.md) | Separation ↔ DIP — Enablement | Points the dependency from detail toward stable policy. |
| [P134](./pair-dossiers/P134-single-responsibility-principle-dependency-inversion-principle.md) | SRP ↔ DIP — Complementary | Combines cohesion with dependency direction. |
| [P147](./pair-dossiers/P147-composition-over-inheritance-dependency-inversion-principle.md) | Composition ↔ DIP — Complementary | Supplies the outer implementation without a subclass hierarchy. |
| [P152](./pair-dossiers/P152-composition-over-inheritance-law-of-demeter.md) | Composition ↔ Law of Demeter — Moderation | Prevents the assembled collaborator graph from leaking through the API. |
| [P215](./pair-dossiers/P215-dependency-inversion-principle-law-of-demeter.md) | DIP ↔ Law of Demeter — Reinforcement | Keeps policy from knowing low-level source or object-graph structure. |

The graph contains one Overlap edge but has multiple non-Overlap connections. It contains no frozen Tension or Conflict.

**Application order:**

1. Prove that policy and detail have different actors or rates of change.
2. Define the narrow policy-owned capability and precise values needed across the boundary.
3. Implement the detail as a composed adapter at the application edge, without a speculative hierarchy.
4. Keep the collaborator graph private; policy talks only to the immediate domain capability.

**Candidate contract clause:**

```text
Introduce an architectural boundary only for a demonstrated independent change or volatile
detail. Define the smallest policy-owned capability, compose its adapter at the edge, and
keep both the provider API and collaborator graph out of the policy.
```

**Counterexample:** A fixed internal helper has no external detail, independent actor, or variation axis. Call it directly; an interface, adapter, strategy, and composition root would be ceremonial structure.

**Decision:** Accepted. The bundle has one boundary objective and preserves the evidence threshold that prevents architecture for its own sake.

## Rejected bundle candidates

### R01 — Universal anti-bloat super-bundle

**Candidate principles:** KISS; YAGNI; DRY; Rule of Three; Separation of Concerns; Dependency Inversion Principle.

**Reason rejected:** “Reduce bloat” is not one operational objective. The set combines local implementation timing with an architectural policy/detail boundary and would encourage Separation or DIP even when their volatility preconditions fail. P015 is a frozen Tension, so the candidate also needs project-specific volatility evidence before it can be resolved. Use B01 for local abstraction timing or B06 for a demonstrated architecture boundary; do not merge them by default.

### R02 — Put all behavior in data and objects

**Candidate principles:** Data-Driven Design; Tell, Don't Ask; Make Illegal States Unrepresentable; Parse, Don't Validate; Functional Core, Imperative Shell.

**Reason rejected:** P219 is a frozen Tension between stateless table policy and state-owned transitions. The candidate provides no domain-specific rule for which behavior belongs in which form. It also tries to rely on P182, which adversarial review rejected. B02 handles regular stateless variation; B05 handles stateful commands.

### R03 — Primitive-first architecture

**Candidate principles:** Refactoring Toward Primitives; Dependency Inversion Principle; Law of Demeter; Composition over Inheritance.

**Reason rejected:** P204 and P209 are frozen Tensions. Without evidence about provider volatility and object-graph leakage, the candidate cannot decide between direct primitive use and an adapter. It would either wrap everything or leak every provider. Reconsider only after the concrete boundary facts are known.

### R04 — Cleanup trio

**Candidate principles:** Negative Code; Dead Code Elimination; Boy Scout Rule.

**Reason rejected:** The graph is connected, but P187 is primarily Overlap and the candidate omits the adequacy and replacement mechanisms that distinguish safe deletion from a narrow unused-code sweep. B04 covers the same objective with KISS and Refactoring Toward Primitives while retaining the bounded cleanup sequence.

### R05 — Layered domain object bundle

**Candidate principles:** Separation of Concerns; Single Responsibility Principle; Tell, Don't Ask.

**Reason rejected:** Its positive connection is only P112 Overlap, while P124 and P138 are Tensions whose resolution depends on the specific infrastructure, actor, and invariant boundaries. A generic bundle would give contradictory placement instructions rather than one usable objective.

### R06 — Convention-driven dependency architecture

**Candidate principles:** Convention over Configuration; Dependency Inversion Principle; Rule of Three.

**Reason rejected:** P159 is a frozen Tension between hidden discovery and inspectable dependency ownership. A particular framework may resolve it, but the catalog-level evidence cannot. The candidate therefore lacks a context-independent combined instruction.
