# Research plan | A04.02.02

## Study design and independent work

Compute both bond prices for n and n-h using the same documented GSW Svensson convention; verify flat-curve log holding return h*y. Compound monthly gross legs and deflate with exact adjacent CPI; fit inflation AR only on available history, use overlapping-horizon HAC or nonoverlap sensitivity and paired date blocks. Label retrospective hedge exposure, not expected return.

## Prespecified implementation

GSW fitted nominal log discount curves at actual month-end observation dates; interpolate log discounts at n-h without extrapolation (5y/10y baseline; n-h exact). Return from buying n-year zero at t and holding 1 or 12 months, not n-year rolling index over h. Equity compound actual total returns; use monthly-average CPI ratio as end-month proxy. Fit expanding AR(1) to released monthly log inflation, one-month lag: if last observed t-1, forecast h+1 steps, discard forecast for t, sum steps t+1..t+h; if actual lag differs use exact mapping. Use same realized and modeled-surprise inflation regressors for nominal and real log returns; coefficient difference exactly one for realized inflation with same sample/intercept. Use common periods, overlap HAC/block, fixed subperiods, 60/40 simple returns with fixed rebalancing convention.

## Required tasks

1. Validate yield units, discount curve, date alignment and zero-bond holding return; compare with duration approximation as diagnostic only.

2. Plot nominal and real returns, cumulative purchasing power and rolling inflation beta.

3. Regress log nominal returns on realized and forecast-error inflation, report nominal and real slopes and HAC intervals.

4. Compare one- and 12-month horizons and predeclared 1971-1989/1990-2007/2008-2025 subperiods; overlapping horizons need HAC or block bootstrap.

5. Assess covariance and variance reduction for a stock/bond mix with fixed ex ante weights; no hindsight optimization.

## Required exhibits

Construction checks, nominal/real return and inflation tables, beta intervals, horizon/regime plots and real portfolio risk comparison.

## Robustness

GSW zero returns are synthetic government bond holdings, not bond-fund returns or OIS. CPI revisions and release timing constrain true real-time surprises; AR residuals are model-based, not structural shocks. Realized inflation is not observable at the investment date. Regressions are descriptive hedging associations, not causal effects.

## Minimum viable thesis

Monthly and annual nominal/real returns of equity and one synthetic zero maturity; realized and modeled surprise inflation, robust intervals and fixed subperiod comparison. Distinct from A04.02.01 cross-sectional pricing.

## Optional extension

Use SPF inflation expectations or real TIPS curve for a shorter sample; distinguish inflation compensation from expected inflation.

## Prerequisites

Fixed income, return compounding, time-series econometrics, Python.

## Thesis outline

1. Inflation and real returns;

2. Equity and Treasury holding returns;

3. Inflation measures;

4. Horizon and regime evidence;

5. Portfolio implications.

## Milestones

W1-3: Fisher relation and data; W4-6: return construction; W7-9: inflation regressions; W10-12: regimes and portfolio risk; W13-16: write and validate.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
