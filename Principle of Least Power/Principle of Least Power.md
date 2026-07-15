# Principle of Least Power

## Definition

The Principle, or Rule, of Least Power says to use the least expressive language or mechanism that is sufficient for a task. The W3C Technical Architecture Group formulated it in terms of information reuse: more powerful languages make it harder for people and tools to determine what a program means without executing it.

A constrained representation cannot express as many behaviors, and that limitation is often an advantage. It improves analysis, validation, transformation, portability, security, and predictability. The principle is not “use weak tools”; it is “do not buy expressive power you do not need.”

## A spectrum of power

For many tasks, mechanisms form a rough progression:

- fixed value;
- structured data;
- schema or declarative rule;
- lookup table or regular expression;
- constrained query or template language;
- general-purpose function;
- arbitrary script or plugin.

Moving upward enables more behavior but also more possible states, side effects, and analysis difficulty. A constant cannot perform I/O. A JSON document cannot loop forever. A database constraint is visible to every writer. Native HTML interaction carries semantics that a generic `div` plus JavaScript must recreate.

## Worked examples

Use:

- a constant instead of a callback when the value never varies;
- a map instead of an `if` chain when variation is a fixed mapping;
- a database uniqueness constraint instead of relying only on pre-insert checks;
- HTML `<details>` instead of JavaScript that manually synchronizes a button, hidden region, keyboard behavior, and accessibility state;
- CSS media queries instead of resize-event scripts for responsive presentation;
- a schema instead of repeated handwritten structural validation;
- a standard query instead of loading all records for custom iteration.

For example, this scripted disclosure:

```html
<button id="toggle" aria-expanded="false">Details</button>
<div id="details" hidden>Shipping takes two days.</div>
<script>
  // Event handling and accessibility-state synchronization omitted.
</script>
```

can often become:

```html
<details>
  <summary>Details</summary>
  <p>Shipping takes two days.</p>
</details>
```

The HTML element is less expressive than arbitrary JavaScript, but the browser supplies the complete interaction semantics.

## Application method

1. **Describe the required behavior.** Include dynamic behavior, error handling, accessibility, performance, and update needs.
2. **List candidate mechanisms from weakest to strongest.** Start with values and existing declarative primitives.
3. **Choose the first mechanism that expresses the complete requirement clearly.** Do not choose a weaker tool that requires contortions.
4. **Evaluate analyzability.** Can tools validate, transform, cache, secure, or document it without executing arbitrary behavior?
5. **Constrain escape hatches.** If a stronger mechanism is needed for one case, isolate it rather than promoting the whole system.
6. **Reassess custom languages.** Configuration plus an interpreter can be more powerful and complex than direct ordinary code.

## Security and operations

Least Power reduces attack surface by limiting what user-controlled or administrator-controlled input can do. Structured policy data is safer than executable scripts; parameterized queries are safer than constructed code. Constrained build descriptions can be cached and analyzed more reliably than arbitrary shell hooks.

Operationally, declarative desired state lets tooling compare, plan, and reconcile. But only when the language remains understandable; a sprawling declarative system with hidden evaluation order can be more difficult than a small explicit script.

## Limits and failure modes

The weaker mechanism must still fit. Regular expressions are a poor substitute for parsers when the grammar is nested. Giant lookup tables can hide complex algorithms. Templating languages often grow into awkward programming languages. Configuration can shift compile-time errors to runtime and create a second API that must be versioned.

Use a stronger mechanism when the task genuinely requires sequencing, rich composition, stateful interaction, dynamic decisions, or precise error recovery. The goal is minimum sufficient power, not minimum theoretical expressiveness.

## Review checklist

- What is the weakest mechanism that fully expresses the requirement?
- Does the proposed language permit unnecessary side effects or control flow?
- Can tools understand the artifact without running it?
- Is configuration actually simpler than direct code plus types and tests?
- Does a native platform feature already provide semantics and accessibility?
- Are escape hatches local and explicit?
- Has a constrained language grown into a poorly tooled general-purpose one?

## Guidance for agentic coding

An agent should prefer direct values, data structures, schemas, native elements, platform constraints, and standard queries before scripts or custom frameworks. It should not introduce executable configuration, callback systems, or plugin APIs when a static mapping or ordinary function suffices. It should choose a stronger mechanism only after identifying the concrete capability the weaker one lacks.

## Sources

- [The Rule of Least Power — W3C Technical Architecture Group](https://www.w3.org/2001/tag/doc/leastPower.html)
- [Principles of Design — Tim Berners-Lee](https://www.w3.org/DesignIssues/Principles.html)
