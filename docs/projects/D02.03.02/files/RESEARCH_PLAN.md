# Research plan | D02.03.02

## Study design and independent work

Use normalized strikes and identical forward inputs before assessing calendars. Distinguish observed masks, withheld truth and artificial tail anchors; check between-node restrictions and report solver slacks and adjustment cost.

## Required tasks

1. Derive normalized conditions and show numerical counterexample to IV-level monotonicity.

2. Generate clean and noisy panels; quantify constraint violations by type and magnitude.

3. Fit unconstrained and joint constrained prices on identical observed cells; invert to IV only within strict BSM bounds.

4. Compare weighted fit, held-out errors and recovered total-variance term structures over a grid; test interpolation between nodes.

5. Repeat across noise scales, sparse expiries and tail choices; distinguish objective trade-off from improved recovery of noiseless prices.

## Required exhibits

Quote and fit surfaces, violation heatmaps, residuals and held-out RMSE, constraint slack/solver status and interpolation diagnostics.

## Robustness

Use common x-grid and explicit convex-order assumptions. A finite grid proof is not a claim about arbitrary extrapolation; test tail sensitivity and do not infer a smooth risk-neutral density from piecewise-linear prices. Unlike D02.03.01, enforce consistency jointly across maturities.

## Minimum viable thesis

One clean truth, three noise levels, unconstrained versus jointly constrained fits on five maturities, checked constraints and held-out comparisons.

## Optional extension

Fit SSVI with sufficient no-arbitrage parameter restrictions and compare computational cost and wing behavior with the constrained grid.

## Prerequisites

BSM and implied volatility, convexity, constrained optimization, numerical Python.

## Thesis outline

1. Implied volatility and calendar arbitrage;

2. Normalization and convex order;

3. Constrained surface estimation;

4. Fit and arbitrage diagnostics;

5. Limits of interpolation.

## Milestones

W1-3: normalized pricing restrictions; W4-6: quote generator and tests; W7-9: constrained optimizer; W10-12: held-out/noise study; W13-16: interpolation audit and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
