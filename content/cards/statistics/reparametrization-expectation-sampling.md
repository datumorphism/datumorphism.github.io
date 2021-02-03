---
title: "Reparametrization in Expectation Sampling"
description: "Reparametrize the sampling distribution to simplify the sampling"
date: 2021-01-20
authors:
  - "LM"
categories:
  - "statistics"
tags:
  - "normalizing flow"
weight:
links:
  - "wiki/machine-learning/bayesian/latent-variable-models.md"
---

The expectation value of a function $f(z)$ over a Guassian distribution $\mathscr N(z;\mu, \sigma)$ is equivalent to the expectation value of $f()$ a Gaussian distribution $\mathscr N(z;\mu=0, \sigma=1)$, i.e.,

{{< m >}}
{\mathbb E}_{\mathscr N(z; \mu, \sigma)} \left[ f(z) \right] = {\mathbb E}_{\mathscr N(z; 0, 1)} \left[ f() \right]
{{< /m >}}

where

{{< m >}}
\mathscr N = \frac{1}{\sqrt{2\pi\sigma^2}} \exp
\left( -\frac{(z-\mu)^2}{2\sigma^2}\right).
{{< /m >}}


{{< m >}}
\begin{align}
{\mathbb E}_{\mathscr N(z; \mu, \sigma)} \left[ f(z) \right] &= \int \mathrm d z \frac{1}{\sqrt{2\pi\sigma^2}}\exp \left( -\frac{(z-\mu)^2}{2\sigma^2}\right) f(z) \\
&= \int \mathrm dz \frac{1}{\sigma} \frac{1}{\sqrt{2\pi}} \exp \left( -\frac{1}{2} \left(\frac{z-\mu}{\sigma}\right)^2 \right) f(z) \\
&= \int \mathrm d \left( \sigma z' + \mu \right) \frac{1}{\sigma} \frac{1}{\sqrt{2\pi}} \exp \left( -\frac{1}{2} z'^2 \right) f(\sigma z' + \mu) \\
&= \int \mathrm d z' \frac{1}{\sqrt{2\pi}}\exp \left( -\frac{1}{2} z'^2 \right) f(\sigma z' + \mu) \\
&= \int \mathrm d z' \mathscr N(z'; \mu=0, \sigma=1) f(\sigma z' + \mu) \\
&= {\mathbb E}_{\mathscr N(z'; \mu=0, \sigma=1)} \left[ f(\sigma z' + \mu) \right]
\end{align}
{{< /m >}}


Define a field $\phi = \{\mu, \sigma\}$, the derivatives of the reparametrization

{{< m >}}
\begin{align}
\frac{\partial}{\partial \phi} {\mathbb E}_{\mathscr N(z; \mu, \sigma)} \left[ f(z) \right] &= \frac{\partial}{\partial \phi}  {\mathbb E}_{\mathscr N(z'; \mu=0, \sigma=1)} \left[ f(\sigma z' + \mu) \right] \\
&= {\mathbb E}_{\mathscr N(z'; \mu=0, \sigma=1)} \left[ \frac{\partial}{\partial \phi} f(\sigma z' + \mu) \right] .
\end{align}
{{< /m >}}

This is a great result. The derivatives are passed onto the function $f$. We do not need to deal with the distribution.


In fact, we have a much general formalism for such properties.