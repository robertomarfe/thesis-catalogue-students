# Research plan | A01.02.01

## Study design and independent work

Require the monthly return blocks, matched RF and common complete calendar, positive GRS degrees of freedom, and at least the original provisional subperiod coverage. Refit paired alpha differences in joint time blocks. Document covariance singularity rather than silently regularizing the classical GRS statistic.

## Required tasks

1. Document factor definitions and common-sample descriptive statistics; estimate FF3 and FF5 for the same excess-return matrix.

2. Compute annualized mean absolute alpha, alpha RMSE, adjusted R-squared, GRS statistic/p-value separately by model and test-asset set; display individual alpha estimates with HAC intervals.

3. Estimate a deliberately nested pair with Mkt-RF, SMB and HML from FF5 held fixed, then add RMW and CMA; compare joint restrictions and factor spanning regressions.

4. Repeat by prespecified subperiod and alternative portfolio family; use block-bootstrap paired alpha-RMSE differences for uncertainty, not raw GRS p-value rankings alone.

## Required exhibits

Factor summary and correlation matrix; pricing-error/GRS table for common assets; alpha scatter or forest plot and portfolio-by-portfolio errors; nested comparison; subperiod and bootstrap table. Interpret any improvement in annualized return units.

## Robustness

Use common dates and factor source conventions; avoid claiming causal risk factors. Report non-iid limitations of classical GRS, and do not use higher adjusted R-squared alone as evidence of better pricing. Check smaller industry set if covariance is ill-conditioned; report all selected asset sets even if results are mixed.

## Minimum viable thesis

Reproduce FF3 and FF5 for industries plus one secondary test-asset set, compare pricing errors and joint tests on a common sample, include the nested-model check and time split. A five-factor rejection or weak improvement is a legitimate conclusion.

## Optional extension

Add momentum as a common factor or compare European factors and matched regional test assets; keep currency and RF consistent. Test factor redundancy with spanning, not by deleting a factor merely because its mean is small.

## Prerequisites

Linear regression, matrix algebra, portfolio returns, multivariate hypothesis tests, pandas/statsmodels. No individual stock database necessary.

## Thesis outline

1. Factor pricing and motivation;

2. CAPM, FF3, FF5 and tests;

3. Data and comparison design;

4. Pricing errors and factor spanning;

5. Stability, limitations and implications.

## Milestones

W1-3: derive factor pricing/GRS and acquire files; W4-6: clean returns and reproduce one regression; W7-10: common-sample model comparison and nested analysis; W11-13: subperiods, bootstrap and interpretation; W14-16: draft and reproduce all results.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
