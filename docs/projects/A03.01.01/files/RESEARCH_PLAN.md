# Research plan | A03.01.01

## Study design and independent work

On a common quarterly calendar report both Euler residuals and beta pricing the bill, then the market residual and covariance identity; resample contiguous joint date blocks. Check compounded nominal gross legs divided by the same inflation ratio and compare beta annualized by beta_q**4. Distinguish arithmetic premium from compound annual growth. Report parameter grid including infeasible beta.

## Prespecified implementation

Normalize FF3M market=RF+Mkt-RF and bill=RF as decimal simple monthly returns; use quarter_real on calendar periods and PCE/PCECTPI levels. On common quarters compute real market minus real bill, covariance with log consumption growth and 4x arithmetic mean. Set beta_q=beta_annual**.25; euler_grid returns beta x gamma x asset residual. Report the two residuals separately, bootstrap common quarterly blocks and recompute beta frontier; no claim realized real bills are known real risk-free. For iid illustration use lognormal joint moments; distinguish mean gross versus log and plausible risk aversion.

## Required tasks

1. Estimate consumption growth and real return moments, align quarterly dates, explain time averaging; compute covariance and annualized mean excess returns using four times quarterly arithmetic mean.

2. For each preference pair compute sample Euler residuals E[mR_m]-1 and E[mR_bill]-1; plot joint errors, optionally choose beta to price bills via sample Euler condition and evaluate market residual.

3. In an iid lognormal illustrative economy evaluate model safe rate and premium using calibrated consumption and return covariance; separate approximation from exact sample tests.

4. Quantify sampling uncertainty with block bootstrap, compare annual aggregation and consumption definitions, and assess economically plausible gamma rather than mechanically minimizing residuals.

## Required exhibits

Moment and covariance table; beta/gamma heatmap of Euler residuals; implied safe-rate and premium plots with empirical comparison; bootstrap intervals; explicit table of real bill proxy caveats. Explain the extent of joint fit, not just the gamma matching one target.

## Robustness

Distinguish quarterly from annual beta and units. Check sensitivity to 2020 and long sample choices with prespecified alternatives; use revised data for unconditional analysis and note measurement error. If real bill Euler condition fails, do not infer exact real risk-free-rate error without modeling inflation. Avoid treating estimated high gamma as a structural identification result.

## Minimum viable thesis

Correct SDF and Euler derivation, publicly sourced consumption/market data, grid-based joint moment exercise, risk-free proxy distinction and uncertainty. The puzzle is assessed even if a chosen sample weakens it.

## Optional extension

Introduce a simple habit or Epstein-Zin illustration after core CRRA diagnostics; compare mechanisms analytically before attempting a high-dimensional calibration.

## Prerequisites

Expected utility, stochastic discount factors, covariance/lognormal algebra, empirical return construction, Python. No structural estimation package required.

## Thesis outline

1. Equity premium and risk-free puzzles;

2. CRRA theory and quantitative restrictions;

3. Data, moments and calibration;

4. Joint fit and preference sensitivity;

5. Limitations and alternative mechanisms.

## Milestones

W1-3: derive Euler/lognormal restrictions; W4-6: align consumption, inflation and returns; W7-10: compute residuals and parameter grids; W11-13: bootstrap and measurement sensitivities; W14-16: write and validate.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
