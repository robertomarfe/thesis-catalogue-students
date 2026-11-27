---
title: "Focused methods — Wrong-Way Risk and Credit Valuation Adjustment"
subtitle: "D09.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Fixed marginal default law
For the contract maturity $T$ let $Z_T=W_T/\sqrt T$ under $\mathbb Q$. With $U$ independent standard normal, $Y=\rho Z_T+\sqrt{1-\rho^2}U$ is standard normal and
$$\tau=-\lambda^{-1}\log(1-\Phi(Y)).$$
Hence survival is $e^{-\lambda t}$ for every $\rho$. Low $Y$ implies early default. Negative $\rho$ associates early default with high terminal stock shocks for a long equity forward; the actual loss effect is a joint exposure calculation. This is an ex-ante copula law, not an adapted intensity.

## Grid and reference
At zero dividends, closeout is $V_t=S_t-Ke^{-r(T-t)}$ with fair $K=S_0e^{rT}$. Let $E(t)=\mathbb E^{\mathbb Q}[e^{-rt}V_t^+]$. Independence implies the same-grid reference $(1-R)\sum_j E(t_j)[e^{-\lambda t_{j-1}}-e^{-\lambda t_j}]$. Do not discount $E(t)$ a second time. Use pre-settlement exposure at maturity and upward-rounded default. Across different contract maturities, a $Z_T$-anchored copula changes the latent horizon; do not interpret that as one fixed joint law.

## Research checks

Check marginal survival at all grid dates, exposure distributions, paired loss differences and grid refinement; distinguish dependence from changes in hazard or recovery. Contrast long and short forwards. A common latent horizon across maturities is a possible redesign, not part of the current frozen scope.
