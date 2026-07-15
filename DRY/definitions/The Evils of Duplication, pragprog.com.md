# Source note: The Evils of Duplication

- Authors: Dave Thomas and Andy Hunt
- Work: *The Pragmatic Programmer*, 20th Anniversary Edition, excerpt supplied by the publisher
- URL: https://media.pragprog.com/titles/tpp20/dry.pdf
- Accessed: 2026-07-15
- Type: primary source for DRY

DRY concerns duplicated **knowledge or intent**, not merely repeated-looking text. A fact is dangerously duplicated when one conceptual change must be made in several representations or locations. Conversely, identical code can represent independent facts and should not automatically be coupled.

The source also applies DRY beyond functions: schemas, documentation, tests, generated artifacts, and build processes can all duplicate authority.
