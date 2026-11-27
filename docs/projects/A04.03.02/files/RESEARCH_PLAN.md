# Research plan | A04.03.02

## Study design and independent work

Validate one actual nominal/real maturity and exact same-window surprise mapping. Estimate all three responses with identical design rows; verify intercept and slope identity beta_BE=beta_N-beta_R and compute inference on the actual difference (not by subtracting standard errors). Report unmatched counts and TIPS caveats; if overlap fails defer or seek explicit daily redesign.

## Prespecified implementation

Use same release USMPD and rate-only surprises as A04.03.01. Verify actual same-maturity nominal and TIPS changes (candidate 5y,10y), exact same response window and documented timestamp; do not pair intraday nominal with daily real. Provider research also reports daily Treasury/TIPS responses to high-frequency surprises: if intraday matching not available, require explicit supervisor approval of daily-response redesign with both daily yield series and separate shock-window label, never silently substitute. Common finite mask for s,n,r; define BE=n-r in bp, same intercept/regressors, HC3. Coefficient identity b_BE=b_N-b_R; use paired meeting bootstrap for maturity comparisons, not independent interval subtraction. Interpret breakeven as inflation compensation including liquidity/risk premia, not pure expectation. 2004-2025 proposal target conditional on verified coverage.

## Required tasks

1. Inspect codebook, units, maturity and event IDs; verify surprise construction.

2. Construct matched nominal/real/breakeven panel and sample flow.

3. Estimate responses with HC3 and meeting-cluster inference if stacked.

4. Verify coefficient identity; plot maturity responses and paired intervals.

5. Compare statement versus press conference, alternative surprise and information-effect controls; report sample changes separately.

## Required exhibits

Event coverage table, maturity response plot, component decomposition, paired confidence intervals and sensitivity.

## Robustness

Do not interpret breakeven as pure expected inflation. TIPS liquidity and information effects; event-window co-movement not automatic causal identification. Data use terms and exact real-yield maturity coverage must pass gate.

## Minimum viable thesis

One verified matched maturity, statements, three response regressions on identical events and coefficient identity.

## Optional extension

Multiple policy factors or SEP/non-SEP interactions with enough common events; adjust for multiple testing.

## Prerequisites

Bond yields, regression, event studies, Python/R.

## Thesis outline

1. Nominal/real yields;

2. Event-study design;

3. Data alignment;

4. Responses and decomposition;

5. Limits.

## Milestones

W1-3: codebook/coverage; W4-6: surprise and panel; W7-9: regressions; W10-12: communication robustness; W13-16: writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
