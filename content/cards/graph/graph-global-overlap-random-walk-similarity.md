---
title: "Graph Global Overlap Measure: Random Walk Similarity"
date: "2021-09-26"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Basics"
  - "Clustering"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "cards/graph/graph-adjacency-matrix.md"
  - "cards/graph/graph-eigenvector-centrality.md"
---

## Random Walk

Construct a stochastic transfer matrix $P$ by normalizing the adjacency matrix $\mathbf A$ using the node degrees of the target nodes,

{{< m >}}
\mathbf P = \mathbf A \mathbf D^{-1},
{{< /m >}}

where $\mathbf A$ is the {{< c "cards/graph/graph-adjacency-matrix.md" "adjacency matrix" >}} and $\mathbf D$ is a diagonalized matrix with the diagonal elements being the degrees.

Given a random walk associated with $\mathbf P$ that starts from node $u$, we find the probability that visits each node $v$, $\mathbf q_u[v]$[^Hamilton2020],

{{< m >}}
\mathbf q_u = c \mathbf P \mathbf q_u + (1-c) \mathbf e_u,
{{< /m >}}

where $\mathbf e_u$ is the onehot encoding of node $u$ and $c$ is a probability that the walk restarts at $u$.

- If $c=0$, we have a constant solution.
- If $c=1$, we have $\mathbf q_u = \mathbf P \mathbf q_u$, which is the {{< c "cards/graph/graph-eigenvector-centrality.md" >}}.

The solution is[^Hamilton2020],

{{< m >}}
\mathbf q_u = (1-c) ( \mathbf I - c \mathbf P )^{-1} \mathbf e_u.
{{< /m >}}


## Random Walk Similarity

The random walk similarity is defined using $\mathbf q_u$,

{{< m >}}
\mathbf S_{\text{RW}}[u, v] = \mathbf q_u[v] + \mathbf q_v[u],
{{< /m >}}

which is symmetry under permutation of $u$ and $v$.

[^Hamilton2020]: {{< cite key="Hamilton2020" >}}