# Data and model setup | D08.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Cboe VIX and VVIX daily closing histories https://www.cboe.com/tradable_products/vix/vix_historical_data; French daily market total return=Mkt-RF+RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Use common dates, proposed 2007-2025 if available. Sample every fifth trading day for nonoverlapping targets; fix calendar phase. First 60% train, next 20% validate, last 20% test, with five-day purge at split boundaries. Standardize predictors using training only; forecast after close t for t+1 onward.

## Inputs
- **FF3D — US FF3 daily** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CBOE_VIX — VIX daily closing history** (Core / planned robustness). Expected file: `VIX_History.csv`. [Download or provider route](https://cdn-api.cboe.com/us/indices/daily_prices/VIX_History.csv); [provider page](https://www.cboe.com/tradable_products/vix/vix_historical_data). Link status from v13 inventory: Provider lists named historical file; candidate direct endpoint not confirmed in this turn. If direct endpoint fails select named historical price link; observe use terms.
- **CBOE_VVIX — VVIX daily closing history** (Core / planned robustness). Expected file: `VVIX_History.csv`. [Download or provider route](https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VVIX_History.csv); [provider page](https://www.cboe.com/tradable-products/vix/vix-historical-data/). Link status from v13 inventory: Exact provider-linked endpoint observed 2026-11-25; web fetch unsupported CSV; bytes not validated. If direct endpoint fails select named historical price link; observe use terms.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct nonoverlapping future five-session total log returns below log(.97) and semivariance, with fixed calendar phase and mature labels. Align VIX/VVIX close at origin, use 60/20/20 split and five-session purge. Compare constant, VIX-only, VVIX-only, joint models; train-only standardization, proper scores, event counts and paired inference.

## Acceptance and first meeting
Actual common VIX/VVIX/FF daily coverage and rights open; no missing-session compression or threshold drift.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. If source fails, obtain explicitly approved redesign or defer.

## Timing, accounting and units

Define the pricing measure, path measure, position and loss signs, trading dates, initial funding and terminal liquidation. Freeze the provider vintage for empirical designs, retain common dates and distinguish price indices from total-return indices. A historical replay of synthetic option quotes is not a realized traded-option backtest.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
