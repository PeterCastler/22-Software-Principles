# Make Illegal States Unrepresentable

## Definition

Make Illegal States Unrepresentable is the data-modeling principle that a program's types and structures should admit valid domain values while excluding invalid combinations. If an invalid state cannot be constructed—or cannot escape a trusted constructor—downstream code does not need defensive branches for it.

“State” includes immutable values, not only mutable state machines. A malformed configuration, empty collection where an element is required, contradictory set of booleans, or unsynchronized duplicate value is an illegal state.

## Why representation controls complexity

Three independent booleans represent eight combinations even when only three are meaningful. Optional fields multiply the state space. Every consumer must then ask which combinations are valid and what to do with the rest.

A precise representation moves that reasoning to construction. Exhaustive pattern matching guides every consumer and future change.

## Core techniques

- replace combinations of booleans with explicit variants;
- attach data only to the variant where it is valid;
- use non-empty collections when emptiness is forbidden;
- use sets or maps when duplicates are illegal;
- use opaque types and smart constructors for constrained values;
- distinguish identifiers with domain-specific types;
- derive dependent values instead of storing synchronized copies;
- separate raw transport shapes from trusted domain types;
- use database constraints for invariants shared by concurrent writers.

## Worked example

An imprecise request representation:

```ts
type Request = {
  loading: boolean;
  failed: boolean;
  data?: string;
  error?: Error;
};
```

It permits “loading and failed,” “successful without data,” and “idle with an error.” A discriminated union admits only defined states:

```ts
type RequestState =
  | { kind: "idle" }
  | { kind: "loading" }
  | { kind: "loaded"; data: string }
  | { kind: "failed"; error: Error };

function render(state: RequestState): string {
  switch (state.kind) {
    case "idle": return "Ready";
    case "loading": return "Loading…";
    case "loaded": return state.data;
    case "failed": return state.error.message;
  }
}
```

There is no branch for contradictory combinations because no such value exists.

## Smart constructors

Some invariants cannot be encoded structurally, such as an integer in a range. Hide construction and expose a function that returns either a trusted type or an error:

```ts
type Port = number & { readonly __brand: "Port" };

function parsePort(value: number): Port | Error {
  return Number.isInteger(value) && value >= 1 && value <= 65535
    ? value as Port
    : new Error("Port must be an integer from 1 to 65535");
}
```

Branding alone is not validation; safety depends on restricting unchecked casts and routing creation through the constructor.

## Application method

1. Enumerate representable combinations in the current model.
2. Mark which are invalid, contradictory, or require fields to co-occur.
3. Determine which invariants are stable and valuable across many consumers.
4. Choose the least elaborate representation that encodes them.
5. Parse or construct the trusted value at the boundary.
6. Update internal functions to require the precise type.
7. Remove redundant checks made impossible by the model.
8. Keep external and concurrent-state validation where still necessary.

## Derived versus stored state

Duplicating a value creates a trivial illegal state: the copies disagree. Prefer deriving totals, counts, status flags, or display values from one authority. If denormalization is required for performance, encapsulate synchronization and enforce it transactionally where possible.

## Limits

Not every invariant belongs in a static type:

- uniqueness across concurrent database writers;
- current authorization;
- inventory or balance at transaction time;
- relationships with remote systems;
- time-dependent business rules;
- incomplete form input while a user is editing.

Represent these honestly at the correct boundary. UI editing state may remain partial and convert to a domain command only on submission.

Advanced type encodings can cost more understanding than the checks they remove. Encode high-value stable invariants, not every theoretical property.

## Risks and misapplications

- creating many wrapper types with no meaningful invariant;
- using casts that bypass smart constructors;
- hiding validation errors behind exceptions when callers need them;
- modeling mutable external facts as permanently proven;
- forcing incomplete UI or migration data into final-domain types too early;
- adding sophisticated type machinery unfamiliar to maintainers for one local check.

## Review checklist

- Which invalid combinations can the current model represent?
- Can variants attach only the fields they need?
- Is a collection type enforcing uniqueness or non-emptiness?
- Can duplicated state be derived?
- Where is construction controlled?
- Which invariants depend on external mutable state?
- Are casts or deserializers bypassing the model?
- Does the type machinery simplify enough consumers to justify itself?

## Guidance for agentic coding

An agent should prefer precise ordinary types, discriminated unions, maps, sets, and narrow constructors before repeated runtime checks. It should parse raw input at boundaries and remove checks only when the representation truly proves them impossible. It must not over-model transient UI state or external mutable facts, and it should avoid advanced type tricks whose cognitive cost exceeds their benefit.

## Sources

- [Make Illegal States Unrepresentable — Functional Software Architecture](https://functional-architecture.org/make_illegal_states_unrepresentable/)
- [Haskell Mini-Patterns — Make Illegal States Unrepresentable](https://kowainik.github.io/posts/haskell-mini-patterns.html#make-illegal-states-unrepresentable)
