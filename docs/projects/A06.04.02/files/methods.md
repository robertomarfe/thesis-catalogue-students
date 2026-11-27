---
title: "Focused methods — Cash Flow News and Discount Rate News in Aggregate Stock Returns"
subtitle: "A06.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For centered return-first VAR $X_{t+1}=AX_t+u_{t+1}$, discount-rate news at horizon $H$ is $N_{DR}=e_1^\top\sum_{j=1}^H\rho^j A^j u_{t+1}$.

Residual cash-flow news is $N_{CF}=e_1^\top u_{t+1}+N_{DR}$, so return innovation equals $N_{CF}-N_{DR}$. The variance identity includes $-2\operatorname{Cov}(N_{CF},N_{DR})$. Infinite discounted news uses $\rho A(I-\rho A)^{-1}$ only when the discounted spectral radius is below one; require a stable VAR for the maintained stationary interpretation. Finite residual news absorbs terminal and approximation errors. Refit VAR and rho in resampling; report unstable draws. This is not an independently identified cash-flow shock.

## Research checks

Use return-first VAR, stable roots, same calendar and real gross convention; verify direct discounted sums and signed Var(CF)+Var(DR)-2Cov identity, report finite and infinite estimates, horizon and information-set sensitivity. Refit rho and VAR inside bootstrap, retain inadmissible draws and note weak stability near unit roots.
