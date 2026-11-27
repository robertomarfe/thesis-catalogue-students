---
title: "Momentum and Long-Term Reversal: Competing Return Patterns"
subtitle: "Research proposal | A12.03.01"
---

**Asset pricing · Portfolio choice, behavioral finance and market frictions · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Momentum and reversal reflect different formation horizons; published spreads differ in orientation, not necessarily holding horizon.

## Research question

Do published portfolios sorted on past returns show systematically different average spreads and factor-adjusted returns across formation windows, and how stable are the differences across market regimes?

## Economic mechanism

For common-date difference $d_t=r^A_t-r^B_t$, identical factor regressors give $\widehat\alpha_d=\widehat\alpha_A-\widehat\alpha_B$.

## Research design

French ST t-1, Mom t-12..t-2, LT t-60..t-13, FF3; CAPM/FF3 and paired differences, pre/post-1990, optional decile/recession checks.

Verify ST, Mom and LT definitions and exact units; align common dates and test the paired return/alpha difference directly with HAC/blocks. Freeze pre/post-1990 dates and report dependent returns; do not claim individual-level trading evidence or use future selection.

\newpage

## Required exhibits

Three orientation-consistent mean/alpha comparisons, factor return and cumulative P&L plots, formation-window diagram, decile profiles if available, dependence-aware paired tests and stability table. Zero-cost cumulative P&L not wealth without capital convention.

## Minimum viable thesis

Verified three factor files and FF3, aligned formation orientation, CAPM/FF3 and paired comparisons, prespecified subperiod stability, careful distinction of formation versus holding horizon. Decile analysis desirable but not mandatory.

## Scope and feasibility

No inference that the same stock reverses after momentum from unrelated sorted portfolios; no causal identification of investor psychology. Factor construction, skip months, rebalance frequency, microstructure and costs differ. Do not subtract RF from zero-cost factors, or claim net tradable performance. Common sample and alternate HAC bandwidth; report uncertainty and publication-vintage limitations.

**Prerequisites:** Factor models, portfolio returns, OLS/HAC and Python data handling.

**Optional extension:** Use individual-stock signal histories from a verified public replication package to trace within-stock horizon dynamics, avoiding look-ahead and survivorship; do not assume such files accessible in core.

## Milestones

W1-3: read literature and verify windows; W4-6: clean factor and portfolio series; W7-10: descriptive and alpha comparisons; W11-13: uncertainty, subsamples and cost caveats; W14-16: write and reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
