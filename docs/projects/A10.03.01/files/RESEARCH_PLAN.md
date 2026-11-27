# Research plan | A10.03.01

## Study design and independent work

Check panel separation (including overlap in underlying portfolio constructions as limitation), training factor means and normalization; perturb held-out returns to test invariance of fitted maps. Use common error metric and dimensions; document identifiability up to rotation.

## Prespecified implementation

Use separate 30 industry panel for PCA raw factor payoffs (frozen training weights), train loading maps on 25 size/BM and size/momentum portfolios with documented ranks. Compare constant and linear rank maps versus shallow tanh at same k; normalize factor columns using training, freeze weights and training means. Ex-post reconstruction uses contemporaneous f; expected return prediction uses training factor means. Record no test-date fitting. Optional OSAP not core.

## Required tasks

1. Validate panel, rank labels, factor excess returns and common sample.

2. Fit PCA k=1,3,5 on training industry panel; estimate unconstrained constant loadings and characteristic-linear loading map on training test portfolios.

3. Fit shallow b(z) with one hidden layer, regularization and locked validation; same PCA factors first to isolate nonlinearity, joint encoder optional.

4. Evaluate holdout reconstruction RMSE, mean residuals and pricing RMSE using training factor means; separately report ex-post factor realizations and true expected-return prediction.

5. Joint date block bootstrap and sensitivity to k, seeds, training period and architecture; compare FF factor alphas on same assets.

## Required exhibits

Factor/exposure design and split audit; pricing and reconstruction errors; predicted versus realized mean plots; complexity and seed stability.

## Robustness

No factor construction from held-out target returns. Fixed characteristic ranks are coarse and do not reproduce firm-level conditional autoencoders. Low holdout sample makes average return estimates noisy; do not infer causality or genuine expected-return gains from reconstruction.

## Minimum viable thesis

Separate French factor/test panels, PCA and linear versus shallow nonlinear exposure map, chronological evaluation and distinction between pricing and reconstruction. Class B retained; core public French data, OSAP optional.

## Optional extension

Joint factor encoder with independent factor-construction assets, or real lagged portfolio characteristics if accessible and authorized.

## Prerequisites

Factor pricing, PCA, regression, basic neural networks, Python/PyTorch or sklearn.

## Thesis outline

1. Latent factor pricing;

2. Linear/nonlinear exposure maps;

3. Panels and validation;

4. Pricing versus fit;

5. Limits.

## Milestones

W1-3: model/data design; W4-6: PCA and linear baseline; W7-9: nonlinear tuning; W10-12: locked evaluation; W13-16: write/reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
