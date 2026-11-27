---
title: "Corporate Credit Quality Spreads and Macroeconomic Conditions"
subtitle: "Research proposal | D09.03.01"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Corporate quality spreads often widen in deteriorating economic conditions, but rating composition, maturity and liquidity can also move them. The study is descriptive: compare the Baa-Aaa yield difference across the business cycle without treating it as a pure default-risk measure.

## Research question

How do the level and changes of the Baa-Aaa quality spread relate to economic activity and financial uncertainty, and are these associations stable across recessions?

## Economic mechanism

In basis points, $s_t=100(y_t^{\mathrm{Baa}}-y_t^{\mathrm{Aaa}})$ when the published yields are in percent.

## Research design

Subject to authorized Moody's access, align the prescribed monthly BAA, AAA, INDPRO, USREC and VIXCLS. Use common samples, recession comparisons, lagged regressions in spread levels and changes, HAC uncertainty and the prespecified crisis sensitivity. Do not replace BAA/AAA silently.

This design remains blocked until the supervisor verifies rights for both Moody series and actual input coverage. Record original filename, vintage and permitted retention separately for each series. No substitute index or simulation can satisfy the unchanged empirical MVT.

\newpage

## Required exhibits

Data dictionary, spread/activity time-series figure, conditional means, regression tables with HAC intervals, subsample and episode sensitivity plots.

## Minimum viable thesis

Monthly matched panel, transparent Baa-Aaa construction, recession comparison, autoregressive and two-variable macro regressions, HAC and crisis sensitivity checks.

## Scope and feasibility

Check maturity and rating-composition caveats, source terms, units, missing values and lag choice. Spread is not a CDS premium or a pure default-risk measure. Avoid interpreting contemporaneous macro associations as causal or tradable forecasts; revised activity data are retrospective.

**Prerequisites:** Fixed income, regression, time-series diagnostics, Python or R; no individual-bond data required.

**Optional extension:** Compare with a separately licensed corporate OAS dataset or evaluate pseudo-out-of-sample prediction using dated macro vintages.

## Milestones

W1-3: theory, source terms and variable definitions; W4-6: acquisition and descriptive analysis; W7-9: benchmark and macro regressions; W10-12: persistence and crisis diagnostics; W13-16: interpretation, reproducibility and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
