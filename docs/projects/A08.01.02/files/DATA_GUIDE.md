# Data and model setup | A08.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French monthly value-weighted 30 Industry Portfolios (total returns), optional 49 industries; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Freeze common complete asset panel 1970-2025 if supported; no full-sample asset screening by realized performance, document missing-data rules and fixed universe. Use 60- and 120-month lookbacks, first OOS date once each has history; compare on common origins from 1980 or later. At end of month t compute covariance on returns through t, set weights for t+1, long-only fully invested, rebalance monthly. Cost grid 0, 10, 25 bp per one-way dollar traded; use beginning-of-period drifted weights and charge c*sum(abs(target-drifted weights)) explicitly per absolute dollar traded.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF30M — US 30 industries monthly** (Core / planned robustness). Expected file: `30_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use value-weighted 30 industries, fixed complete asset universe justified ex ante, common first test date after 120 months. Compare sample covariance (ddof=1) and sklearn LedoitWolf (ML scaling, identity shrinkage target), note scaling difference does not affect unpenalized GMV weights. Verify positive definiteness; if sample covariance singular report and apply declared ridge sensitivity, not silent pseudoinverse. Use monthly 60/120 lookbacks, identical EW, GMV constraints, ledger scale=1; report covariance eigenvalues, condition numbers, concentration and paired realized squared-return/variance differences; full re-fit bootstrap sensitivity.

## Acceptance and first meeting
Actual FF30M/FF3M panel, RF and coverage; PSD/SPD and feasible weights; common sample. Optional 49 industries only after approval.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French monthly value-weighted 30 Industry Portfolios (total returns), optional 49 industries; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Freeze common complete asset panel 1970-2025 if supported; no full-sample asset screening by realized performance, document missing-data rules and fixed universe. Use 60- and 120-month lookbacks, first OOS date once each has history; compare on common origins from 1980 or later. At end of month t compute covariance on returns through t, set weights for t+1, long-only fully invested, rebalance monthly. Cost grid 0, 10, 25 bp per one-way dollar traded; use beginning-of-period drifted weights and charge c*sum(abs(target-drifted weights)) explicitly per absolute dollar traded.

## Design-specific acceptance

Document shrinkage target, intensity and denominator; compare eigenvalues, condition numbers, KKT, weights and predicted risk on common origins. Same costs and drift, equal weight and sample GMV; report singular windows and predefined fallback, compare paired net OOS variance/turnover and block intervals.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
