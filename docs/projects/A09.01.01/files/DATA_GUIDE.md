# Data and model setup | A09.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
French Data Library https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html ; provider conventions https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library/f-f_developed.html . Monthly USD total returns on regional 25 Size-B/M portfolios (or six if insufficient), global Developed FF3 and North American, European, Japanese FF3. Confirm exact portfolio files and common USD RF; no FX conversion. Target Jul 1990-Dec 2025 common sample, value-weighted returns. Use regional portfolios formed on size/profitability if available as alternative assets less mechanically linked to HML/SMB. No claim of independence when factors share constituents.

## Inputs
- **FFDEV — Developed FF3** (Core / planned robustness). Expected file: `Developed_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Developed_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFNA — North America FF3** (Core / planned robustness). Expected file: `North_America_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/North_America_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFEU — Europe FF3** (Core / planned robustness). Expected file: `Europe_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Europe_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFJP — Japan FF3** (Core / planned robustness). Expected file: `Japan_3_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Japan_3_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFNA25 — North_America 25 size/BM portfolios** (Core / planned robustness). Expected file: `North_America_25_Portfolios_ME_BE-ME_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/North_America_25_Portfolios_ME_BE-ME_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFEU25 — Europe 25 size/BM portfolios** (Core / planned robustness). Expected file: `Europe_25_Portfolios_ME_BE-ME_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Europe_25_Portfolios_ME_BE-ME_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FFJP25 — Japan 25 size/BM portfolios** (Core / planned robustness). Expected file: `Japan_25_Portfolios_ME_BE-ME_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Japan_25_Portfolios_ME_BE-ME_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use the value-weight monthly USD portfolio blocks and region/global FF3 on one common contiguous set of dates. Convert percentages once; subtract one verified common USD RF from test asset total returns. Compare three-factor global/local models per region using classical GRS only as iid benchmark; use paired date blocks for alpha differences and HAC for individual alphas. Inspect condition numbers in joint global/local fit; never infer segmentation from R2. Freeze the split before results.

## Acceptance and first meeting
Obtain at least two eligible regional panels and verify actual USD RF equality, factor labels, value-weight block, no missing sentinels, T>N+K for GRS. Artificial nested-model diagnostic only; empirical rights and common sample pending.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Audit identical USD units and RF, dates, portfolio definition and factor count. Report N, T, K, covariance conditioning and paired uncertainty. Separate factor-construction overlap from the economic interpretation.

## Timing, accounting and units

Fix currency quote orientation, base currency, return units, settlement dates, funding convention, measure and annualization. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For simulations distinguish expiry from delivery and quote rate from payoff currency.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
