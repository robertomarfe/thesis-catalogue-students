---
title: Monetary Policy Surprises and the Stock Market
---

**A04.03.01 / Asset pricing / Empirical / Difficulty 2/3 / 16 weeks / Data gate: conditional**

Current research proposal. Not approved for assignment.

## Motivation

Monetary policy communications change expectations about short rates and the economic outlook. Measuring price changes in short announcement windows reduces contamination from unrelated news, but rate movements may still reflect information disclosed by the central bank. Comparing statements and press conferences can reveal differences in conditional market responses without assuming that the measured surprises are pure structural shocks.

## Research question

How strongly do US equity prices respond to unexpected shifts in the expected policy-rate path around FOMC communications, and does the response differ between statements and press conferences? Assess conditional associations without automatically assigning a causal structural policy shock interpretation.

## Model and economic intuition

For event $e$, denote by $s_e$ a rates-only surprise in basis points and by $y_e$ the equity return in decimal units. Estimate

$$y_e=\alpha+\beta s_e+u_e.$$

A positive surprise is defined as an increase in the expected rate path. Target and path surprises need not have the same interpretation. A response to a 25-bp move is $25\beta$ in decimal-return units. Separate the statement and conference windows; a same-meeting pair is not two independent meetings.

## Data and research design

Use the SF Fed US Monetary Policy Event-Study Database full workbook, documentation and surprises ZIP; exact release, variable labels, timestamps and rights must be checked. Statement windows are 30 minutes and conference windows 70 minutes. Match complete events by meeting, window and UTC interval; do not treat combined overlapping windows as independent. No empirical dataset is provided here.

\newpage

## Applied research programme

1. Audit event keys, time zones, window length, missing observations and units; document surprise normalization against rate changes.
2. Estimate window-specific slopes with HC3 intervals; report the scaled 25-bp response.
3. For meetings with both windows, test the slope difference using an interaction and cluster by meeting date; bootstrap dates if appropriate.
4. Predeclare regime splits and sensitivity to target/path measures. Keep influential events in the baseline.
5. Interpret association, discount-rate and information channels; do not infer structural causality from a rates-only surprise.

## Deliverables and acceptance

Coverage and matching table; rates-only surprise definition; scatterplots, coefficients and intervals; paired-window and regime comparisons. If conference coverage is insufficient, record the statement-only scope change before proceeding.

**Minimum viable thesis.** Validated downloaded USMPD file and surprise series; one transparent window-specific regression plus the matched statement/conference comparison where data allow, uncertainty and identification caveats. If press-conference coverage is too small, use statement events only and record the scope change.

## Work plan

Weeks 1--3: theory and source review; 4--6: data or numerical setup; 7--10: core implementation; 11--13: robustness; 14--16: writing and replication. Preserve the more detailed canonical milestones.

## Core reading

Acosta et al. (SF Fed Working Paper 2025-30, use exact revision); Gürkaynak, Sack and Swanson (2005); Jarociński and Karadi (2020). Consult inherited reading guide; no new full-text review is claimed.
