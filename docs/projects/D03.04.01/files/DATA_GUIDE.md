# Data and model setup | D03.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Daily VIXCLS https://fred.stlouisfed.org/series/VIXCLS and French daily market and RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Reconstruct gross market returns (Mkt-RF plus RF, percent to decimal); monthly last trading day forecasts, next calendar month squared daily logs. Adjust VIX horizon by actual calendar days as approximation; SPX vs broad-market proxy explicitly acknowledged. Proposed 1990-2025; 1990-2004 initial training, expanding through 2025. No realized high-frequency variance claim.

## Files to obtain locally
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VXVCLS — VXVCLS** (Optional extension). Expected file: `VXVCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VXVCLS); [provider page](https://fred.stlouisfed.org/series/VXVCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. 3-month implied volatility index.
- **SP500 — SP500** (Optional authorized price proxy). Expected file: `SP500.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500); [provider page](https://fred.stlouisfed.org/series/SP500). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. FRED limited rolling history; price index only.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Monthly last common closing date, next calendar month daily squared log total-market proxy. Convert VIX decimal squared to horizon total variance via actual month days/365 (approximate, VIX is 30 calendar days). Include rolling and GARCH forecasts and VIX-augmented linear forecast with training-only floor. Compare all on identical complete months; delay fitting until labels mature. Do not describe cross-index forecast as exact SPX.

## Acceptance and first meeting
Check month target on a calendar fixture and invalidate a missing session; verify units with .20 volatility and 30-day scale. Test mature-label exclusion with an augmented forecast.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
