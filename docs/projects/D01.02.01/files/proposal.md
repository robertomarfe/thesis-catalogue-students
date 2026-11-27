---
title: "Option Pricing under Stochastic Volatility: The Heston Model"
subtitle: "Research proposal | D01.02.01"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A stochastic-volatility model adds economically meaningful degrees of freedom, but a low pricing residual does not establish that the corresponding parameters are precisely identified. Strike coverage informs asymmetry and curvature; maturity coverage informs the variance dynamics. The project studies whether additional information improves held-out valuation even when the parameter estimates themselves remain imprecise.

## Research question

When does stochastic volatility improve pricing beyond constant volatility, and which dimensions of a cross-section of European options identify its parameters? Assess the hypothesis that strike and maturity coverage jointly improve held-out pricing, even when parameter recovery remains weak.

## Economic mechanism

Heston introduces the variance state $v_t$ with $dv_t=\kappa(\theta-v_t)dt+\xi\sqrt{v_t}dW_t^v$. Its parameters affect both the pricing law and the conditioning of the calibration problem; the latter must be assessed separately from held-out error.

## Research design

Generate synthetic calls for a known Heston economy over four maturities and multiple strikes. Retain alternating strikes and an entire maturity as tests. Fit constant volatility and Heston on identical training quotes under noise-free and noisy designs, including a flat-volatility truth as a negative control.

Begin with a checked pricer and a two-parameter fit, then release all five parameters. Freeze an entire maturity and alternating strikes before generating noise. Report objective profiles, failed starts, parameter recovery and held-out prices as separate exhibits.

\newpage

## Required exhibits

Table of true and fitted parameters with dispersion and training/test errors; smile-by-maturity panels; objective-profile figure for kappa/theta or xi/rho; numerical validation log. Interpret fit improvements relative to the known noise scale, not only percentage changes.

## Minimum viable thesis

A correct BSM and Heston pricer, one full noise-free and one noisy calibration experiment, a prespecified holdout, and a defensible explanation of parameter recovery versus predictive pricing. Pass numerical tests before interpreting calibration. A null improvement is informative under the flat-volatility generating model.

## Scope and feasibility

Check quadrature truncation, alternate initializations, quote weighting, Feller-constrained versus unconstrained (with valid numerical pricing), strike-only versus maturity holdout, and stress a low-skew scenario. Do not describe synthetic holdout fit as market evidence. Never reuse the held-out quotes to choose weights or parameter bounds.

**Prerequisites:** Risk-neutral pricing, Ito calculus, numerical integration, nonlinear optimization, Python/NumPy/SciPy. The characteristic-function derivation is the advanced element; use a published formula if needed and explain its logic.

**Optional extension:** Optionally add a second synthetic generator (Merton jumps) to examine misspecification or a single documented free quote snapshot if available; keep actual-market validation clearly separate.

## Milestones

W1-3: derive pricing equations and reproduce BSM tests; W4-6: implement/validate characteristic function and freeze surface design; W7-10: calibrate with multistart and noise repetitions, lock test set; W11-13: profile parameters and stress scenarios; W14-16: interpret, write, reproduce all exhibits from a clean run.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
