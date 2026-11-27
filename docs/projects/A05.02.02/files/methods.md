---
title: "Focused methods — Principal Components and the Dynamics of Government Bond Yields"
subtitle: "A05.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Statistical object
Use decimal yields or bp consistently; rescaling all maturities together leaves covariance eigenvectors unchanged. Correlation PCA standardizes each maturity, so reconstruction must reverse the training scaling. Persistent yield levels and innovations are different covariance objects.

## Stability
For orthonormal loading matrices $V,W\in\mathbb R^{m\times k}$, singular values of $V^\top W$ equal cosines of principal angles. These are invariant to signs and rotations within the subspace. Report eigenvalue gaps and held-out error by maturity. Align curves on actual common dates and quote type; US off-the-run and euro AAA issuer universes are not identical risk-free instruments.

## Research checks

Separate reconstruction from forecasting. Near tied eigenvalues, use subspace comparisons rather than interpreting a particular eigenvector as an economic structural shock.
