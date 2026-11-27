# Research plan | A11.02.01

## Study design and independent work

Use identical complete quarters for all nested sets. Report raw covariance spectrum, rank policy, bootstrap and labeled shrinkage sensitivity; never claim an observed constant real bill or infer rejection solely from a sample bound gap.

## Required tasks

1. Derive HJ bound for excess returns and verify using simulated low-dimensional covariance.

2. Build quarterly real returns and consumption growth; compute mean/covariance, eigenvalues, maximum Sharpe and bound across nested assets (same dates).

3. Compare normalized CRRA SDF SD and bound across gamma; compute actual pricing errors E[m*x] as additional diagnostic, not infer fit from bound alone.

4. Assess sampling bias using block bootstrap and covariance conditioning/shrinkage sensitivity; separate raw sample bound from regularized estimate and compare population monotonicity with sampling behavior.

## Required exhibits

HJ bound by asset set, covariance condition numbers and uncertainty, CRRA volatility-versus-gamma plot, pricing errors table, real/nominal conversion and quarterly sample audit. Report all measures in quarterly units or transparently annualized Sharpe, not mixed frequencies.

## Robustness

Use excess returns of real bill proxy, not known constant real risk-free; bill is nominal before deflation. Singular covariance requires pseudoinverse only with range/finite bound check; distinguish numerical redundancy. Use common sample and uncertainty; larger raw sample bound may reflect overfit. Total consumption is a proxy for utility-relevant consumption; sensitivity to crises and consumption definition only if BEA series verified.

## Minimum viable thesis

Verified quarterly matched data, derivation and computation for three nested asset sets, comparison with CRRA SDF grid, uncertainty and conditioning checks. No claim of model rejection from bound gap alone without sampling inference.

## Optional extension

Construct the full HJ mean-SD frontier using gross returns and alternative SDF means, or impose nonnegative state prices via convex optimization.

## Prerequisites

SDF theory, covariance and matrix inversion, portfolio theory, elementary bootstrap and Python.

## Thesis outline

1. SDF restrictions and Sharpe ratios;

2. Hansen-Jagannathan derivation;

3. Quarterly data and portfolios;

4. Bounds and consumption SDF evidence;

5. Finite-sample and economic limitations.

## Milestones

W1-3: derive bound and confirm data; W4-6: align real returns and unit-test covariance formulas; W7-10: nested assets and CRRA comparison; W11-13: bootstrap/conditioning robustness; W14-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
