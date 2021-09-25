---
title: "Eigenvector Centrality of a Graph"
date: "2021-09-25"
categories:
  - 'Graph'
tags:
  - "Graph"
  - "Statistics"
references:
  - name: "Hamilton WL. Graph Representation Learning. Morgan & Claypool Publishers; 2020. pp. 1–159. doi:10.2200/S01045ED1V01Y202009AIM046"
    link: "https://www.morganclaypool.com/doi/10.2200/S01045ED1V01Y202009AIM046"
    key: "Hamilton2020"
links:
  - "wiki/graph/basics/what-is-graph.md"
---

Given a graph with adjacency matrix $\mathbf A$, the eigenvector centrality is

{{< m >}}
\mathbf e_u = \frac{1}{\lambda} \sum_{v\in\mathcal V} \mathbf A[u,v] \mathbf e_v, \qquad \forall u \in \mathcal V.
{{< /m >}}

{{< message title="Why is it called Eigenvector Centrality" >}}

The definition is equivalent to

$$
\lambda \mathbf e = \mathbf A\mathbf e.
$$

{{< /message >}}

## Power Iteration

The solution to $\mathbf e$ is the eigenvector that corresponds to the largest eigenvalue $\lambda_1$. Power iteration method can help us get this eigenvector, i.e., the $^{(t+1)}$ iteration is related to the previous iteration $^{(t)}$, through the following relation,

{{< m >}}
\mathbf e^{(t+1)} = \mathbf A \mathbf e^{(t)}.
{{< /m >}}

If we set $\mathbf e^{(0)} \to (1, 1, \cdots , 1)$.


## Indications of the Power Iteration Method

The power iteration method hints that the eigenvector centrality is related to walking through the graph.

For step 0, we have

{{< m >}}
e^{(1)}_i = A_{ij} e^{(0)}_j,
{{< /m >}}

$e^{(0)} _ j$ is the probability of visiting node $j$, which is 1. $A_{ij}$ is the transfer probability from node $j$ to $i$. After this iteration, we get the number of visits on node $i$.

Repeat this, we have a vector that shows the number of visits on node $i$ after $t+1$ steps.

That being said, the eigenvector centrality is proportional to the likelihood of visiting the nodes after infinite steps of random walks on the graph.

