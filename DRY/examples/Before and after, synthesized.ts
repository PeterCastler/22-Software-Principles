// Before: the free-shipping threshold is one business fact in two places.
export const shippingCost = (subtotal: number) => subtotal >= 50 ? 0 : 6;
export const shippingBanner = (subtotal: number) =>
  subtotal >= 50 ? "Free shipping" : "Shipping calculated at checkout";

// After: one authority for the changing knowledge.
const FREE_SHIPPING_MINIMUM = 50;

export const dryShippingCost = (subtotal: number) =>
  subtotal >= FREE_SHIPPING_MINIMUM ? 0 : 6;
export const dryShippingBanner = (subtotal: number) =>
  subtotal >= FREE_SHIPPING_MINIMUM
    ? "Free shipping"
    : "Shipping calculated at checkout";

// Do not merge unrelated constants merely because both currently equal 50:
const SEARCH_PAGE_SIZE = 50; // changes for a different reason
