# Data and model setup | A04.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
SPF mean CPI quarterly forecasts, https://www.philadelphiafed.org/surveys-and-data/cpi-spf; use prior-quarter survey forecast for the target quarter, based on actual release dates. Convert annualized rate using provider convention and compare to quarterly-average seasonally adjusted CPIAUCSL from FRED, https://fred.stlouisfed.org/series/CPIAUCSL. Monthly French 30 industries, 25 size/BM and FF3 from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html compounded to quarters. Target 1985-2025 common sample if available; alternatively use a rolling AR inflation forecast with lagged released data, explicitly labeled proxy.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core / planned robustness). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core / planned robustness). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CPIAUCSL — CPIAUCSL** (Core / planned robustness). Expected file: `CPIAUCSL.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL); [provider page](https://fred.stlouisfed.org/series/CPIAUCSL). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly SA CPI; quarterly average; annualization match.
- **SPFCPI — SPF CPI mean forecast** (Core / planned robustness). Expected file: `Mean_CPI_Level.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/data-files/files/Mean_CPI_Level.xlsx?hash=988348DA9D1AA5EE5B778F6B760F7A1C&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/cpi-spf). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Annualized percentage points based on quarterly-average SA index.
- **SPFDATES — SPF release dates** (Core / planned robustness). Expected file: `spf-release-dates.txt`. [Download or provider route](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Historical v13 inventory note (unverified in current release): Exact link listed in provider documentation; file not inspected. Verify actual coverage and date conventions; do not guess release days.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use previous-quarter SPF mean CPI forecast for target q, verify actual release and annualized quarterly-average SA CPI definition. Convert annualized published mean pp to quarterly simple rate via (1+f/100)^(1/4)-1; nonlinear transform of mean is not mean of individually converted forecasts. Compute realization from three monthly SA CPI levels in each adjacent quarter, forecast error on same convention. Compound French market, RF and portfolio returns separately; compute nominal excess and real excess after deflation, total real hedge returns separately. Estimate market-controlled inflation betas with HAC; jointly resample calendar quarters and re-estimate both beta and cross-sectional slopes (do not bootstrap assets independently). 1985-2025 target with actual coverage, industry baseline and characteristic portfolios robustness; fixed pre/post-2000 split. AR proxy only with approval and disclosed distinct design.

## Acceptance and first meeting
Actual SPF CPI horizon, rates, releases, monthly CPI, French FF3M/30 industry/25 size-BM inputs and rights required; matched-quarter and real-return identities checked on artificial data only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

SPF mean CPI quarterly forecasts, https://www.philadelphiafed.org/surveys-and-data/cpi-spf; use prior-quarter survey forecast for the target quarter, based on actual release dates. Convert annualized rate using provider convention and compare to quarterly-average seasonally adjusted CPIAUCSL from FRED, https://fred.stlouisfed.org/series/CPIAUCSL. Monthly French 30 industries, 25 size/BM and FF3 from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html compounded to quarters. Target 1985-2025 common sample if available; alternatively use a rolling AR inflation forecast with lagged released data, explicitly labeled proxy.

## Design-specific acceptance

Hand-check one quarterly-average CPI realization and one forecast error from the prior vintage; compound market, portfolio and bill legs separately. Estimate nominal and real exposures on matched quarters and jointly bootstrap quarters, re-estimating both stages. Report common sample, rank, regime split and revised-CPI caveat.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
