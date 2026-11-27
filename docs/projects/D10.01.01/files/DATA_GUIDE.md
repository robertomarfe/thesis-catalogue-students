# Data and model setup | D10.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
EIA monthly WTI Cushing spot average in USD/barrel MCOILWTICO https://fred.stlouisfed.org/series/MCOILWTICO ; daily DCOILWTICO optional for exceptional observations. Proposed 1986-2025, verify coverage, positivity and missing months before log transform; preserve monthly average definition, distinguish negative daily 2020 observations from monthly averages. At end of month t assume last published average t-1 (verify release calendar); forecast month t+h using h+1 transitions from t-1, for both OU and random walk. Compare a zero-lag descriptive case separately. Initial training 1986-2005, test 2006 onward; expanding and 120-month rolling estimates; horizons 1,3,12 months.

## Inputs
- **MCOILWTICO — MCOILWTICO** (Core / planned robustness). Expected file: `MCOILWTICO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=MCOILWTICO); [provider page](https://fred.stlouisfed.org/series/MCOILWTICO). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly USD/barrel.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use MCOILWTICO USD/barrel monthly average, inspect positivity and missing months. Fit unconstrained AR(1) to log levels; report finite kappa/half-life only for 0<b<1; estimate constrained alternative separately. End-month origin t uses last published t-1 (or conservative verified lag), forecast t+h via h+lag transitions. Compare RW on same information. Initial through 2005, 2006+ holdout; expanding and rolling 120; 2008/2020 prespecified.

## Acceptance and first meeting
Validate actual monthly calendar and release timing; revised-vintage forecast only unless archival vintages available. Synthetic timing perturbation and AR coefficient tests passed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Audit positivity, complete monthly dates, release lag and actual targets. Verify OU transition and random-walk limit on artificial data, report inadmissible fits and paired loss comparisons.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
