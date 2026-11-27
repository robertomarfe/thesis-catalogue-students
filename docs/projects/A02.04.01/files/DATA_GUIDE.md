# Data and model setup | A02.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal monthly predictors and market excess returns https://sites.google.com/view/agoyal145/; use dividend-price, earnings-price and term spread as prespecified predictors and historical average; French monthly RF/market if necessary https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1965-2025 with initial 20-year training, validation ending 2004, locked final 2005-2025; confirm units and availability. One-month lag for published accounting/macroeconomic variables or conservative additional lag. gamma=3,5,10 fixed, wmax=1 baseline, 0/10/25 bp costs.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use a common lagged variance model and same return/RF source, w=clip(mu/(gamma*v),0,1). Baseline gamma 3/5/10, costs 0/10/25 bp on absolute traded stock weight relative to previous drifted weight. Deduct costs at start before return. Evaluate monthly CE annualized by 12 as arithmetic approximation, gross/net Sharpe, turnover and drawdown; no forecast-dependent volatility specification.

## Acceptance and first meeting
Actual Goyal/French common units, dates and RF gate open. Verify self-financing drift and cost identity; strategy needs consecutive months.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal monthly predictors and market excess returns https://sites.google.com/view/agoyal145/; use dividend-price, earnings-price and term spread as prespecified predictors and historical average; French monthly RF/market if necessary https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1965-2025 with initial 20-year training, validation ending 2004, locked final 2005-2025; confirm units and availability. One-month lag for published accounting/macroeconomic variables or conservative additional lag. gamma=3,5,10 fixed, wmax=1 baseline, 0/10/25 bp costs.

## Design-specific acceptance

Reconcile two consecutive months manually including drifted weight and fees; no contemporaneous variance; check compounding and return units; net CE comparison on common dates; clearly label cost-on-pretrade approximation and annualization.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
