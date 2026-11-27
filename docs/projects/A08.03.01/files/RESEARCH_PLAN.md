# Research plan | A08.03.01

## Study design and independent work

Check contribution sum, positive budget and ERC residual on diagonal and correlated SPD matrices; report KKT for GMV and eigenvalues. Compare four methods with common dates/covariance, cost drift and ex-ante contributions plus held-out realized contribution estimates and uncertainty.

## Prespecified implementation

Use 30 industry value-weighted monthly total returns, 60 months, 1990-2025 target, same positive-definite covariance across EW, inverse-vol, ERC and GMV. ERC via convex log barrier then normalize; contributions w_i(Sigma w)_i/(w'Sigma w); no leverage or cap beyond simplex. Distinguish negative contributions under other weights from impossible negative budgets in ERC. Rebalance monthly and charge scale=1 ledger; risk contributions at formation, realized variance and concentration separately. Optional GSW bond sleeve only documented aging.

## Required tasks

1. Derive risk decomposition; test ERC solution on diagonal and equicorrelation matrices, GMV against unconstrained formula.

2. Simulate known covariance with unequal variances and changing correlation.

3. Run rolling monthly portfolios using only past data; track drifted weights before trading.

4. Compare realized volatility, Sharpe, drawdown, turnover and effective number of holdings; record ex ante RC residuals and realized contributions in evaluation windows.

5. Repeat 36/120-month windows and covariance estimator choices with paired bootstrap; no ex post optimal selection.

## Required exhibits

Weight/risk contribution charts, constraint and solver residuals, performance and transaction-cost tables, sensitivity plots.

## Robustness

Positive definite covariance and solver accuracy checked. ERC with additional caps need not achieve exact equal risk; baseline only long-only. Industry portfolios overlap underlying economy, not distinct asset classes. Risk parity need not beat minimum variance in volatility.

## Minimum viable thesis

Four portfolios on same long-only industry sample, validated ERC and GMV, drift-corrected backtest and contribution analysis.

## Optional extension

Add synthetic constant-maturity bond allocation and inflation scenarios; volatility targeting with stated leverage/funding.

## Prerequisites

Linear algebra, convex optimization, portfolio theory, returns.

## Thesis outline

1. Risk-based allocation;

2. Optimization;

3. Simulation and data;

4. Backtest;

5. Risk and implementation.

## Milestones

W1-3: risk contributions; W4-6: solver/simulation; W7-9: backtest; W10-12: robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
