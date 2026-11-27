# Data and model setup | A04.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use US news-based monthly index USEPUNEWSINDXM and composite USEPUINDXM from https://fred.stlouisfed.org/series/USEPUNEWSINDXM and https://fred.stlouisfed.org/series/USEPUINDXM; VIXCLS end-month and French daily market total returns https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Common 1990-2025 target, train to 2004, validation 2005-2009, test 2010-2025. Use EPU lagged one month at origin, and actual release/vintage check (historical reconstruction is not real-time). News index baseline; composite robustness includes non-news components. VIX percent converted to decimals.

## Inputs
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **VIXCLS — VIXCLS** (Core). Expected file: `VIXCLS.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS); [provider page](https://fred.stlouisfed.org/series/VIXCLS). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Daily closing index, monthly mean only for spread study.
- **USEPUNEWSINDXM — US monthly news-based EPU** (Core). Expected file: `USEPUNEWSINDXM.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USEPUNEWSINDXM); [provider page](https://fred.stlouisfed.org/series/USEPUNEWSINDXM). Historical v13 inventory note (unverified in current release): Series metadata confirmed; standard FRED CSV endpoint, not retrieved. Check units, publication lag/vintage, citation and redistribution conditions; composite includes other components.
- **USEPUINDXM — US monthly composite EPU** (Core robustness). Expected file: `USEPUINDXM.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USEPUINDXM); [provider page](https://fred.stlouisfed.org/series/USEPUINDXM). Historical v13 inventory note (unverified in current release): Series metadata confirmed; standard FRED CSV endpoint, not retrieved. Check units, publication lag/vintage, citation and redistribution conditions; composite includes other components.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
FF3D daily total market log returns, full calendar monthly sum squares; no intraday RV claim. VIX at last common session, convert index points to decimal annual volatility and square/divide 12 as monthly horizon proxy, not exact physical expected variance. News EPU lagged one month and release checked; if later, longer lag; historical reconstruction/revisions pseudo-OOS. Composite EPU robustness includes non-news components. Use common positive rows, nested log-link or log OLS with training-only smearing and expanding matured labels. Initial train through 2004, validation 2005-09, test 2010-25; no test-based selection. Compare lag RV, VIX-only and joint with/without EPU; paired QLIKE differences block bootstrap, refit sensitivity, report availability losses.

## Acceptance and first meeting
Actual FF3D/VIX/EPU data rights, calendar, release lag and common sample required; VIX rights particularly important. News and composite not interchangeable. Smearing/positive forecast check only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Use US news-based monthly index USEPUNEWSINDXM and composite USEPUINDXM from https://fred.stlouisfed.org/series/USEPUNEWSINDXM and https://fred.stlouisfed.org/series/USEPUINDXM; VIXCLS end-month and French daily market total returns https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Common 1990-2025 target, train to 2004, validation 2005-2009, test 2010-2025. Use EPU lagged one month at origin, and actual release/vintage check (historical reconstruction is not real-time). News index baseline; composite robustness includes non-news components. VIX percent converted to decimals.

## Design-specific acceptance

Freeze lag and return-calendar coverage; use only published EPU and VIX at origin, report conservative extra-lag sensitivity. Match forecast horizon, positive variance units and common origins; train smearing only on mature outcomes; compare paired QLIKE/MSE and crisis sensitivity, no causal claim.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
