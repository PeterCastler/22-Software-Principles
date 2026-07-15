# Before and after

## Before: every module configures the ordinary case

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

## After: document and implement one convention

```text
src/features/<name>/index.ts
src/features/<name>/index.test.ts
src/features/<name>/migrations/
```

Only exceptions need configuration. The convention should be discoverable, validated by tooling, and cheap to override when the domain genuinely differs.
