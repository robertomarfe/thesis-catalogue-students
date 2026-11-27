# Research plan | A05.03.02

## Study design and independent work

Do not infer a structural factor from a good in-sample fit. Report fixed and expanding results separately, with actual eligible label counts and stability intervals.

## Required tasks

1. Verify zero/forward/holding-return units and label calendar.

2. Fit common forward factor and reconstruct training loadings.

3. Compare frozen and expanding forecasts at 2-5y with OOS R2 and paired loss differences.

4. Plot rolling weight shape and maturity-specific performance by regime.

5. Use HAC at least 11 monthly lags and common-date blocks; annual nonoverlap and ridge sensitivity.

## Required exhibits

Forward-weight plot, maturity/regime loss table, forecast paths, overlap audit and robustness.

## Robustness

Fitted yields and overlapping returns imply measurement and inference caveats. No causal claim or real-time vintage guarantee. Distinct from A05.03.01: focus on common cross-maturity factor, weight stability and transfer rather than general forward predictability.

## Minimum viable thesis

One common factor, four maturities, historical-mean and slope benchmarks, fixed holdout and overlap-aware inference.

## Optional extension

Compare survey rate expectations or add higher maturities using fixed factor learned on 2-5y only.

## Prerequisites

Fixed income, time-series regression, Python.

## Thesis outline

1. Bond excess returns;

2. Common forward factor;

3. Data and timing;

4. Cross-maturity/regime transfer;

5. Limits.

## Milestones

W1-3: curves and formulas; W4-6: factor fit; W7-9: frozen/expanding evaluation; W10-12: regimes and inference; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
