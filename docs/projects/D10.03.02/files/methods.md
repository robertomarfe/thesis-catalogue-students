---
title: "Focused methods — Currency Hedging of US Equity Investments for Euro-Area Investors"
subtitle: "D10.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Currency and principal accounting
For initial EUR wealth one, buy $S_0$ USD of equities. Terminal EUR wealth without a hedge is $(1+R_{US})S_0/S_1$. Sell $hS_0$ USD forward for EUR at $F$ USD/EUR: the incremental EUR payoff is $hG$ with $G=S_0(1/F-1/S_1)$. Thus the net pre-cost return is $U+hG$. For $h=1$, the initial USD principal is hedged but future equity gains remain FX-sensitive. Use synthetic simple-CIP $F=S_0(1+r_{USD}\tau)/(1+r_{EUR}\tau)$ with positive accrual factors.

## Past-only hedge choice
If $\operatorname{Var}(G)>0$, the unconstrained variance-minimizing hedge ratio is $-\operatorname{Cov}(U,G)/\operatorname{Var}(G)$. The prescribed benchmark clips to $[0,1]$; estimate with at least 40 completed quarters and test after the training cutoff. Compound total US market returns including RF before conversion; do not treat overlapping monthly three-month contracts as independent quarters. Record initial capital, forward notional, cost and basis assumptions, paired uncertainty and realized risk. These are synthetic proxy contracts, not executable hedge returns.

## Research checks

Audit USD/EUR sign, full-principal identity, common dates, lagged rates and no look-ahead. Retain 60 aligned-quarter target; if unavailable agree a descriptive fixed-ratio scope. No ex-post optimized benchmark.
