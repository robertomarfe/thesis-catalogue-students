---
title: "Robust Portfolio Optimization under Parameter Uncertainty"
subtitle: "Research proposal | A08.02.02"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Mean ambiguity penalizes exposure to poorly estimated expected returns. Robust utility and actual economic value need not rank policies the same way.

## Research question

Can uncertainty-set portfolio optimization improve realized utility and stability relative to plug-in mean-variance portfolios without excessive conservatism?

## Economic mechanism

Let $\mu=\widehat\mu+U^{1/2}z$, $\|z\|_2\leq\delta$. Worst-case mean is $w^\top\widehat\mu-\delta\sqrt{w^\top U w}$.

## Research design

10 assets, 500 replications, radius 0/1/2/4, gamma 5, optional cap .25; French 10 industries, 120-month window, 1985–99 validation and 2000–25 test.

Verify support function with explicit worst-case mean vector; radius zero nests plug-in and compare two-asset grid with KKT. Freeze radius menu, window and caps before final sample, report binding constraints, paired OOS net CE and costs with failed windows. If interpreting statistical coverage, justify dependence adjustment separately.

\newpage

## Required exhibits

Optimization validation, sensitivity frontier, simulated utility-loss table, historical net performance and weights, turnover/ambiguity trade-off.

## Minimum viable thesis

Convex robust formulation, plug-in/GMV/equal benchmarks, fixed radius protocol, controlled simulation and monthly historical backtest with net utility and turnover.

## Scope and feasibility

Mean uncertainty set does not robustify covariance unless extended; iid U may understate estimation risk. No test-set tuning or short-selling asymmetry. Historical return panels are not investable products; transaction costs illustrative. Distinct from BL subjective views and covariance-estimator comparison.

**Prerequisites:** Portfolio theory, convex optimization, statistics and Python/CVXPY.

**Optional extension:** Use bootstrap-based uncertainty sets or add covariance ambiguity, with matched constraints and nested selection.

## Milestones

W1-3: derive robust counterpart; W4-6: solver checks and data; W7-9: controlled simulations; W10-12: OOS and costs; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
