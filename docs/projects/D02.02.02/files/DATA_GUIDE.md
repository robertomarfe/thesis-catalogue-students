# Data and model setup | D02.02.02

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Class C, conditional on permission and actual acquisition. Candidate paid provider Cboe DataShop https://datashop.cboe.com/option-eod-summary; a sample file is not sufficient for a full thesis. Target one European cash-settled index option family, e.g. SPX with consistent settlement style, 20 preselected nonconsecutive dates over one year, at least 3 expiries and 15 usable strikes per expiry. Need timestamp, option type, strike, exact expiry/settlement, NBBO bid/ask, synchronous index/forward, curve and dividends or parity; record units, multipliers and exercise type. Use OTM quotes, no crossed/negative spreads, stale and bound failures logged; splits fixed before fitting. No raw quotes yet; use synthetic sanity check only while gate pending.

## Inputs
- **OPTION_QUOTES_LICENSED — Timestamped EOD European index option quotes and synchronous underlying/forward inputs** (Conditional core; license and scope gate). Expected file: `Provider quote package, codebook, underlying and rate/dividend/parity inputs`. [Download or provider route](https://datashop.cboe.com/option-eod-summary); [provider page](https://datashop.cboe.com/option-eod-summary). Link status from v13 inventory: Commercial product described; no entitlement or free archive established. Do NOT purchase or request restricted upload. Confirm access/redistribution, settlement, exact timestamps, bid/ask, strike, expiry, spot/forward and curve inputs. D02.02.02 cross sections, D02.04.02 longitudinal >=500 dates; sample insufficient.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Only after license, normalized one-family one-settlement quotes with timezone-aware snapshot and expiry, exact forward/discount, bid/ask and explicit stale flag. Freeze 20 dates, require 10+ accepted dates, 3+ expiries and 15+ usable strikes each. Report rejected rows; OTM parity conversion, no clipping. Split strikes by rank before fitting; fixed training/validation/test. Compare flat Black, SVI and Heston on held-out common strikes, sensitivity to raw and spread-normalized objective, quote uncertainty, parameter stability and finite-grid arbitrage. Entire-maturity holdout needs a specified interpolation for every model. Any synthetic sanity check uses artificial prices, not observed quotes or evidence of market fit. Heston negative-rho bounds and SVI positive a are fixture choices, broaden or justify before real work.

## Acceptance and first meeting
LICENSED DATA BLOCKED: actual quote rights, schema, 10+ dates and maturity/strike support, synchronous forwards, discount and settlement must be verified. Synthetic cleaning/calibration only. Not assignable on original design without authorized data.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **OPTION_QUOTES_LICENSED — Timestamped EOD European index option quotes and synchronous underlying/forward inputs**: Provider quote package, codebook, underlying and rate/dividend/parity inputs. Route: https://datashop.cboe.com/option-eod-summary. Provider: https://datashop.cboe.com/option-eod-summary. Commercial product; product page reports Jan 2012 onward and NBBO at 15:45 ET and EOD. Index underlying quotes not supplied by default; obtain synchronous index/forward inputs independently. No entitlement established. Prior link status: Commercial product described; no entitlement or free archive established.

### Acceptance of the local input set

Before assignment verify rights, at least 10 usable dates from 20 prespecified dates, 3 expiries/15 strikes each, timestamps, settlement, forwards. Implement input checks and an independent held-out fit; synthetic accuracy is not market evidence.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If no licensed quotes, defer. A retitled synthetic noisy-surface calibration study would overlap D01.02.01/D01.04.03; require a distinct cleaning/arbitrage/held-out-design contribution before approving.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
