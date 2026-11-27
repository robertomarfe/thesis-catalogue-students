# Data and model setup | A07.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French daily FF3 and 30 industry total returns from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; choose three named industry pairs (e.g. financials/energy, utilities/technology and market/financials, exact labels verified). Also compare Mkt-RF with SMB/HML. Target 1990-2025; train 1990-2009, evaluate 2010-2025. Use training empirical CDFs or rank transforms within explicitly descriptive full sample. Thresholds .10,.05,.025; no extreme extrapolation without sensitivity. Optional AQR strategies only if frequency and return convention match.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30D — US 30 industries daily** (Core). Expected file: `30_Industry_Portfolios_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Preselect three actual industry pairs and two market-factor pairs by verified column names. Train 1990–2009, freeze empirical CDF (midranks with open interval) and Gaussian/t copula pseudo-likelihood; evaluate finite-q conditional joint events on 2010–2025. Fit t df>2 in independent implementation; compare predicted finite-q coexceedance using independently seeded MC with counts/SE, not only asymptotic coefficient. Bootstrap time jointly, refit marginals and copula, compare standardized GARCH residuals.

## Acceptance and first meeting
Simulated bivariate Gaussian and t copula with matched correlation: fit Gaussian rho and t rho/df, open PIT boundaries and tail counts. No claim real assets follow t.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
