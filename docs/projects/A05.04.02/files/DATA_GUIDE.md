# Data and model setup | A05.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Fed GSW nominal and TIPS fitted real/compensation curves https://www.federalreserve.gov/data/tips-yield-curve-and-inflation-compensation.htm, TIPS history from 1999 per provider; SPF CPI mean level forecasts and release dates, FRED CPIAUCSL, NFCI. Proposed 2003-2025 quarterly sample, 5Y and 10Y matched zero yields, use SPF CPI10 mean (https://www.philadelphiafed.org/surveys-and-data/cpi10), annual average over current and next nine calendar years; check timing against rolling 10Y yield and disclose horizon mismatch; do not use short SPF horizon to subtract from 10Y BEI. If horizon discrepancy cannot be reconciled or data are unavailable, restrict to co-movement and no residual decomposition. Quarterly survey-date or end-quarter matching with known release, trailing inflation volatility as proxy, not expected uncertainty.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **SPFDATES — SPF release dates** (Core). Expected file: `spf-release-dates.txt`. [Download or provider route](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Link status from v13 inventory: Exact link listed in provider documentation; file not inspected. Verify actual coverage and date conventions; do not guess release days.
- **CPIAUCSL — CPIAUCSL** (Core). Expected file: `CPIAUCSL.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL); [provider page](https://fred.stlouisfed.org/series/CPIAUCSL). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly SA CPI; quarterly average; annualization match.
- **GSW_TIPS — Fitted real TIPS zero yields and inflation compensation** (Core). Expected file: `feds200805.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200805.csv); [provider page](https://www.federalreserve.gov/data/tips-yield-curve-and-inflation-compensation.htm). Link status from v13 inventory: Direct CSV linked; binary unsupported by web fetch, not validated. 1999 onward per provider; verify valid maturity coverage, units and compounding; revisions documented.
- **SPF_CPI10 — Mean 10-year CPI inflation forecasts (CPI10)** (Conditional extension; baseline co-movement feasible without subtraction). Expected file: `Mean_CPI10_Level.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/data-files/files/Mean_CPI10_Level.xlsx?hash=25A051025B7E9CC911D135B577C44502&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/cpi10). Link status from v13 inventory: Direct Mean Responses link observed; binary unsupported, not validated. Annualized percent, current and next nine calendar years. Not automatically same as rolling 10-year bond horizon; residual only with reconciled timing.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Read GSW TIPS real continuously compounded zero yields and nominal GSW at exact common dates and 5/10Y; compute BEI as nominal minus real, cross-check provider matched conventions. Sample quarterly with known survey release. Construct trailing CPI volatility and NFCI with documented lag. CPI10 refers to current plus next nine calendar years, not an exact rolling 10Y forecast. If horizon mismatch cannot be reconciled, restrict to co-movement and no residual decomposition.

## Acceptance and first meeting
Actual TIPS/nominal date-maturity coverage, units, rights, survey release gate open. Subtraction of CPI10 only after approved horizon match; no pure inflation risk premium identification because liquidity and model effects.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify nominal/real compounding, exact common dates, provider identity and release. Never claim a residual decomposition if the survey alignment fails. This thesis studies inflation compensation, not an ACM nominal premium.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
