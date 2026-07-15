# Separation of Concerns

## Definition

Separation of Concerns organizes software so that distinct kinds of work can be understood, changed, and verified with minimal knowledge of one another. A concern is a coherent aspect of a system—business policy, persistence, presentation, transport, authorization, telemetry, scheduling, or another responsibility with its own rules and reasons to change.

Separation is not the physical act of creating more files, classes, services, or layers. It is the logical act of preventing unrelated decisions from becoming entangled. Two private functions in one module may separate concerns well; five deployable services may still mix them badly.

## Why concerns become tangled

A straightforward feature often begins as one procedure that loads data, decides what it means, formats a result, writes state, and reports telemetry. As requirements grow, each part gains branches. A presentation change risks business logic, tests require databases for pure calculations, and infrastructure details spread into domain code.

Entanglement creates change amplification: a request from one stakeholder touches code owned by several others. It also hides the essential rule among incidental mechanics.

## Identifying a useful boundary

Separate two concerns when one or more of these are true:

- they change for different business reasons or stakeholders;
- they operate at different rates of change;
- one can be tested without the other's environment;
- one is stable policy and the other a volatile implementation detail;
- they use distinct vocabularies;
- they have different security, deployment, or reliability requirements;
- reuse of one without the other is a present need.

Keep them together when their steps form one cohesive invariant, always change together, and separation would create only forwarding or navigation.

## Application method

1. Trace one complete use case from input to outcome.
2. Mark the decisions, transformations, effects, and representations.
3. Group operations that use the same vocabulary and change for the same reason.
4. Define narrow boundaries between groups using ordinary values where possible.
5. Keep orchestration thin: it sequences concerns but does not duplicate their rules.
6. Place dependencies so core policy does not need infrastructure internals.
7. Verify each concern independently where that yields simpler tests.
8. Recombine concerns explicitly at the application boundary.

## Worked example

This function mixes retrieval, overdue policy, and HTML presentation:

```ts
async function showOverdueInvoices() {
  const response = await fetch("/api/invoices");
  const invoices = await response.json();
  document.body.innerHTML = invoices
    .filter((invoice: any) => Date.parse(invoice.dueAt) < Date.now())
    .map((invoice: any) => `<strong>${invoice.customer}: ${invoice.total}</strong>`)
    .join("");
}
```

A minimal separation is three functions, not an enterprise layer stack:

```ts
type Invoice = { customer: string; total: number; dueAt: string };

const overdue = (invoices: Invoice[], now: number): Invoice[] =>
  invoices.filter(invoice => Date.parse(invoice.dueAt) < now);

const renderInvoices = (invoices: Invoice[]): string =>
  invoices.map(i => `<strong>${i.customer}: ${i.total}</strong>`).join("");

async function displayOverdueInvoices() {
  const response = await fetch("/api/invoices");
  const invoices: Invoice[] = await response.json();
  document.body.innerHTML = renderInvoices(overdue(invoices, Date.now()));
}
```

Overdue rules can now be tested with values, presentation can change without networking, and the shell remains direct.

## Levels of separation

Separation can exist within a function, between functions, modules, packages, processes, or services. Choose the cheapest boundary that delivers the needed independence. Each stronger boundary adds contracts, serialization, versioning, observability, and failure handling.

Do not infer that separate concerns require separate deployments. Logical modularity inside one application is often enough.

## Cross-cutting concerns

Authorization, logging, retries, and tracing affect many use cases. Centralizing them can prevent duplication, but hiding them in magic middleware can make behavior invisible. Keep policy explicit: a reusable mechanism may enforce it, while use cases still state when and why it applies.

## Failure modes

- **Layer proliferation:** controller → service → manager → repository, each forwarding the call.
- **Fragmentation:** a cohesive algorithm scattered across tiny files.
- **False boundaries:** modules split by technical nouns while business policy remains tangled.
- **Leaky boundaries:** domain code imports database records or HTTP objects directly.
- **Premature distribution:** logical concerns become services without operational justification.
- **Duplicated orchestration:** business rules repeated in controllers, jobs, and event handlers.

## Review checklist

- What distinct kinds of decisions are present?
- Which parts change for different reasons?
- Does each boundary isolate real change or merely forward calls?
- Can plain values cross the boundary?
- Has a logical separation been made unnecessarily deployable?
- Is orchestration thin and free of duplicated policy?
- Can core rules be tested without infrastructure setup?
- Are cross-cutting rules visible and consistently owned?

## Guidance for agentic coding

An agent should separate business decisions from I/O when it materially improves clarity or verification, but should use the smallest local boundary that works. It should not generate controller/service/repository layers by default. New modules or interfaces must isolate a demonstrated concern, not satisfy a template. The final execution path should remain easy to trace.

## Sources

- [Architectural Principles: Separation of Concerns — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#separation-of-concerns)
- [On the Role of Scientific Thought — E. W. Dijkstra](https://www.cs.utexas.edu/~EWD/transcriptions/EWD04xx/EWD447.html)
