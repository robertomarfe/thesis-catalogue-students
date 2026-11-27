# Research plan | D06.04.02

## Study design and independent work

Check the discounted domestic stock martingale and currency units. Hold contractual conversion fixed for delta. Validate random conversion by numeraire invariance; do not use physical correlation as risk-neutral calibration.

## Required tasks

1. Derive drift and pricing identity, specify currency units.

2. Verify domestic martingale for XS and random-conversion benchmark.

3. Check sigma_X=0/rho=0 and deterministic FX carry conventions.

4. Compute quanto price, delta and correlation sensitivity across grid with MC confidence intervals.

5. Stress reversed quote with correct numeraire/drift transformation; distinguish fixed conversion from FX-hedged foreign position. For each FX-volatility and correlation pair, compute analytic, central-bump and pathwise or independent Monte Carlo spot delta with FX spot and contractual conversion fixed. Match the spot-converted foreign option in domestic units.

## Required exhibits

Price and delta curves, quanto adjustment heatmap, domestic/foreign pricing parity and MC error table. Spot-delta comparison in common domestic currency per unit of foreign spot, including numerical validation.

## Robustness

Zero correlation removes drift correction, not discount or fixed-versus-random conversion differences. Reversing X changes sign of diffusion and measure, not just labels. No observed quanto prices; no P correlations used as Q calibration.

## Minimum viable thesis

Analytic and Monte Carlo quanto call prices and spot deltas for two FX volatilities and three equity–FX correlations at one maturity; validate the analytic spot delta by a central bump and a pathwise or independently simulated estimate, holding the fixed conversion rate and FX spot fixed. Include the random-conversion control and the matched spot-converted foreign option price and delta.

## Optional extension

Quanto put or basket under stochastic correlations and rate scenarios, retaining consistent currency ledger.

## Prerequisites

Ito calculus, BSM, change of numeraire, Python.

## Thesis outline

1. FX conventions;

2. Numeraire and drift;

3. Pricing and tests;

4. Sensitivities;

5. Limits.

## Milestones

W1-3: currency and measure; W4-6: formulas and MC; W7-9: parity checks; W10-12: sensitivity; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
