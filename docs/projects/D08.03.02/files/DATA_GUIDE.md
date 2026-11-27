# Data and model setup | D08.03.02

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Cboe PUT index historical levels and methodology: https://www.cboe.com/us/indices/dashboard/PUT/. Target monthly common sample 1990-2025, actual dates conditional on authorization and full history. Use S&P 500 total return if available freely and legally, otherwise French Mkt-RF+RF proxy and RF: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Optional BXM comparison and VIXCLS. Separate backfilled and live history using documented launch dates.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VIXCLS — VIXCLS** (Optional regime analysis). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **SP500_TR — S&P 500 gross total return index in USD** (Optional alternative to French market proxy). Expected file: `Original authorized historical export`. [Download or provider route](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); [provider page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/). Link status from v13 inventory: Optional same-underlying comparator; no free full file verified. Do not purchase or request restricted redistribution; if unavailable use French broad market total return explicitly labeled proxy. FRED SP500 price index is not valid.
- **CBOE_BXM — BXM daily total return index history** (Optional comparison). Expected file: `Original historical download (filename to verify)`. [Download or provider route](https://www.cboe.com/us/indices/dashboard/BXM/); [provider page](https://www.cboe.com/us/indices/dashboard/BXM/). Link status from v13 inventory: Dashboard Historical Data resource confirmed; direct file URL unresolved. Click Historical Data on BXM dashboard. Confirm full history, actual index values, usage rights, launch date and prelaunch backtest; not price-only SP500.
- **CBOE_PUT — S&P 500 PutWrite total return index history** (Core conditional; rights gate). Expected file: `Original historical download (filename to verify)`. [Download or provider route](https://www.cboe.com/us/indices/dashboard/PUT/); [provider page](https://www.cboe.com/us/indices/dashboard/PUT/). Link status from v13 inventory: Official dashboard verified; full-history file and exact direct URL unresolved. Obtain authorized historical index levels and roll/collateral methodology; verify live/backfilled sample; no price-only SP500 comparator.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Obtain authorized PUT index and equity comparator/RF; compare paired excess returns, expected shortfall, downside risk and lagged vol-matched benchmark. Record collateral, settlement and live/backfilled boundaries from methodology; optional BXM/VIX only if rights permit.

## Acceptance and first meeting
BLOCKED until authorized PUT and comparator confirmed; do not substitute BXM or naked option returns.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBOE_PUT — S&P 500 PutWrite total return index history**: Original historical download (filename to verify). Route: https://www.cboe.com/us/indices/dashboard/PUT/. Provider: https://www.cboe.com/us/indices/dashboard/PUT/. Inherited dashboard route, no new direct binary or rights verification. Prior link status: Official dashboard verified; full-history file and exact direct URL unresolved.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.

### Acceptance of the local input set

Verify authorized PUT and comparator, collateral and roll methodology; no second collateral credit, use same common months and lagged risk-match, report ES and crash subsamples.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Keep PUT history on hold; retitle synthetic cash-secured put writing with collateral accrual, funding and tail losses if approved; do not call it index replication.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
