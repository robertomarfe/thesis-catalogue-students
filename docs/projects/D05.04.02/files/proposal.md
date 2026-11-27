---
title: Estimating Option Greeks with Monte Carlo Methods
subtitle: 'Research proposal | D05.04.02'
---
**Derivatives · Numerical methods · 16 weeks · Level 2/3**  
**Data:** synthetic. **Status:** current draft; not approved for assignment.

## Motivation

Hedging and risk management require sensitivities of derivative values, not just accurate prices. Differentiating a simulated price introduces a second numerical problem: the estimator must resolve a change in the payoff without allowing sampling noise to overwhelm it. For a digital option, the payoff jumps at the strike; differentiating individual sample paths misses that jump. An arithmetic Asian option provides a different challenge because every fixing affects the payoff. Comparing estimators across these contracts reveals when a theoretically valid sensitivity can be estimated efficiently.

## Research question

Which of bump-and-revalue, pathwise and likelihood-ratio estimators delivers the best accuracy-cost trade-off for delta and vega of European calls, digitals and Asian options?

## Model and economic mechanism

Let $S_0$ be spot, $K$ strike, $T$ maturity, $r$ the continuously compounded risk-free rate, $q$ the dividend yield and $\sigma$ annual volatility. Under the risk-neutral measure $\mathbb Q$,
$$S_t=S_0\exp\{(r-q-\tfrac12\sigma^2)t+\sigma W_t\},$$
where $W$ is a standard Brownian motion. The price of payoff $H$ at $T$ is $V=e^{-rT}\mathbb E^{\mathbb Q}[H]$. Delta is $\partial V/\partial S_0$ and vega is $\partial V/\partial\sigma$ (per unit volatility). Study European calls, cash-or-nothing digitals paying one unit, and arithmetic Asian calls with $A=m^{-1}\sum_{j=1}^m S_{t_j}$ and payoff $(A-K)^+$.

Bump-and-revalue approximates the derivative using perturbed prices and common random numbers. Pathwise differentiation exploits a continuous payoff with an almost-everywhere derivative. Likelihood-ratio differentiation instead weights the payoff by a density score, which permits discontinuous payoffs. The methods note derives the scores, including the joint density of the Asian fixing vector. Compare finite-difference bias with sampling uncertainty; a small bump need not be an efficient choice, particularly for digitals.

## Experimental design

Use $S_0=100$, $r=2\%$, $q=1\%$, $\sigma=20\%$, $K\in\{80,100,120\}$ and $T\in\{0.25,1\}$ years. Use twelve arithmetic Asian fixings and the geometric Asian control. Start with relative central bumps from $10^{-1}$ to $10^{-5}$. Reuse random numbers within a bump pair but use independent seeds for repeated experiments and independent reference simulations. Report the Asian reference's uncertainty; do not treat it as exact.



## Research tasks and deliverables

1. Derive valid estimators and independent analytic European sensitivities. Explain why naive digital pathwise differentiation is invalid; do not rank it as a legitimate estimator.
2. Implement central differences, pathwise estimators and likelihood-ratio estimators. Use common random numbers for bumps, and assess antithetic controls with appropriate paired uncertainty.
3. Compare bias, empirical standard deviation, RMSE, confidence interval coverage and runtime over several path budgets and independent seeds. Report cost-normalized RMSE with the same hardware and timing convention.
4. Study bump sensitivity, short maturities and out-of-the-money cases. For one arithmetic Asian call, obtain a separate high-precision reference using independent simulations and controlled bump bias. Derive the score of the joint fixing density and the vega of every fixing.

Required outputs: estimator bias/variance table, RMSE versus path count and time, bump-size sensitivity, and reference diagnostics. Distinguish approximation error, Monte Carlo error and reference uncertainty; state whether vega is per unit volatility or per volatility point. No estimator is presumed universally superior.

## Minimum viable thesis and acceptance criteria

European call and digital delta and vega, and one arithmetic Asian call (12 fixings, one strike and maturity), using bump-and-revalue, pathwise and likelihood-ratio estimators where valid. Include analytic European benchmarks, an independently generated numerical Asian reference with uncertainty and bump-size diagnostics, repeated seeds and a cost-normalized RMSE comparison. Explicitly report the invalid digital pathwise estimator rather than rank it.

## Research plan and scope

| Weeks | Deliverable |
|:--|:--|
| 1–3 | Derive estimators and European references |
| 4–6 | Implement and validate the European experiment |
| 7–9 | Repeated-seed efficiency comparisons |
| 10–12 | Asian reference, sensitivity and robustness |
| 13–16 | Interpretation, reproducibility and writing |

Prerequisites: Black–Scholes, calculus, probability, Monte Carlo and Python. Optional extension: conditional smoothing or automatic differentiation for appropriate payoffs. Before assignment, agree on estimator conventions, tolerances and the reference budget.

## Core reading

Broadie and Glasserman (1996), *Management Science*, 42, 269–285. Estimating derivatives by simulation.  
Glasserman (2004), *Monte Carlo Methods in Financial Engineering*. Springer.  
Giles (2009), *Monte Carlo and Quasi-Monte Carlo Methods 2008*. Vibrato sensitivities. Consult the existing reading guide for routes and metadata; full-text verification remains pending.
