---
title: "Evidence Lower Bound: ELBO"
description: "ELBO is an very important concept in variational methods"
date: 2021-04-12
authors:
  - "LM"
categories:
  - "machine learning"
tags:
  - "variational method"
  - "probabilistic"
references:
  - name: "Yang X. Understanding the Variational Lower Bound. Available: http://legacydirs.umiacs.umd.edu/~xyang35/files/understanding-variational-lower.pdf"
    link: "http://legacydirs.umiacs.umd.edu/~xyang35/files/understanding-variational-lower.pdf"
weight:
links:
  - "cards/math/jensens-inequality.md"
  - "wiki/machine-learning/bayesian/latent-variable-models.md"
  - "wiki/machine-learning/basics/kl-divergence.md"
---

{{< message class="warning">}}

This article reuses a lot of materials from the references. Please see the references for more details on ELBO.

{{< /message >}}

Given a probability distribution density $p(X)$ and a latent variable $Z$, we have the marginalization of the join probability being

$$
\int dZ p(X, Z) = p(X).
$$

## Using Jensen's Inequality

In many models, we are interested in the log probability density $\log p(X)$ which can be decomposed using an auxillary density of the latent variable $q(Z)$,

{{< m >}}
\begin{align}
\log p(X) =& \log \int dZ p(X, Z) \\
=& \log \int dZ p(X, Z) \frac{q(Z)}{q(Z)} \\
=& \log \int dZ q(Z) \frac{p(X, Z)}{q(Z)} \\
=& \log \mathbb E_q \left[ \frac{p(X, Z)}{q(Z)} \right].
\end{align}
{{< /m >}}

{{< c "cards/math/jensens-inequality.md" "Jensen's inequality" >}} shows that

{{< m >}}
\log \mathbb E_q \left[ \frac{p(X, Z)}{q(Z)} \right] \geq  \mathbb E_q \left[ \log\left(\frac{p(X, Z)}{q(Z)}\right) \right],
{{< /m >}}

as $\log$ is a concave function.

Applying this inequality, we get

{{< m >}}
\begin{align}
\log p(X) =& \log \mathbb E_q \left[ \frac{p(X, Z)}{q(Z)} \right] \\
\geq&  \mathbb E_q \left[ \log\left(\frac{p(X, Z)}{q(Z)}\right) \right] \\
=& \mathbb E_q \left[ \log p(X, Z)- \log q(Z) \right] \\
=& \mathbb E_q \left[ \log p(X, Z) \right] - \mathbb E_q \left[ \log q(Z) \right] .
\end{align}
{{< /m >}}

Uing the definition of entropy and cross entropy, we know that

{{< m >}}
H(q(Z)) = - \mathbb E_q \left[ \log q(Z) \right]
{{< /m >}}

is the entropy of $q(Z)$ and

{{< m >}}
H(q(Z);p(X,Z)) = -\mathbb E_q \left[ \log p(X, Z) \right]
{{< /m >}}

is the cross entropy. For convinence, we denote

{{< m >}}
L = \mathbb E_q \left[ \log p(X, Z) \right] - \mathbb E_q \left[ \log q(Z) \right] = - H(q(Z);p(X,Z)) + H(q(Z)),
{{< /m >}}

which is called the evidence lower bound (ELBO) as

{{< m >}}
\log p(X) \geq L.
{{< /m >}}

## KL Divergence

In a latent variable model, we might need to calculate the posterior $p(Z|X)$. When this is intractable, we find an approximation $q(Z|\theta)$ where $\theta$ is the parametrization such as neural network parameters. To make sure we have a good approximation of the posterior, we find the KL divergence of $q(Z|\theta)$ and $p(Z|X)$.

The {{< c "wiki/machine-learning/basics/kl-divergence.md" "KL divergence" >}} is

{{< m >}}
\begin{align}
D_\text{KL}(q(Z|\theta)\parallel p(Z|X)) =& -\mathbb E_q \log\frac{p(X|Z)}{q(Z|\theta)} \\
=& -\mathbb E_q \log\frac{p(X, Z)/p(X)}{q(Z|\theta)} \\
=& -\mathbb E_q \log\frac{p(X, Z)}{q(Z|\theta)} - \mathbb E_q \log\frac{1}{p(X)} \\
=& - L + \log p(X).
\end{align}
{{< /m >}}

Since $D(q(Z|\theta)\parallel p(Z|X))\geq 0$, we have

{{< m >}}
\log p(X) \geq L,
{{< /m >}}

which also indicates that $L$ is the lower bound of $\log p(X)$.

In fact,

{{< m >}}
L - \log p(X) = - D_\text{KL}(q(Z|\theta)\parallel p(Z|X))
{{< /m >}}

is the Jensen gap.