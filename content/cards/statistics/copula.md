---
title:  "Copula"
date: 2023-01-01
authors:
  - Lei Ma
categories:
  - statistics
tags:
  - statistics
references:
  - name: "Quant D. A Simple Introduction to Copulas. YouTube. 2021. Available: https://www.youtube.com/watch?v=WFEzkoK7tsE"
    link: "https://www.youtube.com/watch?v=WFEzkoK7tsE"
  - name: "Wiecki T. An intuitive, visual guide to copulas — While My MCMC Gently Samples. In: While My MCMC Gently Samples [Internet]. 3 May 2018 [cited 6 Jan 2023]. Available: https://twiecki.io/blog/2018/05/03/copulas/"
    link: "https://twiecki.io/blog/2018/05/03/copulas/"
  - name: "SDV. Introduction to Copulas — Copulas 0.6.0 documentation. In: Copulas [Internet]. 2018 [cited 6 Jan 2023]. Available: https://sdv.dev/Copulas/tutorials/01_Introduction_to_Copulas.html"
    link: "https://sdv.dev/Copulas/tutorials/01_Introduction_to_Copulas.html"
---

Given two uniform marginals, we can apply the inverse cdf of a continuous distribution to form a new joint distribution.

Some examples in [this notebook](https://deepnote.com/workspace/lm-3917ee58-3e0d-43ba-a6c8-13241298300c/project/distributions-57869f4c-613e-4938-a8f1-ec6096b8269c/%2Fguassian-copula.ipynb).

{{< figure src="../assets/copula/uniform_2d.png" title="Uniform marginals" >}}

{{< c "cards/statistics/distributions/multivariate-normal-distribution.md" "Gaussian" >}} copula:

{{< figure src="../assets/copula/copula_normal_normal.png" title="Normal, Normal" >}}


Some other examples:

1. {{< c "cards/statistics/distributions/normal-distribution.md" "Normal" >}} and {{< c "cards/statistics/distributions/beta.md" "Beta" >}}: {{< figure src="../assets/copula/copula_norm_beta.png" title="Normal, Beta" >}}
2. Gumbel and {{< c "cards/statistics/distributions/beta.md" "Beta" >}}: {{< figure src="../assets/copula/copula_gumbel_beta.png" title="Gumbel, Beta" >}}
3. {{< c "cards/statistics/distributions/t-distribution.md" "t distribution" >}}: {{< figure src="../assets/copula/copula_t.png" title="t, t" >}}
