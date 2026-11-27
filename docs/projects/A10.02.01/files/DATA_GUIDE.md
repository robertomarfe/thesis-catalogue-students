# Data and model setup | A10.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal combined monthly workbook, https://sites.google.com/view/agoyal145/, target 1950-2025. Prespecify 6 predictors (dp, ep, svar, tbl, tms, dfy; verify definitions, release timing and units); use data dated t-1 to predict t+1 as conservative common lag. Construct documented monthly excess return; initial training 1950-1989, validation rolling 1990-2004 and untouched final 2005-2025. Nested chronological validation within each training window, small grid depth 1-3, min leaf 24/48, 200 forest trees, boosting learning rates 0.03/0.1 and iterations 50/100; fixed seed 2718. Ridge uses same inputs and past-only standardization.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Freeze original six features and small RF/boosting grid, training-only scaler inside pipeline. Tune on past folds, lock model menu; report time budget and failed fits. Compare ridge and mean on exact dates, permutation/partial dependence only on past validation; no outcome-driven feature search.

## Acceptance and first meeting
Actual Goyal workbook pending. Test bounded ensemble fit and past-only tuning on known nonlinear DGP; no claim of superiority.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal combined monthly workbook, https://sites.google.com/view/agoyal145/, target 1950-2025. Prespecify 6 predictors (dp, ep, svar, tbl, tms, dfy; verify definitions, release timing and units); use data dated t-1 to predict t+1 as conservative common lag. Construct documented monthly excess return; initial training 1950-1989, validation rolling 1990-2004 and untouched final 2005-2025. Nested chronological validation within each training window, small grid depth 1-3, min leaf 24/48, 200 forest trees, boosting learning rates 0.03/0.1 and iterations 50/100; fixed seed 2718. Ridge uses same inputs and past-only standardization.

## Design-specific acceptance

No random cross-validation; identical dates/features and mature label rules; perturb future inputs and labels; verify depth/minimum leaf constraints; record seeds and failed fits, not only successful winners.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
