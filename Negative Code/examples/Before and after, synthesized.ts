// Before: manual normalization is long, partial, and easy to get wrong.
function slug(value: string): string {
  let result = "";
  for (const character of value.trim().toLowerCase()) {
    if (character >= "a" && character <= "z") result += character;
    else if (character === " " || character === "_") result += "-";
  }
  while (result.includes("--")) result = result.replace("--", "-");
  return result;
}

// After: delete the custom state machine in favor of direct primitives.
function smallerSlug(value: string): string {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z]+/g, "-")
    .replace(/^-|-$/g, "");
}

// This example intentionally defines ASCII-only behavior. If Unicode slugs are
// required, use a well-tested library rather than making the regex “clever.”
