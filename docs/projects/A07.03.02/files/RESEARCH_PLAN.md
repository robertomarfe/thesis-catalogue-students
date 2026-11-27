# Research plan | A07.03.02

## Study design and independent work

Prespecify pair labels and thresholds; do not search over pairs to obtain significant tail dependence. Report sparse counts and uncertainty, and distinguish the conditioning direction in finite samples.

## Required tasks

1. Simulate Gaussian and t copulas with equal rank correlation; validate conditional co-exceedance.

2. Construct daily aligned returns, report marginals and sample tail counts.

3. Fit Gaussian/t via pseudo-likelihood on training data; compare held-out empirical and predicted co-exceedances and joint-tail calibration.

4. Use paired block bootstrap for finite-q intervals and compare upper vs lower tails.

5. Refit on standardized GARCH residuals or volatility-scaled returns to assess marginal heteroskedasticity contribution.

## Required exhibits

Copula scatter and tail plots, finite-q dependence table with counts/intervals, held-out calibration and sensitivity to marginal scaling.

## Robustness

Do not infer asymptotic tail dependence from a single threshold. Keep short-long factor returns distinct from fully invested portfolios. Serial dependence and shared stocks limit inference; avoid multiple pair searches for significance.

## Minimum viable thesis

Three industry pairs and two market-factor pairs, Gaussian/t copula comparison, empirical co-exceedance and uncertainty at .05/.10. Distinct from coskewness pricing A07.03.01.

## Optional extension

Rolling copula parameters or asymmetric Clayton/Gumbel copulas with held-out comparison.

## Prerequisites

Probability, rank statistics, likelihood, time-series bootstrap, Python.

## Thesis outline

1. Diversification and tails;

2. Copula theory;

3. Data and design;

4. Tail dependence estimates;

5. Risk implications.

## Milestones

W1-3: copulas and simulations; W4-6: aligned data; W7-9: estimation; W10-12: tail validation; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
