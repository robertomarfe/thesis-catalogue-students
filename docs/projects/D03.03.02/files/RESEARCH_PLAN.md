# Research plan | D03.03.02

## Study design and independent work

Verify the transition convention, use the same target for GARCH and rolling forecasts, retain false alarms and rare-event counts, and account for overlap. The stress event is high realized variance, not a recession indicator.

## Required tasks

1. Simulate known two-state DGP and validate filtered probabilities/transition recovery with label sorting and multiple starts.

2. Fit two-state and GARCH, check likelihood, state occupancy and degenerate transitions.

3. Forecast 5/20-day variance and event probabilities, using models with identical information cutoff.

4. Compare QLIKE, Brier score, calibration and precision-recall; report event counts.

5. Use non-overlap and block bootstrap, predeclare episode summaries (e.g. 2020) and inspect false alarms rather than selecting crises after fitting.

## Required exhibits

Filtered probability and variance plots; forecast loss and event calibration tables; transition and state-duration diagnostics.

## Robustness

Crisis event means high realized variance, not recession or causal prediction. VIX is option-implied not physical future variance. Revised source data yield pseudo-OOS; overlapping windows invalidate naive IID tests.

## Minimum viable thesis

Validated two-state filter, GARCH/rolling benchmarks, common held-out variance and event score comparison. Distinct from D03.03.01 continuous latent SV density forecasting.

## Optional extension

Student-t emissions or Markov-switching GARCH with careful likelihood validation.

## Prerequisites

Time series, likelihood, simulation, probability, Python.

## Thesis outline

1. Volatility regimes;

2. Filtering and benchmarks;

3. Data and validation;

4. Held-out forecasting;

5. Stress interpretation.

## Milestones

W1-3: Markov filtering; W4-6: simulated validation; W7-9: empirical fits; W10-12: forecasts and rare events; W13-16: write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
