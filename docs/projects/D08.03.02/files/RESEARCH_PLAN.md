# Research plan | D08.03.02

## Study design and independent work

Focus on downside compensation and collateral rather than D08.03.01's upside capture. Defer or explicitly approve redesign if PUT rights or history fail. No silent BXM or synthetic substitution.

## Required tasks

1. Derive payoff and collateral convention, document index roll methodology.

2. Align end-month total-return levels and cash returns; validate missing dates and extreme observations.

3. Compare cumulative wealth, Sharpe, ES, skewness, downside and upside beta.

4. Construct a trailing 60-month volatility-matched equity/cash benchmark (weights capped at one) and a fixed 60/40 equity/cash control.

5. Evaluate conditional performance in predeclared low/high VIX or market-loss regimes; block-bootstrap paired returns, report crisis subsamples.

## Required exhibits

Payoff diagram; common-sample summary and wealth plots; tail/capture statistics; matched-risk and regime table.

## Robustness

PUT is a hypothetical index, not directly investable; do not use price-only S&P500 as benchmark. Avoid interpreting the spread in returns as pure variance premium. Rights, actual data history and launch dates are gates. Costs and collateral yield are not silently ignored.

## Minimum viable thesis

Authorized PUT series plus equity total-return comparator or labeled French proxy, matched-risk comparison and tail-loss analysis. If PUT unavailable, defer or approve a synthetic redesign.

## Optional extension

Compare PUT and BXM with documented collateral and roll differences; incorporate trading-cost scenarios.

## Prerequisites

Option payoff algebra, portfolio statistics, time-series inference and Python.

## Thesis outline

1. Put writing and parity;

2. Index construction;

3. Data and benchmarks;

4. Performance and tail risk;

5. Interpretation.

## Milestones

W1-3: contract/index methods and download gate; W4-6: data alignment; W7-9: matched-risk benchmarks; W10-12: tail and regime checks; W13-16: write/reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
