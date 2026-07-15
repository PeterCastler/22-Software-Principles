# Adversarial Review of Proposed Principle Interactions

## Scope and decision rule

This pre-freeze review evaluates all 82 rows marked `publish` in `pair-screening.csv`, one by one, against the canonical profiles, source register, primary screen, blind independent screen, and the corresponding dossiers. It does not infer or discuss bundles.

Each row was retested for a shared decision surface, an identifiable pair-specific causal mechanism, a material decision consequence, adequate evidence, and a counterexample that actually limits the claim. A `Direct` grade is retained only when an authoritative source explicitly discusses the interaction or explicitly connects the two operational recommendations; co-occurrence of two desirable qualities in one source is insufficient. A `Convergent` grade requires separate credible sources plus a specific mechanism, not generic maintainability similarity.

Verdicts mean:

- `accept`: proposed taxonomy and evidence grade survive.
- `downgrade`: the interaction remains publishable only with the recommended taxonomy or lower evidence grade.
- `reject`: the proposal should return to `Independence / Unsupported`.

## Adversarial findings

- Ten of thirteen proposed `Direct` grades survive. P002, P106, and P134 do not have an authoritative source explicitly establishing the exact claimed interaction and are reduced to `Convergent`.
- Four proposals fail the pair-specific mechanism test: P104, P146, P182, and P189. Each depends on a primitive, type, collaborator, or abstraction happening to participate in both principles rather than one principle materially changing the other's decision.
- Of twelve proposed primary `Tension` rows, eight retain Tension with workable resolution procedures. P045 and P046 are scope-partitioning relationships, P152 is moderation of exposure, and P189 is rejected.
- The accepted Tension procedures reconcile the pressures by defining a stopping test: proven volatility for P015, representational payoff for P017, invariant ownership boundaries for P124 and P138, explicit composition-edge ownership for P159, semantic narrowing for P204 and P209, and stateless-versus-stateful rule placement for P219.

## Sources rechecked

The canonical citations and source IDs remain recorded in [source-register.md](./source-register.md). The following interaction-bearing primary or authoritative URLs were rechecked for this review:

