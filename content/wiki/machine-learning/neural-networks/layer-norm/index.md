---
title: "Layer Norm"
description: "Layer norm"
date: 2021-02-15
categories:
  - "Machine Learning"
tags:
  - "Machine Learning"
references:
  - name: "Ba JL, Kiros JR, Hinton GE. Layer Normalization. arXiv [stat.ML]. 2016. Available: http://arxiv.org/abs/1607.06450"
    link: "http://arxiv.org/abs/1607.06450"
  - name: "Brody S, Alon U, Yahav E. On the expressivity role of LayerNorm in Transformers’ attention. arXiv [cs.LG]. 2023. Available: http://arxiv.org/abs/2305.02582"
    link: "http://arxiv.org/abs/2305.02582"
  - name: "Xu J, Sun X, Zhang Z, Zhao G, Lin J. Understanding and Improving Layer Normalization. Advances in Neural Information Processing Systems. 2019;32. Available: https://proceedings.neurips.cc/paper_files/paper/2019/file/2f4fe03d77724a7217006e5d16728874-Paper.pdf"
    link: "https://proceedings.neurips.cc/paper_files/paper/2019/file/2f4fe03d77724a7217006e5d16728874-Paper.pdf"
    key: "Xu2019"
links:
  - wiki/model-selection/mdl-and-neural-networks.md
weight: 5
---


Layer norm is a normalization method to enable better training[^Xu2019].

> Layer normalization (LayerNorm) is a technique to normalize the distributions of intermediate layers.  It enables smoother gradients, faster training, and better generalization accuracy.
>
> Quote from Xu et al. 2019[^Xu2019]

The key of layer norm is to normalize the input to the layer using the mean and standard deviation.

Layer norm plays two roles in neural networks:

1. Projects the key vectors onto a hyperplane.
2. Scales the key vectors to have the same length.


{{< figure src="assets/xu2019-layer-norm-geometry.png" caption="Xu et al. 2019" >}}



[^Xu2019]: {{< cite key="Xu2019" >}}
