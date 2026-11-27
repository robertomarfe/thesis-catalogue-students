---
title: "Focused methods — Nonlinear Latent Factors and Cross-Sectional Pricing Errors"
subtitle: "A10.03.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Write $r^e_{i,t+1}=b(z_{i,t})^\top f_{t+1}+\epsilon_{i,t+1}$, with latent dimension $K$ fixed across models. A linear map has $b(z)=Bz$; a shallow nonlinear map uses a shallow tanh network and a declared ridge penalty. For expected-return prediction use training-only factor mean $\widehat\mu_f$ and frozen loadings: $\widehat m_{i,t}=\widehat b(z_{i,t})^\top\widehat\mu_f$. Pricing errors summarize average realized excess returns minus predicted means on held-out assets/dates. Contemporaneous reconstruction uses realized factors and is a different estimand. Fix normalization and sign/rotation convention using training data.

## Identification and implementation

PCA weights on the industry panel must be fit once on training data. Training normalization removes scale ambiguity but not arbitrary rotations without a convention; compare pricing errors on later dates and keep reconstruction RMSE distinct. Do not refit factor means or maps on test outcomes or claim full IPCA/autoencoder replication.

## Research checks

Check panel separation (including overlap in underlying portfolio constructions as limitation), training factor means and normalization; perturb held-out returns to test invariance of fitted maps. Use common error metric and dimensions; document identifiability up to rotation.
