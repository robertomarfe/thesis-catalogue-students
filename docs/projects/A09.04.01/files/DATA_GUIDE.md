# Data and model setup | A09.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
AQR Time Series Momentum: Factors, Monthly https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Factors-Monthly (four asset-class series, documented start 1985); French US monthly FF3 market/RF for comparison. Target 1985-2025 common period. Use published excess factor returns in documented units; do not claim independently replicating futures positions. Fixed equal-weight across four factor sleeves and published aggregate if supplied; compare with rolling inverse-volatility sleeve allocation, 60-month window, leverage convention stated. Crisis definition: lowest training-sample quintile of market returns, evaluated on 2005-2025 holdout; also retrospective 2008/2020 event windows.

## Inputs
- **FF3M — US FF3 monthly** (Core). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **TSMOM — Time Series Momentum: Factors, Monthly** (Core). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Factors-Monthly); [provider page](https://www.aqr.com/Insights/Datasets/Time-Series-Momentum-Factors-Monthly). Historical v13 inventory note (unverified in current release): Exact dataset page; direct file URL unresolved. Select named monthly factor dataset, four asset-class sleeves, starts January 1985 per provider. Verify terms and exact filename.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use AQR monthly four sleeves (Jan 1985 onward), documented excess returns, plus US FF3. Fixed equal-weight vs 60-month trailing inverse-vol weights capped at .5 (proposed; keep total notional 1). Freeze bottom-market-quintile threshold on pre-2005 training; evaluate 2005–2025 and retrospective crisis windows. Report additive excess payoff unless collateral/funding specified; no investable track-record claim.

## Acceptance and first meeting
Four documented sleeves, common monthly grid, permitted use and exact units pending; synthetic past-only weights and variance tests passed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Verify four sleeves, monthly units, risk scaling and market benchmark. Use only trailing data in weights and training thresholds, with fixed holdout. No independent futures-position replication claim.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
