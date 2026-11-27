# Research plan | D06.01.01

## Study design and independent work

Change frequency and window separately. Use union-grid draws where practical because grids are not nested. Preserve payment time; do not call a finite fixing grid a continuous average.

## Required tasks

1. Derive geometric Asian closed form from joint lognormal moments; verify single fixing reduces to a European claim when fixing at T.

2. Price arithmetic and geometric Asians; validate ordering, Monte Carlo confidence intervals and variance reduction.

3. Separate monitoring frequency from averaging window, comparing each while holding the other constant.

4. Estimate delta and vega with common-random-number central differences and step-size checks; keep all fixings future at valuation.

5. Map price and Greek differences from European benchmark across strikes and volatilities; explain results through variance and expected average levels.

## Required exhibits

Analytical derivation, verification and confidence interval table, price/Greek panels and averaging-window comparison, documented payoff and fixing schedules.

## Robustness

Use exact time conventions, same maturity and payoff units; note that changing averaging dates changes expected level at nonzero carry. Distinguish price sensitivity at initiation from after some fixings are observed. Avoid calling discrete results continuous-limit values without a convergence test.

## Minimum viable thesis

Validated geometric and arithmetic pricing, two windows and at least three fixing frequencies, delta and vega analysis, interpretation of averaging versus terminal exposure.

## Optional extension

Analyze pricing after partial fixing or introduce a floating strike; do not duplicate D05.01.02's algorithm ranking.

## Prerequisites

Lognormal distributions, BSM, Monte Carlo and Python. No external data required.

## Thesis outline

1. Average-price contingent claims;

2. Geometric and arithmetic valuation;

3. Fixing conventions and simulation;

4. Economic sensitivities;

5. Limitations.

## Milestones

W1-3: derive geometric price; W4-6: code and validate MC; W7-10: monitoring and window experiments; W11-13: Greek analysis; W14-16: robustness and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
