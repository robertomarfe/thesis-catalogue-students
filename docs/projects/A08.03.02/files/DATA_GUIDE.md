# Data and model setup | A08.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Daily and monthly US market/RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; target 1990-2025, train 1990-2004, evaluation 2005-2025. Monthly decisions based on trailing 21/63/252 trading-day returns, annualize by 252; targets 10% and 15%, w_max=1,1.5,2; funding spread 0/100/200 bp annual and trading 0/10/25 bp of turnover. Static comparator uses training-only volatility and same cap; no realized test risk matching in baseline.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
At each month-end use complete trailing 21/63/252 daily total market returns (Mkt-RF+RF), annualize SD sqrt(252); target .10/.15, cap 1/1.5/2. Forecast only with data through t, hold next monthly total market and RF. Borrowing spread 0/100/200bp annual charged on negative cash weight; equity turnover against drifted weight, 0/10/25bp per dollar. Static comparator set with 1990-2004 training-only volatility/cap; 2005-25 final. No ex-post risk matching. Report insolvent paths rather than silently omit; compare net returns and leverage/trading distribution. Daily RF and monthly RF use consistent source vintage, audit month compounding.

## Acceptance and first meeting
Actual FF3D and FF3M calendars/coverage, rate and funding units; exact drift and borrowing check.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Daily and monthly US market/RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; target 1990-2025, train 1990-2004, evaluation 2005-2025. Monthly decisions based on trailing 21/63/252 trading-day returns, annualize by 252; targets 10% and 15%, w_max=1,1.5,2; funding spread 0/100/200 bp annual and trading 0/10/25 bp of turnover. Static comparator uses training-only volatility and same cap; no realized test risk matching in baseline.

## Design-specific acceptance

Check target/cap and funding ledger against two hand-computed periods; keep realized equity and cash returns separately, lag volatility at month end, disclose haircut cost approximation and insolvencies. Predeclare static matched-risk rule and borrowing spread; report turnover, downside, CE and paired test uncertainty.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
