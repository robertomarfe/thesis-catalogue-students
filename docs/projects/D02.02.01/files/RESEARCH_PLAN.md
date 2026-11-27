# Research plan | D02.02.01

## Study design and independent work

Freeze skew regimes, sparsity, noise scales and held-out wing strikes. Compare equal computational budgets and report invalid inversions, failed fits and finite-grid arbitrage rather than claiming smoothness implies absence of arbitrage.

## Required tasks

1. Derive SVI and SABR parameter roles; implement stable ATM evaluation and Black inversion, with price round-trip checks.

2. Fit each slice by multistart, comparing IV RMSE and price loss normalized by forward; report convergence, active bounds and parameter dispersion.

3. Evaluate held-out strikes against clean truth; distinguish interpolation from wing extrapolation.

4. On a dense grid calculate monotonicity, convexity and calendar violations in undiscounted forward-normalized call prices; compare fit accuracy conditional on admissibility.

5. Repeat under quote sparsity/noise and maturities, retaining failed fits as outcomes rather than silently deleting them.

## Required exhibits

True versus fitted smile panels, held-out error distributions in vol points and price units, parameter stability and optimizer failure tables, butterfly/calendar diagnostic heatmaps and timing. A reproducible synthetic quote generator and frozen train/test splits.

## Robustness

Use a common finite strike domain, tolerances and optimizer budget; ensure total variance positive, forward ATM limits and put-call parity. Distinguish grid-based diagnostics from global arbitrage guarantees. Include price weighting sensitivity and one alternative Heston parameter set never used for tuning. No inference about actual market fitting performance from synthetic quotes alone.

## Minimum viable thesis

Two calibrated smile families, verified pricing reference, at least two maturities and skew regimes, sparse/noisy train versus untouched test comparisons, explicit arbitrage and failure diagnostics. No need for a globally arbitrage-free surface or live market data.

## Optional extension

Implement SSVI cross-maturity constraints or repeat with a legally accessible dated option chain; state data provenance and compare with the synthetic experiment rather than conflating them.

## Prerequisites

Black pricing, stochastic calculus, numerical optimization and Python SciPy. Familiarity with Heston characteristic functions helpful; no option database required.

## Thesis outline

1. Implied volatility and static arbitrage;

2. SVI and SABR approximations;

3. Synthetic market and calibration design;

4. Accuracy, stability and arbitrage results;

5. Economic and implementation limitations.

## Milestones

W1-3: derive smile parametrizations and select scenarios; W4-6: implement and test pricing/inversion and optimizers; W7-10: run frozen calibration and held-out experiments; W11-13: robustness and diagnostics; W14-16: interpret, document and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
