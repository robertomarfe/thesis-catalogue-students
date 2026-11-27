# Research plan | A01.04.01

## Study design and independent work

Distinguish literal FF5 from the nested union, do not re-subtract RF from spreads, report covariance condition and separate regularization and leverage constraints from the unrestricted identity. Refit in paired time blocks across train/test segments.

## Required tasks

1. Check return conventions and collinearity, estimate spanning regressions individually and jointly.

2. Verify squared Sharpe gain identity numerically, compare GRS and joint block-bootstrap alpha inference.

3. Estimate tangency weights using training or rolling 120-month window and common covariance regularization; evaluate OOS Sharpe and gross leverage.

4. Compare incremental factors and order dependence; test fixed gross leverage cap and turnover hurdle.

5. Repeat with alternative SMB convention (common base), subperiods and optional BAB common sample.

## Required exhibits

Spanning table, covariance conditioning, squared Sharpe gains with uncertainty, OOS performance and weight stability, leverage/cost sensitivity.

## Robustness

Large in-sample Sharpe gains can be mechanical estimation artifacts; report common-sample uncertainty. Factor spreads are not directly tradable instruments and funding/transaction costs matter. FF3 and FF5 SMB differ; never interpret an unnoticed replacement as nested addition.

## Minimum viable thesis

FF3 versus FF3+RMW+CMA+Mom, identity check, joint spanning and OOS comparison. Distinct from A01.02.02 which focuses on momentum pricing errors for test assets.

## Optional extension

AQR BAB or OSAP portfolios as additional candidates with multiplicity control and separate sample.

## Prerequisites

Mean-variance theory, factor regressions, covariance estimation and bootstrap.

## Thesis outline

1. Mean-variance spanning;

2. Factor definitions;

3. Joint tests and Sharpe gains;

4. OOS economic value;

5. Conclusions.

## Milestones

W1-3: derive identity; W4-6: factor files and checks; W7-9: spanning and inference; W10-12: rolling allocation and sensitivity; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
