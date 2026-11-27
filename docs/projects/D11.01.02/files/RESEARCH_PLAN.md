# Research plan | D11.01.02

## Study design and independent work

Check all three measure transformations at every node, local payoff rank, transition sums, price equality and replication residuals. Extend only after the two-period benchmark is independently reproduced.

## Required tasks

1. Verify discounted stock and bond martingales under Q^B at every node.

2. Derive local and full-path forward-measure probabilities and check sums and positivity.

3. Price claims by backward induction under B and T-bond and compare node-by-node, including replication where one-step payoffs span the binary branches.

4. Repeat using stock numeraire and test sensitivity to rate/stock dependence by changing terminal payoff tree or r states.

5. Deliberately omit the payoff-unit conversion or density and quantify the resulting pricing inconsistency as a diagnostic.

## Required exhibits

Annotated tree, transition and density tables, claim-price invariance residuals, replication check and rate-dependence illustrations.

## Robustness

Numeraires must be strictly positive self-financing traded assets. B is path dependent with stochastic rates; no arbitrary renormalization or P probabilities substituted for Q. Nonrecombination is acceptable; verify local martingales before computing measures.

## Minimum viable thesis

Complete two-period example, money-market/forward/stock measure transformations, at least three claim types, nodewise pricing equality and replication residuals below numerical tolerance.

## Optional extension

Use a longer short-rate tree and price a bond option or caplet with an appropriate forward measure.

## Prerequisites

Conditional probability, discrete-time asset pricing, linear algebra and Python.

## Thesis outline

1. Numeraires and martingale pricing;

2. Discrete change of measure;

3. Consistent stock/bond tree;

4. Numerical invariance and failure modes;

5. Forward-measure applications.

## Milestones

W1-3: derive pricing and RN density; W4-6: build and check tree; W7-9: measure changes and claims; W10-12: rate-dependence and diagnostics; W13-16: proofs, code and writing.

At each meeting submit your independent code, parameter/input ledger, results and unresolved issues. Document failures and null findings.
