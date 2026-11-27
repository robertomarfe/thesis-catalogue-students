---
title: "Focused methods — VIX and VVIX as Indicators of Volatility Derivative Risk"
subtitle: "D08.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Different option markets
VIX and VVIX are annualized index-point measures from different option markets. Neither is a realized return or an observation of physical vol-of-vol. The broad equity proxy differs from SPX. Do not subtract the indices to estimate a premium.

## Timing and score
At close $t$, $p_t=(1+e^{-x_t^\top b})^{-1}$ uses only information available then. The outcome is known after five subsequent audited sessions. Standardize within training; choose models on validation. Compare Brier loss $(D_t-p_t)^2$, calibration and event counts on common test dates. Purge labels crossing splits. Downside semivariance is a supplementary target with a declared return convention.

## Research checks

Distinguish D03.04.02's high realized-variance event from this downside-return event. Report rare-event uncertainty and all predeclared thresholds. No traded derivative returns or causal conclusions.
