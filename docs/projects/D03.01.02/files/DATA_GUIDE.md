# Data and model setup | D03.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French daily US market factor plus RF to obtain total market return; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1990-2025; first 1990-2004 estimation, 2005-2009 validation, 2010-2025 final test if available. Convert percent to decimal and use actual trading days. RV proxy daily squared mean-adjusted returns and sums over next 5 days. Fit Gaussian and optionally standardized Student-t errors; re-estimate monthly using expanding windows, issue forecasts using only past data.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use the original chronological split and zero mean baseline; refit monthly on expanding windows. Fit GARCH, GJR (nonnegative gamma baseline, negative gamma admissible only with alpha+gamma>=0 in extension) and EGARCH on the same decimal log returns. Report scaled likelihood, convergence and boundary flags. For EGARCH simulate expected variance, not exponentiated expected log variance. Plot the news-impact curve at a common previous variance and compare forecasts by sign of the last shock.

## Acceptance and first meeting
Verify GJR nests GARCH at gamma=0 and negative shocks increase next variance under the illustrative positive gamma. Fit both asymmetric models on artificial returns and check finite positive five-day forecasts.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
