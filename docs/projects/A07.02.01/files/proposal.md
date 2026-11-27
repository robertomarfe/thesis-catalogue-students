---
title: "Does Downside Beta Explain Cross-Sectional Stock Returns?"
subtitle: "Research proposal | A07.02.01"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Market beta summarizes linear exposure over all observations. Investors may also care about exposure in falling markets, but incremental downside beta can be noisy and highly correlated with conventional beta. The thesis tests whether predetermined downside exposure contributes to the cross-section of subsequent portfolio returns.

## Research question

Does downside beta help explain cross-sectional mean excess returns of public US equity portfolios after controlling for conventional market beta?

## Economic mechanism

Define $\beta_i^- =\operatorname{Cov}(r_i^e,r_M^e\mid r_M^e<0)/\operatorname{Var}(r_M^e\mid r_M^e<0)$ and $d_i=\beta_i^- -\beta_i$. The added pricing slope is attached to $d_i$, not to an uncentered second moment.

## Research design

Match daily and monthly value-weighted portfolio panels. Estimate rolling daily exposures using only observations before each evaluation year and test subsequent monthly excess returns. Analyze the characteristic and industry panels separately.

Keep daily estimation and monthly evaluation distinct. Verify portfolio definitions and RF units, report conditional counts and collinearity, and do not infer individual-stock pricing or structural risk compensation from portfolio associations.

\newpage

## Required exhibits

Exposure heatmaps, conditional sample counts, beta correlation and rank plots, cross-sectional premium and error tables, generated-regressor uncertainty diagnostics.

## Minimum viable thesis

Verified daily/monthly panel, predetermined rolling betas, beta-only versus downside-augmented cross-sectional tests and a separate portfolio-panel robustness exercise.

## Scope and feasibility

No individual-stock anomaly claim from aggregate portfolios. Distinguish daily beta estimates from monthly pricing regressions; use same RF and market definitions. If conditional betas nearly collinear or imprecise, report weak incremental identification rather than forcing significance. Compare bootstrap sensitivity to block length.

**Prerequisites:** Conditional moments, factor regressions, cross-sectional econometrics and Python.

**Optional extension:** Control for size/value factor exposures or coskewness, only after baseline; avoid claiming a uniquely identified downside risk price.

## Milestones

W1-3: theory and downside beta; W4-6: align daily/monthly data; W7-9: rolling exposures; W10-12: pricing tests and bootstrap; W13-16: robustness and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
