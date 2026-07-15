# Data-Driven Design

## Definition

Data-Driven Design, in the table-driven programming sense, moves regular variation out of repeated control flow and into a data structure. One small interpreter, lookup, or algorithm operates on the data. Adding or changing a case edits the representation rather than duplicating code.

This is distinct from analytics-driven product decisions and from data-oriented memory-layout design. Here, “data-driven” means program behavior is parameterized by explicit tables, maps, schemas, rules, or transition definitions.

## Good candidates

- mappings from statuses to labels, styles, or handlers;
- state-transition tables;
- routing and command dispatch;
- permission matrices;
- pricing tiers and tax bands;
- parser token definitions;
- protocol message metadata;
- parameterized tests;
- build matrices and deployment rules;
- field definitions used to derive types, validation, and UI.

The cases should share one algorithm and differ along regular, inspectable dimensions.

## Why it reduces complexity

Conditional code distributes cases through control flow. A table presents the whole decision space together, enabling review for missing or contradictory entries. The interpreter is tested once, and cases can often be validated or derived from one authority.

Data also enables tooling: editors can autocomplete keys, schemas can validate structure, and generators can produce documentation or types.

## Application method

1. Lay the branches or repeated implementations side by side.
2. Confirm they have the same structural shape and domain meaning.
3. Identify the dimensions that vary and the associated value or operation.
4. Choose the simplest representation: object, map, array, relation, or schema.
5. Derive key types from the data when the language supports it.
6. Write one direct lookup or interpreter.
7. Validate the data at construction or load time.
8. Keep exceptional algorithmic cases in code rather than distorting the table.

## Worked example

Branch-driven mapping:

```ts
function badge(status: string): string {
  if (status === "draft") return "gray";
  if (status === "review") return "blue";
  if (status === "published") return "green";
  throw new Error(`Unknown status: ${status}`);
}
```

Table-driven mapping:

```ts
const badgeByStatus = {
  draft: "gray",
  review: "blue",
  published: "green",
} as const;

type Status = keyof typeof badgeByStatus;

const badge = (status: Status): string => badgeByStatus[status];
```

The valid status type and mapping derive from one representation. No runtime unknown-status branch is needed inside trusted code.

## State machines

State transitions are strong candidates because hand-coded nested conditionals obscure the full graph. A transition table can make allowed events and next states explicit. It should still encode associated data and guards honestly; a generic table is not automatically clearer for highly state-specific logic.

## Code-owned versus remotely configured data

Developer-owned rules deployed with the program can remain in typed source data. Moving them to a database or remote configuration service adds permissions, caching, versioning, rollout, validation, audit, and runtime failure modes. Do that only when non-developer editing or independent deployment is a real requirement.

## The rules-engine trap

A generic rules engine can grow into a poorly tooled programming language. Warning signs include nested expressions, arbitrary callbacks, ordering dependencies, variables, loops, and debugging that requires mentally executing an interpreter.

When cases contain substantial unique algorithms, ordinary functions and control flow are more honest. Data should make behavior more visible, not merely move code into configuration.

## Risks and misapplications

- forcing fundamentally different cases into one table;
- hiding code as callbacks inside data;
- losing type safety through string keys;
- allowing invalid or duplicate entries without startup validation;
- introducing remote configuration for developer-owned constants;
- building a universal interpreter for a few branches;
- duplicating the list of valid keys separately from the table.

## Review checklist

- Do cases share one algorithm and domain meaning?
- What dimensions vary?
- Can the valid key set derive from the table?
- Is the data validated before use?
- Are callbacks hiding distinct algorithms?
- Would direct control flow be easier to understand?
- Does remote configuration have a real independent-editing requirement?
- Has the interpreter become a second programming language?

## Guidance for agentic coding

An agent should replace repetitive regular branches with the simplest typed table only when the shared shape is evident. It should derive types and validation from one authority where practical. It should not build generic rule engines, move code-owned policy to a database, or use opaque callback-filled configuration merely to claim the design is data-driven.

## Sources

- [Data-Driven Programming — The Art of Unix Programming](https://www.catb.org/esr/writings/taoup/html/ch09s01.html)
- [Table-Driven Design — Bill Wake](https://billwake.com/pattern-patter-table-driven-design/)
