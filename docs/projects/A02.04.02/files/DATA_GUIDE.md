# Data and model setup | A02.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal annual/monthly predictor workbook https://sites.google.com/view/agoyal145/; VIXCLS https://fred.stlouisfed.org/series/VIXCLS; French monthly market/RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1990-2025, initial train 1990-2004, expanding 2005-25. At each month-end use available prior-month valuation predictor and current last trading VIX, next month excess return. Revisions imply pseudo-real-time. Benchmark empirical expanding quantiles and rolling mean/vol with normal quantiles; predeclare 60-month window or tune in training only.

## Inputs
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
At least q=.10,.50,.90 (freeze probabilities before test). Quantile regression with identical past features dp and end-month available VIX. Compare expanding empirical quantile and rolling 60-month Gaussian location-scale. Use pinball and coverage, note crossing, predeclare noncrossing rearrangement as sensitivity rather than hiding failures. No future volatility in features.

## Acceptance and first meeting
Goyal, French RF/market, VIX actual files and rights pending. Check pinball asymmetry and fitted quantile against known synthetic linear location.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal annual/monthly predictor workbook https://sites.google.com/view/agoyal145/; VIXCLS https://fred.stlouisfed.org/series/VIXCLS; French monthly market/RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1990-2025, initial train 1990-2004, expanding 2005-25. At each month-end use available prior-month valuation predictor and current last trading VIX, next month excess return. Revisions imply pseudo-real-time. Benchmark empirical expanding quantiles and rolling mean/vol with normal quantiles; predeclare 60-month window or tune in training only.

## Design-specific acceptance

Hand-check pinball loss for positive and negative residuals and empirical quantile convention. Check VIX availability and no future data. Test crossing detection, report event counts, no post-test choice of quantile or rearrangement.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
