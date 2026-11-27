---
title: "The Convexity Adjustment in Volatility Swap Pricing"
subtitle: "Research proposal | D08.01.02"
---

**Derivatives · Hedging and volatility derivatives · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A volatility swap is sensitive to the distribution of future integrated variance rather than only its expectation. The research measures when a second-order convexity adjustment is economically adequate and when a nonlinear numerical benchmark is needed.

## Research question

How does volatility-of-volatility, maturity and mean reversion affect the convexity adjustment in volatility swap pricing?

## Economic mechanism

For $V_T=T^{-1}\int_0^T v_s ds$, the fair volatility strike is $\mathbb E^{\mathbb Q}\sqrt{V_T}$, not $\sqrt{\mathbb E^{\mathbb Q}V_T}$.

## Research design

Use exact CIR transitions and refined integration, including the deterministic limit. Compare Jensen gap and second-order approximation across maturity and vol-of-vol with independent MC precision and integration diagnostics.

Unlike the VIX futures project, the random quantity is realized integrated variance over the entire swap horizon. Report economic errors in volatility points, not only variance units.

\newpage

## Required exhibits

Strike and gap tables, distribution of I and sqrt(I), maturity/vol-of-vol sensitivity maps, MC precision and approximation-error plots.

## Minimum viable thesis

Analytic mean, validated simulation, exact Jensen comparison, second-order approximation and numerical sensitivity to at least maturity and xi.

## Scope and feasibility

Use annualized variance consistently and quote vol points as 100*sqrt(I). No Jensen reversal from sampling noise when strikes use same paths. Test deterministic-variance limit and time-grid bias. No observed swap quotes or calibration claimed.

**Prerequisites:** Risk-neutral pricing, stochastic calculus basics, Monte Carlo and Python.

**Optional extension:** Study a discrete-return realized-variance convention in a full Heston price simulation, with monitoring and convexity corrections separated.

## Milestones

W1-3: contracts and expansion; W4-6: CIR simulation and mean checks; W7-9: sensitivity experiments; W10-12: approximation, MC and grid errors; W13-16: economic interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
