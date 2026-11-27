---
title: "Focused methods — Forward Rates and Time-Varying Bond Risk Premia"
subtitle: "A05.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Common factor and return construction
Use $p_t(n)=-ny_t(n)$ and $rx_{t+12}^{(n)}=p_{t+12}(n-1)-p_t(n)-y_t(1)$, for $n=2,3,4,5$. The equal-weight average across those maturities is the target for training the forward factor. For $f_t(n)=p_t(n-1)-p_t(n)$, let $g_t=\widehat a+\widehat b^\top f_t$. Estimate maturity-specific intercepts and factor loadings without holdout labels.

## Stability and inference
Report weight profiles and predictions under the declared normalization; scaling $g_t$ changes its coefficient, not the forecast. Compare unrestricted maturity regressions using equal information. Re-estimate both stages in any resampling procedure. Overlap, predictor persistence and limited regime sample sizes matter for uncertainty.

## Research checks

Do not infer a structural factor from a good in-sample fit. Report fixed and expanding results separately, with actual eligible label counts and stability intervals.
