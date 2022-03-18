---
title: "Continuous Ranked Probability Score - CRPS"
date: 2022-03-18
categories:
  - 'Time Series'
tags:
  - 'Time Series'
references:
  - name: "Hersbach H. Decomposition of the Continuous Ranked Probability Score for Ensemble Prediction Systems. Weather Forecast. 2000;15: 559–570. doi:10.1175/1520-0434(2000)015<0559:DOTCRP>2.0.CO;2"
    link: "http://dx.doi.org/10.1175/1520-0434(2000)015%3C0559:DOTCRP%3E2.0.CO;2"
    key: "Hersbach2000"
  - name: "Gouttes A, Rasul K, Koren M, Stephan J, Naghibi T. Probabilistic Time Series Forecasting with Implicit Quantile Networks. arXiv [cs.LG]. 2021. doi:10.1109/icdmw.2017.19"
    link: "https://arxiv.org/abs/2107.03743"
    key: "Gouttes2021"
---


The Continuous Ranked Probability Score, known as CRPS, is a score to measure how a proposed distribution approximates the data, without assuming the distributions of the data.


## Definition

CRPS is defined as[^Hersbach2000]

{{< m >}}
CRPS(P, x_a) = \int_{-\infty}^\infty  \lVert P(x) - H(x - x_a) \rVert_2 dx,
{{< /m >}}

where

- $x_a$ is the true value of $x$,
- P(x) is our proposed cumulative distribution for $x$,
- $H(x)$ is the Heaviside step function
  {{< m >}}
  H(x) = \begin{cases}
  1, &\qquad x=0\\
  0, &\qquad x\leq 0\\
  \end{cases}
  {{< /m >}}
- $\lVert \cdot \rVert_2$ is the L2 norm.


## Explain it


The formula looks abstract on first sight, but it becomes crystal clear once we understand it.


Note that the distributions that corresponds to a Heaviside CDF is the delta function $\delta(x-x_a)$. What this score is calculating is the difference between our distribution and a delta function. If we have a model that minimizes CRPS, then we are looking for a distribution that is close to the delta function $\delta(x-x_a)$. In other words, we want our distribution to be large around $x_a$.

To illustrate what the integrand $\lVert P(x) - H(x - x_a) \rVert_2$ means, we consider several scenarios.

{{< figure src="../assets/crps/crps-p-reach-1-faster.jpg" caption="When the proposed CDF $P(x)$ is reaching 1 faster" >}}

{{< figure src="../assets/crps/crps-p-reach-1-slower.jpg" caption="When the proposed CDF $P(x)$ is reaching 1 slower" >}}

{{< figure src="../assets/crps/crps-p-approach-heaviside.jpg" caption="When the proposed CDF $P(x)$ is close to the Heaviside function" >}}

{{< figure src="../assets/crps/crps-dispersed.jpg" caption="When the proposed CDF $P(x)$ is dispersed around $x_a$" >}}

The shade areas determines the integrand of the integral in CRPS. The only way to get a small score is to choose a distribution that is focused around $x_a$.

{{< figure src="../assets/crps/crps-p-approach-heaviside-corresponding-density.jpg" caption="densities of $P(x)$ and $H(x-x_a)$" >}}






## Compared to f-Divergence


Compared to {{< c "wiki/machine-learning/basics/kl-divergence.md" >}} or more generally {{< c "cards/information/f-divergence.md" >}}, CRPS is comparing our proposed CDF to the Heaviside CDF.


{{< e "cards/information/f-divergence.md" >}}

{{< e "wiki/machine-learning/basics/kl-divergence.md" >}}


## Applications


One quite interesting application of the CRPS is to write down the loss for an the quantile function[^Gouttes2021].




[^Hersbach2000]: {{< cite key="Hersbach2000" >}}
[^Gouttes2021]: {{< cite key="Gouttes2021" >}}

