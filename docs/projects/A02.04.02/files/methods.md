---
title: "Focused methods — Predicting the Distribution Rather Than the Mean of Stock Returns"
subtitle: "A02.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For $q\in\{0.10,0.50,0.90\}$, estimate conditional quantile $Q_q(y_{t+1}|x_t)=a_q+b_q^\top x_t$ on matured data by minimizing $\sum_s\rho_q(y_{s+1}-Q_q(x_s))$, where $\rho_q(u)=u(q-\mathbf1\{u<0\})$. Compare pinball loss against empirical historical quantiles and a rolling 60-month Gaussian location-scale benchmark calibrated only on available outcomes. Coverage is $\frac1T\sum_t\mathbf1\{y_{t+1}\le\widehat Q_{q,t}\}$. Report crossing separately; a declared monotone rearrangement is a sensitivity rather than a hidden correction.

## Identification and implementation

For an 80% central interval $[l,u]$, the interval score is $(u-l)+10(l-y)\mathbf{1}\{y<l\}+10(y-u)\mathbf{1}\{y>u\}$. Report marginal coverage and conditional exceedance behavior separately. VIX is an implied risk-neutral volatility indicator, not a physical quantile. Do not infer expected shortfall from three quantiles.

## Research checks

Hand-check pinball loss for positive and negative residuals and empirical quantile convention. Check VIX availability and no future data. Test crossing detection, report event counts, no post-test choice of quantile or rearrangement.
