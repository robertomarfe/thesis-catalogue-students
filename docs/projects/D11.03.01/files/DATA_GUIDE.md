# Data and model setup | D11.03.01

**Current data gate: not_required.** No actual external input bytes are supplied or validated.

## Simulation specification

Five or nine terminal stock states (e.g. 60,80,100,120,140), S0=100, gross risk-free return 1.02. Choose a strictly positive generating Q with E_Q[S_T]=102 (e.g. five-state probabilities 0.15,0.20,0.25,0.20,0.20 yield 102); generate consistent bond, stock and call prices by discounting. Claim payoff e.g. digital 1{S_T>=110} times 100 or call strike 110. Add traded calls strikes 90 and 120 sequentially. For quote uncertainty use explicitly defined bid-ask inequalities with consistent mid prices. Use scipy.optimize.linprog and report numerical tolerances.

## Input construction and acceptance

Record a parameter table in annualized decimal units, deterministic seed policy, independent reference method, admissibility checks and failed configurations. Retain the distinction between a simulated risk-neutral economy and any physical scenario. Optional external context does not change the synthetic core.

## Design-specific acceptance

Verify primal/dual matching, strict feasibility separately, and nested intervals on consistent grids. Report statewise residuals and the role of new payoff directions; do not interpret a failed LP as an economic bound.

## Timing, accounting and units

Specify physical versus risk-neutral probability, discounted versus undiscounted cash flows, maturity and year fractions, and whether rates and spreads are decimals, percentages or basis points. Document default timing and recovery. For empirical panels freeze provider vintage and distinguish observation date, availability and outcome maturity. For finite-state models define the state support, probability mass and numerical tolerance before fitting.

## First-meeting acceptance record

Document actual input rights and original filename, version/date, SHA-256, units and sample or parameter ledger. Preserve rejected cases and missing observations. No automatic approval; if the core input fails, defer or agree an explicit redesign.
