# Research plan | D06.01.02

## Study design and independent work

Use paired SE on identical endpoints within each grid; 12/52/252 are not nested. Do not bridge-adjust a genuine discrete contract. Include the immediate-knockout case and retain underflow diagnostics.

## Required tasks

1. Implement vanilla and barrier payoff; validate limiting cases and knock-in/out parity.

2. Reproduce analytic continuous down-and-out prices for B<K and B<S0; confirm formula domain.

3. Compare naive grid, bridge-weighted estimates and analytic benchmark with paired MC confidence intervals; assess bias, RMSE and computation cost for barrier and grid changes.

4. Interpret the grid-contract premium difference and demonstrate whether bridge estimator residual errors are statistically consistent with zero.

## Required exhibits

Price/error table for each grid and barrier; convergence plot; barrier-distance sensitivity figure; separate table of contractual discrete-versus-continuous price differences; one worked crossing example and numerical test log.

## Robustness

Increase paths to separate MC error from grid bias; check survival products for underflow, immediate knock-out boundary, sigma sensitivity, and very low barrier limit to vanilla. For continuous monitoring the naive grid price is weakly above true price under identical paths, but sampling error affects comparisons. Never describe a bridge adjustment as correcting the price of a discretely monitored contract.

## Minimum viable thesis

One continuous down-and-out call type, analytical validation, three grids and barriers, MC uncertainty and clear distinction between simulation error and contractual monitoring.

## Optional extension

Evaluate the Broadie-Glasserman-Kou continuity correction for actual discrete-monitoring prices, or test a stochastic-volatility model where the simple GBM bridge formula is not exact.

## Prerequisites

Brownian motion, BSM, conditional probabilities, simulation and numerical statistics. No historical options required.

## Thesis outline

1. Barrier contracts and monitoring;

2. Risk-neutral pricing and bridge theory;

3. Analytic and MC implementation;

4. Numerical/economic results;

5. Robustness and product implications.

## Milestones

W1-3: study payoffs, parity and bridge derivation; W4-6: validate vanilla/analytic barrier routines; W7-10: implement grid and bridge comparison; W11-13: convergence, limits and contractual pricing; W14-16: write and archive reproducible experiment.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
