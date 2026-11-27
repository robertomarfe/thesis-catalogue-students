---
title: "Calibrating Equity Option Surfaces with Real Market Quotes"
subtitle: "Research proposal | D02.02.02"
---

**Derivatives · Vanilla pricing and surfaces · Level 3/3**

**Data:** Empirical design blocked pending authorized access and coverage; not assignable on this design. **Status:** current review draft; supervisor approval pending.

## Motivation

Calibration results from actual option quotes depend on the economic model and on how the quotes are selected, aligned and weighted. A study of market prices must separate market microstructure and measurement choices from model differences. This proposal compares slice-based and structural models only after a genuinely usable, authorized quote panel has been established.

## Research question

How sensitive are SVI and Heston calibration and interpolation to quote cleaning, error weighting and held-out market prices on the same underlying?

## Economic mechanism

For synchronized European call and put quotes, $C-P=D(F-K)$. The parity relation is a data consistency check before any model comparison; preserve timestamp, settlement and forward conventions.

## Research design

Subject to licensed access, select 20 nonconsecutive dates and one European cash-settled index option family with synchronized forwards, bids, asks and expiry conventions. Compare flat Black, SVI and Heston on common held-out strikes. The sample file alone does not establish permission or adequate coverage.

Do not assign the original empirical design until rights, underlying/forward synchronization and accepted dates/strikes are verified. Freeze cleaning variants, objective and held-out contracts; compare identical observations and retain rejected quote counts.

\newpage

## Required exhibits

Quote coverage/exclusions table, market-fit and held-out surface panels, spread-normalized errors, parameter stability and finite-grid arbitrage checks.

## Minimum viable thesis

Permission and coverage gate, 10+ suitable dates with 3 expiries, BSM plus SVI/Heston comparison on common held-out strikes, auditable cleaning and uncertainty.

## Scope and feasibility

Bid/ask is a range, not an executable trade at mid; quotes do not ensure synchronous prices. No global arbitrage-free claim from finite grid. License may forbid redistribution. Distinct from synthetic D02.02.01.

**Prerequisites:** Options, IV inversion, nonlinear optimization, data engineering; licensed data access mandatory.

**Optional extension:** Fit a constrained surface parametrization with explicit calendar/butterfly sufficient conditions, compare pricing error.

## Milestones

W1-3: secure permission and coverage; W4-6: clean and benchmark; W7-9: calibration; W10-12: holdouts and robustness; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
