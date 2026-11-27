---
title: "Numerical Stability in Finite-Difference Option Pricing"
subtitle: "Research proposal | D05.02.02"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A scheme that prices a smooth claim accurately may oscillate near a vanilla kink or a digital discontinuity. Even a small price error can conceal large Greek errors. The project isolates stability, monotonicity and convergence of time-stepping schemes in the same European pricing problem.

## Research question

How do explicit, backward-Euler and Crank-Nicolson methods differ in stability, oscillations and accuracy when the option payoff is nonsmooth?

## Economic mechanism

In log spot $x$ and time to expiry $\tau$, $u_\tau=\sigma^2u_{xx}/2+(r-q-\sigma^2/2)u_x-ru$. The $\theta$-step is $(I-\theta hL)u^{n+1}=(I+(1-\theta)hL)u^n$.

## Research design

Compare explicit, backward Euler, Crank–Nicolson and Rannacher startup for calls and digitals across the original time, volatility and grid scenarios. Include deliberately unstable grids, strike alignment and separate space/time/domain refinements.

Compare analytical prices and Greeks over spot, not just ATM. A-stability does not imply positivity or accuracy. Exclude deliberately unstable runs from successful time-to-tolerance comparisons.

\newpage

## Required exhibits

Stencil/stability table, convergence rates, spot profiles of price/Greeks, oscillation figures, error-runtime tradeoffs and boundary tests.

## Minimum viable thesis

Three schemes plus Rannacher variant, European call and digital, analytical references, stable/unstable grids, separate refinement and Greek diagnostics. Distinct from D05.02.01's American optimal-stopping solver comparison.

## Scope and feasibility

For digital options derivatives near strike become steep as T approaches zero; assess at positive T and analytic Greeks. Boundary approximation and discontinuity/grid alignment can dominate convergence. A-stability is not positivity; report negative or oscillating prices rather than silently clip.

**Prerequisites:** Numerical linear algebra, PDEs, BSM and Python/SciPy.

**Optional extension:** Use a nonuniform or adaptive grid and compare efficiency for short-dated digital or barrier options.

## Milestones

W1-3: discretize PDE; W4-6: implement and verify boundaries; W7-9: stability and refinement sweeps; W10-12: Greeks, smoothing and runtime; W13-16: document and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
