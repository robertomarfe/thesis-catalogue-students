# Research plan | D04.02.02

## Study design and independent work

Check actual permissions, warmup and complete sessions before assignment. Report eligible windows and separate historical sampling uncertainty from simulation error. If access fails, defer or approve a retitled simulated stress study; no silent substitution.

## Required tasks

1. Validate one-path cash ledger and GBM convergence, same initial premium for each strategy comparison.

2. Replay all windows with daily and weekly hedge updates; use trading-day time convention.

3. Compare residual distributions with matched GBM, condition on ex post drawdown categories and realized variance surprises.

4. Analyze two fixed illustrative cost rates and no-cost benchmark; separate model error from cost.

5. Show pathwise cumulative hedging residuals and sensitivity to volatility window, strike and stress definition.

## Required exhibits

Historical-window audit, representative paths and hedge ledgers, residual quantiles, stress versus GBM comparison and robustness table.

## Robustness

Price index is not a directly traded asset, dividends, financing and option prices are assumed, and no actual historical option P&L is measured. Stress classification is retrospective, not a trading signal. Small nonoverlapping sample limits tail inference; overlapping windows only as sensitivity with block resampling.

## Minimum viable thesis

Observed stock-price replay plus GBM reference and two hedge rules; no historical options needed. S-class denotes synthetic option pricing, but SP500 input is required for this title. Distinct from D04.02.01's two-asset volatility hedge.

## Optional extension

Add a self-contained dividend-yield scenario or lawful historical option snapshots for separate empirical validation.

## Prerequisites

BSM and Greeks, simulation, time-series cleaning, portfolio accounting.

## Thesis outline

1. Replication and model error;

2. Historical path construction;

3. Synthetic hedge experiment;

4. Stress comparison;

5. External validity.

## Milestones

W1-3: derive cash ledger and validate source; W4-6: GBM checks and windows; W7-9: replay and comparison; W10-12: stress/cost robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
