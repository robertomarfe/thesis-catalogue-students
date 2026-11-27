---
title: Exposure, default and unilateral CVA — focused methods note
---

**D09.04.01 · Currency per forward on one share · Risk-neutral valuation**

## 1. Discounted exposure

For a long forward on a stock paying a continuous dividend yield $q$, let $a=S_0e^{-qT}$ and $b=Ke^{-rT}$. The discounted replacement value at time $t$ is

$$e^{-rt}V_t=a\exp(-\tfrac12\sigma^2t+\sigma W_t)-b.$$

Thus $E(t)=\mathbb E^{\mathbb Q}[e^{-rt}V_t^+]=a\Phi(d_1)-b\Phi(d_2)$, where $\Phi$ denotes the standard normal CDF and

$$d_1=\frac{\log(a/b)+\sigma^2t/2}{\sigma\sqrt t},\qquad d_2=d_1-\sigma\sqrt t.$$

At $t=0$ or $\sigma=0$, use $(a-b)^+$. The exposure defined here is **discounted**: do not discount it again. With independent exponential default of intensity $h$, the continuous benchmark is

$$C=(1-R)\int_0^T E(t)he^{-ht}\,dt.$$

It is nonnegative and vanishes if $R=1$ or $h=0$. An ATM forward with $\sigma=0$ has zero exposure under this specification. The upper-endpoint grid approximation at dates $t_j$ is

$$C_n=(1-R)\sum_{j=1}^n E(t_j)[e^{-ht_{j-1}}-e^{-ht_j}].$$

The difference $C_n-C$ reflects time discretization, not Monte Carlo sampling error. Simulating an independent default clock permits a second estimator; the exact-time exposure benchmark avoids the endpoint approximation. Recovery here applies to positive replacement value, not to notional or a debt face value.

## 2. Adapted Cox intensity

Let $\ell_j=\log(S_{t_j}/S_0)$, $\ell_0=0$, and $\Delta_j=t_j-t_{j-1}$. On interval $j$, fix the intensity at $\lambda_j=b_j\exp(\beta\ell_{j-1})$. It is predictable at the start of the interval. An exponential random variable of mean one, independent of market shocks, supplies the Cox default clock. Conditional survival at node $j$ is

$$G_j=\exp\{-\sum_{i=1}^j\lambda_i\Delta_i\},\qquad G_0=1.$$

\newpage

## 3. Matching the marginal credit curve

On calibration paths indexed by $c$, solve sequentially for nonnegative $b_j$ from

$$\frac{1}{N_c}\sum_c G_{j-1}^{(c)}e^{-b_j e^{\beta\ell_{j-1}^{(c)}}\Delta_j}=e^{-ht_j}.$$

The left side decreases continuously in $b_j$ for finite positive intensities and positive previous weights. Its value at zero equals the preceding fitted survival; its limit at infinity is zero. A bracketed scalar root gives a unique solution for a strictly decreasing target. Reuse the fitted baselines on independent evaluation paths, not the paths used to fit them. For a fixed-baseline comparison set $b_j=h$ without matching. The two comparisons answer different economic questions.

## 4. Conditional estimator and diagnostics

With endpoint exposure $e_j=e^{-rt_j}V_{t_j}^+$, the conditional-on-market-path loss is

$$L=(1-R)\sum_{j=1}^n e_j(G_{j-1}-G_j).$$

Average $L$ on independent evaluation paths; the default probability estimate is $1-\overline G_n$. The conditional estimator integrates out the default clock. A separate exponential-clock draw, first crossing and endpoint payoff gives an independent conditional sampling check, using the same exposure convention. Neither estimator is a continuous-time benchmark at finite grid size.

Report the maximum survival error across all nodes, evaluation-sample standard errors conditional on fitted baselines, paired changes in CVA and uncertainty from independent calibration replications. When the sign of $\beta$ changes, the effect is not inferred from the sign alone: it depends on the exposure, the marginal matching and the path dynamics.

## 5. Notation and code crosswalk

| Symbol | Meaning | Code |
|---|---|---|
| $E(t)$ | Discounted exposure | `forward_epe` |
| $h,R$ | Flat hazard, recovery | `hazard`, `recovery` |
| $\beta,b_j$ | Signed loading, baseline | `beta`, `base` |
| $G_j$ | Path-conditional survival | `surv` |
| $L$ | Conditional discounted loss | `loss` |

Implement the full hazard/volatility grid, independent calibration and evaluation paths, default-clock and grid-refinement checks.
