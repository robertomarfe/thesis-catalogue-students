# Research plan | A10.02.01

## Study design and independent work

No random cross-validation; identical dates/features and mature label rules; perturb future inputs and labels; verify depth/minimum leaf constraints; record seeds and failed fits, not only successful winners.

## Prespecified implementation

Freeze original six features and small RF/boosting grid, training-only scaler inside pipeline. Tune on past folds, lock model menu; report time budget and failed fits. Compare ridge and mean on exact dates, permutation/partial dependence only on past validation; no outcome-driven feature search.

## Required tasks

1. Reproduce expanding mean and ridge; audit feature timing and target dates.

2. Implement expanding RF and gradient boosting with inner walk-forward folds; select hyperparameters by past-only MSE, never final-period outcomes.

3. Compare final loss, OOS R2, forecast correlation, paired block-bootstrap uncertainty and subperiods.

4. Inspect partial dependence or validation permutation importance for a few prespecified features, cautioning correlated predictors.

5. Evaluate bounded market weight from forecasts and past variance against static allocation, with transaction costs and consistent funding.

## Required exhibits

Forecast ledger, chosen hyperparameter history, loss/OOS R2 table, uncertainty, interpretability figures and optional economic value comparison.

## Robustness

Current workbook revised; pseudo-OOS not real-time. No random cross-validation or full-sample scaling. Tree extrapolation is limited and feature importance not causal. If no gains, interpret complexity/variance trade-off, not failed thesis.

## Minimum viable thesis

Expanding mean, ridge and one shallow ensemble, nested chronological tuning, untouched holdout loss table and uncertainty. Distinct from A10.01.01 linear regularization and A10.04.02 search-bias simulations.

## Optional extension

Test real-time vintages or a predefined interaction model; do not expand the model zoo until baseline protocol is frozen.

## Prerequisites

Time series, basic ML, Python/scikit-learn and return arithmetic.

## Thesis outline

1. Equity return forecasting;

2. Trees and regularization;

3. Data and temporal validation;

4. Forecast results;

5. Interpretability and economic value.

## Milestones

W1-3: literature and forecast design; W4-6: data and linear benchmarks; W7-9: nested trees; W10-12: held-out inference; W13-16: interpretation, code and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
