---
title: "Focused methods — Hedging with Model-Free Regression Policies"
subtitle: "D04.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Linear features and identification
Let $h_i=a_i^\top f_i$, where $f_i$ is observable at trading time. The regression design uses products $f_i\Delta\widetilde S_i$, but the future gain is not a policy input. Use training-only scaling and explicitly handle constant columns. At time zero the state is deterministic; redundant feature coefficients may not be uniquely interpretable. Check realized positions and gains, not just coefficients.

## Economic benchmark
For adapted square-integrable policies, discounted martingale gains have mean zero. Do not extend this statement to a drifted physical market. Use a common clean premium per scenario. True latent model parameters may enter an oracle comparison only, not a feasible policy.

## Research checks

Distinguish quadratic regression hedges from neural entropic-risk optimization. Test future-input perturbation, rank and conditioning, validation-only penalty choice, paired test squared loss and tails.
