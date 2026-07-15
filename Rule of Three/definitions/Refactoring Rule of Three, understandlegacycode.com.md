# Source note: Refactoring Rule of Three

- Author: Nicolas Carlo
- URL: https://understandlegacycode.com/blog/refactoring-rule-of-three/
- Accessed: 2026-07-15
- Type: practical explanation

The Rule of Three is the heuristic “three strikes and you refactor”: tolerate early duplication until repeated cases reveal a stable common shape. The article stresses that short code is not automatically maintainable, identical code can represent different concepts, and a wrong abstraction is costlier than duplication.

Three is evidence, not a command. If no coherent name or stable contract emerges, waiting longer is preferable to forcing a parameterized abstraction.
