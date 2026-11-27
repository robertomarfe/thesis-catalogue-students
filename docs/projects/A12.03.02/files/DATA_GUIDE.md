# Data and model setup | A12.03.02

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Generate positive fundamental F_t by a seeded log random walk; use N=100 investors with positive initial shares and heterogeneous reference prices. Specify increasing price bounds, cash/short-sale constraints or explicitly report unconstrained stylized positions; prefer cap sell quantities by holdings and allow liquidity provider to take residual shares. Solve clearing for price with monotone demand (use scaled shares, not returns); test inventory conservation and feasible positive prices. Compare symmetric selling with asymmetric rules holding average sell propensity and common news paths fixed; 200 independent paths of 500 dates, burn-in 100.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Distinguish physical growth laws, state-price kernels and traded payoff definitions. Optional external context does not change the synthetic core.

## Frozen research design (original catalogue)

Generate positive fundamental F_t by a seeded log random walk; use N=100 investors with positive initial shares and heterogeneous reference prices. Specify increasing price bounds, cash/short-sale constraints or explicitly report unconstrained stylized positions; prefer cap sell quantities by holdings and allow liquidity provider to take residual shares. Solve clearing for price with monotone demand (use scaled shares, not returns); test inventory conservation and feasible positive prices. Compare symmetric selling with asymmetric rules holding average sell propensity and common news paths fixed; 200 independent paths of 500 dates, burn-in 100.

## Design-specific acceptance

Check monotone market clearing, nonnegative holdings and exact inventory accounting; reproduce purchase-weighted reference update and no-reference/symmetric/asymmetric controls with identical shocks. Add explicit matched-turnover calibration on development paths only, report unmatched paths and paired simulation intervals; use strictly lagged predictive variables. No claim on actual investor data.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
