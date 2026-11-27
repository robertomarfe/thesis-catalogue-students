---
title: "Focused methods — Backtest Overfitting and the Illusion of Predictability"
subtitle: "A10.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

For candidate set $\mathcal M_K$, a development winner is $j^*=\arg\min_{j\in\mathcal M_K}\overline L_{j,dev}$. Evaluate that fixed rule on independent final data. The invalid oracle $\min_{j\in\mathcal M_K}\overline L_{j,test}$ reuses the final test and is deliberately not deployable. Under a no-conditional-mean-predictability null $y_{t+1}=0.005+\sigma_t\epsilon_{t+1}$ with $E_t\epsilon_{t+1}=0$, compare constant and time-varying $\sigma_t$. Use nested candidate sets and paired paths across $K$ to quantify search-size effects and Monte Carlo uncertainty.

## Identification and implementation

Use $y_{t+1}=0.005+\sigma_t\epsilon_{t+1}$, with constant $\sigma_t=0.04$ in the iid null and prespecified conditional-variance dynamics in the second. Compare the development-selected rule on final data against the invalid test oracle; purge immature labels at the boundary. Report paired gap and Monte Carlo standard error, not an independent-samples standard error.

## Research checks

Perturb immature/final targets and ensure development winner is unchanged. Check nested candidate membership, paired common draws, strict boundary purge and same benchmark dates. Oracle never used in deployable policy. Real illustration remains required under original scope.
