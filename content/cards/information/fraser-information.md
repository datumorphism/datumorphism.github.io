---
title: "Fraser Information"
description: ""
date: 2021-05-05T17:49:12+02:00
authors:
  - "Lei Ma"
categories:
  - "Information"
tags:
  - "Information Theory"
references:
  - name: "Fraser DAS. On Information in Statistics. aoms. 1965;36: 890–896. doi:10.1214/aoms/1177700061"
    link: "https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-36/issue-3/On-Information-in-Statistics/10.1214/aoms/1177700061.full"
weight:
links:
  - "cards/information/fisher-information.md"
  - "wiki/machine-learning/basics/kl-divergence.md"
  - "cards/information/coding-theory-concepts.md"
---


The Fraser information is

$$
I_F(\theta) = \int g(X) \ln f(X;\theta) \, \mathrm d X.
$$

When comparing two models, $\theta_0$ and $\theta_1$, the information gain is

$$
\propto (F(\theta_1) - F(\theta_0)).
$$


The Fraser information is closed related to {{< c "cards/information/fisher-information.md" "Fisher information" >}}, Shannon information, and {{< c "wiki/machine-learning/basics/kl-divergence.md" "Kullback information">}} [^Fraser1965].

[^Fraser1965]: Fraser DAS. On Information in Statistics. aoms. 1965;36: 890–896. doi:10.1214/aoms/1177700061



