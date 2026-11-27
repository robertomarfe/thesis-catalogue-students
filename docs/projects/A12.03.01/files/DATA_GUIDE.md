# Data and model setup | A12.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French Data Library https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html ; exact monthly ST Rev, Mom, LT Rev and FF3, optional 10 portfolios formed on each sorting signal; definitions https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_st_rev_factor.html and https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_lt_rev_factor.html . Value-weighted, US, percentage returns; common Jan 1931-Dec 2025 if file supports, split pre/post 1990 fixed before analysis. Download raw factor and portfolio descriptions; compare matched samples and note annual/monthly reconstitution differences. Do not reconstruct individual stock histories from factor spreads.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFMOM — US momentum monthly** (Core / planned robustness). Expected file: `F-F_Momentum_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFST — US short-term reversal monthly** (Core / planned robustness). Expected file: `F-F_ST_Reversal_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_ST_Reversal_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFLT — US long-term reversal monthly** (Core / planned robustness). Expected file: `F-F_LT_Reversal_Factor_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_LT_Reversal_Factor_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
French US monthly ST_Rev low-minus-high formation t-1, Mom high-minus-low t-12..t-2, LT_Rev low-minus-high t-60..t-13; portfolios formed monthly, holding one month. Align all to exact common Jan 1931-Dec 2025 if supported and FF3. Keep published profitable orientation primary; for continuation comparison explicitly negate reversal factors. CAPM/FF3 HAC on same dates; paired differences using direct regressions of difference rather than independent SE. Fixed pre/post-1990, optional recession dates and decile profiles after verifying sort and weights; no RF subtraction from factors or turnover inference.

## Acceptance and first meeting
Actual FFST/FFMOM/FFLT/FF3M files, date/units, orientation and construction; common sample and paired identity.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

French Data Library https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html ; exact monthly ST Rev, Mom, LT Rev and FF3, optional 10 portfolios formed on each sorting signal; definitions https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_st_rev_factor.html and https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_lt_rev_factor.html . Value-weighted, US, percentage returns; common Jan 1931-Dec 2025 if file supports, split pre/post 1990 fixed before analysis. Download raw factor and portfolio descriptions; compare matched samples and note annual/monthly reconstitution differences. Do not reconstruct individual stock histories from factor spreads.

## Design-specific acceptance

Verify ST, Mom and LT definitions and exact units; align common dates and test the paired return/alpha difference directly with HAC/blocks. Freeze pre/post-1990 dates and report dependent returns; do not claim individual-level trading evidence or use future selection.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish funded wealth from zero-investment spreads, gross from net performance, allocation-time moments from realized risk, and actual turnover from hypothetical trading costs.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
