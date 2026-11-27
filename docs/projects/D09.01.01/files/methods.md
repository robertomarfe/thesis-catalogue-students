---
title: "Focused methods — The Merton Model and the Economics of Corporate Default"
subtitle: "D09.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Terminal claims and probabilities
Under $\mathbb Q$, assume $dV/V=r\,dt+\sigma_V\,dW^{\mathbb Q}$, no payouts and deterministic $r$. Define
$$d_1^\mathbb Q=\frac{\log(V_0/F)+(r+\sigma_V^2/2)T}{\sigma_V\sqrt T},\quad d_2^\mathbb Q=d_1^\mathbb Q-\sigma_V\sqrt T.$$
The call value is $E_0=V_0\Phi(d_1^\mathbb Q)-Fe^{-rT}\Phi(d_2^\mathbb Q)$; debt is $V_0-E_0$. Here $\Phi$ is the standard normal CDF. Equivalently debt equals the risk-free promise minus a put, which is numerically useful in the far tail. Default probability is $\Phi(-d_2^\mathbb Q)$ under pricing probabilities. Under $\mathbb P$ use the asset drift $\mu$ instead of $r$ in $d_2$; do not use physical default probability in the debt pricing formula.

## Equity leverage and credit spread
Ito differentiation gives $\sigma_E=(V_0/E_0)\Phi(d_1^\mathbb Q)\sigma_V$. The promised yield is the yield on the contractual face amount, not expected realized return. Compare both default frequency and conditional loss, with a numerically stable log loss ratio when debt is nearly risk-free.

## Research checks

Verify asset-value conservation, the upper bound on debt and probability intervals. Report simulation uncertainty in rare-default cases and physical-drift sensitivity separately from risk-neutral pricing. Keep all other parameters fixed in each comparative static.
