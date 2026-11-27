# Data and model setup | D10.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use daily EIA WTI Cushing and Brent Europe spot series DCOILWTICO and DCOILBRENTE via FRED, https://fred.stlouisfed.org/series/DCOILWTICO and https://fred.stlouisfed.org/series/DCOILBRENTE. Target 1990-2025, common valid observations, USD/barrel. Compare weekly and monthly nonoverlapping dollar changes. Use expanding or rolling 104-week/60-month training windows; freeze window choices before a 2015-2025 holdout. Hedged value changes are hypothetical matched spot exposures, not self-financing futures P&L.

## Inputs
- **DCOILWTICO — DCOILWTICO** (Core / planned robustness). Expected file: `DCOILWTICO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILWTICO); [provider page](https://fred.stlouisfed.org/series/DCOILWTICO). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily spot; nonpositive prices possible.
- **DCOILBRENTE — DCOILBRENTE** (Core / planned robustness). Expected file: `DCOILBRENTE.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DCOILBRENTE); [provider page](https://fred.stlouisfed.org/series/DCOILBRENTE). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily spot; USD/barrel.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Build weekly W-FRI and monthly endpoints from last common valid date within 7 days, retaining observed dates. Difference consecutive period endpoints only; preserve nonpositive WTI, including 2020. Hedge P&L = dWTI-h*dBrent, implement minvar_ratio(dWTI,-dBrent); train 104 weeks or 60 months; common 2015–2025 holdout, benchmark 0,1 and clipped [0,2]. No log price or percentage division around zero.

## Acceptance and first meeting
Verify WTI/Brent definitions, calendars and nonpositive quotes, actual matched history; no tradable futures position. Synthetic covariance optimizer and endpoint test passed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify common observed endpoints, barrel units, no forward fill and past-only estimation at both horizons. Report basis changes, held-out risk reduction and negative results.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
