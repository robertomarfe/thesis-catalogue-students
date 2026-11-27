# Research plan | A05.01.02

## Study design and independent work

Report unrestricted PCA as a rank-matched comparator. Separate same-date reconstruction from held-out maturity prediction; do not claim the fitted loading uniquely identifies physical or risk-neutral dynamics.

## Required tasks

1. Derive the rank restriction; plot loading shape and curvature implications.

2. Estimate constrained and unrestricted one-factor reconstructions and two/three-factor benchmarks.

3. Report held-out reconstruction RMSE by maturity, residual correlation and fraction of variance explained for levels and changes separately.

4. Use short-maturity-only factor extraction and compare unseen long maturities; avoid calling same-date fit forecasting.

5. Compare pre-crisis and post-crisis windows and bootstrap contiguous dates to quantify loading instability.

## Required exhibits

Yield curve examples, factor loading plot, maturity error table, residual covariance heatmap, sample split and rank diagnostics.

## Robustness

Fitted Treasury yields are already smoothed; latent dimensionality may reflect construction. Rank restriction assumes fixed parameters, affine state loadings, no measurement errors. Estimated kappa from loading shape is not a physical mean reversion estimate. No full Q calibration claimed.

## Minimum viable thesis

Six-maturity common panel, rank-one affine and PCA fit, two-factor comparison, held-out maturity errors and residual structure; distinct from A05.01.01 short-rate transition estimation.

## Optional extension

Compare ECB AAA curves or fit a jointly restricted Gaussian two-factor state-space model using both P and Q dynamics.

## Prerequisites

Bond pricing, linear algebra, least squares and Python; stochastic calculus helpful.

## Thesis outline

1. Affine pricing and rank restrictions;

2. PCA and loading estimation;

3. Data and validation design;

4. Curve reconstruction and residuals;

5. Model implications.

## Milestones

W1-3: derive rank and loadings; W4-6: curve data and PCA; W7-9: constrained reconstruction; W10-12: held-out and stability tests; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
