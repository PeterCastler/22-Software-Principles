# Source note: Parse, don't validate

- Author: Alexis King
- URL: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
- Accessed: 2026-07-15
- Type: originating essay for the slogan

Validation checks a property but often discards what was learned, forcing later code to check again or trust an unenforced assumption. Parsing converts less-structured input into a more precise representation, or returns an error. The result carries the proof needed by downstream operations.

The essay recommends pushing parsing toward the input boundary, using precise data structures, and strengthening argument types so functions need not handle cases callers claim are impossible.
