# Research plan | D04.03.01

## Study design and independent work

Optimize calendars only, unlike D04.03.02. Include opening and liquidation, matched initial premium and paired paths. Never select the risk criterion from final test losses.

## Required tasks

1. Implement BSM delta and cash-account ledger; verify frictionless mean error under Q within MC uncertainty and decreasing discretization error.

2. Compute cost, P&L, variance and turnover by strategy on common paths; discount all cash-flow cost/P&L measures to time zero.

3. For lambda=0.25, 1, 2 choose the loss-minimizing frequency using training only, then evaluate selected and fixed policies on independent test paths. Plot efficient cost-risk frontiers.

4. Stress sigma=10%, 40%, in/out-of-money strikes and a misspecified realized sigma; assess changes in policy ranking.

## Required exhibits

Worked single-path cash ledger; P&L distributions and quantiles; cost-risk frontier per cost regime; optimal frequency heatmap by c and lambda; out-of-sample table with MC confidence intervals. Discuss why an optimum is conditional rather than universal.

## Robustness

Report costs with/without liquidation to expose convention effects; use independent seeds and paired comparisons; distinguish fixed-volatility hedging from true-volatility hedging in misspecification. Check gamma exposure near expiry and tail losses. A cost-free limit should not produce a large nonzero optimal error solely from accounting bugs.

## Minimum viable thesis

Validated self-financing ledger, frequency grid with at least three positive cost levels, prespecified risk-cost objective, independent evaluation, and economically interpretable trade-off. The student need not discover a unique optimum at every grid point.

## Optional extension

Compare no-trade-band hedging or a stochastic-volatility path generator; do not mix this with empirical transaction-cost estimation without suitable quotes.

## Prerequisites

BSM, stochastic simulation, Greeks, basic optimization and Python. No derivatives or bid-ask history required.

## Thesis outline

1. Replication and market frictions;

2. Discrete hedging and cost accounting;

3. Simulation and policy selection;

4. Risk-cost trade-offs and validation;

5. Model risk and conclusion.

## Milestones

W1-3: derive replication and discrete cash flows; W4-6: validate one-path and many-path ledger; W7-10: run cost/frequency experiment and choose on training paths; W11-13: independent evaluation and stress tests; W14-16: document and reproduce findings.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
