# Research plan | A08.04.02

## Study design and independent work

Hand-check P_(t+1)(5-1/12)/P_t(5) and common monthly market total return. Verify EWMA versus direct weighted covariance, lag estimates and training-only tuning. Compare same capital/constraints/costs and out-of-sample periods, net performance with paired block inference.

## Prespecified implementation

Construct synthetic monthly 5-year zero holding returns from GSW Svensson yields at n and exact n-1/12 (annual continuous decimal), market total Mkt-RF+RF. Use actual end-month curve observations and lag GSW predictors when needed; pseudo-real-time caveat. Fixed 60/40, expanding GMV, rolling 36/60 or EWMA half-life selected in chronology after initial 120 months, freeze final 15 years if feasible. Original THEORY uses half-L1 turnover while DESIGN says per one-way turnover: explicitly use scale=.5 for baseline and report equivalent full-L1 cost (half rate) to avoid ambiguous cost comparison. No lookahead, no actual fund claim. Fixed comparator rebalanced, not buy-and-hold.

## Required tasks

1. Validate gross stock and synthetic bond return construction, aging and cash ledger.

2. Compare fixed 60/40 and expanding minimum variance using common holdout.

3. Fit rolling/EWMA policy on training/validation only, freeze choices, then run sequential portfolio.

4. Report annualized return, SD, Sharpe versus RF, drawdown, ES and turnover before/after costs.

5. Evaluate paired block bootstrap, inflation and stock-bond correlation regimes, alternative 10Y bond proxy and lagged data.

## Required exhibits

Wealth and drawdown panels, allocation/correlation paths, net performance and turnover tables, uncertainty and cost break-even sensitivity.

## Robustness

Synthetic constant-maturity strategy ignores security-level execution and tax; modelled cost not observed cost. Fixed 60/40 is rebalanced, not buy-and-hold. No test-window tuning or ex-post regime policy; differences in return and risk both matter.

## Minimum viable thesis

Static and two dynamic policies on same dates, valid aging return and drifted turnover, costs and held-out risk/performance uncertainty.

## Optional extension

Add cash-inclusive target-volatility policy with predeclared volatility target, compare equal ex-ante risk and avoid leverage.

## Prerequisites

Portfolio theory, covariance estimation, fixed income, time series.

## Thesis outline

1. Stock-bond diversification;

2. Portfolio risk and rebalancing;

3. Return construction;

4. Held-out allocation;

5. Limits.

## Milestones

W1-3: theory and sources; W4-6: aging returns/ledger; W7-9: validation and freeze; W10-12: held-out and costs; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
