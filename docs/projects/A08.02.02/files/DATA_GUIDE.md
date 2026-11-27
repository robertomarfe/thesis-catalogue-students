# Data and model setup | A08.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French 10 industry monthly total returns and FF3 RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Common 1963-2025, train/rolling 120 months; validation 1985-1999, test 2000-2025; choose delta among 0,1,2,4 using validation certainty equivalent at fixed gamma=5, monthly mean and covariance (gamma applied to monthly utility). Equal weights and constrained GMV, plug-in MV, robust MV use same estimated shrinkage or sample covariance across methods. Also simulate 10-asset returns with known moments (seed 2027, 500 repetitions) and mean perturbations aligned with U.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use uncertainty U=Sigma/n_eff (iid baseline), delta=0,1,2,4; gamma=5, optional cap .25. Compare support function and worst perturbation, delta=0 must equal MV. 500 simulations seed 2027 with 10 assets, perturbations aligned with U, separate actual true utility from worst-case objective. Rolling 120-month, choose delta on 1985-99 validation net CE, then lock through 2000-25 test. Same covariance estimate, cost and asset set; U diagonal and alternative n_eff sensitivity. Report infeasible/failed optimizers.

## Acceptance and first meeting
FF10M and FF3M common sample rights; support-function equality and KKT; ambiguity radius not a serial-dependence confidence region.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French 10 industry monthly total returns and FF3 RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Common 1963-2025, train/rolling 120 months; validation 1985-1999, test 2000-2025; choose delta among 0,1,2,4 using validation certainty equivalent at fixed gamma=5, monthly mean and covariance (gamma applied to monthly utility). Equal weights and constrained GMV, plug-in MV, robust MV use same estimated shrinkage or sample covariance across methods. Also simulate 10-asset returns with known moments (seed 2027, 500 repetitions) and mean perturbations aligned with U.

## Design-specific acceptance

Verify support function with explicit worst-case mean vector; radius zero nests plug-in and compare two-asset grid with KKT. Freeze radius menu, window and caps before final sample, report binding constraints, paired OOS net CE and costs with failed windows. If interpreting statistical coverage, justify dependence adjustment separately.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
