# Data and model setup | A07.01.01

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Cboe historical VIX https://www.cboe.com/tradable-products/vix/vix-historical-data/ ; SPX price index FRED https://fred.stlouisfed.org/series/SP500 (rolling 10-year history; excludes dividends); French monthly and daily market/RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Freeze latest common file and actual dates. Baseline matched SPX daily log-return physical variance, monthly last common trading day as forecast origin, target FF market total excess return (clearly cross-index). For a long-sample sensitivity use daily FF market reconstructed returns as a different underlying proxy, not SPX. Reserve initial 2 years for physical forecast warmup and at least 3 more years for predictive training where feasible; long proxy sample from 1990 with 2005 OOS start. Report sample size and do not promise precise OOS inference on short SPX history.

## Files to obtain locally
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF3D — US FF3 daily** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **SP500 — SP500** (Core / planned robustness). Expected file: `SP500.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500); [provider page](https://fred.stlouisfed.org/series/SP500). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. FRED limited rolling history; price index only.
- **CBOE_VIX — VIX daily closing history** (Core / planned robustness). Expected file: `VIX_History.csv`. [Download or provider route](https://cdn-api.cboe.com/us/indices/daily_prices/VIX_History.csv); [provider page](https://www.cboe.com/tradable_products/vix/vix_historical_data). Link status from v13 inventory: Provider lists named historical file; candidate direct endpoint not confirmed in this turn. If direct endpoint fails select named historical price link; observe use terms.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
For each origin use a scheduled exchange calendar (not business days as actual calendar); estimate historical/EWMA daily expected squared log returns using past data; multiply by scheduled sessions in next 30 calendar days. Q variance=(VIX/100)^2*30/365. Separate matched SP500 price return baseline (rights and rolling 10-year coverage gate) from French broad-market total-return proxy robustness; do not silently replace. Use FF monthly total market and bill compounded separately for 1/3-month excess targets. Fit only mature labels.

## Acceptance and first meeting
Hand-check horizon VRP and month-gap target handling. A permitted matched SPX source or explicit supervisor-approved proxy redesign is required before empirical assignment; do not imply that FRED permission extends to reproduction.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBOE_VIX — VIX daily closing history**: VIX_History.csv. Route: https://cdn-api.cboe.com/us/indices/daily_prices/VIX_History.csv. Provider: https://www.cboe.com/tradable_products/vix/vix_historical_data. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Provider lists named historical file; candidate direct endpoint not confirmed in this turn.
- **FF3D — US FF3 daily**: F-F_Research_Data_Factors_daily_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.
- **SP500 — SP500**: SP500.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500. Provider: https://fred.stlouisfed.org/series/SP500. Rolling ten years of daily price-index history, not total return. Reproduction requires S&P permission; no permission established. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Obtain documented permission and matched daily sample; freeze 30-calendar-day maturity and scheduled sessions, exclude incomplete labels and compare both 1/3-month compounded excess returns on identical origins with recursive mean. Three-month inference must account for overlap. Any broad-market redesign requires approval.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Use a broad market physical-variance proxy only with explicit approval and label cross-index mismatch; otherwise a synthetic VRP mechanism study, not an empirical SPX predictability result.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
