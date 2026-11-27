---
title: "Rare Disasters and the Joint Behavior of Equity and Bond Returns"
subtitle: "Research proposal | A03.04.01"
---

**Asset pricing · Consumption-based asset pricing and equity term structures · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

Disasters affect both the pricing kernel and cash-flow payoffs. The same shock can raise the price of a safe real payoff while reducing the value of an exposed dividend or defaultable payoff.

## Research question

How do disaster probability, severity and cash-flow exposure jointly affect equity premia, real safe rates and returns on defaultable or nominal bond claims?

## Economic mechanism

For $g=\mu+\sigma\epsilon+JI$ with independent Gaussian $\epsilon$ and Bernoulli $I$, $E[e^{kg}]=e^{k\mu+k^2\sigma^2/2}(1-p+pe^{kJ})$.

## Research design

IID disaster mixture, mean-matched and feasible variance-matched cases, distinct dividend, safe, defaultable and nominal payoffs; independent MC.

Report ordinary variance required by total variance law before solving, regime probabilities and q_d, q_f and payoff prices. Check p=0 and deterministic-mixture exact values, then stratified simulation with disaster counts; compare fixed-mean and feasible fixed-variance designs. Show conditional-on-no-disaster versus unconditional premium without labeling one a population estimate.

\newpage

## Required exhibits

Closed-form derivation; parameter/existence maps; premium and safe-rate tables; bond recovery and inflation sensitivities; sample uncertainty.

## Minimum viable thesis

Exact CRRA mixture, distinct dividend and safe claims, one risky bond payoff, disaster comparative statics and MC check.

## Scope and feasibility

Do not conflate disaster probability with risk-neutral probability, nominal with real safe rate, or consumption claim with equities. i.i.d. model has no predictable time variation; parameter grid is illustrative not calibrated evidence. Report nonexistence rather than clipping ratios.

**Prerequisites:** Consumption-based pricing, probability mixtures, numerical simulation, Python.

**Optional extension:** Introduce two-state disaster probability with Markov transitions and solve finite-state pricing recursion; consider EZ only after baseline.

## Milestones

W1-3: theory; W4-6: exact moments/prices; W7-9: scenario grid; W10-12: bond and finite samples; W13-16: reproducibility and writing.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
