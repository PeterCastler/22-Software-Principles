# Source note: The Single Responsibility Principle

- Author: Robert C. Martin
- URL: https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html
- Accessed: 2026-07-15
- Type: explanation by the principle's formulator

SRP is often misstated as “a function does one thing.” Martin's formulation is about reasons for change: gather things that change for the same reason and separate things that change for different reasons. He grounds a reason in the person or tightly coupled stakeholder group whose business function requests the change.

The Employee example separates pay calculation, persistence, and hours reporting because finance, technology, and operations drive them independently.
