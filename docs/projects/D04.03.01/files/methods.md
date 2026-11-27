---
title: "Focused methods — Optimal Rebalancing Frequency with Transaction Costs"
subtitle: "D04.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Self-financing with costs
Let $h_i$ denote shares after trading at $t_i$, $D_i=e^{-rt_i}$, $h_{-1}=0$ and $h_n=0$ on liquidation. For a short call with common premium $C_0$ and no dividends,
$$\begin{aligned}L={}&D_n g(S_n)-C_0-\sum_{i=0}^{n-1}h_i(D_{i+1}S_{i+1}-D_iS_i)\\&+\sum_{i=0}^n D_i cS_i|h_i-h_{i-1}|.\end{aligned}$$
Here $c$ is cost per dollar traded; ten bp is $0.001$. Liquidation is not a new hedge chosen using the realized payoff. Reconcile discounted gains and the cash ledger.

## Policy choice
Prespecify the risk criterion and candidate calendars. Evaluate mean loss, dispersion, cost and uncertainty on independent paths, retaining near ties. An optimum is conditional on the objective and feasible grid.

## Research checks

Optimize calendars only, unlike D04.03.02. Include opening and liquidation, matched initial premium and paired paths. Never select the risk criterion from final test losses.
