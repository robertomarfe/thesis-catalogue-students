# Research plan | D07.01.02

## Study design and independent work

Report initial zero PV for swaps, matched shocks and risk reduction net of exposure sign mistakes. Distinct from D07.04.02: swap DV01/key-rate hedging rather than PCA zero-bond spanning.

## Required tasks

1. Implement discount factors, par coupons, swap annuity and sign conventions; verify par instruments and cash-flow valuation.

2. Construct a fixed-face bond mix; calculate parallel DV01, convexity and key-rate exposure.

3. Solve a one-swap hedge and a two-swap least-squares key-rate hedge with predeclared notional caps; freeze notionals before next curve shock.

4. Reprice exactly under observed changes and compare unhedged and hedged shock P&L in dollars, SD, tail quantiles and residual exposures.

5. Compare linear DV01 approximation versus exact P&L across parallel, steepening and flattening scenarios.

## Required exhibits

Curve data audit, hedge ratios, P&L distributions, risk reduction by regime and shock type, sensitivity and notional tables, validated pricer.

## Robustness

Use common dates; no rolling live-position claim, carry or funding P&L. Government zero curve is not OIS or term forward curve. Label hedge as a historical shock replay using synthetic contracts. Repeat with smaller bump sizes, maturity grid and stress dates. No execution costs, collateral or basis included.

## Minimum viable thesis

Validated par valuation, signed DV01 hedge, exact shock repricing on a verified daily GSW sample and comparison of one- and two-instrument residual risk.

## Optional extension

Implement genuine rolling coupon/reset schedule with carry and aging, or compare euro government proxy curves; verify separate curves before claiming swap-market evidence.

## Prerequisites

Fixed-income pricing, linear algebra, Python and basic portfolio risk analysis.

## Thesis outline

1. Bond and swap valuation;

2. Duration and key-rate hedging;

3. Historical curve shock design;

4. Hedging results and residual risks;

5. Practical limitations.

## Milestones

W1-3: study curve/swap conventions; W4-6: acquire GSW and validate pricer; W7-10: compute hedge ratios and shock P&L; W11-13: stress and sensitivity; W14-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
