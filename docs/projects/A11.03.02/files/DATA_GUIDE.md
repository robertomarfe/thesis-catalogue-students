# Data and model setup | A11.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly FF3 and 10 industry value-weighted portfolios from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, Goyal predictors https://sites.google.com/view/agoyal145/; target 1963-2025, train through 1999, evaluate 2000-2025. Use RF timing from documentation (align known holding-period bill return), excess returns in decimals, one-month lag for dp and spread. Standardize instruments with training means/SD. Start with 5 fixed industry portfolios or all 10 with adequate observations; separate FF3 pricing of factors from evaluation assets.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use FF3 and fixed five or all ten VW industries; Goyal dp/tms definitions, lagged calendar month only and standardize using 1963–99 training mean/SD. Build z=(1,dp,tms); align holding-period RF to factor returns; m=(1-b'(f-mu_train))/Rf, include both mRf-1 and m times excess return, do not assume conditional bill Euler holds. Fit constant instruments then augmented GMM with common weight, freeze coefficients and train mean on 2000–25. Refit paired block samples; rank, negativity, HAC ridge and J caveats. Conditional b extension optional, not baseline.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; verify Goyal workbook/sheet and info lag, actual sample, no real-time claim from revised vintage.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify lagged calendar and actual availability of predictors; revised data do not establish a real-time exercise. Standardize with training statistics only. Include bill moments, report negativity and rank, and use paired refits to assess held-out pricing error differences.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
