# Data and model setup | A05.01.02

**Current data gate: pending.** No actual external input bytes are supplied or validated.

## Original input contract and sample
GSW nominal continuous zero yields, https://www.federalreserve.gov/data/nominal-yield-curve.htm, common 1,2,3,5,7,10 years, end-of-month 1990-2025 target. Convert percent to decimals; train 1990-2004, evaluate 2005-2025, report yield error in bp. Compare rank-one affine loading, rank-one PCA, rank-two/three PCA, using training mean and loadings frozen in test. For reconstruction infer scores from observed same-date yields; a separate exercise uses only a 2-year observed yield to predict remaining maturities.

## Inputs
- **GSW — GSW nominal fitted yield curve** (Core). Expected file: `feds200628.csv`. [Download or provider route](https://www.federalreserve.gov/data/yield-curve-tables/feds200628.csv); [provider page](https://www.federalreserve.gov/data/nominal-yield-curve.htm). Link status from v13 inventory: Direct link observed; file not inspected. Nominal off-the-run Treasury curve; SVENY zero yields in percent; not OIS.

For external inputs, direct paths are inherited from the frozen inventory, not a guarantee of availability or license. If the expected filename is unspecified, save the actual authorized export under a documented local filename and update your local manifest. Optional sources are not required. Use the provider documentation and document conventions, rights and parsing locally.

## Construction and timing
Use common 1,2,3,5,7,10-year monthly yields. Fit mean and Vasicek loading B(a,T)/T with training-only a selection; compare rank-one and rank-two/three PCA. Freeze mean/loadings. Infer scores from all yields for reconstruction, separately infer a single score from 2Y only and evaluate other maturities. Compare matched errors in bp; rank-three cannot be inferred from one yield.

## Acceptance and first meeting
Actual GSW common sample and revisions open. Verify synthetic exact rank-one recovery; report nonidentification and conditioning of loadings, do not claim arbitrage-free PCA.

Build a local inventory; inspect actual schema and rights. Save input ledger, actual dates, joint sample, complete calendar and missing counts. No actual files validated. Use local normalized CSV exports only after inspecting raw metadata; Excel inputs can be inspected with pandas/openpyxl locally (not needed for the introductory setup check). If source fails, obtain explicitly approved redesign or defer.

## Design-specific acceptance

Report unrestricted PCA as a rank-matched comparator. Separate same-date reconstruction from held-out maturity prediction; do not claim the fitted loading uniquely identifies physical or risk-neutral dynamics.

## Timing, accounting and units

Specify nominal or real, continuous zero yield versus par yield, maturity in years, year fractions, rate units and the information available at each origin. Keep price versus yield changes and aged-bond returns distinct. State the probability measure and discounting convention. Freeze provider vintage; never infer real-time availability from observation dates alone.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
