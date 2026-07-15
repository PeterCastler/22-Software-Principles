# Source note: Boundaries

- Author: Gary Bernhardt
- Event: SCNA 2012
- URL: https://www.destroyallsoftware.com/talks/boundaries
- Accessed: 2026-07-15
- Type: canonical talk associated with the pattern

The talk explores simple values at subsystem boundaries, functional programming, mutability, isolated tests, and concurrency. Its architectural direction is to keep deterministic transformation separate from effectful interaction; the site explicitly identifies Bernhardt's “Functional Core, Imperative Shell” material.

Google's later worked explanation makes the split concrete: pure logic selects expired users and prepares messages, while the shell loads users and sends email.
