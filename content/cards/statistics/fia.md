---
title: "Fisher Information Approximation"
tags:
  - FIA
---


#FIA is a method to describe the [[minimum-description-length|minimum description length ( #MDL )]] of models,

$$
\mathrm{FIA} = -\ln p(y | \hat\theta) + \frac{k}{2} \ln \frac{n}{2\pi} + \ln \int_\Theta \sqrt{ \operatorname{det}[I(\theta)] d\theta }
$$

- $I(\theta)$: Fisher information matrix of sample size 1.
- $$I_{i,j}(\theta) = E\left( \frac{\partial \ln p(y| \theta)}{\partial \theta_i}\frac{ \partial \ln p (y | \theta) }{ \partial \theta_j } \right)$$.