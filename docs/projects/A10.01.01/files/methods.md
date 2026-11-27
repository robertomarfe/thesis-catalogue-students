---
title: "Focused methods — Regularized Regressions for Equity Premium Forecasting"
subtitle: "A10.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For training-standardized $z_s$, minimize $L(a,b)+\alpha P_\eta(b)$, where

$$L(a,b)=\frac{1}{2n}\sum_s(y_{s+1}-a-z_s^\top b)^2,$$

$$P_\eta(b)=(1-\eta)\|b\|_2^2/2+\eta\|b\|_1.$$ Ridge has $\eta=0$, LASSO $\eta=1$; elastic net is optional. Intercept is unpenalized. Record the exact library scaling of $\alpha$. Choose penalties on matured chronological inner validation folds only, then refit on eligible training history; the final test block is for evaluation, not method selection.

## Identification and implementation

With objective $\mathrm{SSE}/(2n)+\alpha\|b\|_2^2/2$, the equivalent Ridge implementation using $\mathrm{SSE}+\lambda\|b\|_2^2$ has $\lambda=n\alpha$. LASSO commonly uses the first loss scaling. Record the actual estimator convention, not a shared numerical penalty across libraries.

## Research checks

Persist scaler means/SD and mature fold IDs; perturb future features and immature labels; earlier tuning and forecasts must be invariant. Check zero penalty against OLS when rank permits; document alpha conventions and zero-variance features.
