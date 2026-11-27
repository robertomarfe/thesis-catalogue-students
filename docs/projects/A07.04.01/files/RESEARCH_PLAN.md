# Research plan | A07.04.01

## Study design and independent work

Check the prediction of VIX is trained strictly before the innovation date. Weak loading dispersion and generated regressors matter; report null evidence and avoid a causal interpretation of the estimated slope.

## Required tasks

1. Build monthly log VIX innovation with recursive estimates, verify factor and portfolio return units.

2. Estimate market/volatility betas using only months through t; examine cross-sectional dispersion and precision.

3. Run monthly cross-sectional regressions with lagged betas; report mean lambda_v and HAC uncertainty; include FF loadings as sensitivity.

4. Form high-low volatility-beta portfolio from lagged sorts; test returns and factor-adjusted alpha.

5. Jointly bootstrap time blocks with re-estimation where feasible; vary windows and control for market downside, test sensitivity to major crises.

## Required exhibits

Beta dispersion/precision plots; Fama-MacBeth price estimates; high-low portfolio return and alpha table; robustness and sample diagnostics.

## Robustness

Generated-regressor error, small cross section, weak beta dispersion and collinearity may prevent identification. No causal or individual-stock claim. VIX innovations include expected variance and risk-premium variation; distinguish priced risk from simple contemporaneous association.

## Minimum viable thesis

One French test-asset set, recursive volatility innovation, lagged betas, cross-sectional pricing test and joint uncertainty discussion.

## Optional extension

Use daily beta estimation aggregated monthly or compare option-based variance-risk measures after data validation.

## Prerequisites

Factor models, rolling regressions, Fama-MacBeth, time-series inference, Python.

## Thesis outline

1. Volatility risk and SDF;

2. Innovation construction;

3. Rolling beta estimation;

4. Cross-sectional pricing and sorts;

5. Robustness.

## Milestones

W1-3: literature and data; W4-6: innovations/betas; W7-9: cross-sectional tests; W10-12: bootstrap and robustness; W13-16: thesis and code.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
