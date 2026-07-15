// Before: checkout knows the customer's wallet and payment implementation graph.
function charge(order: any) {
  order.customer.account.wallet.paymentMethod.charge(order.total);
}

// After: collaborate with the nearest object using a domain-level message.
class Customer {
  constructor(private readonly payments: PaymentService) {}

  pay(amount: number) {
    return this.payments.charge(amount);
  }
}

function checkout(order: { customer: Customer; total: number }) {
  return order.customer.pay(order.total);
}

// The object graph may still exist internally, but callers do not depend on it.
