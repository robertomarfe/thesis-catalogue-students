---
title: "Focused methods — Return Predictability and the Joint-Hypothesis Problem"
subtitle: "A11.04.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## A positive pricing candidate

Let $R_f>0$, $s>0$ and $|\mu(z)|<s$ in both states, with $R_f+\mu(z)-s>0$. Conditional on $z$, $\epsilon$ is symmetric with zero mean and unit second moment. A normalized affine candidate is $m=(1-a(z)\epsilon)/R_f$. Bill pricing follows from symmetry; imposing $E_t[m(R-R_f)]=0$ requires choosing $a(z)$ to offset $\mu(z)$. Derive this coefficient, check positivity, and independently verify the gross stock and bill restrictions for both states. Compare with $m_0=1/R_f$.

The two maintained interpretations use the same return paths. A predictive regression depends only on those paths and observed state, not on which candidate kernel is tested. Additional restrictions on consumption exposure or admissibility may distinguish candidates; a reduced-form distortion is not a solved behavioral equilibrium.

## Research checks

Preserve 5,000 common samples at the specified 80/200 horizons, positivity and conditional moments, and prespecified noisy proxies. Compare paired inference, and distinguish a failure of the constant kernel from an identification of market inefficiency.
