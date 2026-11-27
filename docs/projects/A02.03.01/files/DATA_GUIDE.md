# Data and model setup | A02.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal combined predictor workbook https://sites.google.com/view/agoyal145/, target monthly US excess returns 1963-2025; verify fields for dp, ep, bm, tbl, tms, dfy, svar and total returns/RF. Fix these seven candidates before test; conservative one-month lag on predictors and data vintage caveat. Train through 1989, validation 1990-1999, test 2000-2025. Use expanding regressions; update weights from rolling 120 matured one-step forecasts or available history. Historical mean uses same available return history.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Predeclare seven Goyal predictors and common sample before outcome inspection. At origin t combine individual expanding forecasts using equal weights and inverse MSE on last 120 common matured forecast errors; never in-sample residuals. If fewer matured errors, use available documented history or equal weights under a fixed minimum. Freeze validation decisions before test.

## Acceptance and first meeting
Actual Goyal schema and common dates pending; check combination weights sum to one and ignore immature errors.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal combined predictor workbook https://sites.google.com/view/agoyal145/, target monthly US excess returns 1963-2025; verify fields for dp, ep, bm, tbl, tms, dfy, svar and total returns/RF. Fix these seven candidates before test; conservative one-month lag on predictors and data vintage caveat. Train through 1989, validation 1990-1999, test 2000-2025. Use expanding regressions; update weights from rolling 120 matured one-step forecasts or available history. Historical mean uses same available return history.

## Design-specific acceptance

Toy equal weights sum to one; no immature loss in the adaptive window; perturb future targets and verify earlier weights unchanged; audit common component availability and fixed predictor membership.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
