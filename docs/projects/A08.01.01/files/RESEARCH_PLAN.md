# Research plan | A08.01.01

## Study design and independent work

Run paired known-moment cells: true/estimated mean crossed with true/estimated covariance, same random draws and out-of-sample returns, verify oracle objective and feasibility. For actual data record long-only weights, exact OOS dates, drifted trades, net wealth and CE units; date blocks and estimation uncertainty; report failed cells.

## Prespecified implementation

Freeze N=10 positive-definite monthly covariance and heterogeneous means before simulation; compare oracle, estimated mean only, estimated covariance only and joint estimates at T=24/60/120/240, 1,000 paired replications, independent test paths. Report true-moment utility loss (oracle minus fitted policy) and realized utility separately. In French 10-industry value-weighted panel, use total returns for wealth, excess moments for allocation and matched RF for Sharpe; common origins after 120 months, long-only, gamma=3/5/10, 60/120 histories. Use ledger with scale=1 and 0/10/25bp; disclose initial weights and first trade. Paired block uncertainty with refits where estimating model uncertainty.

## Required tasks

1. Derive unconstrained solution and implement constrained optimizer; check weight sum, feasibility and KKT/objective against reference.

2. Simulate samples with known moments; estimate oracle loss separately for mean-only, covariance-only and joint errors.

3. Run historical rolling backtest using data through t only to set weights for t+1; compute drifted pretrade weights and turnover.

4. Compare annualized CE, volatility, Sharpe using matched RF, drawdown, turnover and cost scenarios (e.g. 0/10/25 bp per dollar traded).

5. Assess paired uncertainty by block resampling and sensitivity to rolling window, gamma and separate industry or size/value panel.

## Required exhibits

Oracle regret plots, simulated weight dispersion, historical portfolio weight/wealth paths, risk/CE and turnover table, optimization failure diagnostics and reproducible timestamp ledger.

## Robustness

No use of future returns in estimation or tuning. Use one-way traded notional convention explicitly (if turnover=0.5*sum absolute trades, convert costs accordingly). Risky portfolios use total returns; same cost schedule and rebalance. Published portfolio returns do not establish implementable net strategy returns. Distinguish mean estimation from covariance shrinkage thesis A08.01.02.

## Minimum viable thesis

Known-moment simulation isolating mean/covariance error, matched rolling 1/N, GMV and mean-variance backtest, weight stability and CE comparison with uncertainty.

## Optional extension

Compare shrinkage of mean toward common mean, without turning thesis into a covariance-shrinkage comparison.

## Prerequisites

Portfolio theory, covariance estimation, convex optimization and Python SciPy/cvxpy.

## Thesis outline

1. Mean-variance and estimation risk;

2. Oracle and estimated portfolio rules;

3. Simulation and historical protocol;

4. Estimation regret and realized performance;

5. Robustness and economic implications.

## Milestones

W1-3: portfolio theory and optimizer; W4-6: clean returns and validate weights; W7-9: oracle simulations; W10-12: rolling backtest; W13-16: costs, uncertainty and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
