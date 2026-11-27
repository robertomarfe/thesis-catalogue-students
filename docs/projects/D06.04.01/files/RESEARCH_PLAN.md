# Research plan | D06.04.01

## Study design and independent work

Keep discount and marginal inputs fixed; test PSD before every bump. Examine different strikes and volatilities rather than extrapolating one correlation sign. Distinguish tail dependence from linear correlation.

## Required tasks

1. Validate correlation matrix and single-asset/perfect-correlation limits.

2. Price both contracts and geometric basket benchmark with MC intervals.

3. Map price versus correlation, maturity and volatility heterogeneity.

4. Estimate correlation sensitivity by paired finite differences with PSD checks and compare tail event probabilities.

5. Stress dependence using a common-shock lognormal mixture with matched marginal distributions, clearly separate correlation from higher-order dependence.

## Required exhibits

Payoff definitions; benchmark checks; correlation-price curves; sensitivity and uncertainty table; joint-tail diagnostics.

## Robustness

Do not infer correlation sensitivity from a single strike or use invalid correlation matrices. Compare same marginal prices and maturity; price versus risk exposure distinction. Dependence mixture optional if exact marginal matching verified.

## Minimum viable thesis

Two assets, exact MC, both payoffs, five admissible correlations, perfect-correlation check and paired error bars.

## Optional extension

Apply results to a stylized worst-of capital-protected note with contract specified separately.

## Prerequisites

Multivariate normal distribution, risk-neutral pricing, Monte Carlo, Python.

## Thesis outline

1. Multi-asset claims;

2. Dependence and pricing;

3. MC design;

4. Correlation risk;

5. Structured-product implications.

## Milestones

W1-3: payoff and model; W4-6: MC/benchmarks; W7-9: correlation grid; W10-12: sensitivity and stress; W13-16: document.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
