# Research plan | A09.01.01

## Study design and independent work

Audit identical USD units and RF, dates, portfolio definition and factor count. Report N, T, K, covariance conditioning and paired uncertainty. Separate factor-construction overlap from the economic interpretation.

## Required tasks

1. Align all data, verify currency, sample and risk-free rate; document constituent overlap.

2. Estimate global and regional FF3 on identical assets/dates. Report average absolute alpha, RMSE alpha, adjusted R2 and individual confidence intervals; test joint alphas by region.

3. Test incremental regional factors controlling for global factors, monitor multicollinearity and covariance rank. Compare Developed ex-region proxies where available (e.g. developed ex US as sensitivity for North America, noting mismatch).

4. Prespecify 1990-2007 and 2008-2025 subsamples; report stability and bootstrap paired model differences without interpreting improved R2 as evidence of market segmentation.

## Required exhibits

Regional factor correlation matrix, alpha heatmaps, benchmark comparison by region, joint-test and incremental-factor tables, paired uncertainty intervals, documented common-currency sample.

## Robustness

Use identical asset sets/dates and number of factors in primary comparisons; disclose portfolio-factor construction overlap, regional size breakpoints and global factor inclusion of tested region. GRS may be invalid for near-redundant portfolios; shrink test set transparently or report bootstrap inference. Integration is not identified by alpha differences alone; currency risks may be omitted.

## Minimum viable thesis

Two or more verified regional portfolio panels plus developed/region FF3; matched USD excess returns, global/local alpha and fit comparisons, joint or dependence-aware tests, and careful interpretation of overlap and integration.

## Optional extension

Add FF5 or currency factors and a formal partial-integration model, only after checking test assets and sample compatibility.

## Prerequisites

CAPM, FF factors, multivariate OLS, hypothesis testing and Python.

## Thesis outline

1. International asset pricing and integration;

2. Traded-factor models and tests;

3. USD data and comparable portfolios;

4. Global versus regional evidence;

5. Integration interpretation and limitations.

## Milestones

W1-3: theory and exact data gate; W4-6: align factor and asset panels; W7-10: estimate matched models and tests; W11-13: overlap, rank and subperiod robustness; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
