---
title: "Barrier Options and Discrete Monitoring Risk"
subtitle: "Research proposal | D06.01.02"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Barrier prices depend on whether a threshold is observed continuously or only at specified dates. A discrete simulation can reproduce one contract exactly while approximating another badly. Near the barrier, unobserved crossings make this economic distinction particularly important.

## Research question

How large is discrete-grid bias in pricing a continuously monitored down-and-out call, and how effectively can a Brownian bridge remove it? How does the economic price difference for a genuinely discretely monitored contract vary with barrier proximity?

## Economic mechanism

For log endpoints $x,y>b=\log B$, constant-volatility GBM bridge survival over $h$ is $1-\exp[-2(x-b)(y-b)/(\sigma^2h)]$. This concerns continuous monitoring, not a discrete contract.

## Research design

Use zero-rebate down-and-out calls at three barriers and 12/52/252 intervals, two maturities and exact GBM endpoints. Compare endpoint-only monitoring, bridge-weighted continuous monitoring and a separate analytical continuous reference.

Use paired SE on identical endpoints within each grid; 12/52/252 are not nested. Do not bridge-adjust a genuine discrete contract. Include the immediate-knockout case and retain underflow diagnostics.

\newpage

## Required exhibits

Price/error table for each grid and barrier; convergence plot; barrier-distance sensitivity figure; separate table of contractual discrete-versus-continuous price differences; one worked crossing example and numerical test log.

## Minimum viable thesis

One continuous down-and-out call type, analytical validation, three grids and barriers, MC uncertainty and clear distinction between simulation error and contractual monitoring.

## Scope and feasibility

Increase paths to separate MC error from grid bias; check survival products for underflow, immediate knock-out boundary, sigma sensitivity, and very low barrier limit to vanilla. For continuous monitoring the naive grid price is weakly above true price under identical paths, but sampling error affects comparisons. Never describe a bridge adjustment as correcting the price of a discretely monitored contract.

**Prerequisites:** Brownian motion, BSM, conditional probabilities, simulation and numerical statistics. No historical options required.

**Optional extension:** Evaluate the Broadie-Glasserman-Kou continuity correction for actual discrete-monitoring prices, or test a stochastic-volatility model where the simple GBM bridge formula is not exact.

## Milestones

W1-3: study payoffs, parity and bridge derivation; W4-6: validate vanilla/analytic barrier routines; W7-10: implement grid and bridge comparison; W11-13: convergence, limits and contractual pricing; W14-16: write and archive reproducible experiment.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
