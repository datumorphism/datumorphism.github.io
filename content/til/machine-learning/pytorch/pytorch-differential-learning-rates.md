---
title: "Differential Learning Rates in PyTorch"
summary: "Using different learning rates in different layers of our artificial neural network."
date: 2021-11-01
authors:
  - L Ma
categories:
  - machine-learning
tags:
  - Python
  - PyTorch
  - "Learning Rate"
references:
  - name: "Pointer I. Programming PyTorch for deep learning: Creating and deploying deep learning applications. Sebastopol, CA: O’Reilly Media; 2019."
    link: "https://www.oreilly.com/library/view/programming-pytorch-for/9781492045342/"
    key: "Pointer2019"
  - name: "torch.optim — PyTorch 1.10.0 documentation. [cited 30 Nov 2021]. Available: https://pytorch.org/docs/stable/optim.html"
    link: "https://pytorch.org/docs/stable/optim.html"
    key: "PyTorchDocs"
links:
  - "cards/machine-learning/practice/learning-rate.md"
---

PyTorch offers optimizer configuration for different learning rates in different layers.

{{< message title="Why Do We Do This" class="info" >}}

In some models, we need to treat the layers differently. For example, in transfer learning, we could fine tuning the pretrained layers using a tiny learning rate.

{{< /message >}}

In the documentation of pytorch, we find that we can set optimizer parameters on a per-layer basis [^PyTorchDocs]. The example from the documentation is

```python
optim.SGD([
    {'params': model.base.parameters()},
    {'params': model.classifier.parameters(), 'lr': 1e-3}
], lr=1e-2, momentum=0.9)
```




[^PyTorchDocs]: {{< cite key="PyTorchDocs" >}}
[^Pointer2019]: {{< cite key="Pointer2019" >}}