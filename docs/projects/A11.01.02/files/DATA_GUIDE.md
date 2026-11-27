# Data and model setup | A11.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly FF3 and 25 size/BM and 30 industry value-weighted test portfolios from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Use RF subtraction once, decimal returns, 1965-2025 common dates. First use identical sample means/covariances and identity weights in both forms. Then compare diagonal inverse residual-variance and regularized covariance weights, free lambda versus traded restriction lambda=mean(f). Use factor and test asset data on identical dates.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core / planned robustness). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core / planned robustness). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use FF3 and separate 25 VW size/BM and 30 industry panels 1965–2025. Compute ML sample covariances with same dates; free lambda via common W and traded lambda=mean(f). Transform b=Omega^{-1}lambda; verify both pricing errors and objective at machine tolerance. Use diagonal inverse residual variance and regularized covariance on same dates, report weight eigenvalues and negative SDF frequency. Bootstrap all means, covariances, betas and weights jointly; normalized m is not a gross bill pricing kernel.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; verify rank Omega and B; common W for equivalence, same factor conventions, not full riskfree pricing claim.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use identical sample conventions for both representations and common WLS weights; verify error equivalence before varying weights. Separate free versus traded lambda, report rank, sign diagnostics and joint date-block refits.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
