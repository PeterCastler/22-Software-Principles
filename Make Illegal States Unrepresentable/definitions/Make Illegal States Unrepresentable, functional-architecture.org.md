# Source note: Make Illegal States Unrepresentable

- Publisher: Functional Software Architecture
- URL: https://functional-architecture.org/make_illegal_states_unrepresentable/
- Accessed: 2026-07-15
- Type: detailed principle and historical synthesis

The principle models data so values that violate domain invariants cannot be constructed. The original connection-state example replaces a flat record full of optional fields with variants whose fields exist only in the states that need them.

Techniques include sum/product types, smart constructors, abstract types, and deriving redundant values rather than storing them. The benefit is fewer defensive checks and fewer state combinations; the cost is additional modeling and possible migration friction.
