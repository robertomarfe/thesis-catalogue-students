# Research plan | A07.01.01

## Study design and independent work

The matched SPX source remains blocked until rights and actual coverage are confirmed. Short samples may support descriptive results only; long-proxy OOS analysis requires explicit supervisor agreement. No silent source substitution or claim of an intraday replication.

## Required tasks

1. Clean closes and calendar; compute trailing 252/21-day historical daily variance and forecast 30-calendar-day sum using only data known at t. Compare a fixed EWMA (lambda=0.94 daily) or GARCH as alternative; use a scheduled calendar and state missing-data rule.

2. Construct horizon-matched VRP in decimal variance units; report descriptive statistics and verify annualization.

3. Regress next 1- and 3-month compounded market-minus-bill returns on lagged VRP, with HAC for overlap; report effect of a one-SD predictor move and incremental R2.

4. Build expanding-window forecasts against historical mean using identical dates; compare OOS R2 and error-difference uncertainty. Repeat long proxy sample separately, and never use realized future variation to construct predictors.

## Required exhibits

Variance-leg and VRP time series; descriptive/correlation table; predictive regression and confidence intervals; chronological OOS loss comparison; short matched-SPX versus longer proxy-sample sensitivity. Discuss limitations relative to Bollerslev et al.'s intraday measure rather than claiming exact replication.

## Robustness

Compare 21 trading-day fixed horizon approximation with calendar-matched baseline, alternative P forecasts, and SPX vs FF variance proxies. Keep forecast tuning inside training and avoid choosing horizons after seeing significance. If matched sample is too short, restrict baseline to descriptive/in-sample results and use longer labeled proxy for OOS; document this before assignment. Check end-of-day alignment and exchange holidays.

## Minimum viable thesis

Reproducible ex ante VRP construction, explicit units/underlying distinction, 1- and 3-month predictive regressions and at least one chronological OOS comparison where sample permits. Null or unstable results are acceptable; no intraday or option-chain subscription required.

## Optional extension

Add Goyal valuation predictors or compare VIX to realized variance separately; if reliable intraday data become available, construct a higher-quality RV proxy without changing baseline claims retroactively.

## Prerequisites

Risk-neutral pricing, return and volatility measurement, predictive regressions, time-series forecasting, Python. Short historical coverage is a key supervision checkpoint.

## Thesis outline

1. Volatility risk and motivation;

2. Variance pricing and forecast theory;

3. Data, timing and VRP construction;

4. Predictive evidence and evaluation;

5. Robustness and limitations.

## Milestones

W1-3: study VIX/VRP theory and verify downloads; W4-6: align dates and test physical forecast; W7-10: freeze VRP, regressions and OOS design; W11-13: compare samples, horizon and forecast sensitivity; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
