---
title: "Generative Model: Normalizing Flow"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "Normalizing Flow"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
weight: 3
links:
  - "reading/normalizing-flow-introduction-1908.09257.md"
---

Normalizing flow is a method to convert a complicated distribution $p(x)$ to a simpler distribution $\tilde p(z)$ by building up a map $z=f(y)$ for the variable $x$ to $z$. The relations between the two distributions is established using the conservation law for distributions, $\int p(x) \mathrm d x = \int \tilde p (z) \mathrm d z = 1$. One could imagine that changing the variable also brings in the Jacobian.

For a probability density $p(x)$ and a transformation of coordinate $x=g(z)$ or $z=f(x)$, the density can be expressed using the coordinate transformations, i.e.,

{{< m >}}
\begin{align}
p(x) &= \tilde p (f(x)) \lvert \operatorname{det} \operatorname{D} g(f(x)) \rvert^{-1} \\
&= \tilde p(f(x)) \lvert \operatorname{det}\operatorname{D} f(x) \rvert
\end{align}
{{< /m >}}

where the Jacobian is

{{< m >}}
\operatorname{D} g(z) \to \frac{\partial }{\partial z} g.
{{< /m >}}


The operation $g _ { * }\circ \tilde p(z)$ is the pushforward of $\tilde p(z)$. The operation $g _ { * }$ will pushforward simple distribution $\tilde p(z)$ to a more complex distribution $p(x)$.

{{< figure src="../assets/generative-flow/generative-flow-encoding-decoding.png" >}}

- The generative direction: sample $z$ from distribution $\tilde p(z)$, apply transformation $g(z)$;
- The normalizing direction: "simplify" $p(x)$ to some simple distribution $\tilde p(z)$.



The key to the flow model is the chaining of the transformations

{{< m >}}
\operatorname{det} \operatorname{D} f(x) = \Pi_{i=1}^N \operatorname{det} \operatorname{D} f_i (x_i)
{{< /m >}}

where

{{< m >}}
\begin{align}
x_i &= g_i \circ \cdots \circ g_1 (z)\\
&= f_{i+1} \circ \cdots \circ f_N (x).
\end{align}
{{< /m >}}



