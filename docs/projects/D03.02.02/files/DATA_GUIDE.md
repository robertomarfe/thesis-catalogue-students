# Data and model setup | D03.02.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
FF3 daily market total returns from https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html, 1963-2025 or common coverage; r=log(1+R). Build nonoverlapping five-trading-day sums RV_w=sum r_d^2; log(RV_w+epsilon), epsilon fixed from training scale. Estimate AR(1), ARFIMA(0,d,0) via exact/approx Gaussian likelihood or local Whittle plus finite truncated filter, HAR weekly 1/4/13 lags; GARCH(1,1) on daily returns as a fourth benchmark. Chronological train through 1999, validation 2000-2009, test 2010-2025. Forecast next 1 and 4 weeks; use training residual smearing or simulated variance forecasts.

## Files to obtain locally
- **FF3D — US FF3 daily** (Core). Expected file: `F-F_Research_Data_Factors_daily_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Link status from v13 inventory: Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

Direct paths are inherited from the frozen acquisition inventory, not a guarantee that current bytes or licenses have been verified. If a path fails, use the official page and select the exact dataset/frequency. Optional sources are not required. Use the provider documentation and the return conventions, publication timing and rights checks in this guide.

## Construction and timing
Use consecutive five-session blocks; discard incomplete blocks rather than glue missing sessions. Fixed epsilon for log RV from training. Estimate local Whittle at m=floor(n^.5), n^.6 and n^.7 (subject to m<n/2); fit finite inverse fractional filter with 50/100/200 lags and recursive predictions. Compare AR(1) and weekly HAR(1,4,13); backtransform using training smearing by horizon, never exp(mean log) alone. Construct 500 matched-length, variance-normalized short-memory break and ARFIMA cases, seed 2027.

## Acceptance and first meeting
Inverse and forward fractional weight convolutions reproduce identity. Local Whittle on a seeded simulated d=.3 sample has a finite interior estimate; do not claim unbiasedness from one draw. Verify d=0 forecasts equal historical log mean.

Build a local inventory, inspect each actual schema and license, save an input ledger, row counts and actual dates. Validate session calendar, coverage, duplicate keys and missingness before merging; do not compress gaps. Provide joint sample and training/validation/evaluation counts, mature-label counts for forecasts and state/event counts for conditional estimates. No real inputs bundled or verified. If a required source fails, seek supervisor-approved adjustment preserving the research question or retain the gate. Do not silently replace data or assert a real-time backtest from revised values.

## Timing and units

Freeze the provider vintage and documented availability of each predictor. Define formation time, return interval, target end and label availability separately. Use common dates for model comparisons; never encode a missing session as a zero return. A revised historical extract supports pseudo-real-time evaluation only unless actual historical vintages are verified.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
