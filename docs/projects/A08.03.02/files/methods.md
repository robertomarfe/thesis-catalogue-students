---
title: "Focused methods — Volatility Targeting in Equity Portfolio Management"
subtitle: "A08.03.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

At month end $w_t=\min(c,\sigma^*/\widehat\sigma_t)$. Next-month gross wealth before spread and cost is $w_tR_m+(1-w_t)R_f$.

This scales inverse standard deviation, not inverse variance. Charge an explicit monthly spread on negative cash and trade against drifted weight. Label the pretrade cost approximation. Freeze static comparator using training risk only. Report insolvencies, do not compound failed paths, and compare net CE, downside and turnover on common dates.

## Research checks

Check target/cap and funding ledger against two hand-computed periods; keep realized equity and cash returns separately, lag volatility at month end, disclose haircut cost approximation and insolvencies. Predeclare static matched-risk rule and borrowing spread; report turnover, downside, CE and paired test uncertainty.
