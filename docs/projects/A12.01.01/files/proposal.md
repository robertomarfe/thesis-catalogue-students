---
title: "Liquidity-Related Anomalies and Factor Pricing"
subtitle: "Research proposal | A12.01.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Liquidity-related spreads may reflect risk or correlated characteristics. Factor regressions and financial-condition interactions measure residual associations, not structural liquidity causation.

## Research question

Are published liquidity-related long-short returns explained by standard factors, and do their residual returns vary with financial conditions?

## Economic mechanism

For a zero-investment spread, $r_{i,t}=a_i+b_i^\top f_t+c_i z_{t-1}+d_i^\top f_t z_{t-1}+e_{i,t}$.

## Research design

OSAP Illiquidity, BidAskSpread and BetaLiquidityPS, same authorized revision; FF3/5+Mom, lagged NFCI, common dates and interactions. No silent substitution.

Pin same OSAP dictionary and return revision, exactly three named signals and direction; match factors/RF conventions and release-aware NFCI. Fit unconditional and interaction models on same dates; conditional alpha=a+c*z, conditional beta=b+d*z. Joint blocks and multiple-comparison sensitivity; defer if no authorized bytes.

\newpage

## Required exhibits

Signal dictionary, sample and missingness audit, alpha tables, factor exposure heatmap, conditional estimates and corrected p-values.

## Minimum viable thesis

Three prespecified liquid/illiquid-related long-short series and FF3/5+Mom alpha comparisons with inference and NFCI interaction. If files fail, hold assignment pending; substitution requires supervisor approval. Distinct from A12.01.02's BAB mechanism.

## Scope and feasibility

October 2026 release migrated to CRSP CIZ and Hugging Face; do not splice earlier releases. Published spread direction and weighting may differ by signal; confirm documentation before interpretation. Portfolio series do not identify causal trading-cost or aggregate liquidity-risk effects. No stock-level data needed.

**Prerequisites:** Factor models, regression/HAC, panel of portfolio returns, Python parquet support.

**Optional extension:** Alternative equal/value weighting, turnover-aware analysis if documented turnover available, or compare to a genuine traded liquidity factor.

## Milestones

W1-3: acquire release and verify signals; W4-6: merge and descriptive checks; W7-9: factor tests; W10-12: state dependence and costs; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
