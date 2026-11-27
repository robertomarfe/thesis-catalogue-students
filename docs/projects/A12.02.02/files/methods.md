---
title: "Focused methods — Sentiment and the Cross-Section of Anomaly Returns"
subtitle: "A12.02.02 | Theory and implementation conventions"
---

**Purpose.** Understand the theoretical restrictions and plan an independent implementation. This note supplies derivations and conventions, not solved research results.

## Mathematical framework

Conditional alpha $\alpha_i(z)=a_i+c_i z$ in a factor regression that also lets beta depend on lagged sentiment state $z$.

Pin actual sentiment workbook and OSAP return/dictionary revision; choose raw or orthogonalized series and eight signals before outcomes. Use past-only state cutoff and scaling, minimum two-month lag; no RF subtraction. Joint date blocks preserve cross-asset dependence. Multiplicity sensitivity and common dates; factor adjustment is retrospective.

## Research checks

Pin actual sentiment workbook and matching eight OSAP signals/dictionary, state definition and fixed selection. Use lagged states and common months, show alpha=a+c*z and beta interactions, joint date-block uncertainty with familywise/FDR sensitivity and predeclared regime robustness. No data substitution without supervisor approval.
