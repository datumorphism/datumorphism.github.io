---
title: "Jackknife Resampling"
description: "Jackknife resampling method"
date: 2020-01-26
category:
- 'Statistics'
tags:
- 'Statistics'
references:
- name: Jackknife Resampling
  link: https://en.wikipedia.org/wiki/Jackknife_resampling
published: true
---


Jackknife resampling is a method for estimation of the mean and higher order moments.

Given a sample $\\{x_i\\}$ of size $n$ for the distribution $X$, the jackknife resampling estimates the mean by leaving out each data point systematically. $n$ estimations of the mean will be obtained, with each of the estimations $x_i$

$$
\bar x_i = \frac{1}{n-1} \sum_{j\neq i} x_j.
$$

The mean of the sample is

$$
\bar x = \frac{1}{n}\sum_i \bar x_i = \frac{1}{n} \sum_i \left(\frac{1}{n-1} \sum_{j\neq i} x_j\right) = \frac{1}{n}\sum_i x_i.
$$


The result is consistent with other sample mean methods. Jackknife estimates the variance of the sample

$$
\operatorname{Var}(X) = \frac{1}{n(n-1)} \sum (x_i - \bar x)^2,
$$

which is different from the direct estimation of the variance.

Jackknife is also used to estimate the bias of parameters.