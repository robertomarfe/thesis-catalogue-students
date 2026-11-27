# Data and model setup | A11.03.01

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
FRED quarterly real PCE per capita A794RX0Q048SBEA, quarterly price index PCECTPI, French monthly RF and 10 Industry portfolios/Mkt-RF. https://fred.stlouisfed.org/series/A794RX0Q048SBEA ; https://fred.stlouisfed.org/series/PCECTPI ; https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html . Compound nominal total returns to quarters then deflate; align g_c from t to t+1 with same quarter payoff. Aim 1947-2025 complete sample. Base q=3: gross bill, market excess and one prespecified industry excess (e.g. utilities). Expanded q adds two industry excess moments; instrument sensitivity uses lagged market return observed at t (demeaned/scaled using fixed rule). Avoid lagged revised consumption as real-time instrument. Parameters beta in [0.8,1.1], gamma in [0,100], quarterly; boundary and plausibility reported, not automatic restriction to conventional estimates.

## Inputs
- **FF3M — US FF3 monthly** (Core / planned robustness). Expected file: `F-F_Research_Data_Factors_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **FF10M — US 10 industries monthly** (Core / planned robustness). Expected file: `10_Industry_Portfolios_CSV.zip`. [Download or provider route](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Industry_Portfolios_CSV.zip); [provider page](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html). Historical v13 inventory note (unverified in current release): Direct link observed in provider page; bytes not inspected. Use correct monthly/daily and value-weighted total return block; retain vintage.
- **A794RX0Q048SBEA — A794RX0Q048SBEA** (Core / planned robustness). Expected file: `A794RX0Q048SBEA.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=A794RX0Q048SBEA); [provider page](https://fred.stlouisfed.org/series/A794RX0Q048SBEA). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly real PCE per capita; revised vintage.
- **PCECTPI — PCECTPI** (Core / planned robustness). Expected file: `PCECTPI.csv`. [Download or provider route](https://fred.stlouisfed.org/graph/fredgraph.csv?id=PCECTPI); [provider page](https://fred.stlouisfed.org/series/PCECTPI). Historical v13 inventory note (unverified in current release): Direct CSV endpoint constructed from exact series ID; not fetched. Quarterly PCE price index; check same quarter.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use quarterly PCE per capita and PCE deflator with separately compounded French gross bill/market/industries. Align all payoffs and gc from previous quarter. Base bill plus market and fixed utilities excess moments; expanded two other fixed industries. Bounds beta [.8,1.1], gamma [0,100]; multistart, fixed identity then two-step Bartlett HAC inverse with explicit eigenvalue ridge, analytical Jacobian, rank and criterion profiles. Instrument lagged nominal market excess return (known at origin), not revised consumption. Bootstrap whole quarters/estimate each draw; report boundary, convergence and J assumptions. Regularized J not a classical chi-square.

## Acceptance and first meeting
Actual source rights, bytes, dates, decimal units, common sample and covariance rank pending; verify real bill is proxy, moments and lagged instruments timing, optimizer/rank/boundary and annual-v-quarter preference units.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel/parquet inputs require the relevant optional reader (openpyxl, xlrd, pyarrow); inspect raw schema and permissions first (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Use quarterly parameters and same-quarter consumption/payoffs; preserve the original broad bounds and fixed moments. Report scaling, HAC bandwidth, effective rank and convergence. Validate independently on a designed simulation before empirical estimation; do not select moments after viewing rejection.

## Timing, accounting and units

Record total, gross and excess return conventions, RF timing, sampling frequency, factor definitions and annualization. Freeze common date and asset sets, provider vintage and information availability. Distinguish training, validation and holdout; do not treat factor returns or long-short spreads as total returns.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
