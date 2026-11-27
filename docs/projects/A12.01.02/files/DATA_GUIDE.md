# Data and model setup | A12.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
AQR Betting Against Beta: Equity Factors Data, Monthly https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly ; US BAB zero-cost series (verify units and workbook), original data as fallback https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Original-Paper-Data . FRED NFCI weekly https://fred.stlouisfed.org/series/NFCI ; optional ANFCI and NFCICREDIT. French monthly FF3/Mom. Use month-end last weekly value available before end-month (weekly ending Friday typically released later; conservatively lag one extra week for predictive specification and flag revised vintage). Aim common 1973-2025 sample subject to coverage. Freeze 2008-2009 and 2020 stress periods; no selection by worst BAB returns.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core / planned robustness). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **NFCI — NFCI** (Core / planned robustness). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **BAB — Betting Against Beta: Equity Factors Data, Monthly** (Core / planned robustness). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly); [provider page](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly). Historical v13 inventory note (unverified in current release): Exact dataset page; direct file URL unresolved. Select named dataset download and retain original file; verify usage terms, no arbitrary substitution.
- **ANFCI — ANFCI** (Optional sensitivity). Expected file: `ANFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=ANFCI); [provider page](https://fred.stlouisfed.org/series/ANFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Adjusted NFCI.
- **NFCICREDIT — NFCICREDIT** (Optional sensitivity). Expected file: `NFCICREDIT.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCICREDIT); [provider page](https://fred.stlouisfed.org/series/NFCICREDIT). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Credit subindex.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use AQR monthly US BAB zero-cost long/short, not a total-return index; no RF subtraction or assumption of gross/net treatment until workbook inspected. NFCI weekly covers Friday, normally published Wednesday 8:30 ET, holidays Thursday; use actual release if supplied and additional one-week buffer for lagged predictor; revised data label. Aggregate month-end last available release, distinguish change during month (association) versus lagged level/change (predictive). Standardize using training scale; factor regression and HAC, fixed 2008-09/2020 windows and ANFCI/NFCICREDIT sensitivity, OOS historical mean optional if enough data. No causal identification of borrowing constraints.

## Acceptance and first meeting
Actual US BAB workbook, rights and normalization, NFCI availability/revisions, common FF/Mom sample; separate same-month and prior-month regressions.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

AQR Betting Against Beta: Equity Factors Data, Monthly https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly ; US BAB zero-cost series (verify units and workbook), original data as fallback https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Original-Paper-Data . FRED NFCI weekly https://fred.stlouisfed.org/series/NFCI ; optional ANFCI and NFCICREDIT. French monthly FF3/Mom. Use month-end last weekly value available before end-month (weekly ending Friday typically released later; conservatively lag one extra week for predictive specification and flag revised vintage). Aim common 1973-2025 sample subject to coverage. Freeze 2008-2009 and 2020 stress periods; no selection by worst BAB returns.

## Design-specific acceptance

Validate BAB workbook version, long-short orientation/units and common FF/Mom panel; separate contemporaneous versus lagged standardized states with past-only scaling. Joint date blocks, fixed crisis windows and optional ANFCI/NFCICREDIT; report no causality and vintage caveat. No OOS claim from contemporaneous controls.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
