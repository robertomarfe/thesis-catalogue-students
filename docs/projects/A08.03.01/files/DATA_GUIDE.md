# Data and model setup | A08.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French 30 industry monthly value-weighted total returns and monthly RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; target 1990-2025, training 60 months, monthly rebalancing through 2025. Same Ledoit-Wolf or sample covariance (positive definite regularization documented) across EW, inverse vol, ERC and GMV. Long-only, fully invested, no leverage, identical fees per one-way traded dollar (0/10/25bp). Optional bond sleeve with GSW synthetic holding returns and explicit maturity roll.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Optional empirical illustration). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use 30 industry value-weighted monthly total returns, 60 months, 1990-2025 target, same positive-definite covariance across EW, inverse-vol, ERC and GMV. ERC via convex log barrier then normalize; contributions w_i(Sigma w)_i/(w'Sigma w); no leverage or cap beyond simplex. Distinguish negative contributions under other weights from impossible negative budgets in ERC. Rebalance monthly and charge scale=1 ledger; risk contributions at formation, realized variance and concentration separately. Optional GSW bond sleeve only documented aging.

## Acceptance and first meeting
Actual FF30M/RF coverage and rights; ERC residual tolerance and diagonal inverse-vol limit; compare same covariance.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French 30 industry monthly value-weighted total returns and monthly RF from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; target 1990-2025, training 60 months, monthly rebalancing through 2025. Same Ledoit-Wolf or sample covariance (positive definite regularization documented) across EW, inverse vol, ERC and GMV. Long-only, fully invested, no leverage, identical fees per one-way traded dollar (0/10/25bp). Optional bond sleeve with GSW synthetic holding returns and explicit maturity roll.

## Design-specific acceptance

Check contribution sum, positive budget and ERC residual on diagonal and correlated SPD matrices; report KKT for GMV and eigenvalues. Compare four methods with common dates/covariance, cost drift and ex-ante contributions plus held-out realized contribution estimates and uncertainty.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
