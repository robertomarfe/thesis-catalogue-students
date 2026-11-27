# Data and model setup | D02.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract
Cboe daily closing VIX9D, VIX, VIX3M and VIX6M when downloadable; https://www.cboe.com/tradable_products/vix/vix_historical_data and FRED VIXCLS/VXVCLS https://fred.stlouisfed.org/series/VXVCLS. Proposed 2014-2025 common dates, subject to file check. Use same close date, no forward fill over holidays, fixed horizon days 9,30,90,180 for approximate calculations; check actual index methodologies. Estimate PCA on first 60% of dates, freeze means/loadings, evaluate remaining 40% and separate rolling 3-year windows.

## Operational specification
Align VIX9D, VIX, VXVCLS and optional verified VIX6M on common actual session dates. Use squared decimal index values; no forward fill. Fit on first 60% of eligible changes and hold fixed in 40% test. Compare one/two PCs with fixed level/slope contrasts; 3 PCs only when >=4 maturities. Rolling 3-year stability is descriptive.

No empirical observations are bundled. Actual data rights, sample and schema are unverified; complete the acquisition gate before empirical work.

## Acceptance checks
At least three actual licensed maturity series; fourth needed for nontrivial 3-factor compression; train-only loadings and gap-safe changes.

## Local source acquisition (no provider data supplied)

- VIX: [FRED VIXCLS](https://fred.stlouisfed.org/series/VIXCLS); use Download > CSV and keep filename `VIXCLS.csv`. `observation_date` (YYYY-MM-DD), `VIXCLS` in annualized volatility percentage points. The direct FRED graph CSV endpoint is `https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS` (not fetched in this release).
- VIX3M: [FRED VXVCLS](https://fred.stlouisfed.org/series/VXVCLS); Download > CSV, `VXVCLS.csv`, same date format, column `VXVCLS`. Candidate direct endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=VXVCLS` (not fetched).
- Check source terms: both FRED series are Cboe copyrighted, citation required; public access does not imply permission to redistribute. Record download date, vintage, rights, raw hashes and units. Never put restricted data in a distributable ZIP. Use the documented methodology for each series and record launch versus retrospective history. If actual column names differ, inspect before configuring the reader.
- Keep missing observations missing. Use the actual market trading sessions for the sample (audited from an official calendar or validated complete daily market panel); do not use generic weekdays as the empirical calendar. Document holidays and missing sessions, date alignment and sample losses. No forward-fill. Read the date and value columns, divide annualized index percentage points by 100 and compute variance by squaring. For every file report row count, duplicate keys (reject), range, missing values, nonpositive quotes (reject) and coverage. A single clean schema fixture is not real-file validation.
- 9-day index: [Cboe official history page](https://www.cboe.com/tradable_products/vix/vix_historical_data), use linked VIX9D historical data. The listed link is `https://cdn-api.cboe.com/api/global/us_indices/daily_prices/VIX9D_History.csv`; browser fetch failed (cache miss); file schema not certified. Save `VIX9D_History.csv`; inspect actual date and closing columns, specify formats explicitly. Verify rights.
- Six-month series VIX6M is optional for a four-dimensional exercise; check current provider methodology and locate official download or licensed local file. A direct link has not been verified in this turn. Do not label an unverified URL as an actual file. Three series are the minimum; four required for nontrivial three-PC compression.
- Target 2014–2025 common dates if coverage permits. Calculate consecutive daily variance changes using the audited session index, after aligning all series to audited sessions; missing days exclude both affected changes. Freeze first 60% of usable dates, train-only centering/loadings; apply to final 40%. Keep index horizons and sample fixed. Record negative forward-variance diagnostics, gaps, initial/held-out dates and common observations.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
