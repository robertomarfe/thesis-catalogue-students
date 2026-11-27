# Research plan | A07.03.01

## Study design and independent work

Do not remove extreme days based on their effect on significance. Verify that the daily and monthly portfolio labels match, that the market is excess return, and that generated-regressor uncertainty is recognized.

## Required tasks

1. Verify daily and monthly portfolio definitions and return conventions; plot exposure distributions and estimation precision.

2. Estimate rolling market beta and coskewness; compare with own skewness and downside beta to clarify concepts.

3. Run monthly cross-sectional regressions on predetermined exposures, average slope and HAC uncertainty; beta-only benchmark and FF factor exposures as controls.

4. Sort fixed test portfolios into coskewness terciles each month and compare next-month returns and FF3/FF5 alpha as descriptive evidence.

5. Joint-date block bootstrap rerunning exposure estimation, windows 2/5 years and alternate industry panel; check sensitivity to crisis observations without selective deletion.

## Required exhibits

Exposure distributions and correlations, Fama-MacBeth slopes, sorted portfolio returns, alpha and uncertainty tables, common-date robustness.

## Robustness

Portfolio-level cross-section is small and overlapping stocks create dependence; no individual-stock pricing claim. Daily third moments noisy and driven by outliers; winsorization, if used, based on past data and clearly changes the estimand. Cross-sectional significance not proof of a structural SDF. Distinct from downside beta and option-implied skew theses.

## Minimum viable thesis

One daily/monthly test-asset panel, lagged beta/coskewness estimation, monthly cross-sectional prices and beta-only comparison with robust inference.

## Optional extension

Use open-source characteristic portfolios for a different cross-section or evaluate polynomial SDF distance on held-out assets.

## Prerequisites

Factor pricing, regression, higher moments, bootstrap and Python.

## Thesis outline

1. Higher-moment asset pricing;

2. Coskewness measures;

3. Portfolio data and exposure estimation;

4. Pricing and sorts;

5. Robustness and limitations.

## Milestones

W1-3: derive quadratic SDF; W4-6: prepare panels and exposures; W7-9: cross-sectional tests; W10-12: bootstrap and alternative panels; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
