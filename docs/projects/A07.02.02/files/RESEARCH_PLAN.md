# Research plan | A07.02.02

## Study design and independent work

Prespecify the sign cutoff and rolling windows. Report all factors, state counts and crisis sensitivity; distinguish conditional descriptive analysis from a trading signal or a pricing test.

## Required tasks

1. Describe factor means, volatility, lower partial moments and payoff distributions in up/down states.

2. Estimate separate and interaction regressions; verify slope equivalence and use HAC intervals.

3. Estimate joint time-block bootstrap confidence intervals for slope differences across all factors; control multiple comparisons (Holm or joint max statistic).

4. Analyze 120-month rolling asymmetry and predefined crisis periods, reporting state counts.

5. Repeat using market bottom/top terciles defined on training sample and examine sensitivity to extreme observations.

## Required exhibits

Conditional payoff table, slope asymmetry estimates and intervals, rolling exposures, state-count and joint-test diagnostics.

## Robustness

Market states are contemporaneous, not a trading signal. Nonlinear slope differences may arise from factor construction and conditional market variance; do not claim structural pricing. Do not subtract RF again from factor payoffs. Report whole sample and crisis sensitivity, not selected best results.

## Minimum viable thesis

Five factors plus Mom, predeclared states, conditional slopes and means, uncertainty and subperiod checks. Distinct from A07.02.01, which tests cross-sectional pricing of downside beta.

## Optional extension

Compare factor-level downside exposure with a drawdown-defined state or BAB, without changing baseline selection after results.

## Prerequisites

Factor models, regression, bootstrap and Python.

## Thesis outline

1. Asymmetric market risk;

2. Factor construction and conditional regressions;

3. Data and state definitions;

4. Conditional exposure evidence;

5. Economic interpretation.

## Milestones

W1-3: risk and factors; W4-6: align data and descriptive statistics; W7-9: conditional regressions; W10-12: joint inference and regimes; W13-16: writing and code.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
