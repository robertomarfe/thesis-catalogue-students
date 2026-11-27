# Data and model setup | D02.04.02

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Class C conditional. Preferred same permitted EOD option quote family as D02.02.02 (https://datashop.cboe.com/option-eod-summary); alternatively documented vendor surface product (https://datashop.cboe.com/volatility-surfaces), separately gated, not raw observed quotes. Target 3+ years daily, 500+ usable common dates minimum after cleaning; k=-.15,-.075,0,.075,.15, T=30,60,90 days, require bracketing expiries/strikes, no fill across future dates. Synchronous forwards, timestamps, expiry and bid/ask or documented vendor coordinate definition. Chronological 60/20/20 split with gap for 5/20-day labels; freeze grids and factors; train scaling only. No data rights or coverage verified.

## Inputs
- **OPTION_QUOTES_LICENSED — Timestamped EOD European index option quotes and synchronous underlying/forward inputs** (Conditional core; license and scope gate). Expected file: `Provider quote package, codebook, underlying and rate/dividend/parity inputs`. [Download or provider route](https://datashop.cboe.com/option-eod-summary); [provider page](https://datashop.cboe.com/option-eod-summary). Link status from v13 inventory: Commercial product described; no entitlement or free archive established. Do NOT purchase or request restricted upload. Confirm access/redistribution, settlement, exact timestamps, bid/ask, strike, expiry, spot/forward and curve inputs. D02.02.02 cross sections, D02.04.02 longitudinal >=500 dates; sample insufficient.
- **OPTION_SURFACE_LICENSED — Longitudinal documented interpolated implied volatility surfaces** (Conditional alternative; not additional mandatory purchase). Expected file: `Provider surface package and methodology`. [Download or provider route](https://datashop.cboe.com/volatility-surfaces); [provider page](https://datashop.cboe.com/volatility-surfaces). Link status from v13 inventory: Commercial product described; no entitlement or free archive established. Alternative only; coordinate definitions, price/delta conventions, timestamp and coverage, license, no conflation with raw quotes.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Authorized daily same-family quotes, >=3 years and >=500 common dates; alternatively separately approved vendor surface with exact forward, coordinate and timing definitions. Normalize total variance on fixed 5×3 nodes and retain interpolation masks. Use actual exchange-session index, missing rows remain missing, do not compress gaps. Interpolate only within snapshot brackets; no future interpolation. Chronological 60/20/20 and purge h=5/20 labels at boundaries; training PCA and direct horizon AR, persistence, node AR on identical origin/target pairs. Prespecify a baseline rank of three if feasible; tune rank only on validation. Report negative/violating forecasts and optional separately declared projections, per-node loss, paired block uncertainty and actual coverage. No vendor file or actual surface validated.

## Acceptance and first meeting
LICENSED HISTORY BLOCKED: rights, actual 3-year and 500-date coverage, common support, timestamps, forwards and session calendar required. No unconditional assignment.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **OPTION_QUOTES_LICENSED — Timestamped EOD European index option quotes and synchronous underlying/forward inputs**: Provider quote package, codebook, underlying and rate/dividend/parity inputs. Route: https://datashop.cboe.com/option-eod-summary. Provider: https://datashop.cboe.com/option-eod-summary. Commercial product; product page reports Jan 2012 onward and NBBO at 15:45 ET and EOD. Index underlying quotes not supplied by default; obtain synchronous index/forward inputs independently. No entitlement established. Prior link status: Commercial product described; no entitlement or free archive established.

### Acceptance of the local input set

Confirm rights and 3 years/500 common sessions, full exchange calendar, bracketing k/T, missing rows retained, actual 5/20 sessions and purged blocks. Require feasible PCA dimension and assess predicted surface violations.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If history fails, consider a clearly labeled synthetic latent-surface forecasting exercise with common-node scoring and chronological holdout, not a market application. Compare distinct scope against D02.04.01.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
