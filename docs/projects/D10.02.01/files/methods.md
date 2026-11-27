---
title: "Focused methods — Commodity Price Risk and the Minimum-Variance Hedge Ratio"
subtitle: "D10.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Minimum-variance proxy
For a fixed long exposure of one WTI barrel and a short $h$ Brent barrels, the change in matched value is $\Delta V=\Delta S_W-h\Delta S_B$. With positive Brent-change variance the unconstrained population ratio is
$$h^*=\frac{\operatorname{Cov}(\Delta S_W,\Delta S_B)}{\operatorname{Var}(\Delta S_B)}.$$
Estimate using only completed intervals before the evaluation interval; report near-zero denominator cases, allowed constraints and resulting notional. The unit-hedge residual is the change in the spot price basis. Compare variance reduction $1-\widehat{\operatorname{Var}}(\Delta V)/\widehat{\operatorname{Var}}(\Delta S_W)$ on common test dates; it may be negative.

## Price observations and limits
Use dollar changes, not log returns, as baseline, so nonpositive prices are not silently deleted. Audit different holidays, fixing times and endpoint gaps. Weekly and monthly horizons have different risk units and sample sizes. Use paired block intervals and regime counts. This design omits futures contract roll, margin and financing; it does not establish executable hedge performance.

## Research checks

Verify common observed endpoints, barrel units, no forward fill and past-only estimation at both horizons. Report basis changes, held-out risk reduction and negative results.
