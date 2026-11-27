# Data and model setup | D08.03.01

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Cboe BXM index total-return levels from https://www.cboe.com/us/indices/dashboard/BXM/ (Historical Data and methodology); target 1990-2025, use actual common dates. Prefer S&P 500 total return if legally obtainable at no cost; otherwise French monthly market total return Mkt-RF+RF is a labeled broad US equity proxy, not the same underlying: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. RF from same file. Baseline monthly returns, daily drawdowns only if both matching daily series. Separate pre-April 2002 backfilled history. Gate rights and actual download.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CBOE_BXM — BXM daily total return index history** (Core conditional). Expected file: `Original historical download (filename to verify)`. [Download or provider route](https://www.cboe.com/us/indices/dashboard/BXM/); [provider page](https://www.cboe.com/us/indices/dashboard/BXM/). Link status from v13 inventory: Dashboard Historical Data resource confirmed; direct file URL unresolved. Click Historical Data on BXM dashboard. Confirm full history, actual index values, usage rights, launch date and prelaunch backtest; not price-only SP500.
- **SP500_TR — S&P 500 gross total return index in USD** (Optional alternative to French market proxy). Expected file: `Original authorized historical export`. [Download or provider route](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); [provider page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/). Link status from v13 inventory: Optional same-underlying comparator; no free full file verified. Do not purchase or request restricted redistribution; if unavailable use French broad market total return explicitly labeled proxy. FRED SP500 price index is not valid.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Obtain authorized BXM levels, SPX total-return comparator or explicitly labeled French proxy and RF. Compute exact common month-end returns, paired risk/capture, trailing volatility-matched benchmark. Separate pre-April 2002 backfill and live history; no observed option trades or bid-ask.

## Acceptance and first meeting
BLOCKED until authorized BXM and comparator common sample validated; actual direct file not established.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBOE_BXM — BXM daily total return index history**: Original historical download (filename to verify). Route: https://www.cboe.com/us/indices/dashboard/BXM/. Provider: https://www.cboe.com/us/indices/dashboard/BXM/. Historical Data and methodology listed; hypothetical buy-write total-return index, including historical backfill. Exact file bytes and rights unverified. Prior link status: Dashboard Historical Data resource confirmed; direct file URL unresolved.
- **FF3M — US FF3 monthly**: F-F_Research_Data_Factors_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.

### Acceptance of the local input set

Verify authorized BXM and total-return comparator, separate backfill/live dates; lag risk weights and compare upside/downside capture and tail risk with uncertainty. French broad-market proxy must be explicitly labeled.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Keep BXM historical comparison on hold; retitle a synthetic covered-call strategy under matched wealth, volatility and roll rules only if distinct from D08.03.02 and D08.04.01.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
