# Data and model setup | A11.04.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Shiller monthly price, annualized dividends and CPI from https://shillerdata.com/ or https://www.econ.yale.edu/~shiller/data.htm; use annual December observations (annual dividend flow approximation; document interpolation), real prices/dividends, target 1926-2025. Estimate deterministic real growth trend on fixed early period or use common deterministic scale; discount scenarios r=4,6,8% with consistent growth adjustment. H=10/20/30y; same origin sample for comparisons. Alternative full-sample backward recursion with terminal price and fixed terminal dividend multiple.

## Inputs
- **SHILLER — US stock market price, dividend, earnings, CPI** (Core). Expected file: `ie_data.xls`. [Download or provider route](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/249997aa-1eef-4237-93ec-2d319f7881ab/ie_data.xls?ver=1794837439406); [provider page](https://shillerdata.com/). Historical v13 inventory note (unverified in current release): Exact link displayed on new author website; click returned unsupported Excel content type, no binary validated. Use annual trailing dividend totals; check current file/link. Previous candidate https://www.econ.yale.edu/~shiller/data/ie_data.xls retained here for provenance; price monthly average, annualized dividend totals interpolated, CPI. Recheck link/version at acquisition.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Acquire Shiller workbook, identify year/month robustly (avoid ambiguous numeric October), take December annual levels P and trailing four-quarter D, deflate same CPI; no sum of twelve annual D entries. Target 1926–2025; scale P and D consistently by fixed early deterministic growth trend and adjust discount (1+r)/(1+g)-1 if detrended. For H=10/20/30 compare same origin dates; future price exact under null, fixed terminal dividend multiple alternate; discount 4/6/8%. Validate projection on artificial constant-discount dividend model; block/simulation null inference with overlapping horizons and terminal value. Future price is not a predictor.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; actual December sequence and trailing dividend convention, price averaged not close; prove stationarity/scaling assumptions or interpret as descriptive.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use identical origin dates for horizon comparisons, report terminal contributions and fixed discount/growth assumptions. Future prices enter only the ex post benchmark. Document stationarity limitations, overlapping horizons and sampling sensitivity; do not confuse this exercise with news decomposition.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
