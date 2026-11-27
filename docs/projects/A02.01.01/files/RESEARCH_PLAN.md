# Research plan | A02.01.01

## Required tasks

1. Audit dates, units, definitions and availability of dividends/earnings; impose a conservative additional lag for earnings as sensitivity and call revised-data exercise pseudo-OOS.

2. Report in-sample coefficients with HAC inference and predictor persistence; estimate separately for d/p and e/p, avoid searching many specifications.

3. Generate expanding-window forecasts, then fixed 20-year rolling estimation as prespecified robustness; compare historical mean forecasts computed using the same information date.

4. Compute OOS R2, cumulative squared-error differences and Clark-West comparison (appropriate nested setting); use block bootstrap sensitivity and subperiod error tables. Quantify forecast magnitudes in annualized units only with stated conversion.

## Required exhibits

Variable dictionary and sample coverage; in-sample regression table; chronological forecast and cumulative loss figures; OOS score table across models/subperiods; lag-sensitivity table. Explicitly explain whether evidence comes from predictability, stability or a small group of episodes.

## Robustness

Do not use full-sample means, scaling, revised predictors described as real-time, or future dividend releases. Avoid selecting predictors on the test sample. Use common sample and examine extreme observations without post-hoc deletion. For longer horizons compound market and RF legs separately, use HAC/block inference for overlapping targets; this is optional, not a core requirement.

## Minimum viable thesis

Two predictors, one historical-mean benchmark, correctly lagged chronological forecasts, OOS R2 and uncertainty, and an explanation of weak/unstable or strong performance. No requirement to beat the historical mean.

## Optional extension

Add a simple constrained forecast or mean-variance timing rule with predeclared risk aversion and trading costs; compute economic gain only on frozen OOS predictions.

## Prerequisites

OLS, time-series forecasting, return conventions, basic present-value theory, Python. No proprietary predictor database required.

## Thesis outline

1. Equity valuation and predictability;

2. Present-value identity and forecast evaluation;

3. Data, timing and research design;

4. In-sample/OOS evidence;

5. Stability and conclusion.

## Milestones

W1-3: study predictability literature and download author data; W4-6: validate variables, benchmark and forecast origin; W7-10: freeze models and compute recursive forecasts; W11-13: OOS inference, lags and regimes; W14-16: write and regenerate exhibits.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
