---
title: "Conditional versus Unconditional Asset Pricing Restrictions"
subtitle: "Research proposal | A11.03.02"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A model may price average returns while failing to price returns conditional on information known when portfolios are formed. Managed payoffs make these conditional restrictions testable, provided instrument timing and the kernel normalization are explicit.

## Research question

Do predetermined valuation and interest-rate instruments reveal conditional pricing errors that an unconditional factor SDF hides?

## Economic mechanism

If $E_t[m_{t+1}x_{t+1}]=0$, then $E[z_t\otimes(m_{t+1}x_{t+1})]=0$ for integrable predetermined instruments.

## Research design

Use FF3, the prescribed fixed industry panel and lagged valuation and term-spread instruments. Freeze training standardization and compare unconditional and managed-payoff moments on the same later dates; conditional coefficient extension remains optional.

Verify lagged calendar and actual availability of predictors; revised data do not establish a real-time exercise. Standardize with training statistics only. Include bill moments, report negativity and rank, and use paired refits to assess held-out pricing error differences.

\newpage

## Required exhibits

Moment definition table, rank/conditioning diagnostics, GMM parameter and J tables, state-specific pricing errors and holdout comparison.

## Minimum viable thesis

One factor SDF, two instruments, conditional managed-payoff moments and holdout comparison; no conditional-parameter extension required. Distinct from A11.03.01's consumption Euler estimation.

## Scope and feasibility

Do not compare J statistics across different moments as if nested without a valid test. Bill return timing, normalization and instrument availability matter. Many instruments can overfit and make HAC singular; report effective rank and regularization. Rejection may reflect omitted risk or misspecification, not arbitrage.

**Prerequisites:** SDF, linear factors, GMM, HAC and matrix algebra.

**Optional extension:** Hansen-Jagannathan distance for managed portfolios or conditional factor means with disciplined instrument selection.

## Milestones

W1-3: derive moments; W4-6: data and timing; W7-9: GMM and diagnostics; W10-12: holdout and robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
