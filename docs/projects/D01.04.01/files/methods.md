---
title: Exponential Lévy Pricing — Moment Matching and Numerical Checks
subtitle: 'Focused methods supplement | D01.04.01'
---

**Purpose.** This supplement connects the proposal's risk-neutral laws to the pricing routines. It complements rather than replaces the shared F01 methods note. The notation follows the proposal; rates are continuously compounded and maturities are in years.

## 1. Common forward, different laws

Write $F=F_{0,T}=S_0e^{(r-q)T}$ and $D=e^{-rT}$. With $L_T=X_T-T\kappa(1)$, the normalized terminal price is $S_T/F=e^{L_T}$. A European call has value

$$ C(K,T)=DF\,\mathbb E^{\mathbb Q}[(e^{L_T}-K/F)^+]. $$

The martingale correction changes only the first cumulant of $X_T$. When the derivatives exist, the $n$th cumulant of $X_T$ equals $T\kappa^{(n)}(0)$. In particular $\operatorname{Var}(L_T)=Tv$, with $v=\kappa''(0)$.

For VG, $G_T\sim\operatorname{Gamma}(T/\nu,\nu)$ and $W$ is independent of $G$. Conditioning on the clock gives

$$ L_T\mid G_T=g\sim\mathcal N(\theta g-T\kappa(1),\sigma^2g). $$

The moment at $u=1$ requires $1-\nu(\theta+\sigma^2/2)>0$. The standardized third and fourth cumulants scale as $T^{-1/2}$ and $T^{-1}$ respectively (when finite). Thus equal annual variance does not imply equal standardized tail behavior at short maturities.

For Merton, let $N_T$ be Poisson with mean $\lambda T$ and let independent log jump sizes be $J_i\sim\mathcal N(\mu_J,s_J^2)$. The unadjusted log process is $X_T=\sigma_M W_T+\sum_{i=1}^{N_T}J_i$, so

$$\begin{aligned}
\kappa_M(u)&=\tfrac12\sigma_M^2u^2+\lambda(e^{u\mu_J+u^2s_J^2/2}-1),\\
L_T\mid N_T=n&\sim\mathcal N(n\mu_J-T\kappa_M(1),\sigma_M^2T+ns_J^2).
\end{aligned}$$

Use $\sigma_M^2=v-\lambda(\mu_J^2+s_J^2)$, requiring nonnegative residual diffusion variance. For the Gaussian comparison, $L_T\sim\mathcal N(-Tv/2,Tv)$. These are three different laws with the same forward and annual log-return variance.

\newpage

## 2. Conditional pricing

For $L_T\mid A=a\sim\mathcal N(m_a,w_a)$, define the conditional arithmetic forward $F_a=F\exp(m_a+w_a/2)$. Let $\Phi$ be the standard normal cumulative distribution function. Then

$$\begin{aligned}
C_a&=D\{F_a\Phi(d_1)-K\Phi(d_2)\},\\
d_1&=\frac{\log(F_a/K)+w_a/2}{\sqrt{w_a}},\quad d_2=d_1-\sqrt{w_a}.
\end{aligned}$$

At $w_a=0$, take $C_a=D(F_a-K)^+$. The unconditional call price is $\mathbb E[C_A]$. For VG, integrate over the gamma clock (or separate the stock and strike terms using the exponential tilt). For Merton, sum over Poisson counts with a truncation check; a small omitted probability alone does not bound the stock-weighted price tail. Your implementation uses these ideas rather than assuming that a mixture has a single Black–Scholes volatility.

## 3. From mathematical symbols to code

| Symbol | Meaning | Routine argument |
|:--|:--|:--|
| $\theta,\sigma,\nu$ | VG drift, diffusion, clock scale | `theta, sigma, nu` |
| $\lambda,\mu_J,s_J$ | jump intensity, log-jump mean and SD | `lam, m, s` |
| $\sigma_M$ | Merton diffusion volatility | `sigma` in `merton_call` |
| $v$ | annual log-return variance | derived; not a price input |
| $k$ | forward log-moneyness | `log(K/F)` |

Implement the three pricing laws independently, then design independent references and maturity/convergence comparisons.

## 4. Acceptance checks

Check the martingale, price bounds and put–call parity $C-P=D(F-K)$. The call must be nonincreasing and convex in $K$; unequal strike spacing requires slope comparisons rather than raw second differences. Check convergence as integration tolerance tightens or as the jump-count cutoff expands. For small $\nu$ compare VG with the corresponding Gaussian limit at fixed $\theta,\sigma$; a separate matched-variance experiment may change these parameters. Inversion uncertainty scales approximately as price error divided by vega, so very low-vega quotes must be flagged. Compare independent numerical error with economically meaningful price and smile differences. No full-text review or empirical calibration is claimed.
