---
title: "f-Divergence"
description: ""
date: 2021-09-04
authors:
  - "Lei Ma"
categories:
  - "Information"
tags:
  - "Information Theory"
  - "Divergence"
references:
  - name: "Contributors to Wikimedia projects. F-divergence. In: Wikipedia [Internet]. 17 Jul 2021 [cited 4 Sep 2021]. Available: https://en.wikipedia.org/wiki/F-divergence"
    link: "https://en.wikipedia.org/wiki/F-divergence"
    key: "f-divergence_wiki"
  - name: "Nowozin S, Cseke B, Tomioka R. f-GAN: Training Generative Neural Samplers using Variational Divergence Minimization. arXiv [stat.ML]. 2016. Available: http://arxiv.org/abs/1606.00709"
    link: "http://arxiv.org/abs/1606.00709"
    key: "Nowozin2016"
links:
  - "wiki/machine-learning/basics/kl-divergence.md"
---


The f-divergence is defined as[^f-divergence_wiki]

$$
\operatorname{D}_f = \int f\left(\frac{p}{q}\right) q\mathrm d\mu,
$$

where $p$ and $q$ are two densities and $\mu$ is a reference distribution.

{{< message title="Requirements on the generating function" >}}

The generating function $f$ is required to

- be convex, and
- $f(1) =0$.

{{< /message >}}


For $f(x) = x \log x$ with $x=p/q$, f-divergence is reduced to the KL divergence

{{< m >}}
\begin{align}
&\int f\left(\frac{p}{q}\right) q\mathrm d\mu \\
=& \int \frac{p}{q} \log \left( \frac{p}{q} \right) \mathrm d\mu \\
=&  \int p \log \left( \frac{p}{q} \right) \mathrm d\mu.
\end{align}
{{< /m >}}

For more special cases of f-divergence, please refer to wikipedia[^f-divergence_wiki]. Nowozin et al also provided a concise review of f-divergence[^Nowozin2016].



[^f-divergence_wiki]: {{< cite key="f-divergence_wiki" >}}

[^Nowozin2016]: {{< cite key="Nowozin2016" >}}