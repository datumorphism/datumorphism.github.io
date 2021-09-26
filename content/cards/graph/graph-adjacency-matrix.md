---
title: "Graph Adjacency Matrix"
authors:
  - "Lei Ma"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

A graph $\mathcal G$ can be represented with an adjacency matrix $\mathbf A$.


## Multiplication of Adjacency Matrices

**Multiplication of adjacency matrices tells us about the path between nodes.**

$A[u,v]$ is the length-1 path between node $u$ and $v$. If $A[u,v]=0$, there is no path. If $A[u,v]=1$, we have a length-1 path.

For $A^2[u,v]$, we have

{{< m >}}
A^2_{uv} = \sum_k A_{uk}A_{kv}.
{{< /m >}}

This is the length-2 path. If node $u$ or node $v$ has no neighbors, $A^2_{uv}=0$. If there is an edge $(u, \tilde u)$ and $(\tilde u, v)$, we get one path, and $A_{u\tilde u}A_{\tilde uv}=1$.

When we sum over all the possible values of index $k$, i.e., $\sum_k A_{uk}A_{kv}$, we get the total number of length-2 path between $u$ and $v$.

This idea is extrapolated to the $i$th power of the adjacency matrix.
