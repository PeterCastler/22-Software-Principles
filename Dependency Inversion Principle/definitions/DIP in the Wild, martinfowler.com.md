# Source note: DIP in the Wild

- Author: Brett Schuchert
- URL: https://martinfowler.com/articles/dipInTheWild.html
- Accessed: 2026-07-15
- Type: production examples and synthesis

The article formulates DIP as dependencies moving toward higher-level, domain-relevant abstractions: policy should not depend directly on low-level details. It emphasizes practical applications rather than an interface-per-class recipe.

For minimal code, inversion pays when a volatile or external detail would otherwise infect stable policy. If there is no real boundary or variation, an abstraction can be needless indirection.
