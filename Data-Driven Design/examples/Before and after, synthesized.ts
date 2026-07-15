// Before: every new status adds another branch.
function badge(status: string): string {
  if (status === "draft") return "gray";
  if (status === "review") return "blue";
  if (status === "published") return "green";
  throw new Error(`Unknown status: ${status}`);
}

// After: regular variation is visible as data, one lookup is the algorithm.
const badgeByStatus = {
  draft: "gray",
  review: "blue",
  published: "green",
} as const;

type Status = keyof typeof badgeByStatus;
const dataDrivenBadge = (status: Status) => badgeByStatus[status];

// The type derives from the same table, avoiding a second list of valid keys.
