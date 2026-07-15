// Before: 2 booleans and optional fields allow contradictory combinations.
type Request = {
  loading: boolean;
  failed: boolean;
  data?: string;
  error?: Error;
};

// After: each variant carries exactly the information valid for that state.
type RequestState =
  | { kind: "idle" }
  | { kind: "loading" }
  | { kind: "loaded"; data: string }
  | { kind: "failed"; error: Error };

function render(state: RequestState): string {
  switch (state.kind) {
    case "idle": return "Ready";
    case "loading": return "Loading…";
    case "loaded": return state.data;
    case "failed": return state.error.message;
  }
}

// There is no “loaded without data” or “loading and failed” value to check.
