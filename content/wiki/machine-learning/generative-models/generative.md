---
title: "An Introduction to Generative Models"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Generative Model"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
weight: 1
---

Discriminative model:
- The conditional probability of class label on data (posterior) $p(C_k\mid x)$

Generative models:
- Likelihood $p(x\mid C_k)$
- Sample from the likelihood to generate data
- With latent variables $z$ and some neural network parameters $\theta$: $P(x,z\mid \theta) = p(x\mid z, \theta)p(z)$
