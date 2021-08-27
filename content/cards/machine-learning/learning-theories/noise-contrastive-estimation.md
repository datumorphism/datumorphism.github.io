---
title: "Noise Contrastive Estimation: NCE"
date: 2021-08-13
categories:
- 'Machine Learning::Theories'
tags:
- 'Learning Theory'
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
---


Noise contrastive estimation (NCE) objective function is[^Liu2020]

{{< m >}}
\mathcal L = \mathbb E_{x, x^{+}, x^{-}} \left[ - \ln \frac{ C(x, x^{+})}{ C(x,x^{+}) + C(x,x^{-}) } \right],
{{< /m >}}

where

- $x^{+}$ represents data similar to $x$,
- $x^{-}$ represents data dissimilar to $x$,
- $C(\cdot, \cdot)$ is a function to compute the similarities.

For example, we can use

{{< m >}}
C(x, x^{+}) = e^{ f(x)^T f(x^{+}) },
{{< /m >}}


so that the objective function becomes

{{< m >}}
\mathcal L = \mathbb E_{x, x^{+}, x^{-}} \left[ - \ln \frac{ e^{ f(x)^T f(x^{+}) } }{ e^{ f(x)^T f(x^{+}) } + e^{ f(x)^T f(x^{-}) } } \right].
{{< /m >}}

The function $f(\cdot)$ can be an encoder.


[^Liu2020]: {{< cite key="Liu2020" >}}