# Research plan | A05.02.02

## Study design and independent work

Separate reconstruction from forecasting. Near tied eigenvalues, use subspace comparisons rather than interpreting a particular eigenvector as an economic structural shock.

## Required tasks

1. Audit fitted-curve definitions, maturity and date alignment; plot level/slope series.

2. Estimate PCA on levels and changes, plot loadings and explained variance.

3. Compare held-out reconstruction with 1/2/3 factors and fixed training basis; this is compression, not forecast.

4. Quantify rolling loading/subspace changes via principal angles and bootstrap covariance variability; align signs consistently.

5. Compare correlation PCA, 2-10 year grid and subperiods; discuss ECB AAA issuer composition versus US sovereign credit.

## Required exhibits

Curve comparison, scree and loading panels, held-out RMSE by maturity, principal-angle stability and sensitivity table.

## Robustness

GSW and ECB curves are model-fitted smooth yields, not individual bond prices. PCA dimensionality partly reflects fitting methodology. Different currencies, issuer composition and negative yields complicate interpretation. No silent interpolation or treating same-date reconstruction as prediction.

## Minimum viable thesis

Common US/euro area grid, PCA on levels and changes, fixed-basis held-out reconstruction and stability comparison. Distinct from A05.02.01 forecasting and A05.01.02 model restrictions.

## Optional extension

Compare DNS fixed loadings or principal components of forward curves, with additional date/grid checks.

## Prerequisites

Bond yields, covariance, eigenvectors, basic time series and Python.

## Thesis outline

1. Yield-curve risk factors;

2. PCA and data definitions;

3. Cross-region comparison;

4. Stability and reconstruction;

5. Limitations.

## Milestones

W1-3: curve definitions and PCA; W4-6: acquire/align series; W7-9: level/change analysis; W10-12: held-out and robustness; W13-16: report.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
