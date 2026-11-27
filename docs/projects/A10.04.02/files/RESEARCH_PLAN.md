# Research plan | A10.04.02

## Study design and independent work

Perturb immature/final targets and ensure development winner is unchanged. Check nested candidate membership, paired common draws, strict boundary purge and same benchmark dates. Oracle never used in deployable policy. Real illustration remains required under original scope.

## Prespecified implementation

Freeze T=600, 300/150/150, nested candidate counts 10/50/200, iid and conditional-variance null, AR(1) phi .8, >=300 common-seed replications. Compare development-selected final performance against same-final best (invalid oracle, deliberately labeled). Report paired differences and uncertainty. Real illustration uses FF3/Mom/ST/LT lagged candidates if actual authorized files, no claim real data satisfy null. Synthetic-only redesign requires explicit approval.

## Required tasks

1. Validate simulation null and forecast alignment with known no-signal model; generate one forecast per date/candidate using only past outcomes.

2. Compare naive best evaluation score (selected on development block and reported on it) with same chosen model's independent final score; also compare an inner-validation selector with frozen final block. Report selection gap and fraction positive OOS R2 across replicates.

3. Vary search size, predictor correlation and conditional volatility; report MC intervals and use paired seeds.

4. Reproduce search protocol on real factor data, split before inspecting final sample; compare development and final gains without claiming real-data false-positive rate. No repeated test-driven redesign.

## Required exhibits

Distribution of apparent versus fresh-test OOS R2 by M, selection gap and MC uncertainty plots, false-discovery proxy (positive reported score under null, not formal p-value), real example cumulative loss table, transparent split/seed and candidate registry.

## Robustness

Preserve predictor persistence and return volatility clustering under alternative null, no return-feature forward leakage. Avoid comparing selectors on different dates or model menus. Define selection on development versus nested training folds precisely; use equal test length and independent seeds. Report if honest selection still underperforms mean; inference about statistical false rejections requires explicit tests, not positive scores alone.

## Minimum viable thesis

One iid and one conditional-variance null, at least three model search sizes, honest versus reused holdout with paired uncertainty, and one real-data illustration. Simulation is core; if real file unavailable, retain synthetic result and explicitly revise empirical scope.

## Optional extension

Add stationary bootstrap reality-check or multiple-testing adjustment on prespecified strategy returns; validate test size with simulations before use.

## Prerequisites

Predictive regressions, Monte Carlo, time-series dependence, Python and basic multiple testing.

## Thesis outline

1. Data mining in finance;

2. Model selection and temporal validation;

3. Null DGP and experimental protocol;

4. Simulation and real-data evidence;

5. Implications for research design.

## Milestones

W1-3: selection-bias theory and preregister grid; W4-6: implement nulls and forecast unit tests; W7-10: run paired experiments and real example; W11-13: dependence and uncertainty; W14-16: write and archive reproducible registry.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
