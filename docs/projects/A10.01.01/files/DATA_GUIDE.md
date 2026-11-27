# Data and model setup | A10.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use author-listed Goyal/Welch updated monthly dataset through 2025 https://sites.google.com/view/agoyal145/ . Freeze vintage and exact columns: log dividend-price, earnings-price, book-to-market, term spread, default spread, T-bill and inflation where available; use only verified timing definitions, lag macro/accounting proxies at least one month when releases uncertain. Excess target total market return minus matching RF using supplied columns, not price-only return. Aim 1927-2025 common sample; initial training through 1964, 1965-1999 development, 2000-2025 untouched final evaluation; shorten consistently if file coverage requires it. Retrospective revised data are pseudo-real-time.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core / planned robustness). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Freeze Goyal seven predictors and calendar. Standardize independently inside each training fold; unpenalized intercept. sklearn Ridge objective uses sum of squares plus alpha L2; LASSO objective uses SSE/(2n)+alpha L1: report actual conventions and scale grid accordingly. Tune ridge/LASSO/elastic net on nested past-origin errors only; no final selection.

## Acceptance and first meeting
Actual workbook and predictor timing open. Synthetic tuning checks exclude immature fold labels; perturb future features and outcomes.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Use author-listed Goyal/Welch updated monthly dataset through 2025 https://sites.google.com/view/agoyal145/ . Freeze vintage and exact columns: log dividend-price, earnings-price, book-to-market, term spread, default spread, T-bill and inflation where available; use only verified timing definitions, lag macro/accounting proxies at least one month when releases uncertain. Excess target total market return minus matching RF using supplied columns, not price-only return. Aim 1927-2025 common sample; initial training through 1964, 1965-1999 development, 2000-2025 untouched final evaluation; shorten consistently if file coverage requires it. Retrospective revised data are pseudo-real-time.

## Design-specific acceptance

Persist scaler means/SD and mature fold IDs; perturb future features and immature labels; earlier tuning and forecasts must be invariant. Check zero penalty against OLS when rank permits; document alpha conventions and zero-variance features.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
