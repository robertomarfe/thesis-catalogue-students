---
title: "Option Pricing and Hedging in the Presence of Extreme Market Movements"
subtitle: "Research proposal | D01.03.03"
---

**Derivatives · Vanilla pricing and surfaces · Level 2/3**

**Data:** Synthetic core; no mandatory external data. **Status:** current review draft; supervisor approval pending.

## Motivation

When returns jump, a delta hedge is exposed to a finite-price residual rather than only a local diffusion error. A second option may reduce this exposure but introduces financing, sensitivity and position-size constraints. This study evaluates the benefit in tail losses using a common initial premium and common physical scenarios, rather than comparing strategies that start with different capital.

## Research question

How sensitive are hedge losses to rare market gaps, and how much can a second traded vanilla option reduce jump-related tail risk at the same initial capital?

## Economic mechanism

Let $C$ and $H$ be the target and secondary option prices. A local gamma hedge holds $g=C_{SS}/H_{SS}$ of the secondary option. Small secondary gamma and large jumps make this approximation economically risky.

## Research design

Use one ATM target option and a secondary option at the same expiry. Price under a Merton law, simulate common physical paths under baseline and jump-stress laws, and compare daily/weekly delta and capped delta–gamma hedging with identical initial capital.

Predeclare gamma caps and fallback before comparing stress scenarios. Use matched paths, initial capital and funding; report ES uncertainty and the frequency of constrained positions, including the no-jump subset.

\newpage

## Required exhibits

Jump residual versus size, hedge error distributions and tail tables, paired bootstrap intervals, turnover and stress loss decomposition.

## Minimum viable thesis

Merton pricing reference, common-path delta versus capped delta-gamma hedge under two P scenarios with ES uncertainty and funding checks.

## Scope and feasibility

Stress is a stipulated scenario not a calibrated market disaster probability. Gamma matching is local, secondary option has its own jumps and transaction costs; compare common caps and capital, disclose rare-tail uncertainty. Distinct from D01.03.01, which emphasizes pricing and diffusion/jump identification.

**Prerequisites:** Option Greeks, jump diffusion, portfolio accounting, Monte Carlo, ES.

**Optional extension:** Choose hedge ratios by conditional squared jump residual or training-sample ES; freeze policy before independent tests.

## Milestones

W1-3: jump model and hedge algebra; W4-6: benchmark/ledger; W7-9: simulation; W10-12: tail and costs; W13-16: dissertation.

Agree the parameter/data contract and acceptance tests with the supervisor before the full research begins. Detailed tasks, milestones and acquisition instructions are in the student workspace.
