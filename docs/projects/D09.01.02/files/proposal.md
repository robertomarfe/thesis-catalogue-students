---
title: "Structural Credit Models with Early Default"
subtitle: "Research proposal | D09.01.02"
---

**Derivatives · Credit risk and incomplete markets · Level 3/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

A covenant can trigger default before debt matures even if the firm later recovers. Short maturity spreads therefore depend on the path of assets, not only the terminal distribution. Distinguish this effect from changes in recovery timing and contractual loss.

## Research question

How do default-barrier level and recovery convention alter the credit spread term structure relative to a maturity-only Merton benchmark?

## Economic mechanism

With $H<V_0$, define $\tau_H=\inf\{t:V_t\le H\}$ and a separate maturity default event $V_T<F$ conditional on survival.

## Research design

Implement the specified constant barrier GBM and recovery at maturity, comparing Merton and early-default prices. Use exact endpoints, conditional Brownian bridges and a first-passage probability benchmark. Refine monitoring and keep the contractual recovery rule fixed.

Show the analytic hit check, bridge versus endpoint-only monitoring and common-path paired intervals. Compare the maturity-only benchmark under identical terminal inputs. Preserve unsuccessful or high-error grid cases and quantify both default timing and loss effects.

\newpage

## Required exhibits

Survival validation, debt price and spread curves, default-timing decomposition, recovery and monitoring sensitivity table.

## Minimum viable thesis

Merton benchmark, one early-default model with explicit recovery, analytic hit check, bridge versus discrete monitoring, spread curves for two barriers and three volatilities. Distinct from maturity-only default thesis.

## Scope and feasibility

Under baseline R*F<=H does not ensure pathwise smaller payout than terminal min(V_T,F) after an early hit; do not impose monotonic comparison to Merton for positive recovery. At R=0 barrier debt is <= Merton pathwise. Q default probability is not historical frequency. No empirical credit-spread calibration or equity/debt joint equilibrium claimed.

**Prerequisites:** Stochastic calculus, first-passage distributions, option pricing and Python.

**Optional extension:** Use a time-dependent covenant barrier or calibrate to synthetic equity and debt quotes with parameter-identification checks.

## Milestones

W1-3: Merton and barrier theory; W4-6: hit probability and bridge code; W7-9: debt prices and curves; W10-12: recovery/timing robustness; W13-16: interpret and write.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
