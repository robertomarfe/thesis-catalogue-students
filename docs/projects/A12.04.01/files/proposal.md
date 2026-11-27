---
title: "Limits to Arbitrage and the Persistence of Mispricing"
subtitle: "Research proposal | A12.04.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Noise demand and predetermined position caps sustain deviations before liquidation. The model separates limits and interim risk without asserting an endogenous funding equilibrium.

## Research question

How do wealth or position constraints and noise persistence affect the magnitude and persistence of mispricing in a stylized finite-horizon market?

## Economic mechanism

Let $d=P-F$, noise demand $n-\beta d$, arbitrage $x=\operatorname{clip}(-d/a,-K,K)$; clearing is $n-\beta d+x=0$.

## Research design

F=100, beta=1, a=.5, caps 0/1/5/20/infinity, rho 0/.5/.9, SD4, 50,000 matched draws, W0=20; persistence, clearing and interim/terminal losses.

Verify analytical regime boundaries, continuity and clearing with independent scalar root solution; verify trading gains and wealth identities including cap=0/infinity. Use matched noise and report binding rates, loss/negative wealth and invalid price rates for every cell. Full 50k-path experiment and endogenous wealth constraint remain student work.

\newpage

## Required exhibits

Piecewise price and position diagrams, mispricing persistence table, binding-frequency and loss distributions, matched-path sensitivities.

## Minimum viable thesis

Closed-form clearing, two dates plus liquidation, at least three caps and noise regimes, persistence/position/loss metrics and exact residual tests.

## Scope and feasibility

Reduced-form positions and exogenous caps are not a dynamic optimal strategy; known payoff alone does not imply an implementable unlimited arbitrage. Do not claim model reproduces actual short-sale or margin behavior. No empirical evidence. Distinguish position/holding-cost assumption from wealth-based financing constraint.

**Prerequisites:** Microeconomic market clearing, asset pricing, probability and Python.

**Optional extension:** Replace fixed caps by simultaneous wealth-dependent margin constraints with explicit solvency, equilibrium selection and dynamic optimization; verify existence before simulation.

## Milestones

W1-3: literature and clearing derivation; W4-6: simulation and unit tests; W7-9: cap/persistence comparisons; W10-12: loss and sensitivity tests; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
