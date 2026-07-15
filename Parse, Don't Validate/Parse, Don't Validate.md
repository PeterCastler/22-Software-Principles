# Parse, Don't Validate

## Definition

“Parse, Don't Validate” means converting less-structured or untrusted input into a more precise representation that carries the facts established during checking. Parsing either returns a trusted domain value or reports why no such value can be produced.

A validator commonly returns `true`, `false`, or nothing. It checks a fact and then discards what it learned, leaving the original value's type and structure unchanged. Downstream code must cast, recheck, or rely on an informal promise. A parser preserves the evidence in its output.

Parsing is broader than turning text into syntax trees. Any function that consumes a weak representation and produces a stronger one can be a parser: unknown JSON to a configuration, a list to a non-empty list, tuples to a duplicate-free map, or a number to a valid network port.

## The information-loss problem

Consider a function that checks that a list is non-empty and returns `void`. A later caller still holds an ordinary list, so a “get first element” operation must handle emptiness or use an unsafe assertion. The check occurred, but its result cannot be seen by the type or API.

A parser returns a non-empty-list representation. Any function accepting that representation can safely provide a first element without another branch. If the parsing check is removed later, callers stop compiling or otherwise fail at the construction boundary instead of silently losing the invariant.

## Boundary model

Programs naturally contain trust boundaries:

- network requests;
- command-line arguments;
- environment variables;
- configuration files;
- database rows written by older versions;
- messages from queues;
- user-entered forms;
- third-party API responses.

Keep raw representations near those boundaries. Parse them before domain behavior acts on them. Internal functions should accept the representation they actually require rather than a broad type plus comments and defensive checks.

## Application method

1. **Design the desired internal type.** Write the function signatures the domain logic wishes it could use.
2. **Identify raw inputs.** Distinguish transport and storage shapes from trusted domain values.
3. **Parse at the earliest useful boundary.** Check structure, types, ranges, relationships, and normalization before performing business effects.
4. **Return evidence.** Produce the precise value or a structured error; do not return only a success flag.
5. **Propagate the trusted type inward.** Change downstream functions so they cannot receive raw data accidentally.
6. **Remove redundant checks.** Delete only checks made impossible by the representation.
7. **Retain contextual checks.** Authorization, concurrent uniqueness, availability, and other mutable facts may still need verification at use time.

## Worked example

Validation that throws away knowledge:

```ts
type RawConfig = { port?: unknown };

function validateConfig(value: RawConfig): void {
  if (!Number.isInteger(value.port) || (value.port as number) <= 0) {
    throw new Error("Invalid port");
  }
}

function start(value: RawConfig) {
  validateConfig(value);
  server.listen(value.port as number);
}
```

The cast is still necessary because `RawConfig` remains weak. Parsing returns the value needed by the program:

```ts
type Config = { port: number };

function parseConfig(value: RawConfig): Config {
  if (!Number.isInteger(value.port) || (value.port as number) <= 0) {
    throw new Error("Invalid port");
  }
  return { port: value.port as number };
}

function start(value: RawConfig) {
  const config = parseConfig(value);
  server.listen(config.port);
}
```

In production, the parser should also enforce the upper port bound and return an error form appropriate to the application.

## Error design

Choose failure reporting based on callers:

- exceptions for unrecoverable startup configuration;
- result types for expected user or API errors;
- accumulated field errors for forms;
- partial success only when the domain explicitly supports it.

Errors should identify location, received value where safe, expected form, and remediation. Avoid leaking secrets or returning parser internals as public contracts.

## Normalization and parsing

Parsing can normalize equivalent external forms into one internal representation: trimming identifiers, canonicalizing case where the domain is case-insensitive, resolving defaults, or converting dates to a standard time basis. Normalization must be intentional; silently changing meaningful input can create bugs.

## Multi-stage parsing

Not all information is available at the outermost boundary. Parsing can occur in stages: first decode syntax, then select a variant, then parse variant-specific fields. The rule is to avoid acting on partially trusted data before the relevant stage is complete.

## Limits

Parsing does not make mutable external facts permanently true. A username can be syntactically valid but become unavailable before insertion. Authorization can change. Inventory and balances require transactional checks. Resource limits may need to be applied before full parsing to prevent denial of service.

Weakly typed languages can still preserve the distinction through modules, private constructors, opaque objects, and naming. Do not build a parser-combinator framework for a small fixed object when direct code is clearer.

## Common mistakes

- validators returning `void` while callers keep raw types;
- unchecked casts after nominal “validation”;
- exposing trusted constructors publicly;
- parsing the same input repeatedly in different modules;
- allowing raw transport types deep into domain code;
- treating authorization or concurrent state as parse-time invariants;
- normalizing input without a domain rule;
- returning vague errors that make invalid input impossible to diagnose.

## Review checklist

- What is the weakest input representation?
- What precise value does downstream code need?
- Does checking return usable evidence?
- Can raw and trusted values be confused?
- Is parsing performed before effects act on the data?
- Are all relevant structural invariants checked?
- Which facts remain mutable and need use-time checks?
- Are errors actionable and safe?
- Can redundant downstream checks now be removed?

## Guidance for agentic coding

An agent should design internal function signatures around trusted values, parse raw input near system boundaries, and return a precise value rather than a boolean-only check. It should remove downstream assertions only when the construction path proves them unnecessary. It must preserve contextual, concurrent, authorization, and resource-safety checks that parsing cannot establish permanently.

## Sources

- [Parse, don't validate — Alexis King](https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/)
- [Type Safety Back and Forth — Matt Parsons](https://www.parsonsmatt.org/2017/10/11/type_safety_back_and_forth.html)

