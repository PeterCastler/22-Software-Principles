# Refactoring Toward Primitives

## Definition

Refactoring Toward Primitives replaces custom machinery with the smallest trustworthy capability already supplied by the language, standard library, framework, database, browser, operating system, protocol, or managed platform.

“Primitive” here means a foundational existing capability relative to the project, not necessarily a low-level CPU or language primitive. A database constraint, native HTML control, standard collection method, or framework router can each be a primitive when it removes code the project would otherwise own.

## Why primitives reduce bloat

Custom implementations require design, testing, documentation, optimization, security review, compatibility work, and edge-case handling. Mature primitives often bundle those obligations with broad ecosystem knowledge and tooling.

Common replacements include:

- standard collection operations for handwritten loops;
- native date, URL, path, and encoding APIs for string manipulation;
- HTML controls for scripted imitations;
- CSS layout and media queries for JavaScript positioning;
- database uniqueness, foreign keys, and transactions for application-only checks;
- framework routing, serialization, validation, and migrations for custom dispatch;
- operating-system scheduling and service management for bespoke daemons;
- standard protocols and formats for proprietary envelopes;
- existing repository utilities for duplicate local helpers.

## Search order

Before creating machinery, search in this order:

1. language syntax and type system;
2. standard library;
3. existing project utility or dependency;
4. current framework and platform;
5. database, browser, or operating-system capability;
6. a new dependency;
7. custom implementation.

This order is a heuristic. A clear ten-line local function can be better than a large new package.

## Replacement method

1. Characterize the current contract, including edge cases, errors, ordering, performance, and compatibility.
2. Find candidate primitives and read their exact semantics.
3. Compare behavior rather than method names.
4. Evaluate runtime support, dependency weight, licensing, security, and migration cost.
5. Add characterization tests where existing behavior is uncertain.
6. Replace the custom path incrementally if risk is high.
7. Delete the implementation, its internal-only tests, and obsolete glue.
8. Retain tests for the application's required contract.

## Worked example

Custom grouping:

```ts
function groupByStatus<T extends { status: string }>(items: T[]) {
  const result: Record<string, T[]> = {};
  for (const item of items) {
    if (!result[item.status]) result[item.status] = [];
    result[item.status].push(item);
  }
  return result;
}
```

When the project's runtime baseline supports it:

```ts
const grouped = Object.groupBy(items, item => item.status);
```

The change must account for semantics: `Object.groupBy` returns a null-prototype object and has runtime-support implications. Primitive-first does not mean contract-blind substitution.

## When a wrapper remains useful

Do not retain a wrapper merely to rename a standard call. A wrapper is justified when it:

- owns domain policy, defaults, or validation;
- adapts an awkward external API to domain values;
- isolates a genuinely volatile dependency;
- centralizes security or observability required by every call;
- provides a stable compatibility layer with multiple consumers.

The wrapper should expose less and more stable behavior than the underlying primitive, not mirror it method for method.

## Dependency economics

A third-party library may replace source lines while adding:

- supply-chain and licensing risk;
- bundle size and startup cost;
- update and vulnerability work;
- transitive dependencies;
- platform incompatibility;
- a new API maintainers must learn.

Prefer the standard library and existing dependencies. Add a new package when the problem is subtle, the implementation would be substantial, and the package is mature and appropriately scoped.

## Risks and misapplications

- semantic mismatch hidden by similar names;
- browser or runtime support gaps;
- platform lock-in that exceeds removed complexity;
- using a regular expression for a grammar needing a parser;
- replacing readable domain code with obscure framework magic;
- wrapping every primitive “in case we switch later”;
- relying on platform behavior without tests for the application's contract.

## Review checklist

- Does the platform already solve this problem?
- What exact semantics does the current code promise?
- Does the primitive match errors, ordering, and edge cases?
- Is runtime support adequate?
- Does a new dependency remove enough complexity to justify its lifecycle cost?
- Does a wrapper own policy or merely rename an API?
- Which custom tests and glue become obsolete?
- Are application-level contract tests preserved?

## Guidance for agentic coding

An agent should search the existing platform and repository before writing helpers or dependencies. It should verify exact semantics and compatibility, not assume a similarly named API is equivalent. It should prefer direct primitive use and add a wrapper only for domain policy or a real volatility boundary. Successful replacement should end with deletion of redundant implementation and glue.

## Sources

- [Don't Reinvent the Wheel: Automatic Replacement of Custom Implementations with APIs](https://arxiv.org/abs/2208.07624)
- [From Custom Logic to APIs: API Replacement Refactorings](https://arxiv.org/abs/2606.06912)
