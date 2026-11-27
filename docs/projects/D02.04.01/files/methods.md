---
title: "Focused methods — Principal Components of Implied Volatility Index Curves"
subtitle: "D02.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Curves and units
For index $I_j$ in volatility percentage points and horizon $T_j$ in years, define $v_j=(I_j/100)^2$ and $w_j=T_jv_j$. A forward-variance proxy between two maturities is $(w_b-w_a)/(T_b-T_a)$. Confirm exact methodology and maturity conventions; negative values are diagnostics. Align all series on actual exchange sessions and retain gaps. Baseline input is consecutive daily changes in annualized variance, not levels or VIX futures prices.

## Out-of-sample factor compression
Let $x_t$ be the vector of variance changes and $\bar x$ the training mean. Diagonalize the training covariance $\Sigma=L\Lambda L^\top$, ordering eigenvalues from largest to smallest. For $m$ components, the held-out reconstruction is
$$\hat x_t=\bar x+L_mL_m^\top(x_t-\bar x).$$
The test mean and covariance are not used to estimate loadings. Compare one and two factors with fixed level and slope contrasts; three components spanning three maturities mechanically reconstruct everything. Require a fourth series for a meaningful three-factor compression test. Rolling eigenvectors have arbitrary signs; compare aligned loadings and subspace angles, especially for close eigenvalues. Reconstruction is descriptive, not forecasting or causal identification.

## Research checks

Verify three distinct horizons, common eligible session changes and the sample before fitting. Freeze training centering and eigenvectors; compare compression against simple contrasts, then investigate rolling stability without interpreting arbitrary sign changes as economic reversals.
