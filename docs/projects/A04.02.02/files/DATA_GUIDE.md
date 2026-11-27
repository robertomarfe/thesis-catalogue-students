# Data and model setup | A04.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW fitted nominal curve https://www.federalreserve.gov/data/nominal-yield-curve.htm; end-of-month observed parameters or interpolate log discounts for fractional maturities (4+11/12,9+11/12). FF3 monthly market total from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; CPIAUCSL https://fred.stlouisfed.org/series/CPIAUCSL; common 1971-2025 or coverage. Compound equity gross returns; monthly-average CPI is a proxy for end-month price level. Estimate expanding AR(1) monthly inflation from 1960 with one-month information lag; aggregate forecast recursively for 12 months.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **CPIAUCSL — CPIAUCSL** (Core). Expected file: `CPIAUCSL.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL); [provider page](https://fred.stlouisfed.org/series/CPIAUCSL). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly SA CPI; quarterly average; annualization match.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
GSW fitted nominal log discount curves at actual month-end observation dates; interpolate log discounts at n-h without extrapolation (5y/10y baseline; n-h exact). Return from buying n-year zero at t and holding 1 or 12 months, not n-year rolling index over h. Equity compound actual total returns; use monthly-average CPI ratio as end-month proxy. Fit expanding AR(1) to released monthly log inflation, one-month lag: if last observed t-1, forecast h+1 steps, discard forecast for t, sum steps t+1..t+h; if actual lag differs use exact mapping. Use same realized and modeled-surprise inflation regressors for nominal and real log returns; coefficient difference exactly one for realized inflation with same sample/intercept. Use common periods, overlap HAC/block, fixed subperiods, 60/40 simple returns with fixed rebalancing convention.

## Acceptance and first meeting
Actual GSW, FF3M, CPI permissions and common sample; verify annual decimal zero yields, maturity interpolation and one-month CPI release lag. No inference from yield changes treated as bond returns.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

GSW fitted nominal curve https://www.federalreserve.gov/data/nominal-yield-curve.htm; end-of-month observed parameters or interpolate log discounts for fractional maturities (4+11/12,9+11/12). FF3 monthly market total from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; CPIAUCSL https://fred.stlouisfed.org/series/CPIAUCSL; common 1971-2025 or coverage. Compound equity gross returns; monthly-average CPI is a proxy for end-month price level. Estimate expanding AR(1) monthly inflation from 1960 with one-month information lag; aggregate forecast recursively for 12 months.

## Design-specific acceptance

Compute both bond prices for n and n-h using the same documented GSW Svensson convention; verify flat-curve log holding return h*y. Compound monthly gross legs and deflate with exact adjacent CPI; fit inflation AR only on available history, use overlapping-horizon HAC or nonoverlap sensitivity and paired date blocks. Label retrospective hedge exposure, not expected return.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
