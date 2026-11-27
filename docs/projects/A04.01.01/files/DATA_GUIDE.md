# Data and model setup | A04.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Philadelphia Fed SPF mean real GDP level/growth forecasts and release dates https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts; French monthly market/RF and Goyal dividend-price https://sites.google.com/view/agoyal145/. Use real GDP only, proposed 1992Q1-2025Q4; verify consistent level definitions and compute annualized expected growth from same-vintage current-quarter and next-quarter mean levels (ratio of mean forecasts, not mean individual growth). At survey release, use end-of-release-month origin, lag valuation ratio by one additional month as availability buffer; target following 3 months, h=12 secondary. Initial 1992-2007 training, 2008-2025 expanding test.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core / planned robustness). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.
- **SPFLEVEL — SPF mean forecast levels** (Core / planned robustness). Expected file: `meanLevel.xlsx`. [Download or provider route](https://www.philadelphiafed.org/-/media/FRBP/Assets/Surveys-And-Data/survey-of-professional-forecasters/historical-data/meanLevel.xlsx?hash=A51C49A6FCF80FE18F2CE81D903F4970&sc_lang=en); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Historical v13 inventory note (unverified in current release): Direct link observed; file not inspected. RGDP level forecasts; same-vintage ratios; preserve documentation.
- **SPFDATES — SPF release dates** (Core / planned robustness). Expected file: `spf-release-dates.txt`. [Download or provider route](https://www.philadelphiafed.org/-/media/frbp/assets/surveys-and-data/survey-of-professional-forecasters/spf-release-dates.txt); [provider page](https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts). Historical v13 inventory note (unverified in current release): Exact link listed in provider documentation; file not inspected. Verify actual coverage and date conventions; do not guess release days.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use 1992 onward real GDP mean levels for vintage q, q+1; derive annualized ratio of means. Actual release day determines month-end origin; dp from preceding month only and verify availability, otherwise pseudo-real-time. Monthly log excess = log(1+RF+Mkt-RF)-log(1+RF), not log(1+Mkt-RF). Exact subsequent 3 months, optional 12; labels ending before new origin only. Use historical mean, EG-only, dp-only and joint OLS on common rows. Implement chronological forecasting and a strict target-maturity mask independently, HAC for overlap and paired block bootstrap with model refits. Do not treat the EG coefficient as causal. Use predeclared 1992-2007 training, 2008-2025 test, report actual usable dates and pre-1992 exclusion.

## Acceptance and first meeting
Verify SPF level horizons, release-date coverage, French units and Goyal dp definition/vintage. Require exact 3-month labels and common-sample benchmark; actual files/rights unverified.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

Provider routes and historical source notes are inherited, not newly verified. Independently implement all algorithms described here; private helper names, if present, denote methodological steps rather than dependencies distributed with this workspace. The v61 source-evidence erratum supersedes historical fresh-verification labels.

## Frozen research design (original catalogue)

Philadelphia Fed SPF mean real GDP level/growth forecasts and release dates https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/mean-forecasts; French monthly market/RF and Goyal dividend-price https://sites.google.com/view/agoyal145/. Use real GDP only, proposed 1992Q1-2025Q4; verify consistent level definitions and compute annualized expected growth from same-vintage current-quarter and next-quarter mean levels (ratio of mean forecasts, not mean individual growth). At survey release, use end-of-release-month origin, lag valuation ratio by one additional month as availability buffer; target following 3 months, h=12 secondary. Initial 1992-2007 training, 2008-2025 expanding test.

## Design-specific acceptance

Create an origin/release/target-end ledger; reconstruct first three forecasts from the actual workbook, and verify mature training targets at each decision. Compare EG, dp and both on identical origins with a mature historical mean; report effective sample, overlapping h=12 sensitivity, paired loss intervals and pseudo-real-time limitation.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish observation and release dates, gross and log returns, physical variance and implied variance, yield changes and holding returns, and nominal-real matching on identical dates.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
