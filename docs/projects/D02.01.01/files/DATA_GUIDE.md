# Data and model setup | D02.01.01

**Current data gate: blocked.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Conditional on rights and consistent vintage, use SKEW history at https://www.cboe.com/data/quotes/skew/metrics/ (candidate CSV SKEW_History.csv), VIXCLS from https://fred.stlouisfed.org/series/VIXCLS and FF daily returns (market total=Mkt-RF+RF) from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Month-end predictors, next-month compounded market return, fixed event below -5%; target common 1990-2025 legacy history, with pre-launch retrospective data flagged. If restated, use only one documented methodology; freeze a sample split 60/20/20% chronologically, require adequate tail events. Avoid overlap in baseline.

## Inputs
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CBOE_SKEW — SKEW daily closing history (one documented methodology)** (Core conditional; rights review). Expected file: `SKEW_History.csv`. [Download or provider route](https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv); [provider page](https://www.cboe.com/data/quotes/skew/metrics/). Link status from v13 inventory: Candidate CSV endpoint; provider dashboard and Oct 2026 consultation checked, not retrieved. Verify rights, legacy versus any restatement and launch dates; no silent splice. Proposed change would restate from Jan 2013.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use authorized one-methodology SKEW history, VIXCLS and FF3D; market total Mkt-RF+RF, exact common final exchange session and complete next month. Preserve missing values; labels are next-calendar-month total returns below -5%. Chronological 60/20/20 split with fixed boundary purge; standardize training only; minimum five events and non-events per split merely a feasibility gate. Compare VIX-only with VIX+SKEW logits on common dates; report event counts, Brier/log loss, calibration and paired block inference. Verify the 2026 consultation outcome and version before acquisition; no splice. If actual coverage/rights fail, defer or approve a separate synthetic redesign, not an artificial exercise as an empirical answer.

## Acceptance and first meeting
BLOCKED for assignment, conditional on data until SKEW final methodology, authorized vintage, rights for all sources, coverage and event counts verified. Candidate 2013 restatement may invalidate 1990–2025 sample. No empirical finding.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** blocked. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **CBOE_SKEW — SKEW daily closing history (one documented methodology)**: SKEW_History.csv. Route: https://cdn.cboe.com/api/global/us_indices/daily_prices/SKEW_History.csv. Provider: https://www.cboe.com/data/quotes/skew/metrics/. Dashboard visible. A separate Oct 2026 methodology consultation was surfaced; final effective method/history not established here. Verify announcement, vintage and historical recalculation before use. Prior link status: Candidate CSV endpoint; provider dashboard and Oct 2026 consultation checked, not retrieved.
- **FF3D — US FF3 daily**: F-F_Research_Data_Factors_daily_CSV.zip. Route: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip. Provider: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct link observed in provider page; bytes not inspected.
- **VIXCLS — VIXCLS**: VIXCLS.csv. Route: https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS. Provider: https://fred.stlouisfed.org/series/VIXCLS. Inherited inventory route; re-check provider, schema, vintage and permissions locally. Prior link status: Direct CSV endpoint constructed from exact series ID; not fetched.

### Acceptance of the local input set

Resolve final Cboe methodology, rights and full exchange calendar for every month. Predeclare split and event count/power gate; no post hoc threshold changes. Historical consultation is not final.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If rights or event counts fail, retitle as a synthetic test of implied tail-risk signals under independently specified P and Q; no market forecasting claims. Distinguish from nearby option-skew pricing projects by forecast scoring.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
