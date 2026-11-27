---
title: "Mean-Variance Optimization and the Cost of Estimation Error"
subtitle: "Research proposal | A08.01.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Optimization amplifies estimation error into unstable allocations. A known-moment experiment separates the effects of mean and covariance estimation before historical evaluation.

## Research question

How much does estimation error in expected returns and covariance reduce out-of-sample mean-variance portfolio performance relative to equal weights and minimum variance?

## Economic mechanism

Maximize $U(w)=w^\top\mu-\gamma w^\top\Sigma w/2$ on the long-only simplex using monthly excess means and covariance.

## Research design

10 assets, 24/60/120/240 months, 1,000 paired replications; French 10 industries, 60/120-month histories, common origins, fixed gamma and cost menu.

Run paired known-moment cells: true/estimated mean crossed with true/estimated covariance, same random draws and out-of-sample returns, verify oracle objective and feasibility. For actual data record long-only weights, exact OOS dates, drifted trades, net wealth and CE units; date blocks and estimation uncertainty; report failed cells.

\newpage

## Required exhibits

Oracle regret plots, simulated weight dispersion, historical portfolio weight/wealth paths, risk/CE and turnover table, optimization failure diagnostics and reproducible timestamp ledger.

## Minimum viable thesis

Known-moment simulation isolating mean/covariance error, matched rolling 1/N, GMV and mean-variance backtest, weight stability and CE comparison with uncertainty.

## Scope and feasibility

No use of future returns in estimation or tuning. Use one-way traded notional convention explicitly (if turnover=0.5*sum absolute trades, convert costs accordingly). Risky portfolios use total returns; same cost schedule and rebalance. Published portfolio returns do not establish implementable net strategy returns. Distinguish mean estimation from covariance shrinkage thesis A08.01.02.

**Prerequisites:** Portfolio theory, covariance estimation, convex optimization and Python SciPy/cvxpy.

**Optional extension:** Compare shrinkage of mean toward common mean, without turning thesis into a covariance-shrinkage comparison.

## Milestones

W1-3: portfolio theory and optimizer; W4-6: clean returns and validate weights; W7-9: oracle simulations; W10-12: rolling backtest; W13-16: costs, uncertainty and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
