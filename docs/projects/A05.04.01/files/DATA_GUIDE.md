# Data and model setup | A05.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
NY Fed ACM published monthly end-of-month term premia, fitted yields and expected-rate components, 1-10Y from 1961 according to provider https://www.newyorkfed.org/research/data_indicators/term-premia-tabs. GSW zeros for comparison, FRED INDPRO, CPIAUCSL, NFCI, USREC. Proposed common sample 1973-2025 or validated intersection; growth and inflation trailing 12 months, lag macro series at least one month and document release vintages. Descriptive revised-data regressions, predeclared predictors and subsamples. Optional Fed Board three-factor series https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm includes convexity in its TP; reconcile conventions and access before comparison.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **USREC — USREC** (Core). Expected file: `USREC.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=USREC); [provider page](https://fred.stlouisfed.org/series/USREC). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly recession indicator; retrospective.
- **INDPRO — INDPRO** (Core). Expected file: `INDPRO.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=INDPRO); [provider page](https://fred.stlouisfed.org/series/INDPRO). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly seasonally adjusted index.
- **NFCI — NFCI** (Core). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **CPIAUCSL — CPIAUCSL** (Core). Expected file: `CPIAUCSL.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL); [provider page](https://fred.stlouisfed.org/series/CPIAUCSL). Link status from v13 inventory: Direct CSV endpoint constructed from exact series ID; not fetched. Monthly SA CPI; quarterly average; annualization match.
- **ACM_MONTHLY — ACM end-month Treasury term premia, fitted yields, expected average short rates, 1-10Y** (Core). Expected file: `Monthly download (retain original name)`. [Download or provider route](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs); [provider page](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs). Link status from v13 inventory: Provider confirms downloadable monthly dataset; exact binary URL unresolved. Select monthly components; 1961 onward per provider, verify exact columns, vintage, decomposition and terms. Published output, not original proprietary input.
- **KW_NOMINAL — Kim-Wright fitted nominal yields and term premia** (Optional model comparison). Expected file: `feds200533.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200533.csv); [provider page](https://www.federalreserve.gov/data/three-factor-nominal-term-structure-model.htm). Link status from v13 inventory: Direct CSV linked; binary unsupported, not validated. Term premium includes convexity by provider convention; reconcile with ACM and compare common dates.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Download ACM monthly workbook through NY Fed Downloads; inspect fitted-yield, expected average short-rate and term-premium tabs/units and exact identity. Construct trailing 12-month log INDPRO/CPI growth; NFCI reference week versus month-end, USREC retrospective regime. For descriptive regressions use documented vintage and lag macro series at least one month; for predictive extension use actual releases/ALFRED. Compare GSW fitted yields separately and optional KW only after convexity convention reconciliation.

## Acceptance and first meeting
Actual workbook schema and bytes not verified; identity at each maturity within 5 bp initial tolerance, refine for rounding; no inferred premium from nominal slope alone. Actual sample/rights open.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Document exact units, maturity, release and decomposition convention. Do not interpret coefficients as causal effects or real-time forecasts. Keep model comparison conditional on verified coverage.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
