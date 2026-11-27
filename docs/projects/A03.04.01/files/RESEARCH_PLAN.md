# Research plan | A03.04.01

## Study design and independent work

Report ordinary variance required by total variance law before solving, regime probabilities and q_d, q_f and payoff prices. Check p=0 and deterministic-mixture exact values, then stratified simulation with disaster counts; compare fixed-mean and feasible fixed-variance designs. Show conditional-on-no-disaster versus unconditional premium without labeling one a population estimate.

## Prespecified implementation

Use ordinary log growth mu+sigma*z+J*I with p disaster probability; for matched log mean set mu=.02-p*J. Match unconditional log variance only if target variance-p(1-p)J^2>=0, flag infeasible rather than clip. Dividend growth phi times consumption shock with explicit drift; compute wealth D=C separately. Real defaultable unit payoff recovery in disaster and nominal payoff exp(-inflation) distinct; compare safe real claim. Compute joint moments and stock/bond covariance analytically or MC; verify p=0 and selected mixture against independent draws. Full grids and missing-disaster short-sample exercise student-owned.

## Required tasks

1. Derive exact mixture expectations and existence conditions, check p=0 against lognormal CRRA.

2. Compute real risk-free, wealth and dividend claim prices, expected simple returns and volatilities.

3. Vary p, J, gamma and phi, compare matched mean/variance feasible benchmarks.

4. Price real defaultable and nominal claims and examine disaster beta, excess return and stock-bond covariance.

5. Simulate long histories and short samples to assess missing-disaster uncertainty; compare analytic and MC moments with fixed seeds.

## Required exhibits

Closed-form derivation; parameter/existence maps; premium and safe-rate tables; bond recovery and inflation sensitivities; sample uncertainty.

## Robustness

Do not conflate disaster probability with risk-neutral probability, nominal with real safe rate, or consumption claim with equities. i.i.d. model has no predictable time variation; parameter grid is illustrative not calibrated evidence. Report nonexistence rather than clipping ratios.

## Minimum viable thesis

Exact CRRA mixture, distinct dividend and safe claims, one risky bond payoff, disaster comparative statics and MC check.

## Optional extension

Introduce two-state disaster probability with Markov transitions and solve finite-state pricing recursion; consider EZ only after baseline.

## Prerequisites

Consumption-based pricing, probability mixtures, numerical simulation, Python.

## Thesis outline

1. Disaster risk and asset prices;

2. Mixture equilibrium;

3. Cashflow exposures;

4. Quantitative comparative statics;

5. Empirical limitations.

## Milestones

W1-3: theory; W4-6: exact moments/prices; W7-9: scenario grid; W10-12: bond and finite samples; W13-16: reproducibility and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
