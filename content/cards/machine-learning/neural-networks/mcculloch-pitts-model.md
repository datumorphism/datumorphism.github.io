---
title: "McCulloch-Pitts Model"
description: "Artificial neuron that separates the state space"
date: "2021-02-25"
authors:
  - "LM"
categories:
  - "Machine Learning"
tags:
  - "Artificial Neuron"
  - "Neural Network"
  - "Basics"
references:
  - name: "Vladimir N. Vapnik. 2000. The Nature of Statistical Learning Theory."
    link: "https://doi.org/10.1007/978-1-4757-3264-1"
weight:
links:
  - "wiki/machine-learning/neural-networks/artificial-neural-networks.md"
---

The McCulloch-Pitts model maps the input $\\{x_1, x_2,\cdots, x_i \cdots, x_N \\}$ into a scalar $y\in\\{1,-1\\}$,

{{< m >}}
y = \operatorname{sign}( w\cdot x - b).
{{< /m >}}

Since $w\cdot x - b = 0$ is a hyperplane, the McCulloch-Pitts model separates the state space using this hyperplane. The shift $b$ determines the interception, and $w$ decides the slope.
