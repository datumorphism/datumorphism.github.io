---
title: "Diffusion Models for Forecasting"
description: ""
date: 2023-02-10
authors:
  - "LM"
categories:
  - 'Energy-based Model'
tags:
  - 'Machine Learning'
  - 'Diffusion Model'
references:
  - name: "Rasul K, Seward C, Schuster I, Vollgraf R. Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting. arXiv [cs.LG]. 2021. Available: http://arxiv.org/abs/2101.12072"
    link: "http://arxiv.org/abs/2101.12072"
weight:
links:
  - ""
---

## Objective

Given input $\mathbf x^0$ from a very complicated and unknown distribution $q(\mathbf x^0)$, we find a latent space with simple and manageable distribution, and the transformations from $\mathbf x^0$ to $\mathbf x^n$ as well as from $\mathbf x^n$ to $\mathbf x^0$. For example, with $N=5$, we have the forward process

{{< mermaid >}}
flowchart LR
x0 --> x1 --> x2 --> x3 --> x4 --> x5
{{< /mermaid >}}

and the reverse process

{{< mermaid >}}
flowchart LR
x5 --> x4 --> x3 --> x2 --> x1 --> x0
{{< /mermaid >}}


Diffusion model assumes each step is Markovian,

$$
q(\mathbf x^1, \mathbf x^2, \mathbf x^3, \mathbf x^4, \mathbf x^5 \vert \mathbf x^0) = q(\mathbf x^5\vert \mathbf x^4) q(\mathbf x^4\vert \mathbf x^3) q(\mathbf x^3\vert \mathbf x^2)q(\mathbf x^2\vert \mathbf x^1)q(\mathbf x^1\vert \mathbf x^0),
$$

with each step being simple diffusion process, e.g.,

$$
q(\mathbf x^n \vert \mathbf x^{n-1}) \equiv \mathcal N (\mathbf x^n ; \sqrt{ 1 - \beta_n} \mathbf x ^{n -1}, \beta_n\mathbf I).
$$

This simulates an information diffusion process. The information in the original data is gradually smeared.

If the chosen diffusion process is revertible, the reverse process of it can be modelled by a similar Makov process

$$
p_\theta (\mathbf x^0, \mathbf x^1, \mathbf x^2, \mathbf x^3, \mathbf x^4, \mathbf x^5) = p_\theta (\mathbf x^0 \vert \mathbf x^1) p_\theta (\mathbf x^1 \vert \mathbf x^2)
p_\theta (\mathbf x^2 \vert \mathbf x^3)
p_\theta (\mathbf x^3 \vert \mathbf x^4)
p_\theta (\mathbf x^4 \vert \mathbf x^5)
p(\mathbf x^5).
$$

This reverse process is the denoising process.

As long as our model estimates $p_\theta (\mathbf x^n \vert \mathbf x^{n-1})$ nicely, we can go $\mathbf x^0 \to \mathbf x^N$ and $\mathbf x^N \to \mathbf x^0$.


In summary,

- forward: perturbs data to noise, step by step
- reverse: converts noise to data, step by step

{{< mermaid >}}
flowchart LR
prior["prior distribution"]
    data --"forward Markov chain"--> noise
    noise --"reverse Markov chain"--> data
	  prior --"sampling"--> noise
{{< /mermaid >}}


### Optimization

We have to find $p_\theta$. A natural loss function is the negative log-likelihood

$$
\mathbb E_{q(\mathbf x^0)} \left( - \log ( p_\theta (\mathbf x^0) ) \right).
$$
