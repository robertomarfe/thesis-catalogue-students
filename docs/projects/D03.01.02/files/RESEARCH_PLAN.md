# Research plan | D03.01.02

## Study design and independent work

Plot news-impact curves at a common prior variance. Report optimization failures and standardized residual checks. Sign-specific forecast improvement is predictive evidence, not proof of financial leverage as a causal mechanism. Use paired time blocks or HAC for overlapping outcomes.

## Required tasks

1. Inspect tails, autocorrelation of squares and sign-conditioned variance; specify constant or zero mean once.

2. Estimate symmetric GARCH, GJR and EGARCH with common likelihood and report convergence and admissibility.

3. Plot news-impact curves at common previous variance; compare response to equal positive and negative innovations.

4. Produce genuine chronological 1- and 5-day forecasts, using simulation for nonlinear EGARCH multi-step expectations.

5. Compare QLIKE and MSE against symmetric GARCH and rolling variance, overall and by sign of last innovation; use HAC or block bootstrap for overlapping loss differences.

## Required exhibits

Parameter and persistence table, standardized residual diagnostics, news-impact curves, forecast loss and conditional loss tables, failure log and forecast date ledger.

## Robustness

Compare normal versus t errors, alternative training windows and crisis exclusions predeclared. Do not use future realized losses to define ex ante states. Squared returns are noisy variance proxies; do not interpret forecast superiority as evidence of balance-sheet leverage.

## Minimum viable thesis

Three fitted models with admissibility checks, news-impact analysis and chronological loss comparison at one horizon (plus five-day as standard extension), including uncertainty and convergence reporting.

## Optional extension

Add a VIX-based forecast using aligned units and a separate verified source; do not duplicate the broad GARCH-vs-historical forecasting pilot.

## Prerequisites

Maximum likelihood, time-series econometrics and Python arch/statsmodels. Understand conditional vs realized variance.

## Thesis outline

1. Conditional variance and asymmetry;

2. GARCH family;

3. Data and forecasting protocol;

4. News-impact and predictive performance;

5. Robustness and interpretation.

## Milestones

W1-3: derive models and losses; W4-5: clean daily returns; W6-8: estimation and diagnostics; W9-12: rolling forecasts and tests; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
