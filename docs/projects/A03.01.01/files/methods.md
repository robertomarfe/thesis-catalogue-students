---
title: "Focused methods — The Equity Premium Puzzle: Theory and Quantitative Evidence"
subtitle: "A03.01.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

With gross consumption growth $G_{t+1}$, power utility implies $m_{t+1}=\beta G_{t+1}^{-\gamma}$ and $E[m R_i]=1$.

For each $\gamma$, the bill Euler equation gives $\beta_b=1/E[G^{-\gamma}R_b]$. Evaluate the market Euler residual at that value, rather than refitting beta for each asset. For $R^e=R_m-R_b$, the exact restriction is $E[R^e]=-\operatorname{Cov}(m,R^e)/E[m]$. This is a mean excess payoff identity even if the bill is risky in real terms. Use compounded nominal gross legs and a common inflation divisor; a quarterly ex post real bill is not a known real safe payoff. Convert annual beta by fourth root and distinguish arithmetic annualization from compound returns.

## Research checks

On a common quarterly calendar report both Euler residuals and beta pricing the bill, then the market residual and covariance identity; resample contiguous joint date blocks. Check compounded nominal gross legs divided by the same inflation ratio and compare beta annualized by beta_q**4. Distinguish arithmetic premium from compound annual growth. Report parameter grid including infeasible beta.
