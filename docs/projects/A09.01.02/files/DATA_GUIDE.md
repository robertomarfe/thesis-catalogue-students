# Data and model setup | A09.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly USD-denominated Fama/French North America, Europe, Japan and Asia Pacific ex Japan 3-factor files plus Developed 3 Factors, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html. Add each file's RF to market excess return for total return; verify a common USD RF. Target 1991-2025 common sample. Use 60-month rolling windows and a simple equally weighted four-region portfolio rebalanced monthly versus each stand-alone region; define high volatility using past global realized volatility with thresholds estimated only in training.

## Inputs
- **FFDEV — Developed FF3** (Core / planned robustness). Expected file: `Developed_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Developed_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFNA — North America FF3** (Core / planned robustness). Expected file: `North_America_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/North_America_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFEU — Europe FF3** (Core / planned robustness). Expected file: `Europe_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Europe_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFJP — Japan FF3** (Core / planned robustness). Expected file: `Japan_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Japan_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFAP — Asia Pacific ex Japan FF3** (Core / planned robustness). Expected file: `Asia_Pacific_ex_Japan_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Asia_Pacific_ex_Japan_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Reconstruct total market returns with matched regional RFs. Four nonoverlapping regions, 60-month windows, lagged global realized-vol threshold fitted on first sample only. Show equal-weight variance and average stand-alone variance (not average vol). Use joint date blocks; rolling leave-one-out beta and standardized PCA; 36/120-month sensitivity.

## Acceptance and first meeting
Four disjoint regional market histories and common dates/RF verified before empirical work. Synthetic variance decomposition and calendar test passed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify the four disjoint constituents and common USD RF. Exclude the overlapping Developed index from portfolio holdings. Record the rolling/regime timing, variance decomposition and sample dependence.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
