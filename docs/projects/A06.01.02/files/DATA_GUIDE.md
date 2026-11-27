# Data and model setup | A06.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Goyal combined annual workbook (https://sites.google.com/view/agoyal145/), 1927-2025 target; verify year-end index price P, annual dividend D and total-return convention; construct P/D and nominal annual dividend growth, use nominal log total return with consistent timing. Shiller https://www.econ.yale.edu/~shiller/data.htm optional cross-check, annual trailing totals and monthly-average prices approximate only. If exact year-end price and annual payout unavailable, use documented proxy and report linearization/accounting residual. Estimate VAR(1) on [z,g,r]; H=1,5,10,20 and stable long-run limit only when rho*A has spectral radius<1.

## Inputs
- **GOYAL2025 — Combined GW/GWZ full-sample workbook through 2025** (Core). Expected file: `Data2025.xlsx`. [Download or provider route](https://docs.google.com/spreadsheets/d/17mw_IpaiLFDrGnrPRQ2o1ugV5nJsZuD1/edit?ouid=113571510202500088860&rtpof=true&sd=true&usp=sharing); [provider page](https://sites.google.com/view/agoyal145/). Historical v13 inventory note (unverified in current release): Exact file page observed; download using Google Sheets File > Download > Excel. Freeze version, include definitions and verify timing; full-sample revised data.
- **SHILLER — US stock market price, dividend, earnings, CPI** (Optional cross-check). Expected file: `ie_data.xls`. [Download or provider route](https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/249997aa-1eef-4237-93ec-2d319f7881ab/ie_data.xls?ver=1794837439406); [provider page](https://shillerdata.com/). Historical v13 inventory note (unverified in current release): Exact link displayed on new author website; click returned unsupported Excel content type, no binary validated. Use annual trailing dividend totals; check current file/link. Previous candidate https://www.econ.yale.edu/~shiller/data/ie_data.xls retained here for provenance; price monthly average, annualized dividend totals interpolated, CPI. Recheck link/version at acquisition.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Original z=log(D/P); pd_identity uses log(P/D) internally, negate returned z before VAR. Compute exact accounting residual using annual gross return versus (P_t+D_t)/P_prev, then loglinear residual. Fit VAR on [z,g,r] annual contiguous data; dp_pv_loadings returns [r,-g,-e,terminal] loadings; covariance with z divided by Var(z) gives signed shares, not positive normalized percentages. Report centered-state identity separately from raw sample accounting residual, stable discounted limit, direct forecast regressions, block/VAR bootstrap refitting rho; no silently discarded unstable draws. Annual Goyal raw variables verify definitions; documented proxy only if exact absent and supervisor approves.

## Acceptance and first meeting
Actual Goyal workbook annual tab, payout timing, and identity residual required; no data substitution. Synthetic direct forecast identity for finite/infinite horizons.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Goyal combined annual workbook (https://sites.google.com/view/agoyal145/), 1927-2025 target; verify year-end index price P, annual dividend D and total-return convention; construct P/D and nominal annual dividend growth, use nominal log total return with consistent timing. Shiller https://www.econ.yale.edu/~shiller/data.htm optional cross-check, annual trailing totals and monthly-average prices approximate only. If exact year-end price and annual payout unavailable, use documented proxy and report linearization/accounting residual. Estimate VAR(1) on [z,g,r]; H=1,5,10,20 and stable long-run limit only when rho*A has spectral radius<1.

## Design-specific acceptance

Use exact annual timing and report accounting residual before log-linear residual; retain signs [future r,-future g,-residual,terminal]. Compare direct finite sums with loadings, covariance shares including negative terms and terminal, and unstable bootstrap draws; if payout data cannot be matched to return convention, stop or obtain approval for clearly labeled proxy.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
