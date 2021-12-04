---
title: "Graph Adjacency Matrix"
authors:
  - "Lei Ma"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
references:
  - link: "https://en.wikipedia.org/wiki/Adjacency_matrix#Undirected_graphs"
    name: "Contributors to Wikimedia projects. Adjacency matrix. In: Wikipedia [Internet]. 4 Oct 2021 [cited 4 Dec 2021]. Available: https://en.wikipedia.org/wiki/Adjacency_matrix#Undirected_graphs"
    key: "wiki_adjacency_matrix"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

A graph $\mathcal G$ can be represented with an adjacency matrix $\mathbf A$. There are some nice and clear examples on wikipedia[^wiki_adjacency_matrix], for example,

{{< m >}}
\begin{pmatrix}
2 & 1 & 0 & 0 & 1 & 0\\
1 & 0 & 1 & 0 & 1 & 0\\
0 & 1 & 0 & 1 & 0 & 0\\
0 & 0 & 1 & 0 & 1 & 1\\
1 & 1 & 0 & 1 & 0 & 0\\
0 & 0 & 0 & 1 & 0 & 0
\end{pmatrix}
{{< /m >}}

for the graph

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/2/28/6n-graph2.svg" caption="Public Domain, [Link](https://commons.wikimedia.org/w/index.php?curid=1041193)" >}}


{{< message title="Diagonal Elements" class="warning">}}

The diagonal elements are 0 for graphs without loops.

{{< /message >}}

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


[^wiki_adjacency_matrix]: {{< cite key="wiki_adjacency_matrix" >}}