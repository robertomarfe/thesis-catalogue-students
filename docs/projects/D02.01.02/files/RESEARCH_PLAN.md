# Research plan | D02.01.02

## Study design and independent work

Check common month-end dates and complete 30/90-calendar-day target intervals before fitting. Preserve the information set at every forecast origin; separate the implied level and forward proxy, and score common outcomes.

## Required tasks

1. Construct aligned v30, v90 and forward slope; diagnose negative forward proxies and data gaps before any trimming.

2. Build 30/90-day future and backward realized-variance measures; show calendar and annualization unit tests.

3. Estimate historical variance, VIX level and level-plus-slope forecasts, with training-only positivity floor. Report slope coefficient and HAC inference (90-day targets overlap).

4. Expanding-window forecast comparison by QLIKE and MSE; only use outcomes fully realized by forecast date. Test whether slope adds incremental rather than just crisis information.

## Required exhibits

Term structure and forward-variance time series, crisis plots, forecast error and coefficient tables, cumulative loss differences, data-coverage/negative-forward diagnostics and SPX proxy sensitivity. Report forecast gains or lack thereof in units of annualized variance.

## Robustness

Use nonoverlapping quarterly forecasts as sensitivity, different calendar alignment and VIX-versus-SPX common sample. Never interpret French market RV as exact SPX underlying; separate baseline proxy from matched-index results. Report HAC/block-bootstrap dependence and revised series limits; no arbitrary deletion of inversion days.

## Minimum viable thesis

Verified two implied indices and return series, horizon-matched variance construction, level/slope/historical benchmark comparison in a chronological holdout, dependence-aware inference and economic interpretation of Q-P gap.

## Optional extension

Add VIX9D or VIX6M only after checking coverage and maturity conventions; compare physical forward variance over days 31-90 rather than adding many regressors.

## Prerequisites

Volatility measures, OLS, time-series forecasting and pandas/statsmodels. No option chains required.

## Thesis outline

1. Implied variance and term structure;

2. Physical volatility forecasts;

3. Data and horizon alignment;

4. Incremental forecasting evidence;

5. Risk premium interpretation and limitations.

## Milestones

W1-3: verify index definitions and data; W4-6: construct aligned features/targets and test units; W7-10: estimate and forecast; W11-13: dependence and proxy robustness; W14-16: document and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
