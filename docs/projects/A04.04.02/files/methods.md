---
title: "Focused methods — Financial Stress and the Stock-Bond Correlation"
subtitle: "A04.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For simple holding returns and fixed stock weight $w$, portfolio variance is $w^2\sigma_S^2+(1-w)^2\sigma_B^2+2w(1-w)c_{SB}$, with conditional covariance $c_{SB}$.

Estimate covariance and correlation on the same regime dates. Relative to within-regime independence, the last term is the signed covariance contribution, not the entire diversification benefit. The monthly net zero return is $\exp[p_{t+1}(n-1/12)-p_t(n)]-1$. Construct stress from the latest eligible released weekly observation from the preceding month or earlier; observation and publication dates differ. Use fixed threshold zero or a quantile fitted only in training. Report counts, marginal risks, covariance and regime contributions with common-date blocks. Distinguish conditional description from implementable forecasts; revised stress histories imply pseudo-real-time.

## Research checks

Use a release ledger or explicitly pseudo-real-time extra lag; set threshold from fixed rule or past data. Compute exact aging bond return and nominal equity total return; report regime counts, marginal variances, covariance and 2*w_s*w_b*cov contribution with date-block inference and fixed-weight risk decomposition.
