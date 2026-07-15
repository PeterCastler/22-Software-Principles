# Source note: Tell, Don't Ask

- Author: Martin Fowler
- URL: https://martinfowler.com/bliki/TellDontAsk.html
- Accessed: 2026-07-15
- Type: principle explanation and critique

Tell, Don't Ask encourages placing behavior with the data and rules it uses: instead of querying an object's state and deciding elsewhere, request the meaningful operation from the responsible object. This preserves encapsulation and prevents policy from being reconstructed by many callers.

Fowler also warns against treating it as absolute. Queries can be the clearer design, and layering or other concerns can outweigh co-location.
