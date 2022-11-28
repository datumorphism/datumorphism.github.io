---
title: "Graph Structure Learning in GNN"
description: "We can learn a graph structure without prior knowledge"
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
weight: 5
---


We extract the definitions in Wu et al., 2020[^Wu2020]. Given node embeddings $\mathbf E_i$[^Wu2020],

{{< m >}}
\begin{align}
\mathbf M_i &= \tanh(\alpha \mathbf E_i \Theta_i) \\
\mathbf A &= \operatorname{ReLU}(\tanh(\alpha (\mathbf M_1 \mathbf M_2^T - \mathbf M_2\mathbf M_1^T))),
\end{align}
{{< /m >}}

The author also proposed sparse requirement and only take the top-$k$ largest elements in $A$.


[^Wu2020]: {{< cite key="Wu2020" >}}
