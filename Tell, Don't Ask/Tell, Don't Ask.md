# Tell, Don't Ask

## Definition

Tell, Don't Ask is an object and module design guideline: instead of retrieving an object's internal state, making a decision elsewhere, and then mutating the object, ask the object that owns the state and invariant to perform a meaningful operation.

The goal is not to ban queries or getters. It is to keep behavior with the information and rules required to perform it, preserving encapsulation and preventing callers from rebuilding the same policy.

“Tell” means issuing a domain-level command such as `withdraw`, `reserve`, `approve`, or `expire`. It does not mean replacing every query with a vague imperative method.

## The problem with ask-driven behavior

Ask-driven client code often follows this pattern:

1. read several fields from another object;
2. decide whether an operation is allowed;
3. calculate a state transition;
4. write fields back;
5. repeat the same logic in another caller.

The object's public surface exposes implementation details, and its invariant exists only by convention. A new field or rule requires changes in every caller. Different callers can make inconsistent decisions.

## Application method

1. Find code that queries state mainly to decide what command to issue next.
2. Identify which object or module owns the relevant invariant.
3. Name the domain operation the caller actually wants.
4. Move the decision and state transition behind that operation.
5. Reduce public setters and field exposure that allow bypassing the rule.
6. Return only the outcome the caller needs to continue orchestration.
7. Keep unrelated presentation, persistence, and workflow concerns outside the operation.

The owner may be a class, module, closure, or pure function operating on a domain value. The guideline does not require object-oriented syntax.

## Worked example

Ask-driven withdrawal:

```ts
class Account {
  constructor(public balance: number) {}
}

function withdraw(account: Account, amount: number): void {
  if (account.balance < amount) throw new Error("Insufficient funds");
  account.balance -= amount;
}
```

The caller can also assign any balance directly. The account should own its transition:

```ts
class Account {
  constructor(private balance: number) {}

  withdraw(amount: number): void {
    if (amount <= 0) throw new Error("Amount must be positive");
    if (this.balance < amount) throw new Error("Insufficient funds");
    this.balance -= amount;
  }

  currentBalance(): number {
    return this.balance;
  }
}
```

The balance query remains because reporting it is legitimate. What moved was the policy and mutation that must remain consistent.

## Commands and outcomes

A command may return:

- nothing when success is sufficient;
- the updated value;
- a domain event;
- a result indicating expected rejection;
- information needed for the next workflow step.

Avoid exposing the entire object merely because one outcome is needed. Also avoid hiding errors so thoroughly that callers cannot coordinate recovery.

## Behavior and data ownership

Place behavior with the data when they share one invariant and change together. A pricing operation belongs near pricing rules; a state transition belongs near the state model. However, an object should not absorb behavior merely because it can access the data. Rendering, persistence, cross-aggregate workflow, and external integration may belong elsewhere.

The correct owner is the smallest component that has all necessary knowledge without reaching through other components' internals.

## Queries are legitimate

Queries are appropriate for:

- presentation and reporting;
- diagnostics and observability;
- composing calculations from immutable values;
- searching and filtering collections;
- interoperability and serialization;
- decisions owned by a higher-level workflow.

The warning sign is not “a getter exists.” It is that a caller repeatedly asks for internal state to enforce an invariant the callee should own.

## Common mistakes

- creating command methods that simply expose generic setters;
- moving unrelated workflow logic into a data object;
- forbidding all queries and producing awkward APIs;
- returning mutable internal collections;
- adding pass-through methods for every nested property;
- hiding failure information callers need;
- creating “god objects” that own every operation involving their data;
- duplicating the same decision in several commands.

## Review checklist

- Is the caller querying state only to decide what to tell the same object?
- Which component owns the invariant?
- Can the desired action be named as a domain command?
- Can public mutation bypass the rule?
- What minimum outcome does the caller need?
- Does moving behavior create an overly broad object?
- Are remaining queries legitimate presentation or orchestration needs?
- Is internal mutable state still exposed indirectly?

## Guidance for agentic coding

An agent should look for repeated query-decide-mutate sequences and move coherent invariant enforcement to the owning component. It should introduce meaningful domain operations, not generic setters or pass-through methods. It must preserve legitimate queries and avoid expanding the owner into unrelated presentation, persistence, or workflow responsibilities.

## Sources

- [Tell Don't Ask — Martin Fowler](https://martinfowler.com/bliki/TellDontAsk.html)
- [Tell, Don't Ask — DevIQ](https://deviq.com/principles/tell-dont-ask/)

