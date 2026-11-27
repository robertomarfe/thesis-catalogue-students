# Research plan | A08.02.01

## Required tasks

1. Derive Gaussian posterior and validate zero-innovation/no-view limits on a two-asset example.

2. Plot posterior mean and weight response to view confidence and conflicts using one historical origin.

3. Implement monthly rolling allocations with same covariance, risk aversion and constraints; calculate returns after drift-adjusted rebalancing.

4. Compare volatility, Sharpe, certainty equivalent, concentration and turnover; add prespecified 10/25 bp turnover costs.

5. Use paired block bootstrap and alternative view definitions chosen before holdout; vary tau at a prespecified origin under a fixed Omega anchor, not as a distinct effect under proportional Omega. Show algebraically and numerically that tau cancels from the posterior mean when Omega is proportional to tau. At one prespecified origin vary tau separately using Omega anchored at tau_ref=0.05; keep the prior mean, return covariance, risk aversion and views fixed. This is sensitivity, not identification of true parameters.

## Required exhibits

Posterior diagnostics, confidence/weight curves, portfolio performance and turnover tables, view sensitivity and reproducible allocation code. Proportional versus anchored Omega sensitivity curves, alongside rolling confidence and cost-adjusted performance comparisons.

## Robustness

View-generating rule is not validated private information. Prior/reference weights not market-cap equilibrium. Use no future data, consistent return units and positive-definite covariance. Report gross and cost-adjusted performance, including worse-than-benchmark cases.

## Minimum viable thesis

Validated posterior, one relative-view pair, at least three confidence settings and long-only rolling comparison with prior/equal/sample-mean benchmarks; show tau invariance under proportional Omega and a separate prior-strength sensitivity at one prespecified origin with Omega anchored at a fixed tau reference. Keep the return covariance and risk aversion fixed in mean comparisons.

## Optional extension

Use predictive covariance or a separately justified macro view with release timing; compare with robust optimization (A08.02.02).

## Prerequisites

Multivariate normal distributions, portfolio optimization, matrix algebra and Python.

## Thesis outline

1. Estimation risk and Bayesian allocation;

2. Black-Litterman derivation;

3. Data, views and constraints;

4. Posterior and backtest;

5. Sensitivity and limitations.

## Milestones

W1-3: posterior derivation; W4-6: portfolio panel and unit tests; W7-9: rolling optimizer; W10-12: costs and sensitivity; W13-16: interpretation and writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
