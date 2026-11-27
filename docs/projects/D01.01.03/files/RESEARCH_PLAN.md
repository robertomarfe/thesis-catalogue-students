# Research plan | D01.01.03

## Study design and independent work

Match log variance and forward before reporting skew or kurtosis. Include a symmetric variance mixture, an asymmetric location mixture and its mirror. Use the same strike coordinates and display the actual moments alongside the smile; the arithmetic variance match is a robustness exercise.

## Required tasks

1. Compute analytic mean, variance, skewness and excess kurtosis; verify forward equality and put-call parity.

2. Compare call/put prices and invert BSM implied vol under arbitrage bounds.

3. Relate skew direction to IV skew and symmetric heavy tails to wings, holding log variance fixed.

4. Vary mixtures with same first two moments; attempt matching skew/kurtosis numerically with alternative mixtures to illustrate remaining nonidentification.

5. Check MC precision, strike-grid convexity and sensitivity to matching terminal simple-return variance instead of log variance.

## Required exhibits

Density and moment tables, option price differences, IV smiles, skew/wing metrics and analytic/MC diagnostics.

## Robustness

Distributions are terminal Q marginals, not dynamic hedging models; maturity-by-maturity construction need not be calendar-arbitrage-free. Do not infer Q tails from P returns. IV inversions near price bounds can be unstable; use explicit tolerance and flags. Cumulants are descriptive, not sufficient statistics for all strikes.

## Minimum viable thesis

At one maturity: Gaussian and at least three mixture cases, exact forward/log variance matches, analytic pricing, no-arbitrage checks and smile comparisons. Distinct from D01.01.01 sensitivities and D01.01.02 dynamic hedging.

## Optional extension

Use a martingale jump-diffusion over all maturities to study how skew and kurtosis vary jointly with maturity.

## Prerequisites

Probability, lognormal pricing, numerical root finding and Python.

## Thesis outline

1. Risk-neutral distributions and moments;

2. Mixture construction and option values;

3. Validation;

4. Smile and tail sensitivities;

5. Identification limitations.

## Milestones

W1-3: Q moments and pricing; W4-6: construct mixtures and validate prices; W7-9: smile analysis; W10-12: alternate matching and MC checks; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
