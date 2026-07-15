# Dead Code Elimination

## Definition

Dead Code Elimination removes code and related artifacts that cannot affect any supported outcome. In compiler optimization, an instruction is dead when its result is unobservable or it is unreachable. At source level, the same liveness idea applies across a wider system boundary that includes public APIs, reflection, plugins, configuration, scripts, data migrations, and operational use.

Dead code is not merely untidy. It creates false choices, misleads maintainers, increases security and dependency surface, slows analysis, and forces tests and changes to preserve behavior no user receives.

## Categories of dead code

- unreachable branches and statements;
- unused private functions, parameters, fields, exports, and files;
- values computed but never observed;
- writes overwritten before any read;
- obsolete feature flags and rollout variants;
- abandoned compatibility and fallback paths;
- commented-out implementations;
- unused dependencies and build plugins;
- configuration keys with no consumer;
- tests, documentation, telemetry, and runbooks for removed behavior;
- data migrations or jobs that can no longer execute in supported environments.

Compilers distinguish dead instructions, dead arguments, dead stores, dead globals, and unreachable control-flow blocks because removing one item can expose another. Source cleanup has the same cascading property.

## Establishing liveness

Static search is useful but incomplete. Code may be reached through:

- reflection or dynamic imports;
- dependency injection registration;
- string-based routes, event names, or serializers;
- plugin discovery;
- public package consumers outside the repository;
- scheduled jobs and administrative scripts;
- database triggers or stored procedures;
- feature flags enabled only for selected tenants;
- incident recovery procedures.

The supported-system boundary must be explicit before “unused” becomes “dead.”

## Elimination method

1. Identify the candidate and why it appears dead.
2. Define all supported entry points and compatibility commitments.
3. Search symbols, strings, config keys, routes, jobs, documentation, and history.
4. Check production usage or add temporary instrumentation when static evidence is insufficient.
5. Confirm rollout and rollback no longer require the path.
6. Remove the smallest coherent behavior slice.
7. Delete dependent flags, tests, configuration, docs, telemetry, and dependencies.
8. Run static checks, focused tests, the broader suite, builds, and relevant integration checks.
9. Monitor the release if external or dynamic use was possible.

## Worked example

After a new total calculation has completed rollout, a permanent false flag leaves the old path in the system:

```ts
const USE_LEGACY_TOTAL = false;

function total(items: Array<{ price: number }>): number {
  if (USE_LEGACY_TOTAL) {
    return items.reduce((sum, item) => sum + Math.round(item.price), 0);
  }
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

Once metrics, rollback policy, and supported versions prove the legacy calculation unnecessary:

```ts
function total(items: Array<{ price: number }>): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}
```

Complete removal also deletes the flag definition, configuration, old-path tests, legacy dashboards, documentation, and any dependency used only there.

## Feature-flag lifecycle

Every temporary flag should have an owner, purpose, creation date, expected removal condition, and cleanup task. Release flags become dead-code generators when no one can say whether the off path is still supported. Long-lived permission or product settings are not release flags and should be modeled as durable domain behavior.

## Deprecation before deletion

For public or uncertain consumers, use a staged approach:

1. mark the surface deprecated;
2. publish the replacement and migration guidance;
3. instrument usage where lawful and practical;
4. communicate a removal version or date;
5. remove only after the compatibility contract allows it.

## Risks and misapplications

- assuming no static references means no dynamic use;
- deleting rare disaster-recovery paths because tests do not call them;
- removing compatibility required by external clients;
- keeping dead code indefinitely because proof is hard;
- deleting only the function while leaving its surrounding artifacts;
- retaining commented code instead of using version history;
- allowing flags to become permanent forks without ownership.

The answer to uncertainty is better evidence, not automatic retention or deletion.

## Review checklist

- What observable result could this code affect?
- Are all dynamic, external, and operational entry points known?
- Does rollback or migration still depend on it?
- Is deprecation required?
- What adjacent artifacts exist solely for this behavior?
- Which verification proves removal safe?
- Does production instrumentation contradict static analysis?
- Who owns temporary flags and their removal?

## Guidance for agentic coding

An agent should not label code dead from a single `rg` result. It should inspect dynamic registration, public contracts, configuration, history, and operational context proportionately to risk. When evidence is strong, it should remove the whole coherent slice and verify broadly. It should never leave commented-out replacements or orphaned flags behind.

## Sources

- [LLVM's Analysis and Transform Passes — Dead Code Elimination](https://llvm.org/docs/Passes.html#dce-dead-code-elimination)
- [Dead Code — Refactoring.Guru](https://refactoring.guru/smells/dead-code)
