---
title: "Over-Smoothing in Graph Neural Networks"
description: ""
date: 2022-08-21T13:45:33+02:00
authors:
  - "Lei Ma"
categories:
  - "Graph"
tags:
  - "graph"
  - "graph neural networks"
  - "GNN"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://link.springer.com/book/10.1007/978-3-031-01588-5"
    key: "Hamilton2020"
garden:
  - "seedling"
---


Over-smoothing is the problem that the representations on each node of the graph neural networks becomes way too similar to each other.[^Hamilton2020] In Chapter 7 of Hamilton2020, the author interprets this phenomenon using the lower pass filter theory in signal processing, i.e., multiplying a signal by $\mathbf A^n$ is similar to a low-pass filter when $n$ is large, with $\mathfb A$ being the adjacency matrix.


[^Hamilton2020]: {{< cite key="Hamilton2020" >}}