---
title: Swaption Pricing and the Impact of Yield Curve Volatility
---

**D07.03.02 · Derivatives · Synthetic data · Difficulty 3/3 · 16 weeks**

Current research proposal. Supervisor approval and applicable data clearance remain pending.

## Motivation

The discount curve determines the present value of deterministic cash flows, but not the distribution of future swap rates. A model can match today's discount factors exactly and still leave material uncertainty about the value of an option on a swap. This project studies how the level and persistence of rate volatility affect optionality and hedging across expiry and tenor, holding the initial curve fixed.

## Research question

How do volatility level and mean reversion affect European payer swaption prices and hedge sensitivities across expiry and tenor in a one-factor Hull–White model fitted to consistent initial yield curves?

## Model and payoff

Let $P(t,T)$ denote the zero-coupon bond price. The short rate is $r_t=x_t+\varphi(t)$, with $dx_t=-a x_t\,dt+\sigma\,dW_t^{\mathbb Q}$ and $x_0=0$. The deterministic shift $\varphi$ fits the initial discount curve; $a$ and $\sigma$ govern future uncertainty, not the curve-fit residual. For exercise date $u$ and fixed-leg dates $T_1,\ldots,T_m$ with accruals $\alpha_i$, define

$$A_u=\sum_{i=1}^{m}\alpha_iP(u,T_i),\qquad S_u=\frac{1-P(u,T_m)}{A_u}.$$

A physically settled payer swaption of unit notional has exercise value $A_u(S_u-K)^+$ (the value of entering the swap, not an assumed cash settlement), where $K$ is the contractual fixed rate. The one-factor model permits Jamshidian's decomposition into bond puts for nonnegative coupon weights. An independent discounted Gaussian simulation is the numerical reference. No factor-correlation parameter exists in the one-factor model.

## Experimental design

Use a flat 2% curve and an upward synthetic curve, annual payments, expiries of 1, 2 and 5 years and tenors of 2, 5 and 10 years. Compare ATM and $\pm50$ bp strikes, retaining nonnegative $K$. Consider $a\in\{0.03,0.10,0.30\}$ per year and $\sigma\in\{0.005,0.01,0.02\}$ in rate units per square-root year. Start with 100,000 exact Gaussian joint draws; assess precision. Optional GSW curves illustrate curve inputs, not swaption quotes.

\newpage

## Applied research programme

1. **Build a consistent curve.** Compute initial discount factors, forward swap rates and annuities. Confirm exact curve fit for each parameter pair.
2. **Validate the pricer.** Derive Jamshidian's exercise root and bond-option decomposition. Compare with independent discounted simulation; check payer--receiver parity and the zero-volatility limit.
3. **Compare expiry and tenor.** Report prices per unit notional, normal implied volatilities when a finite solution exists and simulation uncertainty. Distinguish rate basis points from price basis points.
4. **Measure sensitivities.** Compute vega and at least one curve sensitivity, plus mean-reversion sensitivity. Hold contractual strike fixed across bumps; refit the deterministic shift when the curve changes. Declare bump units and test stability.
5. **Assess identification.** Match one ATM swaption price at alternative mean-reversion parameters and compare other contracts. Discuss why a curve fit or one quote alone does not identify volatility dynamics.

## Deliverables and acceptance

Provide curve-fit and parity tests, an expiry--tenor price and normal-volatility grid, a comparison with independent Monte Carlo including error bars, and fixed-strike sensitivities. Work in a stylized single-curve setting. Do not interpret synthetic prices as observed market premiums or cash-settled payoffs.

**Minimum viable thesis.** One-factor Hull–White fitted to two synthetic curves, analytic-versus-independent Monte Carlo check, expiry–tenor price and volatility sensitivity grid, and at least one vega and one key-rate or parallel-curve sensitivity with a declared bump and recalibration convention. No external swaption quotes required.

Optional G2++ extension: only after supervisor approval, match the initial curve and one ATM quote, then study correlation and slope risk under a genuinely two-factor model.

## Work plan and core reading

Weeks 1--3: swap/annuity and Gaussian model; 4--6: curve and pricer; 7--9: MC; 10--12: grids and sensitivities; 13--16: identification and writing. Prerequisites: fixed income, Gaussian diffusions, option pricing, Python. Jamshidian (1989), *Journal of Finance* 44, 205--209; Hull and White (1990), *Review of Financial Studies* 3, 573--592; Brigo and Mercurio (2006), *Interest Rate Models: Theory and Practice*, Springer. See the original reading guide; no new full-text check is claimed.
