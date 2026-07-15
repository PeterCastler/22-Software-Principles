# Rule of Three

## Definition

The Rule of Three is the refactoring heuristic often summarized as “three strikes and you refactor.” The first time a solution appears, implement it directly. The second time, tolerate the duplication while observing similarities and differences. Around the third real occurrence, enough evidence may exist to extract a stable abstraction.

The number three is not a law. It is a reminder that reuse should be discovered from examples rather than predicted from one case. Its deeper historical form concerns learning a domain across multiple systems, not mechanically extracting every third repeated block into a function.

## The problem it addresses

Premature abstraction turns incomplete knowledge into a contract. A developer sees one instance, predicts future variation, and builds a generalized API. Later cases differ in ways the API did not anticipate, so the abstraction accumulates flags, overrides, callbacks, and exceptions. Callers become coupled to a structure based on an early guess.

Temporary duplication preserves independent evolution while the problem is still being learned. Three examples often reveal:

- which behavior is genuinely invariant;
- which details vary;
- whether cases share a domain concept or only syntax;
- what the abstraction should be named;
- where its ownership boundary belongs;
- whether reuse is valuable enough to offset indirection.

## Application method

1. **First occurrence:** solve the concrete problem cleanly and locally. Do not install a framework for imagined cases.
2. **Second occurrence:** note the resemblance. Compare domain meaning, ownership, inputs, outputs, and likely changes. Small duplication is acceptable.
3. **Third occurrence:** lay all examples side by side. Separate true invariants from accidental similarity.
4. **Name the concept.** If no precise domain name exists, understanding may still be insufficient.
5. **Extract the smallest stable core.** Leave variations at callers rather than parameterizing everything.
6. **Evaluate the result.** The abstraction should reduce coordination and make each caller clearer.
7. **Undo it if necessary.** A failed abstraction is not an asset merely because work was invested in it.

## Worked example

Three collections use the same definition of an active account:

```ts
const activeUsers = users.filter(user => user.enabled && !user.deletedAt);
const activeAdmins = admins.filter(admin => admin.enabled && !admin.deletedAt);
const activeEditors = editors.filter(editor => editor.enabled && !editor.deletedAt);
```

If `User`, `Admin`, and `Editor` are all account roles governed by one lifecycle policy, the examples reveal a coherent abstraction:

```ts
type AccountState = { enabled: boolean; deletedAt?: Date };

const isActive = (account: AccountState): boolean =>
  account.enabled && !account.deletedAt;

const activeUsers = users.filter(isActive);
const activeAdmins = admins.filter(isActive);
const activeEditors = editors.filter(isActive);
```

If the three statuses are owned by different policies—perhaps editors remain active during a grace period—identical code was coincidental. A shared predicate would wrongly couple them.

## When to abstract before three

Earlier extraction can be justified when:

- the domain already defines one authoritative concept;
- duplicated security, financial, or integrity logic creates immediate inconsistency risk;
- a public standard or protocol supplies the contract;
- generation from one schema is the obvious authority;
- the second occurrence exposes an established, stable platform pattern.

The rule is about evidence, not ritual. Strong domain evidence can arrive before a third code copy.

## When to wait beyond three

Wait longer when cases have different owners, the domain is rapidly changing, no clear name emerges, or extraction requires mode flags. Several similar implementations can remain cheaper than a shared abstraction across deployment or organizational boundaries.

## Signals of a healthy abstraction

- It has a specific domain name.
- Its callers use the same concept for the same reason.
- Differences remain explicit rather than hidden behind booleans.
- New cases fit without modifying the abstraction for caller identity.
- The shared contract is smaller than the repeated coordination it replaces.
- A change to the invariant should affect all callers.
- Reading a caller requires less, not more, navigation.

## Common misapplications

- counting copies without considering meaning;
- extracting one-use helpers merely to shorten a function;
- treating three as a mandatory threshold;
- building a generic library when a private function is sufficient;
- keeping a wrong abstraction because reversing it feels like failure;
- applying the rule to repeated test expectations that benefit from explicitness.

## Review checklist

- How many concrete examples exist?
- Do they represent the same domain knowledge?
- What is invariant, and what varies?
- Can the shared concept be named precisely?
- Would all callers change for the same reason?
- Does extraction require flags or caller-specific branches?
- Is the duplication currently causing real coordination risk?
- Would waiting produce materially better evidence?

## Guidance for agentic coding

An agent should preserve small duplication when the common concept is uncertain. It should not create helpers, base classes, or generic utilities from a single example merely to look “clean.” When three or more cases exist, it should still inspect their semantics and ownership before refactoring. If extraction is justified, it should choose the narrowest scope and avoid speculative extension points.

## Sources

- [Don't make Clean Code harder to maintain, use the Rule of Three — Nicolas Carlo](https://understandlegacycode.com/blog/refactoring-rule-of-three/)
- [Origins of “The Rule of Three” — Eoin Noble](https://eoinnoble.com/posts/origins-of-the-rule-of-three/)
