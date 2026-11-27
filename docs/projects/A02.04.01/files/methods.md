---
title: "Focused methods — Does Return Predictability Translate into Better Portfolio Decisions?"
subtitle: "A02.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

A mean-variance policy sets $w_t=\operatorname{clip}(\widehat\mu_t/(\gamma\widehat\sigma_t^2),w_{min},w_{max})$ using information at $t$. Before costs, $R_{p,t+1}=R_{f,t+1}+w_t(R_{m,t+1}-R_{f,t+1})$. Define pretrade risky weight $\widetilde w_t$ from drifted holdings; a declared approximation charges $c|w_t-\widetilde w_t|$ on pretrade wealth. Monthly mean-variance certainty equivalent is $CE=\overline R_p-\gamma\widehat{\mathrm{Var}}(R_p)/2$; report the explicitly annualized convention, not an exact CRRA utility claim. Compare policies on identical dates and cost/variance assumptions.

## Identification and implementation

Absent costs, the post-return risky weight is $w_t(1+R_{m,t+1})/[1+R_{p,t+1}]$. Charge costs on the difference from the drifted weight, at formation; state the cost-on-pretrade-wealth approximation and whether the post-cost return multiplies wealth. Annualize mean-variance CE by 12, not by compounding utility. Sharpe uses excess returns; CE uses net total returns under this convention.

## Research checks

Reconcile two consecutive months manually including drifted weight and fees; no contemporaneous variance; check compounding and return units; net CE comparison on common dates; clearly label cost-on-pretrade approximation and annualization.
