# Data and model setup | A07.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly VIX end-of-month from https://fred.stlouisfed.org/series/VIXCLS, 25 size-value and 30 industry portfolio returns and FF factors from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 1990-2025, first 60 months for innovation model and 60-month betas, common evaluation sample. One primary 25 portfolio set; industries a robustness set, not additional independent observations.

## Files to obtain locally
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Robustness). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use monthly last valid VIX close (record actual date, no stale month-end fill). Recursive AR(1) log VIX innovation uses observations only through t-1 to predict t; measure beta with trailing 60 months of innovations and returns, then forecast next month cross-section. At least 60 months for initial innovation model plus 60 valid innovations for first exposure. No RF subtraction from Mkt-RF. Compare market-only and augmented same panel; test high-low portfolios and bootstrap with innovation and beta re-estimation.

## Acceptance and first meeting
Recursive innovations through a prefix invariant to appended observations. Synthetic cross-sectional regression with separate market/volatility exposure.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
