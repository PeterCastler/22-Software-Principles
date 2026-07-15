# Source note: The Rails Doctrine — Convention over Configuration

- Author: David Heinemeier Hansson
- URL: https://rubyonrails.org/doctrine#convention-over-configuration
- Accessed: 2026-07-15
- Type: canonical framework doctrine

Convention over Configuration replaces recurring low-value decisions with shared defaults. Rails derives relationships such as a `Person` model mapping to a `people` table, and uses conventional migration structure to supply forward and reverse behavior with little user code.

Conventions compound: once tools and developers share them, the ordinary path becomes predictable and automation can infer more. Exceptions remain possible but must be explicit.
