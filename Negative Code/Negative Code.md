# Negative Code

## Definition

Negative Code is the idea that removing code while preserving or improving required behavior is genuine engineering progress. Source code is not productive inventory; it is a continuing liability that must be read, reviewed, tested, secured, migrated, operated, and eventually changed.

The term is associated with the story of Bill Atkinson rewriting the Apple Lisa's QuickDraw region engine. The new algorithm reportedly ran roughly six times faster and removed about 2,000 lines. When managers asked for weekly lines written, he reported `-2000`, exposing why added line count rewards bloat rather than value.

The lesson is not “deletion is always good.” Valuable negative code improves the ratio of supported capability to owned complexity.

## Where negative code comes from

- replacing a complicated algorithm with a simpler one;
- removing an obsolete feature or unsupported compatibility path;
- deleting expired feature flags and rollout branches;
- using a language or platform primitive instead of custom machinery;
- consolidating duplicated knowledge into one authority;
- choosing a representation that eliminates invalid states and checks;
- removing wrappers, adapters, or layers that no longer add policy;
- deleting dependencies whose capability is no longer used;
- automating generation instead of maintaining synchronized copies.

Deletion often propagates. Removing a feature should also remove its configuration, tests, dependencies, metrics, documentation, migrations, and operational procedures.

## Measuring the right thing

Line count is weak evidence because lines have unequal maintenance cost. Better questions are:

- How many concepts and states were removed?
- How many dependencies and failure paths disappeared?
- Is the execution path easier to trace?
- Did behavior, performance, or safety improve?
- Did the change reduce future coordination?
- Can fewer tests now cover the same contract because impossible states vanished?

Generated or declarative artifacts may contain many lines but little independent knowledge. Conversely, one line of reflection or dynamic evaluation can introduce large hidden complexity.

## Safe deletion method

1. **Define the supported contract.** Identify observable behavior, compatibility promises, and operational requirements.
2. **Establish evidence.** Use characterization tests, type checks, traces, production usage, documentation, or stakeholder confirmation.
3. **Search the perimeter.** Find direct and dynamic references, configuration keys, public exports, scripts, database jobs, and external clients.
4. **Remove a coherent slice.** Delete the implementation and everything that exists only to support it.
5. **Verify proportionately.** Run focused tests, broader suites, builds, static checks, and deployment validation as risk requires.
6. **Observe after release.** When liveness depends on production behavior, monitor before removing rollback capability.
7. **Record the reason.** A concise commit or decision note prevents accidental restoration of obsolete complexity.

## Worked example

A hand-written slug algorithm owns character classification, repeated-separator removal, and edge cases:

```ts
function slug(value: string): string {
  let result = "";
  for (const character of value.trim().toLowerCase()) {
    if (character >= "a" && character <= "z") result += character;
    else if (character === " " || character === "_") result += "-";
  }
  while (result.includes("--")) result = result.replace("--", "-");
  return result;
}
```

If the required contract is explicitly ASCII-only, direct primitives can replace it:

```ts
function slug(value: string): string {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z]+/g, "-")
    .replace(/^-|-$/g, "");
}
```

If Unicode transliteration is required, the shorter regex is not complete; a tested library may be the correct negative-code move. Deletion is judged against the full contract.

## Deleting abstractions

Abstractions deserve removal when they have one implementation, one caller, no boundary role, and merely forward behavior. Inlining can restore local clarity. However, a one-implementation interface may still protect stable policy from a volatile external SDK. Count responsibilities, not implementations alone.

Version control is the archive. Commented-out code, unused alternatives, and “just in case” files do not belong in the working system.

## Risks and misapplications

- code golf that reduces lines but increases cognitive load;
- deleting defensive behavior without proving the guarded case impossible;
- removing public API surface based only on repository references;
- replacing local code with a heavy or risky dependency;
- optimizing for a negative line count instead of outcomes;
- large rewrites whose behavior cannot be characterized;
- deleting tests that document a still-supported contract;
- mistaking generated volume for maintained knowledge.

## Review checklist

- What supported behavior must remain?
- What evidence proves the candidate is redundant or replaceable?
- Are dynamic and external consumers accounted for?
- What surrounding artifacts become obsolete?
- Does the replacement introduce hidden dependency or semantic cost?
- Are readability, security, and error behavior preserved?
- Can the deletion be staged or observed if uncertainty remains?
- Are metrics measuring outcomes rather than lines?

## Guidance for agentic coding

An agent should treat safe deletion as a first-class implementation option. It should search beyond direct references, preserve user-visible and operational contracts, and remove the full obsolete perimeter. It must not compress code for appearance or delete unfamiliar safeguards without evidence. After adding behavior, it should perform a focused deletion pass limited to the task's scope.

## Sources

- [-2000 Lines of Code — Andy Hertzfeld, Folklore.org](https://www.folklore.org/Negative_2000_Lines_Of_Code.html)
- [Dispensables — Refactoring.Guru](https://refactoring.guru/refactoring/smells/dispensables)
