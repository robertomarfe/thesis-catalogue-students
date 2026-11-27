# Data and model setup | A02.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal updated predictor workbook https://sites.google.com/view/agoyal145/; monthly excess returns and predeclared dp, term spread and dividend yield (if near collinear replace dy with default spread by prespecified availability/collinearity rule, no outcome search). Target 1950-2025, first forecast after 240 months. Compare expanding OLS, rolling 120/240 months and exponential weights half-life 120 months; fixed windows. Main 1-month target, optional 12-month matured labels. Current revised workbook pseudo-OOS; document release lags and exact predictor definitions.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Fixed expanding, rolling 120/240 months and exponentially weighted OLS half-life 120. Predeclare collinearity rule using training data only. In artificial piecewise slope scenario compare adaptation delay, then actual common dates; no ex-post breakpoint used to forecast. Use historical mean baseline.

## Acceptance and first meeting
Goyal actual data pending. Verify expanding/rolling counts and decay weights against independent weighted least squares.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal updated predictor workbook https://sites.google.com/view/agoyal145/; monthly excess returns and predeclared dp, term spread and dividend yield (if near collinear replace dy with default spread by prespecified availability/collinearity rule, no outcome search). Target 1950-2025, first forecast after 240 months. Compare expanding OLS, rolling 120/240 months and exponential weights half-life 120 months; fixed windows. Main 1-month target, optional 12-month matured labels. Current revised workbook pseudo-OOS; document release lags and exact predictor definitions.

## Design-specific acceptance

Hand-check weighted least squares on a toy matrix; rolling window never uses an immature label; freeze menu before holdout; report MC uncertainty and stable-null behavior; do not optimize break location on final errors.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
