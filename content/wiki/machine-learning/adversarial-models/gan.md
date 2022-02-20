---
title: "GAN"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Adversarial Model"
  - "GAN"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
  - name: "Arjovsky M, Chintala S, Bottou L. Wasserstein GAN. arXiv [stat.ML]. 2017. Available: http://arxiv.org/abs/1701.07875"
    link: "http://arxiv.org/abs/1701.07875"
    key: "Arjovsky2017"
  - name: "Probability Estimation"
    link: "https://neuronstar.github.io/cpe-docs"
weight: 1
notify: "We have built a site dedicated for self-supervised learning: https://neuronstar.github.io/cpe-docs ."
---


The task of GAN is to generate features $X$ from some noise $\xi$ and class labels $Y$,

$$\xi, Y \to X.$$

Many different GANs are proposed. Vanilla GAN has a simple structure with a single discriminator and a single generator. It uses the minmax game setup. However, it is not stable to use minmax game to train a GAN model. WassersteinGAN was proposed to solve the stability problem during training[^Arjovsky2017]. More advanced GANs like BiGAN and ALI have more complex structures.



## Vanilla GAN

{{< card title="Minmax Game" >}}

Suppose we have two players $G$ and $D$, and a utility $v(D, G)$, a minmax game is maximizing the utility $v(D, G)$ for the worst case of $G=\hat G$ that minimizes $v$ then we have to find $D=\hat D$ that maximizes $v$, i.e.,

$$\underset{G, D}{\operatorname{minmax}} v(D, G).$$

{{< /card >}}


The loss for vanilla GAN is the minmax loss

{{< m >}}
\underset{G, D}{\operatorname{minmax}} \mathbb E_{x\sim P_{data}} \left[ \ln D(x) \right] + \mathbb E_{z\sim p_z} \left[ \ln ( 1- D(G(z)) ) \right].
{{< /m >}}


{{< figure src="../assets/adversarial-complete-input/gan-illustration.png" caption="Illustration of GAN" >}}

## BiGAN

BiGAN uses one generator, one encoder and one discriminator[^Liu2020].

{{< figure src="../assets/adversarial-complete-input/bigan-illustration.png" caption="Illustration of BiGAN" >}}



[^Liu2020]: {{< cite key="Liu2020" >}}
[^Arjovsky2017]: {{< cite key="Arjovsky2017" >}}