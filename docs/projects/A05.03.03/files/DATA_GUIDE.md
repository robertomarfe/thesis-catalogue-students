# Data and model setup | A05.03.03

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW nominal zeros and Philadelphia Fed SPF mean levels/GDP/CPI and release dates https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts. Quarterly formation on last trading day of survey quarter, conditional on documented release before decision; lag curves as necessary for publication. Proposed 1981-2025 with matched same-vintage next-four-quarter growth and inflation, verify exact coverage. Forecast 1Y excess holding returns of 2,5,10Y zeros; quarterly overlapping labels must fully mature before entering training. Initial 20 years if feasible; expanding OLS/ridge, pre-test tuning. Benchmark historical mean and yield-curve-only model.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **SPFLEVEL — SPF mean forecast levels** (Core). Expected file: `meanLevel.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/meanLevel.xlsx?hash=A51C49A6FCF80FE18F2CE81D903F4970&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Link status from v13 inventory: Direct link observed; file not inspected. RGDP level forecasts; same-vintage ratios; preserve documentation.
- **SPFCPI — SPF CPI mean forecast** (Core). Expected file: `Mean_CPI_Level.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/data-files/files/Mean_CPI_Level.xlsx?hash=988348DA9D1AA5EE5B778F6B760F7A1C&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/cpi-spf). Link status from v13 inventory: Direct link observed; file not inspected. Annualized percentage points based on quarterly-average SA index.
- **SPFDATES — SPF release dates** (Core). Expected file: `spf-release-dates.txt`. [Download or provider route](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Link status from v13 inventory: Exact link listed in provider documentation; file not inspected. Verify actual coverage and date conventions; do not guess release days.
- **SPF_D2 — SPF D2 forecast dispersion of Q/Q growth** (Optional extension). Expected file: `Dispersion_2.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/Dispersion_2.xlsx?hash=E0A0D114F37EC56209ECB512CA07FA84&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/dispersion-forecasts). Link status from v13 inventory: Exact provider-linked workbook observed 2026-11-25; unsupported binary content in web fetch. D2=75th minus 25th percentile of individual annualized Q/Q growth forecasts in percentage points, not volatility of expected growth; use RGDP horizon T+1, check release dates and coverage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Inspect SPF mean-level GDP/CPI tabs and release dates; document forecast horizon and same-survey base, compute next-four-quarter growth from the available base and horizon only; no later vintage denominators. Join to last trading day of survey quarter using actual release dates (exclude same-day unless release time precedes formation). Construct 2,5,10Y aged one-year returns using 1,2,4,5,9,10Y; use historical mean/yield-only/augmented OLS/ridge with quarterly matured labels and HAC >=3.

## Acceptance and first meeting
Actual SPF horizon definitions, releases and GSW common sample pending. If coverage inadequate use one released horizon and two maturities as minimum; optional dispersion not a substitute for growth.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Require release and horizon metadata before estimation. If necessary use the original minimum of one released horizon and two maturities; do not substitute dispersion for expected growth. Label the result pseudo-OOS unless vintages are truly reconstructible.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
