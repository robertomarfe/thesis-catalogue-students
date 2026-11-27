# Data and model setup | A06.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Shiller monthly aggregate price, annual dividend and CPI series https://www.econ.yale.edu/~shiller/data.htm. Baseline year-end rows 1950-2025 if complete; dividends are trailing annual aggregates interpolated monthly, not monthly payouts. Convert P and D by same CPI for real P/D and derive annual real dividend growth from annual dividend series, not repeated monthly interpolations. Use observed 10th/50th/90th P/D percentiles and historical real growth estimates over prespecified sample and 20-year windows. Annual real k/g scenarios, no market expectation claim.

## Inputs
- **SHILLER — US stock market price, dividend, earnings, CPI** (Core / planned robustness). Expected file: `ie_data.xls`. [Download or provider route](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/249997aa-1eef-4237-93ec-2d319f7881ab/ie_data.xls?ver=1794837439406); [provider page](https://shillerdata.com/). Historical v13 inventory note (unverified in current release): Exact link displayed on new author website; click returned unsupported Excel content type, no binary validated. Use annual trailing dividend totals; check current file/link. Previous candidate https://www.econ.yale.edu/~shiller/data/ie_data.xls retained here for provenance; price monthly average, annualized dividend totals interpolated, CPI. Recheck link/version at acquisition.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Normalize Shiller workbook P,D,CPI using December rows; parse numeric YYYY.MM including .10 as October, maintain missing years. D annual trailing interpolated, P monthly average; use real D and same CPI for P/D. Historical growth scenarios are not survey expectations. DDM uses simple annual growth and required return, k>g; two-stage terminal share and implied k=g+(1+g)/(P/D). Use rolling 20-year contiguous growth, alternative windows and annual payout caveats.

## Acceptance and first meeting
Actual Shiller workbook and rights, December coverage/definition must pass. Test date parser, constant-growth limit and terminal share.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Shiller monthly aggregate price, annual dividend and CPI series https://www.econ.yale.edu/~shiller/data.htm. Baseline year-end rows 1950-2025 if complete; dividends are trailing annual aggregates interpolated monthly, not monthly payouts. Convert P and D by same CPI for real P/D and derive annual real dividend growth from annual dividend series, not repeated monthly interpolations. Use observed 10th/50th/90th P/D percentiles and historical real growth estimates over prespecified sample and 20-year windows. Annual real k/g scenarios, no market expectation claim.

## Design-specific acceptance

Manually verify December dates and units; report missing years and log-to-simple growth conversion, iso-P/D contours and required-return/growth pairs. Compare one- and two-stage prices with identical growth limit and terminal share; show sensitivity to horizon and a small joint parameter perturbation. Do not use historical growth as investor forecast without a model.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
