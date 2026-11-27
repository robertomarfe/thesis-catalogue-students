---
title: The Stochastic Discount Factor and the Geometry of Risk Premia
subtitle: 'Research proposal | A11.01.01'
---

**Asset pricing · Finite-state economies · 16 weeks · Level 1/3**  
**Data:** synthetic; optional public-factor illustration. **Status:** current draft; not approved for assignment.

## Motivation

Asset prices identify the component of the stochastic discount factor (SDF) that lies in the span of traded payoffs, but they generally do not identify the entire SDF in incomplete markets. This distinction is economically important: a pricing kernel that exactly matches traded prices need not be unique or even nonnegative. The project uses finite-state economies to connect this identification problem to portfolio efficiency, the Sharpe ratio and no-arbitrage restrictions. Its main contribution is to establish these relationships exactly, rather than to estimate a structural consumption model.

## Research question

How do the payoff span and market incompleteness determine the minimum-norm SDF, the attainable Sharpe ratio and the set of admissible positive pricing kernels?

## Theoretical and methodological framework

Consider $J$ states with probabilities $\pi_j>0$ that sum to one. Let $X\in\mathbb R^{J\times N}$ contain the payoffs of $N$ traded assets (one row per state), let $q\in\mathbb R^N$ be their price vector and define $\Pi=\operatorname{diag}(\pi_1,\ldots,\pi_J)$. An SDF $m\in\mathbb R^J$ prices the assets if

$$X^\top\Pi m=q.$$

Under full column rank, the minimum probability-weighted norm solution is

$$m_*=X(X^\top\Pi X)^{-1}q,\qquad \|m\|_\pi^2=m^\top\Pi m.$$

For redundant payoffs, use a rank-aware pseudoinverse after testing price consistency. Every other solution takes the form $m_*+h$, with $X^\top\Pi h=0$. Adding traded payoffs restricts this set. A riskless unit payoff with price $q_f=1/R_f$ fixes $\mathbb E[m]=q_f$, where $R_f$ is its gross return. For a zero-cost excess payoff $x$ with positive variance,

$$\frac{|\mathbb E[x]|}{\operatorname{SD}(x)}\leq\frac{\operatorname{SD}(m)}{\mathbb E[m]}.$$

The project derives the bound and its equality condition, and distinguishes the unrestricted minimum-norm kernel, the minimum-norm kernel subject to $m\geq0$, and strict positive feasibility. These are different mathematical and economic objects.

## Experimental design

Construct synthetic economies with 4, 8 and 20 states, using both equal and unequal probabilities. Start with a strictly positive reference kernel and price a riskless payoff and one to six risky payoffs consistently. Add payoffs to build nested spans; include a separate complete-market benchmark, redundant assets and nearly collinear payoffs. Set random seeds and record numerical tolerances. Compare weighted least squares, a nonnegative quadratic program and a linear program that tests strict positive feasibility. No external data are required for the core exercise.

## Required analysis and exhibits

1. **Projection.** Derive the pricing and orthogonality restrictions. Report a payoff/price table, rank and residuals for the numerical solution.
2. **Market incompleteness.** Construct incomplete and complete economies; identify null-space directions and show that alternative kernels price the same traded assets.
3. **Portfolio efficiency.** Add assets sequentially. Compare SDF dispersion with the maximum attainable Sharpe ratio and state the conditions for equality.
4. **Positivity.** Construct a strictly positive reference kernel whose unrestricted projection is negative in at least one state. Compare the unrestricted and nonnegative solutions and report the maximum feasible positivity margin.
5. **Conditioning.** Perturb prices and payoffs, introduce redundant assets and test invariance to changes of basis and payoff scaling. Record inconsistent cases rather than silently dropping them.

The main exhibits are a pricing and rank table, a nested-span SDF/Sharpe frontier, state-by-state kernels and a conditioning diagnostic. Use the probability-weighted inner product throughout. Equality of the Sharpe bound assumes the relevant unrestricted traded excess-payoff span, not arbitrary portfolio constraints. A minimum-norm kernel is not identified structural marginal utility. A11.02.01 studies an empirical Hansen--Jagannathan bound; A11.01.02 studies beta representations. Neither is the core exercise here.

\newpage

## Minimum viable thesis and acceptance criteria

Two nested finite-state economies, exact pricing and projection, null-space alternatives, positivity and Sharpe geometry with numerical verification.

Before assignment, verify the matrix orientation, payoff-price consistency, weighted residuals, null-space orthogonality, feasibility margin and rank tolerances. The supplied notebook checks only payoff orientation and probability units. The student's research must construct and compare the economies, document numerical failures and produce independent results.

An optional extension compares the constrained SDF with an entropy-minimizing kernel or illustrates the projection with public portfolio moments. In the latter case, account for estimation error and clear the applicable input gate.

## Work plan and reading

| Weeks | Milestone |
|:---|:---|
| 1--3 | Derive the pricing restrictions and projection result. |
| 4--6 | Implement and verify the finite-state solver. |
| 7--9 | Compare nested spans and the Sharpe frontier. |
| 10--12 | Study positivity and numerical conditioning. |
| 13--16 | Complete reproducible code, exhibits and thesis. |

Suggested thesis structure: pricing kernels and payoff space; projection geometry; synthetic economies; risk-premium and positivity results; implications.

Prerequisites: linear algebra, probability, asset pricing and convex optimization in Python. Read the focused methods note and the core sources below.

**Core reading** (inherited citations; full bibliographic verification remains pending):

- Hansen, L. P., and Jagannathan, R. (1991). Implications of Security Market Data for Models of Dynamic Economies. *Journal of Political Economy*, 99, 225--262.
- Cochrane, J. H. (2005). *Asset Pricing*. Princeton University Press.
- Hansen, L. P., and Richard, S. F. (1987). The Role of Conditioning Information in Deducing Testable Restrictions Implied by Dynamic Asset Pricing Models. *Econometrica*, 55, 587--613.
