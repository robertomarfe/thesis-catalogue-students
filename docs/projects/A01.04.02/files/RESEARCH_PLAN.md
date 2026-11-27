# Research plan | A01.04.02

## Study design and independent work

Freeze factor dimensions, weights, means and model selection before the test. Audit date and asset holdouts separately, report factor return scaling and rank, and retain common pricing moments. Optional OSAP alternative requires its own access verification.

## Required tasks

1. Audit excess returns, common dates and covariance.

2. Fit PCs using training assets only, verify orthogonality and sign invariance.

3. Fit each pricing model on training assets and dates.

4. Evaluate same-asset future and disjoint-portfolio future pricing errors, alongside variance explained.

5. Compare rolling re-estimation, correlation PCA and factor dimension sensitivity using training-only rules.

## Required exhibits

Eigenvalue plot, factor correlations, held-out pricing RMSE/alpha table, split audit and stability.

## Robustness

PC weights do not identify economic shocks; common underlying equities prevent independent-security interpretation. FF3 versus FF5 are not automatically nested. Same test dates/assets and dimensions, no future data leakage.

## Minimum viable thesis

PC3 and FF3 on French panels, one frozen date/asset holdout and pricing versus covariance comparison.

## Optional extension

OSAP training universe and sparse statistical factors; preserve independent validation dates and candidate selection.

## Prerequisites

Linear algebra, factor models, regression, Python.

## Thesis outline

1. Factor models;

2. PCA and pricing;

3. Data/splits;

4. Held-out comparisons;

5. Limits.

## Milestones

W1-3: PCA and data; W4-6: factor construction; W7-9: pricing fit; W10-12: evaluation; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
