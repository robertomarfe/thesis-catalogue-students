---
title: "Momentum and the Limits of Fundamental Factor Models"
subtitle: "Research proposal | A01.02.02"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Momentum is a useful test of whether fundamental factor models price return patterns not already spanned by their factors. Momentum-sorted portfolios and industries provide different test-asset constructions but share underlying securities. A successful addition need not identify a structural risk.

## Research question

Does a traded momentum factor improve the pricing of momentum portfolios and independent industry portfolios relative to FF3 and FF5, and how stable is the improvement?

## Economic mechanism

Test the spanning restriction $\alpha_{Mom}=0$ in $Mom_t=\alpha_{Mom}+b^\top f_t+u_t$, separately from the changes in test-asset alphas.

## Research design

Estimate the two nested pairs FF3 versus FF3+Mom and FF5 versus FF5+Mom, holding base columns fixed. Keep the 25 size/momentum and 30 industry panels separate, common months within each comparison, and the 1994 split.

Use the same base SMB within each nested pair and same RF for long-only test assets. Report two separate panels and paired uncertainty; distinguish momentum-formation sorts from evidence outside those sorts, without calling industries statistically independent.

\newpage

## Required exhibits

Spanning and pricing error tables, alpha heatmaps, nested-model comparison, GRS/conditioning diagnostics and stability estimates.

## Minimum viable thesis

Both nested pairs, Mom spanning, two test panels, common sample alpha comparisons and robust uncertainty. Distinct from A01.02.01 FF3 vs FF5 and A12.03.01 momentum/reversal payoffs.

## Scope and feasibility

Momentum-sorted portfolios share construction ingredients with Mom, so fit can be mechanical; industry evidence is not fully independent at stock level. Higher R2 is not evidence of lower pricing errors. Do not assert FF3 strictly nested in FF5. No causal risk/behavioral identification.

**Prerequisites:** Asset pricing factors, multivariate regression, inference and Python.

**Optional extension:** Compare additional publicly available test assets or momentum crash states using predeclared dates; distinguish factor spanning from economic explanations.

## Milestones

W1-3: literature and hypotheses; W4-6: data alignment; W7-9: spanning and pricing regressions; W10-12: tests and stability; W13-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
