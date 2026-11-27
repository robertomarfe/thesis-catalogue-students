# Research plan | D11.03.02

## Study design and independent work

Use the degenerate band and convex call limits to check sign and units; record instability and boundary effects. Distinguish the worst-case dynamic control from a search over constant volatilities.

## Required tasks

1. Derive HJB and convex endpoints; prove lower<=upper by control-set nesting.

2. Implement stable solver and verify degenerate band/convex call against BSM.

3. Refine space/time and boundaries for butterfly; compare with constant-vol grid and report bound gaps.

4. Plot optimal volatility region and gamma, avoiding unreliable boundary derivatives.

5. Replay delta hedge on simulated admissible switching-vol paths; distinguish continuous-time superhedge property from discretization residuals and quantify violations.

## Required exhibits

Convergence table; robust price intervals and constant-vol comparison; gamma/control map; discrete hedge shortfall analysis.

## Robustness

Non-convex bounds need dynamic controls, not extrema of constant vol prices. Check stability, boundary sensitivity and discrete comparison principle. Finite sampled paths do not prove superhedging. No empirical volatility-band estimate required.

## Minimum viable thesis

Monotone solver, BSM and convex benchmark, butterfly price bounds and convergence/constant-vol comparison. Hedge replay secondary if time permits.

## Optional extension

Include discrete quoted vanilla constraints or alternative uncertain-drift/transaction-cost models, keeping assumptions separate.

## Prerequisites

PDEs, stochastic control, BSM and numerical analysis; Python.

## Thesis outline

1. Model uncertainty;

2. HJB and bounds;

3. Monotone numerical methods;

4. Convex and non-convex examples;

5. Robustness and hedging.

## Milestones

W1-3: theory; W4-6: solver; W7-9: benchmark/refine; W10-12: nonconvex and hedge checks; W13-16: writing and code.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
