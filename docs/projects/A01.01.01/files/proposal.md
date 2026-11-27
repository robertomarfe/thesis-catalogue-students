---
title: "Testing the CAPM across Size and Value Portfolios"
subtitle: "Research proposal | A01.01.01"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

The CAPM imposes a joint restriction on expected returns, not merely on their comovement with the market. Size and value portfolios provide a deliberately challenging test of that restriction. An industry panel changes the test assets without pretending that the underlying stocks are independent.

## Research question

Does market beta account for differences in average excess returns across size and book-to-market portfolios? How sensitive is the conclusion to test assets and inference?

## Economic mechanism

For monthly excess returns $x_{it}=R_{it}-r_{ft}$, the CAPM implies $E[x_i]=\beta_iE[x_M]$ and a zero intercept in the market regression.

## Research design

Use the prescribed 25 value-weighted size/book-to-market portfolios and common market and bill series over July 1963–December 2025 where available. Compare pricing errors, the security market line and joint inference; use industries separately and retain the 1993 break.

Use one RF subtraction, common complete dates and separate portfolio panels. Report T, N, K, eigenvalues and failed draws. Re-estimate both regression passes in joint date blocks; do not interpret a rejected joint hypothesis as proof of inefficiency.

\newpage

## Required exhibits

Beta/alpha heatmaps, GRS and robust joint test table, security market line scatter, pricing error summary, beta uncertainty and sample split results.

## Minimum viable thesis

One full 25-portfolio panel, derivation, alpha tests, security market line and cross-sectional inference with a separate industry or temporal robustness panel.

## Scope and feasibility

Use a common month index and risk-free series; test equal-weighted size/value portfolios separately, not mixed with value-weighted series. Do not interpret GRS rejection as a unique rejection of rationality; market proxy and joint hypothesis matter. Bootstrap entire time slices jointly; report near-singular matrices.

**Prerequisites:** OLS, multivariate statistics, portfolio theory, Python statsmodels/NumPy.

**Optional extension:** Use rolling or conditional betas, but retain the unconditional CAPM as the primary object.

## Milestones

W1-3: CAPM and test derivations; W4-5: construct portfolio panel; W6-8: estimate alpha/beta and GRS; W9-12: two-pass and bootstrap; W13-16: robustness and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
