# Research plan | D11.04.01

## Study design and independent work

Check one-period orthogonality, out-of-sample error and residual variance for zero, static, dynamic and proxy-delta hedges. Report the full-span continuous limit separately from finite-grid errors.

## Required tasks

1. Prove normal equations and Pythagorean error split.

2. Verify finite-state exact projection and rho=0.

3. Estimate conditional hedge on train paths; check out-of-sample orthogonality and variance.

4. Compare loss RMSE and tails as rho and trading frequency change.

5. Examine estimation error, full-span continuous-time limit and discretization residual at rho=1.

## Required exhibits

Residual risk versus rho, coefficient plots, error decomposition, held-out loss table and numerical convergence.

## Robustness

Identical initial capital and payoff for comparisons; no drift advantage in baseline. Finite rebalancing can leave error even at rho=1. Proxy delta is a feasible control, not the exact discrete optimum.

## Minimum viable thesis

One-period exact projection and multi-period regression with three correlations and independent test paths.

## Optional extension

Nonzero physical risk premium with explicitly derived global mean-variance hedge, or a second hedging asset.

## Prerequisites

Probability, conditional expectations, regression, Python.

## Thesis outline

1. Incomplete markets;

2. L2 projection;

3. Synthetic market;

4. Hedge comparisons;

5. Economic limits.

## Milestones

W1-3: projection; W4-6: one-step checks; W7-9: dynamic regression; W10-12: test and decomposition; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
