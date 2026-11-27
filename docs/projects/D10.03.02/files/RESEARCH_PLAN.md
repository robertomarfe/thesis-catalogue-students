# Research plan | D10.03.02

## Study design and independent work

Audit USD/EUR sign, full-principal identity, common dates, lagged rates and no look-ahead. Retain 60 aligned-quarter target; if unavailable agree a descriptive fixed-ratio scope. No ex-post optimized benchmark.

## Required tasks

1. Validate currency orientation, compounding and terminal hedge P&L with constant equity/FX examples.

2. Construct unhedged and hedged euro quarterly returns; report mean, volatility, downside risk and drawdown, with carry and residual equity-FX exposure separately.

3. Estimate expanding minimum-variance hedge ratio on past quarterly observations only; compare fixed ratios in common test dates.

4. Scenario-test hypothetical 5-20 bp one-way notional costs and 25-100 bp annual basis shifts; report turnover/rebalancing conventions and results across subsamples.

## Required exhibits

Wealth paths, hedge ratio and FX/equity covariance charts, risk-return/ES table, realized carry attribution, cost/basis sensitivity and sample audit. Use same initial capital and quarter boundaries for all portfolios.

## Robustness

Do not use monthly 3m forward rolls as nonoverlapping contracts. No compounding of market excess return without RF. Report portfolio-research series and proxy rates, not executable currency hedge performance. Separate risk reduction from return enhancement; use paired block bootstrap for volatility differences, no optimized full-sample ratio in OOS comparison.

## Minimum viable thesis

At least 60 aligned quarters if available, correctly signed forward P&L, fixed hedge ratios and an expanding benchmark, risk/return comparisons and transparent basis/cost scenarios. If data insufficient, fixed-ratio descriptive exercise with no dynamic forecast claim.

## Optional extension

Compare regional stock portfolios, or model rolling monthly actual 1m hedge only with verified tenor-matched daily rates and forward data.

## Prerequisites

Portfolio variance, FX forwards, return compounding, basic time-series econometrics and Python.

## Thesis outline

1. Currency exposure and hedging;

2. Forward P&L and hedge ratios;

3. Data and portfolio protocol;

4. Historical proxy hedge evidence;

5. Costs, basis and conclusion.

## Milestones

W1-3: theory and data gate; W4-6: align quarterly total returns and verify P&L; W7-10: portfolio and OOS hedge ratios; W11-13: costs, regimes and uncertainty; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
