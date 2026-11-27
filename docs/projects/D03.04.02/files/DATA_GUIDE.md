# Data and model setup | D03.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Cboe VVIX and VIX series https://www.cboe.com/tradable-products/vix/vix-historical-data/ plus French daily market/RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html and VIXCLS https://fred.stlouisfed.org/series/VIXCLS. Monthly last common trading close, next calendar month RV from broad-market gross returns; proposed 2007-2025 subject to coverage, initial 2007-2014 train, 2015-2025 expanding test. Define threshold as 80th training percentile; count tail events. No interpolation of missing VVIX; proxy not exact SPX.

## Files to obtain locally
- **CBOE_VVIX — VVIX daily closing history** (Core). Expected file: `VVIX_History.csv`. [Download or provider route](https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VVIX_History.csv); [provider page](https://www.cboe.com/tradable-products/vix/vix-historical-data/). Link status from v13 inventory: Exact provider-linked endpoint observed 2026-11-25; web fetch unsupported CSV; bytes not validated. If direct endpoint fails select named historical price link; observe use terms.
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use only common VIX/VVIX/market dates; no interpolation. Treat VVIX as volatility of VIX options underlying, not equity variance. Fix 80th percentile threshold from initial training labels. Compare intercept-only, VIX+trailing RV and added VVIX logistic forecasts on identical mature training and evaluation months; scale predictors within each training fold. Choose L2 on validation only, record event count and precision-recall; stress thresholds .75/.90.

## Acceptance and first meeting
Check both classes and proper score implementation; training-only scaler and fixed threshold; reject missing/mismatched data.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
