---
title: "Focused methods — Expected Economic Growth and the Dynamics of Equity Risk Premia"
subtitle: "A04.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For survey vintage $q$, define expected growth from mean real GDP levels $EG_q=100[(F_qY_{q+1}/F_qY_q)^4-1]$.

This is annualized growth of mean forecast levels, not mean individual growth. At month-end origin $t$ after release, define $y_{t,h}=\sum_{j=1}^h(\log R_{m,t+j}-\log R_{b,t+j})$, where the gross market and bill legs are reconstructed separately. Fit $y_{u,h}=a+b EG_u+c dp_u+e_{u,h}$ only on origins whose targets end strictly before $t$. Compare EG-only, dp-only, joint OLS and mature historical mean on identical origins. Positive out-of-sample $R^2$ is not causal evidence. Three- and twelve-month targets overlap; use paired calendar blocks with model refits. Revised data without verified release vintages imply pseudo-real-time evaluation.

## Research checks

Create an origin/release/target-end ledger; reconstruct first three forecasts from the actual workbook, and verify mature training targets at each decision. Compare EG, dp and both on identical origins with a mature historical mean; report effective sample, overlapping h=12 sensitivity, paired loss intervals and pseudo-real-time limitation.
