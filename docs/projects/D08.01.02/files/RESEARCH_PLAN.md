# Research plan | D08.01.02

## Study design and independent work

Unlike the VIX futures project, the random quantity is realized integrated variance over the entire swap horizon. Report economic errors in volatility points, not only variance units.

## Required tasks

1. Derive strikes, Jensen bound and second-order correction; compute analytic expected variance.

2. Simulate I with matched quadrature conventions, verify simulated mean against analytic mean, and estimate gap using paired path statistics.

3. Compare Taylor and MC values in volatility points and relative units; report sampling intervals using path bootstrap or delta method.

4. Map error across maturity, xi and mean reversion and show when Taylor breaks down.

5. Diagnose zero-boundary/Feller violations and quadrature bias without silently discarding paths.

## Required exhibits

Strike and gap tables, distribution of I and sqrt(I), maturity/vol-of-vol sensitivity maps, MC precision and approximation-error plots.

## Robustness

Use annualized variance consistently and quote vol points as 100*sqrt(I). No Jensen reversal from sampling noise when strikes use same paths. Test deterministic-variance limit and time-grid bias. No observed swap quotes or calibration claimed.

## Minimum viable thesis

Analytic mean, validated simulation, exact Jensen comparison, second-order approximation and numerical sensitivity to at least maturity and xi.

## Optional extension

Study a discrete-return realized-variance convention in a full Heston price simulation, with monitoring and convexity corrections separated.

## Prerequisites

Risk-neutral pricing, stochastic calculus basics, Monte Carlo and Python.

## Thesis outline

1. Variance and volatility contracts;

2. Convexity and CIR moments;

3. Simulation validation;

4. Strike differences and approximation error;

5. Limitations.

## Milestones

W1-3: contracts and expansion; W4-6: CIR simulation and mean checks; W7-9: sensitivity experiments; W10-12: approximation, MC and grid errors; W13-16: economic interpretation and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
