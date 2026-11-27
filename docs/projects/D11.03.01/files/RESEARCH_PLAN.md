# Research plan | D11.03.01

## Study design and independent work

Verify primal/dual matching, strict feasibility separately, and nested intervals on consistent grids. Report statewise residuals and the role of new payoff directions; do not interpret a failed LP as an economic bound.

## Required tasks

1. Verify rank of traded payoff matrix and strict feasibility via maximizing minimum pi; include a two-state complete-market example as unit test.

2. Compute primal and dual lower/upper bounds for digital and call; show feasible interior price examples and spanning conditions.

3. Add calls one at a time and verify nested closed intervals, inspect superhedge portfolios and state payoffs.

4. Repeat with finer state grid and consistent new generating probabilities; add bid-ask bands, test infeasible quotes and interpret widening. Distinguish state-grid dependence from mathematical no-arbitrage.

## Required exhibits

State payoff and prices table; LP primal/dual reconciliation and feasibility checks; bound-width plot by added instruments; sub/superhedging payoff figure; stress table for quote bands and state support. Quantify the marginal value of traded instruments in reducing pricing ambiguity.

## Robustness

Check solver status and duality gaps; no interpretation of infeasible markets as valid price ranges. Recompute with alternative positive state probabilities and extreme states, normalize payoffs and prices. When bid-ask bounds are introduced, derive consistent long/short trading costs or use only the dual quote-band problem with explicit assumptions. No price outside a finite state grid is certified in a continuous market.

## Minimum viable thesis

Finite-state example with no-arbitrage feasibility, primal/dual matching, monotone interval narrowing as assets are added, and a complete-market limit. No observed option chain needed.

## Optional extension

Explore constrained short sales or robust bounds with bid-ask costs and extra states; avoid extrapolating finite-state results to model-free continuous-market claims without proving conditions.

## Prerequisites

Linear algebra, no-arbitrage theory, linear programming, Python/SciPy. Mathematical proof and numerical construction are both important.

## Thesis outline

1. Complete versus incomplete markets;

2. State prices, spanning and duality;

3. Finite-state LP design;

4. Pricing bounds and sensitivity;

5. Implications and limitations.

## Milestones

W1-3: finite-state asset pricing and LP duality; W4-6: build feasibility and replication tests; W7-10: run instrument-addition experiment; W11-13: state-grid and quote-band robustness; W14-16: write and reproduce all numerical results.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
