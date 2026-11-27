---
title: "Focused methods — Portfolio Choice under Expected Shortfall Constraints"
subtitle: "A08.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For loss $L=-w^\top r$, ES at confidence $\alpha$ is $\min_z[z+\mathbb E[(L-z)_+]/(1-\alpha)]$.

Introduce nonnegative slacks $u_j\geq -w^\top r_j-z$ and replace expectation by their mean; threshold unrestricted. Fractional tail mass matters. ES is not a guarantee on future losses. Compare each risk budget relative to its own equal-weight training risk. Distinguish infeasible versus failed solves; declare fallback. Use daily drift despite monthly trading, report inadmissible simulated gross returns.

## Research checks

Verify empirical ES by order statistic and direct Rockafellar-Uryasev objective; compare two-asset LP to enumerated frontier. Record solver status/runtime, prespecified fallback and feasible risk budgets. Run rolling daily scenario fit with monthly trading, actual complete calendar and paired date-block ES intervals. Large grid remains student work.
