---
title: "Do Corporate Bond Spreads Forecast Economic Downturns?"
subtitle: "Research proposal | D09.03.02"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Credit-market valuations may contain forward-looking information beyond the Treasury slope. Evaluate whether credit spreads and the excess bond premium add predictive value for a dated recession outcome, relative to a base-rate and term-spread benchmark, without treating a revised series as a genuine real-time forecast.

## Research question

Do corporate credit spreads and the excess bond premium improve recession forecasts relative to the Treasury term spread?

## Economic mechanism

Define $Y_t=\mathbf 1\{\max_{1\le j\le12}\mathrm{USREC}_{t+j}=1\}$ for complete future monthly windows.

## Research design

Use the specified Fed GZ/EBP file, GS10, TB3MS and USREC; retain the one-month information lag as an approximation and the 12-month outcome horizon. Fit expanding logit models on matured labels, compare common-origin probabilities and evaluate Brier/log loss and recession episodes.

Validate the actual file columns, release metadata, units and common coverage before estimation. Preserve pseudo-OOS wording and the planned ridge sensitivity if separation occurs. No inference based solely on a convenient AUC or retrospective fit.

\newpage

## Required exhibits

Forecast probability plot, calibration plot, loss/skill table, recession episode analysis and vintage/timing audit.

## Minimum viable thesis

Public GZ/EBP and Treasury spread, expanding time-ordered logit, base-rate and term-spread comparisons, two proper scores and episode diagnostics.

## Scope and feasibility

NBER dates are retrospective and recognition is delayed; label maturation alone is not real-time availability. Latest-vintage EBP is revised and cannot establish real-time performance. Test extra training-label buffer and report scarcity of recessions. Rights review before any optional Moody's comparison.

**Prerequisites:** Fixed income, logistic regression, time series and Python.

**Optional extension:** Obtain dated predictor and recession-announcement vintages for a true real-time exercise; add permitted rating spreads only as separate robustness.

## Milestones

W1-3: literature and label design; W4-6: merge, release and unit audit; W7-9: expanding forecasts; W10-12: calibration and episode robustness; W13-16: inference, reproducibility and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
