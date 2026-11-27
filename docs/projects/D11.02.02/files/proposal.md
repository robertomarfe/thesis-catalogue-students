---
title: "Risk-Neutral Moments and the Limits of Option-Implied Information"
subtitle: "Research proposal | D11.02.02"
---

**Derivatives · Credit risk and incomplete markets · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Option prices can identify moments of the risk-neutral return distribution with sufficiently rich strike coverage. Empirical implementations truncate option strips and amplify noise in higher moments. The study quantifies this information loss relative to known synthetic truth and support-conditional bounds.

## Research question

How accurately can the variance, skewness and kurtosis of risk-neutral log returns be recovered from truncated and discretely sampled option strips?

## Economic mechanism

For $g(s)=\log(s/F)^j$, static replication uses put/call integrals weighted by $g''(K)$ around forward $F$.

## Research design

Use the two specified synthetic markets and exact log moments; compare strip integration on the prescribed strike intervals and grids with noise. Study a declared tail extrapolation separately and compute at least one bound under an explicit finite-support assumption.

Report absolute moment errors and cancellation across strip, tail and noise choices. Compare central moments only on admissible inputs. Record the exact support and quote tolerance for conditional bounds.

\newpage

## Required exhibits

Moment error surfaces; tail contribution plots; feasible moment intervals and matched-price examples; numerical tolerances.

## Minimum viable thesis

Analytic two-market truth, option-strip moment recovery, truncation/noise study and at least one support-conditional moment bound.

## Scope and feasibility

No finite-strike claim of model-free exact moments. LP bounds apply to declared support; log moment tails near zero may be unbounded without restrictions. Q moments not realized P risk; density recovery is not the objective (D11.02.01).

**Prerequisites:** Option pricing, integration, probability moments, constrained optimization.

**Optional extension:** Compare option-implied crash probabilities or robust bounds with additional traded strikes.

## Milestones

W1-3: spanning derivation; W4-6: generator and moments; W7-9: quadrature grids; W10-12: bounds and noise; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
