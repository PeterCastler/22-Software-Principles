# Source note: LLVM's Analysis and Transform Passes

- Publisher: LLVM Project
- URL: https://llvm.org/docs/Passes.html#dce-dead-code-elimination
- Accessed: 2026-07-15
- Type: canonical compiler documentation

LLVM distinguishes several forms of dead code: unused instructions, unreachable globals, dead arguments, stores whose values cannot matter, and loops with no relevant effect. Basic DCE removes an instruction and then rechecks its inputs, because deletion can expose more dead instructions.

Source-level maintenance uses the same liveness idea but has a broader contract: reflection, public APIs, feature rollout, external callers, and operational procedures can make apparently unused code live.
