# Data and model setup | A08.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French FF3M total market Mkt-RF+RF, GSW fitted nominal zero curve https://www.federalreserve.gov/data/nominal-yield-curve.htm. Construct synthetic monthly holding returns on 5Y zero from P_(t+1)(5-1/12)/P_t(5), using documented Svensson curve at both horizons; not actual bond fund returns. Proposed common sample 1970-2025; use 120-month initial window, rolling 36/60 months and EWMA half-life selected on chronological validation only. All rules rebalance monthly; test final 15 years if enough dates. GSW publication availability lag may require one-month lag; revised data pseudo-real-time. Costs 0,10,25 bp per unit one-way turnover.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Construct synthetic monthly 5-year zero holding returns from GSW Svensson yields at n and exact n-1/12 (annual continuous decimal), market total Mkt-RF+RF. Use actual end-month curve observations and lag GSW predictors when needed; pseudo-real-time caveat. Fixed 60/40, expanding GMV, rolling 36/60 or EWMA half-life selected in chronology after initial 120 months, freeze final 15 years if feasible. Original THEORY uses half-L1 turnover while DESIGN says per one-way turnover: explicitly use scale=.5 for baseline and report equivalent full-L1 cost (half rate) to avoid ambiguous cost comparison. No lookahead, no actual fund claim. Fixed comparator rebalanced, not buy-and-hold.

## Acceptance and first meeting
Actual GSW/FF3M and residual maturity, common dates and publication timing; analytic two-asset weight and drift ledger.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French FF3M total market Mkt-RF+RF, GSW fitted nominal zero curve https://www.federalreserve.gov/data/nominal-yield-curve.htm. Construct synthetic monthly holding returns on 5Y zero from P_(t+1)(5-1/12)/P_t(5), using documented Svensson curve at both horizons; not actual bond fund returns. Proposed common sample 1970-2025; use 120-month initial window, rolling 36/60 months and EWMA half-life selected on chronological validation only. All rules rebalance monthly; test final 15 years if enough dates. GSW publication availability lag may require one-month lag; revised data pseudo-real-time. Costs 0,10,25 bp per unit one-way turnover.

## Design-specific acceptance

Hand-check P_(t+1)(5-1/12)/P_t(5) and common monthly market total return. Verify EWMA versus direct weighted covariance, lag estimates and training-only tuning. Compare same capital/constraints/costs and out-of-sample periods, net performance with paired block inference.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
