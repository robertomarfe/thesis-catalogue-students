---
title: "Focused methods — Volatility-of-Volatility and the Forecasting of Extreme Volatility"
subtitle: "D03.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Event and predictors
Let $Y_t$ be the sum of squared daily log market returns over the next calendar month. The training quantile $c$ defines the binary event $D_t=\mathbf1_{\{Y_t>c\}}$. At formation, log VIX, trailing log variance and log VVIX are predictors, not future values. Standardize them within each training fold. The intercept-only benchmark uses the matured-label event frequency (with a prespecified handling of boundary probabilities).

## Proper probability scoring
For $0<p<1$ the negative log score is $-D\log p-(1-D)\log(1-p)$; Brier loss is $(D-p)^2$. Report probability calibration, precision-recall and the number of events; the latter ranking metric is not a proper probability score. A model trained on too few events may require regularization, not a change of threshold selected from test losses.

## Research checks

Do not treat VVIX as realized equity variance. Report all nested comparisons on identical matured dates, label rights and backfill risks, and use predeclared threshold sensitivity. Retain failed or single-class training fits.
