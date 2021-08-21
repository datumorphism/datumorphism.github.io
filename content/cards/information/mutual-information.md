---
title: "Mutual Information"
description: ""
date: 2021-08-13
authors:
  - "Lei Ma"
categories:
  - "Information"
tags:
  - "Information Theory"
  - "Mutual Information"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
  - name: "Latham PE, Roudi Y. Mutual information. Scholarpedia. 2009;4. doi:10.4249/scholarpedia.1658"
    link: "http://www.scholarpedia.org/article/Mutual_information"
    key: "Latham2009"
links:
  - "wiki/machine-learning/basics/kl-divergence.md"
---

Mutual information is defined as

{{< m >}}
I(X;Y) = \mathbb E_{p_{XY}} \ln \frac{P_{XY}}{P_X P_Y}.
{{< /m >}}

In the case that $X$ and $Y$ are independent variables, we have $P_{XY} = P_X P_Y$, thus $I(X;Y) = 0$. This makes sense as there would be no "mutual" information if the two variables are independent of each other.


## Entropy and Cross Entropy

Mutual information is closely related to entropy. A simple decomposition shows that

{{< m >}}
I(X;Y) = H(X) - H(X\mid Y),
{{< /m >}}

which is the reduction of uncertainty in $X$ after observing $Y$.


## KL Divergence

This definition of mutual information is equivalent to the following {{< c "wiki/machine-learning/basics/kl-divergence.md" >}},

{{< m >}}
D_{\mathrm{KL}} \left(  P_{XY}(x,y) \parallel  P_X(x) P_{Y}(y) \right).
{{< /m >}}





