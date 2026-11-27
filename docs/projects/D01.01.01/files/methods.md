---
title: "Focused methods — The Black-Scholes Model and the Economic Implications of Its Assumptions"
subtitle: "D01.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Replication and local risk
Let $t$ be valuation time, $T$ expiry, and $\tau=T-t$. Write $D=e^{-r\tau}$, $F=S_te^{(r-q)\tau}$, with continuously compounded rate $r$, proportional dividend yield $q$, and volatility $\sigma$. For a continuously traded stock with dividends, a self-financing replicating portfolio holds $C_S$ shares and invests the remainder in the money market. Equating the drift of the derivative and portfolio gives
$$C_t+(r-q)S C_S+\tfrac12\sigma^2 S^2C_{SS}-rC=0.$$
The terminal payoff is $(S_T-K)^+$, where $K$ is strike. With $w=\sigma^2\tau$ and $d_{1,2}=\log(F/K)/\sqrt w\pm\sqrt w/2$, the call price is $D[F\Phi(d_1)-K\Phi(d_2)]$. Here $\Phi$ is the standard normal cdf and $\phi$ its density. Put–call parity is $C-P=D(F-K)$.

## Moment matching and sensitivity units
For $\sigma,\tau>0$, delta is $e^{-q\tau}\Phi(d_1)$ and gamma is $e^{-q\tau}\phi(d_1)/(S\sigma\sqrt\tau)$. Vega is $Se^{-q\tau}\phi(d_1)\sqrt\tau$ per unit decimal volatility; multiply by 0.01 for one volatility point. Rho is $\partial C/\partial r$, and calendar-time theta is $\partial C/\partial t$ at fixed expiry. Derive these remaining Greeks and check signs and units against your own finite differences.

A two-component lognormal mixture with probabilities $p,1-p$, conditional means both $F$, and log variances $a,b$ has $\mathbb E^{\mathbb Q}[S_T^2]/F^2=pe^a+(1-p)e^b$. Match this to $e^w$ by solving for $b$; reject an inadmissible variance. This is **not** matching log-return variance. Compare with independent payoff integration; do not interpret the mixture as a dynamic replication model.

## Research checks

Separate each input perturbation from a change in the terminal law. Hold other inputs fixed for Greeks; for the mixture preserve the forward and arithmetic second moment at every maturity. Report units and distinguish small perturbations from scenario repricing.
