# Research plan | A12.04.01

## Study design and independent work

Verify analytical regime boundaries, continuity and clearing with independent scalar root solution; verify trading gains and wealth identities including cap=0/infinity. Use matched noise and report binding rates, loss/negative wealth and invalid price rates for every cell. Full 50k-path experiment and endogenous wealth constraint remain student work.

## Prespecified implementation

Known F=100 at t=2, beta=1,a=.5, cap 0/1/5/20/infinity. Noise n1=rho*n0+eps, both innovations SD4, rho 0/.5/.9; 50,000 matched draws seed123. Interior p-F=n/(beta+1/a); constrained d=(n+x)/beta, x clipped. W0=20, W1=W0+x0*(p1-p0), terminal W1+x1*(F-p1). Report losses, negative wealth, binding fractions, deviation persistence and conditional profits; no liquidation before t=2 in baseline, no claim implementable unlimited arbitrage. If charging a*x^2/2 as actual holding cost label separate convention. Optional endogenous cap requires new equilibrium proof.

## Required tasks

1. Derive clearing price in interior and constrained regimes; verify numerical solution continuity and monotonicity.

2. Simulate persistent shocks on matched paths and compare price deviations, autocorrelation and binding rates.

3. Calculate interim mark-to-market and terminal trading gains, including reduced-form cost a*x^2/2 if treated as actual cost (label convention).

4. Compare no-arbitrageur, unconstrained risk-averse/holding-cost and constrained cases to separate mechanisms.

5. Vary noise volatility and persistence; report regimes where constraints amplify deviation rather than assume universal sign for profits.

## Required exhibits

Piecewise price and position diagrams, mispricing persistence table, binding-frequency and loss distributions, matched-path sensitivities.

## Robustness

Reduced-form positions and exogenous caps are not a dynamic optimal strategy; known payoff alone does not imply an implementable unlimited arbitrage. Do not claim model reproduces actual short-sale or margin behavior. No empirical evidence. Distinguish position/holding-cost assumption from wealth-based financing constraint.

## Minimum viable thesis

Closed-form clearing, two dates plus liquidation, at least three caps and noise regimes, persistence/position/loss metrics and exact residual tests.

## Optional extension

Replace fixed caps by simultaneous wealth-dependent margin constraints with explicit solvency, equilibrium selection and dynamic optimization; verify existence before simulation.

## Prerequisites

Microeconomic market clearing, asset pricing, probability and Python.

## Thesis outline

1. Noise-trader risk and limits to arbitrage;

2. Stylized market and clearing;

3. Numerical design;

4. Persistence and losses;

5. Limits of the model.

## Milestones

W1-3: literature and clearing derivation; W4-6: simulation and unit tests; W7-9: cap/persistence comparisons; W10-12: loss and sensitivity tests; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
