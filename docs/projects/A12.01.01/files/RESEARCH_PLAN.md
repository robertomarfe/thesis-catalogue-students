# Research plan | A12.01.01

## Study design and independent work

Pin same OSAP dictionary and return revision, exactly three named signals and direction; match factors/RF conventions and release-aware NFCI. Fit unconditional and interaction models on same dates; conditional alpha=a+c*z, conditional beta=b+d*z. Joint blocks and multiple-comparison sensitivity; defer if no authorized bytes.

## Prespecified implementation

Pin OSAP original-paper long-short returns and matching SignalDoc same revision; original proposed October 2026 not verified, public website accessible but repository inaccessible. Verify Illiquidity, BidAskSpread and BetaLiquidityPS names, long-short orientation, holding period and units before data outcomes; do not switch to a different signal silently. FF3/5+Mom common monthly sample, one-month lagged NFCI subject to release, revised vintage label. HAC common dates, state interaction with both alpha and factor loadings, joint calendar-block uncertainty and multiple testing. No RF subtraction for zero-cost returns; no causal liquidity-price claim.

## Required tasks

1. Freeze release, signal definitions, long/short orientation and portfolio formation metadata; inspect missingness without filling.

2. Estimate mean returns, volatility, drawdowns (clearly funded hypothetical spread convention) and factor alphas with HAC.

3. Test joint alpha restrictions with common-date block bootstrap, report Holm-adjusted individual tests.

4. Estimate NFCI-state interactions and conditional alphas with same factors; compare stable subsamples.

5. Apply transparent fixed cost hurdles as sensitivity, not estimated turnover costs, and compare alternative OSAP portfolio weighting if available.

## Required exhibits

Signal dictionary, sample and missingness audit, alpha tables, factor exposure heatmap, conditional estimates and corrected p-values.

## Robustness

October 2026 release migrated to CRSP CIZ and Hugging Face; do not splice earlier releases. Published spread direction and weighting may differ by signal; confirm documentation before interpretation. Portfolio series do not identify causal trading-cost or aggregate liquidity-risk effects. No stock-level data needed.

## Minimum viable thesis

Three prespecified liquid/illiquid-related long-short series and FF3/5+Mom alpha comparisons with inference and NFCI interaction. If files fail, hold assignment pending; substitution requires supervisor approval. Distinct from A12.01.02's BAB mechanism.

## Optional extension

Alternative equal/value weighting, turnover-aware analysis if documented turnover available, or compare to a genuine traded liquidity factor.

## Prerequisites

Factor models, regression/HAC, panel of portfolio returns, Python parquet support.

## Thesis outline

1. Liquidity and asset pricing;

2. Signal construction;

3. Factor tests;

4. Financial states and robustness;

5. Interpretation.

## Milestones

W1-3: acquire release and verify signals; W4-6: merge and descriptive checks; W7-9: factor tests; W10-12: state dependence and costs; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
