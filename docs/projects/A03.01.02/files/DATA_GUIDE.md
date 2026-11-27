# Data and model setup | A03.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
FRED quarterly real PCE per capita A794RX0Q048SBEA https://fred.stlouisfed.org/series/A794RX0Q048SBEA and PCE price index PCECTPI https://fred.stlouisfed.org/series/PCECTPI; French monthly RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1959-2025, actual overlap checked before use. Construct quarterly compounded nominal bill return and divide by same-quarter PCE inflation; this rolling nominal bill proxy is ex post real, not a known real zero-coupon return. Annual beta 0.95-0.995 converted to quarterly via fourth root; gamma 1-10, 25/50 stress only.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **A794RX0Q048SBEA — A794RX0Q048SBEA** (Core / planned robustness). Expected file: `A794RX0Q048SBEA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=A794RX0Q048SBEA); [provider page](https://fred.stlouisfed.org/series/A794RX0Q048SBEA). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly real PCE per capita; revised vintage.
- **PCECTPI — PCECTPI** (Core / planned robustness). Expected file: `PCECTPI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCECTPI); [provider page](https://fred.stlouisfed.org/series/PCECTPI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly PCE price index; check same quarter.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use identical quarterly inputs as A03.01.01; estimate AR(1) of g on contiguous quarterly runs only (no row shift across gaps). For stationary g use conditional mean mu+phi(g_t-mu) and residual SD; annual log safe rate=4*log_safe. Analytic stationary SD of the annualized conditional rate is 4*gamma*abs(phi)*sigma_g, with sigma_g innovation SD/sqrt(1-phi^2). Compare ex post rolling real bill log return proxy, not risk-free asset. Solve annual beta frontier via quarterly log rate mean, flag beta>=1. Refit model inside paired block bootstrap with gaps respected.

## Acceptance and first meeting
Actual consumption, price and FF3M complete quarterly sample required. Gaussian quadrature check of conditional safe rate and artificial AR test only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

FRED quarterly real PCE per capita A794RX0Q048SBEA https://fred.stlouisfed.org/series/A794RX0Q048SBEA and PCE price index PCECTPI https://fred.stlouisfed.org/series/PCECTPI; French monthly RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1959-2025, actual overlap checked before use. Construct quarterly compounded nominal bill return and divide by same-quarter PCE inflation; this rolling nominal bill proxy is ex post real, not a known real zero-coupon return. Annual beta 0.95-0.995 converted to quarterly via fourth root; gamma 1-10, 25/50 stress only.

## Design-specific acceptance

Provide calendar-aware pair counts and separate fitted conditional rate mean/SD from ex-post real bill mean/SD; test the Gaussian formula by quadrature. Derive beta frontier, retain beta outside (0,1) as inadmissible, and include uncertainty in AR persistence and conditional variance; a rate-volatility mismatch need not imply rejection solely of gamma.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
