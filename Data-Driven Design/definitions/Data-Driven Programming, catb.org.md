# Source note: Data-Driven Programming

- Author: Eric S. Raymond
- Work: *The Art of Unix Programming*, Chapter 9
- URL: https://www.catb.org/esr/writings/taoup/html/ch09s01.html
- Accessed: 2026-07-15
- Type: detailed design explanation

Data-driven programming separates code from the structures it acts upon so behavior can change by editing data rather than control flow. The source contrasts rigid hand-coded state machines with tables that expose transitions directly.

The idea applies when many cases share one algorithm and differ regularly. It should not be confused with data-oriented memory-layout design or with “data-driven” product analytics.
