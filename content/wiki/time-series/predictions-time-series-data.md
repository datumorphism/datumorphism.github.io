---
title: "Predictions Using Time Series Data"
description: "Seasonalities etc"
date: 2019-06-21
category:
- 'Time Series Data'
tags:
- 'Seasonality'
references:
- name: "Build Facebook's Prophet in PyMC3; Bayesian time series analyis with Generalized Additive Models"
  link: https://www.ritchievink.com/blog/2018/10/09/build-facebooks-prophet-in-pymc3-bayesian-time-series-analyis-with-generalized-additive-models/
links:
  - cards/statistics/bayes-theorem.md
weight: 3
---


## General Phenological Model for Seasonality

In business, time series data $f(t)$ usually carries information about trend $g(t)$ ($g$ is used since trend is usually growth), seasonalities (periodical effects) $p(t)$, holiday effects (structural effects) $s(t)$, etc. We will decompose a time series $f(t)$ into four components

$$
\begin{equation}
f(t) = g(t) + p(t) + s(t) + \epsilon(t).
\end{equation}
$$

To train a model for the predictions, we need to write down the exact models of these three predictable components.

