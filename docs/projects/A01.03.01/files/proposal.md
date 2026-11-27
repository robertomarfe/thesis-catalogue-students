---
title: "Which Stock Return Anomalies Survive Standard Factor Adjustment?"
subtitle: "Research proposal | A01.03.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Many published anomalies share securities, signals and sample periods. A credible comparison of model-adjusted returns requires a fixed universe and an explicit treatment of multiplicity, not a ranking selected after inspecting t-statistics.

## Research question

Which prespecified replicated anomalies retain nonzero alphas after common factor adjustment and dependence-aware multiplicity controls?

## Economic mechanism

For long-short anomaly payoff $L_{it}$, $L_{it}=\alpha_i+\beta_i^\top f_t+\epsilon_{it}$; the null family is $H_i:\alpha_i=0$.

## Research design

Pin a common OSAP revision for original-paper returns and SignalDoc, verify actual rights and sign definitions, freeze the original availability-based universe and 1970–2009/2010–2025 windows. Compare FF3, FF5 and FF5+Mom on common dates; report discoveries and held-out estimates separately.

Use one shared revision and record a separate SHA-256 for each OSAP file; the October 2026 route and metadata are inherited candidates, not verified. Freeze the coverage-only rule before outcomes; report exclusions, common calendar, sign and multiple-testing family. Resample entire date slices, preserving cross-anomaly dependence.

\newpage

## Required exhibits

Universe flow, alpha scatter and discovery counts, adjusted p-value table, holdout replication plot, dependence diagnostics.

## Minimum viable thesis

Pinned OSAP dictionary and returns, prespecified feasible universe, FF3/5+Mom alpha and multiplicity comparison, common held-out dates. Distinct from A12.01.01 specific liquidity signals.

## Scope and feasibility

Do not interpret historical anomalies as independently discovered or holdout as genuinely post-publication for all. OSAP portfolios use published construction, no firm-level replication, no costs. BH requires dependence conditions; BY conservative alternative.

**Prerequisites:** Factor models, HAC, multiple testing, data processing, Python.

**Optional extension:** Post-publication performance with publication dates and benchmark-adjusted economic significance.

## Milestones

W1-3: literature and file gate; W4-6: universe/data; W7-9: alpha and FDR; W10-12: holdout and null simulation; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
