# DRY — Don't Repeat Yourself

## Definition

DRY states that every piece of knowledge in a system should have one unambiguous, authoritative representation. The principle was formulated by Andy Hunt and Dave Thomas in *The Pragmatic Programmer*. Its subject is duplicated knowledge and intent, not merely repeated source text.

A system violates DRY when one conceptual change requires coordinated edits in several places and those places can become inconsistent. Identical-looking code is not automatically a violation: two operations can currently share an implementation while representing different business facts that will change independently.

## Forms of duplication

Knowledge can be duplicated across many artifact types:

- a business threshold repeated in frontend, backend, and tests;
- a database schema restated manually in application types;
- an API contract copied into documentation and client code;
- a version number maintained in several build files;
- a validation rule implemented at multiple boundaries;
- a deployment matrix duplicated in scripts and CI configuration;
- the same derived value stored in several mutable fields.

Textual duplication is merely one signal. The diagnostic question is: **When this fact changes, must all these locations change together?**

## Coincidental duplication

Suppose both the minimum customer age and a page size are currently `18`. Reusing one constant would reduce a repeated literal but couple unrelated concepts. If legislation changes the age, pagination must not change. The correct design has two authorities:

```ts
const MINIMUM_CUSTOMER_AGE = 18;
const DEFAULT_PAGE_SIZE = 18;
```

Likewise, two validation functions with identical bodies may represent independent policies owned by different stakeholders. Keeping them separate is more maintainable until the domain shows that they are one rule.

## Application method

1. **Identify the knowledge.** State the rule, schema, mapping, or decision in domain language.
2. **Find every representation.** Search code, configuration, tests, documentation, generated artifacts, and operational scripts.
3. **Choose an authority.** Use the representation closest to the source of truth: constant, function, type, schema, table, or generator.
4. **Derive other forms.** Generate clients from schemas, types from tables, documentation from metadata, or UI from domain definitions where practical.
5. **Keep scope narrow.** Place the authority only as high as its actual consumers require.
6. **Remove old authorities.** A new shared function does not solve DRY if callers can still modify independent copies.
7. **Verify change behavior.** A single rule change should now require one authoritative edit and predictable derived updates.

## Worked example

Before:

```ts
export const shippingCost = (subtotal: number) => subtotal >= 50 ? 0 : 6;
export const shippingBanner = (subtotal: number) =>
  subtotal >= 50 ? "Free shipping" : "Shipping calculated at checkout";
```

The value `50` represents one business policy in two places. If the threshold changes, both must change together.

After:

```ts
const FREE_SHIPPING_MINIMUM = 50;

export const shippingCost = (subtotal: number) =>
  subtotal >= FREE_SHIPPING_MINIMUM ? 0 : 6;

export const shippingBanner = (subtotal: number) =>
  subtotal >= FREE_SHIPPING_MINIMUM
    ? "Free shipping"
    : "Shipping calculated at checkout";
```

The functions remain separate because cost calculation and presentation are different concerns, while the policy value has one authority.

## Choosing an abstraction

A good DRY abstraction has a precise domain name, a stable contract, and callers that should all change when it changes. Its implementation is usually smaller than the coordination it removes.

Warning signs of a wrong abstraction include:

- names such as `common`, `shared`, `generic`, or `misc`;
- boolean flags selecting caller-specific behavior;
- many optional parameters;
- type checks for particular consumers;
- callers immediately undoing or overriding shared behavior;
- unrelated teams needing coordination for independent changes.

When these appear, duplicating a small amount of code can be cheaper than preserving a false unity.

## DRY in tests and documentation

Tests may deliberately repeat expected values to remain independent of the production implementation. A test that computes its expectation using the same function as the code can reproduce the same bug and prove nothing. Reuse domain fixtures and builders when they reduce noise, but keep essential expectations explicit.

Documentation should not manually restate volatile facts when it can link to or derive from the authority. Yet concise explanatory repetition can help humans; DRY should not make every document unreadable without navigation.

## Review checklist

- What exact knowledge is duplicated?
- Would every occurrence change for the same reason?
- Which representation should be authoritative?
- Can other forms be derived rather than synchronized?
- Does the abstraction have a precise domain name?
- Are flags or exceptions revealing that cases are not truly one concept?
- Does test reuse hide the expected behavior?
- Is local duplication cheaper than cross-boundary coupling?

## Guidance for agentic coding

An agent should not deduplicate code solely because lines resemble each other. It should identify the shared domain fact, wait when ownership or variation is unclear, and prefer a small local authority over a generalized utility. It should preserve explicit test expectations and avoid creating cross-module abstractions that force unrelated future changes to coordinate.

## Sources

- [The Pragmatic Programmer — DRY excerpt](https://media.pragprog.com/titles/tpp20/dry.pdf)
- [Architectural Principles: DRY — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#dont-repeat-yourself-dry)
