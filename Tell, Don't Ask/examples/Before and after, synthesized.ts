// Before: callers extract state and duplicate the withdrawal policy.
class AskedAccount {
  constructor(public balance: number) {}
}

function withdraw(account: AskedAccount, amount: number) {
  if (account.balance < amount) throw new Error("Insufficient funds");
  account.balance -= amount;
}

// After: the account owns the invariant and exposes a domain operation.
class Account {
  constructor(private balance: number) {}

  withdraw(amount: number): void {
    if (amount <= 0) throw new Error("Amount must be positive");
    if (this.balance < amount) throw new Error("Insufficient funds");
    this.balance -= amount;
  }

  currentBalance(): number { return this.balance; } // Queries are still valid.
}
