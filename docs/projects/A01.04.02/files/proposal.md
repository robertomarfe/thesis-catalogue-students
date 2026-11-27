---
title: "Principal Components versus Observable Asset Pricing Factors"
subtitle: "Research proposal | A01.04.02"
---

**Asset pricing · Cross-sectional pricing and SDF · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Principal components extract directions of high return variance, whereas an asset-pricing model must explain mean returns. An equal-dimensional, frozen comparison on later dates and distinct portfolio constructions separates covariance reconstruction from pricing.

## Research question

At equal factor dimension, do principal-component factors estimated on training assets produce smaller held-out pricing errors than observable FF factors?

## Economic mechanism

With training covariance $\widehat\Sigma=V\Lambda V^\top$, fixed portfolio weights $V_k$ produce traded excess factors $f_t=V_k^\top x_t$.

## Research design

Use industry training portfolios and French factors with the original 1970–1999 fit, 2000–2009 validation and 2010–2025 test. Compare PC3 and FF3, with equal-dimensional PC5/FF5 sensitivity, frozen dates and held-out size/value assets.

Freeze factor dimensions, weights, means and model selection before the test. Audit date and asset holdouts separately, report factor return scaling and rank, and retain common pricing moments. Optional OSAP alternative requires its own access verification.

\newpage

## Required exhibits

Eigenvalue plot, factor correlations, held-out pricing RMSE/alpha table, split audit and stability.

## Minimum viable thesis

PC3 and FF3 on French panels, one frozen date/asset holdout and pricing versus covariance comparison.

## Scope and feasibility

PC weights do not identify economic shocks; common underlying equities prevent independent-security interpretation. FF3 versus FF5 are not automatically nested. Same test dates/assets and dimensions, no future data leakage.

**Prerequisites:** Linear algebra, factor models, regression, Python.

**Optional extension:** OSAP training universe and sparse statistical factors; preserve independent validation dates and candidate selection.

## Milestones

W1-3: PCA and data; W4-6: factor construction; W7-9: pricing fit; W10-12: evaluation; W13-16: writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
