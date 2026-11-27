# Research plan | D03.02.02

## Study design and independent work

The break exercise is a diagnostic for observational equivalence, not a test that a particular historical break generated the sample. Retain the prescribed chronological periods and include four-week overlap in inference.

## Required tasks

1. Plot ACF and periodogram; estimate d with bandwidth sensitivity and document finite-sample constraints.

2. Simulate fractional Gaussian/ARFIMA and a piecewise short-memory variance DGP with equal variance and sample length, seed 2027, 500 repetitions; compare estimated d.

3. Estimate fixed model set and evaluate rolling or expanding forecasts; compare QLIKE and MSE of variance, not logs alone.

4. Use common-date block-bootstrap differences in scores (overlap at four weeks); assess subperiods and training-window length.

5. Repeat using daily HAR proxy and crisis-exclusion diagnostic; distinguish structural-break evidence from proof of memory.

## Required exhibits

ACF, simulated d distributions, parameter table, loss and forecast comparison, sensitivity to breaks and sample.

## Robustness

Daily returns give noisy realized variance, not intraday realized variance. Avoid choosing break dates using future forecasts or selecting d from the final sample. Truncated fractional filter requires burn-in and convergence. Log transformation changes the loss target.

## Minimum viable thesis

Weekly variance proxy, AR(1), ARFIMA and HAR forecasts, controlled break experiment and chronological test at both horizons. Distinct from D03.02.01's horizon forecasting by explicit memory-identification exercise.

## Optional extension

Compare FIGARCH or regime-switching volatility under a common out-of-sample protocol.

## Prerequisites

Time-series econometrics, likelihood, fractional filters, statistical programming.

## Thesis outline

1. Short and long memory;

2. Proxy and fractional estimation;

3. Controlled DGP experiments;

4. Historical forecast evaluation;

5. Identification limits.

## Milestones

W1-3: fractional integration and DGP; W4-6: build proxies and validate filter; W7-9: estimate and simulate breaks; W10-12: rolling forecasts and inference; W13-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
