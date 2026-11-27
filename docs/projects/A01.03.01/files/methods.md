---
title: "Focused methods — Which Stock Return Anomalies Survive Standard Factor Adjustment?"
subtitle: "A01.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Returns and the test family

Long-short payoffs $L_i$ are zero-investment spreads; do not subtract the bill return again. Freeze signed signal definitions and eligibility using metadata and coverage only. Test factor-adjusted intercepts using dependence-aware standard errors for the time series. Declare the family of $m$ hypotheses before testing.

## Multiple testing

Order p-values $p_{(1)}\le\cdots\le p_{(m)}$. At FDR target $q$, BH selects through the largest $k$ with $p_{(k)}\le kq/m$ (zero discoveries if none). BY replaces $q$ by $q/H_m$, where $H_m=\sum_{j=1}^m1/j$. BH needs independence or appropriate positive dependence; BY accommodates arbitrary dependence of valid p-values but is conservative. FDR concerns expected false-discovery proportion, not probability of any false discovery. Distinguish discovery from a later frozen replication sample; neither is a claim of implementable net profits.

## Research checks

Use one shared revision and record a separate SHA-256 for each OSAP file; the October 2026 route and metadata are inherited candidates, not verified. Freeze the coverage-only rule before outcomes; report exclusions, common calendar, sign and multiple-testing family. Resample entire date slices, preserving cross-anomaly dependence.
