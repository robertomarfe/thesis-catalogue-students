# Research plan | D03.01.01

## Required tasks

1. Plot returns and squared returns, estimate autocorrelations and ARCH diagnostics; fix forecast origins and loss evaluation dates.

2. Fit GARCH on training only (omega>0, alpha,beta>=0 and alpha+beta<1); record failures and compare with constant and rolling-variance benchmarks.

3. Generate recursive forecasts at t for t+1 and cumulative t+1 to t+21. Score QLIKE=log(h)+RV/h (positive forecast floor declared), MSE and forecast bias.

4. Compare losses via HAC inference or block bootstrap; evaluate 21-day nonoverlapping dates as a robustness check and display loss by regimes defined using lagged information.

## Required exhibits

Data summary and autocorrelation plot; parameter/persistence table; dated forecast-versus-proxy figures; loss and confidence interval table by horizon and model; convergence/failure report. Compare ranking and magnitude of improvement, not only coefficient significance.

## Robustness

Vary historical window and GARCH refit frequency; use Student-t innovations as extension; alternate simple vs log returns; check common origins and 21-day annualization (do not compare annualized to daily variance); report 2008/2020 influence without choosing samples by outcomes. Squared daily returns omit intraday realized variation; do not claim high-frequency forecast performance.

## Minimum viable thesis

One clean daily series; rolling historical and GARCH forecasts at both horizons on a common evaluation sample; QLIKE and MSE, uncertainty-aware loss comparisons, and honest treatment of noisy targets. No requirement that GARCH wins.

## Optional extension

Compare EWMA or asymmetric GJR-GARCH; add VIX as a distinct risk-neutral predictor with horizon matching rather than as a directly comparable realized variance.

## Prerequisites

Time-series econometrics, maximum likelihood basics, data handling, Python pandas/statsmodels/arch. No intraday feed required.

## Thesis outline

1. Motivation and volatility stylized facts;

2. Conditional heteroskedasticity and forecast evaluation;

3. Data and recursive protocol;

4. Forecast results and regimes;

5. Robustness and practical implications.

## Milestones

W1-3: study GARCH and forecast scoring, acquire and clean factor file; W4-6: define targets and validate historical baseline; W7-10: estimate/refit and generate chronological forecasts; W11-13: evaluate losses, inference and regimes; W14-16: finalize reproducible tables and dissertation.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
