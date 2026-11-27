# Research plan | D09.01.02

## Study design and independent work

Show the analytic hit check, bridge versus endpoint-only monitoring and common-path paired intervals. Compare the maturity-only benchmark under identical terminal inputs. Preserve unsuccessful or high-error grid cases and quantify both default timing and loss effects.

## Required tasks

1. Derive Merton zero debt price and barrier hitting formula; validate no-barrier limit and probability bounds.

2. Implement discrete and bridge survival and compare across grid resolutions; report MC intervals.

3. Price debt and compute annual continuously compounded spread -(log(B/F))/T-r; distinguish early from terminal default.

4. Compare term structures across H, sigma and recovery, holding F and asset dynamics fixed.

5. Test recovery timing as separate scenario using fine-step first-passage approximation with convergence; interpret economic rather than numerical differences.

## Required exhibits

Survival validation, debt price and spread curves, default-timing decomposition, recovery and monitoring sensitivity table.

## Robustness

Under baseline R*F<=H does not ensure pathwise smaller payout than terminal min(V_T,F) after an early hit; do not impose monotonic comparison to Merton for positive recovery. At R=0 barrier debt is <= Merton pathwise. Q default probability is not historical frequency. No empirical credit-spread calibration or equity/debt joint equilibrium claimed.

## Minimum viable thesis

Merton benchmark, one early-default model with explicit recovery, analytic hit check, bridge versus discrete monitoring, spread curves for two barriers and three volatilities. Distinct from maturity-only default thesis.

## Optional extension

Use a time-dependent covenant barrier or calibrate to synthetic equity and debt quotes with parameter-identification checks.

## Prerequisites

Stochastic calculus, first-passage distributions, option pricing and Python.

## Thesis outline

1. Merton and first-passage debt;

2. Survival and recovery;

3. Analytical and simulation checks;

4. Credit spread comparative statics;

5. Economic limits.

## Milestones

W1-3: Merton and barrier theory; W4-6: hit probability and bridge code; W7-9: debt prices and curves; W10-12: recovery/timing robustness; W13-16: interpret and write.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
