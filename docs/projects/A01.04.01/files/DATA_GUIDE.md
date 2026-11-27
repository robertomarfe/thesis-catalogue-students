# Data and model setup | A01.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French monthly FF3, FF5, Mom https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, optional AQR BAB https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly. Baseline F1=FF3 (Mkt-RF,SMB,HML); F2=RMW,CMA,Mom from FF5/Mom; use FF3 SMB for baseline so the comparison is nested by construction. Target 1963-2025 common months, train to 1999, test 2000-2025. All series in same currency and decimal monthly excess/spread returns, no RF subtraction on spreads.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF5M — US FF5 monthly** (Core). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **BAB — Betting Against Beta: Equity Factors Data, Monthly** (Optional sensitivity). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly); [provider page](https://www.aqr.com/insights/datasets/betting-against-beta-equity-factors-monthly). Historical v13 inventory note (unverified in current release): Exact dataset page; direct file URL unresolved. Select named dataset download and retain original file; verify usage terms, no arbitrary substitution.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use FF3 base plus RMW/CMA from FF5 and Mom from French on common dates; align RF, no subtraction on spreads. Estimate spanning regression and joint alpha; prove squared maximum-Sharpe gain with residual covariance. Fit weights on pre-2000 or past 120 months, freeze normalization (unit gross exposure or prespecified cap) and covariance regularization. Assess realized OOS excess payoff mean/SD, turnover and cost hurdle; long-short factors not literal investable portfolios without financing conventions. Change SMB only in a separate common-base robustness.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; ensure full rank, common factor conventions, no double RF subtraction; report leverage and realized out-of-sample sample.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Distinguish literal FF5 from the nested union, do not re-subtract RF from spreads, report covariance condition and separate regularization and leverage constraints from the unrestricted identity. Refit in paired time blocks across train/test segments.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
