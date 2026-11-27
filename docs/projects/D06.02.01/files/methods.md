---
title: "Focused methods — The Early Exercise Premium of American Options"
subtitle: "D06.02.01 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Exercise and carry
Use CRR multipliers $u=e^{\sigma\sqrt h}$, $d=1/u$, and $p=(e^{(r-q)h}-d)/(u-d)$ in $[0,1]$. Discounted continuation is $e^{-rh}[pV_u+(1-p)V_d]$. American value maximizes this and intrinsic payoff; European value only continues. Derive the recursion with identical terminal payoffs and discounting. The premium is the same-grid price difference, with European BSM error reported separately.

## Interpreting boundaries
For a non-dividend-paying stock and nonnegative rates the standard American call has no positive early-exercise premium. Dividends may make exercise valuable; positive rates favor earlier receipt of a put strike. These are conditional arguments, not universal signs. Compare at matched time to expiry and positive intrinsic value. A pricing-measure exercise frequency is not a physical frequency.

## Research checks

Use adjacent lattice refinements, verify q=0 with nonnegative r and the maturity limit. Report boundary resolution separately from price precision. Discrete dividends require different cashflow treatment.
