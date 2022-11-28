---
title: "Mix-hop Propagation in GNN"
description: "Mix-hop is a strategy to avoid oversmoothing in GNN"
date: 2022-11-28
categories:
  - "Graph Neural Network"
tags:
  - "GNN"
  - "Forecasting"
  - "Graph"
references:
  - name: "Wu Z, Pan S, Long G, Jiang J, Chang X, Zhang C. Connecting the Dots: Multivariate Time Series Forecasting with Graph Neural Networks. arXiv [cs.LG]. 2020. Available: http://arxiv.org/abs/2005.11650"
    link: "http://arxiv.org/abs/2005.11650"
    key: "Wu2020"
weight: 4
---

The mix-hop propagation layer has two steps[^Wu2020]:
1. information propagation step:
   {{< m >}}
   \mathbf H^{(k)} = \beta \mathbf H_{in} + (1-\beta)\mathbf L \mathbf H^{(k-1)},
   {{< /m >}}
   where
   $\mathbf L= (1+ \operatorname{A}) (\mathbf A + \mathbf I)$. This convolution step tries to disentangle the correlation between the nodes.
2. information selection step:
   {{< m >}}
   \mathbf H_{out} = \sum_k \mathbf H^{(k)} \mathbf W^{(k)}.
   {{< /m >}}

See Fig 4 in the paper[^Wu2020].

[^Wu2020]: {{< cite key="Wu2020" >}}
