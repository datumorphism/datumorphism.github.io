---
title: "Cauchy-Lorentz Distribution"
excerpt: "also known as Breit–Wigner distribution"
date: 2020-03-14
category:
- 'Statistics'
tags:
- 'Statistics'
- 'Distributions'
references:
- name: Cauchy Distribution @ Wikipedia
  link: https://en.wikipedia.org/wiki/Cauchy_distribution
- name: stdlib.js documentation
  link: https://stdlib.io/docs/api/v0.0.90/@stdlib/stats/base/dists/cauchy
---

## Cauchy-Lorentz Distribution

> .. ratio of two independent normally distributed random variables with mean zero.
>
> Source: https://en.wikipedia.org/wiki/Cauchy_distribution

Lorentz distribution is frequently used in physics.

PDF:

$$
\frac{1}{\pi\gamma} \left( \frac{\gamma^2}{ (x-x_0)^2 + \gamma^2} \right)
$$

The median and mode of the Cauchy-Lorentz distribution is always $x_0$. $\gamma$ is the FWHM.

## Visualize

![](../assets/cauchy/cauchy.png)