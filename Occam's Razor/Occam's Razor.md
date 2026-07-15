# Occam's Razor

## Definition

Occam's Razor is the reasoning principle that when several explanations or solutions account for the evidence equally well, prefer the one that introduces fewer unsupported assumptions or unnecessary entities. It does not say that reality is always simple or that the shortest answer is automatically true. Adequacy to evidence comes first; parsimony breaks a tie.

In software, the “entities” being multiplied include services, databases, queues, caches, frameworks, deployment units, state copies, protocols, feature flags, background jobs, and bespoke abstractions. Each should be supported by a requirement or observed constraint.

## Worked example: architectural choice

Consider two architectures for a small internal approval tool:

- three independently deployed services, separate databases, a message broker, distributed tracing, and eventual-consistency repair jobs;
- one deployable application, one transactional database, and clear internal modules.

If no current scale, security, ownership, or release requirement needs distribution, the first option assumes future traffic, independent teams, and acceptable consistency tradeoffs. The second explains the same requirements with fewer assumptions and failure modes. Occam's Razor favors it until evidence changes.

This is not “monoliths are always better.” If measured load requires independent scaling, legal rules require data isolation, or teams need separate release control, those facts support additional entities.

## Diagnostic use

The razor also helps debugging. When a build suddenly fails, start with explanations that require little novelty: a recent edit, configuration drift, expired credentials, disk exhaustion, or dependency change. Do not begin with compiler corruption or a rare concurrency defect unless evidence points there.

A practical diagnostic sequence is:

1. Reproduce the observation.
2. Establish what changed.
3. Test the smallest, cheapest explanations.
4. Eliminate hypotheses with evidence.
5. Escalate to more complex explanations only as simpler ones fail.

This is a search-order heuristic, not permission to ignore severe low-probability risks where safety demands early consideration.

## Comparing complexity honestly

Count whole-system obligations:

- implementation and configuration;
- deployment and rollback;
- data ownership and consistency;
- authentication and authorization between components;
- observability and incident response;
- dependency upgrades and vendor contracts;
- failure recovery and disaster scenarios;
- cognitive load for maintainers.

Moving code to a managed service can reduce local source while adding a network dependency, billing model, permissions surface, and outage mode. Conversely, a mature managed database may remove far more operational complexity than it adds. The location of code is not the same as total complexity.

## Application method

1. Define the evidence and requirements every candidate must satisfy.
2. List the independent assumptions each option makes.
3. Count state holders, boundaries, and failure modes.
4. Prefer the adequate option with fewer unsupported commitments.
5. Record what evidence would justify revisiting the choice.
6. Measure after deployment instead of defending simplicity dogmatically.

## Limits and misuse

Some complexity is essential. Financial rules, distributed coordination, accessibility, security, resilience, and regulatory obligations cannot be removed by declaring a simple design. Redundancy may be necessary for availability. A sophisticated algorithm may be justified by measured performance. A more explicit design may use additional types or modules yet reduce reasoning complexity.

Common misuses include:

- equating fewer lines with fewer assumptions;
- using “simple” to dismiss requirements the designer dislikes;
- choosing familiar technology without counting its hidden costs;
- refusing needed boundaries after evidence appears;
- treating the razor as proof instead of a preference among adequate options.

## Review checklist

- Do all candidates satisfy the same complete requirements?
- Which assumptions are supported by current evidence?
- How many independent state holders and failure modes exist?
- Has local brevity hidden remote or operational complexity?
- What concrete observation justifies each service, queue, cache, or framework?
- What future evidence would trigger a more complex design?
- Are safety-critical hypotheses being considered proportionately?

## Guidance for agentic coding

An agent should begin with the simplest explanation consistent with repository evidence and the smallest architecture consistent with the task. It should not introduce distributed systems, caches, abstraction layers, or generic infrastructure without observed need. During diagnosis it should test common local causes before proposing broad rewrites, while still respecting high-impact security and data-integrity risks.

## Sources

- [Occam's Razor — Laws of Software Engineering](https://lawsofsoftwareengineering.com/laws/occams-razor/)
- [Simplicity — Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/simplicity/)
