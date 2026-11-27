# Research plan | A08.04.01

## Study design and independent work

Verify empirical ES by order statistic and direct Rockafellar-Uryasev objective; compare two-asset LP to enumerated frontier. Record solver status/runtime, prespecified fallback and feasible risk budgets. Run rolling daily scenario fit with monthly trading, actual complete calendar and paired date-block ES intervals. Large grid remains student work.

## Prespecified implementation

Daily value-weighted 10 industries baseline, 30 robustness, five-year trailing window, monthly rebalance but daily drift and daily net returns. Loss=-w'r, alpha=.95 (90/97.5 robustness), fractional tail mass at boundary. Set ES budget from training EW or preregistered multiples; variance benchmark on comparable training EW variance budget, not equating ES and variance units. LP with unrestricted VaR threshold, nonnegative auxiliaries; report infeasibility and explicit equal-weight fallback. Normal and Student-t matched covariance (scale t shocks by sqrt((nu-2)/nu)). Evaluate realized net daily ES with paired date-block inference; monthly trades scale=1; report solver memory and timing (dense teaching LP; sparse extension before full large grid).

## Required tasks

1. Verify LP objective/constraint on small hand-computed losses and discrete ES definition.

2. Simulate normal and heavy-tail data, compare feasible frontiers and weights.

3. Estimate monthly ES and variance-constrained weights using past-only windows; record infeasible instances and predefined fallback to equal weight.

4. Evaluate net daily ES, volatility, CE, return, turnover and drawdown out of sample with date-block bootstrap.

5. Stress tail confidence, lookback and cost; compare equal-weight risk budget and stability under repeated sampling.

## Required exhibits

Optimization tests; ES/mean frontiers; out-of-sample risk and wealth table; constraint feasibility ledger and sensitivity.

## Robustness

Tail estimation error and changing dependence matter; compare same risk/capital convention. No guarantee that ex-ante ES budget holds realized. Do not select risk budget or confidence level using test outcomes.

## Minimum viable thesis

Ten industries, historical-scenario LP, equal-weight and variance benchmark, rolling evaluation and realized ES uncertainty.

## Optional extension

Add shrinkage or distributionally robust ES with separate validation; include turnover penalty inside optimization.

## Prerequisites

Convex optimization, portfolio theory, risk measures, Python/SciPy.

## Thesis outline

1. Risk measures;

2. ES optimization;

3. Simulation and data;

4. Portfolio results;

5. Robustness and limits.

## Milestones

W1-3: ES derivation and data; W4-6: LP and simulations; W7-9: rolling optimizer; W10-12: held-out evaluation; W13-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
