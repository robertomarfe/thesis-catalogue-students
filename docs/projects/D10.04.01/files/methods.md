---
title: "Focused methods — Currency Option Pricing and Interest Rate Differentials"
subtitle: "D10.04.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Two rates and option sensitivities
For $S$ in domestic per foreign units, deterministic rates $r_d,r_f$, and volatility $\sigma$, a European call costs
$$C=Se^{-r_fT}\Phi(d_1)-Ke^{-r_dT}\Phi(d_2),$$
where $d_1=(\log(S/K)+(r_d-r_f+\sigma^2/2)T)/(\sigma\sqrt T)$ and $d_2=d_1-\sigma\sqrt T$. Put-call parity is $C-P=Se^{-r_fT}-Ke^{-r_dT}$. Spot delta is $e^{-r_fT}\Phi(d_1)$; domestic and foreign rhos at fixed contract are $TK e^{-r_dT}\Phi(d_2)$ and $-TS e^{-r_fT}\Phi(d_1)$. Matched K/F changes the contract across rate cases and is not a fixed-strike Greek.

## Foreign accrual
Under domestic pricing probabilities $dS/S=(r_d-r_f)dt+\sigma dW^{\mathbb Q_d}$. At time $t$, a foreign money-market unit has domestic value $S_t e^{r_ft}$, so a position replicating spot delta holds $\Delta_t e^{-r_ft}$ units. Domestic cash accrues at $r_d$; account for foreign accrual and self-financing at each rebalance. Optional spot/rate proxies do not provide observed market option prices.

## Research checks

Check parity, fixed-strike sensitivities and self-financing ledger. Separate matched moneyness comparisons from Greeks. Keep quote orientation and foreign accrual explicit.
