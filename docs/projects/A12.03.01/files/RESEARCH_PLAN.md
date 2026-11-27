# Research plan | A12.03.01

## Study design and independent work

Verify ST, Mom and LT definitions and exact units; align common dates and test the paired return/alpha difference directly with HAC/blocks. Freeze pre/post-1990 dates and report dependent returns; do not claim individual-level trading evidence or use future selection.

## Prespecified implementation

French US monthly ST_Rev low-minus-high formation t-1, Mom high-minus-low t-12..t-2, LT_Rev low-minus-high t-60..t-13; portfolios formed monthly, holding one month. Align all to exact common Jan 1931-Dec 2025 if supported and FF3. Keep published profitable orientation primary; for continuation comparison explicitly negate reversal factors. CAPM/FF3 HAC on same dates; paired differences using direct regressions of difference rather than independent SE. Fixed pre/post-1990, optional recession dates and decile profiles after verifying sort and weights; no RF subtraction from factors or turnover inference.

## Required tasks

1. Verify orientation, formation and holding windows; reproduce spread means and autocorrelations on common months.

2. Estimate CAPM and FF3 alphas, with HAC intervals for each and paired difference tests between continuation spreads.

3. Analyze optional decile portfolio mean/alpha profiles across formation windows, compare value versus equal-weight if files support and distinguish factor vs decile construction.

4. Prespecify subperiod and recession sensitivity using available NBER dates (optional), report covariance and severe loss episodes; distinguish turnover-sensitive short reversal from long reversal.

## Required exhibits

Three orientation-consistent mean/alpha comparisons, factor return and cumulative P&L plots, formation-window diagram, decile profiles if available, dependence-aware paired tests and stability table. Zero-cost cumulative P&L not wealth without capital convention.

## Robustness

No inference that the same stock reverses after momentum from unrelated sorted portfolios; no causal identification of investor psychology. Factor construction, skip months, rebalance frequency, microstructure and costs differ. Do not subtract RF from zero-cost factors, or claim net tradable performance. Common sample and alternate HAC bandwidth; report uncertainty and publication-vintage limitations.

## Minimum viable thesis

Verified three factor files and FF3, aligned formation orientation, CAPM/FF3 and paired comparisons, prespecified subperiod stability, careful distinction of formation versus holding horizon. Decile analysis desirable but not mandatory.

## Optional extension

Use individual-stock signal histories from a verified public replication package to trace within-stock horizon dynamics, avoiding look-ahead and survivorship; do not assume such files accessible in core.

## Prerequisites

Factor models, portfolio returns, OLS/HAC and Python data handling.

## Thesis outline

1. Return continuation and reversal mechanisms;

2. Portfolio formation and factor adjustment;

3. Public data and protocol;

4. Horizon patterns and stability;

5. Alternative explanations and conclusion.

## Milestones

W1-3: read literature and verify windows; W4-6: clean factor and portfolio series; W7-10: descriptive and alpha comparisons; W11-13: uncertainty, subsamples and cost caveats; W14-16: write and reproduce.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
