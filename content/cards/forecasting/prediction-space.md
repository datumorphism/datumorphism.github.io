---
title: "Prediction Space in Forecasting"
date: 2022-04-08
categories:
  - "Time Series"
tags:
  - "Time Series"
  - "Forecasting"
references:
  - name: "Gneiting T, Katzfuss M. Probabilistic Forecasting. Annu Rev Stat Appl. 2014;1: 125–151. doi:10.1146/annurev-statistics-062713-085831"
    link: "https://www.annualreviews.org/doi/10.1146/annurev-statistics-062713-085831"
    key: "Gneiting2014"
weight: 1
---

In a forecasting problem, we have

- $\mathcal P$, the priors, e.g., price and demand is negatively correlated,
- $\mathcal D$, available dataset,
- $Y$, the observations, and
- $F$, the forecasts.


{{< message title="Information Set $\mathcal A$" class="info" >}}

The priors $\mathcal D$ and the available data $\mathcal P$ can be summarized together as the information set $\mathcal A$.

{{< /message >}}



Under a probabilistic view, a forecaster will find out or approximate a CDF $\mathcal F$ such that[^Gneiting2014]

{{< m >}}
\mathcal F(Y\vert \mathcal D, \mathcal P) \to F.
{{< /m >}}

Naively speaking, once the density $\rho(F, Y)$ is determined or estimated, a probabilistic forecaster can be formed. The joint probability of $(F, Y)$ is our prediction space.






[^Gneiting2014]: {{< cite key="Gneiting2014" >}}