---
title: "Focused methods — Momentum and the Limits of Fundamental Factor Models"
subtitle: "A01.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Incremental pricing

In each pair estimate $x_{it}=\alpha_i+\beta_i^\top f_t+\epsilon_{it}$ and $x_{it}=\alpha_i^++\beta_i^{+\top}f_t+c_iMom_t+\epsilon_{it}^+$. Addition of a regressor cannot lower the in-sample unadjusted $R^2$; it need not reduce the joint vector of pricing errors. Compare $\mathrm{RMSE}_\alpha$ and paired individual alphas. A GRS rejection tests all alphas jointly under its maintained assumptions.

## Factor spanning

Regress the traded momentum spread on the same base factors. The intercept measures the mean of its residual payoff after a linear factor hedge. The spanning restriction is not equivalent to pricing the two panels. Moment estimates and residual covariances share dates, so re-estimate both nested models and the spanning regression on common resampled time blocks. The published Mom series is already a long-short payoff.

## Research checks

Use the same base SMB within each nested pair and same RF for long-only test assets. Report two separate panels and paired uncertainty; distinguish momentum-formation sorts from evidence outside those sorts, without calling industries statistically independent.
