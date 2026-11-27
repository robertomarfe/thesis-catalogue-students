# Data and model setup | D10.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use French monthly US market Mkt-RF+RF (total return, percent) and compound into nonoverlapping calendar quarters; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . End-quarter spot DEXUSEU and lagged OECD 3m interbank proxies IR3TIB01USM156N, IR3TIB01EZM156N from FRED. Use most recent published prior-month averages at start (two-month lag if availability cannot be verified), no assumed simultaneous executable quotes. Target 1999-2025 common complete quarters, training through 2010 then expanding hedge ratio (minimum 40 quarters); test h=0,0.5,1 and rolling estimate. Rate/spot definitions as in D10.03.01, tau=0.25 baseline.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **DEXUSEU — DEXUSEU** (Core / planned robustness). Expected file: `DEXUSEU.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=DEXUSEU); [provider page](https://fred.stlouisfed.org/series/DEXUSEU). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. USD per EUR.
- **IR3TIB01USM156N — IR3TIB01USM156N** (Core / planned robustness). Expected file: `IR3TIB01USM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01USM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01USM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly annual percentage rate proxy.
- **IR3TIB01EZM156N — IR3TIB01EZM156N** (Core / planned robustness). Expected file: `IR3TIB01EZM156N.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=IR3TIB01EZM156N); [provider page](https://fred.stlouisfed.org/series/IR3TIB01EZM156N). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. EA19 monthly annual rate proxy; verify coverage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Compound 3 complete monthly total US market returns (Mkt-RF+RF). End-quarter spot USD/EUR start/end, prior-month rates lagged 2 months if release unknown; F via simple CIP tau=.25. EUR net return U+hG with U=(1+R_US)S0/S1-1 and G=S0(1/F-1/S1). Past-only 40-quarter minimum variance fit, clipped [0,1]; fixed 0,.5,1; proportional cost on notional and hypothetical basis shifts, compare common 2011+ test.

## Acceptance and first meeting
At least 60 aligned quarters if available, rate permissions and calendar checked; full principal hedge identity and no look-ahead test passed. If sample too short descriptive fixed ratios only with approval.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Audit USD/EUR sign, full-principal identity, common dates, lagged rates and no look-ahead. Retain 60 aligned-quarter target; if unavailable agree a descriptive fixed-ratio scope. No ex-post optimized benchmark.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
