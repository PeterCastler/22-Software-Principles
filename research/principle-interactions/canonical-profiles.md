# Canonical Principle Profiles

These profiles normalize the library's 22 principles into operational decisions. They are the only inputs used for the initial pair screens. A profile describes what a principle actually asks a practitioner to decide; it does not assert any relationship with another catalog entry.

## KISS — Keep It Simple, Stupid

Principle: Choose the least complicated design that completely satisfies the present behavior and quality constraints.

Primary problem addressed: Accidental complexity—extra concepts, states, dependencies, execution paths, indirection, and operational obligations not demanded by the problem.

Recommended action: State the complete requirements, compare adequate designs across their lifecycle, and remove or avoid mechanisms whose cost is not justified by a present constraint.

Decision object: The overall mechanism and complexity budget of an implementation or design.

Preconditions: The required behavior and relevant correctness, security, performance, compatibility, accessibility, and operational constraints are known well enough to judge adequacy.

Expected benefit: Lower cognitive and operational load, clearer execution paths, and less code and infrastructure to maintain.

Common over-application: Treating short code, one file, missing error handling, familiar technology, or hidden framework behavior as inherently simple.

Known limitations: Essential domain and operational complexity cannot be removed; additional structure can be the simpler whole-system design when it isolates real change or risk.

Primary sources:

