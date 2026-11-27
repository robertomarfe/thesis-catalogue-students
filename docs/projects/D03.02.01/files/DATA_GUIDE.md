# Data and model setup | D03.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use daily Fama/French market excess return and RF, https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html; add RF in simple-return units before logs. Target 1990-2025. Freeze 1990-2004 training, 2005-2009 validation and 2010-2025 final evaluation if coverage supports them; otherwise report a common chronological alternative. Expand estimates at fixed monthly dates using labels fully observed at the forecast origin. Compare h=1,5,22 and overlapping targets with horizon-aware inference.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Build X=(means of trailing 1,5,22 squared returns) and next h-session sum as target, h=1,5,22. Use each h-specific training set with label end <= origin, fixed validation and test dates, positive floor learned from training, common masks versus GARCH and historical forecasts. Re-estimate monthly; between refits recompute features without updating coefficients. Preserve actual sessions and do not compress missing days.

## Acceptance and first meeting
Hand-check feature and target alignment. Replace every immature label with a huge number: the forecast must be unchanged. Score only common realized labels.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
