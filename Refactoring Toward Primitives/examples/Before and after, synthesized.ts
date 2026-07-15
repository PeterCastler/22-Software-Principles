// Before: a hand-written grouping helper owns edge cases and typing.
function groupByStatus<T extends { status: string }>(items: T[]) {
  const result: Record<string, T[]> = {};
  for (const item of items) {
    if (!result[item.status]) result[item.status] = [];
    result[item.status].push(item);
  }
  return result;
}

// After: when the runtime baseline supports it, use the language primitive.
const grouped = Object.groupBy(items, item => item.status);

// Confirm semantic differences: Object.groupBy returns a null-prototype object
// and may affect the project's runtime/polyfill requirements.
