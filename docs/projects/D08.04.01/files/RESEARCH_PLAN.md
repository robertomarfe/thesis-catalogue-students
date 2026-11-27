# Research plan | D08.04.01

## Study design and independent work

Unlike D08.04.02, this is historical rolling insurance evaluation. Gate remains blocked. Report achieved risk and uncertainty; simulation-only redesign needs explicit approval.

## Required tasks

1. Verify index construction, permissions, dividends, roll timing and common dates.

2. Compute compound returns, volatility, max drawdown, ES95 and worst months.

3. Compare risk-matched stock-cash allocation fixed using training sample; evaluate later period.

4. Estimate paired return/ES differences with block bootstrap; examine stress and tranquil periods without tuning after seeing outcomes.

5. Simulate premium/payoff attribution under several Q/P scenarios; never attribute actual index cost from synthetic premiums.

## Required exhibits

Index provenance and comparator check; wealth/drawdown charts; risk-return and stress table; synthetic insurance-cost decomposition.

## Robustness

Do not use price-only SP500; distinguish hypothetical index, trade costs and actual investability. Tail estimates imprecise; no claim of optimal insurance. If rights or history unavailable, switch to synthetic-only variant only with supervisor approval and revise empirical claim.

## Minimum viable thesis

Authorized PPUT and comparator, historical risk-matched comparison and a small transparent synthetic payoff exercise, or approved simulation variant.

## Optional extension

Compare puts with put spreads at common budget, separating protection and cap.

## Prerequisites

Options, portfolio returns, risk measures, bootstrap, Python.

## Thesis outline

1. Protective puts and insurance;

2. Pricing versus realized cost;

3. Benchmark data;

4. Tail and performance analysis;

5. Limitations.

## Milestones

W1-3: acquisition/rights and payoff; W4-6: index validation; W7-9: benchmarks; W10-12: tail and synthetic attribution; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
