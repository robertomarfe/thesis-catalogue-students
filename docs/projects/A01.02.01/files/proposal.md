---
title: "Three Factors or Five? Comparing Fama-French Asset Pricing Models"
subtitle: "Research proposal | A01.02.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A larger factor model can explain more return variation without improving the pricing of expected returns. A further complication is that published FF3 and FF5 need not share identical size factors. A literal comparison and a deliberately nested comparison answer different questions.

## Research question

Does the Fama-French five-factor model improve pricing of US industry and characteristic portfolios relative to the three-factor model, and are the gains stable across samples? Do the additional factors have explanatory power conditional on common market, size and value factors?

## Economic mechanism

In $x_{it}=\alpha_i+\beta_i^\top f_t+\epsilon_{it}$, pricing concerns $\alpha_i$, while fit concerns the residual variance.

## Research design

Compare published FF3 and FF5 on the same 30 industry and secondary 25 size/value panels. Separately hold the market, SMB and HML columns from the FF5 file fixed and add RMW and CMA. Use the prespecified dates and 1999 split.

Require the monthly return blocks, matched RF and common complete calendar, positive GRS degrees of freedom, and at least the original provisional subperiod coverage. Refit paired alpha differences in joint time blocks. Document covariance singularity rather than silently regularizing the classical GRS statistic.

\newpage

## Required exhibits

Factor summary and correlation matrix; pricing-error/GRS table for common assets; alpha scatter or forest plot and portfolio-by-portfolio errors; nested comparison; subperiod and bootstrap table. Interpret any improvement in annualized return units.

## Minimum viable thesis

Reproduce FF3 and FF5 for industries plus one secondary test-asset set, compare pricing errors and joint tests on a common sample, include the nested-model check and time split. A five-factor rejection or weak improvement is a legitimate conclusion.

## Scope and feasibility

Use common dates and factor source conventions; avoid claiming causal risk factors. Report non-iid limitations of classical GRS, and do not use higher adjusted R-squared alone as evidence of better pricing. Check smaller industry set if covariance is ill-conditioned; report all selected asset sets even if results are mixed.

**Prerequisites:** Linear regression, matrix algebra, portfolio returns, multivariate hypothesis tests, pandas/statsmodels. No individual stock database necessary.

**Optional extension:** Add momentum as a common factor or compare European factors and matched regional test assets; keep currency and RF consistent. Test factor redundancy with spanning, not by deleting a factor merely because its mean is small.

## Milestones

W1-3: derive factor pricing/GRS and acquire files; W4-6: clean returns and reproduce one regression; W7-10: common-sample model comparison and nested analysis; W11-13: subperiods, bootstrap and interpretation; W14-16: draft and reproduce all results.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
