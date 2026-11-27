---
title: "Variance Reduction in Monte Carlo Option Pricing"
subtitle: "Research proposal | D05.01.01"
---

**Derivatives · Numerical pricing and exotics · Level 1/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Monte Carlo pricing is attractive for path-dependent claims, but a small standard error need not imply computational efficiency. Variance reduction changes the sampling procedure rather than the pricing model. The project asks which methods save computation for the same payoff and why the gains depend on moneyness and averaging.

## Research question

Which of antithetic variates, control variates and their combination yields the best pricing precision per unit runtime for European and discretely monitored Asian calls? Does the efficiency ranking depend on moneyness?

## Economic mechanism

For discounted payoff $X$ and control $Y$ of known mean $\mu_Y$, the estimator is $\bar X-b(\bar Y-\mu_Y)$. The coefficient and pilot costs must be accounted for.

## Research design

Compare plain, antithetic, control-variate and combined estimators for European and Asian calls at three strikes and four path budgets. Use exact GBM at the contractual fixings and independent replications, including pilot cost.

Freeze the payoff, seed and timing protocol. The combined estimator addresses the full question even when the MVT requires only two methods. Do not label a high-budget arithmetic reference exact.

\newpage

## Required exhibits

Benchmark validation table; convergence plot; precision/cost table (standard error, RMSE, runtime, coverage); variance reduction ratio by strike; reproducible timing log. Explain why low-variance or rare-payoff cases can make relative ratios unstable.

## Minimum viable thesis

Two payoffs, plain MC plus two variance-reduction methods, independent replications, known analytic European benchmark, and a timing-normalized comparison. A ranking reversal across strikes is a useful finding.

## Scope and feasibility

Use independent random streams; exclude compilation warmup consistently but include sampling and coefficient estimation; repeat timing to reduce jitter. Confirm antithetic samples are not treated as independent observations. Test alternative sigma and number of monitoring dates; do not attribute discretization error to exact GBM at contractual dates.

**Prerequisites:** Probability, risk-neutral valuation, basic statistics, Python vectorization. Suitable for a student developing quantitative programming skills.

**Optional extension:** Randomized quasi-Monte Carlo with multiple independent scrambles or conditional Monte Carlo; measure uncertainty over scrambles, not deterministic sequence points.

## Milestones

W1-3: derive MC and analytic controls; W4-6: implement and validate pricing; W7-10: build repeated budget-controlled experiment; W11-13: timing/coverage and robustness; W14-16: write and regenerate outputs.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
