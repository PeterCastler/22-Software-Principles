# Source note: The Rule of Least Power

- Publisher: W3C Technical Architecture Group
- URL: https://www.w3.org/2001/tag/doc/leastPower.html
- Accessed: 2026-07-15
- Type: canonical technical finding

The rule recommends the least powerful language suitable for a purpose. More expressive mechanisms are harder for people and tools to analyze without executing them, which inhibits reuse, transformation, and safety. Descriptive data, markup, constrained expressions, and general-purpose programs form a rough progression of power.

For local software, the same tradeoff supports constants over callbacks, schemas over handwritten validators, CSS over JavaScript behavior, and declarative policy over an embedded general-purpose language—when the weaker mechanism fully meets the requirement.
