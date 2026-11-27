---
title: "Optimal Rebalancing Frequency with Transaction Costs"
subtitle: "Research proposal | D04.03.01"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Frequent rebalancing improves replication in a frictionless model, but each trade consumes resources. The relevant economic decision is a finite calendar chosen according to the hedger's risk tolerance and costs, not a universal optimal frequency.

## Research question

How does the optimal discrete delta-hedging frequency depend on transaction costs, volatility, maturity and the hedger's risk tolerance? Is the optimal frequency robust to model misspecification?

## Economic mechanism

For discounted seller loss $L$, one possible declared objective is $J=\mathbb E[L]+\lambda_R\operatorname{SD}(L)$ with $\lambda_R\ge0$.

## Research design

Compare the prescribed candidate calendars on common paths. Choose the frequency on training paths for each risk-cost criterion and evaluate it unchanged on independent paths; vary costs, maturity, volatility and misspecification.

Optimize calendars only, unlike D04.03.02. Include opening and liquidation, matched initial premium and paired paths. Never select the risk criterion from final test losses.

\newpage

## Required exhibits

Worked single-path cash ledger; P&L distributions and quantiles; cost-risk frontier per cost regime; optimal frequency heatmap by c and lambda; out-of-sample table with MC confidence intervals. Discuss why an optimum is conditional rather than universal.

## Minimum viable thesis

Validated self-financing ledger, frequency grid with at least three positive cost levels, prespecified risk-cost objective, independent evaluation, and economically interpretable trade-off. The student need not discover a unique optimum at every grid point.

## Scope and feasibility

Report costs with/without liquidation to expose convention effects; use independent seeds and paired comparisons; distinguish fixed-volatility hedging from true-volatility hedging in misspecification. Check gamma exposure near expiry and tail losses. A cost-free limit should not produce a large nonzero optimal error solely from accounting bugs.

**Prerequisites:** BSM, stochastic simulation, Greeks, basic optimization and Python. No derivatives or bid-ask history required.

**Optional extension:** Compare no-trade-band hedging or a stochastic-volatility path generator; do not mix this with empirical transaction-cost estimation without suitable quotes.

## Milestones

W1-3: derive replication and discrete cash flows; W4-6: validate one-path and many-path ledger; W7-10: run cost/frequency experiment and choose on training paths; W11-13: independent evaluation and stress tests; W14-16: document and reproduce findings.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
