# Single Responsibility Principle

## Definition

The Single Responsibility Principle (SRP) says to gather together things that change for the same reason and separate things that change for different reasons. Robert C. Martin's more precise interpretation is stakeholder-oriented: a software module should be responsible to one cohesive actor or business function.

SRP is commonly diluted into “a class should do one thing.” That wording is too vague and encourages microscopic classes. A module may perform several operations while serving one responsibility. The important question is who asks it to change and which business purpose those changes serve.

## Historical foundation

SRP builds on David Parnas's information-hiding criterion: modules should hide difficult or likely-to-change design decisions. Martin refined that change-oriented view by asking which organizational actors originate those changes.

## The actor test

Consider an employee module with methods to calculate pay, save records, and report hours. Finance determines pay policy, technology owns database storage, and operations or audit owns report format. Putting all three in one class means a database change can break payroll or a pay change can alter reporting.

The responsibilities are not “calculate,” “save,” and “format” merely because those are verbs. They are financial policy, persistence, and operational reporting because those are independent sources of change.

## Application method

1. List the ways the module has changed or is expected to change from known requirements.
2. Identify the stakeholder, business capability, or policy behind each change.
3. Group data and behavior that maintain one invariant for one cohesive actor.
4. Separate infrastructure and representations owned elsewhere.
5. Choose the smallest useful module boundary; a function or file may suffice.
6. Keep interfaces narrow and expressed in the responsibility's vocabulary.
7. Check that each new part has meaningful cohesion rather than one arbitrary method.

## Worked example

Before:

```ts
class Invoice {
  constructor(readonly items: Array<{ price: number }>) {}

  total() {
    return this.items.reduce((sum, item) => sum + item.price, 0);
  }

  async save(db: Database) {
    await db.insert("invoices", this);
  }

  toHtml() {
    return `<p>Total: ${this.total()}</p>`;
  }
}
```

Pricing policy, database representation, and HTML presentation change independently. A direct separation is:

```ts
type Invoice = { items: Array<{ price: number }> };

const invoiceTotal = (invoice: Invoice): number =>
  invoice.items.reduce((sum, item) => sum + item.price, 0);

const saveInvoice = (db: Database, invoice: Invoice) =>
  db.insert("invoices", invoice);

const invoiceHtml = (invoice: Invoice): string =>
  `<p>Total: ${invoiceTotal(invoice)}</p>`;
```

No interface or class hierarchy is needed. Each responsibility has a clear owner and can be tested at the appropriate level.

## Choosing module size

SRP does not determine an absolute size. A pricing module may contain many related functions because all enforce one pricing policy. Splitting each into its own class would reduce cohesion and increase navigation.

Signals that a module has multiple responsibilities include:

- unrelated domain vocabularies;
- imports from UI, database, and business layers together;
- tests requiring unrelated fixtures;
- merge conflicts from independent teams;
- changes that repeatedly touch disjoint subsets;
- a name such as `Manager`, `Processor`, or `Utils` covering many concepts.

## Failure modes

- **One-method-class explosion:** confusing responsibility with operation count.
- **Interface-per-class ceremony:** adding abstractions without variation or a boundary.
- **Speculative actors:** separating code for teams or requirements that do not exist.
- **Anemic modules:** moving all behavior into orchestration and leaving data without invariant ownership.
- **Scattered cohesion:** splitting one algorithm so understanding it requires many jumps.
- **Microservice literalism:** assuming each responsibility needs independent deployment.

## Review checklist

- Who asks this module to change?
- Are those requesters one cohesive business function?
- Which invariants belong together?
- Does the module mix policy, persistence, and presentation?
- Would splitting reduce coupling or only add forwarding?
- Can each resulting part be named in domain language?
- Are responsibilities based on current evidence rather than predicted teams?
- Does the new structure keep the use case traceable?

## Guidance for agentic coding

An agent should not enforce SRP by creating tiny classes or files. It should identify real reasons for change and split only independently owned concerns. Cohesive logic should remain together. Interfaces should be added only when they protect a meaningful boundary, and a private function should be preferred when it provides enough separation.

## Sources

- [The Single Responsibility Principle — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html)
- [On the Criteria To Be Used in Decomposing Systems into Modules — David Parnas](https://www.cs.umd.edu/class/spring2003/cmsc838p/Design/criteria.pdf)
