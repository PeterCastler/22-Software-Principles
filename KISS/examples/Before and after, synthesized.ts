// Before: a strategy framework for one fixed rule.
interface DiscountStrategy {
  apply(total: number): number;
}

class ThresholdDiscount implements DiscountStrategy {
  constructor(
    private readonly threshold: number,
    private readonly rate: number,
  ) {}

  apply(total: number): number {
    return total >= this.threshold ? total * (1 - this.rate) : total;
  }
}

const strategy: DiscountStrategy = new ThresholdDiscount(100, 0.1);
export const complicatedTotal = (total: number) => strategy.apply(total);

// After: current requirements contain one stable rule and no runtime variation.
export const simpleTotal = (total: number) =>
  total >= 100 ? total * 0.9 : total;

// If a second independently changing rule actually arrives, revisit the design
// using evidence from both cases. KISS does not forbid later refactoring.
