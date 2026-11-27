---
title: Epstein-Zin Preferences and the Separation of Risk Aversion from Intertemporal Substitution
---

**A03.03.01 / Asset pricing / Synthetic / Difficulty 2/3 / 16 weeks / No mandatory external data**

Current research proposal. Not approved for assignment.

## Motivation

Time-additive power utility links relative risk aversion to the willingness to substitute consumption over time. Recursive utility breaks this restriction, yet its pricing implications depend on the distribution of consumption growth and on continuation wealth. The project isolates preference effects in an iid economy before introducing a predictable growth state, rather than treating a richer calibration as evidence of a particular economic mechanism.

## Research question

How do risk aversion and the elasticity of intertemporal substitution independently affect equilibrium prices, and what changes when consumption growth becomes predictable?

## Model and economic intuition

Let $G_{t+1}=C_{t+1}/C_t$, $\beta$ be the discount factor, $\gamma$ risk aversion and $\psi$ the elasticity of intertemporal substitution. Define $\theta=(1-\gamma)/(1-1/\psi)$ away from singular preference limits. With ex-dividend consumption wealth $w_i=W_t/C_t$ in state $i$, the gross wealth return and stochastic discount factor are

$$R^w_{ij}=G_{t+1}\frac{1+w_j}{w_i},\qquad M_{ij}=\beta^\theta G_{t+1}^{-\theta/\psi}(R^w_{ij})^{\theta-1}.$$

The Euler condition $\mathbb E_i[M R^w]=1$ identifies the nonlinear wealth equation. In the iid case a constant wealth ratio admits a closed form; in a Markov economy the continuation value introduces an additional state-dependent risk channel.

## Data and research design

Use annual log growth with mean 2% and SD 2% in the iid economy; beta 0.96, 0.98, 0.99; gamma 2, 5, 10; psi 0.5, 1.5, 2.5. For two states use growth means 0.005 and 0.035, stay probability 0.9 and matched conditional SD; disclose the change in unconditional variance, then match it as a sensitivity. Reject nonfinite wealth and dividend values explicitly.

\newpage

## Applied research programme

1. Derive the iid formulas and distinguish log and arithmetic expected excess returns.
2. Compute preference grids, including admissibility and the CRRA restriction.
3. Solve the two-state wealth equation using two independent numerical methods.
4. Price bills and, optionally, a leveraged dividend claim; report Euler residuals and spectral margins.
5. Interpret the independent preference effects and compare a matched-variance iid economy.

## Deliverables and acceptance

Derivation, preference grids, state-dependent prices, equilibrium residuals and admissibility diagnostics. Wealth is a claim to consumption, not automatically an observed stock-market portfolio. Optional: public consumption moments or a persistent Gaussian expected-growth state.

**Minimum viable thesis.** Iid closed form and two-state solution with CRRA check, preference grids and equilibrium verification; leveraged claim optional. Distinct from A03.03.02's long-run risk calibration.

## Work plan

Weeks 1--3: theory and source review; 4--6: data or numerical setup; 7--10: core implementation; 11--13: robustness; 14--16: writing and replication. Preserve the more detailed canonical milestones.

## Core reading

Epstein and Zin (1989); Weil (1989); Bansal and Yaron (2004). Verify full citations against the inherited reading guide and the versions read.
