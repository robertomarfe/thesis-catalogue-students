# Research plan | D01.04.02

## Study design and independent work

Validate the covariance and cross-covariance before simulating prices. Keep the initial variance curve and other parameters fixed across H. Separate grid refinement, sampling uncertainty and finite-maturity asymptotic bias, with a Brownian-kernel reference.

## Required tasks

1. Verify Gaussian kernel covariance and E[v_t]=xi0(t), H=.5 limit.

2. Price short-dated calls using common random numbers and independent finer-grid checks.

3. Recover IV and paired finite-difference ATM skew with MC uncertainty.

4. Estimate log absolute skew versus log T over predeclared short-maturity subsets; compare H-.5 as asymptotic prediction, not finite-T equality.

5. Study eta/rho, grid refinement and strike-window sensitivity.

## Required exhibits

Variance-path statistics, short-tenor smiles, log-log skew and slope uncertainty, martingale and runtime diagnostics.

## Robustness

Small option-price errors inflate IV derivative error. Do not claim empirical roughness estimation; synthetic H is known. Compare equal variance curves and rho; finite-T asymptotic bias, discretization and MC error must be reported separately.

## Minimum viable thesis

Two H values including .5, validated Gaussian kernel, 4+ maturities with error bars, short-skew scaling and convergence caveats.

## Optional extension

Compare a Markovian multifactor exponential-kernel approximation with the rough benchmark under matched error budget.

## Prerequisites

Gaussian processes, stochastic calculus, option pricing, MC and numerical linear algebra.

## Thesis outline

1. Roughness and option skew;

2. Rough Bergomi;

3. Kernel simulation and validation;

4. Short-time scaling;

5. Limits.

## Milestones

W1-3: Volterra kernel and asymptotics; W4-6: exact covariance and simulation; W7-9: price/skew panels; W10-12: grid and MC tests; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
