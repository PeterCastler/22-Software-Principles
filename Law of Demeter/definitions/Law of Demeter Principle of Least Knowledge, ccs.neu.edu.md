# Source note: Law of Demeter — Principle of Least Knowledge

- Maintainer: Karl Lieberherr, Northeastern University
- URL: https://www.ccs.neu.edu/home/lieber/LoD.html
- Accessed: 2026-07-15
- Type: original research-group resource

The Law of Demeter, also called the Principle of Least Knowledge, limits a method to close collaborators rather than the internal object graph behind them. The resource points to Lieberherr and Holland's 1989 paper and reports practical use in JPL systems.

The goal is lower structural coupling. The familiar “one dot” heuristic is only a warning sign; fluent APIs, local value transformations, and collection chains are not necessarily violations.
