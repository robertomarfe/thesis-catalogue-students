# Data and model setup | A07.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly US FF5 market, SMB,HML,RMW,CMA plus Mom, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Common 1963-2025 target, value-weighted factor returns in decimals; use Rm-Rf state and zero cutoff predeclared. Use 1963-1994 and 1995-2025 splits and rolling 120-month windows; minimum 24 observations per state. AQR BAB optional separate factor only if consistent dates/units/rights. Factors are long-short returns, not excess returns to a fully funded stock portfolio.

## Files to obtain locally
- **FF5M — US FF5 monthly** (Core). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **BAB — Betting Against Beta: Equity Factors Data, Monthly** (Optional sensitivity). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly); [provider page](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly). Link status from v13 inventory: Exact dataset page; direct file URL unresolved. Select named dataset download and retain original file; verify usage terms, no arbitrary substitution.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
FF5 plus momentum, keep long-short factor returns as supplied; no subtraction of RF from factors. Predeclare Mkt-RF<0, two fixed periods and 120-month rolling windows with at least 24 observations per state. Include state intercept and interaction, verify equivalence to separate regressions. Use common time-block resampling across factors, Holm correction; training-defined terciles as robustness.

## Acceptance and first meeting
Check separate-slope identity with nonzero intercept shift and exact synthetic coefficients; require two states and full rank.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
