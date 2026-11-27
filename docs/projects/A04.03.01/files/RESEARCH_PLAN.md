# Research plan | A04.03.01

## Required tasks

1. Audit unique event IDs, windows, missing rows and units; match the published surprise data by date/type and verify signs/scale against rate changes.

2. Plot equity reactions versus normalized surprises, estimate separate OLS slopes for statements and conferences with heteroskedasticity-robust intervals. Report response to +25 bp (rescale from a coefficient per bp).

3. In stacked same-day pairs test slope difference via event-type interaction, cluster by FOMC date; bootstrap by date if sample is small.

4. Prespecify regime splits (e.g. effective-lower-bound periods based on institutional dates) and target/path measures if data support. Leave extreme events in baseline and show influence sensitivity.

## Required exhibits

Event coverage table; distribution and first-stage rate-surprise correlations; scatterplots with regression fits; coefficients/intervals for a 25 bp change; paired-window comparison and regime table. Explain that sign differences may reflect information effects rather than pure policy transmission.

## Robustness

No same equity response used to construct the baseline surprise (avoid mechanical correlation); if exploring information-shock sign classification, treat it as descriptive or use independently identified shocks. Do not infer precise causal effects of policy levels from surprise variation. Distinguish percentage points, percent changes and bp; do not mix event windows.

## Minimum viable thesis

Validated downloaded USMPD file and surprise series; one transparent window-specific regression plus the matched statement/conference comparison where data allow, uncertainty and identification caveats. If press-conference coverage is too small, use statement events only and record the scope change.

## Optional extension

Reproduce the rate-only PC surprise using provided R code or Python; add 2Y/10Y yield responses and discuss transmission. A different public surprises dataset is an acceptable fallback only after reconciling definitions and windows.

## Prerequisites

OLS and robust inference, monetary policy basics, event study, pandas/statsmodels; PCA optional. No proprietary tick data needed if public extract is usable.

## Thesis outline

1. Monetary policy and asset valuation;

2. High-frequency identification and information effects;

3. Event data and estimators;

4. Equity reaction evidence;

5. Identification, robustness and conclusion.

## Milestones

W1-3: study surprise construction and acquire full USMPD release; W4-6: audit windows and reproduce summary; W7-10: estimate responses and paired comparisons; W11-13: regime/influence tests and interpretation; W14-16: document data/code and write.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
