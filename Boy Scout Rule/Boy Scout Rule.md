# Boy Scout Rule

## Definition

The Boy Scout Rule adapts the camping maxim “leave the campsite cleaner than you found it” to software maintenance: when changing code, make a small, safe improvement to the area you already need to understand.

It is a practice of continuous local stewardship, not authorization for broad cleanup. The codebase improves through bounded, repeated changes that remain easy to review and verify.

## Why incremental cleanup matters

Code quality tends to drift as requirements change, names lose accuracy, temporary branches remain, and local workarounds accumulate. Large cleanup projects are easy to defer and risky to merge. A developer already modifying an area has fresh context, active tests, and a reason to inspect its behavior, making small improvement relatively cheap.

Useful Boy Scout changes include:

- renaming a misleading local identifier;
- simplifying a conditional directly affected by the task;
- deleting a proven-dead branch in the touched path;
- replacing an unexplained literal with domain language;
- updating stale nearby documentation;
- removing a redundant comment;
- adding a focused characterization test before modification;
- making an error message more actionable;
- reducing duplication introduced or exposed by the current change.

## Scope rule

A cleanup belongs with the current task when:

1. it is in code that must be understood or modified for the task;
2. its intent is obvious and behavior-preserving, or its behavior change is part of the task;
3. it can be reviewed and verified with the main change;
4. it reduces more complexity than it adds;
5. it does not broaden public APIs, architecture, or dependencies without necessity.

If the cleanup expands into another module, requires new design decisions, or obscures the requested change, make it separate work.

## Worked example

The requested change is to support a configurable request timeout. The touched function also has a misleading name, an unexplained status literal, and an unhelpful error:

```ts
async function doIt(url: string) {
  const response = await fetch(url);
  if (response.status === 200) return response.json();
  throw new Error("failed");
}
```

A bounded improvement is:

```ts
const HTTP_OK = 200;

async function fetchJson(url: string, timeoutMs: number) {
  const response = await fetch(url, {
    signal: AbortSignal.timeout(timeoutMs),
  });

  if (response.status === HTTP_OK) return response.json();
  throw new Error(`Request failed with status ${response.status}`);
}
```

The new behavior is implemented, and the immediately touched code becomes clearer. Redesigning every HTTP caller in the repository would exceed the rule's local scope.

## Separating cleanup from behavior change

Reviewers need to distinguish what preserves behavior from what changes it. Helpful techniques include:

- a characterization test before refactoring;
- a preparatory behavior-preserving commit followed by the feature commit;
- small diffs with mechanical moves separated from logic edits;
- explicit notes identifying cleanup included in the change.

Separate commits are useful when risk or review complexity warrants them, but do not create ceremony for a trivial rename.

## Risk-based application

During an incident, the safest immediate action may be the smallest targeted fix. Cleanup can follow after service is restored. In fragile untested code, first establish behavior. In safety-critical or regulated code, even a rename may require formal review and traceability.

The rule is subordinate to change safety and the project's release process.

## Agentic-coding constraints

Autonomous agents can interpret “clean up as you go” too broadly because they can edit large areas quickly. Guardrails are essential:

- limit cleanup to the task's touched execution path;
- preserve unrelated user changes;
- do not reformat whole files or repositories;
- do not upgrade dependencies as incidental cleanup;
- do not redesign public APIs or architecture;
- verify behavior proportionately;
- stop when cleanup requires new product or design decisions.

## Common mistakes

- drive-by refactoring of unrelated modules;
- mixing a broad style migration with a feature;
- changing behavior under the label “cleanup”;
- adding abstractions merely to make code appear cleaner;
- reformatting that hides substantive changes;
- deleting unfamiliar safeguards without evidence;
- turning every task into a mandate for perfection;
- making cleanup so large it delays user value.

## Review checklist

- Is the improvement in code required by the task?
- Can its intent be understood independently?
- Is behavior preserved or explicitly covered by the request?
- Is verification adequate for the risk?
- Does the cleanup make the main diff easier or harder to review?
- Has scope expanded into unrelated files or APIs?
- Are user changes and repository conventions preserved?
- Should a larger improvement become separate work?

## Guidance for agentic coding

An agent should make only small, adjacent improvements while implementing the requested change. It should state or make obvious which edits are cleanup, preserve behavior with tests or equivalent evidence, and avoid repository-wide formatting, dependency updates, public API redesign, or unrelated refactors. When a cleanup requires materially new judgment, it should stop or separate the work rather than silently expand scope.

## Sources

- [The Boy Scout Rule — Laws of Software Engineering](https://lawsofsoftwareengineering.com/laws/boy-scout-rule/)
- [The Boy Scout Rule — 97 Things Every Programmer Should Know](https://www.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)
