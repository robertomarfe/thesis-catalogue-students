# Data and model setup | A02.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal monthly predictor workbook, https://sites.google.com/view/agoyal145/, and FRED GS10, TB3MS for monthly rates, https://fred.stlouisfed.org/. Use Goyal total market returns/RF and dp with documented definitions; rates in percent convert consistently. Target 1965-2025 common sample with 1965-1994 initial training and 1995-2025 expanding evaluation, validation of data conventions before freezing. Lag monthly rate averages by one month to ensure availability; revised file is pseudo-OOS. Fix one-month primary horizon and 12-month secondary horizon with matured training labels.

## Inputs
- **GS10 — GS10** (Core / planned robustness). Expected file: `GS10.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=GS10); [provider page](https://fred.stlouisfed.org/series/GS10). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly Treasury yield percent.
- **TB3MS — TB3MS** (Core / planned robustness). Expected file: `TB3MS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS); [provider page](https://fred.stlouisfed.org/series/TB3MS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly discount-basis bill rate.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core / planned robustness). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
GS10 and TB3MS are monthly average annualized percent rates, not realized monthly RF. Lag both by one calendar month. Use dp alone, rates alone and combined on common Goyal target. 12-month secondary horizon requires maturity audit. Record whether rate effects remain conditional on valuation.

## Acceptance and first meeting
Actual Goyal, GS10, TB3MS histories and timing open; confirm rates are percent and monthly average. Test compounded 12-month label and strict end-date purge.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal monthly predictor workbook, https://sites.google.com/view/agoyal145/, and FRED GS10, TB3MS for monthly rates, https://fred.stlouisfed.org/. Use Goyal total market returns/RF and dp with documented definitions; rates in percent convert consistently. Target 1965-2025 common sample with 1965-1994 initial training and 1995-2025 expanding evaluation, validation of data conventions before freezing. Lag monthly rate averages by one month to ensure availability; revised file is pseudo-OOS. Fix one-month primary horizon and 12-month secondary horizon with matured training labels.

## Design-specific acceptance

First three forecasts recomputed by hand; no forward fill from later observations; exact common evaluation origin list; risk-free and yield units checked separately. Negative OOS R2 retained.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
