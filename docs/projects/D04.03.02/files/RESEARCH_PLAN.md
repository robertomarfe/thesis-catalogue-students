# Research plan | D04.03.02

## Study design and independent work

Report achieved risk, not merely the intended budget. The comparison must use the same opportunities, shares, premium and cost convention across policies; this is not a neural-policy training study.

## Required tasks

1. Verify BSM prices, deltas and discounted ledger in the zero-cost limit.

2. Implement calendar, reset-to-delta and band-edge policies on common paths.

3. On training paths choose bands to minimize mean cost subject to a predeclared 95% expected-shortfall loss limit; report infeasibility.

4. Freeze policies and compare held-out error-cost frontiers with paired confidence intervals.

5. Stress volatility mismatch and time-to-expiry gamma; examine how a gamma-scaled band changes turnover.

## Required exhibits

Self-financing unit tests; error-cost frontier; turnover and ES table; band policy trajectories; out-of-sample stress comparison.

## Robustness

Keep initial premium, trade convention and paths identical. Distinguish hedge error before costs from net P&L. Do not optimize bands on evaluation paths; compare uncertainty and not just mean loss. This is a finite-grid policy comparison, not a proof of global optimality.

## Minimum viable thesis

One ATM call, three nonzero cost levels, two band rules and calendar benchmarks, independent evaluation with paired uncertainty. Distinct from D04.03.01 (calendar optimization).

## Optional extension

Fit a state-dependent band using gamma and remaining maturity, with separate validation; compare under Heston dynamics.

## Prerequisites

BSM, stochastic calculus, simulation, risk measures and Python.

## Thesis outline

1. Replication with frictions;

2. No-trade regions;

3. Simulation and ledger;

4. Cost-risk frontiers;

5. Implications and limits.

## Milestones

W1-3: derive ledger and policies; W4-6: validate GBM engine; W7-9: train and select bands; W10-12: evaluate and stress; W13-16: reproduce and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
