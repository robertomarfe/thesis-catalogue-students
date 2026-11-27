# Data and model setup | A01.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French monthly US 25 size/book-to-market value-weighted portfolios, monthly FF3 market and RF, and 30 industry portfolios as separate robustness panel; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed July 1963-December 2025, common valid dates; remove documented missing sentinels and divide percentages by 100. Predeclare split 1963-1993/1994-2025. Estimate CAPM on same excess returns for all tests; FF3 only as diagnostic benchmark, not a replication of the FF3-vs-FF5 thesis.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core / planned robustness). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core / planned robustness). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use 25 VW size/BM as primary, 30 industries separately. RF exactly once; common dates July 1963–Dec 2025 and frozen 1993 break. Estimate CAPM alpha, GRS and robust joint alpha, descriptive two-pass with intercept and no intercept; compare slope to mean market premium. Re-estimate betas and premia within jointly resampled circular month blocks (6/12/24 months, ≥999 successful draws if feasible); report failed draws and percentile intervals. Do not use annualized slopes in monthly tests.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; confirm 25 labels, two separate panels, positive GRS df and noncompressed monthly sample.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use one RF subtraction, common complete dates and separate portfolio panels. Report T, N, K, eigenvalues and failed draws. Re-estimate both regression passes in joint date blocks; do not interpret a rejected joint hypothesis as proof of inefficiency.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
