# KISS — Keep It Simple, Stupid

## Definition

KISS is the design principle that a system should be no more complicated than necessary to satisfy its real requirements. In software, it means choosing the clearest complete solution with the fewest justified concepts, states, dependencies, execution paths, and operational obligations.

“Simple” does not mean short, primitive, or hastily written. It means that the design exposes its essential behavior directly and does not add accidental complexity. A ten-line expression that relies on obscure coercions can be less simple than a readable twenty-line function. Likewise, one deployable application can be simpler than five services even if its source file is longer.

The practical unit of simplicity is the whole lifecycle: implementation, testing, deployment, operation, debugging, change, and eventual deletion.

## The problem KISS addresses

Codebases become bloated when developers add machinery that is not demanded by the problem:

- interfaces with one implementation and no meaningful boundary;
- factories that only call constructors;
- wrappers that merely rename an API;
- configuration for values that never vary;
- plugin systems without plugins;
- generic engines for a single concrete rule;
- layers that forward requests without adding policy;
- distributed components without independent scaling, security, or ownership needs.

Every added concept imposes a tax. A maintainer must learn its name, contract, interactions, failure modes, and reason for existence. Tests must cover it, tooling must understand it, and future changes must preserve it. KISS asks each concept to earn that continuing cost.

## What KISS optimizes

KISS minimizes cognitive and operational load while preserving required quality. Useful measures include:

- number of concepts a maintainer must hold in mind;
- number of possible states and branches;
- number of dependencies and integration boundaries;
- distance between a requirement and the code implementing it;
- amount of indirection needed to trace execution;
- number of failure and recovery paths;
- effort required to make and verify a likely change.

Line count can be a clue, but it is not the objective. Generated code may be large and cheap to maintain; a tiny metaprogram may be difficult to reason about.

## Application method

1. **State the current behavior and constraints.** Include correctness, security, performance, compatibility, accessibility, and operational requirements. Anything omitted here may be falsely labeled “unnecessary.”
2. **Start with the platform.** Check the language, standard library, existing project dependencies, framework, database, browser, and operating system before designing custom machinery.
3. **Model the data directly.** A precise representation can eliminate validation branches and synchronization logic.
4. **Prefer explicit control flow.** Direct conditionals and loops are often clearer than callbacks, reflection, inheritance, or configuration-driven dispatch.
5. **Add one mechanism at a time.** Each abstraction should solve an observed problem and remove more complexity than it introduces.
6. **Keep scope local.** A private function is preferable to a cross-project framework when only one module needs the behavior.
7. **Perform a deletion pass.** After correctness is established, remove unused helpers, speculative options, redundant comments, and obsolete compatibility paths.

## Worked example

Suppose the only current pricing rule is a ten-percent discount for orders of at least 100 units.

An over-designed version introduces a `DiscountStrategy` interface, a `ThresholdDiscount` class, a registry, a factory, and configuration identifying the selected strategy. That structure may be appropriate after several independently changing discount policies exist, but today it adds five concepts to express one conditional.

A KISS implementation is direct:

```ts
export function discountedTotal(total: number): number {
  return total >= 100 ? total * 0.9 : total;
}
```

This is not a promise never to refactor. If a second real policy arrives, its concrete differences provide evidence for the right abstraction. Delaying the framework preserves flexibility because there is less structure to undo.

## When more structure is simpler

KISS does not require everything to live in one function or file. Separation is simpler when responsibilities change independently. A named type is simpler when raw values are easily confused. An interface is simpler when it protects stable policy from a volatile vendor. Redundancy is simpler when the alternative is a wrong abstraction. A queue is simpler when asynchronous delivery is a current reliability requirement.

The comparison must include the problem being solved. Essential complexity cannot be deleted; it can only be represented honestly and placed where it is easiest to manage.

## Misapplications

- **Code golf:** reducing characters while increasing cognitive work.
- **Happy-path minimalism:** omitting required error handling, security, or recovery.
- **One-file minimalism:** avoiding useful modular boundaries merely to reduce files.
- **Hidden complexity:** relying on global state, magic conventions, implicit coercion, or undocumented framework behavior.
- **Premature consolidation:** merging distinct domain concepts because their implementations currently look similar.
- **Dependency blindness:** replacing local code with a library without counting supply-chain, runtime, and upgrade costs.

## Review checklist

- Can a maintainer explain the execution path without opening many unrelated files?
- Does every abstraction have more than a hypothetical consumer or a clear boundary role?
- Does each dependency remove more owned complexity than it adds?
- Are configuration options backed by current variation?
- Are failure states explicit rather than hidden?
- Could a standard primitive or direct data structure replace custom machinery?
- Is any compact code relying on cleverness?
- After the change passes verification, what can be deleted?

## Guidance for agentic coding

An implementation agent applying KISS should build the smallest complete change, preserve existing conventions, and resist unsolicited architecture. It should not add wrappers, interfaces, factories, fallback modes, compatibility layers, or configuration unless the task or existing design requires them. It should favor direct functions and data, then make a final pass asking which newly added concepts can be removed without harming correctness, readability, testing, security, or operability.

## Sources

- [KISS Software Design Principle — Baeldung](https://www.baeldung.com/cs/kiss-software-design-principle)
- [Keep it simple — UK Home Office Engineering Guidance](https://engineering.homeoffice.gov.uk/principles/keep-it-simple/)
