---
title: "Contrastive Model: Instance-Instance"
date: 2021-08-13
categories:
  - "Machine Learning"
tags:
  - "Self-supervised Learning"
  - "Contrastive Model"
  - "Basics"
references:
  - name: "Liu X, Zhang F, Hou Z, Wang Z, Mian L, Zhang J, et al. Self-supervised Learning: Generative or Contrastive. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2006.08218"
    link: "http://arxiv.org/abs/2006.08218"
    key: "Liu2020"
weight: 3
---

It was discovered that the success of {{< c "wiki/machine-learning/contrastive-models/context-instance.md" "mutual information based contrastive learning" >}} is more related to the encoder architecture and the negative sampling strategy[^Liu2020]. Instance-instance method is more direct in solving the contrastive problem. It take the instance itself directly and make comparisons for discrimination.

## Cluster Discrimination


{{< figure src="../assets/contrastive-instance-instance/deep-cluster-illustration.png" caption="Illustration of Deep Cluster based on Liu2020." >}}





## Instance Discrimination

There are two interesting models under the umbrella of instance discrimination,

- MoCo, and
- SimCLR.


{{< figure src="../assets/contrastive-instance-instance/moco-illustration.png" caption="Illustration of MoCo based on Liu2020." >}}


{{< figure src="../assets/contrastive-instance-instance/simclr-illustration.png" caption="Illustration of SimCLR based on Liu2020." >}}





[^Liu2020]: {{< cite key="Liu2020" >}}