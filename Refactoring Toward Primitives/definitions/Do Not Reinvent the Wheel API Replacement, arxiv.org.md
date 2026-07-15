# Source note: Don't Reinvent the Wheel — API Replacement Refactoring

- Authors: Arghavan Moradi Dakhel et al.
- URL: https://arxiv.org/abs/2208.07624
- Accessed: 2026-07-15
- Type: research paper

The paper studies replacing custom implementations with existing APIs. This library generalizes that move to language, standard-library, framework, database, browser, operating-system, and managed-platform primitives.

Replacement is not automatically beneficial: behavior, compatibility, dependency weight, security, performance, and lifecycle must be compared. The ideal primitive removes more owned machinery than the contract it introduces.
