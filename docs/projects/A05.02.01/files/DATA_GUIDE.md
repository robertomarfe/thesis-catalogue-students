# Data and model setup | A05.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Fed GSW daily nominal continuous zero yields SVENY01,...,SVENY10, plus 15/20 if common; select last valid trading day each month and convert percent to decimal. https://www.federalreserve.gov/data/nominal-yield-curve.htm . Proposed 1985-2025 with 1985-2004 training and 2005-2025 evaluation, conditional on actual availability. Fix maturities 1-10 years and lambda=0.7308 per year as Diebold-Li style reference (0.0609 per month); alternative training-selected lambda on a small grid. GSW curves themselves are smoothed Nelson-Siegel/Svensson estimates, not raw bond yields; this matters for interpretation.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core / planned robustness). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Take last common trading observation per month for 1–10Y; fix lambda=.7308/year and estimate betas by OLS. Fit AR(1) to training factors (calendar-adjacent transitions only); forecast 1,3,12 months and no change on identical origins; alternative lambda chosen using training only. Freeze initial fit or declare expanding refit. Score in bp and use overlap-aware uncertainty.

## Acceptance and first meeting
Actual GSW dates and common sample open; require full-rank loadings, missing calendar periods not compressed; label revised-data backtest, not real-time feed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Freeze decay or select it only on training data. A negative OOS result is informative. Do not describe a fitted DNS model as automatically arbitrage-free or an implementable trading rule.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
