# Research plan | D04.01.01

## Required tasks

1. Derive BSM hedge and self-financing cash update; verify one deterministic path by hand and test accounting identities.

2. Simulate exact GBM with nested rebalance grids; compare discounted terminal error mean, SD, RMSE and quantiles.

3. Plot error convergence on log-log axes against theoretical order under regularity; avoid assuming a finite-grid exact exponent.

4. Analyze error by strike, maturity, terminal moneyness and initial gamma; conditional results on terminal outcomes are descriptive only.

5. Report stock turnover and optionally exposure through time, and use independent seeds for Monte Carlo uncertainty.

## Required exhibits

Cash-account unit tests, error distributions, convergence plots, tail loss and turnover tables, comparison of gamma diagnostics and exact terminal payoffs.

## Robustness

Change drift and volatility; verify convergence is not an artifact of independently sampled paths across frequencies. Avoid trading at maturity after payoff is known. Distinguish discounted dollar error and error as percent of option premium for small premiums. No empirical hedging claim.

## Minimum viable thesis

Exact GBM, verified self-financing hedge, four frequencies and three strikes, quantitative convergence and distribution analysis with Monte Carlo precision.

## Optional extension

Compare delta computed using a deliberately misspecified volatility, but keep model-consistent frictionless hedging the primary exercise.

## Prerequisites

Stochastic calculus, BSM, simulation, Python arrays and basic statistical inference.

## Thesis outline

1. Replication and incompleteness from discrete trading;

2. BSM hedge and error expansion;

3. Simulation design;

4. Error distributions and convergence;

5. Economic implications.

## Milestones

W1-3: derive delta replication and error; W4-6: implement/test cash accounting; W7-9: simulation across grids; W10-12: gamma and tail diagnostics; W13-16: robustness and writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
