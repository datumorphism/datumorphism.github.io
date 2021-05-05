---
title: Bayesian Information Criterion
description: "BIC considers the number of parameters and the total number of data records."
date: 2020-11-08
tags:
  - Bayesian
  - Model Selection
references:
  - link: https://www.oxfordhandbooks.com/view/10.1093/oxfordhb/9780199957996.001.0001/oxfordhb-9780199957996-e-14
    name: Vandekerckhove, J., & Matzke, D. (2015). Model comparison and the principle of parsimony. Oxford Library of Psychology.
links:
  - wiki/model-selection/goodness-of-fit.md
  - cards/statistics/aic.md
---

BIC is Bayesian information criterion, it replaced the $+2k$ term in {{< c "/cards/statistics/aic.md" "AIC" >}} with $k\ln n$ to bring in punishment for the number of parameters of the model based on the number of data records,

{{< m >}}
\mathrm{BIC} = -2\ln p(y|\hat\theta) + k\ln n = \ln \left(\frac{n^k}{p^2}\right)
{{< /m >}}

- $n$ is the observations.

We prefer the model with a small BIC.