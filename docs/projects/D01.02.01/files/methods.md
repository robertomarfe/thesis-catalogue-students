---
title: "Focused methods — Option Pricing under Stochastic Volatility: The Heston Model"
subtitle: "D01.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Heston dynamics and a pricing reference
Under $\mathbb Q$, let
$$dS_t/S_t=(r-q)dt+\sqrt{v_t}\,dW_t^S,\qquad dv_t=\kappa(\theta-v_t)dt+\xi\sqrt{v_t}\,dW_t^v,$$
with instantaneous correlation $\rho$, initial variance $v_0>0$, mean reversion $\kappa>0$, long-run variance $\theta>0$, and vol-of-vol $\xi>0$. The condition $2\kappa\theta\ge\xi^2$ ensures an inaccessible zero boundary from positive variance in the standard CIR process; its violation is not by itself a failed calibration.

With $X_T=\log(S_T/F)$, the characteristic function $\varphi(u)=\mathbb E^Q[e^{iuX_T}]$ has form $\exp(A+Bv_0)$. The Riccati system (time to maturity) is
$$B'=\tfrac12\xi^2B^2+(i\rho\xi u-\kappa)B-\tfrac12(u^2+iu),\quad A'=\kappa\theta B,$$
with zero initial conditions. Derive a Fourier representation and build an independent pricing check, including the constant-variance limit when $v_0=\theta$ and $\xi\to0$.

## Identification is not prediction
Let $\mathcal T$ be training quotes and $s_i>0$ fixed scales determined from training information (e.g., vega with a floor). Minimize $\sum_{i\in\mathcal T}[(C_i(\vartheta)-C_i^{obs})/s_i]^2$ for the parameter vector $\vartheta$. Freeze the split and scales, record objective profiles and singular values of a scaled residual Jacobian. Similar objective values may correspond to very different parameters. Independent holdouts in strikes and maturity evaluate pricing, not identification; a flat-volatility truth is a meaningful negative control.

## Research checks

Begin with a checked pricer and a two-parameter fit, then release all five parameters. Freeze an entire maturity and alternating strikes before generating noise. Report objective profiles, failed starts, parameter recovery and held-out prices as separate exhibits.
