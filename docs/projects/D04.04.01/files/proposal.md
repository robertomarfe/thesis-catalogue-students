---
title: "Deep Hedging with Transaction Costs"
subtitle: "Research proposal | D04.04.01"
---

**Derivatives · Hedging and volatility derivatives · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

With frictions, a feasible hedge can depend on time, moneyness and the existing position. A flexible neural policy may exploit this state dependence, but apparent gains can result from overfitting or unequal constraints. The project tests economic value against strong tuned benchmarks.

## Research question

Can a small neural hedging policy improve the net loss distribution of a short option relative to delta hedging and tuned no-trade bands at the same cost and risk objective?

## Economic mechanism

For discounted loss $L$ and $\eta>0$, the entropic risk criterion is $\rho_\eta(L)=\eta^{-1}\log\mathbb E[e^{\eta L}]$.

## Research design

Train the prescribed small shared policy on GBM paths; use validation paths for tuning policy and comparator bands. Evaluate frozen policies on identical independent test paths, recording optimization seeds and runtime.

The student develops the network, objective, ledger and complete comparison. Report tail loss, turnover, risk objective and stability; in-sample improvement alone is insufficient.

\newpage

## Required exhibits

Policy slices versus moneyness/position; held-out loss and turnover tables; learning curves; seed sensitivity and stress results.

## Minimum viable thesis

One ATM call, GBM, two cost levels, neural vs delta and band, independent test and ledger checks.

## Scope and feasibility

No future price input; shared information and initial premium; avoid optimizing on test paths. Include liquidation costs, separate model risk and sampling uncertainty. No claim of global optimality or empirical trading performance.

**Prerequisites:** Options, numerical simulation, optimization, basic neural networks and Python.

**Optional extension:** Heston with observable variance or a noisy past-return volatility proxy; separate information advantage from policy advantage.

## Milestones

W1-3: ledger and risk; W4-6: benchmarks; W7-9: training; W10-12: held-out stress; W13-16: reproducible code and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
