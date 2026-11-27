# Data and model setup | A02.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly Goyal/Welch updated dataset https://sites.google.com/view/agoyal145/; verify dividend and index columns, total market returns including dividends and RF. Proposed 1950-2025; use common endpoint across h and document whether returns reconstructed or supplied. Freeze horizon grid h=1,3,12; h=60 optional. Use 2,000+ null simulations, observed T and covariance; assess rho estimates plus local-to-unity sensitivity. Revised data are acceptable for retrospective inference, not live forecasts.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core / planned robustness). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use gross total and bill compounded separately for simple h-month excess (or explicitly choose additive log excess consistently). Common complete origins h=1,3,12. For null simulation choose log excess additive version or simulate gross total/bill consistent with observed units; estimate persistence and innovation correlation under slope-zero null, compare naive/HAC t and max |t| across horizons per same simulated path; >=2000 replications left to student.

## Acceptance and first meeting
Actual workbook and calendar/return convention must pass. Check finite-sample null persistence and innovation sign; synthetic overlap sum and HAC slope test are primitives, not a size/power study.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Monthly Goyal/Welch updated dataset https://sites.google.com/view/agoyal145/; verify dividend and index columns, total market returns including dividends and RF. Proposed 1950-2025; use common endpoint across h and document whether returns reconstructed or supplied. Freeze horizon grid h=1,3,12; h=60 optional. Use 2,000+ null simulations, observed T and covariance; assess rho estimates plus local-to-unity sensitivity. Revised data are acceptable for retrospective inference, not live forecasts.

## Design-specific acceptance

Check that h=1 target uses only t+1; h=12 uses exactly 12 consecutive months; incomplete paths are excluded. Compare simple and HAC inference on a toy sequence. Verify joint critical value is based on max absolute t from the same path, not independent marginal draws. Preserve negative and insignificant results.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
