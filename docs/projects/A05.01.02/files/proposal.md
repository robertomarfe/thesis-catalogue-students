---
title: "Can One-Factor Interest Rate Models Explain the Dynamics of the Yield Curve?"
subtitle: "Research proposal | A05.01.02"
---

**Asset pricing · Fixed income and interest rates · Level 2/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

A one-factor affine term structure forces all cross-sectional yield movements to share a single loading vector. Treasury curves may bend or twist independently. The project measures which dimensions remain unexplained and whether a model-implied loading restriction is costly relative to unconstrained statistical factors.

## Research question

How much variation across Treasury maturities can one affine factor explain, and which systematic curve movements remain unexplained?

## Economic mechanism

An affine bond price $P_t(\tau)=\exp(A(\tau)-B(\tau)x_t)$ implies $y_t(\tau)=-A(\tau)/\tau+[B(\tau)/\tau]x_t$.

## Research design

Use the six prescribed GSW maturities and chronological sample split. Fit a restricted Vasicek loading shape with free intercepts and training-estimated mean reversion; compare rank-one and higher-rank PCA. Distinguish reconstruction using contemporaneous yields from prediction of unobserved maturities using the two-year yield alone.

Report unrestricted PCA as a rank-matched comparator. Separate same-date reconstruction from held-out maturity prediction; do not claim the fitted loading uniquely identifies physical or risk-neutral dynamics.

\newpage

## Required exhibits

Yield curve examples, factor loading plot, maturity error table, residual covariance heatmap, sample split and rank diagnostics.

## Minimum viable thesis

Six-maturity common panel, rank-one affine and PCA fit, two-factor comparison, held-out maturity errors and residual structure; distinct from A05.01.01 short-rate transition estimation.

## Scope and feasibility

Fitted Treasury yields are already smoothed; latent dimensionality may reflect construction. Rank restriction assumes fixed parameters, affine state loadings, no measurement errors. Estimated kappa from loading shape is not a physical mean reversion estimate. No full Q calibration claimed.

**Prerequisites:** Bond pricing, linear algebra, least squares and Python; stochastic calculus helpful.

**Optional extension:** Compare ECB AAA curves or fit a jointly restricted Gaussian two-factor state-space model using both P and Q dynamics.

## Milestones

W1-3: derive rank and loadings; W4-6: curve data and PCA; W7-9: constrained reconstruction; W10-12: held-out and stability tests; W13-16: interpretation and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
