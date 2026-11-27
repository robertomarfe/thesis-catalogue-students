---
title: "Focused methods — Rare Disasters and the Joint Behavior of Equity and Bond Returns"
subtitle: "A03.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For $g=\mu+\sigma\epsilon+JI$ with independent Gaussian $\epsilon$ and Bernoulli $I$, $E[e^{kg}]=e^{k\mu+k^2\sigma^2/2}(1-p+pe^{kJ})$.

Matching the log mean requires $\mu=\bar g-pJ$; matching the log variance requires $\sigma^2=\bar v-p(1-p)J^2\geq0$. Reject infeasible cells. With CRRA $m=\beta e^{-\gamma g}$, a real safe unit costs $E[m]$, a defaultable claim costs $E[m(1-I+\delta I)]$, and a nominal unit costs $E[m e^{-\pi}]$ in real units. For iid dividend growth $G_D$, $q_D=E[mG_D]$ and $P_D/D=q_D/(1-q_D)$ only when $q_D<1$. Separate no-disaster sample moments from unconditional moments.

## Research checks

Report ordinary variance required by total variance law before solving, regime probabilities and q_d, q_f and payoff prices. Check p=0 and deterministic-mixture exact values, then stratified simulation with disaster counts; compare fixed-mean and feasible fixed-variance designs. Show conditional-on-no-disaster versus unconditional premium without labeling one a population estimate.
