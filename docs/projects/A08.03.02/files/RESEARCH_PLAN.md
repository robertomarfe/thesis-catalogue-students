# Research plan | A08.03.02

## Study design and independent work

Check target/cap and funding ledger against two hand-computed periods; keep realized equity and cash returns separately, lag volatility at month end, disclose haircut cost approximation and insolvencies. Predeclare static matched-risk rule and borrowing spread; report turnover, downside, CE and paired test uncertainty.

## Prespecified implementation

At each month-end use complete trailing 21/63/252 daily total market returns (Mkt-RF+RF), annualize SD sqrt(252); target .10/.15, cap 1/1.5/2. Forecast only with data through t, hold next monthly total market and RF. Borrowing spread 0/100/200bp annual charged on negative cash weight; equity turnover against drifted weight, 0/10/25bp per dollar. Static comparator set with 1990-2004 training-only volatility/cap; 2005-25 final. No ex-post risk matching. Report insolvent paths rather than silently omit; compare net returns and leverage/trading distribution. Daily RF and monthly RF use consistent source vintage, audit month compounding.

## Required tasks

1. Validate total and excess returns, dates and lagged volatility forecasts.

2. Implement portfolio wealth and drifted turnover, borrowing cost only on exposure above one.

3. Compare volatility targeting with buy-and-hold, fixed risk-matched equity/cash and inverse-variance alternative on common evaluation dates.

4. Report realized target deviation, leverage, turnover, Sharpe, ES, drawdown and certainty equivalent; use block bootstrap of paired outcomes.

5. Test alternative horizons, caps/costs and high-volatility states; lock hyperparameter selection to training.

## Required exhibits

Weight and forecast volatility time series; realized volatility/target plot; wealth and drawdown; leverage/cost/performance table; paired uncertainty.

## Robustness

No use of month t+1 information for w_t; do not set target scale using full test sample. Excess returns may not include cash financing at investor rates; make assumptions explicit. Leverage caps and drawdown paths matter. Index-based synthetic portfolios not executed trades.

## Minimum viable thesis

Market and cash, one target and two caps, fixed equity/cash benchmark, past-only weights and cost-aware evaluation. Distinct from risk parity across multiple assets.

## Optional extension

Compare conditional mean forecasts or apply to FF factors with explicit notional/margin conventions.

## Prerequisites

Portfolio theory, volatility estimation, Python and backtest discipline.

## Thesis outline

1. Volatility-managed portfolios;

2. Forecasts and allocation;

3. Data and ledger;

4. Performance and costs;

5. Robustness.

## Milestones

W1-3: theory/data checks; W4-6: ledger and forecasts; W7-9: baseline; W10-12: stress and costs; W13-16: reproduce/write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
