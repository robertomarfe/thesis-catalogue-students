---
title: "Monetary Policy and the Joint Response of Nominal and Real Yields"
subtitle: "Research proposal | A04.03.02"
---

**Asset pricing · Macro-finance and policy risk · Level 2/3**

**Data:** Empirical design conditional on actual access and coverage. **Status:** current review draft; supervisor approval pending.

## Motivation

Joint movements of nominal and real yields describe the inflation-compensation component of monetary announcement responses. A valid comparison requires the same event, maturity and response window.

## Research question

How do the matched-maturity nominal and real Treasury yield responses to FOMC surprises vary with horizon and communication window, and what is the associated breakeven response?

## Economic mechanism

For matched maturity $n$, define $\Delta BE_e(n)=\Delta y^N_e(n)-\Delta y^R_e(n)$, all in basis points, on the identical event window $e$.

## Research design

USMPD and surprises from one pinned release; statements first, candidate 5/10-year matched maturities; three same-row regressions, HC3 and meeting resampling; conference comparison only with verified coverage.

Validate one actual nominal/real maturity and exact same-window surprise mapping. Estimate all three responses with identical design rows; verify intercept and slope identity beta_BE=beta_N-beta_R and compute inference on the actual difference (not by subtracting standard errors). Report unmatched counts and TIPS caveats; if overlap fails defer or seek explicit daily redesign.

\newpage

## Required exhibits

Event coverage table, maturity response plot, component decomposition, paired confidence intervals and sensitivity.

## Minimum viable thesis

One verified matched maturity, statements, three response regressions on identical events and coefficient identity.

## Scope and feasibility

Do not interpret breakeven as pure expected inflation. TIPS liquidity and information effects; event-window co-movement not automatic causal identification. Data use terms and exact real-yield maturity coverage must pass gate.

**Prerequisites:** Bond yields, regression, event studies, Python/R.

**Optional extension:** Multiple policy factors or SEP/non-SEP interactions with enough common events; adjust for multiple testing.

## Milestones

W1-3: codebook/coverage; W4-6: surprise and panel; W7-9: regressions; W10-12: communication robustness; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
