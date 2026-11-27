# Research plan | A06.01.02

## Study design and independent work

Use exact annual timing and report accounting residual before log-linear residual; retain signs [future r,-future g,-residual,terminal]. Compare direct finite sums with loadings, covariance shares including negative terms and terminal, and unstable bootstrap draws; if payout data cannot be matched to return convention, stop or obtain approval for clearly labeled proxy.

## Prespecified implementation

Original z=log(D/P); pd_identity uses log(P/D) internally, negate returned z before VAR. Compute exact accounting residual using annual gross return versus (P_t+D_t)/P_prev, then loglinear residual. Fit VAR on [z,g,r] annual contiguous data; dp_pv_loadings returns [r,-g,-e,terminal] loadings; covariance with z divided by Var(z) gives signed shares, not positive normalized percentages. Report centered-state identity separately from raw sample accounting residual, stable discounted limit, direct forecast regressions, block/VAR bootstrap refitting rho; no silently discarded unstable draws. Annual Goyal raw variables verify definitions; documented proxy only if exact absent and supervisor approves.

## Required tasks

1. Audit annual timing, dividend definitions and exact versus approximate log-return identity.

2. Estimate small VAR and discounted forecast sums; report return, negative-growth, terminal and residual contributions to variance.

3. Compare direct long-horizon forecasting regressions and VAR-implied coefficients.

4. Bootstrap jointly by blocks or stable VAR residuals, recomputing rho and coefficients; report wide intervals and instability.

5. Repeat post-1946, alternative lag and nominal versus consistently deflated real quantities if available.

## Required exhibits

Valuation ratio history, identity-residual plot, horizon contribution table including terminal term, VAR coefficients and bootstrap uncertainty.

## Robustness

Small annual sample and near-unit-root valuations create bias; no causal cash-flow/discount-rate shocks identified. Do not treat rolling annual dividend observations as monthly payouts. Preserve timing; avoid ignoring terminal terms or linearization residual to force shares to sum to one.

## Minimum viable thesis

Consistent annual data, identity check, VAR(1) finite-horizon decomposition with terminal and residual, uncertainty and at least one subsample check.

## Optional extension

Use a separately validated dividend strip dataset to compare forecast-based and model-implied discount-rate variation without asserting equivalence.

## Prerequisites

Asset pricing, VAR, matrix algebra and Python; advanced time-series skills.

## Thesis outline

1. Valuation ratios and present-value identity;

2. VAR forecasting and variance accounting;

3. Annual data and timing;

4. Decomposition results;

5. Identification and robustness.

## Milestones

W1-3: derive identity and select data; W4-6: audit timing and estimate VAR; W7-9: decompositions; W10-12: bootstrap and sensitivity; W13-16: interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
