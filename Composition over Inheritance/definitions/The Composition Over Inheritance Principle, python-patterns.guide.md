# Source note: The Composition Over Inheritance Principle

- Author: Brandon Rhodes
- URL: https://python-patterns.guide/gang-of-four/composition-over-inheritance/
- Accessed: 2026-07-15
- Type: detailed worked explanation

The source traces “favor object composition over class inheritance” to the Gang of Four. Its logging example shows subclass explosion when output destinations and filtering vary along independent axes. Composition makes those behaviors independently replaceable and combinable at runtime.

The source also demonstrates that composition has several forms—adapters, bridges, decorators—and that a standard-library adapter can eliminate custom code entirely.
