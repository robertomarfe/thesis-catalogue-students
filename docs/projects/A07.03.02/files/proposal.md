---
title: "Tail Dependence in Equity Portfolios and Factor Strategies"
subtitle: "Research proposal | A07.03.02"
---

**Asset pricing · Volatility forecasting and tail risk · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Two assets with the same ordinary correlation may have very different probabilities of jointly extreme losses. A copula comparison separates the marginal distributions from dependence and asks whether Gaussian dependence understates joint downside events at observable thresholds.

## Research question

Do US equity industry portfolios and factor strategies display excess lower-tail co-exceedance relative to Gaussian copulas with the same rank dependence?

## Economic mechanism

For continuous uniform transforms $(U,V)$, finite-threshold lower-tail co-exceedance is $\chi(q)=\Pr(V\le q\mid U\le q)=C(q,q)/q$. The asymptotic coefficient is the limit as $q\downarrow0$, not a single observed tail fraction.

## Research design

Prespecify three industry and two market-factor pairs, fit Gaussian and Student-t copulas using training pseudo-observations, and compare held-out lower-tail probabilities at fixed thresholds with common-date uncertainty.

Prespecify pair labels and thresholds; do not search over pairs to obtain significant tail dependence. Report sparse counts and uncertainty, and distinguish the conditioning direction in finite samples.

\newpage

## Required exhibits

Copula scatter and tail plots, finite-q dependence table with counts/intervals, held-out calibration and sensitivity to marginal scaling.

## Minimum viable thesis

Three industry pairs and two market-factor pairs, Gaussian/t copula comparison, empirical co-exceedance and uncertainty at .05/.10. Distinct from coskewness pricing A07.03.01.

## Scope and feasibility

Do not infer asymptotic tail dependence from a single threshold. Keep short-long factor returns distinct from fully invested portfolios. Serial dependence and shared stocks limit inference; avoid multiple pair searches for significance.

**Prerequisites:** Probability, rank statistics, likelihood, time-series bootstrap, Python.

**Optional extension:** Rolling copula parameters or asymmetric Clayton/Gumbel copulas with held-out comparison.

## Milestones

W1-3: copulas and simulations; W4-6: aligned data; W7-9: estimation; W10-12: tail validation; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
