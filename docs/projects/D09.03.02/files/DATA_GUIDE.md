# Data and model setup | D09.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Federal Reserve GZ/EBP updated CSV, https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv; metadata at https://www.federalreserve.gov/econres/notes/feds-notes/updating-the-recession-risk-and-the-excess-bond-premium-20161006.html. Monthly GS10 minus TB3MS (rate-convention approximation, pp), USREC from FRED https://fred.stlouisfed.org/. Target 1973-2025 with final origin at least 12 months before last recession observation. Lag credit and rate data one month as conservative availability proxy; use revised-vintage pseudo-OOS. GZ replaces restricted Moody's in baseline; do not use Fed-published model probability as a predictor.

## Inputs
- **GS10 — GS10** (Core). Expected file: `GS10.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10); [provider page](https://fred.stlouisfed.org/series/GS10). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly Treasury yield percent.
- **TB3MS — TB3MS** (Core). Expected file: `TB3MS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS); [provider page](https://fred.stlouisfed.org/series/TB3MS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly discount-basis bill rate.
- **USREC — USREC** (Core). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **BAA — BAA** (Optional only after rights review). Expected file: `BAA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAA); [provider page](https://fred.stlouisfed.org/series/BAA). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Moody's proprietary source: verify permitted use before obtaining/retaining; do NOT upload/redistribute without permission.
- **AAA — AAA** (Optional only after rights review). Expected file: `AAA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=AAA); [provider page](https://fred.stlouisfed.org/series/AAA). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Moody's proprietary source: verify permitted use before obtaining/retaining; do NOT upload/redistribute without permission.
- **GZEBP — GZ credit spread and excess bond premium monthly** (Core). Expected file: `ebp_csv.csv`. [Download or provider route](https://www.federalreserve.gov/econres/notes/feds-notes/ebp_csv.csv); [provider page](https://www.federalreserve.gov/econres/notes/feds-notes/updating-the-recession-risk-and-the-excess-bond-premium-20161006.html). Link status from v13 inventory: Permanent CSV URL explicitly listed in provider documentation; bytes not inspected. Core replacement for restricted Moody spreads. Check columns and revised-vintage timing; do not use published fitted recession probability as an input.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use 1973–94 initial sample; from 1995 estimate expanding logit with one-month lagged predictors, only complete 12-month future labels ending strictly before each origin. Use identical training/evaluation masks across models; base rate, term spread, GZ and nested GZ/EBP; report overlap, separation and fixed ridge sensitivity.

## Acceptance and first meeting
Actual Fed CSV and GS10/TB3MS/USREC rights/schema/coverage not checked; no optional Moody’s series required. Verify calendar label maturation and common sample. Revised-vintage pseudo-OOS only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Validate the actual file columns, release metadata, units and common coverage before estimation. Preserve pseudo-OOS wording and the planned ridge sensitivity if separation occurs. No inference based solely on a convenient AUC or retrospective fit.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
