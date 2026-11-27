---
title: "Focused methods — Conditional versus Unconditional Asset Pricing Restrictions"
subtitle: "A11.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## From conditional to managed moments

For gross bill payoff $R_{f,t}$ known at formation, $E_t[mR_{f,t}]=1$; for excess returns $x$, $E_t[mx]=0$. With $z_t=(1,dp_t,ts_t)^\top$ measurable at formation, the law of iterated expectations implies zero unconditional moments for $z_t$ times each residual. Finite instruments test selected implications, not all conditional restrictions.

Use the affine candidate $m=(1-b^\top(f-\mu_f))/R_{f,t}$, with $\mu_f$ a fixed training mean. Even with this scaling, conditional bill pricing need not hold: $E_t[mR_{f,t}-1]=-b^\top(E_t[f]-\mu_f)$. Include the bill residual with the excess moments. GMM weights and Jacobian rank depend on instrument count; compare frozen kernels on an identical evaluation moment menu rather than comparing J statistics across different menus.

## Research checks

Verify lagged calendar and actual availability of predictors; revised data do not establish a real-time exercise. Standardize with training statistics only. Include bill moments, report negativity and rank, and use paired refits to assess held-out pricing error differences.
