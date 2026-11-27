# Research plan | D10.03.01

## Study design and independent work

Verify quote orientation, rate units, positive accrual, zero initial PV and reciprocal identity. Record availability and exact overlap. No observed basis or executable trade claim.

## Required tasks

1. Derive cash-and-carry with both quote orientations; demonstrate sign change when inverting rates/quote correctly.

2. Build date-aligned rates and synthetic forwards, verify units, spot/forward points and parity on flat/zero differential tests.

3. Decompose variation of log forward into log spot and log accrual ratio; report regime comparisons including negative-rate period.

4. For representative contracts compute signed value after spot/rate shocks and sensitivity to day count and hypothetical cross-currency basis, using fixed contractual K. Distinguish remaining maturity from original tenor.

## Required exhibits

Spot and synthetic forward curves/time series, forward points versus rate differential, decomposition and shock table in USD per EUR and USD notionals; precise metadata and timestamp convention. Explicitly state all forward prices are hypothetical rather than observed.

## Robustness

Check no negative accrual factors, reciprocal quote conversion and zero initial PV. Test actual calendar accrual versus 0.25 and stale versus contemporaneous monthly averages; non-synchronous observations and proxy funding differences are limitations, not arbitrage. No claim of executable CIP trades or post-crisis deviations.

## Minimum viable thesis

Verified spot and rate sources, correct parity and valuation identities, one tenor with historical synthetic points and stress/sensitivity analysis. Fallback to transparent synthetic scenarios if no overlapping rate series; empirical title/claim must then be reviewed.

## Optional extension

Use verified daily OIS/term curves or actual traded forward quotes if institutional access is available; then separately measure basis with consistent collateral, timestamps and bid-ask.

## Prerequisites

Fixed income discounting, FX conventions, elementary calculus and Python data manipulation.

## Thesis outline

1. Currency forwards and covered interest parity;

2. Discounting and quote conventions;

3. Public rate and spot proxies;

4. Synthetic forward and valuation results;

5. Market frictions and limitations.

## Milestones

W1-3: derive parity and confirm sources; W4-6: construct aligned proxies and validate identities; W7-10: historical decomposition and stress analysis; W11-13: timing/proxy robustness; W14-16: document and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
