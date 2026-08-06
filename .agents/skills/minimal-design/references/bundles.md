# Validated Bundles

Use a bundle only when its objective and every member's preconditions hold. Prefer no bundle to a thematic match. Preserve the order and counterexample.

## Contents

- B01 Evidence-led minimal design
- B02 Constrained data for regular variation
- B03 Trusted functional boundary
- B04 Evidence-backed deletion
- B05 Encapsulated domain commands
- B06 Minimal policy-owned architecture

## B01 — Evidence-led minimal design

- **Objective:** deliver the smallest present solution while preventing premature or wrongly scoped abstraction.
- **Principles:** KISS, YAGNI, Rule of Three, DRY.
- **Activate when:** a current implementation is accumulating predicted capability, shared helpers, or abstractions before stable repeated knowledge is established.
- **Order:** establish the complete present requirement; implement the clearest adequate direct design; observe real repetitions; centralize only one stable jointly owned fact.
- **Instruction:** implement only the current complete requirement. Leave uncertain early duplication local; give stable repeated knowledge one authority once evidence establishes it.
- **Counterexample:** centralize a published protocol, security invariant, or regulated rule immediately rather than waiting for three copies.
- **Accepted edges:** P001, P003, P022, P042.

## B02 — Constrained data for regular variation

- **Objective:** replace repeated regular branching with one inspectable, trusted, minimally expressive data representation.
- **Principles:** Rule of Three, Data-Driven Design, DRY, Principle of Least Power, Parse Don't Validate, Make Illegal States Unrepresentable.
- **Activate when:** real cases demonstrate one stable algorithm, regular variation, and a finite or precisely parseable row shape.
- **Order:** prove regularity; define one table and interpreter; keep rows declarative; parse external rows and keys into precise values before use.
- **Instruction:** make the typed table the single authority and let one shared interpreter operate only on trusted rows and keys.
- **Counterexample:** keep direct code when cases are different algorithms or the table would store arbitrary callbacks.
- **Accepted edges:** P073, P055, P106, P218, P217, P222.

## B03 — Trusted functional boundary

- **Objective:** convert weak external effects into trusted domain values before deterministic policy executes.
- **Principles:** Separation of Concerns, Functional Core Imperative Shell, Dependency Inversion Principle, Parse Don't Validate, Make Illegal States Unrepresentable.
- **Activate when:** domain policy is materially tangled with I/O, vendor shapes, and weak external values.
- **Order:** acquire effects in the shell; parse in the adapter; call deterministic policy with precise values and narrow domain capabilities; perform resulting effects at the boundary.
- **Instruction:** keep I/O and vendor details outside policy and make the policy signature express only trusted domain needs.
- **Counterexample:** keep lock-dependent acquisition, validation, and decision inside one transactional shell.
- **Accepted edges:** P116, P120, P180, P183, P213, P212, P222.

## B04 — Evidence-backed deletion

- **Objective:** remove project-owned machinery safely and within current scope.
- **Principles:** KISS, Negative Code, Dead Code Elimination, Refactoring Toward Primitives, Boy Scout Rule.
- **Activate when:** code may be dead or an exact existing primitive may make custom machinery redundant.
- **Order:** protect the contract; prove liveness absence or primitive adequacy; delete implementation and obsolete perimeter; keep incidental cleanup inside the touched path.
- **Instruction:** remove only machinery proven dead or exactly replaced, and verify the supported behavior that remains.
- **Counterexample:** preserve a supported rare recovery path; reject a large dependency that replaces a small clear function.
- **Accepted edges:** P012, P013, P014, P187, P188, P195, P203.

## B05 — Encapsulated domain commands

- **Objective:** turn weak input into a valid command and let the nearest state owner enforce the contextual transition without leaking object graphs.
- **Principles:** Parse Don't Validate, Make Illegal States Unrepresentable, Tell Don't Ask, Law of Demeter.
- **Activate when:** domain code reconstructs commands from transport or collaborator graphs and callers perform invariant-sensitive query-decide-mutate sequences.
- **Order:** parse a precise command; pass it directly to the state owner; let the owner decide contextual validity and transition; return an explicit outcome.
- **Instruction:** keep raw transport and graph traversal at the boundary while the state owner protects its transition.
- **Counterexample:** renderers may read immutable report values and parsers may traverse syntax trees they own; do not manufacture forwarding commands.
- **Accepted edges:** P222, P223, P226, P227 (Reasoned Inference), P229.

## B06 — Minimal policy-owned architecture

- **Objective:** isolate a demonstrated volatile detail behind the smallest cohesive, policy-owned, composable boundary.
- **Principles:** Separation of Concerns, Single Responsibility Principle, Composition over Inheritance, Dependency Inversion Principle, Law of Demeter.
- **Activate when:** evidence shows an independent actor, rate of change, external provider, or collaborator graph that should not shape stable policy.
- **Order:** prove the independent change; define the narrow policy-owned capability; compose the adapter at the edge; keep provider and collaborator structure private.
- **Instruction:** introduce only the boundary required by demonstrated volatility and keep assembly outside policy.
- **Counterexample:** call a fixed internal helper directly when it has no external detail, independent actor, or variation axis.
- **Accepted edges:** P112, P113, P120, P134, P147, P152, P215.
