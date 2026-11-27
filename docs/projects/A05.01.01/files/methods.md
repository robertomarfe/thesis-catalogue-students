---
title: "Focused methods — Gaussian and Square-Root Interest Rate Models: Theory and Empirical Performance"
subtitle: "A05.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Observed proxy and transition densities
For annualized decimal bill discount quote $d$ and assumed 91-day tenor, $r=-\log(1-91d/360)/(91/365)$. Document the actual quotation basis and sensitivity to tenor. For Vasicek, conditional mean is $\theta+(r-\theta)e^{-\kappa h}$ and variance is $\sigma^2(1-e^{-2\kappa h})/(2\kappa)$. For CIR, $r_{t+h}=c_h Z$ with
$$c_h=\frac{\eta^2(1-e^{-\kappa h})}{4\kappa},\quad Z\sim\chi'^2_{4\kappa\theta/\eta^2}(r_te^{-\kappa h}/c_h).$$
Use the Jacobian $1/c_h$ in the transition density. The Feller inequality $2\kappa\theta\ge\eta^2$ prevents reaching zero from a positive state; it is not required for a nonnegative CIR process. No flooring or arbitrary positive shift of observed rates.

## Pricing versus estimation
Under separately declared $\mathbb Q$ parameters, $P(t,t+\tau)=A(\tau)e^{-B(\tau)r_t}$. Physical estimates alone do not identify risk prices or bond valuations.

## Research checks

Compare held-out log scores, PIT calibration and parameter uncertainty on identical positive observations. Record optimizer failures and missing months. Distinct from A05.01.03: primary target is the whole conditional density, not conditional variance alone.
