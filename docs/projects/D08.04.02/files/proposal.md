---
title: "Designing Cost-Constrained Tail Risk Hedges"
subtitle: "Research proposal | D08.04.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A fixed insurance budget forces choices between strike protection, quantity and surrendered upside. Protective puts, spreads and collars insure different parts of the distribution. Compare feasible structures at equal wealth across physical tail scenarios.

## Research question

For a fixed annual initial premium budget, how do a protective put, a put spread and a collar differ in expected shortfall, expected return and extreme-loss protection? Which rankings survive changes in the tail distribution and the volatility risk premium?

## Economic mechanism

With net premium $p$ and overlay payoff $H(S_T)$, $W_T=S_T+H(S_T)-pe^{rT}$ and $p\le bS_0$.

## Research design

Choose feasible contracts from the declared strike and quantity grids, price all legs under Q, then evaluate common physical GBM and negative-jump scenarios. Select any optimized design before independent test paths.

Separate single-horizon synthetic choice from historical rolling strategies. Verify equal net wealth, budget and extreme-spot payoff limits; report cost, expected return, tail protection, upside and paired uncertainty.

\newpage

## Required exhibits

Budget/payoff table, terminal wealth and ES distributions, protection-cost frontier, tail stress table, sensitivity to Q-P differences and upside cost. Confidence intervals from simulation replications or independent seed batches.

## Minimum viable thesis

Three feasible hedge structures and unhedged benchmark, explicit budget and financing, baseline and jump-tail physical distributions, cost/ES trade-off and limiting cases; results may favor different hedges by criterion.

## Scope and feasibility

Use matched initial wealth and feasible quantities, no free arbitrage from pricing choices, common random draws and explicit Q/P separation. Report budget utilization and separate severe scenarios from expected performance. Historical French returns may contextualize physical volatility but cannot establish historical option returns; no actual executable backtest is claimed.

**Prerequisites:** Vanilla option pricing, risk measures, simulation and elementary optimization. No proprietary quotes required.

**Optional extension:** Add repeated monthly roll in a fully specified joint P/Q simulation with transaction cost, or public Cboe put-protection benchmark as a separate descriptive comparison after access check.

## Milestones

W1-3: payoff and ES definitions; W4-6: implement pricing and budget constraints; W7-10: run independent scenario comparisons; W11-13: frontier and tail robustness; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
