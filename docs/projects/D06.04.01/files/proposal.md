---
title: "Basket and Worst-of Options: The Role of Correlation"
subtitle: "Research proposal | D06.04.01"
---

**Derivatives · Numerical pricing and exotics · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Dependence affects a payoff on the average differently from a payoff on the minimum. The former depends on basket dispersion, while the latter is exposed to joint tail events. The project keeps marginal asset laws fixed and studies how admissible correlation changes alter both claims.

## Research question

How do correlation and volatility heterogeneity affect arithmetic basket calls and worst-of puts, and when does the sign of correlation sensitivity differ?

## Economic mechanism

For normalized prices $R_i=S_i(T)/S_i(0)$ compare $(\sum_iw_iR_i-K)^+$ and $(K-\min_iR_i)^+$. A correlation perturbation must preserve the marginal laws and positive semidefiniteness.

## Research design

Use two assets as the core with the prescribed correlations, strikes, maturities and heterogeneous volatilities. Compare both payoffs on paired exact terminal simulations; check the perfect-correlation limit and an independent worst-of reference.

Keep discount and marginal inputs fixed; test PSD before every bump. Examine different strikes and volatilities rather than extrapolating one correlation sign. Distinguish tail dependence from linear correlation.

\newpage

## Required exhibits

Payoff definitions; benchmark checks; correlation-price curves; sensitivity and uncertainty table; joint-tail diagnostics.

## Minimum viable thesis

Two assets, exact MC, both payoffs, five admissible correlations, perfect-correlation check and paired error bars.

## Scope and feasibility

Do not infer correlation sensitivity from a single strike or use invalid correlation matrices. Compare same marginal prices and maturity; price versus risk exposure distinction. Dependence mixture optional if exact marginal matching verified.

**Prerequisites:** Multivariate normal distribution, risk-neutral pricing, Monte Carlo, Python.

**Optional extension:** Apply results to a stylized worst-of capital-protected note with contract specified separately.

## Milestones

W1-3: payoff and model; W4-6: MC/benchmarks; W7-9: correlation grid; W10-12: sensitivity and stress; W13-16: document.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
