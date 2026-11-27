---
title: "Focused methods — The Stability of Anomaly Returns after Publication"
subtitle: "A01.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Event time and identifying variation

Let $s_i$ denote the last original-sample month and $p_i$ the verified first post-publication month. Require $s_i<p_i$ and define $I^s_{it}=1\{t>s_i\}$, $I^p_{it}=1\{t\ge p_i\}$. The middle window has $(I^s,I^p)=(1,0)$, the final window $(1,1)$. If only a publication year is verified, use January of the following year as specified. Do not impute uncertain dates.

With signal fixed effects, $b_s$ is the post-sample change and $b_p$ the incremental post-publication change; the total contrast is $b_s+b_p$. Adding calendar fixed effects absorbs common shocks and requires residual timing variation. Inspect design rank and overlap. For factor-adjusted outcomes document how exposures are estimated and propagate their uncertainty. Date blocks must preserve common shocks and labels. Selection and dissemination timing prevent a causal interpretation.

## Research checks

Retain the minimum 20 dated predictors and original minimum coverage; distinguish a permitted two-window subset from a three-window design. Log every date source and exclusion; do not equate journal publication with first dissemination or the OSAP migration with verified access.
