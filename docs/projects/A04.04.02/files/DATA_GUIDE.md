# Data and model setup | A04.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly US market total return and RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; fitted GSW zero curve https://www.federalreserve.gov/data/nominal-yield-curve.htm; weekly STLFSI4 https://fred.stlouisfed.org/series/STLFSI4 and NFCI https://fred.stlouisfed.org/series/NFCI. Target 1994-2025, exact common months. Use last available prior-month stress observation with conservative release lag; revised data imply pseudo-real-time exercise. Build 2/5/10y rolling synthetic zero returns, monthly equity returns, inflation robustness optional.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **NFCI — NFCI** (Robustness). Expected file: `NFCI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=NFCI); [provider page](https://fred.stlouisfed.org/series/NFCI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Weekly; release lag and vintage.
- **STLFSI4 — St. Louis Fed Financial Stress Index, version 4** (Core). Expected file: `STLFSI4.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=STLFSI4); [provider page](https://fred.stlouisfed.org/series/STLFSI4). Historical v13 inventory note (unverified in current release): Series metadata verified; standard FRED CSV endpoint, bytes pending. Weekly ending Friday from December 1993. Use available lagged observation; revisions and index components constrain real-time/causal claims. Cite source; verify rights.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct stock total returns and 5y synthetic zero one-month holding returns (2/10y robustness) from GSW; exact remaining maturity and dates, convert log bond return with expm1 before variance comparison. Decision month t: choose latest stress observation from prior month or earlier, actual release strictly before origin and max age declared. STLFSI4 weekly ending Friday; series revised, do not assign observation as release. If only revised histories, conservative lag and pseudo-real-time; NFCI robustness. Pair next-month returns with lagged stress state; fixed >0 baseline, threshold quantile estimated training-only. Use rolling 36/60 month correlation and vol/cov; common-date moving blocks with regime assignment preserved/recomputed as appropriate. Compare 60/40 variance to independence counterfactual using within-state variances, disclose event counts; no causal stress interpretation.

## Acceptance and first meeting
Actual GSW, FF3M, STLFSI4 and release/vintage coverage/rights required; verify stress lags, date matching and at least adequate observations per regime. NFCI optional robustness.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Monthly US market total return and RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; fitted GSW zero curve https://www.federalreserve.gov/data/nominal-yield-curve.htm; weekly STLFSI4 https://fred.stlouisfed.org/series/STLFSI4 and NFCI https://fred.stlouisfed.org/series/NFCI. Target 1994-2025, exact common months. Use last available prior-month stress observation with conservative release lag; revised data imply pseudo-real-time exercise. Build 2/5/10y rolling synthetic zero returns, monthly equity returns, inflation robustness optional.

## Design-specific acceptance

Use a release ledger or explicitly pseudo-real-time extra lag; set threshold from fixed rule or past data. Compute exact aging bond return and nominal equity total return; report regime counts, marginal variances, covariance and 2*w_s*w_b*cov contribution with date-block inference and fixed-weight risk decomposition.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
