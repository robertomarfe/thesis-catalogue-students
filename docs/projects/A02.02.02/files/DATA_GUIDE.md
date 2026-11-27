# Data and model setup | A02.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Weekly Chicago Fed NFCI https://fred.stlouisfed.org/series/NFCI and ANFCI for robustness, Goyal monthly Data2025 workbook https://sites.google.com/view/agoyal145/ (total equity return, bill and log dividend-price ratio); FF3 monthly for cross-check. Start 1973 or first common month, initial training to 1999, 2000-2009 validation, 2010-2025 final test. Use only NFCI observations released by month-end, conservatively lag one calendar month for revised series; target next-month simple excess return. Freeze all models before final test.

## Inputs
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **ANFCI — ANFCI** (Optional sensitivity). Expected file: `ANFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=ANFCI); [provider page](https://fred.stlouisfed.org/series/ANFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Adjusted NFCI.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.
- **FF3M — US FF3 monthly** (Optional cross-check). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Map weekly NFCI observations to calendar month, use latest observation whose release date precedes origin if vintage available; otherwise lag last observation of prior month conservatively, no forward fill beyond one month. ANFCI sensitivity only. Freeze dp and combined models by validation end and retain 2010–2025 final dates. Separate FF3 optional cross-check from target definition.

## Acceptance and first meeting
NFCI, Goyal actual files and historical release timestamps open; revised monthly lag not real-time. Artificial perturbation after origin verifies no use of future target or scaling.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Weekly Chicago Fed NFCI https://fred.stlouisfed.org/series/NFCI and ANFCI for robustness, Goyal monthly Data2025 workbook https://sites.google.com/view/agoyal145/ (total equity return, bill and log dividend-price ratio); FF3 monthly for cross-check. Start 1973 or first common month, initial training to 1999, 2000-2009 validation, 2010-2025 final test. Use only NFCI observations released by month-end, conservatively lag one calendar month for revised series; target next-month simple excess return. Freeze all models before final test.

## Design-specific acceptance

Assert availability timestamp <= origin for every observation. Perturb all post-origin NFCI observations and ensure features do not change. Check holidays, missing weeks, release lag and common sample. Flag revised values.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
