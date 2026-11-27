# Research plan | D07.04.02

## Study design and independent work

Do not treat physical PCA loadings as risk-neutral parameters. Unlike D07.01.02, compare statistical factor spanning with zero-bond hedges rather than single-curve swap DV01.

## Required tasks

1. Estimate one/two/three PCA factors on training windows and align signs; document loadings and out-of-sample scores.

2. Solve exposure-matching hedges; compare unhedged, parallel DV01 and first-factor alternatives.

3. Reprice each portfolio under next observed curve shock at fixed maturities; report residual SD, tail loss and variance reduction.

4. Diagnose hedge matrix condition numbers, gross notionals and periods of hedge instability; compare bounded least-squares hedge.

5. Repeat using alternate hedge tenors fixed before evaluation and separate slope stress scenarios.

## Required exhibits

Factor loading plots, hedge notional and conditioning diagnostics, residual P&L and variance reduction table, parallel/twist shock scenarios.

## Robustness

Yield curves are fitted and revised; basis and liquidity excluded. No swap, carry, roll, margin or tradable performance claim. Compare identical target and shock samples. A second factor need not improve held-out risk when estimated.

## Minimum viable thesis

GSW panel, rolling PCA, one- and two-factor zero-bond hedges, held-out shock repricing and notional/condition diagnostics. Distinct from D07.01.02, which focuses on swap DV01.

## Optional extension

Use coupon-bond cash flows or a two-factor Gaussian model with separately specified Q parameters; repeat with ECB curves.

## Prerequisites

Fixed income, linear algebra, PCA, Python and regression.

## Thesis outline

1. Curve risk and hedge design;

2. Factor estimation and sensitivities;

3. Data and fixed-maturity shocks;

4. Hedge effectiveness;

5. Conditioning and limitations.

## Milestones

W1-3: PCA and duration; W4-6: curve acquisition and repricing; W7-9: hedge optimization; W10-12: held-out and stress tests; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
