# Data and model setup | A09.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
AQR Value and Momentum Everywhere: Original Paper Data https://www.aqr.com/insights/datasets/value-and-momentum-everywhere-original-paper-data . Provider lists Jan 1972-Jul 2011 and eight markets/classes; identify factor sheets and verify currency, units, actual start dates for equity regions, government bonds, currencies and commodities. Do not fill missing early observations. Freeze the largest common panel (at least three distinct asset classes with both styles); target minimum 120 months. Use original vintage; split by first 60% of common dates for training and rest for test, fixed before inspecting results.

## Inputs
- **VME — Value and Momentum Everywhere: Original Paper Data** (Core / planned robustness). Expected file: `Original provider workbook (filename to verify)`. [Download or provider route](https://www.aqr.com/insights/datasets/value-and-momentum-everywhere-original-paper-data); [provider page](https://www.aqr.com/insights/datasets/value-and-momentum-everywhere-original-paper-data). Historical v13 inventory note (unverified in current release): Exact dataset page; direct file URL unresolved. Select named dataset download and retain original file; verify usage terms, no arbitrary substitution.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use original VME workbook native vintage 1972–2011, at least three classes with both styles, minimum 120 common months. Freeze first 60% train, estimate standardization and PCA on train only; keep same columns/scale for held-out reconstruction. Compare equal-weight sleeves, training-only risk scaling and leave-one-class-out style composites. Do not fill incomplete start dates or conflate class and region.

## Acceptance and first meeting
Verify workbook sheet, return units, class labels and actual common panel; terms and source bytes pending. Toy PCA and variance identities passed.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Inspect workbook tabs and exact periods; preserve common dates and no imputation. Fit all scales/loadings on training. Report sleeves, overlap, risk normalization and holdout uncertainty.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
