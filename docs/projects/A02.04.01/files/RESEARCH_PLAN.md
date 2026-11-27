# Research plan | A02.04.01

## Study design and independent work

Reconcile two consecutive months manually including drifted weight and fees; no contemporaneous variance; check compounding and return units; net CE comparison on common dates; clearly label cost-on-pretrade approximation and annualization.

## Prespecified implementation

Use a common lagged variance model and same return/RF source, w=clip(mu/(gamma*v),0,1). Baseline gamma 3/5/10, costs 0/10/25 bp on absolute traded stock weight relative to previous drifted weight. Deduct costs at start before return. Evaluate monthly CE annualized by 12 as arithmetic approximation, gross/net Sharpe, turnover and drawdown; no forecast-dependent volatility specification.

## Required tasks

1. Build date-indexed expanding forecasts and trailing variance; verify no future inputs.

2. Implement historic mean and predictor/combination forecasts; record OOS R2 and loss.

3. Implement self-financing weight and drifted-turnover ledger; validate buy-and-hold and cash limits.

4. Compare test-period CE, Sharpe, turnover and drawdown against fixed 60% and historical mean weights; pair date block bootstrap.

5. Vary gamma, costs and leverage cap without selecting best test setting; report when statistical and economic rankings diverge.

## Required exhibits

Forecast and position ledger; OOS accuracy table; net wealth and CE; sensitivity and paired intervals.

## Robustness

Use identical RF and return series; estimate forecast variance on past returns only; revised predictors make pseudo-real-time experiment, not historical live trading. Avoid optimizing CE on test data.

## Minimum viable thesis

Historical mean and two prespecified predictor policies, common variance model, locked evaluation and net CE with uncertainty.

## Optional extension

Use shrinkage of expected returns toward historical mean; compare forecast combination and uncertainty-adjusted weights.

## Prerequisites

Predictive regressions, portfolio choice, time series and Python.

## Thesis outline

1. Predictability and investor utility;

2. Forecast-to-weight mapping;

3. Data and timing;

4. Economic value;

5. Robustness.

## Milestones

W1-3: utility and data; W4-6: forecast pipeline; W7-9: ledger and validation; W10-12: locked evaluation; W13-16: sensitivity and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
