# Composition over Inheritance

## Definition

“Favor object composition over class inheritance” recommends building behavior by combining focused collaborators rather than encoding reuse and variation primarily in class hierarchies. Inheritance establishes a fixed relationship between a subclass and its parent; composition assembles behavior from values or objects and can vary the combination independently.

The principle is a preference, not a ban. Stable subtype relationships and closed hierarchies can be clear. Composition is favored when the main need is reuse, optional behavior, or variation along independent axes.

## Why inheritance becomes costly

A subclass depends on more than a public method signature. It can depend on protected state, construction order, lifecycle hooks, override rules, and assumptions embedded in parent methods. This “fragile base class” coupling makes local changes ripple through descendants.

The larger problem appears when behavior varies along several axes. If loggers vary by output destination and formatting, inheritance tends toward one subclass per combination: text console, JSON console, text file, JSON file, and so on. Adding filtering or buffering multiplies combinations again.

Composition models each axis separately and combines them at runtime or construction time.

## Worked example

An inheritance approach begins:

```ts
class Logger { log(message: string) { console.log(message); } }
class JsonLogger extends Logger { /* JSON formatting */ }
class FileLogger extends Logger { /* file output */ }
class JsonFileLogger extends FileLogger { /* JSON plus file */ }
```

The JSON behavior is duplicated or forced through multiple inheritance patterns. Composition uses two independent functions:

```ts
type Format = (message: string) => string;
type Write = (message: string) => void;

const createLogger = (format: Format, write: Write) =>
  (message: string): void => write(format(message));

const text: Format = message => message;
const json: Format = message => JSON.stringify({ message });
const consoleWrite: Write = message => console.log(message);

const jsonConsoleLogger = createLogger(json, consoleWrite);
```

A file writer can be added without a JSON-file subclass. The types are functions because no additional class state is needed.

## Forms of composition

Composition need not mean dependency-injected classes. It includes:

- functions passed to higher-order functions;
- records containing strategies or capabilities;
- adapters that present an existing object through a needed interface;
- decorators that wrap behavior;
- pipelines of transformations;
- components assembled from child components;
- discriminated unions for closed variants.

Prefer the lightest form that fits. A function parameter is often enough.

## Application method

1. Identify the axes along which behavior actually varies.
2. Separate those behaviors into focused functions or objects.
3. Define only the contract the composer uses.
4. Assemble dependencies explicitly near the application boundary.
5. Keep fixed behavior direct; do not make everything injectable.
6. Use platform adapters before writing custom wrappers.
7. Check that combinations replace subclasses rather than merely moving boilerplate.

## When inheritance is appropriate

Inheritance can be clear when:

- the language or framework explicitly requires it;
- the relationship is a genuine behavioral subtype, not merely code reuse;
- the hierarchy is shallow and stable;
- the base class was designed for extension with a documented contract;
- a closed family of related implementations benefits from shared behavior;
- substitution can be tested and upheld.

Even then, inherited implementation should be modest. Prefer interfaces or sealed variants when the goal is type classification rather than shared mutable machinery.

## Failure modes of composition

Composition can also bloat code:

- one-method interfaces for fixed collaborators;
- constructors with dozens of injected dependencies;
- factories and containers that hide assembly;
- forwarding methods that add no policy;
- runtime strategies where a direct conditional is clearer;
- excessive mocking caused by over-segmented design.

If behavior does not vary and no boundary is protected, direct code is simpler than either inheritance or composition infrastructure.

## Review checklist

- Is inheritance being used for subtype semantics or only implementation reuse?
- How many independent axes of variation exist?
- Will subclasses multiply for combinations?
- Can a function or small value represent the behavior?
- Is the base-class extension contract stable and documented?
- Does composition create excessive wiring or forwarding?
- Are dependencies explicit at the assembly point?
- Is fixed behavior being made configurable without need?

## Guidance for agentic coding

An agent should avoid adding inheritance hierarchies for simple reuse. When real variation exists, it should prefer small functions or structural contracts and compose them explicitly. It should not create a strategy interface, factory, and dependency-injection registration for one implementation. Existing framework-mandated inheritance should be respected rather than rewritten without a task-driven reason.

## Sources

- [The Composition Over Inheritance Principle — Brandon Rhodes](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)
- [Replace Inheritance with Delegation — Refactoring.Guru](https://refactoring.guru/replace-inheritance-with-delegation)
