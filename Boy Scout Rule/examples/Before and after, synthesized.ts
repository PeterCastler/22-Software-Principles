// Before: the requested change is to support a configurable timeout, but the
// touched function also has a misleading name and magic status string.
async function doIt(url: string) {
  const response = await fetch(url);
  if (response.status === 200) return response.json();
  throw new Error("failed");
}

// After: the requested behavior plus small, local clarity improvements.
const HTTP_OK = 200;

async function fetchJson(url: string, timeoutMs: number) {
  const response = await fetch(url, { signal: AbortSignal.timeout(timeoutMs) });
  if (response.status === HTTP_OK) return response.json();
  throw new Error(`Request failed with status ${response.status}`);
}

// Do not also redesign every HTTP caller in the repository without separate
// scope, evidence, and review.
