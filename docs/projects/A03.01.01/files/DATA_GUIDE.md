# Data and model setup | A03.01.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Use FRED quarterly real PCE per capita A794RX0Q048SBEA (https://fred.stlouisfed.org/series/A794RX0Q048SBEA), quarterly PCE price index (PCECTPI; verify https://fred.stlouisfed.org/series/PCECTPI), and French monthly Mkt-RF, RF (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Target 1950-2025 common complete quarters. Form quarterly market and bill gross nominal returns by separately compounding monthly legs, deflate both by matched quarterly inflation; real bill return is an ex post proxy and not conditionally risk-free if inflation is uncertain. Use beta annual 0.95-0.995 raised to 1/4 and gamma grid 1,2,5,10,20,40 (last values diagnostic). Aggregate PCE includes durables; alternative nondurables/services use correctly constructed BEA chain index or nominal-share growth weights, never simply sum chained real levels.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **A794RX0Q048SBEA — A794RX0Q048SBEA** (Core / planned robustness). Expected file: `A794RX0Q048SBEA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=A794RX0Q048SBEA); [provider page](https://fred.stlouisfed.org/series/A794RX0Q048SBEA). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly real PCE per capita; revised vintage.
- **PCECTPI — PCECTPI** (Core / planned robustness). Expected file: `PCECTPI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCECTPI); [provider page](https://fred.stlouisfed.org/series/PCECTPI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly PCE price index; check same quarter.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Normalize FF3M market=RF+Mkt-RF and bill=RF as decimal simple monthly returns; use quarter_real on calendar periods and PCE/PCECTPI levels. On common quarters compute real market minus real bill, covariance with log consumption growth and 4x arithmetic mean. Set beta_q=beta_annual**.25; euler_grid returns beta x gamma x asset residual. Report the two residuals separately, bootstrap common quarterly blocks and recompute beta frontier; no claim realized real bills are known real risk-free. For iid illustration use lognormal joint moments; distinguish mean gross versus log and plausible risk aversion.

## Acceptance and first meeting
Actual FF3M, consumption and PCECTPI levels, rights and complete sample required; artificial quarterly matching and exact Euler moment tests only.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Frozen research design (original catalogue)

Use FRED quarterly real PCE per capita A794RX0Q048SBEA (https://fred.stlouisfed.org/series/A794RX0Q048SBEA), quarterly PCE price index (PCECTPI; verify https://fred.stlouisfed.org/series/PCECTPI), and French monthly Mkt-RF, RF (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Target 1950-2025 common complete quarters. Form quarterly market and bill gross nominal returns by separately compounding monthly legs, deflate both by matched quarterly inflation; real bill return is an ex post proxy and not conditionally risk-free if inflation is uncertain. Use beta annual 0.95-0.995 raised to 1/4 and gamma grid 1,2,5,10,20,40 (last values diagnostic). Aggregate PCE includes durables; alternative nondurables/services use correctly constructed BEA chain index or nominal-share growth weights, never simply sum chained real levels.

## Design-specific acceptance

On a common quarterly calendar report both Euler residuals and beta pricing the bill, then the market residual and covariance identity; resample contiguous joint date blocks. Check compounded nominal gross legs divided by the same inflation ratio and compare beta annualized by beta_q**4. Distinguish arithmetic premium from compound annual growth. Report parameter grid including infeasible beta.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Separate model-implied curves from traded prices, real safe payoffs from ex post real returns, and conditional from unconditional moments.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
