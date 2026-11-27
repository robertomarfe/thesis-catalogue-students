---
title: "Volatility-of-Volatility and the Forecasting of Extreme Volatility"
subtitle: "Research proposal | D03.04.02"
---

**Derivatives · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

High volatility and uncertainty about volatility are distinct phenomena. VVIX measures option-implied variation of the volatility index; its incremental forecasting value should be assessed after controlling for the prevailing VIX level and past market variance. The focus is calibrated tail-event probabilities.

## Research question

Does VVIX incrementally forecast extreme physical volatility over the next month after controlling for VIX and lagged realized variance?

## Economic mechanism

Define $D_{t+1}=\mathbf1_{\{Y_{t,\mathrm{month}}>c\}}$ with $c$ fixed from initial training. Compare nested logistic forecasts $p_t=\{1+\exp(-x_t^\top b)\}^{-1}$ with and without lagged VVIX.

## Research design

Use the common observed VIX, VVIX and market dates with no interpolation. Freeze the training threshold, compare intercept-only and nested models, and choose regularization without consulting final-period outcomes.

Do not treat VVIX as realized equity variance. Report all nested comparisons on identical matured dates, label rights and backfill risks, and use predeclared threshold sensitivity. Retain failed or single-class training fits.

\newpage

## Required exhibits

Tail-probability paths, calibration plot, paired scores, event counts, coefficient stability and coverage audit.

## Minimum viable thesis

Two nested logistic forecasts plus unconditional benchmark, common dates and at least two proper scores.

## Scope and feasibility

Limited extreme events and backfilled index history constrain inference. No Q=P identification or causal mechanism. Do not optimize tail threshold on test dates; rights and actual VVIX history must be confirmed.

**Prerequisites:** Probability, logistic regression, time-series forecasting, Python.

**Optional extension:** Add trailing realized variation of VIX as a physical proxy, with lagged availability and matched horizon.

## Milestones

W1-3: data and labels; W4-6: baseline; W7-9: VVIX forecasts; W10-12: score and calibration; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
