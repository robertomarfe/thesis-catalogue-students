---
title: "Factor Spanning and the Economic Value of Additional Factors"
subtitle: "Research proposal | A01.04.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Adding a traded factor can enlarge the mean-variance opportunity set even when it does not resolve pricing errors on a chosen test-asset panel. Estimation error, leverage and transaction costs may erode the apparent in-sample improvement.

## Research question

Which additional traded factors improve the mean-variance opportunity set beyond FF3, and do gains survive out-of-sample estimation?

## Economic mechanism

If $f_2=a+Bf_1+e$, the unrestricted population squared Sharpe gain is $a^\top\Omega^{-1}a$ with $\Omega=\operatorname{Var}(e)$.

## Research design

Use FF3 and the RMW, CMA and Mom additions on common months, freezing FF3 SMB by construction. Verify the population/sample identity, test spanning jointly and compare frozen training weights through the 2000–2025 holdout.

Distinguish literal FF5 from the nested union, do not re-subtract RF from spreads, report covariance condition and separate regularization and leverage constraints from the unrestricted identity. Refit in paired time blocks across train/test segments.

\newpage

## Required exhibits

Spanning table, covariance conditioning, squared Sharpe gains with uncertainty, OOS performance and weight stability, leverage/cost sensitivity.

## Minimum viable thesis

FF3 versus FF3+RMW+CMA+Mom, identity check, joint spanning and OOS comparison. Distinct from A01.02.02 which focuses on momentum pricing errors for test assets.

## Scope and feasibility

Large in-sample Sharpe gains can be mechanical estimation artifacts; report common-sample uncertainty. Factor spreads are not directly tradable instruments and funding/transaction costs matter. FF3 and FF5 SMB differ; never interpret an unnoticed replacement as nested addition.

**Prerequisites:** Mean-variance theory, factor regressions, covariance estimation and bootstrap.

**Optional extension:** AQR BAB or OSAP portfolios as additional candidates with multiplicity control and separate sample.

## Milestones

W1-3: derive identity; W4-6: factor files and checks; W7-9: spanning and inference; W10-12: rolling allocation and sensitivity; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
