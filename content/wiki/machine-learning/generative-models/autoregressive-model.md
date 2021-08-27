---
title: "Generative Model: Autoregressive Model"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "Autoregressive Model"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
weight: 2
links:
  - "wiki/machine-learning/neural-networks/deep-autoregressive-networks.md"
  - "wiki/time-series/autoregressive-model.md"
---

{{< figure src="../assets/generative-autoregressive-model/autoregressive-overview.png" >}}

The likelihood is modeled as

{{< m >}}
\begin{align}
p_\theta (x) &= \Pi_{t=1}^T p_\theta (x_t \mid x_{1:t-1}) \\
&= p_\theta(x_2 \mid x_{1:1}) p_\theta(x_3 \mid x_{1:2}) \cdots p_\theta(x_T \mid x_{1:T-1})
\end{align}
{{< /m >}}

Taking the log of it

{{< m >}}
\ln p_\theta (x) = \sum_{t=1}^T \ln p_\theta (x_t \mid x_{1:t-1})
{{< /m >}}