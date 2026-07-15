# YAGNI — You Aren't Gonna Need It

## Definition

YAGNI is the Extreme Programming rule that a capability should not be built until a current requirement needs it. It applies to visible features and to invisible extensibility: options, plugin points, abstractions, generalized APIs, compatibility paths, infrastructure, and configuration created for presumed future use.

YAGNI is not a claim that the future will never arrive. It is a strategy for delaying irreversible knowledge commitments until better information exists. The question is not “Could this ever be useful?” but “Does its value now justify its cost now?”

## Why speculative capability is expensive

Martin Fowler separates several costs that speculative work creates:

- **Build cost:** analysis, design, implementation, review, tests, documentation, migration, and deployment.
- **Delay cost:** present value ships later because effort went to a future possibility.
- **Carry cost:** every intervening change must understand, preserve, test, and operate the extra machinery.
- **Repair cost:** when the need arrives, the early guess may be wrong and must be reshaped or removed.

There is also an opportunity cost: the team forgoes learning that would have come from shipping and observing the current feature. Even when the prediction is correct, requirements, scale, vendors, and user behavior often change the correct implementation.

## What counts as speculative

Typical YAGNI candidates include:

- an interface designed solely because a second implementation might appear;
- support for output formats no current caller requests;
- generic sorting, filtering, or plugin systems around one fixed operation;
- feature flags without an active rollout plan and removal date;
- multi-tenant architecture for a single-tenant product with no contracted expansion;
- fallbacks for platforms the project does not support;
- database columns and API fields reserved “for later”;
- configuration for constants that have no known variation.

The presence of a future roadmap item is not always enough. If it is not part of the current delivery commitment, building it early must beat the costs of delay and inaccurate design.

## Application method

1. **Name the present consumer.** Every new capability should map to a current acceptance criterion, caller, migration, risk, or operational need.
2. **Separate reversible preparation from implementation.** A neutral name or clean module boundary may cost almost nothing; a generalized framework does not.
3. **Imagine the later refactor concretely.** If adding the capability later is local and mechanical, postpone it.
4. **Preserve malleability.** Keep code tested, cohesive, and readable so future change remains affordable.
5. **Record, do not implement, ideas.** Put plausible future work in an issue or decision note instead of dormant code.
6. **Remove presumptive remnants.** Delete unused flags, parameters, interfaces, and fields when no current requirement owns them.

## Worked example

A service currently exports JSON. A speculative implementation defines:

```ts
type Format = "json" | "xml" | "csv";
interface Serializer { serialize(value: unknown): string }
class ExportRegistry { /* registration, lookup, and error handling */ }
```

Only a JSON serializer exists. The framework must now define format discovery, unsupported-format behavior, registration lifecycle, and test doubles without any concrete XML or CSV requirements.

The YAGNI implementation is:

```ts
export const exportJson = (value: unknown): string => JSON.stringify(value);
```

When CSV is actually requested, the team will know its delimiter, quoting, encoding, streaming, schema, and error requirements. Those facts determine whether two functions, a map, or a serializer abstraction is appropriate.

## What YAGNI does not prohibit

YAGNI does not reject work that creates present value by keeping software safe and changeable:

- refactoring code that is already difficult to modify;
- tests that protect current behavior;
- security controls for current threat models;
- observability needed to operate the present system;
- backups, migrations, and rollback required for the current deployment;
- a simple boundary that isolates an existing volatile dependency;
- standards compliance and accessibility required now.

Fowler's crucial qualification is that YAGNI needs a malleable codebase. Neglecting design and tests makes deferred change expensive and turns YAGNI into recklessness.

## Exceptions and judgment

Some decisions have long lead times or extreme reversal costs: public protocols, persistent data formats, cryptographic choices, regulated audit records, physical hardware, and contractual compatibility. Planning for them can be a current risk-control requirement even before full use. The correct response is usually the smallest preparation that keeps the decision safe, not implementation of every predicted feature.

## Common misapplications

- using YAGNI to dismiss known nonfunctional requirements;
- shipping brittle code because cleanup is labeled “future work”;
- refusing a cheap neutral choice that prevents a costly lock-in;
- leaving speculative code in place because it has already been written;
- confusing “likely soon” with evidence while ignoring delivery cost;
- applying YAGNI to documentation or tests needed by current maintainers.

## Review checklist

- Which current requirement or caller uses this capability?
- What complexity will every intervening change carry?
- What will be learned by waiting?
- How hard is the real later refactor?
- Can the future idea be recorded instead of implemented?
- Is preparation needed because reversal is genuinely costly?
- Does the change add options, fields, flags, or interfaces with no active consumer?
- Is the codebase sufficiently tested and cohesive to change later?

## Guidance for agentic coding

An agent should implement only requested behavior and the engineering necessary to make that behavior correct and maintainable. It should not infer authorization for future formats, providers, platforms, modes, or extension systems. When it notices a plausible future need, it may mention it in the handoff, but it should not encode the possibility unless doing so has negligible complexity or is required by an existing contract.

## Sources

- [Yagni — Martin Fowler](https://martinfowler.com/bliki/Yagni.html)
- [Is Design Dead? — Martin Fowler](https://martinfowler.com/articles/designDead.html)
