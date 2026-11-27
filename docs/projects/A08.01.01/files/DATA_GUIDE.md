# Data and model setup | A08.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French monthly 10 industry portfolios (value-weighted) https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, proposed 1963-2025 with 60/120-month rolling estimation and monthly rebalancing. Same dates and fully invested long-only constraints, gamma=3/5/10. Compare sample mean-variance, sample GMV and 1/N. Synthetic complement: N=10, fixed positive-definite covariance and heterogeneous means frozen from an early calibration window or specified scenarios, Gaussian draws with T=24/60/120/240; 1,000 replications and independent test paths. Use monthly units throughout.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core / planned robustness). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Freeze N=10 positive-definite monthly covariance and heterogeneous means before simulation; compare oracle, estimated mean only, estimated covariance only and joint estimates at T=24/60/120/240, 1,000 paired replications, independent test paths. Report true-moment utility loss (oracle minus fitted policy) and realized utility separately. In French 10-industry value-weighted panel, use total returns for wealth, excess moments for allocation and matched RF for Sharpe; common origins after 120 months, long-only, gamma=3/5/10, 60/120 histories. Use ledger with scale=1 and 0/10/25bp; disclose initial weights and first trade. Paired block uncertainty with refits where estimating model uncertainty.

## Acceptance and first meeting
Actual French monthly total-return panel and RF, common dates and permissions; analytic unconstrained and constrained KKT checks. Research 1,000 replications pending.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French monthly 10 industry portfolios (value-weighted) https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, proposed 1963-2025 with 60/120-month rolling estimation and monthly rebalancing. Same dates and fully invested long-only constraints, gamma=3/5/10. Compare sample mean-variance, sample GMV and 1/N. Synthetic complement: N=10, fixed positive-definite covariance and heterogeneous means frozen from an early calibration window or specified scenarios, Gaussian draws with T=24/60/120/240; 1,000 replications and independent test paths. Use monthly units throughout.

## Design-specific acceptance

Run paired known-moment cells: true/estimated mean crossed with true/estimated covariance, same random draws and out-of-sample returns, verify oracle objective and feasibility. For actual data record long-only weights, exact OOS dates, drifted trades, net wealth and CE units; date blocks and estimation uncertainty; report failed cells.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
