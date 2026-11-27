# Data and model setup | A05.03.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

Status: source/conventions verified; local acquisition and 1972–2025 coverage not validated. Source-level reader, common-date curve and calendar-aged return tests on synthetic input pass. No estimates of forward factor or predictability. Existing proposal: `02_proposals/individual_md/A05.03.02.md`.

## Core input
Only baseline source: Federal Reserve Board `feds200628.csv`, [direct download](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv), [landing page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Required fields `Date`, `SVENY01`…`SVENY05`; no par yield, constant maturity coupon series or separate T-bill needed for the log one-year excess-return definition. Research fitted off-the-run Treasury data, revised vintage, not OIS nor observed tradable zeros. Board disclaimer permits public-domain Board material unless otherwise indicated; cite Board and GSW; retain original, check specific notice and log hash/date. No other source mandatory for baseline.

Install shared dependencies, run `python src/local_preflight.py /path/to/feds200628.csv > GSW_validation.json`. Review five maturity series daily missingness and observed dates; validate source preamble and percent units. Use `gsw(path)` to obtain decimal continuously compounded yields and `monthly_common_curve(daily)` for last common valid date of each calendar month. Flag month-end lags >7 calendar days (provisional rule); inspect causes and exclude or revise the date rule before model fitting. Log actual observation date, never create a vector by merging different maturity dates. Missing months remain missing, not interpolation. Use data from 1972–2025; include earlier history only if separately declared. End-of-2025 is last permitted realization date. If there are fewer than 240 valid monthly training origins or 180 test origins with all four fully matured returns, revisit the sample design before inspecting outcomes. These minimum counts are proposed pilot gates, not original empirical results.

## Construction and timing
For each n=1,...,5, p_t(n)=-n*y_t(n), p_t(0)=0 and one-year forward f_t(n)=p_t(n-1)-p_t(n). For n=2,...,5, rx_(t+12)(n)=p_(t+12)(n-1)-p_t(n)-y_t(1). Use `forward_and_aged_returns(monthly)`; it preserves origin PeriodIndex and realization_month, and uses exact calendar t+12 rather than row offset. Actual endpoint dates approximate one year; report irregular date/day-count variation. Verify flat-curve zero excess and manual price ratio for one real date once file obtained. Do not use change in yield as holding return or subtract a long-maturity yield as risk-free. Keep log annual excess units consistently.

Frozen design: training origins from 1972, labels must be realized by end-Dec 1999. Origins Jan–Dec 1999 whose labels mature in 2000 must be excluded (Dec 1998 maturity Dec 1999 is eligible). Test origins start Jan 2000, last eligible Dec 2024 when realization is Dec 2025 (calendar matching and actual common sample may shorten). Any expanding model can only use labels matured by the exact evaluation date under a documented end-of-month information convention. Historical mean, slope, PC, ridge and forward factor must use equal information sets. Compare four maturities jointly with fixed common sample; overlap-aware HAC and blocks. Revised source is pseudo-real-time, no claim that historic vintages were known. Main factor fit, weights, predictive regressions, OOS results and inference are student tasks.

## Week 1–2 gate
Produce original-file hash, validation JSON, daily and monthly coverage table by maturity, dated missing month/long-lag exclusions, manual forward/aged return check, sample count with purged training and matured test labels. Supervisor reviews prior to forecast fitting. If source/sample fails, adjust only through explicit recorded approval; no proxy par yields or invented missing returns. The alternative FRED constant-maturity series do not provide the same fitted zero-return construction, so cannot silently replace GSW.


The v18 preflight reports coverage, last valid common dates and training/test count; it does not fit an empirical model. Any gaps or flagged long lags require review before assignment.

## Design-specific acceptance

Do not infer a structural factor from a good in-sample fit. Report fixed and expanding results separately, with actual eligible label counts and stability intervals.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
