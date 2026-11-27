# Data and model setup | A01.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French Portfolios Formed on Market Beta, 25 Size and Market Beta, FF3 and FF5 monthly, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. AQR US monthly BAB, https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly, complementary series. Use common 1965-2025 sample where feasible; verify sorted portfolio labels, value-weighted panels and RF, use common available BAB sample separately. Compare 1965-1999 and 2000-2025 without ex post selection.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFBETA — US beta portfolios monthly** (Core / planned robustness). Expected file: `Portfolios_Formed_on_BETA_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Portfolios_Formed_on_BETA_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFSIZEBETA — US size-beta 25 monthly** (Core / planned robustness). Expected file: `25_Portfolios_ME_BETA_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_BETA_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **BAB — Betting Against Beta: Equity Factors Data, Monthly** (Core / planned robustness). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly); [provider page](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly). Historical v13 inventory note (unverified in current release): Exact dataset page; direct file URL unresolved. Select named dataset download and retain original file; verify usage terms, no arbitrary substitution.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Freeze 1965–1999/2000–2025. Verify beta-sort and 5×5 size-beta ordering from provider metadata; estimate realized beta, not the formation signal. Compare low-minus-high mean and CAPM/FF3/FF5 alpha separately, with paired date-block bootstrap. Use AQR US monthly BAB only over its available joint dates, not subtract RF from long-short spread. Use published factors as distinct complement; no assumption BAB is exactly beta-neutral in sample.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; BAB is a complementary route only if authorized; do not label low-minus-high as BAB.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Freeze provider labels, estimate realized beta separately, compare all within-size low/high groups and refit in paired month blocks. BAB is complementary only; do not rename an unscaled spread BAB or infer a funding constraint from the line alone.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
