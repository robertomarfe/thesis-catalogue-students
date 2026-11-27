# Data and model setup | A11.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French monthly FF3, FF5, 10 industry and 25 size/BM portfolios, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Target 1963-2025; gross returns=1+decimal total return; RF is gross bill return, not constant if monthly RF varies. Train 1963-1994, evaluate 1995-2025; fit on 25 size/BM+bill and evaluate both same assets in later dates and 10 industries+bill held out in asset dimension. Use common train/evaluation sample per comparison; each sample's common second-moment matrix with identical eigenvalue tolerance, no model-specific weights.

## Inputs
- **FF5M — US FF5 monthly** (Core). Expected file: `F-F_Research_Data_5_Factors_2x3_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use FF3 and FF5, 25 VW size/BM + gross bill as training assets 1963–94; evaluate 1995–2025 on same and 10 industries+bill. Use common sample G=E[XX'] per evaluation panel for all candidates, not covariance or model-specific weights; affine m=a-b'f. Require full rank; explicit common ridge only sensitivity and label regularized metric not exact distance. Train/holdout paired block resampling within separate time segments, refit training and use identical evaluation draws. Inspect negative m and raw errors; no positivity-constrained claim.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; all gross test returns including actual monthly bill, common G and rank required.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Construct gross returns including the actual monthly bill, not excess returns with unit prices. Distinguish train and holdout metrics and apply common conditioning rules; paired time-block resampling should refit the training step and evaluate common holdout draws.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
