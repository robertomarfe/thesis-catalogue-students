# Research plan | A09.02.02

## Study design and independent work

Audit the G10 gross definition and dates before use. Report state counts, training thresholds, information lags and common forecast origins. Do not substitute other carry factors or claim causal effects.

## Required tasks

1. Document published portfolio construction, funding and gross/net conventions.

2. Compare average return, volatility, skewness, drawdown and losses by contemporaneous market/VIX state.

3. Estimate carry on market and market*stress interaction, with HAC and stress-count reporting.

4. Forecast next-month carry using lagged VIX/NFCI against expanding mean; initial 120 months, no full-sample thresholds.

5. Compare gross vs net, fixed subperiods and paired block-bootstrap uncertainty.

## Required exhibits

Carry wealth and drawdown plot; state means/exposures; predictive OOS R2 and loss intervals; gross/net comparison.

## Robustness

Published carry is not bilateral UIP or newly implementable strategy. Check long-short return leverage/normalization. VIX contemporaneous conditioning is descriptive; NFCI revised vintage is pseudo-real-time. Rare states have limited power.

## Minimum viable thesis

One documented G10 gross carry series, common monthly market/VIX data, state-dependent returns and lagged forecasting; net optional if accessible. Distinct from A09.02.01 bilateral forward premium puzzle.

## Optional extension

Compare G10 and broader currency universe if same provider definitions; tail regressions.

## Prerequisites

FX returns, conditional regressions, portfolio factors, time-series inference.

## Thesis outline

1. Carry economics;

2. Global risk states;

3. Data and timing;

4. Conditional and predictive results;

5. Limits.

## Milestones

W1-3: theory and data gate; W4-6: common sample; W7-9: state exposures; W10-12: forecasts and robustness; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
