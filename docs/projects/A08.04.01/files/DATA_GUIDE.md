# Data and model setup | A08.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French 10/30 industry daily total returns and RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1990-2025, 5-year trailing window, monthly rebalance, 95% daily ES baseline, 90/97.5% sensitivity; choose risk budget as training-sample equal-weight ES or fixed preregistered multiples. Daily weights drift between trades; use realized net daily returns, 0/10/25 bp turnover cost. Simulated multivariate normal and t return samples with same covariance for controlled comparison.

## Inputs
- **FF30D — US 30 industries daily** (Core). Expected file: `30_Industry_Portfolios_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/30_Industry_Portfolios_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10D — US 10 industry portfolios daily** (Core). Expected file: `10_Industry_Portfolios_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Standard French candidate path; verify direct link and bytes. Core parsimonious 10-industry universe; FF30D robustness. Confirm value-weighted total returns, units and dates.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Daily value-weighted 10 industries baseline, 30 robustness, five-year trailing window, monthly rebalance but daily drift and daily net returns. Loss=-w'r, alpha=.95 (90/97.5 robustness), fractional tail mass at boundary. Set ES budget from training EW or preregistered multiples; variance benchmark on comparable training EW variance budget, not equating ES and variance units. LP with unrestricted VaR threshold, nonnegative auxiliaries; report infeasibility and explicit equal-weight fallback. Normal and Student-t matched covariance (scale t shocks by sqrt((nu-2)/nu)). Evaluate realized net daily ES with paired date-block inference; monthly trades scale=1; report solver memory and timing (dense teaching LP; sparse extension before full large grid).

## Acceptance and first meeting
Actual FF10D, FF30D robustness and FF3D, audited complete trading calendar and units; hand LP and ES fractional-tail test. Full rolling LP runtime and inferential calibration pending.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French 10/30 industry daily total returns and RF https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Proposed 1990-2025, 5-year trailing window, monthly rebalance, 95% daily ES baseline, 90/97.5% sensitivity; choose risk budget as training-sample equal-weight ES or fixed preregistered multiples. Daily weights drift between trades; use realized net daily returns, 0/10/25 bp turnover cost. Simulated multivariate normal and t return samples with same covariance for controlled comparison.

## Design-specific acceptance

Verify empirical ES by order statistic and direct Rockafellar-Uryasev objective; compare two-asset LP to enumerated frontier. Record solver status/runtime, prespecified fallback and feasible risk budgets. Run rolling daily scenario fit with monthly trading, actual complete calendar and paired date-block ES intervals. Large grid remains student work.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
