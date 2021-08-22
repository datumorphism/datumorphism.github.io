---
title: "Contrastive Model: Context-Instance"
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
weight: 2
links:
  - "cards/information/mutual-information.md"
  - "cards/machine-learning/learning-theories/noise-contrastive-estimation.md"
---

In contrastive methods, we can manipulate the data to create data entries and infer the changes using a model. These methods are models that "predict relative position"[^Liu2020]. Common tricks are

- shuffling image sections like jigsaw, and
- rotate the image.

We can also adjust the model to discriminate the similarities and differences. For example, to generate contrast, we can also use {{< c "cards/information/mutual-information.md" >}} as the objective. Take two encoded space from the encoder, $g_1$ and $g_2$, we shall maximize the mutual information between the two representations if they are representing the same thing.

## Deep InfoMax

However, mutual information is hard to calculate. Models such as Deep InfoMax use {{< c "cards/machine-learning/learning-theories/noise-contrastive-estimation.md" "NCE" >}} instead[^Liu2020]. For Deep InfoMax, the loss function is

{{< m >}}
\mathcal L = \mathbb E_{v, x} \left[ -\ln \frac{e^{v^T\cdot s}}{e^{v^T\cdot s} + e^{v^T\cdot s^-}}  \right].
{{< /m >}}

{{< figure src="../assets/contrastive-max-mutual-info/deep-infomax-illustration.png" caption="Illustration of Deep InfoMax based on Liu2020." >}}





[^Liu2020]: {{< cite key="Liu2020" >}}