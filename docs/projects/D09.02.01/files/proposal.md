---
title: "Reduced-Form Credit Risk and the Term Structure of Default Probabilities"
subtitle: "Research proposal | D09.02.01"
---

**Derivatives · Credit risk and incomplete markets · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A CDS term structure constrains a collection of expected discounted default payments, rather than revealing physical default frequencies. The inverse problem becomes delicate when quotes are noisy or recovery is uncertain. Examine when a nonnegative hazard bootstrap is feasible and when regularization is necessary.

## Research question

Can a parsimonious piecewise-constant intensity curve reproduce synthetic CDS par spreads, and how sensitive are inferred default probabilities to recovery and discretization?

## Economic mechanism

For deterministic hazard $\lambda(t)$, $Q(t)=\exp[-\int_0^t\lambda(u)du]$ and $s(T)=(1-R)\mathcal L(T)/\mathcal A(T)$.

## Research design

Generate the specified four-bucket synthetic CDS curve with quarterly premiums and default accrual. Recover each bucket using nonnegative roots. Reprice all knots; examine noisy quotes, failed roots, recovery changes and the constant-hazard and regularized alternatives.

Report survival curves and repricing residuals in basis points. Compare alternative recovery at fixed quotes, rather than relabeling the physical hazard. Retain infeasible noisy cases and disclose the objective and penalty.

\newpage

## Required exhibits

Hazard, survival and bond-spread curves; CDS repricing table; recovery/noise sensitivity and infeasibility diagnostics.

## Minimum viable thesis

Synthetic four-bucket bootstrap, constant hazard check, repricing and recovery sensitivity with explicit convention. Distinct from structural default projects D09.01.

## Scope and feasibility

Do not silently clip negative hazards while claiming exact fit. CDS accrued premiums, payment schedule and discounting must be consistent. Q survival is not physical default forecast; spread is not pure expected loss in real markets.

**Prerequisites:** Discounting, probability, numerical root finding, credit-risk basics.

**Optional extension:** Stochastic intensity CIR with conditional survival transform; compare synthetic term structures.

## Milestones

W1-3: derivations; W4-6: integration and CDS generator; W7-9: bootstrap; W10-12: stress and bond prices; W13-16: documentation.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
