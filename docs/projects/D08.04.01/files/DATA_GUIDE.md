# Data and model setup | D08.04.01

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Conditional core: authorized daily/monthly Cboe S&P 500 5% Put Protection Index PPUT https://www.cboe.com/us/indices/dashboard/PPUT/ plus authorized S&P500 total return; French market+RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html as explicitly mismatched proxy if exact comparator unavailable. Common history up to 2025, inspect live/backfilled boundary and methodology. Supplement stylized synthetic monthly roll with GBM or jumps, 95% strike and Q vol grid, P drift scenarios, equal wealth.

## Inputs
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **SP500_TR — S&P 500 gross total return index in USD** (Conditional preferred exact comparator; French proxy alternative). Expected file: `Original authorized historical export`. [Download or provider route](https://www.spglobal.com/spdji/en/indices/equity/sp-500/); [provider page](https://www.spglobal.com/spdji/en/indices/equity/sp-500/). Link status from v13 inventory: Optional same-underlying comparator; no free full file verified. Do not purchase or request restricted redistribution; if unavailable use French broad market total return explicitly labeled proxy. FRED SP500 price index is not valid.
- **CBOE_PPUT — S&P 500 5% Put Protection Index history** (Core conditional; rights gate). Expected file: `Original historical download (filename to verify)`. [Download or provider route](https://www.cboe.com/us/indices/dashboard/PPUT/); [provider page](https://www.cboe.com/us/indices/dashboard/PPUT/). Link status from v13 inventory: Official dashboard verified; complete history, binary URL and rights unresolved. Require authorized total-return PPUT plus exact comparator or explicitly labeled French proxy. Obtain roll methodology and distinguish live/backfilled. Synthetic-only redesign needs approval.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Obtain authorized PPUT and SPX total-return comparator or labeled French proxy. Aggregate daily FF3 total returns/RF to complete months if proxy. Compare historical risk-matched portfolio and stress outcomes; add a transparent synthetic 95% put roll with Q premium/P payoff, not pretend synthetic marks reproduce PPUT.

## Acceptance and first meeting
BLOCKED until authorized PPUT and comparator validated or explicitly approved redesign; synthetic illustration alone does not satisfy original title.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBOE_PPUT — S&P 500 5% Put Protection Index history**: Original historical download (filename to verify). Route: https://www.cboe.com/us/indices/dashboard/PPUT/. Provider: https://www.cboe.com/us/indices/dashboard/PPUT/. Inherited dashboard route, no new direct binary or rights verification. Prior link status: Official dashboard verified; complete history, binary URL and rights unresolved.
- **FF3D — US FF3 daily**: F-F_Research_Data_Factors_daily_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.

### Acceptance of the local input set

Verify authorized PPUT and comparator, launch and roll rules; use common months and lagged weights, plus separate stylized payoff exercise. Explicitly approve a synthetic variant if data fail.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

Retitle synthetic protective put insurance with equal initial wealth, roll costs and jump regimes if history unavailable. No PPUT evidence or claims of realized crash protection.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
