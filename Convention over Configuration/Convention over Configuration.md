# Convention over Configuration

## Definition

Convention over Configuration makes common behavior follow shared defaults so developers specify only meaningful exceptions. Instead of asking every project or module to repeat routine choices—file locations, table names, test discovery, identifiers, build targets—the system adopts one predictable convention.

The principle became strongly associated with Ruby on Rails, where model names, database tables, migrations, routes, and directory structure work together through consistent naming. Its value is broader: any repository, framework, or organization can replace repeated low-value decisions with stable defaults.

## How conventions remove code

Configuration is code-like inventory. It must be parsed, validated, documented, versioned, tested, and synchronized. When most configurations say the same thing, they encode noise rather than intent.

A good convention provides:

- less configuration and glue;
- fewer naming and layout decisions;
- predictable discovery by tools and people;
- easier onboarding;
- stronger generators and automation;
- a clear visual distinction between ordinary and exceptional behavior.

Conventions compound. Once a model name predicts a table, the same knowledge can drive associations, migrations, fixtures, and administrative tools.

## Worked example

Repeated configuration:

```yaml
users:
  source: src/features/users/index.ts
  tests: src/features/users/index.test.ts
  migrations: src/features/users/migrations
orders:
  source: src/features/orders/index.ts
  tests: src/features/orders/index.test.ts
  migrations: src/features/orders/migrations
```

One documented convention replaces it:

```text
src/features/<name>/index.ts
src/features/<name>/index.test.ts
src/features/<name>/migrations/
```

Tooling can discover all modules. Configuration is reserved for an exceptional module that genuinely cannot follow the pattern.

## Designing a good convention

1. Observe repeated choices across real cases.
2. Select the most unsurprising existing ecosystem pattern.
3. Cover the dominant case, not every possible case.
4. Make the convention visible in documentation and generated structure.
5. Validate it automatically and report actionable errors.
6. Provide a narrow explicit override for legitimate exceptions.
7. Remove redundant configuration after adoption.
8. Version convention changes deliberately because many consumers depend on them.

Prefer language, framework, and community conventions over inventing local ones. Familiarity is part of simplicity.

## Defaults, policy, and magic

A default is valuable when users can predict it or discover it quickly. Hidden behavior becomes “magic” when its cause is unclear, its override is obscure, or it depends on global state. Good convention-based systems show what was inferred and where to customize it.

Conventions should encode routine choices, not conceal important business policy. A tax rule, authorization condition, or data-retention period deserves explicit domain representation even if most deployments share it.

## Precedence and overrides

A convention-based system needs a simple precedence model. A useful order is: explicit local override, project-level setting, framework convention, then platform default. If multiple implicit sources can override one another, maintainers cannot predict behavior and the saved configuration returns as debugging cost.

Overrides should be narrow. Let a model override its table name without replacing the entire discovery system. Validate overrides eagerly, include the inferred and explicit values in diagnostics, and avoid environment-dependent inference that cannot be reproduced locally.

## Adopting a convention safely

For an existing codebase, inventory current variants before standardizing them. Choose the dominant or ecosystem-native form, migrate in small mechanical steps, and update generators, tests, documentation, and CI together. Compatibility aliases may be useful during a staged migration, but they need an explicit removal condition; otherwise the repository permanently supports two conventions.

The success measure is not merely fewer configuration lines. Maintainers should be able to predict where a new artifact belongs, tools should discover it automatically, and exceptions should be obvious in review.

## Failure modes

- undocumented naming or lifecycle hooks;
- conventions covering too few cases, causing constant overrides;
- exceptions expressed through awkward filenames or dummy structures;
- several overlapping conventions with unclear precedence;
- changing mature defaults without migration support;
- inventing local conventions that conflict with framework expectations;
- making critical policy implicit;
- adding configuration knobs before any exception exists.

When exceptions dominate, explicit configuration or ordinary code may be clearer.

## Review checklist

- Which repeated decisions are truly routine?
- Is there an existing ecosystem convention?
- Does the default cover most real cases?
- Can a newcomer discover what was inferred?
- Are errors and overrides clear?
- Is business policy being hidden as a default?
- Are many exceptions evidence that the convention is wrong?
- Can redundant configuration now be deleted?

## Guidance for agentic coding

An agent should first follow repository and framework conventions rather than create new layouts or configuration. It should add explicit configuration only for a real exception. It must not infer important domain policy from opaque naming alone. When introducing a convention, it should document it, make tooling errors clear, and preserve a straightforward escape hatch.

## Sources

- [The Rails Doctrine — Convention over Configuration](https://rubyonrails.org/doctrine#convention-over-configuration)
- [Active Record Basics — Rails Guides](https://guides.rubyonrails.org/active_record_basics.html#convention-over-configuration-in-active-record)
