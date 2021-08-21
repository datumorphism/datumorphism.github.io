---
title: "Contrastive Model: Max Mutual Info"
date: 2021-08-13
category:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Contrastive Model"
  - "Mutual Information"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
weight: 6
links:
  - "cards/information/mutual-information.md"
  - "cards/machine-learning/learning-theories/noise-contrastive-estimation.md"
---

To generate contrast, we can also use {{< c "cards/information/mutual-information.md" >}} as the objective. Take two encoded space from the encoder, $g_1$ and $g_2$, we shall maximize the mutual information between the two representations if they are representing the same thing.

However, mutual information is hard to calculate. Models such as Deep InfoMax use {{< c "cards/machine-learning/learning-theories/noise-contrastive-estimation.md" "NCE" >}} instead[^Liu2020].



[^Liu2020]: {{< cite key="Liu2020" >}}