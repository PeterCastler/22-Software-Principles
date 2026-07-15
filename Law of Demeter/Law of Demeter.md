# Law of Demeter — Principle of Least Knowledge

## Definition

The Law of Demeter is a design guideline that limits how much one unit knows about the internal structure of its collaborators. A method should communicate with its immediate collaborators through meaningful operations rather than navigate through a chain of returned objects and depend on the shape of an entire object graph.

It is also called the Principle of Least Knowledge. The law aims to reduce structural coupling: changes to a collaborator's internal arrangement should not force changes in distant callers.

## Classic method formulation

A method may normally send messages to:

- its own object;
- its parameters;
- objects it creates;
- its direct fields or collaborators;
- elements of a collection it directly owns, depending on the formulation.

This is a heuristic for deciding which relationships are local enough to know. The precise goal is stable collaboration, not policing syntax.

## Worked example: the train-wreck problem

Consider:

```ts
order.customer.account.wallet.paymentMethod.charge(order.total);
```

The checkout code knows that an order has a customer, the customer has an account, the account has a wallet, and the wallet has a payment method. Renaming, replacing, or reorganizing any link changes the caller. Many callers may repeat the path and then apply inconsistent handling.

A nearer collaborator can expose the capability:

```ts
class Customer {
  constructor(private readonly payments: PaymentService) {}

  pay(amount: number): Promise<PaymentResult> {
    return this.payments.charge(amount);
  }
}

function checkout(order: { customer: Customer; total: number }) {
  return order.customer.pay(order.total);
}
```

The internal payment graph may still exist, but checkout depends only on the customer capability relevant to the use case.

## Application method

1. Identify navigation chains and calls made on objects obtained through other objects.
2. Determine whether the caller depends on unstable internal structure or merely transforms transparent data.
3. Find the nearest collaborator that owns the needed capability or information.
4. Add a cohesive operation at that boundary, or pass the required value directly.
5. Hide mutable internal collections and collaborators where callers could bypass invariants.
6. Remove duplicated navigation and handling from callers.
7. Reassess whether the new operation is meaningful or only a pass-through.

## One dot is not the law

Counting dots produces false positives. These can be perfectly reasonable:

```ts
users.filter(isActive).map(toSummary).join("\n");
builder.withName(name).withTimeout(500).build();
point.translate(dx, dy).scale(factor);
```

Fluent APIs return the same conceptual receiver, and collection pipelines operate on transparent values. The concern is knowledge of nested ownership and structure, not punctuation.

## Choosing between an operation and direct data

Use a domain operation when the navigation exposes an invariant, policy, or volatile structure. Pass a direct value when the caller legitimately owns the decision and adding a method would create a middle man.

For example, a report renderer may reasonably accept a plain `Address` value. Requiring `customer.renderShippingLabel()` would mix presentation into the customer solely to avoid accessing data.

## Collections

Returning a mutable internal collection exposes both structure and mutation. Prefer:

- a read-only snapshot;
- an iterator;
- a query method representing a stable need;
- a domain operation that performs controlled mutation.

Do not create a separate forwarding method for every imaginable collection query. Expose stable data when callers need general read access.

## Costs and misapplications

- pass-through methods that duplicate an entire nested API;
- “middle man” objects with no policy;
- hiding simple immutable data behind dozens of commands;
- moving unrelated responsibilities inward;
- treating fluent calls as violations;
- excessive copying to avoid returning values;
- depending on global service locators as a shortcut around navigation;
- obscuring performance by hiding expensive remote calls behind innocent-looking methods.

The replacement API must reveal relevant cost and failure semantics. A `customer.pay()` method should not pretend a network operation is an ordinary field access.

## Review checklist

- Does this code know the internal ownership chain of another component?
- Which links in the chain are likely to change?
- Is there a meaningful capability at a nearer boundary?
- Would passing one value be clearer than adding a forwarding method?
- Is the data intentionally transparent and immutable?
- Are mutable collections or collaborators exposed?
- Does the replacement reveal latency and failure?
- Has reducing navigation created a middle-man API?

## Guidance for agentic coding

An agent should treat long object-navigation chains as review signals, not automatic violations. It should distinguish transparent value pipelines from dependence on nested ownership. When a real structural dependency exists, it should expose the smallest meaningful operation or pass the needed value directly. It should avoid forests of pass-through methods and preserve visible cost and error behavior.

## Sources

- [Law of Demeter: Principle of Least Knowledge — Northeastern University](https://www.ccs.neu.edu/home/lieber/LoD.html)
- [The Paperboy, the Wallet, and the Law of Demeter](https://www.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/demeter.pdf)
