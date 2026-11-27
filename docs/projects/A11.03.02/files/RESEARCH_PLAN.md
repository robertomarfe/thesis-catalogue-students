# Research plan | A11.03.02

## Study design and independent work

Verify lagged calendar and actual availability of predictors; revised data do not establish a real-time exercise. Standardize with training statistics only. Include bill moments, report negativity and rank, and use paired refits to assess held-out pricing error differences.

## Required tasks

1. Derive managed portfolio equivalence and construct bill and excess moments.

2. Estimate unconditional GMM (constant instruments) and evaluate all conditional moments on identical dates.

3. Estimate augmented GMM with fixed identity and regularized HAC weights; report J statistic only with appropriate rank and identification.

4. Evaluate frozen kernels on holdout dates, compare moment RMSE and state-dependent errors; block bootstrap estimation and evaluation.

5. Assess one instrument at a time, alternative test assets and conditional b extension.

## Required exhibits

Moment definition table, rank/conditioning diagnostics, GMM parameter and J tables, state-specific pricing errors and holdout comparison.

## Robustness

Do not compare J statistics across different moments as if nested without a valid test. Bill return timing, normalization and instrument availability matter. Many instruments can overfit and make HAC singular; report effective rank and regularization. Rejection may reflect omitted risk or misspecification, not arbitrage.

## Minimum viable thesis

One factor SDF, two instruments, conditional managed-payoff moments and holdout comparison; no conditional-parameter extension required. Distinct from A11.03.01's consumption Euler estimation.

## Optional extension

Hansen-Jagannathan distance for managed portfolios or conditional factor means with disciplined instrument selection.

## Prerequisites

SDF, linear factors, GMM, HAC and matrix algebra.

## Thesis outline

1. Conditional Euler equations;

2. Instruments and GMM;

3. Data and identification;

4. Pricing tests;

5. Limitations.

## Milestones

W1-3: derive moments; W4-6: data and timing; W7-9: GMM and diagnostics; W10-12: holdout and robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
