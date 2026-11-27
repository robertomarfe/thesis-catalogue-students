# Research plan | A09.04.01

## Study design and independent work

Verify four sleeves, monthly units, risk scaling and market benchmark. Use only trailing data in weights and training thresholds, with fixed holdout. No independent futures-position replication claim.

## Required tasks

1. Verify methodology, units and factor labels; compute individual means, volatility and correlations.

2. Decompose variance contributions and compare fixed equal-weight vs rolling inverse-vol sleeves using only past data.

3. Estimate contemporaneous market beta, conditional payoff means and correlations in market-tail months; calculate paired block intervals.

4. Plot cumulative excess payoffs (or funded wealth only with explicit collateral convention), drawdowns with funding convention and crisis-event summaries.

5. Compare early/late periods and leave-one-class-out portfolios; report whether results depend on bonds or a single crisis.

## Required exhibits

Factor correlation/variance tables, portfolio comparisons, conditional payoff plot, rolling beta, crisis and sensitivity analysis.

## Robustness

Published strategies may embed leverage and hypothetical costs; no claim of implementable net performance. Do not subtract RF twice. Market-tail states are ex post descriptions. Use source methodology rather than pretending to reconstruct original contracts.

## Minimum viable thesis

Four documented monthly sleeves, common sample, diversification metrics, equal-weight vs risk-scaled comparison, market-conditional evidence and intervals.

## Optional extension

Compare with separately documented long-run trend-following series; reconstruct signals only with actual contract-level returns and roll rules.

## Prerequisites

Portfolio theory, futures fundamentals, regression and Python.

## Thesis outline

1. Trend following and multi-asset premia;

2. Portfolio risk and state dependence;

3. Published factors and methodology;

4. Diversification and conditional evidence;

5. Limitations.

## Milestones

W1-3: TSMOM literature and source; W4-6: panel and methodology audit; W7-9: allocation and risk analysis; W10-12: conditional/robustness tests; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
