# Unix Philosophy

## Definition

The Unix Philosophy is a family of design principles centered on small, focused programs that cooperate through simple interfaces. Doug McIlroy's classic formulation emphasizes doing one job well, producing output suitable as another program's input, trying software early, replacing clumsy parts, and using tools to amplify effort.

The philosophy is not “make every program tiny” or “everything must be text.” Its power comes from **composability**: focused components remain replaceable because they communicate through stable, general interfaces.

## Core commitments

### Do one coherent thing well

A tool should have a clear purpose and avoid absorbing every adjacent feature. “One thing” is a judgment about cohesion, not one function or verb. A compiler does many internal operations yet performs one recognizable transformation.

### Design for composition

Output should be usable by other tools, including tools not known when the program was written. Machine-facing output should avoid decoration, prompts, and unstable formatting. Inputs and outputs should use documented standards.

### Keep components replaceable

A component with a narrow contract can be tested, substituted, or discarded without rewriting the system. Replaceability supports experimentation and deletion.

### Iterate and rebuild

Working software provides evidence. Try designs early and replace awkward parts rather than preserving them because they already exist.

### Use leverage

Automate repetitive work with tools and compose existing utilities instead of implementing each capability from scratch.

## Worked example

A custom “overdue report” program might own file reading, CSV parsing, filtering, sorting, limiting, formatting, and a flag for every variation. For a controlled simple input format, a pipeline can express the work:

```sh
awk -F, '$4 == "overdue" { print $2 "," $3 }' invoices.csv |
  sort -t, -k2,2nr |
  head -n 10
```

Each stage has one role, works with streams, and can be replaced independently. If real CSV fields can contain commas or newlines, `awk -F,` is inadequate; a standards-compliant CSV parser should replace that stage. Composability does not excuse incorrect primitives.

## Modern interfaces

Text streams were historically universal because both humans and programs could inspect them. Modern systems may appropriately use:

- newline-delimited JSON;
- typed in-process values;
- stable files and standard formats;
- event streams;
- narrow HTTP or RPC contracts;
- database relations.

The relevant properties are openness, stability, inspectability, and ease of composition. Binary formats can be appropriate when performance or fidelity requires them, provided tooling and contracts remain strong.

## Command-line behavior

Unix-style tools generally benefit from:

- standard input and output support;
- data on stdout and diagnostics on stderr;
- meaningful exit statuses;
- quiet success unless output is the product;
- deterministic output where possible;
- flags that combine predictably;
- no requirement for interactive input in pipelines;
- streaming instead of loading entire inputs when practical.

## Applying the philosophy inside programs

The same ideas apply to modules and functions: accept ordinary values, return ordinary values, avoid hidden global state, keep effects at explicit boundaries, and build larger behavior by composition. Do not mechanically create a process for each responsibility; process boundaries are expensive.

## Failure modes

- fragmenting a cohesive operation into microscopic tools;
- relying on ad hoc text formats that lose types or mishandle escaping;
- pipelines with poor error propagation and observability;
- excessive process startup or serialization cost;
- adding dozens of flags until a tool becomes several programs in disguise;
- interpreting “do one thing” without considering user workflow;
- assuming small components are automatically simple when their integration is not.

Sometimes one cohesive in-process function is simpler than a shell pipeline. Sometimes a single application provides a better transaction and error boundary than many services.

## Review checklist

- Does the component have a coherent purpose?
- Can its output be consumed without scraping decoration?
- Are data and diagnostics separated?
- Is the interface stable, documented, and standard where possible?
- Can the component be replaced independently?
- Would composition be clearer than another built-in feature?
- Does fragmentation add more integration cost than it removes?
- Are input edge cases handled by an adequate parser?

## Guidance for agentic coding

An agent should favor small composable functions, standard formats, and existing tools. Command-line changes should preserve stdin/stdout/stderr and exit-code conventions. It should not build a monolithic custom utility when a short reliable composition suffices, nor split cohesive application logic into processes merely to appear Unix-like.

## Sources

- [UNIX Time-Sharing System Foreword — McIlroy, Pinson, and Tague](https://www.textbookoflinux.com/references/mcilroy1978.html)
- [The Art of Unix Programming — Basics of the Unix Philosophy](https://www.catb.org/esr/writings/taoup/html/ch01s06.html)
