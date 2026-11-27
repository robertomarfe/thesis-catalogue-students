# Data and model setup | A10.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly French FF3 and momentum, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, and Goyal monthly predictor workbook, https://sites.google.com/view/agoyal145/. Freeze SMB/HML/Mom targets and a small menu (dp, term spread, default spread, short rate, past factor return). Proposed 1965-1994 training, 1995-2009 expanding validation, 2010-2025 final holdout subject to coverage. Lag predictors conservatively and document revised data. Select penalties in nested expanding windows; allow no post-holdout model selection.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core / planned robustness). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core / planned robustness). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Build factor-specific SMB,HML,Mom targets in decimal; no RF subtraction from spreads. Features common Goyal dp/tms/dfy/tbl plus lagged own factor. For each target tune ridge and LASSO by prior dates and use factor-specific recursive mean. Joint date-block bootstrap across three loss gains; funding/collateral needed for economic factor timing.

## Acceptance and first meeting
Actual French FF3, Mom, Goyal rights and common monthly dates open. Check shared date-block resampling preserves joint loss dependence.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Monthly French FF3 and momentum, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, and Goyal monthly predictor workbook, https://sites.google.com/view/agoyal145/. Freeze SMB/HML/Mom targets and a small menu (dp, term spread, default spread, short rate, past factor return). Proposed 1965-1994 training, 1995-2009 expanding validation, 2010-2025 final holdout subject to coverage. Lag predictors conservatively and document revised data. Select penalties in nested expanding windows; allow no post-holdout model selection.

## Design-specific acceptance

Check factor signs, dates, percent scaling, source vintage and lags. Keep all three factor loss gains together in resampling. Freeze OLS specification; negative R2 and weak gains allowed; no selected winner p-value.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
