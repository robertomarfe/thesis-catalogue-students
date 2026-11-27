---
title: "Neural Networks versus Linear Models in Financial Forecasting"
subtitle: "Research proposal | A10.02.02"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Pooling portfolios can improve effective training information, but observations in a given month share shocks. Random row splits leak common time information, and a large network may mistake cross-sectional dependence for independent evidence.

## Research question

Can a deliberately small neural network improve next-month portfolio return forecasts over linear models under date-blocked validation?

## Economic mechanism

Compare pooled ridge with portfolio intercepts to a one-hidden-layer MLP using the same information at each forecast origin.

## Research design

Use French 25 size/BM VW portfolios and FF3. Train 1970–1999, validate 2000–2009 and test 2010–2025; annual expanding refits, fixed features and five seeds, MLP widths 4/8/16. All assets of each date stay in one fold.

Assert no date appears on both sides of a fold; same test rows across models; labels mature before fitting; feature scaler learned on training only; check asset-specific mean benchmark and date-level averaging.

\newpage

## Required exhibits

Sample/split diagram, training diagnostics, per-model forecast errors, OOS R2 by portfolio, date-bootstrap intervals and seed sensitivity.

## Minimum viable thesis

French panel, same features for ridge/MLP, one locked chronological test and uncertainty across dates/seeds. Distinct from aggregate tree-based A10.02.01.

## Scope and feasibility

No random row-level cross-validation. Do not train on test labels or rescale full sample. Effective date sample is limited; repeated tuning on test invalid. Published portfolio series may be revised; no firm-level forecasts.

**Prerequisites:** Regression, basic ML, Python scikit-learn, temporal validation.

**Optional extension:** OSAP long-short panel from pinned release; compare nonlinear interactions and stability without expanding model search.

## Milestones

W1-3: theory and simulation; W4-6: data/splits; W7-9: tuning; W10-12: test and robustness; W13-16: write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
