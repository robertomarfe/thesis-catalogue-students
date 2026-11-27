---
title: "Principal Components and the Dynamics of Government Bond Yields"
subtitle: "Research proposal | A05.02.02"
---

**Asset pricing · Fixed income and interest rates · Level 1/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Curve shocks across maturities often appear low-dimensional. Whether that representation remains stable across economies and episodes matters for interpreting common rate risk. This study compares covariance eigenspaces, not the forecast performance of a dynamic model.

## Research question

How stable are the dimensionality and loading shapes of government yield curves across the US and euro area and across time?

## Economic mechanism

For centered yields $Y$, covariance PCA uses $\Sigma v_j=\lambda_jv_j$ and projection $V_kV_k^\top$ onto the retained subspace.

## Research design

Build common-date US Treasury and euro-area AAA spot curves on the annual 1--10 year grid. Compare levels and adjacent-month changes, covariance versus correlation PCA, fixed training bases and rolling 60-month subspace stability.

Separate reconstruction from forecasting. Near tied eigenvalues, use subspace comparisons rather than interpreting a particular eigenvector as an economic structural shock.

\newpage

## Required exhibits

Curve comparison, scree and loading panels, held-out RMSE by maturity, principal-angle stability and sensitivity table.

## Minimum viable thesis

Common US/euro area grid, PCA on levels and changes, fixed-basis held-out reconstruction and stability comparison. Distinct from A05.02.01 forecasting and A05.01.02 model restrictions.

## Scope and feasibility

GSW and ECB curves are model-fitted smooth yields, not individual bond prices. PCA dimensionality partly reflects fitting methodology. Different currencies, issuer composition and negative yields complicate interpretation. No silent interpolation or treating same-date reconstruction as prediction.

**Prerequisites:** Bond yields, covariance, eigenvectors, basic time series and Python.

**Optional extension:** Compare DNS fixed loadings or principal components of forward curves, with additional date/grid checks.

## Milestones

W1-3: curve definitions and PCA; W4-6: acquire/align series; W7-9: level/change analysis; W10-12: held-out and robustness; W13-16: report.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
