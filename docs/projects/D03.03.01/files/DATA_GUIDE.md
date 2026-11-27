# Data and model setup | D03.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French daily market total return (Mkt-RF+RF) from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, target 1990-2025. Log returns in decimals, train 1990-2009, validation 2010-2015, final 2016-2025. Start with simulated SV parameters mu=log(0.0001), phi=.97,sigma_h=.2 and 3,000 days. Estimate SV by approximate log-square state-space likelihood (document approximation and zero-return handling) or particle likelihood with multiple starts; use bootstrap particle filter for forecast evaluation. Compare GARCH ML and historical variance; freeze parameters or common annual refit schedule.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use the proposed SV DGP and 3000 days for the full student experiment. The Gaussian log-square QML uses E log chi-square=-1.27036 and variance pi^2/2; fix zero-return floor from training, report affected fraction. Compare GARCH on raw returns and PF predictive log density evaluated before observing the return. Use independent 1000/5000 particle seeds, ESS and repeated log likelihood; compare filtering (not smoothing) and five-day summed variance.

## Acceptance and first meeting
At sigma_h=0 reproduce analytic Gaussian log density and constant variance. Fit approximate SV on a small synthetic sample and confirm PF forecasts on identical prefix are unaffected by later observations.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
