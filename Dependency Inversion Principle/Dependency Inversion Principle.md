# Dependency Inversion Principle

## Definition

The Dependency Inversion Principle (DIP) says that high-level policy should not depend directly on low-level implementation details. Both should depend on abstractions shaped by the policy, and details should implement those abstractions rather than controlling them.

In practical terms, source-code dependencies should point toward stable domain decisions. Runtime control may still flow outward to a database, email provider, filesystem, or framework, but the core describes what it needs in its own vocabulary.

## Inversion versus injection

Dependency injection supplies a collaborator from outside rather than constructing it internally. It can support DIP, but the two are not identical. If high-level code accepts a vendor SDK interface defined by the vendor, the dependency was injected but not necessarily inverted. DIP asks who owns the contract and which direction source dependencies point.

No container is required. A function argument can express the entire boundary.

## Source direction and runtime direction

At runtime, policy calls outward: checkout asks a receipt sender to deliver a message. At source level, the detail points inward: the vendor adapter imports and implements the contract owned by checkout. This distinction is the “inversion.” The execution order does not reverse; ownership of the compile-time contract does.

Keeping the composition root at the application edge makes both directions visible. It constructs concrete details, passes them to policy, and owns lifetimes and configuration. Domain modules should not import the composition root or resolve collaborators from a global registry.

## When DIP earns its cost

Use inversion when:

- stable business policy must outlive a volatile infrastructure choice;
- an external API exposes irrelevant or unstable details;
- multiple real implementations exist;
- a side effect prevents focused testing of important policy;
- architecture, security, or deployment requires an explicit boundary;
- the domain needs a narrower capability than the underlying system exposes.

Do not add an abstraction solely because every class “should have an interface.”

## Application method

1. Identify the high-level policy and the low-level detail it currently imports or constructs.
2. State the smallest capability the policy needs in domain language.
3. Define that contract next to, or owned by, the policy.
4. Implement an adapter in the infrastructure layer.
5. Compose the adapter and policy at an outer application boundary.
6. Keep vendor types, configuration, and errors from leaking inward.
7. Test policy through the domain contract and adapter through integration tests.

## Worked example

Direct dependency:

```ts
class Checkout {
  async complete(receipt: Receipt) {
    const client = new VendorEmailSdk(process.env.EMAIL_KEY!);
    await client.send(receipt.orderId, receipt.total);
  }
}
```

Inverted dependency:

```ts
type Receipt = { orderId: string; total: number };
type SendReceipt = (receipt: Receipt) => Promise<void>;

const completeCheckout = async (
  receipt: Receipt,
  sendReceipt: SendReceipt,
): Promise<void> => {
  await sendReceipt(receipt);
};

const sendVendorReceipt: SendReceipt = receipt =>
  vendorClient.send(receipt.orderId, receipt.total);
```

Checkout owns a domain-shaped capability. The adapter translates it to the vendor. A function type is enough; a factory, interface file, and dependency-injection container would add no value here.

## Boundary design

A useful policy-owned abstraction is:

- narrow—only operations actually used;
- stable—expressed in domain terms;
- honest about errors and latency;
- free of vendor request and response types;
- located where its ownership is clear;
- implemented by details without forcing policy changes.

Do not flatten meaningful infrastructure semantics. If an operation is eventually consistent, transactional, paginated, or rate-limited, the domain contract must represent consequences relevant to policy.

## Testing the boundary

Test high-level policy with a small in-memory function or fake that implements the domain contract; assert domain outcomes rather than a long sequence of mocked calls. Test the adapter separately against the real protocol or a faithful test environment. Contract tests can verify that every adapter honors shared error, idempotency, and result semantics.

Avoid designing the abstraction around what a mocking library makes convenient. The contract should remain useful in production even if the tests were removed.

## Over-application

DIP can produce severe bloat:

- interfaces with one stable implementation;
- repository abstractions that merely mirror every database method;
- mock-heavy tests coupled to call sequences;
- dependency-injection containers hiding construction and lifetime;
- factories creating objects with ordinary constructors;
- domain contracts predicting hypothetical providers;
- adapters that rename methods without isolating volatility.

Mockability alone is not enough. A pure function, local parameter, or direct integration test may be simpler.

## Review checklist

- Which code is policy, and which is an implementation detail?
- Does policy import vendor or framework types?
- Who owns the abstraction?
- Is the contract smaller and more stable than the detail?
- Is there actual volatility, variation, or isolation value?
- Could a function parameter replace an interface hierarchy?
- Are errors, transactions, and latency modeled honestly?
- Is a container making dependencies less visible?

## Guidance for agentic coding

An agent should add DIP boundaries only around demonstrated volatile or external details. It should use the narrowest domain-shaped contract, usually a function or small structural type, and assemble it explicitly. It should not create interface/implementation/factory/container stacks for one fixed class or invent provider portability that the task does not require.

## Sources

- [DIP in the Wild — Brett Schuchert](https://martinfowler.com/articles/dipInTheWild.html)
- [Architectural Principles: Dependency Inversion — Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles#dependency-inversion)
