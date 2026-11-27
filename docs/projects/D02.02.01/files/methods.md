---
title: "Focused methods — SVI versus SABR: A Comparative Study of Implied Volatility Surface Fitting"
subtitle: "D02.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Smile coordinates
Use log-forward moneyness $k=\log(K/F)$ and total implied variance $w(k,T)=TI(k,T)^2$. Raw SVI represents a slice as
$$w=a+b\{\rho(k-m)+[(k-m)^2+s^2]^{1/2}\},$$
where $b\ge0$, $s>0$, $|\rho|<1$. Positive total variance is necessary, not sufficient for butterfly freedom. Under the forward measure SABR uses $dF=\alpha F^\beta dW$, $d\alpha=\nu\alpha dZ$, with correlation $\rho$. Fix $\beta=1$ and derive the lognormal Hagan approximation. In that case its ATM limit is $\alpha[1+(\rho\nu\alpha/4+(2-3\rho^2)\nu^2/24)T]$; evaluate the $z/\chi(z)$ term by a stable limit near $z=0$. The approximation is not exact in all wings and maturities.

## Sparse and noisy quote experiments
Generate clean Heston prices with an independent validated pricer, then perturb training quotes using the stated seeds. Compare both models using identical slices, optimizer budgets, weights and held-out strikes. When converting IV to price, test call bounds and irregular-grid convexity. Compare IV and price losses with fixed scales; record inadmissible or failed fits rather than dropping them selectively. Slice-wise success does not ensure consistency across maturities, so label the domain of each arbitrage diagnostic.

## Research checks

Freeze skew regimes, sparsity, noise scales and held-out wing strikes. Compare equal computational budgets and report invalid inversions, failed fits and finite-grid arbitrage rather than claiming smoothness implies absence of arbitrage.
