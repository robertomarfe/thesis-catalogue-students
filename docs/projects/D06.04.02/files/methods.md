---
title: "Focused methods — Quanto Options and Currency Risk in International Derivatives"
subtitle: "D06.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Currency convention and measure
Let $X$ be domestic currency per foreign unit and $S$ foreign equity in foreign currency. Under domestic $\mathbb Q_d$, $dX/X=(r_d-r_f)dt+\sigma_XdW_X$. For $dS/S=\mu_Sdt+\sigma_SdW_S$, Itô's product rule gives drift of $XS$ equal to $r_d-r_f+\mu_S+\rho\sigma_S\sigma_X$. Equating it to $r_d-q$ implies $\mu_S=r_f-q-\rho\sigma_S\sigma_X$.

## Fixed and random conversion
A quanto pays $k(S_T-K)^+$ in domestic units, with lognormal forward $F_q=S_0e^{\mu_ST}$ and domestic discount. Derive price and spot delta at fixed $k,X_0,K$; check with central bump and pathwise or independently simulated estimates. Random conversion pays $X_T(S_T-K)^+$ and must price at $X_0$ times the foreign option under $\mathbb Q_f$. Zero covariance removes the drift correction, not the discount or conversion distinction. Inverting the quote requires transforming drift, diffusion and measure consistently.

## Research checks

Check the discounted domestic stock martingale and currency units. Hold contractual conversion fixed for delta. Validate random conversion by numeraire invariance; do not use physical correlation as risk-neutral calibration.
