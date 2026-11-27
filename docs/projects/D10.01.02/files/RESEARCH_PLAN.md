# Research plan | D10.01.02

## Required tasks

1. Derive closed-form Gaussian expectation and check deterministic-yield limit.

2. Validate analytical prices against MC confidence intervals for each maturity.

3. Plot backwardation/contango regimes and quantify the sensitivity of log forward to spot and delta.

4. Compute covariance of changes across maturities under specified Q dynamics; separate spot level and convenience-yield slope shocks.

5. Compare a constant-carry model at the same initial spot and short forward, and examine long-maturity behavior.

## Required exhibits

Forward curve families, sensitivity term structures, covariance heatmaps, analytic/MC error table and regime interpretation.

## Robustness

Synthetic positive lognormal spot excludes negative-price episodes, delivery constraints and seasonality. Q dynamics do not identify physical risk premia. Convenience yield is not recoverable from spot history alone. No observed futures calibration or roll strategy claim.

## Minimum viable thesis

Derivation, analytic implementation, MC check, at least three convenience-yield states, two persistence values and constant-carry benchmark.

## Optional extension

Fit a two-factor state-space model only if a licensed contract-level futures panel becomes available; public EIA spot can contextualize levels but cannot validate curves.

## Prerequisites

Stochastic calculus, Gaussian processes, derivatives and Python.

## Thesis outline

1. Storage economics and cost of carry;

2. Two-factor risk-neutral model;

3. Solution and simulation;

4. Curve shapes and risks;

5. Economic limitations.

## Milestones

W1-3: theory and derivations; W4-6: analytic curves and simulator; W7-9: parameter sensitivities; W10-12: numerical checks and covariance; W13-16: interpretation and writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
