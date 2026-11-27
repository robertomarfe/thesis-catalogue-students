# Data and model setup | A07.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
FRED VIXCLS, French daily market return plus RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, FRED news-based USEPUNEWSINDXM https://fred.stlouisfed.org/series/USEPUNEWSINDXM and NFCI. Rights and publication lag checked before use. Monthly month-end formation 1990-2025 proposed, 10-year initial training. French broad total-return market differs from SPX; explicit proxy, prefer same-underlying permitted S&P series if sufficient history. HAR-style daily lagged variance forecasts (1,5,22 days), direct 30-calendar-day targets and expanding train with mature labels. Lag EPU at least one month, stress actual release/vintage; revised-data exercise labeled pseudo-real-time.

## Files to obtain locally
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **USEPUNEWSINDXM — US monthly news-based EPU** (Core). Expected file: `USEPUNEWSINDXM.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USEPUNEWSINDXM); [provider page](https://fred.stlouisfed.org/series/USEPUNEWSINDXM). Link status from v13 inventory: Series metadata confirmed; standard FRED CSV endpoint, not retrieved. Check units, publication lag/vintage, citation and redistribution conditions; composite includes other components.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **SP500 — SP500** (Conditional robustness; same-underlying proxy only if licensed and adequate history). Expected file: `SP500.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500); [provider page](https://fred.stlouisfed.org/series/SP500). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. FRED limited rolling history; price index only.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use horizon-matched 30-day annualized Q and P measures with prequential HAR-style and historical forecasts. Use explicitly lagged log EPU (news-based USEPUNEWSINDXM, not headline composite) and NFCI: use actual release dates/vintage if available, otherwise clearly labeled revised pseudo-real-time. For EPU use month t-1 only if released by origin; NFCI weekly Wednesday release through previous Friday, aggregate last published value. Refit physical forecasts in time-block uncertainty exercise.

## Acceptance and first meeting
Check synthetic 30-day conversion and immature-label exclusion. Supervisor must confirm rights, release timing and sample; no causal inference from association.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
