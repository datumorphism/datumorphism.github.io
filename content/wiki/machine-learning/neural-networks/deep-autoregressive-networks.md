---
title: "Deep Autoregressive Network"
description: "DARN"
date: 2021-02-15
categories:
  - "Machine Learning"
tags:
  - "Machine Learning"
  - "Autoregressive Network"
references:
  - name: "Gregor, K., Danihelka, I., Mnih, A., Blundell, C., & Wierstra, D. (2013). Deep AutoRegressive Networks. 31st International Conference on Machine Learning, ICML 2014, 4, 2991–3000."
    link: "http://arxiv.org/abs/1310.8499"
links:
  - wiki/model-selection/mdl-and-neural-networks.md
weight: 4
---

![](../assets/deep-autoregressive-networks/deep-autoregressive-network-structure.png)


There are two levels of autoregressiveness in the DARN network:
- Inlayer autoregressive connections of the nodes,
- Intralayer autoregressive connections of nodes.

![](../assets/deep-autoregressive-networks/deep-autoregressive-network-autoregressiveness.jpg)

The network is trained on MDL loss.

![](../assets/deep-autoregressive-networks/deep-autoregressive-network-mdl.png)

