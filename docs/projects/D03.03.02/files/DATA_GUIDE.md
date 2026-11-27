# Data and model setup | D03.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French daily Mkt-RF+RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html and VIXCLS from https://fred.stlouisfed.org/series/VIXCLS for optional external comparison; target 1990-2025. Train 1990-2004, select specification 2005-2009, evaluate 2010-2025; annual refit with expanding sample. 5/20-trading-day future mean squared return and event exceeding fixed training 90th percentile of 20-day target. Keep same forecasts and label maturity; use only data through origin.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VIXCLS — VIXCLS** (Optional comparison). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Estimate a zero-mean two-state Gaussian variance HMM with transition probabilities bounded away from 0/1; sort states by variance after every fit and flag low occupancy/boundaries. Freeze threshold at training 90th percentile of future 20-day mean square (not smoothed state). Annual refit; recursive filtering, forecast variance by transition powers, event probability by simulated state/return paths. Compare GARCH and rolling variance with same event definition; bootstrap paired calendar blocks.

## Acceptance and first meeting
Verify forward likelihood against direct Gaussian Bayes updates, multi-step forecast against matrix powers; event MC at identical state variance and h=1 matches analytic chi-square probability. Check estimation on your own simulated variance shifts; no recovery guarantee.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
