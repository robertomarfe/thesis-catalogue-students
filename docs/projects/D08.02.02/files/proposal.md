---
title: "VIX and VVIX as Indicators of Volatility Derivative Risk"
subtitle: "Research proposal | D08.02.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A high implied-volatility level and uncertainty about that level are distinct signals. The question is whether VVIX improves near-term equity downside forecasts after controlling for VIX, not whether subtracting the two indices identifies a risk premium.

## Research question

Does VVIX contain incremental information beyond VIX about near-term equity downside risk, and are their joint stress signals stable out of sample?

## Economic mechanism

Define $D_t=\mathbf1\{\prod_{j=1}^{5}(1+R_{t+j})-1<c\}$ for the declared downside threshold $c$.

## Research design

Align authorized VIX, VVIX and French daily total returns. Freeze the five-session sampling phase, chronological splits and purge, and compare downside-event forecasts with and without VVIX on identical matured dates.

Distinguish D03.04.02's high realized-variance event from this downside-return event. Report rare-event uncertainty and all predeclared thresholds. No traded derivative returns or causal conclusions.

\newpage

## Required exhibits

Joint index scatter/time plots, event counts, coefficient and loss tables, calibration plot and held-out predictions with dates; source and target definitions.

## Minimum viable thesis

Verified common VIX/VVIX/market panel; descriptive stress analysis and incremental out-of-sample downside-event comparison with uncertainty and event counts.

## Scope and feasibility

Use several predeclared thresholds and report all; few tail events imply wide uncertainty. Market return is a broad proxy, not exactly SPX. Avoid using future stress states as predictors, converting VVIX into realized vol-of-vol or interpreting regression association causally. No actual VIX option/futures returns are used.

**Prerequisites:** Derivatives concepts, logistic regression, time-series validation and Python.

**Optional extension:** Use actual volatility derivative settlement data only after separate access and contract-roll validation; index-only conclusions remain separate.

## Milestones

W1-3: study VIX/VVIX methods; W4-5: data alignment; W6-8: descriptive and baseline models; W9-12: holdout and robustness; W13-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
