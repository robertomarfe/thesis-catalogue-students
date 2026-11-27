# Research plan | A11.01.01

## Required tasks

1. Derive projection, orthogonality and normalization; verify pricing residual and rank.

2. Generate incomplete/complete economies, compute minimum-norm and positive alternative SDFs, show common pricing.

3. Add assets sequentially, compare projection variance, maximum attainable Sharpe and equality conditions.

4. Construct cases where unrestricted minimum-norm SDF is negative despite an arbitrage-free positive alternative; solve constrained minimum-norm and compare.

5. Perturb payoffs/prices to examine numerical conditioning and redundant assets; test invariance to basis change and scaling.

## Required exhibits

Payoff/price tables; projection and null-space diagnostics; SDF dispersion and Sharpe frontier; positive feasibility and conditioning plots.

## Robustness

Use probability-weighted inner product. Distinguish a minimum-norm linear SDF from true structural marginal utility; positivity matters for arbitrage but is not automatic. Bound equality requires traded span and unconstrained portfolio assumptions. Distinct from empirical HJ bound A11.02.01 and beta mapping A11.01.02.

## Minimum viable thesis

Two nested finite-state economies, exact pricing and projection, null-space alternatives, positivity and Sharpe geometry with numerical verification.

## Optional extension

Compare constrained SDF with entropy-minimizing kernel or apply projection to public portfolio moments, with estimation-error caveat.

## Prerequisites

Linear algebra, probability, asset pricing and convex optimization in Python.

## Thesis outline

1. Pricing kernels and payoff space;

2. Projection geometry;

3. Synthetic economies;

4. Risk-premium and positivity results;

5. Implications.

## Milestones

W1-3: theory and proof; W4-6: finite-state solver; W7-9: nested spans; W10-12: positivity/conditioning; W13-16: code and thesis.

At every meeting submit your own code, inputs/parameter ledger, outputs and unresolved issues. Report null results and failed cases.
