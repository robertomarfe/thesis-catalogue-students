# Data and model setup | D02.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract
Daily closing VIXCLS and VXVCLS at https://fred.stlouisfed.org/series/VIXCLS and https://fred.stlouisfed.org/series/VXVCLS ; Cboe methodology https://www.cboe.com/tradable-products/vix/vix-historical-data/ . Use month-end joint observations with targets over following 30 and 90 calendar days; aggregate French daily Mkt-RF+RF as an explicitly different broad-market return proxy https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . SP500 FRED close is optional matched-index robustness on its available limited history. Baseline common start 2008 if coverage allows, end 2025; pre-2016 train, thereafter expanding forecasts with complete target horizons, no forward fills across dates.

## Operational specification
At last common month-end observation, compute 30/90-day squared-return proxies using verified sessions, retain negative forward variance diagnostics. Start training before 2016 if data allow; each forecast uses only targets matured by its origin. Compare positive forecasts using QLIKE/MSE and overlapping-label HAC/block inference.

No empirical observations are bundled. Actual data rights, sample and schema are unverified; complete the acquisition gate before empirical work.

## Acceptance checks
Rights and actual source checks pending; calendar horizon and maturity-aware training, broad-market proxy explicitly not SPX.

## Local source acquisition (no provider data supplied)

- VIX: [FRED VIXCLS](https://fred.stlouisfed.org/series/VIXCLS); use Download > CSV and keep filename `VIXCLS.csv`. `observation_date` (YYYY-MM-DD), `VIXCLS` in annualized volatility percentage points. The direct FRED graph CSV endpoint is `https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS` (not fetched in this release).
- VIX3M: [FRED VXVCLS](https://fred.stlouisfed.org/series/VXVCLS); Download > CSV, `VXVCLS.csv`, same date format, column `VXVCLS`. Candidate direct endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=VXVCLS` (not fetched).
- Check source terms: both FRED series are Cboe copyrighted, citation required; public access does not imply permission to redistribute. Record download date, vintage, rights, raw hashes and units. Never put restricted data in a distributable ZIP. Use the documented methodology for each series and record launch versus retrospective history. If actual column names differ, inspect before configuring the reader.
- Keep missing observations missing. Use the actual market trading sessions for the sample (audited from an official calendar or validated complete daily market panel); do not use generic weekdays as the empirical calendar. Document holidays and missing sessions, date alignment and sample losses. No forward-fill. Read the date and value columns, divide annualized index percentage points by 100 and compute variance by squaring. For every file report row count, duplicate keys (reject), range, missing values, nonpositive quotes (reject) and coverage. A single clean schema fixture is not real-file validation.
- Market proxy: [French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), Fama/French 3 Factors [Daily ZIP](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip). Keep the daily main block; convert percentage values to decimal and form total market return as Mkt-RF+RF. This is a broad-market proxy, not SPX; record CRSP vintage. Optional matched-index SP500 via FRED only after rights/coverage checks.
- Choose the last common valid observation of each calendar month (retain its date). Do not use future endpoints; the target for t is fully observable only at t+h, even if last session was earlier. Construct 30- or 90-calendar-day targets; restrict estimation to targets matured at each forecast origin. For target intervals missing any verified trading session, mark missing. Check common sample 2008–2025 and initial training before 2016; revise scope with supervisor if coverage fails.
- Minimum: two aligned indices and complete return calendar; both 30/90-day proxy targets and maturity timestamps; historical, level and level-plus-slope comparisons on same held-out origins. Require initial training sample and a viable test span before assigning. Positivity floor fitted on training only.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
