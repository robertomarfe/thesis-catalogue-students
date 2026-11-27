# Data and model setup | A06.04.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal annual Data2025 workbook https://sites.google.com/view/agoyal145/ with aggregate total returns, dividend-price and short-rate series; deflate nominal gross return with annual CPI from https://fred.stlouisfed.org/series/CPIAUCSL, consistent year-end CPI timing. Common 1948-2025 or first feasible year (CPIAUCSL starts in 1947); annual avoids using rolling annual dividends as monthly payouts. Use 3-variable VAR(1) and alternative with term spread; rho from mean P/D (report fixed 0.95 annual sensitivity); ensure stability and compare finite H=5,10,20 with infinite solution. Optional Shiller annual data and FF market return cross-check.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.
- **FF3M — US FF3 monthly** (Optional cross-check). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **CPIAUCSL — CPIAUCSL** (Core). Expected file: `CPIAUCSL.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL); [provider page](https://fred.stlouisfed.org/series/CPIAUCSL). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Monthly SA CPI; quarterly average; annualization match.
- **SHILLER — US stock market price, dividend, earnings, CPI** (Optional cross-check). Expected file: `ie_data.xls`. [Download or provider route](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/249997aa-1eef-4237-93ec-2d319f7881ab/ie_data.xls?ver=1794837439406); [provider page](https://shillerdata.com/). Historical v13 inventory note (unverified in current release): Exact link displayed on new author website; click returned unsupported Excel content type, no binary validated. Use annual trailing dividend totals; check current file/link. Previous candidate https://www.econ.yale.edu/~shiller/data/ie_data.xls retained here for provenance; price monthly average, annualized dividend totals interpolated, CPI. Recheck link/version at acquisition.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Original VAR state first log real total return, then log D/P and short rate, alternative term spread. Deflate nominal gross returns by December CPI ratio, preserve year timing and avoid Shiller interpolated payout as annual exact. Center stationary VAR; return_news(A,rho,H) uses H future dates, excluding t, returns CF residual and DR. N_CF=u_r+N_DR; residual CF absorbs terminal and approximation/omitted news. Report Var(CF)+Var(DR)-2Cov and signed shares; bootstrap VAR and rho with joint innovations, retain invalid draw counts, compare finite and infinite horizons and two information sets. Optional direct dividend-news check requires actual g and alternative state order; not an independent identified shock.

## Acceptance and first meeting
Actual annual Goyal data, CPI rights/coverage and stationary VAR required; check algebra and finite/infinite sums. Synthetic accounting only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal annual Data2025 workbook https://sites.google.com/view/agoyal145/ with aggregate total returns, dividend-price and short-rate series; deflate nominal gross return with annual CPI from https://fred.stlouisfed.org/series/CPIAUCSL, consistent year-end CPI timing. Common 1948-2025 or first feasible year (CPIAUCSL starts in 1947); annual avoids using rolling annual dividends as monthly payouts. Use 3-variable VAR(1) and alternative with term spread; rho from mean P/D (report fixed 0.95 annual sensitivity); ensure stability and compare finite H=5,10,20 with infinite solution. Optional Shiller annual data and FF market return cross-check.

## Design-specific acceptance

Use return-first VAR, stable roots, same calendar and real gross convention; verify direct discounted sums and signed Var(CF)+Var(DR)-2Cov identity, report finite and infinite estimates, horizon and information-set sensitivity. Refit rho and VAR inside bootstrap, retain inadmissible draws and note weak stability near unit roots.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
