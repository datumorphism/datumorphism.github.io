---
title: "Uni-Polar Sigmoid"
description: "Uni-polar sigmoid function and its properties"
date: "2018-11-19"
authors:
  - "L Ma"
categories:
  - "Neural Networks"
tags:
  - "Artificial Neuron"
  - "Neural Network"
  - "Basics"
  - "Activation Function"
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
---


A uni-Polar sigmoid function is

{{< m >}}
\sigma(x) = \frac{1}{1+e^{-x}}.
{{< /m >}}

## Visualization

{{< figure src="../assets/uni-polar-sigmoid/uni-polar-sigmoid.png" title="Uni-polar Sigmoid function" >}}


## Tricks

A very useful trick:
{{< m >}}
1 - \sigma(x) = \sigma(-x).
{{< /m >}}
