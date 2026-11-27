# Data and model setup | A10.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use French daily market total returns https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, VIXCLS, NFCI, GS10 and TB3MS from https://fred.stlouisfed.org/. Construct past 1/3/12-month variance, end-month VIX squared divided by 12, term spread, lagged NFCI (one-month conservative lag). Common sample 1990-2025 or verified intersection; train through 2009, validation 2010-2015, test 2016-2025. Use expanding folds, same features and target for all models; retain revised-vintage caveat. Hyperparameters selected only in validation, modest tree depth.

## Inputs
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **GS10 — GS10** (Core). Expected file: `GS10.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10); [provider page](https://fred.stlouisfed.org/series/GS10). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly Treasury yield percent.
- **TB3MS — TB3MS** (Core). Expected file: `TB3MS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS); [provider page](https://fred.stlouisfed.org/series/TB3MS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly discount-basis bill rate.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct next-month sum squared daily market log returns (or centered simple squares consistently as declared); use same target and past 1/3/12-month realized variance. VIX^2/12 in decimal units approximates monthly Q variance; horizon mismatch disclose, NFCI/GS10/TB3MS lagged. Train linear/HAR and shallow RF/boost on identical inputs; require positive forecasts for QLIKE with predeclared floor, report clipping. Group correlated predictors for permutation importance on validation only; final attributions descriptive, no tuning.

## Acceptance and first meeting
Actual FF3D and macro/VIX rights, complete sessions and calendar commonity pending. Test grouped permutation loss and artificial positive variance target.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Use French daily market total returns https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, VIXCLS, NFCI, GS10 and TB3MS from https://fred.stlouisfed.org/. Construct past 1/3/12-month variance, end-month VIX squared divided by 12, term spread, lagged NFCI (one-month conservative lag). Common sample 1990-2025 or verified intersection; train through 2009, validation 2010-2015, test 2016-2025. Use expanding folds, same features and target for all models; retain revised-vintage caveat. Hyperparameters selected only in validation, modest tree depth.

## Design-specific acceptance

Hand-check daily squared-return aggregation and annualization (same for forecast and target); record zero/clipped values; check availability ledger and positive forecasts. Permute grouped blocks, not rows; distinguish importance variability from loss uncertainty.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
