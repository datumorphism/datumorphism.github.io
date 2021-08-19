---
title: "Generative Model: Flow"
date: 2021-08-13
category:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "Flow"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
weight: 2
links:
  - "reading/normalizing-flow-introduction-1908.09257.md"
---

{{< figure src="../assets/generative-flow/generative-flow-encoding-decoding.png" >}}

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


The operation $g_{*}\circ \tilde p(z)$ is the push forward of $\tilde p(z)$. The operation $g_{*}$ will pushforward simple distribution $\tilde p(z)$ to a more complex distribution $p(x)$.

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



