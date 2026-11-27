# Data and model setup | A04.03.02

**Current data gate: conditional.** No actual external input bytes are supplied or validated.

## Original input contract and sample
SF Fed USMPD https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/ includes Treasury/TIPS changes and policy surprises/code. Freeze release; choose maturities with documented same-window overlap (candidate 5y/10y, verify actual columns), common events and no imputation. Baseline statement windows, separate press conferences, never treat combined events as independent. Use provider surprise sign/scale; proposed 2004-2025 conditional on coverage. No matching across different windows.

## Inputs
- **USMPD — Full USMPD** (Core). Expected file: `USMPD.xlsx`. [Download or provider route](https://www.frbsf.org/wp-content/uploads/USMPD.xlsx?2026-11-24=); [provider page](https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Use full workbook, not chart data; query suffix may rotate.
- **USMPD_SURPRISE — Monetary policy surprises and code** (Core). Expected file: `monetary-policy-surprises.zip`. [Download or provider route](https://www.frbsf.org/wp-content/uploads/monetary-policy-surprises.zip?2026-11-24=); [provider page](https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Preserve code and event-window documentation.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use same release USMPD and rate-only surprises as A04.03.01. Verify actual same-maturity nominal and TIPS changes (candidate 5y,10y), exact same response window and documented timestamp; do not pair intraday nominal with daily real. Provider research also reports daily Treasury/TIPS responses to high-frequency surprises: if intraday matching not available, require explicit supervisor approval of daily-response redesign with both daily yield series and separate shock-window label, never silently substitute. Common finite mask for s,n,r; define BE=n-r in bp, same intercept/regressors, HC3. Coefficient identity b_BE=b_N-b_R; use paired meeting bootstrap for maturity comparisons, not independent interval subtraction. Interpret breakeven as inflation compensation including liquidity/risk premia, not pure expectation. 2004-2025 proposal target conditional on verified coverage.

## Acceptance and first meeting
CONDITIONAL: verify actual common TIPS/nominal maturity and response window, surprise definition/units, usable common events and rights. If no common window, explicit redesign or defer. Do not assume provider raw columns.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Stage 2B | Student-local acquisition and decision gate (v47)

**Current gate:** conditional. No actual empirical file or permission has been validated. Do not redistribute raw files or change data source without authorization.

### Exact requested routes

- **USMPD — Full USMPD**: USMPD.xlsx. Route: https://www.frbsf.org/wp-content/uploads/USMPD.xlsx?2026-11-24=. Provider: https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/. Full Excel listed; statements 30 minutes, press conferences 70 minutes, combined and minutes separate. Source LSEG Tick History; rights and actual maturity columns require review. Historical link note, not fresh verification: Direct link observed; file not inspected.
- **USMPD_SURPRISE — Monetary policy surprises and code**: monetary-policy-surprises.zip. Route: https://www.frbsf.org/wp-content/uploads/monetary-policy-surprises.zip?2026-11-24=. Provider: https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/. Separate ZIP contains surprise code/output; rate-path PCA, not necessarily structural shock; match release/event/window. Historical link note, not fresh verification: Direct link observed; file not inspected.

### Acceptance of the local input set

Validate one actual nominal/real maturity and exact same-window surprise mapping. Estimate all three responses with identical design rows; verify intercept and slope identity beta_BE=beta_N-beta_R and compute inference on the actual difference (not by subtracting standard errors). Report unmatched counts and TIPS caveats; if overlap fails defer or seek explicit daily redesign.

Keep a local ledger with provider, original filename, release/version or commit, download date, SHA-256, terms/permission and permitted use; inspect actual headers/tabs, date range, missing/duplicate observations, units and calendar; retain raw files only as allowed. Provide code and a nonrestricted audit summary, not raw data unless rights permit. Preserve planned common-sample and timing rules. The supervisor decides whether the input gate passes.

### If the gate fails

If common Treasury/TIPS maturity and window unavailable, defer; a daily nominal-real design requires new identification and timing protocol.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

SF Fed USMPD https://www.frbsf.org/research-and-insights/data-and-indicators/us-monetary-policy-event-study-database/ includes Treasury/TIPS changes and policy surprises/code. Freeze release; choose maturities with documented same-window overlap (candidate 5y/10y, verify actual columns), common events and no imputation. Baseline statement windows, separate press conferences, never treat combined events as independent. Use provider surprise sign/scale; proposed 2004-2025 conditional on coverage. No matching across different windows.

## Design-specific acceptance

Validate one actual nominal/real maturity and exact same-window surprise mapping. Estimate all three responses with identical design rows; verify intercept and slope identity beta_BE=beta_N-beta_R and compute inference on the actual difference (not by subtracting standard errors). Report unmatched counts and TIPS caveats; if overlap fails defer or seek explicit daily redesign.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
