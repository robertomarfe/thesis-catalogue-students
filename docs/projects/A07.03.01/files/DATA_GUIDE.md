# Data and model setup | A07.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French daily FF3, 25 size/book-market and 30 industry daily returns https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; use value-weighted total returns, subtract daily RF, convert percent to decimal. Monthly realized portfolio excess returns from monthly matching panels. Sample 1963-2025 or common dates; at each month end use last 756 trading days (minimum 500) to estimate beta/gamma and standardized coskewness, using only past moments to orthogonalize; next-month dependent return. Scale exposures by training-window cross-sectional SD, keep units documented.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25D — US 25 size/BM daily** (Core). Expected file: `25_Portfolios_5x5_Daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_Daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30D — US 30 industries daily** (Core). Expected file: `30_Industry_Portfolios_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Core). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use trailing 756 daily observations (min 500), excess return panels with matched RF. Construct centered market x and z=x^2-projection on 1,x using training moments only; helper standardizes x by its window SD, so translate coefficients to original units or use consistently standardized exposures. Compare conventional beta, standardized coskewness and own skewness; regress next monthly excess return on predetermined scaled exposures. Sort portfolios, not stocks; recompute generated exposures in joint bootstrap.

## Acceptance and first meeting
Quadratic orthogonalization must produce zero mean and zero covariance with centered market; artificial squared-market payoff has unit normalized quadratic exposure.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
