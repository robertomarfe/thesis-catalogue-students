---
title: "Focused methods — Exchange Rate Jumps and Currency Option Smiles"
subtitle: "D10.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Compensated jump mixture
Let $J\sim N(m_J,s_J^2)$ and $N_T\sim\operatorname{Poisson}(\lambda T)$ be independent of the diffusion. The compensator is $\zeta=e^{m_J+s_J^2/2}-1$, making $E^{\mathbb Q_d}[S_T]=F=S_0e^{(r_d-r_f)T}$. Given $N_T=n$, the log-forward ratio is Gaussian with mean $-\sigma^2T/2-\lambda T\zeta+nm_J$ and variance $\sigma^2T+ns_J^2$. Weight conditional lognormal payoff values by Poisson probabilities and discount domestically. For call-tail control, monitor omitted probability and omitted stock-weighted mass (the latter corresponds to Poisson mean $\lambda T E[e^J]$).

## Match and compare
Solve the nonnegative diffusion volatility at the fixed ATM target; if jump-only price exceeds target, record infeasibility. Evaluate the same $K/F$ and maturity, invert domestic option prices with the same rates, and report skew/curvature, truncation and Monte Carlo uncertainty. For inverted FX quotes, the pricing measure changes: do not invert the process under unchanged domestic Q. Physical jump estimates alone do not identify risk-neutral jumps.

## Research checks

Check martingale, parity, zero intensity, truncation including stock-weighted tail, ATM feasibility and independent Monte Carlo. Report infeasible cases; no observed smile claim.
