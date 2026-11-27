---
title: "Nonlinear Latent Factors and Cross-Sectional Pricing Errors"
subtitle: "Research proposal | A10.03.01"
---

**Asset pricing · Predictability and machine learning · Level 3/3**

**Data:** Empirical core; actual rights, coverage and input validation pending. **Status:** current review draft; supervisor approval pending.

## Motivation

Explaining return variance is not equivalent to pricing average returns. A characteristic-dependent factor loading can improve cross-sectional generalization, but flexible maps may fit noise or exploit test assets when constructing factors.

## Research question

Can a characteristic-conditioned nonlinear exposure map reduce held-out portfolio pricing errors relative to PCA and a linear conditional factor model at the same latent dimension?

## Economic mechanism

$r^e_{it}=b(z_i)^\top f_t+\epsilon_{it}$ separates factor payoffs from characteristic-conditioned exposures.

## Research design

Extract factors from separate 30-industry panel; fixed portfolio rank labels for 25 size/BM and 25 size/momentum. Compare constant, linear and shallow tanh loading maps at equal latent dimension. Train through 1999, tune 2000–2009 and hold out 2010–2025. OSAP optional only.

Check panel separation (including overlap in underlying portfolio constructions as limitation), training factor means and normalization; perturb held-out returns to test invariance of fitted maps. Use common error metric and dimensions; document identifiability up to rotation.

\newpage

## Required exhibits

Factor/exposure design and split audit; pricing and reconstruction errors; predicted versus realized mean plots; complexity and seed stability.

## Minimum viable thesis

Separate French factor/test panels, PCA and linear versus shallow nonlinear exposure map, chronological evaluation and distinction between pricing and reconstruction. Class B retained; core public French data, OSAP optional.

## Scope and feasibility

No factor construction from held-out target returns. Fixed characteristic ranks are coarse and do not reproduce firm-level conditional autoencoders. Low holdout sample makes average return estimates noisy; do not infer causality or genuine expected-return gains from reconstruction.

**Prerequisites:** Factor pricing, PCA, regression, basic neural networks, Python/PyTorch or sklearn.

**Optional extension:** Joint factor encoder with independent factor-construction assets, or real lagged portfolio characteristics if accessible and authorized.

## Milestones

W1-3: model/data design; W4-6: PCA and linear baseline; W7-9: nonlinear tuning; W10-12: locked evaluation; W13-16: write/reproduce.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
