# Functional Core, Imperative Shell

## Definition

Functional Core, Imperative Shell structures a program so that domain decisions and transformations live in deterministic, side-effect-free functions, while a thin outer shell performs I/O, reads time and randomness, mutates external state, and coordinates failures.

The core accepts values and returns values. The shell acquires inputs, calls the core, and executes the resulting actions. This is an architectural tendency rather than a demand for a purely functional language.

## Why mixed code becomes complex

When a function simultaneously queries a database, reads the clock, applies business rules, and sends email, every test must control several external systems. Business branches become entangled with network failures and mutable state. Reusing the rule requires reusing the effects.

Moving decisions into a pure core makes dependencies explicit in arguments. Tests become ordinary input/output examples. The shell still handles retries, transactions, and operational concerns, but it contains little domain policy.

## Application method

1. Trace an effectful workflow and identify the decision hidden inside it.
2. Represent external context—time, configuration, permissions, random choices—as explicit input values.
3. Make the core return a result or a simple description of intended actions.
4. Keep database, filesystem, network, and UI operations in the shell.
5. Test the core with values; test the shell with a smaller number of integration tests.
6. Keep orchestration direct and avoid inventing a command language unless the workflow needs one.
7. Preserve transaction boundaries where decisions depend on concurrent state.

## Worked example

Mixed version:

```ts
async function notifyExpired(db: Database, mailer: Mailer) {
  for (const user of await db.users()) {
    if (user.expiresAt <= Date.now() && !user.trial) {
      await mailer.send(user.email, `Expired: ${user.name}`);
    }
  }
}
```

Separated version:

```ts
type User = { name: string; email: string; expiresAt: number; trial: boolean };
type Message = { to: string; body: string };

const expiryMessages = (users: User[], now: number): Message[] => users
  .filter(user => user.expiresAt <= now && !user.trial)
  .map(user => ({ to: user.email, body: `Expired: ${user.name}` }));

async function sendExpiryMessages(db: Database, mailer: Mailer) {
  const messages = expiryMessages(await db.users(), Date.now());
  await Promise.all(messages.map(m => mailer.send(m.to, m.body)));
}
```

The expiration policy and message generation need no mocks. The shell clearly exposes the two effects.

## Values at boundaries

Simple immutable values decouple subsystems better than rich objects carrying hidden behavior and resources. Boundary values should contain the information needed by the next stage without leaking database sessions, request objects, or vendor SDK types into the core.

Parse untrusted input before it reaches the core. The core should operate on domain representations whose invariants are already established.

## Error handling

The core can return explicit domain errors or decisions. The shell translates infrastructure failures, chooses retry and logging behavior, and maps outcomes to transport responses. Do not hide all failures in exceptions if callers need to reason about expected domain rejection.

## Limits

Some behavior is inherently effectful:

- transactions whose decision must be made against locked state;
- streaming pipelines too large to materialize;
- concurrency and timing protocols;
- interactive UI lifecycles;
- algorithms using controlled local mutation for performance.

Extract the largest practical deterministic portion without duplicating huge datasets or obscuring the lifecycle. Purity is valuable only when it simplifies reasoning.

## Failure modes

- elaborate free-monad or command-algebra machinery for simple effects;
- a “thin” shell that still duplicates business rules;
- pure functions that merely move mutable global access behind wrappers;
- returning enormous action graphs instead of performing clear orchestration;
- ignoring transactions and race conditions to preserve a pure shape;
- excessive interfaces and mocks around every function.

## Review checklist

- Which lines make decisions, and which perform effects?
- Can time, randomness, and configuration become explicit inputs?
- Can the core return ordinary values?
- Are vendor or transport types leaking inward?
- Are expected domain errors explicit?
- Does the shell contain policy that belongs in the core?
- Are transactions or streaming constraints being preserved?
- Is the functional machinery simpler than direct code?

## Guidance for agentic coding

An agent should extract deterministic business rules from effectful workflows when this materially improves testing and clarity. It should use plain function parameters and return values before interfaces or command frameworks. It must preserve real transaction, streaming, and concurrency semantics and should not pursue purity as an aesthetic rewrite outside the task.

## Sources

- [Boundaries — Gary Bernhardt](https://www.destroyallsoftware.com/talks/boundaries)
- [Simplify Your Code: Functional Core, Imperative Shell — Google Testing Blog](https://testing.googleblog.com/2025/10/simplify-your-code-functional-core.html)
