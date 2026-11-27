---
title: "Arbitrage-Free Interpolation of Implied Volatility Smiles"
subtitle: "Research proposal | D02.03.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

An implied-volatility smile can appear smooth while implying a negative butterfly price. With sparse noisy quotes, forcing price convexity changes the fit, and the trade-off is measurable against an independently generated clean surface. This project focuses on a single expiry and on the economic meaning of finite-grid restrictions, not on global extrapolation.

## Research question

Which interpolation method balances fidelity to sparse and noisy quotes, accuracy at unobserved strikes and the absence of butterfly arbitrage? What is the cost of imposing no-arbitrage restrictions?

## Economic mechanism

On irregular strikes, call-price secants must be nondecreasing and lie in $[-D,0]$. This is a restriction on prices rather than on the visual smoothness of implied volatility.

## Research design

Generate two clean terminal distributions and noisy sparse samples at two expiries. Compare cubic IV interpolation, unconstrained price interpolation and a constrained price projection on nonuniform strikes, assessing clean held-out errors and quote adjustments. Restrict the claim to the tested interior domain.

Use irregular strike spacing, two independently constructed clean laws and fixed noise draws. Report adjustment cost and holdout recovery separately; distinguish discrete state-price mass from a differentiable density.

\newpage

## Required exhibits

Smile and call-price plots, butterfly spread/convexity maps, held-out error table, feasibility and quote-adjustment statistics, reproducible projection and diagnostic code. Include at least one example where visually smooth IV generates a violation.

## Minimum viable thesis

Correct finite-grid arbitrage restrictions, three interpolation alternatives, two clean DGPs, controlled noise experiment, held-out errors and economic interpretation of convexity. No requirement for a smooth global density.

## Scope and feasibility

Test exact BSM prices and nonuniform spacing; compare deterministic tolerance with floating-point error and verify constraints on each knot interval. Do not claim arbitrage-free extrapolation outside domain or calendar freedom for independent slices. Test price- versus vega-weighted projection with prespecified weights; report whether clean truth is inside quote intervals.

**Prerequisites:** Black-Scholes inversion, convexity, elementary linear/quadratic programming, SciPy or CVXPY.

**Optional extension:** Extend to convex spline or joint calendar-constrained normalized call surfaces with maturity-consistent forwards, and test on a second synthetic DGP or verified public quotes.

## Milestones

W1-3: derive inequalities and benchmark prices; W4-6: implement projection and interpolation tests; W7-10: run noise/sparsity grid; W11-13: stress domain and weights; W14-16: finalize reproducible figures and thesis.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