- [Keep it simple — UK Home Office Engineering Guidance](https://engineering.homeoffice.gov.uk/principles/keep-it-simple/)
- [KISS Software Design Principle — Baeldung](https://www.baeldung.com/cs/kiss-software-design-principle)

## YAGNI — You Aren't Gonna Need It

Principle: Do not build a capability or extension point until a current requirement, consumer, or risk-control obligation needs it.

Primary problem addressed: Speculative features and flexibility that incur build, delay, carry, and repair costs before providing value.

Recommended action: Name the present consumer, postpone presumptive capability, preserve low-cost malleability, and record future ideas outside the running design.

Decision object: The timing of adding a capability, option, abstraction, compatibility path, or extension mechanism.

Preconditions: The proposed work can be separated from current delivery, and deferral does not violate a current contract or create disproportionate irreversible risk.

Expected benefit: Earlier delivery, less carrying complexity, and better future design decisions based on concrete requirements.

Common over-application: Using YAGNI to omit current nonfunctional requirements, tests, refactoring, observability, or inexpensive preparation for truly irreversible decisions.

Known limitations: Public protocols, persistent data formats, regulated records, hardware, and other high-reversal-cost decisions can make limited preparation a present requirement.

Primary sources:

- [Yagni — Martin Fowler](https://martinfowler.com/bliki/Yagni.html)
- [Is Design Dead? — Martin Fowler](https://martinfowler.com/articles/designDead.html)

## DRY — Don't Repeat Yourself

Principle: Give each changing piece of knowledge or intent one unambiguous authoritative representation.

Primary problem addressed: Multiple authorities for one fact that must be changed together and can diverge.

Recommended action: Identify the shared knowledge, choose its narrowest proper authority, derive other representations when practical, and remove competing authorities.

Decision object: The ownership and representation of a rule, schema, mapping, contract, or other knowledge.

Preconditions: The occurrences represent the same domain fact, have the same ownership, and should change for the same reason.

Expected benefit: Lower synchronization risk, fewer contradictory representations, and smaller change sets for one conceptual change.

Common over-application: Deduplicating similar syntax whose meanings or owners are independent, or centralizing test expectations so tests merely repeat the implementation.

Known limitations: Explanatory repetition can aid readers; independent policies may temporarily or permanently share identical code; deriving artifacts can add tooling cost.

Primary sources:

- [The Pragmatic Programmer — DRY excerpt](https://media.pragprog.com/titles/tpp20/dry.pdf)
- [Architectural Principles: DRY — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#dont-repeat-yourself-dry)

## Rule of Three

Principle: Let multiple concrete cases reveal a stable abstraction before extracting one; three is an evidence heuristic, not a mandatory count.

Primary problem addressed: Premature abstraction based on incomplete understanding that later accumulates flags, exceptions, and caller-specific behavior.

Recommended action: Implement early cases locally, compare their meaning and variation, and extract only the smallest stable concept once evidence and a precise name emerge.

Decision object: The timing and scope of abstraction over repeated implementations.

Preconditions: More than one concrete occurrence exists, their similarities and differences can be compared, and the cost of temporary duplication is acceptable.

Expected benefit: Better-fitting abstractions, preserved independent evolution while learning, and less speculative generalization.

Common over-application: Treating the third copy as an automatic refactoring command or refusing earlier abstraction despite a pre-existing authoritative domain concept.

Known limitations: High-risk duplicated policy, standards, or already-defined domain authority can justify extraction before three; unrelated cases can justify waiting indefinitely.

Primary sources:

- [Don't make Clean Code harder to maintain, use the Rule of Three — Nicolas Carlo](https://understandlegacycode.com/blog/refactoring-rule-of-three/)
- [Origins of “The Rule of Three” — Eoin Noble](https://eoinnoble.com/posts/origins-of-the-rule-of-three/)

## Occam's Razor

Principle: Among explanations or solutions that account for the same evidence and requirements, prefer the one with fewer unsupported assumptions and unnecessary entities.

Primary problem addressed: Designs and diagnoses multiplied beyond what current evidence supports.

Recommended action: Hold adequacy constant, enumerate assumptions and whole-system obligations, test cheaper explanations first, and add entities only when evidence warrants them.

Decision object: Selection among competing adequate designs or explanatory hypotheses.

Preconditions: Candidates are being compared against the same complete evidence, requirements, and risk thresholds.

Expected benefit: Fewer unjustified state holders, boundaries, failure modes, and speculative commitments.

Common over-application: Treating parsimony as proof, equating fewer lines with fewer assumptions, or discarding required redundancy and safety mechanisms.

Known limitations: It cannot decide between candidates with different adequacy; rare high-impact risks may require early investigation; observed constraints can justify complex designs.

Primary sources:

- [Simplicity — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/simplicity/)
- [Occam's Razor — Laws of Software Engineering](https://lawsofsoftwareengineering.com/laws/occams-razor/)

## Principle of Least Power

Principle: Use the least expressive language or mechanism that can fully and clearly express the requirement.

Primary problem addressed: Unnecessary expressive power that increases possible behavior, side effects, analysis difficulty, and security surface.

Recommended action: Order candidate mechanisms from constrained data or declarations toward arbitrary code and choose the first that remains adequate and comprehensible.

Decision object: The expressive power of the language, representation, configuration, query, template, callback, script, or plugin mechanism used for a task.

Preconditions: The required behavior—including sequencing, error recovery, accessibility, and dynamic needs—can be stated accurately enough to test mechanism sufficiency.

Expected benefit: Better static analysis, validation, transformation, portability, predictability, and confinement.

Common over-application: Forcing complex algorithms into giant tables, regular expressions, or configuration languages that become poorly tooled programs.

Known limitations: Stateful interaction, rich composition, sequencing, or precise recovery can require a more expressive mechanism; minimum theoretical power is not the goal.

Primary sources:

- [The Rule of Least Power — W3C Technical Architecture Group](https://www.w3.org/2001/tag/doc/leastPower.html)
- [Principles of Design — Tim Berners-Lee](https://www.w3.org/DesignIssues/Principles.html)

## Separation of Concerns

Principle: Isolate distinct kinds of decisions so each can be understood, changed, and verified with minimal knowledge of the others.

Primary problem addressed: Entanglement of independently changing policy, effects, representations, or stakeholder concerns.

Recommended action: Trace a use case, group coherent decisions, create the cheapest boundary that yields meaningful independence, and recombine explicitly.

Decision object: The logical boundary between distinct concerns and the values or contracts crossing it.

Preconditions: The candidate concerns have different rules, vocabularies, owners, rates of change, test environments, or operational requirements.

Expected benefit: Reduced change amplification, clearer policy, focused verification, and replaceable details.

Common over-application: Layer proliferation, microscopic files, pass-through modules, or separate services without an independent deployment need.

Known limitations: Concerns that maintain one invariant and always change together are often clearer together; every stronger boundary adds integration cost.

Primary sources:

- [On the Role of Scientific Thought — E. W. Dijkstra](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)
- [Architectural Principles: Separation of Concerns — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#separation-of-concerns)

## Single Responsibility Principle

Principle: Gather elements that change for the same reason and separate elements that change for different stakeholder or business-function reasons.

Primary problem addressed: Modules coupled to multiple independent actors, policies, or sources of change.

Recommended action: Identify demonstrated change reasons and actors, group one cohesive responsibility and its invariants, and separate independently owned work at the smallest useful boundary.

Decision object: The cohesion and ownership boundary of a module.

Preconditions: Actual or well-supported change reasons and responsible actors can be identified; the split reduces coupling rather than merely shrinking files.

Expected benefit: Changes from one actor affect a smaller coherent area and are less likely to break unrelated responsibilities.

Common over-application: One-method-class explosion, interface-per-class ceremony, speculative actors, anemic models, or microservice-per-responsibility literalism.

Known limitations: A responsibility can include many operations; module size is contextual; splitting cohesive algorithms can increase navigation and reduce understanding.

Primary sources:

- [The Single Responsibility Principle — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
- [On the Criteria To Be Used in Decomposing Systems into Modules — David Parnas](https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf)

## Composition over Inheritance

Principle: Prefer assembling focused behavior through composition when reuse or variation does not require a stable subtype hierarchy.

Primary problem addressed: Fragile base-class coupling and subclass multiplication across independent axes of variation.

Recommended action: Identify real variation axes, represent each with the lightest useful function or collaborator, and assemble them explicitly near the boundary.

Decision object: The reuse and variation mechanism—composition, inheritance, or direct fixed code.

Preconditions: Behavior varies independently, the need is reuse or replaceability rather than genuine subtype semantics, and composition reduces combinatorial or lifecycle coupling.

Expected benefit: Independently replaceable behaviors, shallower coupling, and fewer subclasses for combinations.

Common over-application: Strategy interfaces, factories, containers, forwarding layers, and injected collaborators for behavior that never varies.

Known limitations: Framework-required inheritance, shallow stable subtypes, and closed hierarchies can be clearer; composition wiring can itself become costly.

Primary sources:

- [The Composition Over Inheritance Principle — Brandon Rhodes](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
- [Replace Inheritance with Delegation — Refactoring.Guru](https://refactoring.guru/replace-inheritance-with-delegation)

## Convention over Configuration

Principle: Make the ordinary case follow a shared, discoverable default so only meaningful exceptions require configuration.

Primary problem addressed: Repeated low-value configuration and naming or layout decisions that obscure intent and burden tooling.

Recommended action: Observe repeated choices, adopt the unsurprising ecosystem convention, validate it, provide a narrow explicit override, and remove redundant configuration.

Decision object: Which routine choices are inferred by convention and which exceptions remain explicit.

Preconditions: A dominant stable case exists, users and tooling can discover the convention, and exceptions are fewer and clearer than explicit configuration would be.

Expected benefit: Less configuration and glue, predictable discovery, easier onboarding, and stronger automation.

Common over-application: Undocumented magic, hidden business policy, overlapping implicit precedence, and conventions whose exceptions dominate.

Known limitations: Important domain policy should remain explicit; migration and versioning may be required; explicit code is clearer when commonality is weak.

Primary sources:

- [The Ruby on Rails Doctrine](https://rubyonrails.org/doctrine#convention-over-configuration)
- [Active Record Basics — Rails Guides](https://guides.rubyonrails.org/active_record_basics.html#convention-over-configuration-in-active-record)

## Unix Philosophy

Principle: Build focused components that do one coherent job and compose through stable, simple, general interfaces.

Primary problem addressed: Monolithic tools that absorb adjacent features and components whose outputs cannot be reused or replaced.

Recommended action: Define a cohesive purpose, accept and emit composable values or standard streams, separate data from diagnostics, and combine existing focused tools.

Decision object: Component scope and the design of its composition interface.

Preconditions: The work can be decomposed without losing needed transactions, error propagation, performance, or user-workflow cohesion.

Expected benefit: Replaceability, reuse, inspectability, incremental development, and leverage from existing tools.

Common over-application: Microscopic processes, ad hoc text formats, unobservable pipelines, excessive flags, or fragmentation with higher integration cost than benefit.

Known limitations: Cohesive in-process functions or a single application can provide better transaction and failure boundaries; not every interface should be text.

Primary sources:

- [UNIX Time-Sharing System Foreword — McIlroy, Pinson, and Tague](https://www.textbookoflinux.com/references/mcilroy1978.html)
- [The Art of Unix Programming — Basics of the Unix Philosophy](https://www.catb.org/esr/writings/taoup/html/ch01s06.html)

## Functional Core, Imperative Shell

Principle: Put deterministic domain decisions in a side-effect-free core and keep I/O, external mutation, time, randomness, and operational coordination in a thin shell.

Primary problem addressed: Business decisions entangled with infrastructure effects, producing complex tests and duplicated or inaccessible policy.

Recommended action: Make external context explicit as values, return domain outcomes or simple intended actions, and keep effect execution and failure coordination at the boundary.

Decision object: The placement of deterministic decisions versus external effects in a workflow.

Preconditions: A material portion of the workflow can be expressed as value-to-value logic without breaking transaction, streaming, timing, or concurrency semantics.

Expected benefit: Direct input/output tests, explicit dependencies, reusable policy, and a smaller integration surface.

Common over-application: Elaborate command algebras, purity wrappers over global mutation, enormous action graphs, or transaction loss for aesthetic separation.

Known limitations: Some decisions are inherently effectful or concurrent; streams may not fit in memory; the extracted core must be large enough to repay the boundary.

Primary sources:

- [Boundaries — Gary Bernhardt](https://www.destroyallsoftware.com/talks/boundaries)
- [Simplify Your Code: Functional Core, Imperative Shell — Google Testing Blog](https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html)

## Negative Code

Principle: Treat safe removal of owned code and supporting machinery, while preserving or improving the required contract, as engineering progress.

Primary problem addressed: Code volume and mechanisms retained as inventory despite their continuing maintenance, security, and operational costs.

Recommended action: Define the supported contract, establish evidence, replace or remove a coherent slice, delete its obsolete perimeter, and verify outcomes rather than line count.

Decision object: Whether a change can deliver equal or better supported capability with less owned implementation and machinery.

Preconditions: Observable behavior and compatibility commitments are known, and there is proportionate evidence that removal or replacement preserves them.

Expected benefit: Fewer concepts, states, dependencies, failure paths, and future change obligations.

Common over-application: Code golf, deleting safeguards or tests without proof, replacing local code with a heavier dependency, or optimizing a negative line count.

Known limitations: Some larger or more explicit implementations are safer and clearer; dynamic and external consumers complicate proof; generated volume is not equivalent to maintained knowledge.

Primary sources:

- [-2000 Lines of Code — Andy Hertzfeld, Folklore.org](https://www.folklore.org/Negative_2000_Lines_Of_Code.html)
- [Dispensables — Refactoring.Guru](https://refactoring.guru/refactoring/smells/dispensables)

## Dead Code Elimination

Principle: Remove behavior and artifacts that cannot affect any supported observable outcome.

Primary problem addressed: Unreachable or unused code, flags, dependencies, configuration, tests, and operational artifacts that create false choices and maintenance surface.

Recommended action: Define the liveness boundary, search static and dynamic entry points, establish non-use or unobservability, remove the coherent slice, and verify broadly.

Decision object: The liveness of a code or artifact candidate within the supported system and compatibility boundary.

Preconditions: Supported entry points, dynamic registration, external contracts, rollout and rollback needs, and operational paths are known or adequately investigated.

Expected benefit: Smaller attack, analysis, dependency, testing, and maintenance surfaces without changing supported behavior.

Common over-application: Equating no static references with deadness, deleting disaster-recovery or external API paths, or removing only code while leaving dependent artifacts.

Known limitations: Reflection, plugins, scripts, external consumers, and rare operations can hide liveness; staged deprecation or instrumentation may be required.

Primary sources:

- [LLVM's Analysis and Transform Passes — Dead Code Elimination](https://llvm.org/docs/Passes.html#dce-dead-code-elimination)
- [Dead Code — Refactoring.Guru](https://refactoring.guru/smells/dead-code)

## Refactoring Toward Primitives

Principle: Replace custom machinery with the smallest trustworthy capability already provided by the language, standard library, repository, framework, database, browser, operating system, protocol, or platform.

Primary problem addressed: Bespoke implementations that duplicate mature capabilities and inherit avoidable design, testing, security, compatibility, and lifecycle work.

Recommended action: Characterize the current contract, search existing primitives in increasing ownership order, compare exact semantics and costs, replace, and delete obsolete glue.

Decision object: Whether an existing primitive can assume a custom implementation's required contract at lower total lifecycle cost.

Preconditions: Current behavior and edge cases are known; candidate semantics, support baseline, dependency weight, licensing, and migration cost can be evaluated.

Expected benefit: Less owned code, fewer edge cases and dependencies, and leverage from maintained ecosystem capabilities.

Common over-application: Contract-blind substitution, obscure framework magic, platform lock-in, unnecessary wrappers, or importing a large package for a small clear function.

Known limitations: Similar API names can hide semantic differences; a local implementation may be cheaper; domain policy or a real volatility boundary can justify a wrapper.

Primary sources:

- [Don't Reinvent the Wheel: Towards Automatic Replacement of Custom Implementations with APIs](https://arxiv.org/abs/2208.07624)
- [From Custom Logic to APIs: API Replacement Refactorings](https://arxiv.org/abs/2606.06912)

## Dependency Inversion Principle

Principle: Make stable policy own and depend on a narrow domain-shaped contract, with volatile details implementing that contract from the outside.

Primary problem addressed: High-level policy coupled directly to low-level vendor, framework, storage, or transport details.

Recommended action: Identify a demonstrated volatile boundary, define only the capability policy needs, implement an outer adapter, and compose it explicitly at the application edge.

Decision object: The source-dependency direction and ownership of the contract between policy and a detail.

Preconditions: A real policy/detail distinction and meaningful volatility, variation, test-isolation, security, or deployment boundary exist.

Expected benefit: Stable policy outlives detail changes, vendor types remain outside, and important policy can be tested through a small contract.

Common over-application: Interface-per-class, mirrored repositories, factory/container stacks, mock-driven contracts, and hypothetical provider portability.

Known limitations: Injection alone is not inversion; direct code is simpler for stable fixed details; the contract must preserve relevant latency, failure, and transaction semantics.

Primary sources:

- [DIP in the Wild — Brett Schuchert](https://martinfowler.com/articles/dipInTheWild.html)
- [Architectural Principles: Dependency Inversion — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#dependency-inversion)

## Data-Driven Design

Principle: Represent regular case variation as explicit data operated on by one small lookup, interpreter, or algorithm.

Primary problem addressed: Repeated conditionals or implementations that scatter a regular decision space through control flow.

Recommended action: Compare cases, confirm one shared algorithm and meaning, encode varying dimensions in the simplest typed table or schema, validate it, and keep true exceptions in code.

Decision object: Whether variation belongs in control flow or in a data representation, and the shape of that representation.

Preconditions: Cases share one algorithm and domain meaning, vary along inspectable dimensions, and can be validated without hiding distinct algorithms in callbacks.

Expected benefit: Visible decision space, one authority for cases, simpler extension, and tooling that can validate or derive types and documentation.

Common over-application: Universal rules engines, callback-filled configuration, unsafe string keys, remotely configuring developer-owned constants, or forcing exceptional algorithms into tables.

Known limitations: Irregular or state-specific algorithms are clearer as code; remote data adds lifecycle and failure modes; an interpreter can become a second programming language.

Primary sources:

- [Data-Driven Programming — The Art of Unix Programming](https://www.catb.org/esr/writings/taoup/html/ch09s01.html)
- [Table-Driven Design — Bill Wake](https://billwake.com/pattern-patter-table-driven-design/)

## Make Illegal States Unrepresentable

Principle: Choose types and structures that admit valid domain values while excluding invalid combinations or preventing them from escaping trusted construction.

Primary problem addressed: Broad representations whose many impossible or contradictory states force repeated defensive branches in every consumer.

Recommended action: Enumerate invalid combinations, select the least elaborate precise representation, control construction, and remove checks that the representation genuinely makes unnecessary.

Decision object: The domain representation and which invariants it enforces structurally or at construction.

Preconditions: The invariants are stable, valuable across consumers, and enforceable in the type, collection, constructor, or database boundary being chosen.

Expected benefit: Smaller state space, centralized invariant proof, exhaustive handling, and fewer downstream checks and synchronization bugs.

Common over-application: Wrapper-type proliferation, unchecked casts, advanced type tricks, or treating mutable external facts and partial editing states as permanently proven.

Known limitations: Authorization, concurrent uniqueness, inventory, time, and remote facts need use-time checks; some advanced encodings cost more than the branches they remove.

Primary sources:

- [Make Illegal States Unrepresentable — Functional Software Architecture](https://functional-architecture.org/make_illegal_states_unrepresentable/)
- [Haskell Mini-Patterns — Make Illegal States Unrepresentable](https://kowainik.github.io/posts/haskell-mini-patterns.html#make-illegal-states-unrepresentable)

## Parse, Don't Validate

Principle: Convert weak or untrusted input into a more precise value that preserves the facts established during checking, or return a useful error.

Primary problem addressed: Validation that discards knowledge and leaves downstream code holding the same broad type, causing casts, rechecks, and informal assumptions.

Recommended action: Design the trusted internal type, parse raw data at the earliest useful boundary, propagate the precise value inward, and retain checks for mutable contextual facts.

Decision object: The boundary conversion from a raw representation to a trusted domain representation and error form.

Preconditions: A stronger internal representation exists and the relevant structural facts can be established before domain effects rely on them.

Expected benefit: One-time boundary checks, evidence carried in values, safer function signatures, and removal of redundant impossible-case handling.

Common over-application: Parser frameworks for tiny objects, unchecked casts after nominal parsing, premature normalization, or treating authorization and concurrent state as parse-time facts.

Known limitations: Mutable facts require later checks; partial workflows can require staged parsing; resource limits may need enforcement before full parsing.

Primary sources:

- [Parse, don't validate — Alexis King](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Type Safety Back and Forth — Matt Parsons](https://www.parsonsmatt.org/2017/10/11/type_safety_back_and_forth.html)

## Tell, Don't Ask

Principle: Ask the component that owns state and an invariant to perform a meaningful domain operation instead of rebuilding the decision through external query-and-mutate code.

Primary problem addressed: Callers that expose, duplicate, and inconsistently enforce another component's invariant.

Recommended action: Identify repeated query-decide-mutate sequences, locate the invariant owner, introduce the smallest meaningful command, and expose only the outcome callers need.

Decision object: The ownership and placement of a state-dependent domain decision and transition.

Preconditions: One component coherently owns the state and invariant, and moving the operation inward does not absorb unrelated workflow, persistence, or presentation work.

Expected benefit: Encapsulated invariants, fewer bypass paths and duplicated policies, and a smaller mutation surface.

Common over-application: Banning queries, adding generic setters or pass-through commands, hiding needed errors, or creating god objects.

Known limitations: Reporting, presentation, immutable calculations, diagnostics, and higher-level orchestration legitimately query data; layering can outweigh co-location.

Primary sources:

- [Tell Don't Ask — Martin Fowler](https://martinfowler.com/bliki/TellDontAsk.html)
- [Tell, Don't Ask — DevIQ](https://deviq.com/principles/tell-dont-ask/)

## Law of Demeter — Principle of Least Knowledge

Principle: Collaborate through immediate, meaningful interfaces rather than depend on the internal object graph behind a collaborator.

Primary problem addressed: Structural coupling in which distant callers know and navigate unstable ownership chains.

Recommended action: Identify graph navigation that exposes structure, locate the nearest owner of the needed capability, add a cohesive operation or pass the needed value directly, and avoid middle-men.

Decision object: The set and depth of structural relationships a unit knows about through its collaborators.

Preconditions: Navigation reflects dependence on nested ownership rather than a transparent immutable value pipeline, and a nearer stable boundary can express the need honestly.

Expected benefit: Fewer distant changes when internal object structure changes, narrower collaboration surfaces, and protected mutable internals.

Common over-application: Counting dots, wrapping fluent or collection pipelines, forests of pass-through methods, or hiding remote cost behind innocent-looking operations.

Known limitations: Direct access to plain immutable values can be clearer; replacement methods can create middle-men; interfaces must preserve latency and failure visibility.

Primary sources:

- [Law of Demeter: Principle of Least Knowledge — Northeastern University](https://www.ccs.neu.edu/home/lieber/LoD.html)
- [The Paperboy, the Wallet, and the Law of Demeter](https://www.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/demeter.pdf)

## Boy Scout Rule

Principle: While changing code for a real task, make a small, safe, adjacent improvement to the area already being understood.

Primary problem addressed: Local quality drift that accumulates because large cleanup projects are deferred and touched code is left no clearer.

Recommended action: Select a bounded improvement in the touched execution path, keep behavior-preserving cleanup distinguishable from requested behavior, and verify it proportionately.

Decision object: The scope, timing, and safety of incidental local cleanup during a task.

Preconditions: The area is already in task scope, the improvement is clear and reviewable, and it does not require unrelated product or architectural judgment.

Expected benefit: Continuous low-risk stewardship, clearer touched code, and gradual reduction of local friction without separate large rewrites.

Common over-application: Drive-by refactoring, repository-wide formatting, dependency upgrades, public API redesign, or disguising behavior changes as cleanup.

Known limitations: Incidents, fragile untested code, regulated systems, and broad cleanup needs can require postponement, characterization, or separate work.

Primary sources:

- [The Boy Scout Rule — Laws of Software Engineering](https://lawsofsoftwareengineering.com/laws/boy-scout-rule/)
- [The Boy Scout Rule — 97 Things Every Programmer Should Know](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)
