# Research plan | D10.02.01

## Study design and independent work

Verify common observed endpoints, barrel units, no forward fill and past-only estimation at both horizons. Report basis changes, held-out risk reduction and negative results.

## Required tasks

1. Align prices, inspect nonpositive quotes and gaps, plot WTI-Brent basis and correlation.

2. Derive the hedge ratio in dollars per barrel and test zero and unit-ratio benchmarks.

3. Estimate rolling covariance ratios from past observations only; compare unrestricted and clipped [0,2] ratios.

4. Evaluate OOS mean, SD, variance reduction, downside quantiles and hedge-ratio turnover at each horizon.

5. Assess crisis sensitivity, including 2020, with paired block bootstrap and no deletion of unfavorable observations from the baseline.

## Required exhibits

Aligned price panel, basis and hedge ratio plots, in-sample versus OOS variance reduction, regime and horizon tables, discussion of physical basis and implementation gaps.

## Robustness

Never treat Brent spot as a traded WTI futures contract; no roll return, margin or funding claim. Use price changes, not logs, as primary specification; handle date matching and endpoint holiday gaps explicitly. Report negative OOS hedge effectiveness if found.

## Minimum viable thesis

Two spot series, two horizons, rolling minimum-variance and unit hedge benchmarks, honest held-out variance reduction and basis diagnostics.

## Optional extension

If actual contract-level futures settlements become available, specify expiry, roll timing, contract size and collateral before a separate hedge evaluation.

## Prerequisites

Derivatives fundamentals, covariance and regression, basic time series and Python.

## Thesis outline

1. Commodity price and basis risk;

2. Minimum-variance hedging;

3. Spot data and proxy design;

4. Hedge-ratio dynamics and effectiveness;

5. Limitations and futures extension.

## Milestones

W1-3: hedge theory and units; W4-6: align oil prices and construct changes; W7-9: fit rolling hedges; W10-12: holdout and regime tests; W13-16: inference, interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
