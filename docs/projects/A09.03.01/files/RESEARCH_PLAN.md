# Research plan | A09.03.01

## Study design and independent work

Inspect workbook tabs and exact periods; preserve common dates and no imputation. Fit all scales/loadings on training. Report sleeves, overlap, risk normalization and holdout uncertainty.

## Required tasks

1. Reproduce descriptive means, volatilities and correlations for value/momentum factors; distinguish same-style cross-class correlations from within-class cross-style correlations.

2. Fit PCA on training standardized factor returns, report explained variance, loadings and test reconstruction errors with frozen scaling/loadings.

3. Compare equal-weight value-only, momentum-only and balanced style portfolios across the same classes; evaluate unscaled and ex-ante volatility-scaled sleeves (training window only, leverage cap).

4. Regress class-style returns on leave-one-class-out style averages, compare alpha and residual risk; test diversification differences using paired block bootstrap.

## Required exhibits

Data coverage matrix, correlation heatmaps by style, PCA loadings and OOS variance share, portfolio risk/Sharpe table, cumulative research-factor P&L and covariance attribution. No compounded wealth for zero-cost spreads without a specified capital account.

## Robustness

Avoid including a global aggregate as both component and benchmark. Use leave-one-class-out factors to avoid mechanical self-spanning; compare different covariance windows and scale choices. Report dated sample and no claim of current performance. Correlation/PCA is not causal or proof of priced risk; provider returns may not include all implementation costs.

## Minimum viable thesis

Verified original AQR factor workbook, at least three asset classes and both styles, matched sample, correlation/PCA and portfolio diversification exercise with frozen OOS protocol; robust interpretation of risk scaling and limited replication.

## Optional extension

Use separately verified updated AQR multi-asset datasets for temporal extension; harmonize style definitions rather than splice incompatible series.

## Prerequisites

Factor investing, covariance matrices, PCA, portfolio mathematics and Python.

## Thesis outline

1. Value and momentum economics;

2. Common factors and diversification;

3. Published data and normalization;

4. Cross-class covariance and portfolio evidence;

5. Limitations and interpretation.

## Milestones

W1-3: literature and workbook gate; W4-6: clean factor matrix and reproduce descriptive statistics; W7-10: PCA and portfolio tests; W11-13: leave-one-out and uncertainty; W14-16: write and document.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
