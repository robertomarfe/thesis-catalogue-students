---
title: "Focused methods — Forecasting the Yield Curve: Econometric Models versus Machine Learning"
subtitle: "A05.02.03 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Temporal indexing
Predict $y_{t+h}(\tau)$, not the yield of a bond whose remaining maturity is $\tau-h$. For a forecast formed at $t$, a training example originating at $s$ is eligible only if $s+h\le t$ and its target is available. Scale features using training data; fit decay, lag choices and tuning only in training/validation. Use expanding refits with a predetermined schedule.

## Comparable losses
Compute maturity-level errors in bp and aggregate with declared weights. For each horizon and model, report the same forecast origins, paired loss differences and serial-dependence-aware uncertainty. A negative $R^2_{\mathrm{OOS}}$ is possible. Prediction of a constant-maturity yield does not itself measure a tradable excess return.

## Research checks

Implement a strong DNS baseline independently before ML. Lock temporal validation and data features, log all tuning choices and missing outcomes, and never select the final model using the final test loss.
