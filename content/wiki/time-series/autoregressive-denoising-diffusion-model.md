---
title: "Autoregressive Denoising Diffusion Model"
description: "TimeGrad"
date: 2023-02-10
categories:
    - 'Time Series'
tags:
    - 'Diffusion Model'
references:
  - name: "Rasul K, Seward C, Schuster I, Vollgraf R. Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting. arXiv [cs.LG]. 2021. Available: http://arxiv.org/abs/2101.12072"
    link: "http://arxiv.org/abs/2101.12072"
    key: "Rasul2021"
garden:
  - "seedling"
links:
  - "wiki/machine-learning/energy-based-model/diffusion-model.md"
  - "wiki/forecasting/forecasting-problem.md"
---

## Autoregressive

In an multivariate {{< c "wiki/forecasting/forecasting-problem.md" "forecasting problem" >}}, given an input sequence $\mathbf x_{t-K: t}$, we forecast $\mathbf x_{t+1:t+H}$.

To apply the {{< c "wiki/machine-learning/energy-based-model/diffusion-model.md" "denoising diffusion model" >}} in our multivariate forecasting problem, we define our forecasting task as an autoregressive problem

$$
q(\mathbf x^0_{t - K:t} \vert \mathbf x^0_{1:t_0 - 1}) = \Pi_{t=t_0}^T q(\mathbf x^0_t \vert \mathbf x^0_{1:t-1}).
$$

{{< figure src="../assets/autoregressive-denoising-diffusion-model/ar-denoising-diffusion-model-problem.jpg" >}}


## Time Dynamics

Time dynamics can be easily captured by some RNN, meanwhile, we need a model for the diffusion process at each time step. Note that in {{< c "wiki/machine-learning/energy-based-model/diffusion-model.md" "denoising diffusion model" >}}, we minimize

{{< m >}}
\operatorname{min}_\theta \mathbb E_{q(\mathbf x^0)} \left[ -\log p_\theta (\mathbf x^0) \right]
{{< /m >}}

The above loss becomes that of the denoising model for a single time step. Explicitly,

{{< m >}}
\operatorname{min}_\theta \mathbb E_{q(\mathbf x^0_t )} \left[ -\log p_\theta (\mathbf x^0_t) \right].
{{< /m >}}

To include the time dynamics, we use the RNN state of the previous time step $\mathbf h_{t-1}$[^Rasul2021]

{{< m >}}
\operatorname{min}_\theta \mathbb E_{q(\mathbf x^0_t )} \left[ -\log p_\theta (\mathbf x^0_t \vert \mathbf h_{t-1}) \right].
{{< /m >}}

Apart from the usual time dimension $t$, the autoregressive denoising diffusion model has another dimension to optimize: the diffusion step $n$ for each time $t$.

The loss for each time step $t$ is[^Rasul2021]

{{< m >}}
\mathcal L_t = \mathbb E_{\mathbf x^0_t, \epsilon, n} \left[ \lVert \epsilon - \epsilon_\theta ( \sqrt{\bar \alpha_n} \mathbf x^0_t + \sqrt{1-\bar \alpha_n}\epsilon, \mathbf h_{t-1}, n ) \rVert^2  \right].
{{< /m >}}

That being said, we just need to minimize $\mathcal L_t$ for each time step $t$.

## Training Algorithm

See Rasul et al., (2021)[^Rasul2021].

## How to Forecast


After training, we obtain the time dynamics encoding $\mathbf h_T$, with which the denoising steps can be calculated using the reverse process

{{< m >}}
\mathbf x^{n-1}_{T+1} = \frac{1}{\alpha_n} \left( \mathbf x^n_{T+1} - \frac{\beta_n}{1 - \bar\alpha_n} \epsilon_\theta( \mathbf x^n_{T+1}, \mathbf h_{T}, n ) \right) + \sqrt{\Sigma_\theta} \mathbf z,
{{< /m >}}

where $\mathbf z \sim \mathcal N(\mathbf 0, \mathbf I)$.

For example,

{{< m >}}
\mathbf x^{0}_{T+1} = \frac{1}{\alpha_1} \left( \mathbf x^1_{T+1} - \frac{\beta_1}{1 - \bar\alpha_1} \epsilon_\theta( \mathbf x^1_{T+1}, \mathbf h_{T}, 1 ) \right) + \sqrt{\Sigma_\theta} \mathbf z.
{{< /m >}}


## It is Probabilistic

The quantiles is calculated by repeating many times for each forecasted time step[^Rasul2021].



[^Rasul2021]: {{< cite key="Rasul2021" >}}