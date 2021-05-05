---
title: "Fisher Information Approximation"
date: 2020-11-08
tags:
  - Bayesian
  - Model Selection
  - FIA
links:
  - cards/statistics/mdl.md
  - cards/statistics/nml.md
---


FIA is a method to describe the minimum description length ({{< c "cards/statistics/mdl.md" "MDL" >}}  ) of models,

$$
\mathrm{FIA} = -\ln p(y | \hat\theta) + \frac{k}{2} \ln \frac{n}{2\pi} + \ln \int_\Theta \sqrt{ \operatorname{det}[I(\theta)] d\theta }
$$

- $I(\theta)$: Fisher information matrix of sample size 1.
- $$I_{i,j}(\theta) = E\left( \frac{\partial \ln p(y| \theta)}{\partial \theta_i}\frac{ \partial \ln p (y | \theta) }{ \partial \theta_j } \right)$$.