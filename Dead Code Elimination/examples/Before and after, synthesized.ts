// Before: an expired flag and unreachable branch still impose obligations.
const USE_LEGACY_TOTAL = false;

function total(items: Array<{ price: number }>): number {
  if (USE_LEGACY_TOTAL) {
    return items.reduce((sum, item) => sum + Math.round(item.price), 0);
  }
  return items.reduce((sum, item) => sum + item.price, 0);
}

// After rollout is verified and rollback no longer depends on the old path:
function liveTotal(items: Array<{ price: number }>): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// Also remove the flag declaration, configuration, legacy-specific tests,
// documentation, dashboards, and dependencies. Dead code has a perimeter.
