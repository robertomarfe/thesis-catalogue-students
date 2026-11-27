# Data and model setup | A11.02.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
Monthly French market, 10 industry and 25 Size/BM value-weighted total return portfolios plus RF; compound each total gross return and bill separately to quarter. FRED quarterly real PCE per capita A794RX0Q048SBEA and PCE price index PCECTPI; deflate all nominal gross returns by same quarterly price ratio. https://fred.stlouisfed.org/series/A794RX0Q048SBEA ; https://fred.stlouisfed.org/series/PCECTPI ; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Aim 1947-2025 common complete quarters; nested sets market, market+10 industries, +25 portfolios; drop redundant assets only by prespecified rank rule. CRRA grid gamma=1,2,5,10,20, beta=0.99 quarterly.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF25M — US 25 size/BM monthly** (Core / planned robustness). Expected file: `25_Portfolios_5x5_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core / planned robustness). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **A794RX0Q048SBEA — A794RX0Q048SBEA** (Core / planned robustness). Expected file: `A794RX0Q048SBEA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=A794RX0Q048SBEA); [provider page](https://fred.stlouisfed.org/series/A794RX0Q048SBEA). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly real PCE per capita; revised vintage.
- **PCECTPI — PCECTPI** (Core / planned robustness). Expected file: `PCECTPI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCECTPI); [provider page](https://fred.stlouisfed.org/series/PCECTPI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly PCE price index; check same quarter.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Compound monthly nominal market total (Mkt-RF+RF), portfolios and bill separately into complete calendar quarters; deflate each by PCECTPI current/prior quarter. PCE per capita SAAR level ratio, no annualization of quarterly growth; 1947–2025 common complete quarters and lagged prior price/consumption. Nested market, +10 industries, +25 size/BM; reject singular and use predeclared independent basis. HJ SD(m)/mean(m) bound and CRRA gamma 1,2,5,10,20 beta .99; also pricing errors. Block bootstrap quarters, shrinkage only labeled sensitivity.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; confirm positive PCE levels, complete quarters, real gross bill is not known constant real risk-free.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use identical complete quarters for all nested sets. Report raw covariance spectrum, rank policy, bootstrap and labeled shrinkage sensitivity; never claim an observed constant real bill or infer rejection solely from a sample bound gap.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
