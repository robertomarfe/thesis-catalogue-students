---
title: "Focused methods — Black versus Bachelier Pricing in Low-Rate Environments"
subtitle: "D07.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Common contract and units
For displaced Black use $\widetilde F=F+s$, $\widetilde K=K+s$, both strictly positive, and $d_1=[\log(\widetilde F/\widetilde K)+\sigma_B^2u/2]/(\sigma_B\sqrt u)$, $d_2=d_1-\sigma_B\sqrt u$. Payer PV is $A[\widetilde F\Phi(d_1)-\widetilde K\Phi(d_2)]$. Normal volatility is in rate units per square root year; Black volatility is dimensionless per square root year. Compare matched prices or normal-equivalent implied vols, not raw quote magnitudes.

## Checks
Payer minus receiver equals $A(F-K)$. The shifted Black ATM price is bounded above by $A(F+s)$, so a normal target may be outside the attainable range. Holding annuity and shift fixed gives delta with respect to the forward, not full curve DV01. Check derivatives by centered bumps on the same contract and independent payoff quadrature.

## Research checks

Keep infeasible targets and strikes in a domain map. Distinguish rate-volatility pricing convention from D07.03.02 one-factor model calibration and curve risk.
