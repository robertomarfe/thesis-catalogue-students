# Research plan | D09.04.01

## Required tasks

1. Derive forward value and EPE via BSM.

2. Check h=0, R=1, sigma=0 and short/long sign conventions.

3. Compare quadrature and MC with confidence intervals.

4. Map exposure and CVA to maturity, hazard and recovery; compare fixed-hazard versus fixed-credit-spread scenarios.

5. Stress wrong-way dependence and report marginal default probabilities separately. Add one maturity with Cox intensity depending on the preceding underlying price. Calibrate a deterministic baseline sequentially to match the independent marginal survival curve at every grid node. Use separate calibration and evaluation paths; compare signed dependence and fixed-baseline cases, refine the grid and check with independent default-time simulation.

## Required exhibits

EPE curves, CVA/notional heatmap, analytic versus MC error, sensitivity table and default probability diagnostic. CVA and marginal default probabilities with matched and fixed baseline, evaluation survival errors and simulation/grid uncertainty.

## Robustness

Do not interpret Q intensities as physical default forecasts. Clean closeout, deterministic rates and unilateral default are stylized. No market CVA quotes or XVA calibration; exposure integration and MC error reported separately.

## Minimum viable thesis

One equity forward, independent default, analytic exposure and independent Monte Carlo check, four hazard/volatility scenarios; at one maturity, compare independent and two signed adapted Cox-intensity cases after matching the marginal survival curve on a common grid. Report default probabilities, CVA, simulation and time-grid uncertainty and the separate fixed-baseline comparison.

## Optional extension

Portfolio netting or collateral thresholds under matched exposure and closeout conventions.

## Prerequisites

BSM, credit intensity, numerical integration, Python.

## Thesis outline

1. Counterparty risk;

2. Exposure and default pricing;

3. Numerical verification;

4. Sensitivity and wrong-way risk;

5. Limits.

## Milestones

W1-3: pricing and closeout; W4-6: EPE and MC; W7-9: CVA validation; W10-12: sensitivities; W13-16: robustness and writing.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