- Simplicity and evolutionary design: [Is Design Dead?](https://martinfowler.com/articles/designDead.html), [Beck Design Rules](https://martinfowler.com/bliki/BeckDesignRules.html), and [Keep it simple](https://engineering.homeoffice.gov.uk/principles/keep-it-simple/).
- Abstraction timing and dependency direction: [Rule of Three](https://understandlegacycode.com/blog/refactoring-rule-of-three/), [DIP in the Wild](https://martinfowler.com/articles/dipInTheWild.html), and [Common web application architectures](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures).
- Representation and parsing: [The Rule of Least Power](https://www.w3.org/2001/tag/doc/leastPower.html), [XML Schema 1.1 Structures](https://www.w3.org/TR/xmlschema11-1/), and [Parse, don't validate](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/).
- Unix and data-driven design: [Basics of the Unix Philosophy](https://www.catb.org/esr/writings/taoup/html/ch01s06.html) and [Data-Driven Programming](https://www.catb.org/esr/writings/taoup/html/ch09s01.html).
- Replacement and deletion: [Don't Reinvent the Wheel](https://arxiv.org/abs/2208.07624), [Remove Dead Code](https://refactoring.com/catalog/removeDeadCode.html), and [-2000 Lines of Code](https://www.folklore.org/Negative_2000_Lines_Of_Code.html).
- Defaults and effects: [The Ruby on Rails Doctrine](https://rubyonrails.org/doctrine#convention-over-configuration) and [Simplify Your Code: Functional Core, Imperative Shell](https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html).

## Machine-readable adjudication table

| pair_id | pair | proposed_taxonomy | proposed_evidence | verdict | recommended_taxonomy | recommended_evidence | rationale |
|---|---|---|---|---|---|---|---|
| P001 | KISS ↔ YAGNI | Reinforcement | Direct | accept | Reinforcement | Direct | I001 explicitly treats YAGNI as simple design and explains that deferred capability avoids current complexity; the current-requirement counterexample correctly stops the claim. |
| P002 | KISS ↔ DRY | Moderation | Direct | downgrade | Moderation | Convergent | I001 and I003 explicitly place duplication inside simple-design criteria, but neither directly establishes the dossier's abstraction-cost moderation; the mechanism is still supported by converging simplicity and DRY evidence. |
| P003 | KISS ↔ Rule of Three | Moderation | Convergent | downgrade | Reinforcement | Convergent | Waiting for concrete cases does not constrain KISS; it reinforces KISS by preventing speculative abstraction. A predefined protocol remains a valid stopping counterexample. |
| P004 | KISS ↔ Occam's Razor | Overlap | Convergent | accept | Overlap | Convergent | Both principles compare equally adequate candidates and reject unnecessary complexity for distinct reasons; omission of a required audit trail correctly falls outside both preconditions. |
| P005 | KISS ↔ Principle of Least Power | Reinforcement | Convergent | accept | Reinforcement | Convergent | Less expressive adequate mechanisms remove possible behavior and analysis burden from the KISS complexity budget; an overgrown declarative workaround is a valid adequacy counterexample. |
| P006 | KISS ↔ Separation of Concerns | Moderation | Convergent | accept | Moderation | Convergent | The boundary decision is shared and KISS materially limits separation strength to the cheapest boundary that repays integration cost; the cohesive-invariant counterexample is specific. |
| P009 | KISS ↔ Convention over Configuration | Moderation | Convergent | accept | Moderation | Convergent | Convention removes routine configuration while KISS limits hidden discovery and exception precedence; the proposed moderation and exception-dominance boundary are operational. |
| P012 | KISS ↔ Negative Code | Reinforcement | Convergent | accept | Reinforcement | Convergent | Contract-preserving removal directly reduces concepts and obligations counted by KISS; the code-golf counterexample distinguishes deletion from genuine simplification. |
| P013 | KISS ↔ Dead Code Elimination | Reinforcement | Convergent | accept | Reinforcement | Convergent | Proven-dead behavior adds complexity with no supported consequence, so DCE directly reinforces KISS; rare operational liveness is an adequate falsifier. |
| P014 | KISS ↔ Refactoring Toward Primitives | Reinforcement | Convergent | accept | Reinforcement | Convergent | A contract-equivalent primitive can remove custom machinery and lifecycle load; semantic mismatch or dependency weight is a concrete counterexample rather than generic reuse praise. |
| P015 | KISS ↔ Dependency Inversion Principle | Tension | Convergent | accept | Tension | Convergent | The Tension resolution is sound: establish real volatility first, then use the narrowest policy-owned boundary; otherwise keep the stable detail direct. |
| P016 | KISS ↔ Data-Driven Design | Moderation | Convergent | accept | Moderation | Convergent | KISS materially moderates the data-versus-control-flow choice by rejecting both callback-filled tables and sprawling regular branches; irregular algorithms stop the interaction. |
| P017 | KISS ↔ Make Illegal States Unrepresentable | Tension | Convergent | accept | Tension | Convergent | The Tension is real and resolved by comparing removed invalid-state branches with added representational burden; the single-check case is a valid stopping rule. |
| P022 | YAGNI ↔ DRY | Moderation | Convergent | accept | Moderation | Convergent | The shared abstraction decision distinguishes current duplicated authority from predicted reuse, so YAGNI specifically moderates DRY rather than merely sharing a maintenance benefit. |
| P023 | YAGNI ↔ Rule of Three | Reinforcement | Convergent | accept | Reinforcement | Convergent | Both govern abstraction timing and repeated cases supply present-need evidence; an already authoritative security rule correctly permits earlier extraction. |
| P024 | YAGNI ↔ Occam's Razor | Reinforcement | Convergent | accept | Reinforcement | Convergent | Forecast-only capability is an unsupported assumption in Occam's comparison, creating a specific reinforcing mechanism; a contracted irreversible migration is current evidence. |
| P035 | YAGNI ↔ Dependency Inversion Principle | Moderation | Direct | accept | Moderation | Direct | I010 explicitly discusses YAGNI while applying SRP or DIP factoring, warning against speculative design; this satisfies Direct evidence for the moderation. |
| P036 | YAGNI ↔ Data-Driven Design | Moderation | Convergent | accept | Moderation | Convergent | YAGNI specifically limits a current table from expanding into a speculative rules platform; a finite present mapping is a concrete counterexample and material decision. |
| P042 | DRY ↔ Rule of Three | Moderation | Direct | accept | Moderation | Direct | I004 explicitly discusses DRY, wrong abstractions, tolerated duplication, and the Rule of Three as the timing heuristic, satisfying the Direct standard. |
| P045 | DRY ↔ Separation of Concerns | Tension | Convergent | downgrade | Complementary | Convergent | Correctly applied DRY centralizes one owned fact while Separation of Concerns separates facts with independent ownership; those tests partition cases rather than exert opposing pressures. |
| P046 | DRY ↔ Single Responsibility Principle | Tension | Convergent | downgrade | Moderation | Convergent | SRP's actor and reason-for-change test limits when DRY may create an authority. Because DRY already excludes independently owned facts, the relation is moderation, not genuine Tension. |
| P048 | DRY ↔ Convention over Configuration | Reinforcement | Convergent | accept | Reinforcement | Convergent | A stable convention can act as the single authority for a routine non-domain choice and remove restated configuration; independent regulatory settings are an appropriate counterexample. |
| P055 | DRY ↔ Data-Driven Design | Enablement | Direct | accept | Enablement | Direct | I015 explicitly presents data representation as a single point of knowledge replacing scattered logic, so a typed case table can directly enable DRY. |
| P056 | DRY ↔ Make Illegal States Unrepresentable | Enablement | Direct | accept | Enablement | Direct | I007 explicitly states that duplicated mutable data creates the illegal out-of-sync state and recommends a single source of truth; Direct evidence and the denormalization boundary both hold. |
| P057 | DRY ↔ Parse, Don't Validate | Enablement | Direct | accept | Enablement | Direct | I007 explicitly contrasts shotgun repeated validation with one parsing boundary that preserves proof, directly supporting removal of duplicate structural checks. |
| P065 | Rule of Three ↔ Composition over Inheritance | Sequencing | Convergent | accept | Sequencing | Convergent | Concrete variants reveal independent axes before composition is introduced, yielding a specific sequence and a subclass-combination consequence; an external composition contract is a valid exception. |
| P066 | Rule of Three ↔ Convention over Configuration | Sequencing | Convergent | accept | Sequencing | Convergent | Observed repeated choices supply evidence for a dominant default before convention makes it implicit; an established ecosystem convention correctly supplies evidence externally. |
| P072 | Rule of Three ↔ Dependency Inversion Principle | Moderation | Convergent | accept | Moderation | Convergent | The Rule of Three moderates ceremonial inversion without imposing a literal count when one real volatile boundary exists; the payment-SDK counterexample preserves that qualification. |
| P073 | Rule of Three ↔ Data-Driven Design | Sequencing | Convergent | accept | Sequencing | Convergent | Several cases reveal the common algorithm and table dimensions before data extraction, creating a concrete sequencing mechanism; protocol-defined mappings can supply earlier evidence. |
| P079 | Occam's Razor ↔ Principle of Least Power | Reinforcement | Convergent | accept | Reinforcement | Convergent | For equally adequate mechanisms, lower expressiveness removes unsupported possible behavior, specifically reinforcing Occam rather than merely offering the same generic benefit. |
| P088 | Occam's Razor ↔ Refactoring Toward Primitives | Reinforcement | Convergent | accept | Reinforcement | Convergent | Contract-equivalent primitive use can remove project-owned entities and assumptions in Occam's comparison; incompatible errors or lock-in correctly defeat equal adequacy. |
| P104 | Principle of Least Power ↔ Refactoring Toward Primitives | Reinforcement | Convergent | reject | Independence | Unsupported | The claim that primitives are often constrained is contingent coincidence: existing capabilities may be more expressive, and Least Power may favor a custom declarative form. Neither principle causally changes the other's decision. |
| P106 | Principle of Least Power ↔ Data-Driven Design | Enablement | Direct | downgrade | Reinforcement | Convergent | I005 directly applies Least Power to declarative constraint choices, but it does not discuss regular case variation as Data-Driven Design. Data representation reinforces lower expressiveness; it does not enable the principle. |
| P107 | Principle of Least Power ↔ Make Illegal States Unrepresentable | Reinforcement | Convergent | accept | Reinforcement | Convergent | A representation excluding invalid combinations is less powerful along the exact harmful state dimension, with advanced or mutable-fact encodings as concrete limits. |
| P112 | Separation of Concerns ↔ Single Responsibility Principle | Overlap | Convergent | accept | Overlap | Convergent | Both govern boundaries for independently changing work, while SRP narrows the test to actor or business reason; the cohesive multi-operation module properly limits the overlap. |
| P113 | Separation of Concerns ↔ Composition over Inheritance | Enablement | Convergent | accept | Enablement | Convergent | Separating observed variation axes enables their recombination without subclass multiplication; fixed behavior is a concrete counterexample to adding strategies. |
| P115 | Separation of Concerns ↔ Unix Philosophy | Reinforcement | Direct | accept | Reinforcement | Direct | I016 explicitly states the Unix Rule of Separation within the connected Unix design rules, so focused composable components directly operationalize separation. |
| P116 | Separation of Concerns ↔ Functional Core, Imperative Shell | Enablement | Convergent | downgrade | Reinforcement | Convergent | Functional Core, Imperative Shell is a specific instance of separating decisions from effects, not something independently enabled by generic separation. The pair therefore reinforces the same boundary. |
| P120 | Separation of Concerns ↔ Dependency Inversion Principle | Enablement | Direct | accept | Enablement | Direct | I008 explicitly moves from separation by responsibility to DIP as the correction for inward policy dependence, establishing the boundary and dependency-direction interaction directly. |
| P123 | Separation of Concerns ↔ Parse, Don't Validate | Sequencing | Convergent | downgrade | Reinforcement | Convergent | Parsing creates and preserves a raw-to-trusted concern boundary, reinforcing separation. Separation of Concerns itself does not impose the proposed parse-before-domain sequence. |
| P124 | Separation of Concerns ↔ Tell, Don't Ask | Tension | Convergent | accept | Tension | Convergent | The Tension resolution genuinely reconciles pressures: keep invariant behavior with its state owner while leaving persistence, presentation, and orchestration outside. |
| P125 | Separation of Concerns ↔ Law of Demeter | Reinforcement | Convergent | accept | Reinforcement | Convergent | Object-graph navigation can bypass a real concern boundary, and a meaningful near-neighbor capability materially restores it; transparent immutable view data is a valid boundary. |
| P129 | Single Responsibility Principle ↔ Unix Philosophy | Overlap | Convergent | accept | Overlap | Convergent | Both select cohesive component scope but use distinct tests, with Unix additionally requiring composability; a cohesive compiler with many internal operations correctly limits literal one-job readings. |
| P134 | Single Responsibility Principle ↔ Dependency Inversion Principle | Complementary | Direct | downgrade | Complementary | Convergent | I008 and I010 discuss responsibility decomposition and DIP together, but do not explicitly establish SRP's actor-based test as the cause of DIP direction. The complementary mechanism remains convergently supported. |
| P138 | Single Responsibility Principle ↔ Tell, Don't Ask | Tension | Convergent | accept | Tension | Convergent | The Tension resolution is sound: SRP sets the actor boundary and Tell, Don't Ask places only that actor's invariant behavior with the state, excluding storage and rendering. |
| P142 | Composition over Inheritance ↔ Unix Philosophy | Reinforcement | Convergent | accept | Reinforcement | Convergent | Unix composition of focused tools and composition of focused behavior share an operational assembly surface, with process fragmentation serving as a material counterexample. |
| P146 | Composition over Inheritance ↔ Refactoring Toward Primitives | Enablement | Convergent | reject | Independence | Unsupported | A platform primitive can happen to serve as a collaborator, but that does not generally enable composition or eliminate inheritance. The proposed adapter example is a tactic-specific coincidence. |
| P147 | Composition over Inheritance ↔ Dependency Inversion Principle | Complementary | Convergent | accept | Complementary | Convergent | DIP defines the policy-owned contract while composition supplies the outer implementation without a base class; a fixed mock-only helper correctly stops the interaction. |
| P152 | Composition over Inheritance ↔ Law of Demeter | Tension | Convergent | downgrade | Moderation | Convergent | Composition does not pressure callers to expose or traverse the collaborator graph, so no genuine Tension exists. Demeter instead moderates how a composed object exposes its assembly. |
| P158 | Convention over Configuration ↔ Refactoring Toward Primitives | Reinforcement | Convergent | accept | Reinforcement | Convergent | When a maintained platform primitive embodies a stable convention, adopting it can remove custom discovery and configuration; opaque inference with dominant overrides is a specific counterexample. |
| P159 | Convention over Configuration ↔ Dependency Inversion Principle | Tension | Convergent | accept | Tension | Convergent | The Tension resolution is coherent: use convention only at the composition edge while retaining explicit policy ownership, lifetimes, and dependency direction; switch to explicit wiring when inspection fails. |
| P166 | Unix Philosophy ↔ Functional Core, Imperative Shell | Complementary | Convergent | accept | Complementary | Convergent | Focused value-oriented stages and a core/shell effect boundary perform distinct complementary work; an I/O-only pass-through command correctly lacks a useful core. |
| P169 | Unix Philosophy ↔ Refactoring Toward Primitives | Reinforcement | Convergent | accept | Reinforcement | Convergent | Unix's explicit reuse-and-composition pressure supplies candidate existing capabilities, while primitive refactoring verifies contract fit and removes custom machinery. |
| P171 | Unix Philosophy ↔ Data-Driven Design | Enablement | Direct | accept | Enablement | Direct | I015 is an explicit Data-Driven Programming chapter within the Unix design synthesis and I016 names the Rule of Representation, satisfying Direct interaction evidence. |
| P173 | Unix Philosophy ↔ Parse, Don't Validate | Sequencing | Convergent | accept | Sequencing | Convergent | At an open pipeline boundary, parsing must precede trusted domain transformation; an intentionally opaque text stage is a concrete case where the sequence does not apply. |
| P180 | Functional Core, Imperative Shell ↔ Dependency Inversion Principle | Complementary | Convergent | accept | Complementary | Convergent | Core/shell placement separates policy from effects, while DIP shapes and points the capability boundary; pure calculations without effects correctly need neither. |
| P182 | Functional Core, Imperative Shell ↔ Make Illegal States Unrepresentable | Enablement | Convergent | reject | Independence | Unsupported | Precise types benefit deterministic and imperative code alike; a pure core neither causes nor requires illegal-state exclusion. The dossier offers generic type-safety benefit rather than a pair-specific mechanism. |
| P183 | Functional Core, Imperative Shell ↔ Parse, Don't Validate | Sequencing | Convergent | accept | Sequencing | Convergent | The shell's acquisition of raw input and the core's trusted signature create a concrete parse-before-decision sequence; transactional state is a valid exception. |
| P187 | Negative Code ↔ Dead Code Elimination | Enablement | Convergent | downgrade | Overlap | Convergent | DCE is the liveness-proven subset of Negative Code, while Negative Code also covers replacement of live machinery. That set relationship is primarily Overlap, not Enablement. |
| P188 | Negative Code ↔ Refactoring Toward Primitives | Enablement | Convergent | accept | Enablement | Convergent | A contract-matching primitive specifically makes the custom implementation and glue removable, directly enabling negative code; dependency weight limits false line-count wins. |
| P189 | Negative Code ↔ Dependency Inversion Principle | Tension | Convergent | reject | Independence | Unsupported | Negative Code's deletion test applies to every abstraction; a one-implementation DIP boundary is merely one counterexample to careless deletion, not a unique causal interaction between the principles. |
| P191 | Negative Code ↔ Make Illegal States Unrepresentable | Enablement | Convergent | accept | Enablement | Convergent | Controlled precise construction can make repeated impossible-state guards and synchronized fields removable; mutable authorization correctly remains live. |
| P192 | Negative Code ↔ Parse, Don't Validate | Enablement | Convergent | accept | Enablement | Convergent | A parser result carried in signatures makes repeated structural validators and casts safely removable, while use-time limits remain valid counterexamples. |
| P195 | Negative Code ↔ Boy Scout Rule | Sequencing | Convergent | accept | Sequencing | Convergent | Boy Scout scope supplies a concrete task sequence for small verified deletions, while unfamiliar cross-system fallback removal correctly exceeds that scope. |
| P199 | Dead Code Elimination ↔ Make Illegal States Unrepresentable | Sequencing | Convergent | accept | Sequencing | Convergent | Closing all supported construction paths can make old defensive branches unreachable, after which DCE applies; legacy persisted rows correctly keep them live. |
| P200 | Dead Code Elimination ↔ Parse, Don't Validate | Sequencing | Convergent | accept | Sequencing | Convergent | When every entry path parses into a trusted type, downstream malformed-structure branches can become unreachable; any raw public bypass defeats the sequence. |
| P203 | Dead Code Elimination ↔ Boy Scout Rule | Enablement | Convergent | downgrade | Complementary | Convergent | DCE supplies the liveness proof and Boy Scout supplies incidental scope and timing; neither enables the other, so Complementary better captures the two distinct controls. |
| P204 | Refactoring Toward Primitives ↔ Dependency Inversion Principle | Tension | Convergent | accept | Tension | Convergent | The Tension resolution is sound: call a fitting primitive directly unless a real policy boundary requires semantic narrowing, and delete wrappers that only mirror it. |
| P206 | Refactoring Toward Primitives ↔ Make Illegal States Unrepresentable | Enablement | Convergent | accept | Enablement | Convergent | A matching set, union, constructor, or storage constraint can replace custom enforcement while excluding the invalid state; error-semantics mismatch is a material counterexample. |
| P207 | Refactoring Toward Primitives ↔ Parse, Don't Validate | Enablement | Convergent | accept | Enablement | Convergent | A standard parser or decoder can construct the precise trusted value and replace handwritten checks, subject to exact normalization and error semantics. |
| P209 | Refactoring Toward Primitives ↔ Law of Demeter | Tension | Convergent | accept | Tension | Convergent | The Tension resolution is coherent: use flat stable primitives directly, adding only a narrow capability boundary when callers would otherwise traverse a volatile graph. |
| P212 | Dependency Inversion Principle ↔ Make Illegal States Unrepresentable | Complementary | Convergent | accept | Complementary | Convergent | A domain-owned port with precise values specifically prevents vendor states from widening policy's representable space; a passthrough adapter falsifies the mechanism. |
| P213 | Dependency Inversion Principle ↔ Parse, Don't Validate | Sequencing | Convergent | accept | Sequencing | Convergent | An outer adapter must parse weak vendor data before satisfying a policy-owned precise contract; an already typed collaborator correctly needs inversion without parsing. |
| P215 | Dependency Inversion Principle ↔ Law of Demeter | Reinforcement | Convergent | accept | Reinforcement | Convergent | DIP controls source dependency while Demeter controls graph knowledge through the boundary, jointly preventing policy from traversing volatile detail structure. |
| P217 | Data-Driven Design ↔ Make Illegal States Unrepresentable | Enablement | Convergent | accept | Enablement | Convergent | When a table is the authoritative finite case set, derived precise keys can remove unknown-key states and duplicated enums; user-defined runtime keys defeat closure. |
| P218 | Data-Driven Design ↔ Parse, Don't Validate | Sequencing | Convergent | accept | Sequencing | Convergent | Untrusted selectors or rule rows must be parsed before the shared table interpreter can assume valid keys and schema; compiler-generated keys remove the need. |
| P219 | Data-Driven Design ↔ Tell, Don't Ask | Tension | Convergent | accept | Tension | Convergent | The Tension resolution genuinely separates stateless regular mappings from state-owner transitions, allowing an owner operation to consult data without moving its invariant into callbacks. |
| P222 | Make Illegal States Unrepresentable ↔ Parse, Don't Validate | Enablement | Direct | accept | Enablement | Direct | I007 explicitly instructs parsing into the most precise representation and directly names making illegal states unrepresentable, satisfying Direct evidence. |
| P223 | Make Illegal States Unrepresentable ↔ Tell, Don't Ask | Complementary | Convergent | accept | Complementary | Convergent | Precise representations constrain static states while owner commands constrain transitions, producing distinct complementary protections; immutable report values need no command API. |
| P226 | Parse, Don't Validate ↔ Tell, Don't Ask | Sequencing | Convergent | accept | Sequencing | Convergent | Parsing establishes structural trust before the state owner evaluates contextual validity, with reporting queries correctly stopping the command sequence. |
| P227 | Parse, Don't Validate ↔ Law of Demeter | Complementary | Convergent | downgrade | Complementary | Reasoned Inference | The mechanism is plausible only when raw transport graph leakage and weak input coincide; I007 and the Demeter sources do not explicitly discuss their interaction, so Convergent overstates the evidence. |
| P229 | Tell, Don't Ask ↔ Law of Demeter | Reinforcement | Convergent | accept | Reinforcement | Convergent | Both replace caller knowledge of nested mutable state with a meaningful nearest-owner operation, while legitimate rendering of immutable values is a clear counterexample. |

## Exact counts

Verdicts:

- accept: 66
- downgrade: 12
- reject: 4
- total: 82

Recommended primary taxonomy:

- Reinforcement: 22
- Enablement: 13
- Moderation: 11
- Sequencing: 11
- Complementary: 9
- Overlap: 4
- Tension: 8
- Conflict: 0
- Independence: 4

Recommended evidence grade:

- Direct: 10
- Convergent: 67
- Reasoned Inference: 1
- Unsupported: 4
