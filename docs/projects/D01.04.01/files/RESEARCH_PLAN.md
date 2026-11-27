# Research plan | D01.04.01

## Required tasks

1. Derive kappa, martingale adjustment and cumulants; check nu->0 limit.

2. Implement conditional-normal option integrals and independent CF/MC reference.

3. Check put-call parity, price monotonicity, convexity and implied-volatility inversion.

4. Compare strike and maturity behavior at fixed variance and forward; quantify skew/kurtosis versus IV.

5. Compare numerical error and cost under alternative tail parameters and maturities. For the required Merton case, use a common forward and annual log-return variance with VG and BSM; validate the Poisson-mixture price independently.

## Required exhibits

Smile and cumulant panels, price/reference errors, convergence and runtime table, parameter-domain diagnostics. Matched-variance Merton prices and convergence evidence at two maturities and three or more log-moneyness points.

## Robustness

Do not match a fourth moment when the relevant moment does not exist; enforce damping-domain conditions if using Fourier inversion. Inactive or ill-conditioned IV tails should be flagged. Synthetic panels are not empirical calibration.

## Minimum viable thesis

VG, Gaussian and one finite-activity Merton benchmark with common forward and annual log-return variance at two maturities and at least three forward log-moneyness points; one independent pricing reference for each non-Gaussian model, martingale and put-call parity checks, and comparative smile and convergence analysis.

## Optional extension

Add NIG or CGMY with valid exponential moments and compare tail behavior under common moment restrictions.

## Prerequisites

Characteristic functions, stochastic processes, option pricing, quadrature.

## Thesis outline

1. Levy processes;

2. Exponential martingale pricing;

3. VG mixture and reference;

4. Surface comparisons;

5. Limitations.

## Milestones

W1-3: Levy exponents; W4-6: pricing and limits; W7-9: smile experiments; W10-12: error/tail robustness; W13-16: writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
