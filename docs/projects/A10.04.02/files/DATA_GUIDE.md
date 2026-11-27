# Data and model setup | A10.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Simulation: T=600 months, 300 initial train, 150 development, 150 final; r=0.005+0.04*z with Gaussian z, second null with GARCH-like conditional heteroskedasticity but constant mean. Generate independent AR(1) predictors (phi=0.8), with block-correlated features in second scenario. Candidate counts 10,50,200 nested feature sets; model per predictor expanding OLS plus mean benchmark. At least 300 replications fixed seed, increase for precision. Real illustration: French monthly market excess return and lagged factor returns (FF3, momentum and reversal where verified), lags 1-12 and rolling means prespecified to generate candidates; common 1931-2025 or shorter. https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Real data need not satisfy null.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core / planned robustness). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFST — US short-term reversal monthly** (Core / planned robustness). Expected file: `F-F_ST_Reversal_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_ST_Reversal_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFLT — US long-term reversal monthly** (Core / planned robustness). Expected file: `F-F_LT_Reversal_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_LT_Reversal_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Freeze T=600, 300/150/150, nested candidate counts 10/50/200, iid and conditional-variance null, AR(1) phi .8, >=300 common-seed replications. Compare development-selected final performance against same-final best (invalid oracle, deliberately labeled). Report paired differences and uncertainty. Real illustration uses FF3/Mom/ST/LT lagged candidates if actual authorized files, no claim real data satisfy null. Synthetic-only redesign requires explicit approval.

## Acceptance and first meeting
Synthetic null/selection check passed locally; real illustration required by original MVT, actual French files pending. Verify fixed common split, candidate nesting, no test-tuning for honest protocol.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Simulation: T=600 months, 300 initial train, 150 development, 150 final; r=0.005+0.04*z with Gaussian z, second null with GARCH-like conditional heteroskedasticity but constant mean. Generate independent AR(1) predictors (phi=0.8), with block-correlated features in second scenario. Candidate counts 10,50,200 nested feature sets; model per predictor expanding OLS plus mean benchmark. At least 300 replications fixed seed, increase for precision. Real illustration: French monthly market excess return and lagged factor returns (FF3, momentum and reversal where verified), lags 1-12 and rolling means prespecified to generate candidates; common 1931-2025 or shorter. https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Real data need not satisfy null.

## Design-specific acceptance

Perturb immature/final targets and ensure development winner is unchanged. Check nested candidate membership, paired common draws, strict boundary purge and same benchmark dates. Oracle never used in deployable policy. Real illustration remains required under original scope.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
