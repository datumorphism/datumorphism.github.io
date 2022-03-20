---
title: "Graph Edge Sampling"
date: "2022-03-20"
categories:
  - 'Graph'
tags:
  - "Graph"
references:
  - link: "http://arxiv.org/abs/1503.03578"
    name: "Tang J, Qu M, Wang M, Zhang M, Yan J, Mei Q. LINE: Large-scale Information Network Embedding. arXiv [cs.LG]. 2015. Available: http://arxiv.org/abs/1503.03578"
    key: "Tang2015"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

Edge sampling is a technique to deal with weighted edges in large {{< c "wiki/graph/basics/what-is-graph.md" "graph" >}}. For weighted graph, one treatment is to create multiple edges between the same nodes but removing the weights. But this will require a lot of memory.

Edge sampling as a method samples edges with a probability proportional to the weights. By sampling and creating sampled binary edges, we create new unweighted graphs that represents the original graph.